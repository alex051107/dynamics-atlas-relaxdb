"""Canonical domain contract (Pydantic v2) for Dynamics Atlas extraction.

One contract replaces the per-stage prompt variants: `PaperRecord.model_json_schema()` is the output schema a reader
(model or human) must satisfy, and `export_active_prompt()` writes it into the single live extraction prompt.

Physical checks run as validators, so a wrongly typed row cannot be constructed:
  * NOE / S2 are dimensionless; a frequency unit (Hz, MHz, GHz) is a field strength, not a unit of the value.
  * R1 / R2 / Rex / kex are rates; a time unit (s, ms, msec, us, ns, ps) means a T1/T2/tau was mislabeled.
  * S2 with a time unit is a tau_c / tau_e mislabel.
  * An oligomer or dimer fraction cannot be stored as a conformational population (pB / population).
  * species_relation 'same_protein_other_construct' or 'homolog' contradicts same_as_deposit == 'yes'.
Raw printed strings are never modified; display normalization (s21 -> s^-1, uC -> °C) is a computed view.
"""
from __future__ import annotations

import json
import math
import re
import unicodedata
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, computed_field, field_validator, model_validator

WORK = Path(__file__).resolve().parents[1]
ACTIVE_PROMPT_PATH = Path(__file__).resolve().parent / "ACTIVE_EXTRACTION_PROMPT.md"
ACTIVE_PROMPT_POINTER = WORK / "config" / "active_prompt.txt"

# Held-out RelaxDB entries (same list as ledger/extract_20261118/verify_b5_delivery.py). Never read or emitted.
SEALED_ENTRIES = frozenset({
    "ALP", "ECOADK", "HMG1A", "HMG1B", "MLC1PC", "NUSGTD", "PYP", "VILHP",
    "19335", "CDNFCT", "RNASEHI", "UBE2G1",
})

Stance = Literal["supports", "no_dynamics_in_window", "unclear", "artefact_suspected"]
SourceRole = Literal["this_study", "cited_prior_work", "uncertain"]
EvidenceModality = Literal["text", "table", "si_table", "figure_vector", "figure_raster", "figure_caption"]
DocumentRole = Literal["main_article", "supplement_si"]
FigureClass = Literal["VECTOR_PLOT", "RASTER_IMAGE", "MIXED_VECTOR_RASTER"]
SpeciesRelation = Literal["target", "same_protein_other_construct", "homolog", "unknown"]
SameAsDeposit = Literal["yes", "no", "unclear"]
MeasuredEntity = Literal["conformational_exchange", "oligomer_or_association", "other", "unknown"]
QualitativeCategory = Literal["dynamic_region", "alternate_state", "cryptic_pocket", "no_dynamics_in_window", "artefact_suspected"]
EvidenceLevel = Literal["experimental", "author_interpretation", "simulation_or_prediction"]
SlotState = Literal["matched", "incompatible", "unknown"]
ComparisonStatus = Literal[
    "AGREE_INDEPENDENT", "CONDITIONAL_DIFF", "LABEL_SOURCE_ONLY", "REVIEW_SECONDARY", "NOT_COMPARABLE_ABSTAIN",
]
FigureLinkStatus = Literal["EXACT_FIGURE_OR_PANEL", "FIGURE_LEVEL_ONLY", "UNRESOLVED_MISSING_FIGURE", "NOT_A_FIGURE_LOCATOR"]


