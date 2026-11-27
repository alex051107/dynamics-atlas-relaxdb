"""Command line: ingest, figures, validate, extract, compare, cards, e2e.

    python3 -m atlas_pipeline.cli e2e [--out DIR] [--docling] [--run-extract]
    python3 -m atlas_pipeline.cli extract [--out DIR] [--backend auto|anthropic_sdk|claude_cli|swarm_agent_direct]

Live inputs are four local PDFs (AQADK main + SI, CypA main, KRAS SI) addressed by exact path; nothing is downloaded.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from . import adapters
from .schema import WORK

OUT_DEFAULT = WORK / "outputs/atlas_pipeline_run_20261123"
LIVE_SPECS: list[dict[str, Any]] = [
    {"entry": "AQADK_CPMG", "doi": "10.1038/nature06410", "title": "Intrinsic motions along an enzymatic reaction trajectory",
     "path": WORK / "sources_cache/AQADK_nature06410.pdf", "document_role": "main_article", "stem": "AQADK_main"},
    {"entry": "AQADK_CPMG", "doi": "10.1038/nature06410", "title": "",
     "path": WORK / "sources_cache/AQADK_CPMG_SI/41586_2007_BFnature06410_MOESM269_ESM.pdf", "document_role": "supplement_si",
     "stem": "AQADK_SI"},
    {"entry": "CYPA_CPMG", "doi": "10.1038/nature04105", "title": "Intrinsic dynamics of an enzyme underlies catalysis",
     "path": WORK / "sources_cache/CYPA_CPMG/Eisenmesser2005.pdf", "document_role": "main_article", "stem": "CYPA_main"},
    {"entry": "KRAS_CPMG", "doi": "10.1038/s41594-023-01070-z", "title": "",
     "path": WORK / "sources_cache/KRAS2023_SI.pdf", "document_role": "supplement_si", "stem": "KRAS_SI"},
]

# Full 10/10 OPEN RelaxDB-CPMG live source manifest (zero sealed proteins; never touches RNASEHI).
# Notes:
# - BLAC_CPMG/2020_si.pdf and 2025_phosphate_si.pdf are 1817-byte HTML download stubs, not PDFs;
#   we use the verified PMC8284444 JATS XML main article + real 10-page PDF SI aac02628-20_supp_s1_seq7.pdf.
# - HTPDZ/2024_SI.pdf (36 pp., 14.4 MB) sets use_docling=False for fast deterministic PyMuPDF ingest.
# - CHEY_CPMG uses PMC3552614.xml (10.1016/j.str.2012.05.008, RelaxDB label source) for dynamics extraction
#   plus Cho2000.pdf (10.1006/jmbi.2000.3595, structural NMR paper) for local figure crops.
LIVE_SPECS_10: list[dict[str, Any]] = [
    *LIVE_SPECS,
    {"entry": "ARGKIN_CPMG", "doi": "10.1021/bi101664u",
     "title": "Rate limiting domain and loop motions in arginine kinase",
     "path": WORK / "sources_cache/ARGKIN_PMC3091953.jats.xml", "document_role": "main_article",
     "stem": "ARGKIN_2011_main", "record_stem": "ARGKIN_CPMG"},
    {"entry": "ARGKIN_CPMG", "doi": "10.1021/bi101664u",
     "title": "Rate limiting domain and loop motions in arginine kinase",
     "path": WORK / "sources_cache/ARGKIN_bi101664u_si_001.pdf", "document_role": "supplement_si",
     "stem": "ARGKIN_2011_SI", "record_stem": "ARGKIN_CPMG", "use_docling": True},
    {"entry": "ARGKIN_CPMG", "doi": "10.1021/jacs.7b00236",
     "title": "The Michaelis Complex of Arginine Kinase Samples the Transition State at a Frequency that Matches the Catalytic Rate",
     "path": WORK / "sources_cache/ARGKIN_PMC5663447.jats.xml", "document_role": "main_article",
     "stem": "ARGKIN_2017_main", "record_stem": "ARGKIN_CPMG_jacs7b00236"},
    {"entry": "ARGKIN_CPMG", "doi": "10.1021/jacs.7b00236",
     "title": "The Michaelis Complex of Arginine Kinase Samples the Transition State at a Frequency that Matches the Catalytic Rate",
     "path": WORK / "sources_cache/ARGKIN_ja7b00236_si_001.pdf", "document_role": "supplement_si",
     "stem": "ARGKIN_2017_SI", "record_stem": "ARGKIN_CPMG_jacs7b00236", "use_docling": True},
    {"entry": "BLAC_CPMG", "doi": "10.1128/aac.02628-20",
     "title": "Two β-Lactamase Variants with Reduced Clavulanic Acid Inhibition Display Different Millisecond Dynamics",
     "path": WORK / "sources_cache/BLAC_CPMG/PMC8284444.xml", "document_role": "main_article",
     "stem": "BLAC_2020_main"},
    {"entry": "BLAC_CPMG", "doi": "10.1128/aac.02628-20",
     "title": "Two β-Lactamase Variants with Reduced Clavulanic Acid Inhibition Display Different Millisecond Dynamics",
     "path": WORK / "sources_cache/BLAC_CPMG_SI/PMC8284444/aac02628-20_supp_s1_seq7.pdf", "document_role": "supplement_si",
     "stem": "BLAC_2020_SI", "use_docling": True},
    {"entry": "BLVRB_CPMG", "doi": "10.3389/fmolb.2023.1244587",
     "title": "Identifying structural and dynamic changes during the Biliverdin Reductase B catalytic cycle",
     "path": WORK / "sources_cache/BLVRB_CPMG/2023.pdf", "document_role": "main_article",
     "stem": "BLVRB_2023_main"},
    {"entry": "CHEY_CPMG", "doi": "10.1016/j.str.2012.05.008",
     "title": "Segmental motions, not a two-state concerted switch, underlie allostery in CheY",
     "path": WORK / "sources_cache/PMC3552614.xml", "document_role": "main_article",
     "stem": "CHEY_2012_main", "record_stem": "CHEY_CPMG"},
    {"entry": "CHEY_CPMG", "doi": "10.1006/jmbi.2000.3595",
     "title": "NMR Structure of Activated CheY",
     "path": WORK / "sources_cache/CHEY_CPMG/Cho2000.pdf", "document_role": "main_article",
     "stem": "CHEY_Cho2000_main", "extract_dynamics": False},
    {"entry": "HTPDZ_CPMG", "doi": "10.1038/s41467-024-48997-5",
     "title": "Structural basis of substrate recognition and allosteric activation of the proapoptotic mitochondrial HtrA2 protease",
     "path": WORK / "sources_cache/HTPDZ/2024_main.pdf", "document_role": "main_article",
     "stem": "HTPDZ_2024_main"},
    {"entry": "HTPDZ_CPMG", "doi": "10.1038/s41467-024-48997-5",
     "title": "Structural basis of substrate recognition and allosteric activation of the proapoptotic mitochondrial HtrA2 protease",
     "path": WORK / "sources_cache/HTPDZ/2024_SI.pdf", "document_role": "supplement_si",
     "stem": "HTPDZ_2024_SI", "use_docling": False},
    {"entry": "RNASE_CPMG", "doi": "10.1021/ja0514949",
     "title": "Conservation of us-ms Enzyme Motions in the Apo- and Substrate-Mimicked State",
     "path": WORK / "sources_cache/RNASE_CPMG/Beach2005_complete.pdf", "document_role": "main_article",
     "stem": "RNASE_Beach2005_main"},
    {"entry": "VHR_CPMG", "doi": "10.1021/acs.biochem.0c00245",
     "title": "Allosteric Impact of the Variable Insert Loop in Vaccinia H1-Related (VHR) Phosphatase",
     "path": WORK / "sources_cache/VHR2020.pdf", "document_role": "main_article",
     "stem": "VHR_2020_main"},
    {"entry": "VHR_CPMG", "doi": "10.1021/acs.biochem.0c00245",
     "title": "Allosteric Impact of the Variable Insert Loop in Vaccinia H1-Related (VHR) Phosphatase",
     "path": WORK / "sources_cache/VHR2020_bi0c00245_si_001.pdf", "document_role": "supplement_si",
     "stem": "VHR_2020_SI", "use_docling": True},
]


def _dump(obj: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1, ensure_ascii=False, default=str), encoding="utf-8")


def cmd_ingest(
    out: Path,
    specs: list[dict[str, Any]] = LIVE_SPECS,
    *,
    use_docling: bool = False,
    use_docling_si: bool = False,
) -> dict[str, Any]:
    from .ingest import ingest_jats, ingest_pdf, ingest_xlsx

    docs, summary = {}, []
    for s in specs:
        path = Path(s["path"])
        suffix = path.suffix.lower()
        if "use_docling" in s:
            doc_use_docling = bool(s["use_docling"]) and suffix == ".pdf"
        else:
            doc_use_docling = bool(use_docling or (use_docling_si and s["document_role"] == "supplement_si")) and suffix == ".pdf"
        if suffix in {".xml", ".nxml"}:
            doc = ingest_jats(path, s["doi"], s["title"], s["document_role"])
        elif suffix in {".xlsx", ".xlsm"}:
            doc = ingest_xlsx(path, s["doi"], s["document_role"])
        else:
            doc = ingest_pdf(path, s["doi"], s["title"], s["document_role"], use_docling=doc_use_docling)
        doi_key = s["doi"].lower()
        docs[(doi_key, s["document_role"])] = doc
        summary.append({
            "entry": s["entry"], "doi": doi_key, "path": str(path), "document_role": s["document_role"],
            "reader": doc.reader, "use_docling": doc_use_docling,
            "identity_ok": doc.identity_ok, "identity_reason": doc.identity_reason, "usable": doc.usable,
            "n_chars": len(doc.text), "pages": doc.pages, "rotated_pages": doc.rotated_pages,
            "n_tables": len(doc.tables), "n_figure_captions": len(doc.figure_captions),
            "n_si_references": len(doc.si_references), "sha256": doc.sha256,
        })
    _dump({"generated_at": datetime.now().isoformat(timespec="seconds"), "documents": summary}, out / "ingest_summary.json")
    return {"docs": docs, "summary": summary}


def texts_by_doi(docs: dict) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for (doi, role), doc in docs.items():
        if doc.usable:
            out.setdefault(doi.lower(), {})[role] = doc.text
    return out


def cmd_figures(out: Path, specs: list[dict[str, Any]] = LIVE_SPECS) -> dict[str, Any]:
    from .figures import run_figures

    pdf_specs = [
        {k: v for k, v in s.items() if k in {"entry", "doi", "path", "document_role", "stem", "license_scope"}}
        for s in specs
        if Path(s["path"]).suffix.lower() == ".pdf"
    ]
    return run_figures(pdf_specs, out / "figures")


def merge_figure_manifests(primary: dict[str, Any], *extras: dict[str, Any]) -> dict[str, Any]:
    """Merge figure manifests while preserving every primary digitization (and its verification dict) intact."""
    sources = list(primary.get("sources") or [])
    seen_sources = {(s.get("entry"), s.get("doi"), s.get("pdf")) for s in sources}
    figures = list(primary.get("figures") or [])
    seen_figs = {f.get("figure_id") for f in figures}
    unpaired = list(primary.get("unpaired_captions") or [])
    skipped = list(primary.get("skipped_regions") or [])
    digitizations = list(primary.get("digitizations") or [])
    seen_digs = {(d.get("figure_id"), tuple(d.get("clip") or ()), d.get("overlay_png")) for d in digitizations}

    for extra in extras:
        if not extra:
            continue
        for s in extra.get("sources") or []:
            k = (s.get("entry"), s.get("doi"), s.get("pdf"))
            if k not in seen_sources:
                sources.append(s)
                seen_sources.add(k)
        for f in extra.get("figures") or []:
            fid = f.get("figure_id")
            if fid not in seen_figs:
                figures.append(f)
                seen_figs.add(fid)
        unpaired.extend(extra.get("unpaired_captions") or [])
        skipped.extend(extra.get("skipped_regions") or [])
        for d in extra.get("digitizations") or []:
            dk = (d.get("figure_id"), tuple(d.get("clip") or ()), d.get("overlay_png"))
            if dk not in seen_digs:
                digitizations.append(d)
                seen_digs.add(dk)

    merged = dict(primary)
    merged["generated_at"] = datetime.now().isoformat(timespec="seconds")
    merged["sources"] = sources
    merged["figures"] = figures
    merged["unpaired_captions"] = unpaired
    merged["skipped_regions"] = skipped
    merged["digitizations"] = digitizations
    merged["summary"] = dict(primary.get("summary") or {}) | {
        "n_pdfs": len(sources),
        "n_pages_inspected": sum(len(s.get("pages_inspected") or []) for s in sources),
        "n_figure_regions": len(figures),
        "by_class": {
            c: sum(1 for f in figures if f.get("classification") == c)
            for c in ("VECTOR_PLOT", "RASTER_IMAGE", "MIXED_VECTOR_RASTER")
        },
        "n_digitized_panels_ok": sum(1 for d in digitizations if d.get("status") == "OK"),
        "n_overlays": sum(1 for d in digitizations if d.get("overlay_png")),
    }
    return merged


def score_live_extractions_all_batches(
    records: list[Any],
    *,
    backend: str = "swarm_agent_direct",
    auth: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Score accepted live PaperRecords against SQLite + ALL F14 batches (batch1 & batch2) via compare.score_record()."""
    from collections import Counter

    from .compare import (
        DB_PATH,
        F14_BATCHES,
        _connect,
        load_f14_rows,
        load_sqlite_rows,
        parse_single_residue,
        score_record,
    )
    from .extract import _to_score_dict_from_gold, _to_score_dict_from_measurement, auth_status

    entries = {r.entry for r in records}
    con = _connect(DB_PATH)
    try:
        sq_rows = load_sqlite_rows(con, entries)
    finally:
        con.close()
    f14_rows = load_f14_rows(entries, F14_BATCHES)
    all_gold = sq_rows + f14_rows

    auth_info = auth if auth is not None else auth_status(check_cli=True)
    per_paper: list[dict[str, Any]] = []
    slot_totals: Counter = Counter()
    reason_totals: Counter = Counter()
    total_matched = total_all5 = total_naive2 = total_same_doi_gold = total_same_doi_gold_dyn = 0

    for rec in records:
        sample_map = {s.sample_id: s for s in rec.samples}
        live_primary = rec.primary_measurements()
        live_dicts = [(_to_score_dict_from_measurement(m, sample_map.get(m.sample_id)), m) for m in live_primary]
        same_doi_gold = [g for g in all_gold if g.entry == rec.entry and g.doi == rec.doi.lower()]
        other_doi_gold = [g for g in all_gold if g.entry == rec.entry and g.doi != rec.doi.lower()]
        same_doi_dyn = [g for g in same_doi_gold if g.role != "other"]

        candidates: list[tuple[tuple, int, int, dict[str, Any]]] = []
        for gi, g in enumerate(same_doi_dyn):
            g_dict = _to_score_dict_from_gold(g)
            g_res = g.residue
            for li, (p_dict, m) in enumerate(live_dicts):
                if m.quantity_canonical != g.role:
                    continue
                p_res = parse_single_residue(m.residues_raw)
                if g_res is not None and p_res is not None and p_res[1] != g_res[1]:
                    continue
                sc = score_record(p_dict, g_dict)
                slot_sum = sum(int(sc[k]) for k in ("quantity_ok", "value_ok", "construct_ok", "ligand_state_ok", "temperature_ok"))
                res_exact = int(g_res is not None and p_res is not None and p_res[1] == g_res[1])
                pv, gv = p_dict["value"], g_dict["value"]
                rel = abs(float(pv) - float(gv)) / max(abs(float(gv)), 1e-9) if isinstance(pv, (int, float)) and isinstance(gv, (int, float)) else 999.0
                if not sc["value_ok"] and not (sc["construct_ok"] and sc["ligand_state_ok"] and rel < 0.5):
                    continue
                cand_key = (int(sc["all_5_ok"]), res_exact, int(sc["value_ok"]), int(sc["construct_ok"]),
                            int(sc["ligand_state_ok"]), slot_sum, -rel)
                candidates.append((cand_key, gi, li, sc))

        candidates.sort(key=lambda x: x[0], reverse=True)
        used_gold: set[int] = set()
        used_live: set[int] = set()
        matched_by_gold: dict[int, tuple[int, dict[str, Any]]] = {}
        for _key, gi, li, sc in candidates:
            if gi in used_gold or li in used_live:
                continue
            used_gold.add(gi)
            used_live.add(li)
            matched_by_gold[gi] = (li, sc)

        scored_pairs: list[dict[str, Any]] = []
        unmatched_gold: list[dict[str, Any]] = []
        for gi, g in enumerate(same_doi_dyn):
            if gi in matched_by_gold:
                li, best_score = matched_by_gold[gi]
                p_dict, m = live_dicts[li]
                scored_pairs.append({
                    "gold_index": gi,
                    "live_row_id": m.row_id,
                    "quantity_canonical": g.role,
                    "gold_value": g.value,
                    "gold_unit": g.unit_raw,
                    "gold_residues": g.residues_raw,
                    "gold_locator": g.location,
                    "gold_construct": g.construct,
                    "gold_ligand": g.ligand,
                    "gold_temperature": g.temp_raw,
                    "live_value": p_dict["value"],
                    "live_unit": m.unit_raw,
                    "live_residues": m.residues_raw,
                    "live_locator": m.locator,
                    "live_construct": p_dict["sample_construct"],
                    "live_ligand": p_dict["ligand_state"],
                    "live_temperature": p_dict["temperature"],
                    "score": best_score,
                })
                total_matched += 1
                total_all5 += int(best_score["all_5_ok"])
                total_naive2 += int(best_score["two_tuple_naive_ok"])
                for k in ("quantity_ok", "value_ok", "construct_ok", "ligand_state_ok", "temperature_ok"):
                    slot_totals[k] += int(best_score[k])
                for rc in best_score["failure_reasons"]:
                    reason_totals[rc.split(":")[0]] += 1
            else:
                unmatched_gold.append({
                    "gold_index": gi,
                    "quantity": g.quantity,
                    "role": g.role,
                    "value": g.value,
                    "unit": g.unit_raw,
                    "residues": g.residues_raw,
                    "locator": g.location,
                    "source": g.source,
                })

        cross_doi_checks: list[dict[str, Any]] = []
        if not same_doi_gold and other_doi_gold:
            for g in [x for x in other_doi_gold if x.role == "kex"][:4]:
                g_dict = _to_score_dict_from_gold(g)
                kex_live = [(p_dict, m) for p_dict, m in live_dicts if m.quantity_canonical == "kex"]
                if kex_live:
                    p_dict, m = kex_live[0]
                    cross_doi_checks.append({
                        "live_doi": rec.doi,
                        "gold_doi": g.doi,
                        "live_row_id": m.row_id,
                        "gold_value": g.value,
                        "live_value": p_dict["value"],
                        "score": score_record(p_dict, g_dict),
                    })

        total_same_doi_gold += len(same_doi_gold)
        total_same_doi_gold_dyn += len(same_doi_dyn)
        n_p_matched = len(scored_pairs)
        n_p_all5 = sum(1 for x in scored_pairs if x["score"]["all_5_ok"])
        n_p_naive2 = sum(1 for x in scored_pairs if x["score"]["two_tuple_naive_ok"])
        per_paper.append({
            "entry": rec.entry,
            "doi": rec.doi,
            "n_live_total": len(rec.measurements),
            "n_live_primary": len(live_primary),
            "n_same_doi_gold_total": len(same_doi_gold),
            "n_same_doi_gold_dynamics": len(same_doi_dyn),
            "n_same_doi_gold_other_excluded": len(same_doi_gold) - len(same_doi_dyn),
            "n_other_doi_gold": len(other_doi_gold),
            "other_doi_gold_dois": sorted({g.doi for g in other_doi_gold}),
            "same_doi_gold_status": "SCORED" if same_doi_gold else "NO_SAME_DOI_GOLD_STANDARD",
            "n_matched_pairs": n_p_matched,
            "n_all_5_ok": n_p_all5,
            "n_two_tuple_naive_ok": n_p_naive2,
            "all_5_rate_on_matched": round(n_p_all5 / n_p_matched, 4) if n_p_matched else None,
            "slot_pass_counts": {
                k: sum(1 for x in scored_pairs if x["score"][k])
                for k in ("quantity_ok", "value_ok", "construct_ok", "ligand_state_ok", "temperature_ok")
            },
            "failure_reason_counts": dict(Counter(
                rc.split(":")[0] for x in scored_pairs for rc in x["score"]["failure_reasons"]
            )),
            "unmatched_gold_dynamics_count": len(unmatched_gold),
            "unmatched_gold_dynamics": unmatched_gold,
            "cross_doi_sanity_checks": cross_doi_checks,
            "scored_pairs": scored_pairs,
        })

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "scorer": "atlas_pipeline.compare.score_record (default strict tolerances: temp_tol_k=1.0, rel_tol=0.02)",
        "gold_sources": [str(DB_PATH), *(str(p) for p in F14_BATCHES)],
        "backend": backend,
        **auth_info,
        "summary": {
            "n_papers": len(records),
            "n_entries": len(entries),
            "n_live_measurements_total": sum(len(r.measurements) for r in records),
            "n_live_primary": sum(len(r.primary_measurements()) for r in records),
            "n_same_doi_gold_total": total_same_doi_gold,
            "n_same_doi_gold_dynamics": total_same_doi_gold_dyn,
            "n_matched_pairs": total_matched,
            "n_all_5_ok": total_all5,
            "n_two_tuple_naive_ok": total_naive2,
            "all_5_rate_on_matched": round(total_all5 / total_matched, 4) if total_matched else None,
            "two_tuple_rate_on_matched": round(total_naive2 / total_matched, 4) if total_matched else None,
            "slot_pass_counts": dict(slot_totals),
            "failure_reason_counts": dict(reason_totals),
        },
        "papers": per_paper,
    }


