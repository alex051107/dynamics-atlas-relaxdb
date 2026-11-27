"""Five-slot attribution scoring, data-driven cross-paper comparison and the RelaxDB label recall benchmark.

Slots (Fable 2026-11-23): (1) quantity + state role, (2) value + unit dimension, (3) construct / species relation,
(4) ligand, stoichiometry and solvent, (5) temperature in kelvin; field strength is a sixth slot only for
field-dependent quantities (R1, R2, R1rho, Rex, NOE).

Inputs, all read-only and limited to the 131 open entries listed in the expert-review SQLite:
  * SQLite `measurements_clean` joined to `samples` (and `observations` for qualitative exchange regions),
  * F14 CPMG sprint JSONs (batch1, batch2),
  * curated RelaxDB labels (`hf_relaxdb_open131_curated_labels.json`),
  * `inputs/<entry>.json` for open entries only, opened by exact path (the folder is never listed).

Label-source papers are derived from data, never from a hand table: the F14 per-row `is_relaxdb_label_source`
flag, `samples.same_as_deposit == 'yes'` (the BMRB deposit's own sample), DOIs inside the curated
`curation_source` / `doi_missing` fields, and DOIs in `inputs/<entry>.json` source notes.
`config/relaxdb_source_dois.json` is not read because it also carries sealed entries.

Outcome statuses: AGREE_INDEPENDENT, CONDITIONAL_DIFF, LABEL_SOURCE_ONLY, REVIEW_SECONDARY, NOT_COMPARABLE_ABSTAIN.
Values that differ while every recorded slot matches are CONDITIONAL_DIFF with VALUES_DIFFER_ALL_SLOTS_MATCHED:
the cause must be an unrecorded condition (pH, buffer, fit model), which the reason codes name when known.
"""
from __future__ import annotations

import csv
import json
import math
import os
import re
import sqlite3
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

from .schema import (
    FIELD_DEPENDENT_QUANTITIES,
    POPULATION_QUANTITIES,
    QUANTITY_DIMENSIONS,
    SEALED_ENTRIES,
    WORK,
    ComparisonOutcome,
    canonical_quantity,
    is_room_temperature,
    normalize_minus,
    normalize_unit,
    parse_field_mhz,
    parse_temperature_kelvin,
    parse_temperatures_kelvin,
    quantity_role,
    unit_dimension,
    unit_scale_factor,
)

def _default_db_path() -> Path:
    if os.environ.get("ATLAS_DB_PATH"):
        return Path(os.environ["ATLAS_DB_PATH"])
    repo_rel = Path(__file__).resolve().parents[1] / "data/expert_review_20261119/RelaxDB_expert_review_DRAFT.sqlite"
    if repo_rel.is_file():
        return repo_rel
    return Path.home() / "dynamics-atlas-relaxdb/data/expert_review_20261119/RelaxDB_expert_review_DRAFT.sqlite"


DB_PATH = _default_db_path()
F14_BATCHES = (
    WORK / "outputs/cpmg_sprint_20261122/extractions/batch1_kras_rnase_htpdz.json",
    WORK / "outputs/cpmg_sprint_20261122/extractions/batch2_chey_vhr_blvrb_argkin.json",
)
CURATED_LABELS = Path(os.environ.get("ATLAS_CURATED_LABELS", str(WORK / "outputs/relaxdb_label_vs_qualitative_20261122/hf_relaxdb_open131_curated_labels.json")))
INPUTS_DIR = WORK / "inputs"
OUT_DIR = Path(os.environ.get("ATLAS_OUT_DIR", str(WORK / "outputs/atlas_pipeline_run_20261123")))

VALUE_REL_TOL = 0.25  # cross-paper agreement: different labs, fits and error models
ABS_FLOOR = {"fraction": 0.01, "dimensionless": 0.03, "chemical_shift": 0.05, "rate": 0.5, "time": 0.0, "energy": 0.5}
TEMP_TOL_K = 2.0
PER_RESIDUE_AGREE_FRACTION = 0.6
NON_COMPARABLE_QUANTITY_RE = re.compile(r"^other|^distance$|unknown", re.I)
# "SI Table 9 cited" names the paper's own supplement; only wording that attributes the value to other work counts.
SECONDARY_RE = re.compile(r"\b(review article|reviewed in|cited from|citing (?:ref|prior|previous|earlier)|"
                          r"previously (?:reported|determined|measured|published)|taken from|reported in ref|"
                          r"from ref(?:erence)?s?\b|ref\.\s*\d)", re.I)
EXCHANGE_EVIDENCE_QUANTITIES = {"rex", "delta_omega"}
PER_RESIDUE_KINETIC_EVIDENCE = {"kex", "pb"}

# Per-residue label alphabet as used by the team's 2026-11-22 audit (run_label_vs_qualitative_audit.py). The
# public dataset card was not available offline; `STRICT_POSITIVE` (^ and Y) is reported beside it as a check.
LABEL_CLASS = {
    "^": "EXCHANGE_POSITIVE", "b": "EXCHANGE_POSITIVE", "X": "EXCHANGE_POSITIVE", "Y": "EXCHANGE_POSITIVE",
    "v": "FAST_MOTION_ONLY", "A": "NO_EXCHANGE_DETECTED", ".": "MISSING_PEAK",
    "x": "NO_DATA_OR_PROLINE", "t": "NO_DATA_OR_PROLINE", "N": "NO_DATA_OR_PROLINE", "p": "NO_DATA_OR_PROLINE",
    "P": "NO_DATA_OR_PROLINE",
}
STRICT_POSITIVE = {"^", "Y"}
AA3 = {"ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q", "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I",
       "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V"}
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s,;\"'<>)\]]+")


def _norm_doi(d: str | None) -> str:
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", (d or "").strip(), flags=re.I).rstrip(".").lower()


def _dois_in(text: Any) -> set[str]:
    return {_norm_doi(m.group(0)) for m in DOI_RE.finditer(str(text or ""))}


# ============================================================================ slot logic (ported + upgraded)
# Source: outputs/cpmg_sprint_20261122/score_attribution_5tuple.py (2026-11-23). Changes: tri-state slots
# (matched / incompatible / unknown) instead of booleans, schema-based units with an optional pint fallback,
# kelvin parsing that ignores "± x" uncertainties, and species-relation awareness in the construct slot.

MUTANT_TOKEN_RE = re.compile(r"\b([A-Z]\d{1,4}[A-Z])\b|\b(delta\s*\d+|Δ\s*\d+|truncat\w*|chimer\w*)\b", re.I)
STOICH_RE = re.compile(r"\b(\d+\s*:\s*\d+)\b")
SOLVENT_PCT_RE = re.compile(r"(\d+(?:\.\d+)?)\s*%\s*(h2o|d2o)", re.I)
APO_RE = re.compile(r"\b(apo|unliganded|ligand[- ]free|free enzyme|substrate[- ]free|unbound|resting)\b", re.I)
HOLO_RE = re.compile(r"\b(bound|holo|complex|inhibitor|substrate|peptide|gdp|gtp|gppnhp|gmp-?pnp|atp|adp|amp-?pnp|ap5a|nadp\+?|nadph|"
                     r"tungstate|bef3|ca2\+|zn2\+|mg2\+|turnover|phospho\w*|ligand)\b", re.I)
_UNKNOWN_LIGAND_RE = re.compile(
    r"^(?:not\s+(?:stated|specified|reported|printed|given|mentioned|restated)\b.*|"
    r"no\s+ligand\s+(?:stated|specified|reported|mentioned)\b.*|"
    r"unknown\b.*|n/?a\b.*|none\s+stated\b.*)$",
    re.I,
)
_NEGATED_ION_RE = re.compile(
    r"(?<![a-z0-9])(mg2?\+|ca2?\+|zn2?\+|mn2?\+|mg|ca|zn|mn|magnesium|calcium|zinc|manganese)[- ]free\b"
    r"|\b(?:no|without)\s+(mg2?\+|ca2?\+|zn2?\+|mn2?\+|magnesium|calcium|zinc|manganese)(?![a-z0-9])",
    re.I,
)
_NEGATED_HOLO_RE = re.compile(
    r"\b(?:ligand|substrate|inhibitor|peptide|nucleotide|cofactor|metal|ion)[- ]free\b",
    re.I,
)
_FUSED_MG_NUC_RE = re.compile(r"(?<![a-z0-9])mg(?=(?:atp|adp|amp-?pnp|amppcp|gtp|gdp|gppnhp|gmp-?pnp|ap5a)(?![a-z0-9]))", re.I)
_TOKEN_BOUND_SUFFIX_RE = re.compile(r"-(?:bound|loaded|saturated|complexed|liganded)$")
LIGAND_STOP = {"apo", "unliganded", "free", "ligand", "bound", "complex", "with", "in", "saturating", "excess", "state", "buffer", "ph",
               "mm", "um", "nm", "nacl", "tris", "mops", "pbs", "hepes", "h2o", "d2o", "and", "the", "of", "to", "at", "no",
               "not", "stated", "none", "enzyme", "resting", "form", "protein", "wt", "wild", "type", "sample", "saturated",
               "loaded", "presence", "absence", "alone", "equivalents", "equiv", "molar", "ratio", "titration", "complexed"}