class PhysicalValidationError(ValueError):
    """Raised (and wrapped by Pydantic) when a row breaks a physical-dimension rule; `.code` is machine readable."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code


def require_open_entry(entry: str) -> str:
    if str(entry).strip().upper() in SEALED_ENTRIES:
        raise PermissionError(f"refusing sealed RelaxDB entry {entry!r}")
    return entry


# ----------------------------------------------------------------------------- text normalization

MINUS_CHARS = "−‒–—‐‑﹣－⫺⫺"


def normalize_minus(text: str) -> str:
    out = text or ""
    for ch in MINUS_CHARS:
        out = out.replace(ch, "-")
    return out


_OCR_DISPLAY_RULES = (
    (re.compile(r"(?<![A-Za-z])s\s?(?:21|⫺1|−1|-1|–1)(?![\w])"), "s^-1"),
    (re.compile(r"(?<=\d)\s?uC\b"), " °C"),
    (re.compile("⬍⬍"), "<<"),
    (re.compile("⫻"), "×"),
)


def normalize_ocr_display(text: str | None) -> str:
    """Display-only cleanup of PDF-to-text artifacts. Never apply to stored raw fields or grounding text."""
    out = str(text or "")
    for pattern, repl in _OCR_DISPLAY_RULES:
        out = pattern.sub(repl, out)
    return out


# ----------------------------------------------------------------------------- units and quantities

UNIT_ALIASES: dict[str, tuple[str, str, float | None]] = {}  # compact -> (display unit, dimension, factor to base unit)


def _alias(dimension: str, display: str, scale: float | None, *forms: str) -> None:
    for f in forms:
        UNIT_ALIASES[f] = (display, dimension, scale)


_alias("rate", "s^-1", 1.0, "s^-1", "s-1", "s^(-1)", "/s", "1/s", "sec-1", "sec^-1", "s21", "persecond", "rad/s", "rads-1", "rad.s-1")
_alias("rate", "Hz", 1.0, "hz")
_alias("rate", "kHz", 1e3, "khz")
_alias("rate", "ms^-1", 1e3, "ms-1", "ms^-1", "/ms", "1/ms")
_alias("rate", "min^-1", 1.0 / 60.0, "min-1", "min^-1", "/min")
_alias("rate", "h^-1", 1.0 / 3600.0, "h-1", "hr-1", "hr^-1", "h^-1", "/h")
_alias("spectrometer_frequency", "MHz", None, "mhz")
_alias("spectrometer_frequency", "GHz", None, "ghz")
_alias("time", "s", 1.0, "s", "sec", "second", "seconds")
_alias("time", "ms", 1e-3, "ms", "msec", "millisecond", "milliseconds")
_alias("time", "us", 1e-6, "us", "usec", "microsecond", "microseconds")
_alias("time", "ns", 1e-9, "ns", "nsec", "nanosecond", "nanoseconds")
_alias("time", "ps", 1e-12, "ps", "psec", "picosecond", "picoseconds")
_alias("dimensionless", "", 1.0, "", "dimensionless", "unitless", "none", "ratio", "dimensionless_ratio",
       "dimensionless_or_unspecified", "a.u.", "au")
_alias("fraction", "%", 0.01, "%", "percent", "pct")
_alias("fraction", "fraction", 1.0, "fraction", "frac")
_alias("chemical_shift", "ppm", 1.0, "ppm")
_alias("chemical_shift", "ppb", 1e-3, "ppb")
_alias("temperature", "K", None, "k", "kelvin")
_alias("temperature", "°C", None, "°c", "degc", "c")
_alias("energy", "kcal/mol", 4.184, "kcal/mol", "kcalmol-1", "kcal.mol-1")
_alias("energy", "kJ/mol", 1.0, "kj/mol", "kjmol-1")
_alias("length", "Å", 1.0, "å", "angstrom")
_alias("length", "nm", 10.0, "nm")


def _compact_unit(raw: str | None) -> str:
    s = unicodedata.normalize("NFKC", str(raw or "")).strip()
    s = normalize_minus(s).replace("µ", "u").replace("μ", "u").replace("·", ".")
    s = re.sub(r"\(.*?\)\s*$", "", s).strip()  # trailing notes such as "ms (column header unit)"
    s = re.sub(r"\s+", "", s).lower()
    s = s.replace("^(-1)", "^-1")
    if not s.startswith(("1/", "10^")):
        s = re.sub(r"^[+-]?\d+(?:\.\d+)?", "", s)  # "600 MHz", "50.7 MHz": a printed field strength, keep its unit
    return s


def normalize_unit(raw: str | None) -> str:
    """Canonical display unit for a printed unit (raw stays untouched). Unknown units are returned compacted."""
    compact = _compact_unit(raw)
    hit = UNIT_ALIASES.get(compact)
    return hit[0] if hit else compact


def unit_dimension(raw: str | None) -> str:
    """'rate', 'time', 'spectrometer_frequency', 'dimensionless', 'fraction', 'chemical_shift', ... or 'unknown'."""
    compact = _compact_unit(raw)
    hit = UNIT_ALIASES.get(compact)
    return hit[1] if hit else "unknown"


def unit_scale_factor(raw: str | None) -> tuple[str, float] | None:
    """Return (dimension, scale_to_base) from the single canonical UNIT_ALIASES table, or None."""
    compact = _compact_unit(raw)
    hit = UNIT_ALIASES.get(compact)
    if hit and hit[2] is not None:
        return hit[1], hit[2]
    return None


QUANTITY_ALIASES = {
    "r1": "r1", "r2": "r2", "r2eff": "r2", "r_2": "r2", "r_1": "r1", "r1rho": "r1rho", "r1p": "r1rho",
    "rex": "rex", "r_ex": "rex", "kex": "kex", "k_ex": "kex", "kab": "kab", "k_ab": "kab", "kba": "kba", "k_ba": "kba",
    "k12": "kab", "k21": "kba", "kopen": "kopen", "kclose": "kclose", "kct": "kct",
    "t1": "t1", "t2": "t2", "t1rho": "t1rho", "tauex": "tau_ex", "tau_ex": "tau_ex", "taue": "tau_e", "tau_e": "tau_e",
    "taum": "tau_m", "tau_m": "tau_m", "tauc": "tau_c", "tau_c": "tau_c", "taus": "tau_s", "tau_s": "tau_s",
    "noe": "noe", "hetnoe": "noe", "1h15nnoe": "noe", "s2": "s2", "s2f": "s2f", "s2s": "s2s", "s2axis": "s2axis",
    "pb": "pb", "p_b": "pb", "pa": "pa", "p_a": "pa", "pi": "pi", "p_i": "pi", "population": "population",
    "excited_state_population": "pb", "minor_state_population": "pb",
    "delta_omega": "delta_omega", "deltaomega": "delta_omega", "dw": "delta_omega", "Δω": "delta_omega",
}

# Allowed unit dimensions per canonical quantity. Quantities not listed are not dimension-checked.
QUANTITY_DIMENSIONS: dict[str, frozenset[str]] = {
    **{q: frozenset({"rate"}) for q in ("r1", "r2", "r1rho", "rex", "kex", "kab", "kba", "kopen", "kclose", "kct")},
    **{q: frozenset({"time"}) for q in ("t1", "t2", "t1rho", "tau_ex", "tau_e", "tau_m", "tau_c", "tau_s")},
    "noe": frozenset({"dimensionless"}),
    **{q: frozenset({"dimensionless"}) for q in ("s2", "s2f", "s2s", "s2axis")},
    **{q: frozenset({"fraction", "dimensionless"}) for q in ("pb", "pa", "pi", "population")},
    "delta_omega": frozenset({"chemical_shift", "rate"}),
}
POPULATION_QUANTITIES = frozenset({"pb", "pa", "pi", "population"})
FIELD_DEPENDENT_QUANTITIES = frozenset({"r1", "r2", "r1rho", "rex", "noe", "t1", "t2", "t1rho"})

OLIGOMER_RE = re.compile(r"\b(dimer(?:ic|ization|s)?|trimer(?:ic)?|tetramer(?:ic)?|oligomer(?:ic|ization|s)?|monomer[- ]dimer|"
                         r"self[- ]association|aggregat\w*)\b", re.I)
CONFORM_RE = re.compile(r"\b(excited[- ]state|minor[- ]state|invisible state|conformational|cpmg|cest|r1rho|relaxation dispersion)\b", re.I)


def canonical_quantity(name: str | None) -> str:
    s = unicodedata.normalize("NFKC", str(name or "")).strip()
    s = s.replace("Δω", "delta_omega").replace("δω", "delta_omega").replace("τ", "tau_").replace("ρ", "rho")
    s = s.lower()
    s = re.sub(r"\((?:s|ms)?\^?-?1?\)$", "", s)
    s = re.sub(r"[\s\-,{}\[\]]+", "", s)
    s = s.replace("^", "")
    if s in QUANTITY_ALIASES:
        return QUANTITY_ALIASES[s]
    flat = s.replace("_", "")
    return QUANTITY_ALIASES.get(flat, s)


def quantity_role(name: str | None, context: str = "") -> str:
    """Canonical quantity plus state role: an oligomer fraction or an intermediate-state pI is not a pB."""
    q = canonical_quantity(name)
    if q in POPULATION_QUANTITIES and OLIGOMER_RE.search(context or "") and not CONFORM_RE.search(context or ""):
        return "oligomer_fraction"
    if q in {"population", "pb"} and re.search(r"\b(?:p_?i|intermediate state|state\s+i)\b", context or "", re.I) \
            and not re.search(r"\b(?:p_?b|state\s+b|excited state)\b", context or "", re.I):
        return "pi"
    return q


def check_quantity_unit(quantity: str | None, unit: str | None) -> str | None:
    """Return an error code if the unit's physical dimension is impossible for the quantity, else None."""
    q = canonical_quantity(quantity)
    allowed = QUANTITY_DIMENSIONS.get(q)
    if not allowed:
        return None
    if not str(unit or "").strip() and "dimensionless" not in allowed:
        return "UNIT_MISSING"  # a rate, time or shift without a unit cannot be checked or compared
    dim = unit_dimension(unit)
    if dim in allowed:
        return None
    s2_family = q in {"s2", "s2f", "s2s", "s2axis"}
    if (q == "noe" or s2_family) and dim in {"rate", "spectrometer_frequency"}:
        return "NOE_FREQUENCY_UNIT" if q == "noe" else "S2_FREQUENCY_UNIT"
    if s2_family and dim == "time":
        return "S2_TIME_UNIT"
    if allowed == {"rate"} and dim == "time":
        return "RATE_WITH_TIME_UNIT"
    if allowed == {"rate"} and dim == "spectrometer_frequency":
        return "RATE_WITH_SPECTROMETER_FREQUENCY"
    if dim == "unknown":
        return "UNIT_UNRECOGNIZED"
    return "UNIT_DIMENSION_MISMATCH"


