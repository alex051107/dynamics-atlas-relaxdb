# Changelog

## 0.2.1-draft, 26 November 2026 (`update/post-anthropic-20261126`)

First-principles cleanup aligning the public repository with the post-Anthropic Batch 1 collaboration without altering `main` (`f8cde2f`) or the frozen review branch (`review/expert-check-20261119` @ `c39e120`):

- Added [`atlas_pipeline/`](atlas_pipeline/) as the single canonical Python contract and QC package (`schema.py`, `extract.py`, `ingest.py`, `figures.py`, `compare.py`, `store.py`, `cards.py`, `cli.py`, `adapters.py`, `ACTIVE_EXTRACTION_PROMPT.md`, and Jinja2 template) with zero local hardcoded paths, sample-level `uniprot_accession` / `isoform_version`, first-class `QualitativeObservation` (dynamic regions, alternate states, cryptic pockets with `evidence_level`), unified non-truncated system prompts across SDK/CLI/Batches, and `public_safe=True` HTML rendering stripping all embedded `data:image` URIs.
- Added [`tests/test_atlas_pipeline_public.py`](tests/test_atlas_pipeline_public.py) (`6 / 6` self-contained synthetic tests passing under both normal Python and `python3 -O`).
- Added [`PROPOSED_RULES_20261126.md`](PROPOSED_RULES_20261126.md) (`3` verbatim edge cases with proposed strict-abstain defaults awaiting expert sign-off) and [`ANTHROPIC_HANDOFF.md`](ANTHROPIC_HANDOFF.md) + [`data/batch1_open_proteins_draft.json`](data/batch1_open_proteins_draft.json) (`12` stratified open non-pilot entries).
- Refreshed [`README.md`](README.md), [`REVIEW_GUIDE.md`](REVIEW_GUIDE.md), and [`methods/check_review_consistency.py`](methods/check_review_consistency.py) to separate all four snapshot denominators honestly, recompute frozen SQLite counts live, demote raw BMRB and S3 link inventories to an appendix, and enforce zero `data:image` or local path leaks.

## 0.2-draft, 19 November 2026 (`review/expert-check-20261119`)

Expert-review checkpoint bridging the scaled November full-text extraction sweep (`104 / 131` open entries; `12` held-out entries excluded) back to readable protein syntheses and clear scope questions for Gina before running `v4`:

- Added [`REVIEW_GUIDE.md`](REVIEW_GUIDE.md) and [`atlas/walkthrough_ets1.md`](atlas/walkthrough_ets1.md): 15-minute expert checklist, full single-paper audit of murine Ets-1 (`doi:10.1021/acs.biochem.6b00460`, including blind-caught `14.8 ns` row and self-audited sample temperature note), and 4 ranked boundary decisions (`DBD82`, `FKBP`, `BARSTAR`, `CHEA/16392`).
- Added [`figures/`](figures/): four centered 2x-DPI figures covering the unified 7-step architecture ([`pipeline_architecture.png`](figures/pipeline_architecture.png)), Ets-1 walkthrough ([`single_paper_walkthrough.png`](figures/single_paper_walkthrough.png)), four audit bugs and fixes ([`known_bugs_and_fixes.png`](figures/known_bugs_and_fixes.png)), and the formal workflow state machine ([`formal_statechart.png`](figures/formal_statechart.png)).
- Added [`methods/bugs_and_fixes.md`](methods/bugs_and_fixes.md) and updated [`methods/how_it_is_built.md`](methods/how_it_is_built.md), [`methods/changes_since_v01.md`](methods/changes_since_v01.md), and [`methods/quality.md`](methods/quality.md) with external system comparisons (Bindwell, Elicit, FutureHouse PaperQA2/Kosmos, Asta, OpenScholar), formal TLA+/TLC verification (`methods/statechart/`), batch metrics (`771` records, `752` unique DOIs, `19,958` measurement rows), and known unclosed gaps (`988` unread Nov-12 DOIs including `244` full text, `336` Kosmos rows, `168` early un-reread records, `5687/50332` `'x'` collapse, `BARSTAR` condition conflation, and uncontrolled `method` labels).
- Built the complete **131-Protein Dynamics Atlas** ([`atlas/ATLAS_131.md`](atlas/ATLAS_131.md) + `131` individual protein pages in `atlas/all_proteins/`) unifying Release `0.1` (`42` expert-reviewed proteins), `v3` (`104` entries), and `2026-11-19` supplemental reads & bug fixes (`128 / 131` covered by full text / Release `0.1` / twin UniProt; only `3` paywalled BMRB dossiers).
- Fixed concrete data bugs in the review branch ([`supplemental_20261119.json`](data/v3_draft_20261118/supplemental_reads/supplemental_20261119.json), `55 / 55` verbatim quotes verified): split conflated `BARSTAR` (`10.1021/jacs.0c00807`) `S1` into `S1` (HyperW `pD 7`) + `S2` (CLEANEX `pH 7`); separated `5687` from `50332` and read `PMC263778` (`1P68`); read OA primary papers for `15451` (`2JUO`), `5841` (`1MZK`), `CMTIV`, and `7432` IscU (`PMC3258623`, `+8` ZZ-exchange/population rows); normalized all `85` raw `method` strings into `9` `method_group` buckets + `4` `row_tier` classes.
- Added [`atlas/v3_previews/`](atlas/v3_previews/README.md) (`FKBP`, `DBD82`, `CHEA/CHEAYBD`, `16392 & BARSTAR`) and [`data/v3_draft_20261118/`](data/v3_draft_20261118/README.md) (`RelaxDB_dynamics_from_papers_DRAFT_20261118.xlsx` upgraded to 10 tabs with formula-driven `Start_Here`, `Exchange_Highlights` [`575` rows], lossless `Measurements` [`19,989` rows], `release_01_call` & `audit_flag` on `Proteins`; plus synced `proteins_summary.csv` and `coverage_gap_audit.csv`).
- Preserved all `42` Release `0.1` alternate APO protein pages (`atlas/proteins/`), structure tables (`data/structures/`), and pipeline scripts (`code/`) untouched on `main`.

## 0.1 — 21 October 2026

First release organised as an atlas: one page for each protein, machine-readable tables and separate method pages.

- 42 proteins in slice 1 (alternate APO states): 13 yes, 18 possible, 11 unknown.
- We read 11 RelaxDB source papers in full. Before: 12 yes, 11 possible, 19 unknown.
  - Azurin moved to yes. The full text gives the sample: reduced Cu(I) azurin, pH 5.5, 41 °C. It also gives an EXSY rate of 45 ± 6 s⁻¹ for the His35 exchange.
  - Seven proteins moved from unknown to possible: RNase HI, calbindin D9k, thioredoxin, TGF-α, an anti-digoxin VL domain, the TTF-1 homeodomain and SilB.
  - VcPth moved to possible because of the single-field Rex rule, not new evidence.
- Deposited-structure comparison for all 10 CPMG proteins, with side chains and alternate conformers for CypA, RNase A and K-Ras.
- Pipeline fixes:
  - Rows that both readers cannot verify go to adjudication.
  - The worker receives the accessions with an identical sequence.
  - A failed re-read cannot inherit an old file.
  - The structure comparison detects fused peptides.

## 0.0 — 20 October 2026

First public push: the calls for 42 proteins, judgments, evidence rows, structure tables for 7 proteins and the pipeline code.
