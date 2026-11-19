# Changelog

## 0.2-draft, 19 November 2026 (`review/expert-check-20261119`)

Expert-review checkpoint bridging the scaled November full-text extraction sweep (`104 / 131` open entries; `12` held-out entries excluded) back to readable protein syntheses and clear scope questions for Gina before running `v4`:

- Added [`REVIEW_GUIDE.md`](REVIEW_GUIDE.md) and [`atlas/walkthrough_ets1.md`](atlas/walkthrough_ets1.md): 15-minute expert checklist, full single-paper audit of murine Ets-1 (`doi:10.1021/acs.biochem.6b00460`, including blind-caught `14.8 ns` row and self-audited sample temperature note), and 4 ranked boundary decisions (`DBD82`, `FKBP`, `BARSTAR`, `CHEA/16392`).
- Added [`figures/`](figures/): four centered 2x-DPI figures covering the unified 7-step architecture ([`pipeline_architecture.png`](figures/pipeline_architecture.png)), Ets-1 walkthrough ([`single_paper_walkthrough.png`](figures/single_paper_walkthrough.png)), four audit bugs and fixes ([`known_bugs_and_fixes.png`](figures/known_bugs_and_fixes.png)), and the formal workflow state machine ([`formal_statechart.png`](figures/formal_statechart.png)).
- Added [`methods/bugs_and_fixes.md`](methods/bugs_and_fixes.md) and updated [`methods/how_it_is_built.md`](methods/how_it_is_built.md), [`methods/changes_since_v01.md`](methods/changes_since_v01.md), and [`methods/quality.md`](methods/quality.md) with external system comparisons (Bindwell, Elicit, FutureHouse PaperQA2/Kosmos, Asta, OpenScholar), formal TLA+/TLC verification (`methods/statechart/`), batch metrics (`771` records, `752` unique DOIs, `19,958` measurement rows), and known unclosed gaps (`988` unread Nov-12 DOIs including `244` full text, `336` Kosmos rows, `168` early un-reread records, `5687/50332` `'x'` collapse, `BARSTAR` condition conflation, and uncontrolled `method` labels).
- Added [`atlas/v3_previews/`](atlas/v3_previews/README.md) (`FKBP`, `DBD82`, `CHEA/CHEAYBD`, `16392 & BARSTAR`) and [`data/v3_draft_20261118/`](data/v3_draft_20261118/README.md) (`RelaxDB_dynamics_from_papers_DRAFT_20261118.xlsx`, `proteins_summary.csv`, `coverage_gap_audit.csv`).
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