# Named small-molecule ligands and metal ions are compared as sets: GDP-bound and GTP-bound KRAS share "Mg2+" but are
# different states, which the older shared-token rule accepted as the same ligand state.
LIGAND_VOCAB_RE = re.compile(
    r"(?<![a-z0-9])(gppnhp|gmp-?pnp|gtp[γg]s|gtp|gdp|gmp|amp-?pnp|amppcp|ap5a|atp|adp|amp|utp|ctp|camp|cgmp|nadph|nadp\+?|nadh|"
    r"nad\+?|fad|fmn|plp|coa|heme|methotrexate|mtx|folate|dhf|thf|tungstate|vanadate|bef3-?|alf4-?|no3-?|nitrate|"
    r"(?<!d-)l-arginine|(?<![a-z0-9-])arginine|"
    r"mg(?:2\+|\+\+|cl2)?|ca(?:2\+|\+\+|cl2)?|zn(?:2\+|cl2)?|mn(?:2\+|cl2)?|cd2\+|ni2\+|co2\+|cu2\+|fe[23]\+)(?![a-z0-9])")
ION_CANON = {
    "mg": "mg2+", "mg2+": "mg2+", "magnesium": "mg2+",
    "ca": "ca2+", "ca2+": "ca2+", "calcium": "ca2+",
    "zn": "zn2+", "zn2+": "zn2+", "zinc": "zn2+",
    "mn": "mn2+", "mn2+": "mn2+", "manganese": "mn2+",
}
LIGAND_CANON = {
    "gmppnp": "gppnhp",
    "no3": "nitrate",
    "larginine": "arginine",
    "nad": "nad+",
    "nadp": "nadp+",
}


def construct_features(text: str | None) -> dict[str, Any]:
    s = normalize_minus(str(text or "")).strip()
    if not s or s.lower() in {"not stated", "unknown", "n/a", "na", "none"}:
        return {"known": False}
    muts = {m.group(0).upper().replace(" ", "") for m in MUTANT_TOKEN_RE.finditer(s)} - {"H2O", "D2O"}
    is_wt = bool(re.search(r"\b(wt|wild[- ]?type)\b", s, re.I)) and not muts
    return {"known": True, "muts": muts, "wt": is_wt or not muts, "raw": re.sub(r"\s+", " ", s.lower())}


def construct_slot(a: str | None, b: str | None, rel_a: str = "", rel_b: str = "") -> tuple[str, str]:
    ra, rb = (rel_a or "").strip(), (rel_b or "").strip()
    if ra and rb and ra != rb:
        return "incompatible", f"SPECIES_RELATION_DIFFERS:{ra}/{rb}"
    fa, fb = construct_features(a), construct_features(b)
    if not fa["known"] or not fb["known"]:
        return "unknown", "MISSING_CONSTRUCT"
    if fa["muts"] or fb["muts"]:
        if fa["muts"] != fb["muts"]:
            return "incompatible", f"CONSTRUCT_DIFFERS:{'+'.join(sorted(fa['muts'])) or 'WT'}/{'+'.join(sorted(fb['muts'])) or 'WT'}"
        return "matched", "SAME_MUTATIONS"
    if ra == "homolog" and rb == "homolog" and fa["raw"] != fb["raw"]:
        return "unknown", "HOMOLOGS_NOT_PROVEN_IDENTICAL"
    return "matched", "BOTH_WILD_TYPE"


def ligand_features(text: str | None) -> dict[str, Any]:
    s = normalize_minus(str(text or "")).strip()
    sl = s.lower()
    if not s or _UNKNOWN_LIGAND_RE.match(sl):
        return {"known": False}
    stoich = {re.sub(r"\s+", "", m) for m in STOICH_RE.findall(sl)}
    solvents = {solv.lower(): float(pct) for pct, solv in SOLVENT_PCT_RE.findall(sl)}
    absent_ions: set[str] = set()
    for m in _NEGATED_ION_RE.finditer(sl):
        raw_ion = (m.group(1) or m.group(2) or "").lower().rstrip("+")
        raw_ion = re.sub(r"2$", "", raw_ion)
        absent_ions.add(ION_CANON.get(raw_ion, raw_ion))
    sl_no_neg = _NEGATED_HOLO_RE.sub(" ", _NEGATED_ION_RE.sub(" ", sl))
    cleaned = re.sub(r"\d+(?:\.\d+)?\s*%\s*(?:h2o|d2o)", " ", sl_no_neg)
    cleaned = re.sub(r"\b\d+\s*:\s*\d+\b", " ", cleaned)
    cleaned = _FUSED_MG_NUC_RE.sub("mg2+ ", cleaned)
    named = set()
    for m in LIGAND_VOCAB_RE.finditer(cleaned):
        tok = re.sub(r"(?:\+\+|cl2)$", "", m.group(1)).replace("-", "")
        tok = ION_CANON.get(tok, LIGAND_CANON.get(tok, tok))
        named.add(tok)
    cleaned = LIGAND_VOCAB_RE.sub(" ", cleaned)
    raw_tokens = re.findall(r"[a-z][a-z0-9+\-]{1,}", cleaned)
    tokens = set()
    for t in raw_tokens:
        t = _TOKEN_BOUND_SUFFIX_RE.sub("", t)
        if len(t) > 1 and t not in LIGAND_STOP:
            tokens.add(t)
    ions = {t for t in named if t.endswith("+") and t[:2] in {"mg", "ca", "zn", "mn", "cd", "ni", "co", "cu", "fe"}}
    ligands = named - ions
    is_apo = bool(APO_RE.search(sl))
    has_holo = bool(HOLO_RE.search(sl_no_neg) or ligands) and not re.search(r"\b(?:no|without)\s+(?:ligand|nucleotide|substrate)", sl)
    if is_apo and not has_holo:
        tokens, ligands = set(), set()  # an apo enzyme keeps its buffer ions (e.g. apo with MgCl2)
    return {"known": True, "apo": is_apo and not has_holo, "holo": has_holo or (bool(tokens) and not is_apo), "stoich": stoich,
            "solvents": solvents, "tokens": tokens, "ions": ions, "absent_ions": absent_ions, "ligands": ligands}


def ligand_slot(a: str | None, b: str | None) -> tuple[str, str]:
    fa, fb = ligand_features(a), ligand_features(b)
    if not fa["known"] or not fb["known"]:
        return "unknown", "MISSING_LIGAND_STATE"
    if fa["apo"] != fb["apo"] and (fa["apo"] or fb["apo"]):
        return "incompatible", "LIGAND_APO_VS_HOLO"
    for solv in ("h2o", "d2o"):
        if solv in fa["solvents"] and solv in fb["solvents"] and abs(fa["solvents"][solv] - fb["solvents"][solv]) > 5.0:
            return "incompatible", f"SOLVENT_{solv.upper()}_PCT_DIFFERS:{fa['solvents'][solv]:g}/{fb['solvents'][solv]:g}"
    if fa["solvents"] and fb["solvents"] and set(fa["solvents"]) != set(fb["solvents"]):
        ha = fa["solvents"].get("h2o", 100.0 - fa["solvents"].get("d2o", 0.0))
        hb = fb["solvents"].get("h2o", 100.0 - fb["solvents"].get("d2o", 0.0))
        if abs(ha - hb) > 5.0:
            return "incompatible", f"SOLVENT_ISOTOPE_DIFFERS:H2O_{ha:g}/{hb:g}"
    if (fa["stoich"] or fb["stoich"]) and fa["stoich"] != fb["stoich"]:
        return "incompatible", f"STOICHIOMETRY_DIFFERS:{'/'.join(sorted(fa['stoich'])) or '-'}|{'/'.join(sorted(fb['stoich'])) or '-'}"
    if fa["ligands"] and fb["ligands"] and fa["ligands"] != fb["ligands"]:
        return "incompatible", f"LIGAND_IDENTITY_DIFFERS:{'+'.join(sorted(fa['ligands']))}/{'+'.join(sorted(fb['ligands']))}"
    neg_conflict = (fa["ions"] & fb["absent_ions"]) | (fb["ions"] & fa["absent_ions"])
    if neg_conflict:
        return "incompatible", f"METAL_ION_DIFFERS:{'+'.join(sorted(neg_conflict))}-free/{'+'.join(sorted(neg_conflict))}"
    if fa["ions"] and fb["ions"] and fa["ions"] != fb["ions"]:
        return "incompatible", f"METAL_ION_DIFFERS:{'+'.join(sorted(fa['ions']))}/{'+'.join(sorted(fb['ions']))}"
    if fa["holo"] and fb["holo"] and fa["tokens"] and fb["tokens"] and not (fa["tokens"] & fb["tokens"]):
        return "incompatible", "LIGAND_IDENTITY_DIFFERS:free_text"
    if (fa["ligands"] | fa["ions"]) != (fb["ligands"] | fb["ions"]):
        one = sorted((fa["ligands"] | fa["ions"]) ^ (fb["ligands"] | fb["ions"]))
        return "unknown", f"LIGAND_COMPONENT_STATED_IN_ONE_PAPER_ONLY:{'+'.join(one)}"
    return "matched", "LIGAND_STATE_MATCHED"