def cmd_validate(out: Path, record_path: Path | None = None) -> dict[str, Any]:
    from pydantic import ValidationError

    from .schema import MeasurementRow, PaperRecord, PhysicalValidationError, export_active_prompt

    prompt_path = export_active_prompt()
    probes = [  # (quantity, unit, measured_entity, quote) -> must be rejected / accepted
        ("NOE", "600 MHz", "unknown", "NOE 0.8"), ("R2", "ms", "unknown", "R2 12"), ("S2", "ns", "unknown", "S2 0.85"),
        ("pB", "%", "oligomer_or_association", "90% dimeric"), ("R2", "s-1", "unknown", "R2 12"), ("NOE", "", "unknown", "NOE 0.8"),
    ]
    results = []
    for q, unit, ent, quote in probes:
        val = next(t for t in quote.split() if t[0].isdigit()).rstrip("%")
        try:
            MeasurementRow(row_id="probe", sample_id="s1", quantity=q, value_raw=val, unit_raw=unit, source_role="this_study",
                           evidence_modality="text", measured_entity=ent, quote=quote)
            results.append({"quantity": q, "unit": unit, "accepted": True})
        except (ValidationError, PhysicalValidationError) as exc:
            results.append({"quantity": q, "unit": unit, "accepted": False, "error": str(exc).splitlines()[0][:160]})
    record_result = None
    if record_path:
        try:
            rec = PaperRecord.model_validate_json(Path(record_path).read_text(encoding="utf-8"))
            record_result = {"valid": True, "n_measurements": len(rec.measurements), "n_primary": len(rec.primary_measurements())}
        except (ValidationError, PhysicalValidationError, ValueError) as exc:
            record_result = {"valid": False, "error": str(exc)[:500]}
    payload = {"active_prompt": str(prompt_path), "pointer": (WORK / "config/active_prompt.txt").read_text(encoding="utf-8").strip(),
               "unit_probes": results, "record": record_result}
    _dump(payload, out / "validate_summary.json")
    return payload