# ----------------------------------------------------------------------------- numbers, temperatures, fields

_NUM_RE = re.compile(r"(?<![\w.])([+-]?)(\d+(?:\.\d+)?|\.\d+)(?:[eE]([+-]?\d+))?(?!\w)(?!\.\d)")
_THOUSANDS_RE = re.compile(r"(?<![\d,])(\d{1,3}(?:,\d{3})+)(?![\d,])")


def numeric_values(text: str | None) -> list[float]:
    """Signed numeric tokens with token boundaries: '5' is not found inside '150', '-5' differs from '+5'."""
    s = normalize_minus(unicodedata.normalize("NFKC", str(text or "")))
    out = []
    for sign, digits, exp in _NUM_RE.findall(s):
        v = float(digits) * (10 ** int(exp) if exp else 1)
        out.append(-v if sign == "-" else v)
    return out


def _numeric_values_any(text: str) -> list[float]:
    collapsed = _THOUSANDS_RE.sub(lambda m: m.group(1).replace(",", ""), normalize_minus(text or ""))
    return numeric_values(text) + numeric_values(collapsed)


def verify_value_tokens(value_raw: str | float | int | None, quote: str) -> tuple[bool, list[str]]:
    """Every numeric token of the printed value must occur in the quote as a whole token with the same sign."""
    expected = numeric_values(str(value_raw)) if value_raw is not None else []
    if not expected:
        return False, ["NO_NUMERIC_TOKEN_IN_VALUE"]
    available = _numeric_values_any(quote)
    missing = [v for v in expected if not any(math.isclose(v, a, rel_tol=1e-9, abs_tol=1e-12) for a in available)]
    if missing:
        return False, [f"VALUE_TOKEN_NOT_IN_QUOTE:{m:g}" for m in missing]
    return True, []


_SCI_RE = re.compile(r"([+-]?\d+(?:\.\d+)?)\s*[×xX*]\s*10\s*\^?\s*([+-]?\d+)")


def _value_num_consistent(value_num: float, value_raw: str) -> bool:
    """value_num must equal a printed token, the printed scientific-notation value, or a %<->fraction conversion."""
    raw = normalize_minus(unicodedata.normalize("NFKC", value_raw))
    candidates = list(_numeric_values_any(raw))
    candidates += [float(m) * 10 ** int(e) for m, e in _SCI_RE.findall(raw)]
    candidates += [c / 100.0 for c in candidates] + [c * 100.0 for c in candidates]
    return any(math.isclose(value_num, c, rel_tol=1e-6, abs_tol=1e-12) for c in candidates)