def _normalize_temp_side(
    val: float | int | str | Iterable[float] | None,
    raw: str | None = None,
) -> tuple[list[float], bool]:
    if isinstance(val, str):
        temps = parse_temperatures_kelvin(val, "C")
        return temps, (not temps) and is_room_temperature(val)
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        return [float(val)], False
    if val is not None:
        temps = sorted(float(x) for x in val)
        return temps, (not temps) and is_room_temperature(raw)
    if raw:
        temps = parse_temperatures_kelvin(raw, "C")
        return temps, (not temps) and is_room_temperature(raw)
    return [], False


def temperature_slot(
    ta: float | int | str | Iterable[float] | None,
    tb: float | int | str | Iterable[float] | None,
    tol: float = TEMP_TOL_K,
    *,
    raw_a: str | None = None,
    raw_b: str | None = None,
    allow_multi_contains: bool = True,
) -> tuple[str, str]:
    temps_a, rt_a = _normalize_temp_side(ta, raw_a)
    temps_b, rt_b = _normalize_temp_side(tb, raw_b)
    if not temps_a and not temps_b and rt_a and rt_b:
        return "matched", "ROOM_TEMP_MATCH"
    if (rt_a and temps_b) or (rt_b and temps_a):
        return "unknown", "ROOM_TEMP_VS_NUMERIC_TEMP"
    if not temps_a or not temps_b:
        return "unknown", "MISSING_TEMPERATURE"
    if len(temps_a) == 1 and len(temps_b) == 1:
        if abs(temps_a[0] - temps_b[0]) > tol:
            return "incompatible", f"TEMPERATURE_DIFFERS:{temps_a[0]:.1f}K/{temps_b[0]:.1f}K"
        return "matched", "TEMPERATURE_MATCHED"
    fmt_a = "/".join(f"{x:.1f}K" for x in temps_a)
    fmt_b = "/".join(f"{x:.1f}K" for x in temps_b)
    if len(temps_a) == 1 or len(temps_b) == 1:
        single, multi = (temps_a[0], temps_b) if len(temps_a) == 1 else (temps_b[0], temps_a)
        if any(abs(single - m) <= tol for m in multi):
            if allow_multi_contains:
                return "matched", "MULTI_TEMP_CONTAINS_MATCH"
            return "unknown", "MULTI_TEMP_AMBIGUOUS"
        return "incompatible", f"TEMPERATURE_DIFFERS:{fmt_a}|{fmt_b}"
    if all(abs(x - y) > tol for x in temps_a for y in temps_b):
        return "incompatible", f"TEMPERATURE_DIFFERS:{fmt_a}|{fmt_b}"
    if allow_multi_contains and len(temps_a) == len(temps_b) and all(abs(x - y) <= tol for x, y in zip(temps_a, temps_b)):
        return "matched", "MULTI_TEMP_MATCH"
    return "unknown", "MULTI_TEMP_AMBIGUOUS"


def field_slot(fa: tuple[float, ...], fb: tuple[float, ...]) -> tuple[str, str]:
    if not fa or not fb:
        return "unknown", "MISSING_FIELD_STRENGTH"
    if set(fa) & set(fb) or (len(fa) == 1 and len(fb) == 1 and abs(fa[0] - fb[0]) <= 10):
        return "matched", "FIELD_MATCHED"
    return "incompatible", f"FIELD_DIFFERS:{'/'.join(f'{x:g}' for x in fa)}|{'/'.join(f'{x:g}' for x in fb)}"


def unit_dim_for_role(role: str, dim: str) -> str:
    """NOE, S2 and pB are printed without a unit; a blank unit is only an error for rates, times and shifts."""
    allowed = QUANTITY_DIMENSIONS.get(role, frozenset())
    if dim in {"missing", "dimensionless"} and allowed & {"dimensionless", "fraction"}:
        return "fraction" if role in POPULATION_QUANTITIES else "dimensionless"
    return dim


def to_base(value: float | None, unit: str | None) -> tuple[float | None, str]:
    """Value in the base unit of its dimension (rate s^-1, time s, fraction, ppm, kJ/mol) and that dimension."""
    if not str(unit or "").strip():
        return value, "missing"
    scale = unit_scale_factor(unit)
    if scale is not None:
        dim, factor = scale
        return (value * factor if value is not None else None), dim
    return value, unit_dimension(unit)


def values_agree(a: float, b: float, dim: str, rel_tol: float = VALUE_REL_TOL) -> bool:
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), ABS_FLOOR.get(dim, 0.0))


def score_record(pred: dict[str, Any], gold: dict[str, Any], temp_tol_k: float = 1.0, rel_tol: float = 0.02) -> dict[str, Any]:
    """Extraction benchmark: one predicted measurement against a gold one on all five slots (strict tolerances)."""
    reasons: list[str] = []
    pq = quantity_role(pred.get("quantity"), f"{pred.get('quote', '')} {pred.get('residues_raw', '')}")
    gq = quantity_role(gold.get("quantity"), f"{gold.get('quote', '')} {gold.get('residues_raw', '')}")
    quantity_ok = bool(pq) and pq == gq
    if not quantity_ok:
        reasons.append(f"QUANTITY_ROLE_MISMATCH:{pq}/{gq}")
    pv, pdim = to_base(_num(pred.get("value")), pred.get("unit"))
    gv, gdim = to_base(_num(gold.get("value")), gold.get("unit"))
    pdim, gdim = unit_dim_for_role(pq, pdim), unit_dim_for_role(gq, gdim)
    if pv is None or gv is None:
        value_ok = False
        reasons.append("VALUE_UNPARSEABLE")
    elif pdim != gdim:
        value_ok = False
        reasons.append(f"UNIT_DIMENSION_MISMATCH:{pdim}/{gdim}")
    elif (pv < 0) != (gv < 0) and max(abs(pv), abs(gv)) > 1e-9:
        value_ok = False
        reasons.append("SIGN_MISMATCH")
    else:
        value_ok = math.isclose(pv, gv, rel_tol=rel_tol, abs_tol=1e-9)
        if not value_ok:
            reasons.append(f"VALUE_MISMATCH:{pv:g}/{gv:g}")
    c_state, c_reason = construct_slot(pred.get("sample_construct"), gold.get("sample_construct"))
    l_state, l_reason = ligand_slot(pred.get("ligand_state"), gold.get("ligand_state"))
    p_temp_raw, g_temp_raw = pred.get("temperature"), gold.get("temperature")
    t_state, t_reason = temperature_slot(
        parse_temperatures_kelvin(p_temp_raw, "C"),
        parse_temperatures_kelvin(g_temp_raw, "C"),
        temp_tol_k,
        raw_a=str(p_temp_raw or ""),
        raw_b=str(g_temp_raw or ""),
        allow_multi_contains=True,
    )
    for state, reason in ((c_state, c_reason), (l_state, l_reason), (t_state, t_reason)):
        if state != "matched":
            reasons.append(reason)
    naive = (str(pred.get("quantity", "")).strip().lower() == str(gold.get("quantity", "")).strip().lower()
             and pv is not None and gv is not None and math.isclose(pv, gv, rel_tol=rel_tol, abs_tol=1e-9))
    return {
        "quantity_ok": quantity_ok, "value_ok": value_ok, "construct_ok": c_state == "matched",
        "ligand_state_ok": l_state == "matched", "temperature_ok": t_state == "matched",
        "two_tuple_naive_ok": naive,
        "all_5_ok": quantity_ok and value_ok and c_state == l_state == t_state == "matched",
        "failure_reasons": reasons,
    }


def _num(v: Any) -> float | None:
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    m = re.search(r"[+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?", normalize_minus(str(v)))
    return float(m.group(0)) if m else None