def cmd_extract(
    out: Path,
    specs: list[dict[str, Any]] = LIVE_SPECS,
    *,
    docs: dict | None = None,
    backend: str = "auto",
    model: str | None = None,
    use_docling: bool = False,
    use_docling_si: bool = True,
    payloads_dir: Path | None = None,
) -> dict[str, Any]:
    from .extract import auth_status, extract_paper, load_and_ground_payload

    live_dir = out / "live_extractions"
    live_dir.mkdir(parents=True, exist_ok=True)
    if docs is None:
        docs = cmd_ingest(out, specs, use_docling=use_docling, use_docling_si=use_docling_si)["docs"]

    grouped: dict[tuple[str, str], dict[str, Any]] = {}
    for s in specs:
        doi_low = s["doi"].lower()
        key = (s["entry"], doi_low)
        grp = grouped.setdefault(key, {
            "entry": s["entry"], "doi": doi_low, "title": "", "roles": [],
            "record_stem": s.get("record_stem") or "", "extract_dynamics": s.get("extract_dynamics", True),
        })
        if s.get("title") and not grp["title"]:
            grp["title"] = s["title"]
        if s.get("record_stem") and not grp["record_stem"]:
            grp["record_stem"] = s["record_stem"]
        if s.get("extract_dynamics") is False:
            grp["extract_dynamics"] = False
        grp["roles"].append(s["document_role"])

    dois_per_entry: dict[str, int] = {}
    for entry, _doi in grouped:
        dois_per_entry[entry] = dois_per_entry.get(entry, 0) + 1

    auth = auth_status(check_cli=True)
    records, summaries = [], []
    pdir = payloads_dir or live_dir
    for (entry, doi), grp in grouped.items():
        if not grp["extract_dynamics"]:
            continue
        paper_docs = {
            role: docs[(doi, role)]
            for role in ("main_article", "supplement_si")
            if (doi, role) in docs and docs[(doi, role)].usable
        }
        if not paper_docs:
            continue
        stem = grp["record_stem"] or (entry if dois_per_entry[entry] == 1 else f"{entry}__{doi.replace('/', '_')}")
        if backend == "swarm_agent_direct":
            raw_path = pdir / f"{stem}_raw_payload.json"
            if not raw_path.is_file():
                raise FileNotFoundError(f"swarm_agent_direct payload not found: {raw_path}")
            res = load_and_ground_payload(
                entry, doi, grp["title"], raw_path, paper_docs,
                backend="swarm_agent_direct",
                model=model or "swarm_extractor_direct_read",
                auth=auth,
            )
        else:
            res = extract_paper(entry, doi, grp["title"], paper_docs, backend=backend, model=model)
        records.append(res.record)
        rec_path = live_dir / f"{stem}_record.json"
        rec_path.write_text(res.record.model_dump_json(indent=1, exclude_computed_fields=True), encoding="utf-8")
        rej_path = live_dir / f"{stem}_rejected.json"
        _dump({
            "entry": entry, "doi": doi, "record_stem": stem, "backend": res.backend, "model": res.model, **res.auth,
            "n_samples_rejected": len(res.rejected_samples),
            "n_measurements_rejected": len(res.rejected_rows),
            "rejected_samples": res.rejected_samples,
            "rejected_rows": res.rejected_rows,
        }, rej_path)
        summaries.append(res.summary() | {"record_stem": stem, "record_json": str(rec_path), "rejected_json": str(rej_path)})

    summary_payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "backend": summaries[0]["backend"] if summaries else backend,
        **auth,
        "n_papers": len(summaries),
        "n_entries": len({s["entry"] for s in summaries}),
        "totals": {
            "samples_accepted": sum(s["n_samples_accepted"] for s in summaries),
            "samples_rejected": sum(s["n_samples_rejected"] for s in summaries),
            "measurements_accepted": sum(s["n_measurements_accepted"] for s in summaries),
            "measurements_primary": sum(s["n_measurements_primary"] for s in summaries),
            "measurements_rejected": sum(s["n_measurements_rejected"] for s in summaries),
            "alternate_states": sum(s["n_alternate_states"] for s in summaries),
        },
        "papers": summaries,
    }
    _dump(summary_payload, live_dir / "extraction_summary.json")
    score_payload = score_live_extractions_all_batches(records, backend=summary_payload["backend"], auth=auth) if records else None
    if score_payload is not None:
        _dump(score_payload, live_dir / "live_5tuple_score.json")
        summary_payload["live_5tuple_score"] = score_payload["summary"] | {"json": str(live_dir / "live_5tuple_score.json")}
        _dump(summary_payload, live_dir / "extraction_summary.json")
    return {"records": records, "summary": summary_payload, "score": score_payload, "docs": docs}


