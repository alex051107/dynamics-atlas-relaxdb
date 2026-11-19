# Changes since Release 0.1 (`21 October -> 19 November 2026`)

This page traces how Dynamics Atlas moved from **Release 0.1** (hand-curated alternate APO synthesis on `42` proteins), through our October 22 meeting with Gina and Soojung and a November 12 wide candidate table, to the **November 19 expert-review branch (`review/expert-check-20261119`)**.

---

## 1. Chronology from collaborator meetings to today

| Milestone | Scope & artifact | What improved | What regressed or remained undone |
|---|---|---|---|
| **Sept 29 meeting & Slack notes** | Defined goal with Gina and Soojung (`10 CPMG -> 133 -> broader`), five required fields (residues, alternate states, experiments, timescale, % populations), and cross-method scope (CPMG/CEST, crystallography, FRET, EPR/DEER, MD). | Set clear scientist requirements and requested evidence + conflicts preserved per protein. | Left definition of alternate APO vs all-timescale dynamics open until pilot examples reached Gina. |
| **Release 0.1 (`21 Oct 2026`)** | `42` RelaxDB proteins (`10` CPMG + `32` others): [`atlas/proteins/`](../atlas/README.md) (`13 yes, 18 possible, 11 unknown`), `data/*.csv`, `data/structures/` (`10` CPMG PDB overlays), raw BMRB checks (`data/relaxdb_data_issues.md`). | Produced scientist-first verdicts per protein, dual re-reads + adjudication, and structural state comparisons. | Covered `42 / 131` open proteins; slow to scale across dense multi-paper entries. |
| **Oct 22 meeting & architecture / Bindwell survey** | Team agreed to split source-grounded observation extraction from reasoning (`Action items`), test NSF ACCESS open-weight budgets, and adapt Bindwell's per-paper `rubric.json` evaluation method. Surveys (`Oct 13–20`) compared Elicit, PaperQA2/3, Kosmos, OpenScholar, and Asta. | Established gold-key evaluation criteria, deterministic quote verification design, and Step-1-only isolation for external retrieval platforms. | Schema standardization and Gina's sign-off on the 10-protein examples still waited. |
| **Nov 12 draft table** *(external workspace)* | `127` entries, `1,437` DOIs, `3,977` evidence rows. | Broad candidate intake testing what open/citing literature reported dynamics. | Mixed `744` abstract-only DOIs with `full_text`; `988` of these DOIs (`244` full text) have not yet entered our strict extraction pass. |
| **Nov 18–19 expert checkpoint (`review/expert-check-20261119`)** | `104 / 131` open entries (`752` full-text DOIs, `771` records, `19,958` rows; `12` held-out entries excluded) plus `REVIEW_GUIDE.md`, `walkthrough_ets1.md`, `4` worked protein previews, `4` centered architecture/bug/statechart figures. | `85 / 86` core rates on 4 keyed papers (`102 / 102` Table 1 XML cells on arginine kinase); explicit `Gaps` (`944`) and `States` (`794`); honest exposure of 5 real bugs (`BARSTAR`, `CHEA`, `DBD82`, `16392`, coverage gaps). | Dropped per-protein synthesis at table scale (restored for 4 previews here); unchecked sample-condition binding (`Bug 1`); mid-run rule drift and `168` early un-reread records (`Bug 3`); `988` Nov-12 DOIs + `336` Kosmos rows + `23` unread entries still paused; **zero Gina review yet**. |

---

## 2. Summary of real gains vs regressions

### Gains we keep going into `v4`
1. **Per-paper answer-key calibration.** Against 4 manually verified paper keys (`arginine kinase`, `CRABP2`, `p38 gamma`, `IscU`), the extractor recovered `85 / 86` core rates and populations with `0` ungrounded numbers, matching `102 / 102` numeric Table 1 cells of arginine kinase against PMC XML.
2. **Explicit accounting of figure-only and SI gaps (`944` items).** Instead of quietly dropping unprintable plots, the `Gaps` tab names where missing data live (`Figures`, `BMRB`, unavailable SI).
3. **Hard test-set isolation.** All `12` held-out evaluation entries are physically blocked before staging (`NoSealedEntryRead` proved in `WorkflowV3.tla`).

### Regressions exposed and documented for Gina before scaling
1. **Per-protein synthesis and structure/BMRB anchoring fell behind Step 3.** Release `0.1` delivered biological syntheses and `PDB` structure comparisons (`data/structures/`). The November sweep stopped at raw spreadsheet rows (`19,958`), so a single SI table (`1,879` rows in TEM-1) hides `4` Ω-loop CEST rows.
2. **Sample-condition binding was not verified mechanically.** Substring checks cannot detect when two experiments (`BARSTAR` HyperW `~1.8% H2O` vs CLEANEX `90% H2O`) merge into one `sample` block (`Bug 1`).
3. **Uncontrolled schema and mid-run drift.** Duplicate RelaxDB IDs (`CHEA` vs `CHEAYBD`), `'x'` placeholder collapse (`5687` onto `50332`), uncontrolled `method` strings (`md_simulation` vs `molecular_dynamics`, `FRET` vs `fret`, 4 `DEER` labels), and `168` early un-reread records leave cross-entry counts uneven (`Bug 2`, `Bug 3`).

---

## 3. Four-step plan to Release `0.3` (after Gina's ruling)

We intentionally paused reading the remaining `244` full-text DOIs and downloading the `336` Kosmos rows until Gina resolves [`REVIEW_GUIDE.md`](../REVIEW_GUIDE.md). Once settled:

1. **Freeze `v4` contract and canonical IDs.** Index once per verified `UniProt` ID (preserving `domain` tags), close `method` and `scope` enums, enforce `1` condition per `sample` ID, and block placeholder `'x'`.
2. **Enforce condition-binding checks in code.** Apply mixed-solvent / temperature / stoichiometry cross-checks across **all** records (retroactively scanning `B1–B3` too) and verify with planted condition-swap tests.
3. **Close coverage debt with cheap triage first.** Filter clinical/imaging noise before full-text reading on the `244` unread full-text DOIs, download the `336`-row Kosmos package, re-run the `168` early records under the frozen contract, and reserve second-family reads for valued or borderline papers.
4. **Restore Step 5 and Step 6 across all open entries.** Separate `PerResidueRelaxation` from `ExchangeProcesses`, align numbering to UniProt, generate per-protein syntheses matching [`CYPA_CPMG.md`](../atlas/proteins/CYPA_CPMG.md), and reconnect PDB ensemble comparisons and raw BMRB checks.
