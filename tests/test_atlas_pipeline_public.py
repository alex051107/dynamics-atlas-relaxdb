#!/usr/bin/env python3
"""Self-contained public regression suite for `atlas_pipeline` (zero local PDF or private file dependencies).

Run from repository root:
    python3 tests/test_atlas_pipeline_public.py
    python3 -O tests/test_atlas_pipeline_public.py
"""
from __future__ import annotations

import json
import sqlite3
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from atlas_pipeline.cards import render_html
from atlas_pipeline.compare import run_self_test
from atlas_pipeline.extract import build_batch_request, canonical_system_prompt, load_and_ground_payload
from atlas_pipeline.ingest import IngestedDocument
from atlas_pipeline.schema import (
    ACTIVE_PROMPT_PATH,
    SEALED_ENTRIES,
    SampleSpec,
    canonical_prompt_rules,
)
from atlas_pipeline.store import write_store


class CheckFailed(AssertionError):
    pass


def check(cond: bool, msg: str) -> None:
    if not cond:
        raise CheckFailed(msg)


def test_unified_prompt_and_active_file() -> None:
    rules = canonical_prompt_rules()
    sys_prompt = canonical_system_prompt()
    active_txt = ACTIVE_PROMPT_PATH.read_text(encoding="utf-8")
    check(rules in sys_prompt, "canonical_system_prompt diverged from canonical_prompt_rules")
    check("STATUS: PROPOSED 2026-11-26, default strict-abstain" in active_txt, "proposed rule status missing in ACTIVE_EXTRACTION_PROMPT.md")
    check("QualitativeObservation" in active_txt, "QualitativeObservation schema missing in ACTIVE_EXTRACTION_PROMPT.md")
    check("uniprot_accession" in active_txt, "sample-level uniprot_accession missing in ACTIVE_EXTRACTION_PROMPT.md")

    doc = IngestedDocument(
        doc_id="synth_prompt", path="synthetic.pdf", format="pdf", reader="synthetic", sha256="0" * 64,
        document_role="main_article", text="Synthetic text for batch prompt test.", identity_ok=True, identity_reason="synthetic",
    )
    req = build_batch_request("batch_1", "16392", "10.1073/pnas.2106473118", "TEM-1", {"main_article": doc})
    check(req["params"]["system"] == sys_prompt, "build_batch_request truncated or modified canonical_system_prompt")
    check("Proposed Rule P3" in req["params"]["system"], "Proposed Rule P3 missing from batch system prompt")


def test_sample_uniprot_validation() -> None:
    s_none = SampleSpec(sample_id="S0", uniprot_accession="  ", isoform_version=" ")
    check(s_none.uniprot_accession is None and s_none.isoform_version is None, f"blank fields did not normalize to None: {s_none}")
    s_ok = SampleSpec(sample_id="S1", uniprot_accession="P62593", isoform_version="P62593-1")
    check(s_ok.uniprot_accession == "P62593" and s_ok.isoform_version == "P62593-1", f"valid UniProt failed: {s_ok}")
    for bad in ("x", "unknown", "N/A", "not_a_uniprot"):
        rejected = False
        try:
            SampleSpec(sample_id="SBAD", uniprot_accession=bad)
        except Exception:
            rejected = True
        check(rejected, f"invalid UniProt placeholder {bad!r} was accepted")