def load_live_records(out: Path) -> list[Any]:
    from .schema import PaperRecord

    live_dir = out / "live_extractions"
    if not live_dir.is_dir():
        return []
    records = []
    for path in sorted(live_dir.glob("*_record.json")):
        records.append(PaperRecord.model_validate_json(path.read_text(encoding="utf-8")))
    return records


def cmd_compare(out: Path) -> dict[str, Any]:
    from .compare import write_outputs

    return write_outputs(out)


def cmd_cards(out: Path, compare_res: dict[str, Any] | None = None, manifest: dict[str, Any] | None = None,
              docs: dict | None = None, specs: list[dict[str, Any]] = LIVE_SPECS,
              records: list[Any] | None = None) -> dict[str, Any]:
    from .cards import f14_papers_read, write_cards
    from .compare import F14_BATCHES, rows_from_paper_record, run_recall_benchmark, write_outputs

    compare_res = compare_res or write_outputs(out)
    if manifest is None:
        mpath = out / "figures/figures_manifest.json"
        manifest = json.loads(mpath.read_text(encoding="utf-8")) if mpath.is_file() else None
    data = compare_res["data"]
    live_records = list(records) if records is not None else load_live_records(out)
    if live_records:
        existing_pairs = {(r.entry, r.doi.lower()) for r in data["rows"]}
        extra_rows = []
        for rec in live_records:
            if (rec.entry, rec.doi.lower()) not in existing_pairs:
                extra_rows.extend(rows_from_paper_record(rec, source="live_paper_record"))
        if extra_rows:
            data = {**data, "rows": list(data["rows"]) + extra_rows}
    bench_path = Path(compare_res["benchmark_json"])
    bench = json.loads(bench_path.read_text(encoding="utf-8")) if bench_path.is_file() else run_recall_benchmark(
        data["open_list"], data["curated"], data["rows"], data["observations"], data["label_sources"], data["warnings"])
    if docs is None:
        docs = cmd_ingest(out, specs)["docs"]
    return write_cards(out, data, compare_res["outcomes"], bench, manifest, texts_by_doi(docs), f14_papers_read(F14_BATCHES))