_TEMP_UNIT_PAT = r"(?:K|°\s*C|º\s*C|o\s*C|uC|deg(?:rees)?\s*C|C)\b"
_TEMP_RE = re.compile(rf"(?<![A-Za-z0-9.])([+-]?\d+(?:\.\d+)?)\s*({_TEMP_UNIT_PAT})")
_TEMP_LIST_RE = re.compile(
    rf"(?:^|[;(:]\s*|\bat\s+)((?:[+-]?\d+(?:\.\d+)?\s*(?:,|and)\s*)+[+-]?\d+(?:\.\d+)?)\s*({_TEMP_UNIT_PAT})"
)
_TEMP_RANGE_RE = re.compile(
    rf"\d+(?:\.\d+)?\s*(?:{_TEMP_UNIT_PAT}\s*)?(?:-|to)\s*\d+(?:\.\d+)?\s*(?:{_TEMP_UNIT_PAT})"
)
_TEMP_INEQ_RANGE_RE = re.compile(
    rf"\d+(?:\.\d+)?\s*{_TEMP_UNIT_PAT}\s*<=?\s*T\s*<=?\s*\d+(?:\.\d+)?\s*{_TEMP_UNIT_PAT}",
    re.I,
)
_BARE_RANGE_RE = re.compile(r"^\s*[+-]?\d+(?:\.\d+)?\s*(?:-|to)\s*[+-]?\d+(?:\.\d+)?\s*$", re.I)
_BARE_LIST_RE = re.compile(r"^\s*[+-]?\d+(?:\.\d+)?(?:\s*,\s*[+-]?\d+(?:\.\d+)?)+\s*$")
_ROOM_TEMP_RE = re.compile(r"\b(?:room\s+temp(?:erature)?|ambient(?:\s+temp(?:erature)?))\b|\bambient\b|\br\.t\.", re.I)
_RT_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9])RT(?![A-Za-z0-9])")


def _clean_temp_text(text: str | float | int | None) -> str:
    if text is None:
        return ""
    s = normalize_minus(unicodedata.normalize("NFKC", str(text))).strip()
    if not s:
        return ""
    s = re.sub(r"\s*(?:±|\+/-|\+-)\s*\d+(?:\.\d+)?", "", s)  # "25 ± 0.5 °C" is 25 °C, not 0.5 °C
    # Old PDF Symbol-font '±' often extracts as ' 6 ' before a fractional error (e.g. "25 6 0.1°C" -> "25°C").
    s = re.sub(rf"(\d+(?:\.\d+)?)\s+6\s+0?\.\d+(?=\s*{_TEMP_UNIT_PAT})", r"\1", s)
    return s


def _dedup_kelvin(items: list[tuple[float, str]]) -> list[float]:
    """Collapse exact duplicates and dual-unit printings of one temperature (e.g. '30 °C (303 K)' -> [303.0])."""
    out: list[tuple[float, str]] = []
    for k, u in sorted(items):
        if out:
            pk, pu = out[-1]
            if abs(k - pk) <= 1e-6:
                continue
            if pu != u and abs(k - pk) <= 1.0:
                best_k = min((pk, k), key=lambda x: abs(x - round(x)))
                out[-1] = (round(best_k, 2), "K" if best_k == round(best_k) else pu)
                continue
        out.append((round(k, 2), u))
    return [k for k, _ in out]


def parse_temperatures_kelvin(text: str | float | int | None, default_unit: Literal["K", "C"] | None = None) -> list[float]:
    """All unambiguous discrete temperatures in kelvin (sorted, deduplicated); ranges and qualitative RT yield []."""
    s = _clean_temp_text(text)
    if not s or _BARE_RANGE_RE.fullmatch(s) or _TEMP_RANGE_RE.search(s) or _TEMP_INEQ_RANGE_RE.search(s):
        return []
    cleaned = s
    items: list[tuple[float, str]] = []

    def _consume_list(m: re.Match[str]) -> str:
        unit_kind = "K" if m.group(2).strip().upper() == "K" else "C"
        for tok in re.findall(r"[+-]?\d+(?:\.\d+)?", m.group(1)):
            v = float(tok)
            items.append((round(v if unit_kind == "K" else v + 273.15, 2), unit_kind))
        return " "

    cleaned = _TEMP_LIST_RE.sub(_consume_list, cleaned)
    for num, unit in _TEMP_RE.findall(cleaned):
        unit_kind = "K" if unit.strip().upper() == "K" else "C"
        v = float(num)
        items.append((round(v if unit_kind == "K" else v + 273.15, 2), unit_kind))
    if items:
        return _dedup_kelvin(items)
    if default_unit:
        if re.fullmatch(r"[+-]?\d+(?:\.\d+)?", s):
            v = float(s)
            return [round(v if default_unit == "K" else v + 273.15, 2)]
        if _BARE_LIST_RE.fullmatch(s):
            for tok in re.findall(r"[+-]?\d+(?:\.\d+)?", s):
                v = float(tok)
                items.append((round(v if default_unit == "K" else v + 273.15, 2), default_unit))
            return _dedup_kelvin(items)
    return []


def is_room_temperature(text: str | float | int | None) -> bool:
    """True when text states qualitative room/ambient temperature with no numeric temperature value."""
    if text is None or isinstance(text, (int, float)):
        return False
    s = _clean_temp_text(text)
    if not s or parse_temperatures_kelvin(s, "C"):
        return False
    if _ROOM_TEMP_RE.search(s) or _RT_TOKEN_RE.search(s):
        return True
    return s.lower().strip(" .()") in {"rt", "r.t", "r.t."}


def parse_temperature_kelvin(text: str | float | int | None, default_unit: Literal["K", "C"] | None = None) -> float | None:
    """One unambiguous temperature in kelvin, or None (missing, a range, qualitative RT, or several different temperatures)."""
    s = _clean_temp_text(text)
    if not s or _BARE_RANGE_RE.fullmatch(s) or _TEMP_RANGE_RE.search(s) or _TEMP_INEQ_RANGE_RE.search(s):
        return None
    temps = parse_temperatures_kelvin(s, default_unit)
    return temps[0] if len(temps) == 1 else None


def parse_field_mhz(text: str | None) -> list[float]:
    """Spectrometer fields printed as '600 MHz', '600/850 MHz' or '600 (14.1 T) MHz'."""
    s = str(text or "")
    out: list[float] = []
    for m in re.finditer(r"((?:\d{3,4}(?:\.\d+)?\s*(?:/|,|and)\s*)*\d{3,4}(?:\.\d+)?)\s*(?:\([^)]*\)\s*)?MHz", s):
        out.extend(float(x) for x in re.findall(r"\d{3,4}(?:\.\d+)?", m.group(1)))
    return sorted(set(out))