def test_qualitative_cryptic_pocket_and_dimer_guard_e2e() -> None:
    doc = IngestedDocument(
        doc_id="synth_tem1_plexin", path="synthetic.pdf", format="pdf", reader="synthetic", sha256="1" * 64,
        document_role="main_article",
        text=(
            "The population of the excited state was determined to be 1.05 +/- 0.03% (kex = 98 +/- 6 s-1) "
            "around the Omega-loop pocket (L169, N170). Since approximately 90% of the protein is in its dimeric state, "
            "T83 showed Rex = 7.0 s-1. Flexible 80s loop opens transiently without a reported rate constant."
        ),
        identity_ok=True, identity_reason="synthetic",
    )
    raw = {
        "stance": "supports",
        "samples": [
            {"sample_id": "S1", "uniprot_accession": "P62593", "isoform_version": "P62593-1",
             "construct_label": "WT", "ligand_state": "apo", "temperature_raw": "25 C"}
        ],
        "measurements": [
            {"row_id": "M_DIMER_BLOCK", "sample_id": "S1", "quantity": "pB", "value_raw": "90", "unit_raw": "%",
             "measured_entity": "oligomer_or_association", "source_role": "this_study", "evidence_modality": "text",
             "document_role": "main_article", "quote": "Since approximately 90% of the protein is in its dimeric state"},
            {"row_id": "M_REX_KEEP", "sample_id": "S1", "quantity": "Rex", "value_raw": "7.0", "unit_raw": "s-1",
             "residues_raw": "T83", "measured_entity": "conformational_exchange", "source_role": "this_study",
             "evidence_modality": "text", "document_role": "main_article", "quote": "T83 showed Rex = 7.0 s-1"},
        ],
        "qualitative_observations": [
            {"obs_id": "Q1", "sample_id": "S1", "document_role": "main_article", "category": "cryptic_pocket",
             "evidence_level": "experimental", "residues_raw": "L169, N170",
             "summary": "Omega-loop pocket excited state observed by CEST", "locator": "Results",
             "quote": "around the Omega-loop pocket (L169, N170)"},
            {"obs_id": "Q2", "sample_id": "S1", "document_role": "main_article", "category": "dynamic_region",
             "evidence_level": "author_interpretation", "residues_raw": "80s loop",
             "summary": "Transient loop opening without printed rate", "locator": "Discussion",
             "quote": "Flexible 80s loop opens transiently without a reported rate constant."},
        ],
    }
    res = load_and_ground_payload(
        "16392", "10.1073/pnas.2106473118", "TEM-1", raw, {"main_article": doc},
        auth={"anthropic_sdk_auth": "TEST", "claude_cli_auth": "TEST"},
    )
    check([m.row_id for m in res.record.measurements] == ["M_REX_KEEP"], f"unexpected kept rows: {res.record.measurements}")
    check(len(res.rejected_rows) == 1 and "OLIGOMER_FRACTION_AS_POPULATION" in res.rejected_rows[0]["reason"],
          f"expected dimer fraction rejection: {res.rejected_rows}")
    check(len(res.record.qualitative_observations) == 2, f"expected 2 qualitative observations: {res.record.qualitative_observations}")

    with tempfile.TemporaryDirectory() as td:
        dbp = Path(td) / "public_e2e.sqlite"
        info = write_store(dbp, [res.record], {"10.1073/pnas.2106473118": {"main_article": doc.text}})
        check(info["integrity_check"] == "ok", f"integrity failed: {info}")
        check(info["row_counts"]["qualitative_observations"] == 2, f"wrong qualitative row count: {info}")
        con = sqlite3.connect(dbp)
        try:
            qrows = con.execute(
                "SELECT obs_id, category, evidence_level, grounding_ok FROM qualitative_observations ORDER BY obs_id"
            ).fetchall()
            srow = con.execute("SELECT uniprot_accession, isoform_version FROM samples").fetchone()
        finally:
            con.close()
        check(qrows == [("Q1", "cryptic_pocket", "experimental", 1), ("Q2", "dynamic_region", "author_interpretation", 1)],
              f"unexpected sqlite qualitative rows: {qrows}")
        check(srow == ("P62593", "P62593-1"), f"unexpected sqlite sample uniprot: {srow}")


def test_five_tuple_attribution_self_test() -> None:
    st = run_self_test()
    check(st["passed"], f"five-tuple self-test failed: {st}")


def test_public_safe_html_emits_no_inline_images() -> None:
    card = [{
        "entry": "TEST", "protein": "Synthetic Enzyme", "uniprot": "P62593", "twin_entries": [],
        "evidence_tier": "synthetic", "sequence_length": 100, "n_rows": 0, "rows_by_source": {},
        "dois": ["10.1000/synthetic"], "verbatim_span_counts": {},
        "q1": {"n_positive": 0, "n_positive_strict": 0, "positive_ranges": "", "label_class_counts": {},
               "label_source_dois": [], "recall_label_source": None, "recall_independent": None,
               "recall_provenance_unknown": None, "independent_agreement": None, "papers": []},
        "q2": {"n": 0, "band": "none"}, "q3": [],
        "q4": {"methods": [], "comparison_status_counts": {}, "comparisons": []},
        "q5": [], "n_figures_in_manifest": 1,
        "figures": [{
            "figure_id": "F1", "caption_label": "Fig 1", "caption": "Synthetic plot",
            "classification": "VECTOR_PLOT", "document_role": "main_article", "page": 1,
            "doi": "10.1000/synthetic", "permission": "UNKNOWN_RESTRICTED", "png_path": "crop.png",
            "thumb": "data:image/jpeg;base64,/9j/FAKEJPEG",
            "digitized_ok": [{"n_points": 4, "alignment": 1.0, "x_scale": "linear", "y_scale": "linear",
                              "overlay": "data:image/png;base64,FAKEPNG"}],
            "digitize_abstain": [],
        }],
        "s3_links": [],
    }]
    pub_html = render_html(card, {"generated_at": "2026-11-26", "label_alphabet_provenance": "synthetic"}, public_safe=True)
    check("data:image" not in pub_html, "public_safe=True HTML still contained embedded data:image URI")


def test_batch1_open_proteins_draft_hygiene() -> None:
    p = REPO / "data/batch1_open_proteins_draft.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    entries = data["entries"]
    check(len(entries) == 12, f"expected 12 Batch 1 entries, got {len(entries)}")
    names = [e["entry"].upper() for e in entries]
    check(len(names) == len(set(names)), "duplicate entries in batch1_open_proteins_draft.json")
    leaked = set(names) & SEALED_ENTRIES
    check(not leaked, f"sealed entries leaked into Batch 1 draft: {leaked}")
    for e in entries:
        check(e.get("uniprot_status") == "from_relaxdb_unverified_sequence", f"unverified status missing on {e}")


TESTS = [
    test_unified_prompt_and_active_file,
    test_sample_uniprot_validation,
    test_qualitative_cryptic_pocket_and_dimer_guard_e2e,
    test_five_tuple_attribution_self_test,
    test_public_safe_html_emits_no_inline_images,
    test_batch1_open_proteins_draft_hygiene,
]


def main() -> int:
    failed = 0
    for fn in TESTS:
        try:
            fn()
            print(f"PASS: {fn.__name__}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"FAIL: {fn.__name__} -> {exc}")
    print(f"\nSummary: {len(TESTS) - failed}/{len(TESTS)} passed, {failed} failed (python -O: {bool(sys.flags.optimize)}).")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