def cmd_store(
    out: Path,
    compare_res: dict[str, Any],
    manifest: dict[str, Any] | None,
    *,
    records: list[Any] | None = None,
    docs: dict | None = None,
) -> dict[str, Any]:
    from .schema import FigureAsset, PaperRecord
    from .store import write_store

    by_paper_figs: dict[tuple[str, str], list[FigureAsset]] = {}
    fields = set(FigureAsset.model_fields)
    for f in (manifest or {}).get("figures", []):
        by_paper_figs.setdefault((f["entry"], f["doi"].lower()), []).append(
            FigureAsset(**{k: v for k, v in f.items() if k in fields})
        )

    live_records = list(records) if records is not None else load_live_records(out)
    merged: dict[tuple[str, str], PaperRecord] = {}
    for rec in live_records:
        key = (rec.entry, rec.doi.lower())
        figs = by_paper_figs.get(key) or list(rec.figures)
        merged[key] = rec.model_copy(update={"figures": figs})
    for key, figs in sorted(by_paper_figs.items()):
        if key not in merged:
            e, d = key
            merged[key] = PaperRecord(
                entry=e, doi=d, figures=figs,
                notes="figure inventory only; measurements stay in the expert-review SQLite",
            )
    final_records = [merged[k] for k in sorted(merged)]
    texts = texts_by_doi(docs) if docs is not None else None
    res = write_store(out / "atlas_pipeline_run.sqlite", final_records, texts_by_doi=texts, comparisons=compare_res["outcomes"])
    res["datasette_command"] = " ".join(adapters.datasette_command(Path(res["db_path"])))
    return res