HISTORICAL_TRAPS = [
    ("BARSTAR_solvent_swap",
     {"quantity": "kex", "value": "120", "unit": "s-1", "sample_construct": "WT", "ligand_state": "apo, 1.8% H2O", "temperature": "298 K"},
     {"quantity": "kex", "value": "120", "unit": "s-1", "sample_construct": "WT", "ligand_state": "apo, 90% H2O", "temperature": "298 K"},
     "SOLVENT_H2O_PCT_DIFFERS"),
    ("EF4_stoichiometry_merge",
     {"quantity": "kex", "value": "850", "unit": "s-1", "sample_construct": "WT", "ligand_state": "1:1 Ca2+-bound", "temperature": "298 K"},
     {"quantity": "kex", "value": "850", "unit": "s-1", "sample_construct": "WT", "ligand_state": "2:1 Ca2+-bound", "temperature": "298 K"},
     "STOICHIOMETRY_DIFFERS"),
    ("PLEXINB1_dimer_as_pB",
     {"quantity": "pB", "value": "90", "unit": "%", "sample_construct": "WT", "ligand_state": "apo", "temperature": "298 K",
      "residues_raw": "fraction of protein in dimeric state", "quote": "Since approximately 90% of the protein is in its dimeric state"},
     {"quantity": "pB", "value": "90", "unit": "%", "sample_construct": "WT", "ligand_state": "apo", "temperature": "298 K",
      "quote": "minor excited state population pB = 90%"},
     "QUANTITY_ROLE_MISMATCH"),
    ("AQADK_holo_vs_apo_label",
     {"quantity": "delta_omega", "value": "0.75", "unit": "ppm", "sample_construct": "WT", "ligand_state": "Mg2+.Ap5A-bound", "temperature": "20 uC"},
     {"quantity": "delta_omega", "value": "0.75", "unit": "ppm", "sample_construct": "WT", "ligand_state": "apo", "temperature": "10 °C"},
     "LIGAND_APO_VS_HOLO"),
    ("CheY_pI_vs_pB_state_swap",
     {"quantity": "pB", "value": "4.5", "unit": "%", "sample_construct": "WT", "ligand_state": "apo", "temperature": "25 C",
      "quote": "intermediate state pI population was 4.5%"},
     {"quantity": "pB", "value": "4.5", "unit": "%", "sample_construct": "WT", "ligand_state": "apo", "temperature": "298.15 K",
      "quote": "minor state pB population was 4.5%"},
     "QUANTITY_ROLE_MISMATCH"),
]
VALID_CASES = [
    ("Valid_OCR_unit_and_temp_conversion",
     {"quantity": "kex", "value": "950", "unit": "s21", "sample_construct": "WT", "ligand_state": "apo, 10% D2O", "temperature": "20 uC"},
     {"quantity": "kex", "value": 950.0, "unit": "s-1", "sample_construct": "wild-type", "ligand_state": "apo, 90% H2O", "temperature": "293.15 K"}),
    ("Valid_pct_vs_fraction_and_mutant_match",
     {"quantity": "pB", "value": "3.2", "unit": "%", "sample_construct": "D57E mutant", "ligand_state": "Mg2+-bound", "temperature": "25 °C"},
     {"quantity": "excited_state_population", "value": 0.032, "unit": "fraction", "sample_construct": "D57E", "ligand_state": "Mg2+-bound",
      "temperature": "298.15 K"}),
    ("Valid_room_temperature_equivalence",
     {"quantity": "kopen", "value": "6500", "unit": "s21", "sample_construct": "Y52C/V145C FRET-labelled", "ligand_state": "apo (ligand-free)",
      "temperature": "room temperature"},
     {"quantity": "kopen", "value": 6500.0, "unit": "s-1", "sample_construct": "Y52C/V145C", "ligand_state": "apo", "temperature": "RT"}),
    ("Valid_multi_temp_contains_match",
     {"quantity": "kex", "value": "950", "unit": "s21", "sample_construct": "WT", "ligand_state": "apo (ligand-free)", "temperature": "10 uC"},
     {"quantity": "kex", "value": 950.0, "unit": "s-1", "sample_construct": "WT", "ligand_state": "apo (ligand-free)",
      "temperature": "10 uC (CPMG); 20 uC (R2 eff profiles too fast, Supplementary Fig. 6)"}),
]
TEMPERATURE_EDGE_TRAPS = [
    ("Room_temp_vs_numeric_20C_rejected",
     {"quantity": "kex", "value": "7000", "unit": "s-1", "sample_construct": "WT", "ligand_state": "apo", "temperature": "20 °C"},
     {"quantity": "kex", "value": "7000", "unit": "s-1", "sample_construct": "WT", "ligand_state": "apo", "temperature": "room temperature"},
     "ROOM_TEMP_VS_NUMERIC_TEMP"),
    ("Room_temp_vs_numeric_10C_rejected",
     {"quantity": "kex", "value": "950", "unit": "s-1", "sample_construct": "WT", "ligand_state": "apo", "temperature": "10 °C"},
     {"quantity": "kex", "value": "950", "unit": "s-1", "sample_construct": "WT", "ligand_state": "apo", "temperature": "ambient"},
     "ROOM_TEMP_VS_NUMERIC_TEMP"),
    ("Multi_temp_mismatch_30C_rejected",
     {"quantity": "kex", "value": "950", "unit": "s-1", "sample_construct": "WT", "ligand_state": "apo", "temperature": "30 uC"},
     {"quantity": "kex", "value": "950", "unit": "s-1", "sample_construct": "WT", "ligand_state": "apo",
      "temperature": "10 uC (CPMG); 20 uC (R2 eff profiles too fast, Supplementary Fig. 6)"},
     "TEMPERATURE_DIFFERS"),
]


def run_self_test() -> dict[str, Any]:
    """The five historical RelaxDB attribution errors must fail all-5 while passing naive (quantity, value) checks."""
    report: dict[str, Any] = {"traps": [], "temperature_traps": [], "valid_cases": [], "passed": True}
    for name, pred, gold, expected in HISTORICAL_TRAPS:
        res = score_record(pred, gold)
        caught = not res["all_5_ok"] and any(r.startswith(expected) for r in res["failure_reasons"])
        report["traps"].append({"name": name, "caught_by_5tuple": caught, "naive_2tuple_passed": res["two_tuple_naive_ok"],
                                "reasons": res["failure_reasons"]})
        report["passed"] &= caught
    for name, pred, gold, expected in TEMPERATURE_EDGE_TRAPS:
        res = score_record(pred, gold)
        caught = not res["all_5_ok"] and not res["temperature_ok"] and any(r.startswith(expected) for r in res["failure_reasons"])
        report["temperature_traps"].append({"name": name, "caught_by_5tuple": caught, "reasons": res["failure_reasons"]})
        report["passed"] &= caught
    for name, pred, gold in VALID_CASES:
        res = score_record(pred, gold)
        report["valid_cases"].append({"name": name, "all_5_ok": res["all_5_ok"], "reasons": res["failure_reasons"]})
        report["passed"] &= res["all_5_ok"]
    return report


run_five_tuple_self_test = run_self_test


# ============================================================================ residues

_ATOM_METHYL_RE = re.compile(r"methyl|CH3|\bC[δγεβ]\d?\b|\bC[dge]\d\b|δ1|γ2|γ1|ε1|ε2|\bme\b", re.I)
_ATOM_SC_RE = re.compile(r"side ?chain|\bNH2\b|N[εδ]\d?|H[εδ]\d?|indole|guanidin", re.I)
_MULTI_RE = re.compile(r"\d\s*[-–—]\s*\d|,|;|\band\b|global|whole|all residues|average|mean|overall|domain|region|segment", re.I)


def parse_single_residue(text: str | None) -> tuple[str | None, int, str] | None:
    """(one-letter aa or None, residue number, atom class bb/sc/methyl) for a single-residue string, else None."""
    s = normalize_minus(str(text or "")).strip()
    if not s or _MULTI_RE.search(s):
        return None
    atom = "methyl" if _ATOM_METHYL_RE.search(s) else ("sc" if _ATOM_SC_RE.search(s) else "bb")
    m = re.match(r"^(?:residue\s*)?([A-Z][a-z]{2})\s*-?\s*(\d{1,4})\b", s)
    if m and m.group(1).upper() in AA3:
        return AA3[m.group(1).upper()], int(m.group(2)), atom
    m = re.match(r"^(?:residue\s*)?([ACDEFGHIKLMNPQRSTVWY])\s*-?\s*(\d{1,4})\b", s)
    if m:
        return m.group(1), int(m.group(2)), atom
    m = re.match(r"^(?:residue\s*)?(\d{1,4})(?:\s*\(?([A-Z][a-z]{2})\)?)?(?:\b|$)", s)
    if m:
        aa = AA3.get((m.group(2) or "").upper())
        return aa, int(m.group(1)), atom
    return None


def residue_tokens(text: str | None) -> tuple[list[tuple[str, int]], list[int]]:
    """All (aa, number) pairs and residue numbers (ranges expanded) named in a free-text region string."""
    if not text:
        return [], []
    s = normalize_minus(str(text))
    pairs: list[tuple[str, int]] = []
    for m in re.finditer(r"\b(" + "|".join(a.title() for a in AA3) + r")\s*[-–]?\s*(\d{1,4})\b", s):
        pairs.append((AA3[m.group(1).upper()], int(m.group(2))))
    for m in re.finditer(r"(?<![A-Za-z0-9])([ACDEFGHIKLMNPQRSTVWY])(\d{1,4})(?![A-Za-z0-9])", s):
        tok = f"{m.group(1)}{m.group(2)}"
        if tok not in {"R1", "R2", "T1", "T2", "S1", "S2", "S3", "S4", "S5", "D1", "D2", "D3", "H1", "H2", "H3", "N1", "C1"}:
            pairs.append((m.group(1), int(m.group(2))))
    pairs = list(dict.fromkeys(pairs))
    nums = {n for _, n in pairs}
    cleaned = re.sub(r"\b\d+(?:\.\d+)?\s*[-–—]\s*\d+(?:\.\d+)?\s*(?:°?\s*[CKF]\b|uC\b|mM\b|µM\b|uM\b|nM\b|MHz\b|Hz\b|s-?1\b|ms\b|ns\b|ps\b|"
                     r"µs\b|us\b|%|ppm\b|Å\b|nm\b|kDa\b)", " ", s, flags=re.I)
    for m in re.finditer(r"(?<![A-Za-z0-9.])(?:[ACDEFGHIKLMNPQRSTVWY])?(\d{1,4})\s*[-–—]\s*(?:[ACDEFGHIKLMNPQRSTVWY])?(\d{1,4})(?!\d)", cleaned):
        a, b = int(m.group(1)), int(m.group(2))
        if 1 <= a <= b <= 3000 and b - a <= 80:
            nums.update(range(a, b + 1))
    for m in re.finditer(r"\b(?:residue|res\.?)\s*#?\s*(\d{1,4})\b", cleaned, re.I):
        nums.add(int(m.group(1)))
    single = parse_single_residue(text)
    if single:
        nums.add(single[1])
        if single[0]:
            pairs.append((single[0], single[1]))
    return list(dict.fromkeys(pairs)), sorted(nums)