# ----------------------------------------------------------------------------- figure locators

_FIG_LOCATOR_RE = re.compile(r"\b(Supplementary\s+|Extended\s+Data\s+)?Fig(?:ure)?s?\.?\s*(S?\d+)\s*([a-z])?\b", re.I)


def figure_number(label: str | None) -> str:
    """'Figure S6' -> 'S6', 'Supplementary Fig. 4' -> 'S4', 'Extended Data Fig. 2' -> 'ED2', 'Fig. 3' -> '3'."""
    parsed = parse_figure_locator(label)
    return parsed[0] if parsed else ""


def parse_figure_locator(locator: str | None) -> tuple[str, str] | None:
    m = _FIG_LOCATOR_RE.search(str(locator or ""))
    if not m:
        return None
    prefix, number, panel = (m.group(1) or "").lower(), m.group(2).upper(), (m.group(3) or "").lower()
    if prefix.startswith("supplementary") and not number.startswith("S"):
        number = "S" + number
    elif prefix.startswith("extended"):
        number = "ED" + number.lstrip("S")
    return number, panel


def resolve_figure_link(locator: str | None, figures: list["FigureAsset"]) -> tuple[FigureLinkStatus, str | None]:
    """Exact figure/panel or figure-level link for a locator. Never substitutes another figure for a missing one."""
    parsed = parse_figure_locator(locator)
    if parsed is None:
        return "NOT_A_FIGURE_LOCATOR", None
    number, panel = parsed
    same_number = [f for f in figures if f.figure_number.upper() == number]
    if not same_number:
        return "UNRESOLVED_MISSING_FIGURE", None
    if panel:
        exact = [f for f in same_number if f.panel.lower() == panel]
        if exact:
            return "EXACT_FIGURE_OR_PANEL", exact[0].figure_id
        return "FIGURE_LEVEL_ONLY", same_number[0].figure_id
    whole = [f for f in same_number if not f.panel]
    if whole:
        return "EXACT_FIGURE_OR_PANEL", whole[0].figure_id
    return "FIGURE_LEVEL_ONLY", same_number[0].figure_id


# ----------------------------------------------------------------------------- models

class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=False)


class GroundingResult(_Strict):
    row_id: str
    ok: bool
    char_start: int | None = None
    char_end: int | None = None
    reasons: list[str] = Field(default_factory=list)


_UNIPROT_RE = re.compile(
    r"^(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})(?:-\d+)?$"
)


class SampleSpec(_Strict):
    sample_id: str = Field(min_length=1)
    uniprot_accession: str | None = None
    isoform_version: str | None = None
    construct_label: str = ""
    species_relation: SpeciesRelation = "unknown"
    same_as_deposit: SameAsDeposit = "unclear"
    ligand_state: str = ""
    temperature_raw: str = ""
    ph: str = ""
    buffer: str = ""
    field_mhz_raw: str = ""
    note: str = ""
    quote: str = ""

    @field_validator("uniprot_accession", mode="before")
    @classmethod
    def _validate_uniprot(cls, v: object) -> str | None:
        if v is None:
            return None
        s = str(v).strip()
        if not s:
            return None
        if s.lower() in {"x", "none", "null", "n/a", "na", "unknown"}:
            raise ValueError(f"invalid UniProt placeholder: {v!r}; use null when absent")
        if not _UNIPROT_RE.fullmatch(s):
            raise ValueError(f"not a valid UniProt accession: {v!r}")
        return s

    @field_validator("isoform_version", mode="before")
    @classmethod
    def _clean_isoform(cls, v: object) -> str | None:
        if v is None:
            return None
        s = str(v).strip()
        return s or None

    @computed_field  # type: ignore[prop-decorator]
    @property
    def temperature_k(self) -> float | None:
        return parse_temperature_kelvin(self.temperature_raw)

    @model_validator(mode="after")
    def _deposit_consistency(self) -> "SampleSpec":
        if self.species_relation in {"same_protein_other_construct", "homolog"} and self.same_as_deposit == "yes":
            raise PhysicalValidationError(
                "CONTRADICTORY_DEPOSIT",
                f"sample {self.sample_id}: species_relation={self.species_relation!r} cannot be the deposited sample",
            )
        return self