def cmd_e2e(
    out: Path,
    specs: list[dict[str, Any]] = LIVE_SPECS,
    *,
    use_docling: bool = False,
    use_docling_si: bool | None = None,
    run_extract: bool = False,
    extract_backend: str = "auto",
    payloads_dir: Path | None = None,
    reuse_figures_manifest: bool = False,
    extra_figures_manifests: list[Path] | None = None,
) -> dict[str, Any]:
    out.mkdir(parents=True, exist_ok=True)
    existing_live = load_live_records(out)
    si_docling = bool(run_extract or existing_live) if use_docling_si is None else bool(use_docling_si)
    ing = cmd_ingest(out, specs, use_docling=use_docling, use_docling_si=si_docling)
    mpath = out / "figures/figures_manifest.json"
    if reuse_figures_manifest and mpath.is_file():
        manifest = json.loads(mpath.read_text(encoding="utf-8"))
        extras = [json.loads(Path(p).read_text(encoding="utf-8")) for p in (extra_figures_manifests or []) if Path(p).is_file()]
        if extras:
            manifest = merge_figure_manifests(manifest, *extras)
            mpath.write_text(json.dumps(manifest, indent=2, default=str), encoding="utf-8")
    else:
        manifest = cmd_figures(out, specs)
    val = cmd_validate(out)
    ext_summary = None
    ext_records = None
    if run_extract:
        ext = cmd_extract(out, specs, docs=ing["docs"], backend=extract_backend, payloads_dir=payloads_dir)
        ext_records = ext["records"]
        ext_summary = ext["summary"]
    elif (out / "live_extractions/extraction_summary.json").is_file():
        ext_summary = json.loads((out / "live_extractions/extraction_summary.json").read_text(encoding="utf-8"))
    cmp_res = cmd_compare(out)
    store = cmd_store(out, cmp_res, manifest, records=ext_records, docs=ing["docs"])
    cards = cmd_cards(out, cmp_res, manifest, ing["docs"], specs=specs, records=ext_records)
    summary: dict[str, Any] = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "adapters": adapters.adapter_status(),
        "ingest": [{k: d[k] for k in ("entry", "document_role", "reader", "identity_ok", "identity_reason", "n_chars", "n_tables")}
                   for d in ing["summary"]],
        "figures": manifest["summary"] | {"manifest": str(mpath)},
        "validate": {"active_prompt": val["active_prompt"], "pointer": val["pointer"],
                     "rejected": [p["quantity"] + "/" + p["unit"] for p in val["unit_probes"] if not p["accepted"]],
                     "accepted": [p["quantity"] + "/" + (p["unit"] or "blank") for p in val["unit_probes"] if p["accepted"]]},
        "compare": {k: cmp_res["summary"][k] for k in ("n_open_entries", "n_entries_with_outcomes", "n_outcomes", "by_status",
                                                        "five_tuple_self_test_passed")} | {"json": cmp_res["comparisons_json"],
                                                                                           "csv": cmp_res["comparisons_csv"]},
        "recall_benchmark": cmp_res["benchmark_summary"] | {"json": cmp_res["benchmark_json"]},
        "store": store,
        "cards": {k: cards[k] for k in ("html", "md", "json", "n_cards", "n_figure_previews", "entries_with_figure_previews")},
    }
    if ext_summary is not None:
        summary["live_extractions"] = {
            "backend": ext_summary.get("backend"),
            "anthropic_sdk_auth": ext_summary.get("anthropic_sdk_auth"),
            "claude_cli_auth": ext_summary.get("claude_cli_auth"),
            "n_papers": ext_summary.get("n_papers"),
            "n_entries": ext_summary.get("n_entries"),
            "totals": ext_summary.get("totals"),
            "summary_json": str(out / "live_extractions/extraction_summary.json"),
        }
    score_path = out / "live_extractions/live_5tuple_score.json"
    if score_path.is_file():
        sc = json.loads(score_path.read_text(encoding="utf-8"))
        summary["live_5tuple_score"] = sc.get("summary", {}) | {"json": str(score_path)}
    _dump(summary, out / "e2e_summary.json")
    return summary


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="atlas_pipeline")
    ap.add_argument("command", choices=["ingest", "figures", "validate", "extract", "compare", "cards", "e2e"])
    ap.add_argument("--out", type=Path, default=OUT_DEFAULT)
    ap.add_argument("--all-10", action="store_true", help="Use LIVE_SPECS_10 covering all 10/10 open RelaxDB-CPMG proteins")
    ap.add_argument("--record", type=Path, default=None, help="PaperRecord JSON to validate (validate command)")
    ap.add_argument("--docling", action="store_true", help="Enable Docling table extraction on all PDFs")
    ap.add_argument("--no-docling-si", action="store_true", help="Disable Docling table extraction on SI PDFs during extract")
    ap.add_argument("--backend", default="auto", choices=["auto", "anthropic_sdk", "claude_cli", "swarm_agent_direct"])
    ap.add_argument("--model", default=None)
    ap.add_argument("--payloads-dir", type=Path, default=None, help="Directory containing <STEM>_raw_payload.json for swarm_agent_direct")
    ap.add_argument("--run-extract", action="store_true", help="Run extraction step inside e2e")
    ap.add_argument("--reuse-figures", action="store_true", help="Reuse existing figures/figures_manifest.json in e2e")
    ap.add_argument("--extra-figures-manifest", type=Path, action="append", default=None,
                    help="Additional figures_manifest.json to merge with figures/figures_manifest.json when --reuse-figures is set")
    args = ap.parse_args(argv)
    out = args.out
    specs = LIVE_SPECS_10 if args.all_10 else LIVE_SPECS
    if args.command == "ingest":
        res = cmd_ingest(out, specs, use_docling=args.docling, use_docling_si=not args.no_docling_si)["summary"]
    elif args.command == "figures":
        res = cmd_figures(out, specs)["summary"]
    elif args.command == "validate":
        res = cmd_validate(out, args.record)
    elif args.command == "extract":
        res = cmd_extract(
            out,
            specs,
            backend=args.backend,
            model=args.model,
            use_docling=args.docling,
            use_docling_si=not args.no_docling_si,
            payloads_dir=args.payloads_dir,
        )["summary"]
    elif args.command == "compare":
        r = cmd_compare(out)
        res = {"summary": r["summary"], "benchmark_summary": r["benchmark_summary"]}
    elif args.command == "cards":
        res = {k: v for k, v in cmd_cards(out, specs=specs).items()}
    else:
        res = cmd_e2e(
            out,
            specs,
            use_docling=args.docling,
            use_docling_si=None if not args.no_docling_si else False,
            run_extract=args.run_extract,
            extract_backend=args.backend,
            payloads_dir=args.payloads_dir,
            reuse_figures_manifest=args.reuse_figures,
            extra_figures_manifests=args.extra_figures_manifest,
        )
    print(json.dumps(res, indent=1, ensure_ascii=False, default=str))
    if args.command == "validate" and isinstance(res, dict) and res.get("record") and not res["record"]["valid"]:
        return 1
    if args.command in {"compare", "e2e"}:
        passed = (res.get("summary") or res.get("compare") or {}).get("five_tuple_self_test_passed")
        if passed is not True:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