def known_offset(warning: str | None) -> int | None:
    m = re.search(r"Auth_seq_ID\s*-\s*Seq_ID\s*=\s*([+-]?\d+)", warning or "")
    if m:
        return int(m.group(1))
    m = re.search(r"\(\s*([+-]\d+)\s*vs\s*signal", warning or "", re.I)
    return int(m.group(1)) if m else None


def resolve_offset(pairs: list[tuple[str, int]], nums: list[int], seq: str, warning: str | None) -> tuple[int | None, str]:
    """offset = author number - 1-based sequence index; verified by amino-acid letters when they are given."""
    has_warning = bool((warning or "").strip()) and (warning or "").strip().lower() not in {"no", "none", "0", "false"}
    kno = known_offset(warning)
    if pairs:
        cands = {0} | ({kno} if kno is not None else set())
        if len(pairs) >= 2:
            votes = Counter(n - (i + 1) for aa, n in pairs for i, ch in enumerate(seq) if ch == aa)
            cands |= {d for d, _ in votes.most_common(5)}
        scored = []
        for d in cands:
            hits = sum(1 for aa, n in pairs if 0 <= n - d - 1 < len(seq) and seq[n - d - 1] == aa)
            scored.append((hits, d))
        best = max(h for h, _ in scored)
        tied = [d for h, d in scored if h == best]
        if len(tied) > 1:
            if kno is not None and kno in tied and best >= 2:
                tied = [kno]
            elif 0 in tied and not has_warning and best >= 2:
                tied = [0]
            else:
                return None, f"ABSTAIN_AMBIGUOUS_OFFSET_TIE:{len(tied)}"
        d = tied[0]
        if len(pairs) >= 2 and best / len(pairs) >= 0.9:
            return d, f"AA_VERIFIED_OFFSET_{d:+d}:{best}/{len(pairs)}"
        if len(pairs) == 1 and best == 1 and (d == 0 and not has_warning or d == kno):
            return d, f"AA_SINGLE_MATCH_OFFSET_{d:+d}"
        return None, f"ABSTAIN_AA_OFFSET_MISMATCH:{best}/{len(pairs)}"
    if not nums:
        return None, "NO_RESIDUE_NUMBERS"
    if not has_warning:
        return (0, "NO_OFFSET_WARNING_ASSUMED_0") if all(1 <= n <= len(seq) for n in nums) else (None, "ABSTAIN_OUT_OF_SEQUENCE")
    if kno is not None:
        return (kno, f"BMRB_OFFSET_{kno:+d}") if all(1 <= n - kno <= len(seq) for n in nums) else (None, "ABSTAIN_OUT_OF_SEQUENCE")
    return None, "ABSTAIN_UNVERIFIED_NUMBERING_OFFSET"


# ============================================================================ loading

@dataclass
class Row:
    entry: str
    doi: str
    source: str
    sample: str
    quantity: str
    role: str
    value: float | None
    value_base: float | None
    dim: str
    unit_raw: str
    construct: str
    species_relation: str
    ligand: str
    temp_k: float | None
    temp_raw: str
    fields: tuple[float, ...]
    ph: str
    buffer: str
    method: str
    residues_raw: str
    residue: tuple[str | None, int, str] | None
    quote: str
    location: str
    secondary: bool
    same_as_deposit: str = ""
    f14_label_flag: bool | None = None
    comparator: str = "="


def _connect(db_path: Path = DB_PATH) -> sqlite3.Connection:
    con = sqlite3.connect(f"file:{db_path}?mode=ro&immutable=1", uri=True)
    con.row_factory = sqlite3.Row
    return con


def open_entries(con: sqlite3.Connection) -> list[str]:
    entries = [r["entry"] for r in con.execute("SELECT entry FROM proteins ORDER BY entry")]
    leaked = set(entries) & SEALED_ENTRIES
    if leaked:
        raise RuntimeError(f"sealed entries present in the open SQLite: {sorted(leaked)}")
    return entries


def _make_row(entry, doi, source, sample, quantity, value, unit, construct, rel, ligand, temp, fields_text, ph, buffer, method,
              residues, quote, location, same_as_deposit="", f14_flag=None, comparator="=") -> Row:
    role = quantity_role(quantity, f"{quote or ''} {residues or ''}")
    vb, dim = to_base(value, unit)
    dim = unit_dim_for_role(role, dim)
    if role == "delta_omega" and vb is not None:
        if dim == "rate" and "rad" in str(unit or "").lower():
            vb = vb / (2 * math.pi)  # rad s^-1 -> Hz
        vb = abs(vb)  # CPMG yields |Δω|; signs come from separate HSQC/HMQC data
    return Row(entry=entry, doi=_norm_doi(doi), source=source, sample=str(sample or ""), quantity=str(quantity or ""), role=role,
               value=value, value_base=vb, dim=dim, unit_raw=str(unit or ""), construct=str(construct or ""),
               species_relation=str(rel or ""), ligand=str(ligand or ""), temp_k=parse_temperature_kelvin(temp, "C"),
               temp_raw=str(temp or ""), fields=tuple(sorted(set(parse_field_mhz(str(fields_text or ""))))), ph=str(ph or ""),
               buffer=str(buffer or ""), method=str(method or ""), residues_raw=str(residues or ""),
               residue=parse_single_residue(residues), quote=str(quote or ""), location=str(location or ""),
               secondary=bool(SECONDARY_RE.search(f"{method or ''} {location or ''}")), same_as_deposit=str(same_as_deposit or ""),
               f14_label_flag=f14_flag, comparator=str(comparator or "="))


def load_sqlite_rows(con: sqlite3.Connection, open_set: set[str]) -> list[Row]:
    rows = []
    sql = """SELECT m.entry, m.doi, m.sample, m.quantity, m.comparator, m.value_num, m.unit_canonical, m.unit_raw, m.method,
                    m.species_relation, m.same_sample_as_deposit, m.construct AS m_construct, m.residues_raw, m.location_in_paper,
                    m.quote, s.construct AS s_construct, s.ligand_state, s.temperature, s.ph, s.buffer, s.field_mhz,
                    s.same_as_deposit
             FROM measurements_clean m
             LEFT JOIN samples s ON s.entry = m.entry AND LOWER(TRIM(s.doi)) = LOWER(TRIM(m.doi)) AND s.sample = m.sample"""
    for r in con.execute(sql):
        if r["entry"] not in open_set:
            continue
        unit = r["unit_canonical"] or r["unit_raw"] or ""
        if unit in {"dimensionless_ratio", "dimensionless_or_unspecified"}:
            unit = "dimensionless"
        rows.append(_make_row(r["entry"], r["doi"], "sqlite_measurements_clean", r["sample"], r["quantity"], r["value_num"], unit,
                              r["s_construct"] or r["m_construct"], r["species_relation"], r["ligand_state"], r["temperature"],
                              r["field_mhz"], r["ph"], r["buffer"], r["method"], r["residues_raw"], r["quote"], r["location_in_paper"],
                              r["same_as_deposit"] or r["same_sample_as_deposit"], None, r["comparator"]))
    return rows


def load_f14_rows(open_set: set[str], batches: Iterable[Path] = F14_BATCHES) -> list[Row]:
    rows = []
    for path in batches:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        for ent in data.get("entries", []):
            entry = ent.get("entry", "")
            if entry not in open_set:
                continue
            for m in ent.get("measurements", []):
                temp = m.get("temperature_c")
                temp_text = f"{temp} °C" if temp not in (None, "") and re.fullmatch(r"[+-]?\d+(?:\.\d+)?", str(temp).strip()) else temp
                rows.append(_make_row(entry, m.get("doi"), "f14_cpmg_sprint", m.get("sample", ""), m.get("quantity"),
                                      m.get("value_num") if m.get("value_num") is not None else _num(m.get("value_raw")),
                                      m.get("unit_canonical") or m.get("unit_raw"), m.get("construct"), "", m.get("ligand_state"),
                                      temp_text, m.get("sample"), "", "", m.get("method"), m.get("residues_raw"), m.get("quote"),
                                      m.get("location_in_paper"), "", bool(m.get("is_relaxdb_label_source")), "="))
    return rows


def load_curated_labels(open_set: set[str], path: Path = CURATED_LABELS) -> dict[str, dict[str, Any]]:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    out = {}
    for bucket in ("relaxdb_open", "relaxdb_cpmg_open"):
        for r in raw.get(bucket, []):
            if r["id"] in open_set:
                out[r["id"]] = {"sequence": r.get("sequence") or "", "label": r.get("label") or "", "dataset": bucket,
                                "curation_source": r.get("curation_source") or "", "doi_missing": r.get("doi_missing") or ""}
    return out


def load_open_inputs(open_set: set[str], inputs_dir: Path = INPUTS_DIR) -> dict[str, dict[str, Any]]:
    out = {}
    for entry in sorted(open_set):
        p = inputs_dir / f"{entry}.json"  # exact path for an open entry; the folder itself is never listed
        if p.is_file():
            out[entry] = json.loads(p.read_text(encoding="utf-8"))
    return out