class MeasurementRow(_Strict):
    row_id: str = Field(min_length=1)
    sample_id: str = Field(min_length=1)
    quantity: str = Field(min_length=1)
    value_raw: str = Field(min_length=1)
    value_num: float | None = None
    unit_raw: str = ""
    uncertainty_raw: str = ""
    residues_raw: str = ""
    method: str = ""
    source_role: SourceRole
    evidence_modality: EvidenceModality
    document_role: DocumentRole = "main_article"
    stance: Stance | None = None
    measured_entity: MeasuredEntity = "unknown"
    locator: str = ""
    quote: str = Field(min_length=1)
    char_start: int | None = Field(default=None, ge=0)
    char_end: int | None = Field(default=None, ge=0)

    @computed_field  # type: ignore[prop-decorator]
    @property
    def quantity_canonical(self) -> str:
        return quantity_role(self.quantity, f"{self.quote} {self.residues_raw}")

    @computed_field  # type: ignore[prop-decorator]
    @property
    def unit_canonical(self) -> str:
        return normalize_unit(self.unit_raw)

    @computed_field  # type: ignore[prop-decorator]
    @property
    def quote_display(self) -> str:
        return normalize_ocr_display(self.quote)

    @field_validator("value_raw", "quote")
    @classmethod
    def _not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("must not be blank")
        return v

    @model_validator(mode="after")
    def _physical_rules(self) -> "MeasurementRow":
        code = check_quantity_unit(self.quantity, self.unit_raw)
        if code:
            raise PhysicalValidationError(code, f"{self.row_id}: quantity {self.quantity!r} with unit {self.unit_raw!r}")
        q = canonical_quantity(self.quantity)
        if q in POPULATION_QUANTITIES and (
            self.measured_entity == "oligomer_or_association"
            or quantity_role(self.quantity, f"{self.quote} {self.residues_raw}") == "oligomer_fraction"
        ):
            raise PhysicalValidationError(
                "OLIGOMER_FRACTION_AS_POPULATION",
                f"{self.row_id}: an oligomer/dimer fraction is not a conformational population ({self.quantity!r})",
            )
        if (self.char_start is None) != (self.char_end is None):
            raise ValueError("char_start and char_end must be given together")
        if self.char_start is not None and self.char_end is not None and self.char_end <= self.char_start:
            raise ValueError("char_end must exceed char_start")
        if self.value_num is not None and not _value_num_consistent(self.value_num, self.value_raw):
            raise ValueError(f"{self.row_id}: value_num {self.value_num} disagrees with value_raw {self.value_raw!r}")
        return self

    def verify_grounding(self, source_text: str) -> GroundingResult:
        """LangExtract-style check: exact span (given or located) plus signed, token-bounded value match."""
        reasons: list[str] = []
        start, end = self.char_start, self.char_end
        if start is not None and end is not None:
            if end > len(source_text) or source_text[start:end] != self.quote:
                reasons.append("SPAN_MISMATCH")
        else:
            idx = source_text.find(self.quote)
            if idx < 0:
                reasons.append("QUOTE_NOT_VERBATIM")
            else:
                start, end = idx, idx + len(self.quote)
                if source_text.find(self.quote, idx + 1) >= 0:
                    reasons.append("AMBIGUOUS_SPAN_FIRST_OCCURRENCE_USED")
        ok_val, val_reasons = verify_value_tokens(self.value_raw, self.quote)
        reasons.extend(val_reasons)
        hard = [r for r in reasons if not r.startswith("AMBIGUOUS_SPAN")]
        return GroundingResult(row_id=self.row_id, ok=not hard and ok_val, char_start=start, char_end=end, reasons=reasons)


class FigureAsset(_Strict):
    figure_id: str
    source_pdf: str
    document_role: DocumentRole
    page_index: int = Field(ge=0)
    bbox: tuple[float, float, float, float]
    caption_label: str = ""
    figure_number: str = ""
    panel: str = ""
    caption_text: str = ""
    caption_page_index: int | None = None
    classification: FigureClass
    n_vector_paths: int = Field(default=0, ge=0)
    n_raster_images: int = Field(default=0, ge=0)
    raster_area_fraction: float = Field(default=0.0, ge=0.0, le=1.0)
    png_path: str = ""
    png_dpi: int = 300
    png_width_px: int = 0
    png_height_px: int = 0
    png_sha256: str = ""
    redistribution_permission: Literal["UNKNOWN_RESTRICTED", "EXPLICIT_PER_FIGURE_GRANT"] = "UNKNOWN_RESTRICTED"
    license_scope: Literal["unknown", "article_level_unverified_for_third_party_figures", "per_figure_explicit_grant"] = "unknown"


class AxisCalibration(_Strict):
    axis: Literal["x", "y"]
    scale: Literal["linear", "log10"]
    slope: float
    intercept: float
    tick_values: list[float]
    tick_positions: list[float]
    max_residual_frac: float = Field(ge=0.0)
    loo_max_rel_error: float | None = None

    def to_data(self, pos: float) -> float:
        v = self.slope * pos + self.intercept
        return 10 ** v if self.scale == "log10" else v

    def to_page(self, value: float) -> float:
        v = math.log10(value) if self.scale == "log10" else value
        return (v - self.intercept) / self.slope


class DigitizedSeries(_Strict):
    kind: Literal["marker", "polyline"]
    color: str
    points: list[tuple[float, float]]
    page_points: list[tuple[float, float]]


class PlotDigitizationResult(_Strict):
    source_pdf: str
    page_index: int
    clip: tuple[float, float, float, float]
    frame: tuple[float, float, float, float] | None = None
    status: Literal["OK", "ABSTAIN"]
    abstain_reason: str = ""
    panels_detected: int = 0
    x_calibration: AxisCalibration | None = None
    y_calibration: AxisCalibration | None = None
    series: list[DigitizedSeries] = Field(default_factory=list)
    overlay_png: str = ""
    crop_png: str = ""
    pixel_alignment_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    warnings: list[str] = Field(default_factory=list)

    @computed_field  # type: ignore[prop-decorator]
    @property
    def n_points(self) -> int:
        return sum(len(s.points) for s in self.series)

    def marker_points(self) -> list[tuple[float, float]]:
        return [p for s in self.series if s.kind == "marker" for p in s.points]


class QualitativeObservation(_Strict):
    """Source-grounded qualitative observation (dynamic region, alternate state, cryptic pocket) without requiring a numeric value."""

    obs_id: str = Field(min_length=1)
    sample_id: str = Field(min_length=1)
    document_role: DocumentRole = "main_article"
    category: QualitativeCategory
    evidence_level: EvidenceLevel
    residues_raw: str = ""
    pdb_ids: list[str] = Field(default_factory=list)
    summary: str = Field(min_length=1)
    locator: str = ""
    quote: str = Field(min_length=1)
    char_start: int | None = Field(default=None, ge=0)
    char_end: int | None = Field(default=None, ge=0)

    @field_validator("summary", "quote")
    @classmethod
    def _not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("must not be blank")
        return v

    @field_validator("pdb_ids")
    @classmethod
    def _validate_pdbs(cls, v: list[str]) -> list[str]:
        out: list[str] = []
        for item in v:
            code = str(item).strip().upper()
            if not re.fullmatch(r"[0-9][A-Z0-9]{3}", code):
                raise ValueError(f"not a PDB id: {item!r}")
            out.append(code)
        return out

    @model_validator(mode="after")
    def _span_order(self) -> "QualitativeObservation":
        if (self.char_start is None) != (self.char_end is None):
            raise ValueError("char_start and char_end must be given together")
        if self.char_start is not None and self.char_end is not None and self.char_end <= self.char_start:
            raise ValueError("char_end must exceed char_start")
        return self

    def verify_grounding(self, source_text: str) -> GroundingResult:
        """Verify exact verbatim quote span without requiring a printed numeric token."""
        reasons: list[str] = []
        start, end = self.char_start, self.char_end
        if start is not None and end is not None:
            if end > len(source_text) or source_text[start:end] != self.quote:
                reasons.append("SPAN_MISMATCH")
        else:
            idx = source_text.find(self.quote)
            if idx < 0:
                reasons.append("QUOTE_NOT_VERBATIM")
            else:
                start, end = idx, idx + len(self.quote)
                if source_text.find(self.quote, idx + 1) >= 0:
                    reasons.append("AMBIGUOUS_SPAN_FIRST_OCCURRENCE_USED")
        hard = [r for r in reasons if not r.startswith("AMBIGUOUS_SPAN")]
        return GroundingResult(row_id=self.obs_id, ok=not hard, char_start=start, char_end=end, reasons=reasons)