def derive_label_sources(open_set: set[str], rows: list[Row], curated: dict[str, dict], inputs: dict[str, dict]) -> dict[str, dict[str, list[str]]]:
    """entry -> doi -> provenance tags. Every tag comes from data shipped with the entry, not from a hand table."""
    src: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for r in rows:
        if r.doi and r.f14_label_flag:
            src[r.entry][r.doi].add("f14_is_relaxdb_label_source")
        if r.doi and r.same_as_deposit.strip().lower() == "yes":
            src[r.entry][r.doi].add("sqlite_same_as_deposit_yes")
    for entry, c in curated.items():
        for d in _dois_in(c["curation_source"]) | _dois_in(c["doi_missing"]):
            src[entry][d].add("curated_label_curation_source")
    for entry, inp in inputs.items():
        for d in _dois_in(inp.get("source_lead")) | _dois_in(inp.get("curator_note")):
            src[entry][d].add("inputs_source_lead")
    return {e: {d: sorted(t) for d, t in m.items()} for e, m in src.items() if e in open_set}


# ============================================================================ cross-paper comparison

@dataclass
class Group:
    entry: str
    doi: str
    role: str
    dim: str
    construct: str
    species_relation: str
    ligand: str
    temp_k: float | None
    fields: tuple[float, ...]
    ph: str
    buffer: str
    temp_raw: str = ""
    sources: set[str] = field(default_factory=set)
    rows: list[Row] = field(default_factory=list)

    @property
    def per_residue(self) -> bool:
        return sum(1 for r in self.rows if r.residue) >= 0.6 * len(self.rows)

    def residue_values(self) -> dict[tuple[int, str], tuple[str | None, float]]:
        acc: dict[tuple[int, str], list[tuple[str | None, float]]] = defaultdict(list)
        for r in self.rows:
            if r.residue and r.value_base is not None and r.comparator == "=":
                aa, num, atom = r.residue
                acc[(num, atom)].append((aa, r.value_base))
        return {k: (next((a for a, _ in v if a), None), statistics.median(x for _, x in v)) for k, v in acc.items()}

    def global_values(self) -> list[float]:
        return [r.value_base for r in self.rows if r.value_base is not None and r.comparator == "="]

    def condition(self) -> str:
        if self.temp_k is not None:
            t = f"{self.temp_k:.1f} K"
        elif is_room_temperature(self.temp_raw):
            t = "room temperature"
        else:
            t = "T?"
        f = "/".join(f"{x:g}" for x in self.fields) + " MHz" if self.fields else ""
        parts = [self.construct or "construct?", self.species_relation, self.ligand or "ligand?", t, f, f"n={len(self.rows)}"]
        return " | ".join(p for p in parts if p)


def build_groups(rows: list[Row]) -> dict[tuple[str, str], list[Group]]:
    groups: dict[tuple, Group] = {}
    for r in rows:
        if not r.doi or NON_COMPARABLE_QUANTITY_RE.search(r.role):
            continue
        fields_key = r.fields if r.role in FIELD_DEPENDENT_QUANTITIES else ()
        if r.temp_k is not None:
            temp_key: Any = round(r.temp_k * 2) / 2
        elif is_room_temperature(r.temp_raw):
            temp_key = "RT"
        else:
            multi_t = parse_temperatures_kelvin(r.temp_raw, "C")
            temp_key = tuple(round(x * 2) / 2 for x in multi_t) if multi_t else None
        key = (r.entry, r.doi, r.role, r.dim, construct_key(r.construct), r.species_relation, r.ligand.strip().lower(),
               temp_key, fields_key)
        g = groups.get(key)
        if g is None:
            g = groups[key] = Group(r.entry, r.doi, r.role, r.dim, r.construct, r.species_relation, r.ligand, r.temp_k, fields_key,
                                    r.ph, r.buffer, r.temp_raw)
        g.rows.append(r)
        g.sources.add(r.source)
    out: dict[tuple[str, str], list[Group]] = defaultdict(list)
    for g in groups.values():
        out[(g.entry, g.role)].append(g)
    return out


def construct_key(text: str) -> str:
    f = construct_features(text)
    if not f["known"]:
        return "?"
    return "+".join(sorted(f["muts"])) or "WT"


def _independence(a: Group, b: Group, sources: dict[str, list[str]]) -> tuple[str, bool, bool]:
    la, lb = a.doi in sources, b.doi in sources
    if not sources:
        return "label_source_unknown_for_entry", la, lb
    if la and lb:
        return "both_label_source_papers", la, lb
    if la or lb:
        return "label_source_vs_independent_paper", la, lb
    return "both_independent_of_label_source", la, lb


def compare_pair(a: Group, b: Group, sources: dict[str, list[str]], offset_warning: str, cid: str) -> ComparisonOutcome:
    basis, la, lb = _independence(a, b, sources)
    base = dict(comparison_id=cid, entry=a.entry, quantity_role=a.role, doi_a=a.doi, doi_b=b.doi, condition_a=a.condition(),
                condition_b=b.condition(), independence_basis=basis,
                provenance_a=";".join(sources.get(a.doi, [])) or "not_label_source",
                provenance_b=";".join(sources.get(b.doi, [])) or "not_label_source", sources=sorted(a.sources | b.sources))
    if any(r.secondary for r in a.rows + b.rows):
        return ComparisonOutcome(status="REVIEW_SECONDARY", reason_codes=["SECONDARY_OR_CITED_SOURCE_ROW"], **base)
    if la and lb:
        return ComparisonOutcome(status="LABEL_SOURCE_ONLY", reason_codes=["BOTH_PAPERS_ARE_RELAXDB_LABEL_SOURCES"], **base)
    if a.dim != b.dim or "unknown" in (a.dim, b.dim) or "missing" in (a.dim, b.dim):
        code = "UNIT_MISSING" if "missing" in (a.dim, b.dim) else f"UNIT_DIMENSION_MISMATCH:{a.dim}/{b.dim}"
        return ComparisonOutcome(status="NOT_COMPARABLE_ABSTAIN", reason_codes=[code],
                                 slot_states={"value_unit": "unknown" if "missing" in (a.dim, b.dim) else "incompatible"}, **base)
    slots: dict[str, str] = {"quantity_role": "matched"}
    reasons: list[str] = []
    for name, (state, reason) in (("construct", construct_slot(a.construct, b.construct, a.species_relation, b.species_relation)),
                                  ("ligand_stoich_solvent", ligand_slot(a.ligand, b.ligand)),
                                  ("temperature_k", temperature_slot(a.temp_k, b.temp_k, raw_a=a.temp_raw, raw_b=b.temp_raw,
                                                                     allow_multi_contains=False))):
        slots[name] = state
        if state != "matched":
            reasons.append(reason)
    if a.role in FIELD_DEPENDENT_QUANTITIES:
        state, reason = field_slot(a.fields, b.fields)
        slots["field_mhz"] = state
        if state != "matched":
            reasons.append(reason)
    # values
    n_shared = n_agree = 0
    med = None
    if a.per_residue != b.per_residue:
        slots["value_unit"] = "unknown"
        reasons.append("SCOPE_MISMATCH_PER_RESIDUE_VS_GLOBAL")
        values_agree_flag = None
    elif a.per_residue:
        ra, rb = a.residue_values(), b.residue_values()
        shared = sorted(set(ra) & set(rb))
        aa_conflicts = [k for k in shared if ra[k][0] and rb[k][0] and ra[k][0] != rb[k][0]]
        if aa_conflicts:
            reasons.append(f"AA_MISMATCH_AT_SHARED_RESIDUES:{len(aa_conflicts)}")
        shared = [k for k in shared if k not in aa_conflicts]
        letters_both = all(ra[k][0] and rb[k][0] for k in shared) if shared else False
        if shared and offset_warning and not letters_both:
            reasons.append("UNRESOLVED_NUMBERING_OFFSET")
            slots["value_unit"] = "unknown"
            values_agree_flag = None
        elif not shared:
            reasons.append("NO_SHARED_RESIDUES")
            slots["value_unit"] = "unknown"
            values_agree_flag = None
        else:
            diffs = [abs(ra[k][1] - rb[k][1]) / max(abs(ra[k][1]), abs(rb[k][1]), 1e-12) for k in shared]
            n_shared, med = len(shared), statistics.median(diffs)
            n_agree = sum(1 for k in shared if values_agree(ra[k][1], rb[k][1], a.dim))
            values_agree_flag = n_agree >= PER_RESIDUE_AGREE_FRACTION * n_shared and n_shared >= 3
            if n_shared < 3:
                reasons.append(f"TOO_FEW_SHARED_RESIDUES:{n_shared}")
                values_agree_flag = None
            slots["value_unit"] = "matched" if values_agree_flag else ("unknown" if values_agree_flag is None else "incompatible")
    else:
        va, vb = a.global_values(), b.global_values()
        if not va or not vb:
            reasons.append("NO_EXACT_NUMERIC_VALUE")
            slots["value_unit"] = "unknown"
            values_agree_flag = None
        else:
            ma, mb = statistics.median(va), statistics.median(vb)
            med = abs(ma - mb) / max(abs(ma), abs(mb), 1e-12)
            values_agree_flag = values_agree(ma, mb, a.dim)
            n_agree = int(values_agree_flag)
            slots["value_unit"] = "matched" if values_agree_flag else "incompatible"
    incompatible = [k for k, v in slots.items() if v == "incompatible" and k != "value_unit"]
    unknown = [k for k, v in slots.items() if v == "unknown"]
    common = dict(slot_states=slots, n_shared_residues=n_shared, n_value_agree=n_agree,
                  median_rel_diff=None if med is None else round(med, 4), **base)
    if incompatible:
        reasons.append("VALUES_AGREE" if values_agree_flag else ("VALUES_DIFFER" if values_agree_flag is False else "VALUES_NOT_COMPARED"))
        return ComparisonOutcome(status="CONDITIONAL_DIFF", reason_codes=reasons, **common)
    if unknown:
        return ComparisonOutcome(status="NOT_COMPARABLE_ABSTAIN", reason_codes=reasons or ["SLOT_UNKNOWN"], **common)
    if values_agree_flag:
        info = [] if sources else ["LABEL_SOURCE_PROVENANCE_UNKNOWN"]
        return ComparisonOutcome(status="AGREE_INDEPENDENT", reason_codes=info, **common)
    extra = ["VALUES_DIFFER_ALL_SLOTS_MATCHED"]
    pa, pb_ = _num(a.ph), _num(b.ph)
    if pa is not None and pb_ is not None and abs(pa - pb_) > 0.3:
        extra.append(f"PH_DIFFERS:{pa:g}/{pb_:g}")
    if a.buffer and b.buffer and a.buffer.strip().lower() != b.buffer.strip().lower():
        extra.append("BUFFER_DIFFERS")
    if len(extra) == 1:
        extra.append("UNRECORDED_CONDITION_OR_FIT_MODEL")
    return ComparisonOutcome(status="CONDITIONAL_DIFF", reason_codes=reasons + extra, **common)


def run_comparisons(rows: list[Row], open_list: list[str], label_sources: dict[str, dict[str, list[str]]],
                    offset_warnings: dict[str, str]) -> list[ComparisonOutcome]:
    grouped = build_groups(rows)
    outcomes: list[ComparisonOutcome] = []
    by_entry_roles: dict[str, list[str]] = defaultdict(list)
    for (entry, role) in grouped:
        by_entry_roles[entry].append(role)
    for entry in open_list:
        sources = label_sources.get(entry, {})
        roles = sorted(by_entry_roles.get(entry, []))
        entry_rows = [r for r in rows if r.entry == entry]
        if not roles:
            why = "NO_MEASUREMENT_ROWS" if not entry_rows else "ONLY_UNDEFINED_QUANTITIES_OR_MISSING_DOI"
            outcomes.append(ComparisonOutcome(comparison_id=f"{entry}:entry:0000", entry=entry, quantity_role="*",
                                              status="NOT_COMPARABLE_ABSTAIN", reason_codes=[why], doi_a="",
                                              sources=sorted({r.source for r in entry_rows})))
            continue
        k = 0
        for role in roles:
            groups = sorted(grouped[(entry, role)], key=lambda g: (g.doi, g.condition()))
            dois = sorted({g.doi for g in groups})
            if len(dois) == 1:
                k += 1
                doi = dois[0]
                is_src = doi in sources
                outcomes.append(ComparisonOutcome(
                    comparison_id=f"{entry}:{role}:{k:04d}", entry=entry, quantity_role=role,
                    status="LABEL_SOURCE_ONLY" if is_src else "NOT_COMPARABLE_ABSTAIN",
                    reason_codes=["ONLY_RELAXDB_LABEL_SOURCE_REPORTS_QUANTITY"] if is_src else ["SINGLE_PAPER_NO_CROSS_PAPER_PAIR"],
                    doi_a=doi, condition_a=f"{len(groups)} condition group(s)",
                    independence_basis="label_source_only" if is_src else ("single_paper" if sources else "label_source_unknown_for_entry"),
                    provenance_a=";".join(sources.get(doi, [])) or "not_label_source",
                    sources=sorted({s for g in groups for s in g.sources})))
                continue
            if all(d in sources for d in dois):
                k += 1
                outcomes.append(ComparisonOutcome(
                    comparison_id=f"{entry}:{role}:{k:04d}", entry=entry, quantity_role=role, status="LABEL_SOURCE_ONLY",
                    reason_codes=["ALL_PAPERS_ARE_RELAXDB_LABEL_SOURCES"], doi_a=dois[0], doi_b=dois[1],
                    independence_basis="label_source_only", sources=sorted({s for g in groups for s in g.sources})))
            for i, a in enumerate(groups):
                for b in groups[i + 1:]:
                    if a.doi == b.doi:
                        continue
                    k += 1
                    outcomes.append(compare_pair(a, b, sources, offset_warnings.get(entry, ""), f"{entry}:{role}:{k:04d}"))
    return outcomes


# ============================================================================ RelaxDB label as a recall benchmark

def _evidence_residues(rows: list[Row], observations: list[dict]) -> dict[str, dict[str, list]]:
    """entry -> doi -> {"pairs": [...], "nums": [...], "classes": Counter} for rows that assert conformational exchange."""
    ev: dict[str, dict[str, dict[str, Any]]] = defaultdict(lambda: defaultdict(lambda: {"pairs": [], "nums": [], "classes": Counter()}))
    for r in rows:
        if not r.doi or r.residue is None:
            continue
        is_ex = (r.role in EXCHANGE_EVIDENCE_QUANTITIES and r.value_base is not None and r.value_base > 0) or \
                (r.role in PER_RESIDUE_KINETIC_EVIDENCE and r.value_base is not None and r.value_base > 0)
        if not is_ex:
            continue
        aa, num, _atom = r.residue
        slot = ev[r.entry][r.doi]
        if aa:
            slot["pairs"].append((aa, num))
        slot["nums"].append(num)
        slot["classes"][f"{r.role}_per_residue"] += 1
    for o in observations:
        if o.get("physical_scope") != "solution_conformational_exchange" or not o.get("doi"):
            continue
        pairs, nums = residue_tokens(o.get("region"))
        if not nums:
            continue
        slot = ev[o["entry"]][_norm_doi(o["doi"])]
        slot["pairs"].extend(pairs)
        slot["nums"].extend(nums)
        slot["classes"]["observation_exchange_region"] += len(nums)
    return ev


def run_recall_benchmark(open_list: list[str], curated: dict[str, dict], rows: list[Row], observations: list[dict],
                         label_sources: dict[str, dict[str, list[str]]], offset_warnings: dict[str, str]) -> dict[str, Any]:
    evidence = _evidence_residues(rows, observations)
    per_entry = []
    totals = Counter()
    for entry in open_list:
        cur = curated.get(entry)
        if not cur:
            per_entry.append({"entry": entry, "status": "NO_CURATED_LABEL"})
            continue
        seq, lab = cur["sequence"], cur["label"]
        positives = {i + 1 for i, ch in enumerate(lab) if LABEL_CLASS.get(ch) == "EXCHANGE_POSITIVE"}
        strict = {i + 1 for i, ch in enumerate(lab) if ch in STRICT_POSITIVE}
        sources = label_sources.get(entry, {})
        role_hits: dict[str, set[int]] = {"label_source": set(), "independent": set(), "provenance_unknown": set()}
        independent_on: Counter = Counter()
        doi_rows = []
        for doi, ev in sorted(evidence.get(entry, {}).items()):
            offset, status = resolve_offset(list(dict.fromkeys(ev["pairs"])), sorted(set(ev["nums"])), seq, offset_warnings.get(entry, ""))
            role = "label_source" if doi in sources else ("independent" if sources else "provenance_unknown")
            mapped = set()
            if offset is not None:
                mapped = {n - offset for n in set(ev["nums"]) if 1 <= n - offset <= len(seq)}
                role_hits[role] |= mapped
                if role == "independent":
                    for idx in mapped:
                        independent_on[LABEL_CLASS.get(lab[idx - 1], "OTHER")] += 1
            doi_rows.append({"doi": doi, "role": role, "offset_status": status, "n_evidence_residues": len(set(ev["nums"])),
                             "n_mapped": len(mapped), "n_on_label_positive": len(mapped & positives),
                             "evidence_classes": dict(ev["classes"])})
        rec = {
            "entry": entry, "dataset": cur["dataset"], "sequence_length": len(seq),
            "label_class_counts": dict(Counter(LABEL_CLASS.get(ch, "OTHER") for ch in lab)),
            "n_label_positive": len(positives), "n_label_positive_strict_caret_Y": len(strict),
            "label_source_dois": sorted(sources), "label_source_provenance": {d: t for d, t in sources.items()},
            "recalled_by_label_source": len(role_hits["label_source"] & positives),
            "recalled_by_independent": len(role_hits["independent"] & positives),
            "recalled_by_provenance_unknown": len(role_hits["provenance_unknown"] & positives),
            "recalled_strict_by_independent": len(role_hits["independent"] & strict),
            "independent_evidence_on_label_class": dict(independent_on),
            "papers": doi_rows,
        }
        for key in ("label_source", "independent", "provenance_unknown"):
            rec[f"recall_{key}"] = round(len(role_hits[key] & positives) / len(positives), 4) if positives else None
        assessable = independent_on["EXCHANGE_POSITIVE"] + independent_on["NO_EXCHANGE_DETECTED"] + independent_on["FAST_MOTION_ONLY"]
        rec["independent_agreement"] = round(independent_on["EXCHANGE_POSITIVE"] / assessable, 4) if assessable else None
        rec["status"] = "SCORED" if positives else "NO_EXCHANGE_POSITIVE_LABELS"
        per_entry.append(rec)
        totals["entries"] += 1
        totals["positives"] += len(positives)
        totals["positives_strict"] += len(strict)
        totals["recalled_label_source"] += rec["recalled_by_label_source"]
        totals["recalled_independent"] += rec["recalled_by_independent"]
        totals["recalled_provenance_unknown"] += rec["recalled_by_provenance_unknown"]
        totals["recalled_strict_independent"] += rec["recalled_strict_by_independent"]
        totals["independent_on_positive"] += independent_on["EXCHANGE_POSITIVE"]
        totals["independent_on_no_exchange"] += independent_on["NO_EXCHANGE_DETECTED"]
        totals["independent_on_fast_motion"] += independent_on["FAST_MOTION_ONLY"]
        totals["independent_on_missing_or_nodata"] += independent_on["MISSING_PEAK"] + independent_on["NO_DATA_OR_PROLINE"]
        if sources:
            totals["entries_with_label_source_doi"] += 1
        if rec["recalled_by_independent"] or any(p["role"] == "independent" and p["n_mapped"] for p in doi_rows):
            totals["entries_with_mapped_independent_evidence"] += 1
    pos = totals["positives"] or 1
    assessable = totals["independent_on_positive"] + totals["independent_on_no_exchange"] + totals["independent_on_fast_motion"]
    summary = {
        "n_open_entries": len(open_list),
        "n_entries_with_curated_label": totals["entries"],
        "n_entries_with_label_source_doi": totals["entries_with_label_source_doi"],
        "n_entries_with_mapped_independent_evidence": totals["entries_with_mapped_independent_evidence"],
        "n_label_positive_residues": totals["positives"],
        "n_label_positive_residues_strict": totals["positives_strict"],
        "micro_recall_label_source_papers": round(totals["recalled_label_source"] / pos, 4),
        "micro_recall_independent_papers": round(totals["recalled_independent"] / pos, 4),
        "micro_recall_provenance_unknown_papers": round(totals["recalled_provenance_unknown"] / pos, 4),
        "micro_recall_independent_strict": round(totals["recalled_strict_independent"] / (totals["positives_strict"] or 1), 4),
        "independent_agreement_on_assessable_residues": round(totals["independent_on_positive"] / assessable, 4) if assessable else None,
        "independent_evidence_residue_counts": {k.replace("independent_on_", ""): totals[k] for k in totals if k.startswith("independent_on_")},
    }
    return {"summary": summary, "entries": per_entry}