class AlternateStatePDB(_Strict):
    pdb_id: str
    state_label: str
    relation: SpeciesRelation = "unknown"
    ligand: str = ""
    source_role: SourceRole = "this_study"
    quote: str = ""
    char_start: int | None = None
    char_end: int | None = None

    @field_validator("pdb_id")
    @classmethod
    def _pdb(cls, v: str) -> str:
        if not re.fullmatch(r"[0-9][A-Za-z0-9]{3}", v.strip()):
            raise ValueError(f"not a PDB id: {v!r}")
        return v.strip().upper()


class ComparisonOutcome(_Strict):
    comparison_id: str
    entry: str
    quantity_role: str
    status: ComparisonStatus
    reason_codes: list[str] = Field(default_factory=list)
    slot_states: dict[str, SlotState] = Field(default_factory=dict)
    doi_a: str
    doi_b: str = ""
    condition_a: str = ""
    condition_b: str = ""
    n_shared_residues: int = 0
    n_value_agree: int = 0
    median_rel_diff: float | None = None
    independence_basis: str = ""
    provenance_a: str = ""
    provenance_b: str = ""
    sources: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _status_consistency(self) -> "ComparisonOutcome":
        if self.status == "AGREE_INDEPENDENT":
            if not self.doi_b or self.doi_a == self.doi_b:
                raise ValueError("AGREE_INDEPENDENT needs two different DOIs")
            if any(state != "matched" for state in self.slot_states.values()):
                raise ValueError("AGREE_INDEPENDENT needs every attribution slot matched")
        if self.status != "AGREE_INDEPENDENT" and not self.reason_codes:
            raise ValueError(f"{self.status} needs at least one reason code")
        return self


class PaperRecord(_Strict):
    entry: str
    doi: str
    title: str = ""
    samples: list[SampleSpec] = Field(default_factory=list)
    measurements: list[MeasurementRow] = Field(default_factory=list)
    qualitative_observations: list[QualitativeObservation] = Field(default_factory=list)
    figures: list[FigureAsset] = Field(default_factory=list)
    alternate_states: list[AlternateStatePDB] = Field(default_factory=list)
    stance: Stance | None = None
    notes: str = ""

    @field_validator("entry")
    @classmethod
    def _open_entry(cls, v: str) -> str:
        return require_open_entry(v.strip())

    @field_validator("doi")
    @classmethod
    def _doi(cls, v: str) -> str:
        d = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", v.strip(), flags=re.I).lower()
        if not re.fullmatch(r"10\.\d{4,9}/\S+", d):
            raise ValueError(f"not a DOI: {v!r}")
        return d

    @model_validator(mode="after")
    def _references(self) -> "PaperRecord":
        sample_ids = [s.sample_id for s in self.samples]
        if len(sample_ids) != len(set(sample_ids)):
            raise ValueError("duplicate sample_id")
        row_ids = [m.row_id for m in self.measurements]
        if len(row_ids) != len(set(row_ids)):
            raise ValueError("duplicate row_id")
        obs_ids = [q.obs_id for q in self.qualitative_observations]
        if len(obs_ids) != len(set(obs_ids)):
            raise ValueError("duplicate obs_id")
        known = set(sample_ids) | {"unknown"}
        missing = sorted({m.sample_id for m in self.measurements} - known)
        if missing:
            raise ValueError(f"measurements reference unknown samples: {missing}")
        missing_q = sorted({q.sample_id for q in self.qualitative_observations} - known)
        if missing_q:
            raise ValueError(f"qualitative_observations reference unknown samples: {missing_q}")
        return self

    def primary_measurements(self) -> list[MeasurementRow]:
        """Rows this paper measured itself; cited prior work and uncertain origin are excluded from primary counts."""
        return [m for m in self.measurements if m.source_role == "this_study"]

    def verify_grounding(self, texts: dict[str, str]) -> list[GroundingResult]:
        """`texts` maps document_role ('main_article' / 'supplement_si') to the exact ingested text."""
        results = []
        for m in self.measurements:
            src = texts.get(m.document_role)
            if src is None:
                results.append(GroundingResult(row_id=m.row_id, ok=False, reasons=[f"NO_TEXT_FOR_{m.document_role.upper()}"]))
            else:
                results.append(m.verify_grounding(src))
        return results

    def verify_qualitative_grounding(self, texts: dict[str, str]) -> list[GroundingResult]:
        """Verify verbatim span grounding for all qualitative observations (no numeric token required)."""
        results = []
        for q in self.qualitative_observations:
            src = texts.get(q.document_role)
            if src is None:
                results.append(GroundingResult(row_id=q.obs_id, ok=False, reasons=[f"NO_TEXT_FOR_{q.document_role.upper()}"]))
            else:
                results.append(q.verify_grounding(src))
        return results

    def figure_links(self) -> dict[str, tuple[FigureLinkStatus, str | None]]:
        return {m.row_id: resolve_figure_link(m.locator, self.figures) for m in self.measurements if parse_figure_locator(m.locator)}