# ============================================================================ extracted PaperRecords -> comparator

def rows_from_paper_record(record: Any, source: str = "paper_record") -> list[Row]:
    """Measurements of a validated PaperRecord as comparator rows; cited prior work and uncertain origin are secondary."""
    samples = {s.sample_id: s for s in record.samples}
    rows = []
    for m in record.measurements:
        s = samples.get(m.sample_id)
        value = m.value_num if m.value_num is not None else _num(m.value_raw)
        row = _make_row(record.entry, record.doi, source, m.sample_id, m.quantity, value, m.unit_raw,
                        s.construct_label if s else "", s.species_relation if s and s.species_relation != "unknown" else "",
                        s.ligand_state if s else "", s.temperature_raw if s else "", s.field_mhz_raw if s else "",
                        s.ph if s else "", s.buffer if s else "", m.method, m.residues_raw, m.quote, m.locator,
                        s.same_as_deposit if s else "", None, "=")
        row.secondary = row.secondary or m.source_role != "this_study"
        rows.append(row)
    return rows


def compare_paper_records(records: list[Any], label_source_dois: dict[str, set[str]] | None = None,
                          offset_warnings: dict[str, str] | None = None) -> list[ComparisonOutcome]:
    rows = [r for rec in records for r in rows_from_paper_record(rec)]
    entries = sorted({rec.entry for rec in records})
    sources = {e: {_norm_doi(d): ["caller_declared_label_source"] for d in dois} for e, dois in (label_source_dois or {}).items()}
    return run_comparisons(rows, entries, sources, offset_warnings or {})


# ============================================================================ driver

def load_all(db_path: Path = DB_PATH) -> dict[str, Any]:
    con = _connect(db_path)
    try:
        open_list = open_entries(con)
        open_set = set(open_list)
        rows = load_sqlite_rows(con, open_set) + load_f14_rows(open_set)
        warnings = {r["entry"]: (r["numbering_offset_warning"] or "") for r in con.execute("SELECT entry, numbering_offset_warning FROM proteins")}
        warnings = {e: w for e, w in warnings.items() if w.strip() and w.strip().lower() not in {"no", "none", "0", "false"}}
        observations = [dict(r) for r in con.execute("SELECT entry, doi, region, physical_scope FROM observations") if r["entry"] in open_set]
    finally:
        con.close()
    curated = load_curated_labels(open_set)
    inputs = load_open_inputs(open_set)
    sources = derive_label_sources(open_set, rows, curated, inputs)
    return {"open_list": open_list, "rows": rows, "warnings": warnings, "observations": observations, "curated": curated,
            "inputs": inputs, "label_sources": sources}


def write_outputs(out_dir: Path = OUT_DIR, data: dict[str, Any] | None = None) -> dict[str, Any]:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    data = data or load_all()
    outcomes = run_comparisons(data["rows"], data["open_list"], data["label_sources"], data["warnings"])
    status_counts = Counter(o.status for o in outcomes)
    reason_counts = Counter(rc.split(":")[0] for o in outcomes for rc in o.reason_codes)
    entries_covered = {o.entry for o in outcomes}
    per_entry_status = defaultdict(Counter)
    for o in outcomes:
        per_entry_status[o.entry][o.status] += 1
    self_test = run_self_test()
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "tool": "atlas_pipeline.compare",
        "inputs": {"sqlite": str(DB_PATH), "f14_batches": [str(p) for p in F14_BATCHES], "curated_labels": str(CURATED_LABELS),
                   "open_inputs_read": len(data["inputs"]), "config_relaxdb_source_dois_read": False},
        "parameters": {"value_rel_tol": VALUE_REL_TOL, "abs_floor": ABS_FLOOR, "temperature_tol_k": TEMP_TOL_K,
                       "per_residue_agree_fraction": PER_RESIDUE_AGREE_FRACTION},
        "summary": {
            "n_open_entries": len(data["open_list"]), "n_entries_with_outcomes": len(entries_covered),
            "n_measurement_rows": len(data["rows"]),
            "n_rows_by_source": dict(Counter(r.source for r in data["rows"])),
            "n_outcomes": len(outcomes), "by_status": dict(status_counts), "by_reason": dict(reason_counts.most_common()),
            "n_entries_with_label_source_doi": len(data["label_sources"]),
            "label_source_provenance_counts": dict(Counter(t for m in data["label_sources"].values() for tags in m.values() for t in tags)),
            "five_tuple_self_test_passed": self_test["passed"],
        },
        "five_tuple_self_test": self_test,
        "label_sources": data["label_sources"],
        "per_entry_status": {e: dict(c) for e, c in sorted(per_entry_status.items())},
        "outcomes": [o.model_dump() for o in outcomes],
    }
    json_path = out_dir / "data_driven_comparisons.json"
    json_path.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    csv_path = out_dir / "data_driven_comparisons.csv"
    cols = ["comparison_id", "entry", "quantity_role", "status", "reason_codes", "slot_quantity_role", "slot_value_unit",
            "slot_construct", "slot_ligand_stoich_solvent", "slot_temperature_k", "slot_field_mhz", "doi_a", "doi_b", "condition_a",
            "condition_b", "n_shared_residues", "n_value_agree", "median_rel_diff", "independence_basis", "provenance_a", "provenance_b",
            "sources"]
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for o in outcomes:
            d = o.model_dump()
            w.writerow({**{k: d[k] for k in cols if k in d}, "reason_codes": ";".join(o.reason_codes), "sources": ";".join(o.sources),
                        **{f"slot_{k}": v for k, v in o.slot_states.items()}})
    bench = run_recall_benchmark(data["open_list"], data["curated"], data["rows"], data["observations"], data["label_sources"],
                                 data["warnings"])
    bench_payload = {
        "generated_at": payload["generated_at"], "tool": "atlas_pipeline.compare.run_recall_benchmark",
        "definition": ("RelaxDB per-residue labels are the reference. A residue is recalled when a paper reports exchange there "
                       "(Rex > 0, fitted |Δω|, per-residue kex or pB, or a curated solution-exchange observation region) after "
                       "sequence-verified numbering. Label-source papers (data-derived) and independent papers are scored separately; "
                       "'independent agreement' is the share of independent-evidence residues that RelaxDB labels exchange-positive "
                       "among residues the label can assess (positive, no exchange, fast motion)."),
        "label_alphabet": LABEL_CLASS, "strict_positive_letters": sorted(STRICT_POSITIVE),
        "label_alphabet_provenance": "outputs/relaxdb_label_vs_qualitative_20261122/run_label_vs_qualitative_audit.py (team audit 2026-11-22)",
        **bench,
    }
    bench_path = out_dir / "relaxdb_label_recall_benchmark.json"
    bench_path.write_text(json.dumps(bench_payload, indent=1, ensure_ascii=False), encoding="utf-8")
    return {"comparisons_json": str(json_path), "comparisons_csv": str(csv_path), "benchmark_json": str(bench_path),
            "summary": payload["summary"], "benchmark_summary": bench["summary"], "outcomes": outcomes, "data": data}