# ----------------------------------------------------------------------------- live prompt export

def _rule_lines() -> list[str]:
    dims = "\n".join(f"  - `{q}`: {', '.join(sorted(d))}" for q, d in sorted(QUANTITY_DIMENSIONS.items()))
    return [
        "1. Output exactly one JSON object valid against the schema below; nothing else.",
        "2. `quote` is copied verbatim from the given text; `char_start`/`char_end` index that exact text (end exclusive).",
        "3. `value_raw` is the number as printed (sign, comparator, uncertainty kept); every numeric token in it must"
        " appear in `quote` as a whole token with the same sign.",
        "4. `source_role`: `this_study` only for values this paper measured; values the paper attributes to earlier work"
        " are `cited_prior_work`; undecidable origin is `uncertain`.",
        "5. `evidence_modality` names where the value is printed: " + ", ".join(f"`{v}`" for v in EvidenceModality.__args__) + ".",
        "6. `stance` (optional per row, required per paper when the paper interprets dynamics): "
        + ", ".join(f"`{v}`" for v in Stance.__args__) + ".",
        "7. Allowed unit dimensions per quantity (a spectrometer field such as 600 MHz is never the unit of a value):\n" + dims,
        "8. Oligomer, dimer or association fractions are never `pB`/`population`; set `measured_entity` accordingly.",
        "9. One sample card per construct, mutant, ligand stoichiometry and solvent step; record `uniprot_accession`"
        " and `isoform_version` on each sample (use `null` when absent, never placeholders like `x`); a homolog or"
        " other construct cannot have `same_as_deposit` = `yes`.",
        "10. Main-article and supplementary text are separate sources: set `document_role` to `main_article` or"
        " `supplement_si` for every measurement and qualitative observation; supplementary tables use"
        " `evidence_modality` = `si_table`.",
        "11. A value only shown in a figure is recorded with `evidence_modality` `figure_vector` or `figure_raster` and"
        " the exact figure/panel locator; never point a locator at a different figure.",
        "12. Record non-numeric dynamics findings (dynamic regions, alternate states, cryptic pockets, no-dynamics"
        " controls, suspected artefacts) in `qualitative_observations` with `category`, `evidence_level`"
        " (`experimental` vs `author_interpretation` vs `simulation_or_prediction`), `sample_id`, `document_role`,"
        " `locator`, and verbatim `quote`.",
    ]


def _proposed_rule_lines() -> list[str]:
    return [
        "STATUS: PROPOSED 2026-11-26, default strict-abstain (awaiting expert sign-off; see PROPOSED_RULES_20261126.md).",
        "- Proposed Rule P1 (Ligand condition isolation, AQADK Nature 2007): keep ligand-bound (e.g. Mg2+.Ap5A holo)"
        " observations strictly separate and non-comparable (abstain) against unbound (apo) labels.",
        "- Proposed Rule P2 (Association vs conformational exchange, Plexin-B1 JPCB 2012): route dimeric/oligomeric"
        " fractions (e.g. '~90% in its dimeric state') into `measured_entity = 'oligomer_or_association'`, never"
        " conformational `pB`, while keeping true exchange (e.g. T83 Rex = 7.0 s^-1) as `conformational_exchange`.",
        "- Proposed Rule P3 (Cryptic pocket evidence bar, TEM-1 PNAS 2021 vs BRD4 JMC 2024): tag direct experimental"
        " exchange/excited-state pocket measurements (e.g. TEM-1 Omega-loop CEST 1.05%, kex = 98 s^-1) as"
        " `evidence_level = 'experimental'`; keep MD pocket predictions and ligand-mobility broadening (BRD4"
        " Ile146/Leu94) in `author_interpretation` or `simulation_or_prediction` rather than experimental pocket counts.",
    ]


def canonical_prompt_rules() -> str:
    """Single canonical rules block shared by ACTIVE_EXTRACTION_PROMPT.md and all extract.py entry points."""
    return "\n".join([
        "## Core extraction rules",
        *_rule_lines(),
        "",
        "## Proposed boundary rules",
        *_proposed_rule_lines(),
    ])


def export_active_prompt(out_path: Path | None = None, pointer_path: Path | None = ACTIVE_PROMPT_POINTER) -> Path:
    """Write the single live extraction prompt (rules + live JSON schema) and point config/active_prompt.txt at it."""
    out_path = Path(out_path or ACTIVE_PROMPT_PATH)
    previous = pointer_path.read_text(encoding="utf-8").strip() if pointer_path and pointer_path.exists() else ""
    if pointer_path is not None:
        try:
            rel = out_path.resolve().relative_to(pointer_path.resolve().parents[1])
        except ValueError:
            rel = out_path.resolve()
        if previous == rel.as_posix() and out_path.is_file():  # a rerun: keep the value the first export replaced
            m = re.search(r"Supersedes the previous pointer value: `([^`]*)`", out_path.read_text(encoding="utf-8"))
            previous = m.group(1) if m else previous
    schema = PaperRecord.model_json_schema()
    body = "\n".join([
        "# Active extraction prompt (generated)",
        "",
        "Generated by `atlas_pipeline.schema.export_active_prompt()` from the live `PaperRecord` Pydantic model."
        " Edit the model, not this file.",
        f"Supersedes the previous pointer value: `{previous or 'none'}`.",
        "",
        canonical_prompt_rules(),
        "",
        "## Output JSON schema (`PaperRecord.model_json_schema()`)",
        "",
        "```json",
        json.dumps(schema, indent=2, ensure_ascii=False),
        "```",
        "",
    ])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(body, encoding="utf-8")
    if pointer_path is not None:
        pointer_path.parent.mkdir(parents=True, exist_ok=True)
        pointer_path.write_text(f"{rel.as_posix()}\n", encoding="utf-8")
    return out_path
