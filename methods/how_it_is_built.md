# How the atlas is built

Dynamics Atlas aims to answer one practical question from published structural biology and biophysics literature, framed with our collaborators on September 29 and October 22, 2026: **for each protein, does experiment show conformational dynamics or alternate states, on what timescale, in which residues, under what exact sample conditions, and how does that connect to PDB structures and deposited BMRB data?**

Rather than inventing an isolated workflow, our design builds directly on published literature-curation research and team discussions, combining **Bindwell's per-paper rubric**, **Elicit's cited table structure**, **deterministic verification gates around every LLM call**, and **expert NMR review**.

![Dynamics Atlas, unified 7-step literature pipeline](../figures/pipeline_architecture.png)

---

## 1. How other teams extract from papers, and what we fused

Before scaling beyond our 10-protein pilot, we surveyed curation benchmarks and production literature-mining tools so we would reuse verified patterns instead of building ad hoc prompts.

| External system or study | Core idea & published evidence | What we adopted vs rejected | How it maps to our files |
|---|---|---|---|
| **Bindwell** (*The Bitter Lesson for Biology*, shared by Soojung) | Write a gold `rubric.json` for each paper first ("what a perfect extraction contains"), extract one printed value per row, and benchmark model/cost pairs (`Figure 12` & `13`) against the key rather than trusting intuition. | **Adopted** per-paper rubric scoring (`KEY_FORMAT`), one-value-per-row extraction, and cost-accuracy benchmarking (`Haiku` `74/86` vs `Sonnet` `85/86` on 4 keys; `102/102` arginine kinase Table 1 cells vs PMC XML). **Rejected** copying Bindwell's binding-affinity Haiku tier blindly, since NMR dynamics requires separating fitted exchange rates from bulk relaxation arrays and prior citations. | `data/v3_draft_20261118/` workbook (`Measurements`, `Samples`, `Gaps`), `methods/quality.md` |
| **Elicit systematic review** | Split the job into screening then structured extraction, backing every cell with a supporting quote and letting humans override any row. | **Adopted** strict screen-before-read splitting (`Step 2` -> `Step 3`) and cell-level quote provenance. **Extended** with sample-condition separation audits because verbatim quotes alone do not stop a model from attaching a number to the wrong experimental condition (`arXiv:2609.15964`). | `code/tools/screen_candidates.py`, `methods/bugs_and_fixes.md` |
| **PaperQA2/3 (Edison Literature) & Kosmos** (FutureHouse) | Retrieval-augmented QA over full texts (`PaperQA2`: `85.2%` precision / `66.0%` accuracy on LitQA2) and shared-world-model discovery (`Kosmos`: expert scientists judged `79.4%` accurate overall, `82.1%` literature, **`57.9%` synthesis/interpretation**, noting over-claiming and stochastic non-convergence). | **Adopted** Edison Literature strictly as an upstream **candidate-DOI discovery probe** (`Step 1`), alongside OpenAlex, BMRB, PDB, and Europe PMC. **Rejected** letting free-text agent synthesis write database claims or evidence tables directly without per-paper extraction and deterministic checks. | Candidate pool (`11,682` citations) and undownloaded Kosmos bundle (`336` rows) queued behind `Step 7` |
| **Ai2 Asta & OpenScholar** (*Nature* 2026) | Citation-grounded literature summaries. OpenScholar authors emphasize synthesis cannot be fully automated; Asta exhibited unstable reference lists across repeat runs (`arXiv:2606.08301`, surveyed Oct 13/20). | Confirms keeping candidate discovery deterministic and auditable, and reserving protein-level interpretation (`Step 5`) as a dedicated synthesis stage checked by independent readers and human experts (`Step 7`). | `atlas/README.md` (`42` Release `0.1` syntheses) and `atlas/v3_previews/` |
| **WASP 2025, PubMed 39399004, PubTator 3.0 & Wood et al. 2026** | Linearizing tables line-by-line boosted F1 (`67.9%` vs `56.7%`); dual-LLM concordance gave `0.94` accuracy vs `0.41–0.50` on discordant cells; canonical database IDs curb hallucinations; human-in-the-loop sign-off remains consensus (*Bioinformatics Advances* 2026). Errors concentrate in condition binding (`arXiv:2512.10004`, `arXiv:2604.07584`). | **Adopted** row-by-row PMC XML table serialization (`table` lines kept intact), empty-table blocker checks, cross-family blind checks (Claude / GPT / Gemini), UniProt sequence-identity verification, and explicit Gina sign-off before release. **Exposed** where condition binding (`Bug 1`) and uncontrolled method vocabularies (`Bug 3`) still need hard code gates. | [`bugs_and_fixes.md`](bugs_and_fixes.md), [`quality.md`](quality.md) |

---

## 2. Our unified 7-step architecture (and where we stand today)

On October 13 we designed a 7-step deterministic pipeline (`Astra` architecture review) that keeps models inside bounded, schema-checked steps while Python scripts control state, integrity, and release gates. Release `0.1` (`21 October 2026`) implemented the whole loop on `42` proteins. In November, we upgraded `Step 3` using the Bindwell per-paper schema across `104` open entries (`752` papers), **which left `Steps 5–6` temporarily disconnected from the new `19,958`-row table**. Reconnecting them after Gina's review is the purpose of this checkpoint.

| Step | What happens | Fixed rule (code) vs model judgment | Current status (19 Nov 2026) |
|---|---|---|---|
| **1. Discover & verify identity** | Pool citations from seed papers, OpenAlex, BMRB, PDB, Europe PMC, and Edison. Verify `UniProt` accession matches entry sequence; exclude `12` held-out test entries. | Fixed code enforces `12`-entry split and identity checks; curator fixes card errors (`HGMCSF` is G-CSF, `5991` is murine Ets-1). | **Built.** `11,682` candidates pooled; twin-entry deduplication & `'x'` placeholder guard needed (`Bug 2`). |
| **2. Screen full candidate pool** | Backfill missing abstracts (`Europe PMC`, `Crossref`, `OpenAlex`); classify `A/B/C/X` from title & abstract; map DOIs in code. | Model assigns tier under fixed prompt; Python handles backfill, index/DOI normalization, and missing-decision failure. | **Built** in Release `0.1` code (`code/tools/screen_candidates.py`), not yet applied before all November reads. |
| **3. Extract per paper into fixed schema** | Read one full text at a time into `samples`, `methods`, `expected_rows` (`1` value/row + quote), `expected_states` (PDBs), `expected_residue_sets`, and `out_of_reach` (`Gaps`). | Prompt sets NMR/dynamics scope; borderline non-NMR methods and condition grouping currently involve model judgment. | **Built for `752` unique DOIs (`771` records, `19,958` rows).** `23` open entries, `988` earlier DOIs (`244` full text), & `336` Kosmos rows wait on Step 7. |
| **4. Verify against paper text + blind audit** | Check every quote substring (`char-for-char`), value-inside-quote, non-empty table bodies, and spot-check blind with a second model family (`GPT`, `Claude Haiku/Sonnet`). | Deterministic text checks (`771/771` pass); human curator adjudicates blind disagreements. | **Partial (`Gap 1`).** Misses sample-condition conflation (`BARSTAR`) and lacks closed `method` enum (`Bug 1`, `Bug 3`). |
| **5. Synthesize by protein, region & condition** | Collapse raw rows into protein pages answering where it moves, timescale, populations, conflicts, detection windows, and buffer artefacts. | Fixed aggregation script groups verified rows; synthesis reviewer verifies biological reading against quotes. | **Done for `42` in `0.1`; `4` worked previews built (`FKBP`, `DBD82`, `CHEA`, `16392/BARSTAR`) to reconnect `v3` rows.** |
| **6. Anchor to PDB structures & raw BMRB** | Superpose apo/holo PDB ensembles (`Cα`, side-chain rotamers, `altlocs`, fused ligands) and cross-check literature relaxation rates against raw BMRB tables. | Deterministic structural alignment & BMRB parsers (`data/structures/`, `data/relaxdb_data_issues.md`). | **Done for `10` CPMG in `0.1`; not yet extended to remaining `131` entries.** |
| **7. Expert NMR review & sign-off** | Gina checks 1 complete paper ([`walkthrough_ets1.md`](../atlas/walkthrough_ets1.md)) and 4 uncertain boundaries ([`REVIEW_GUIDE.md`](../REVIEW_GUIDE.md)) before scaling `v4`. | Human expert owns domain definitions, method inclusion, and condition-splitting rules. | **Not done (`Gap 2`).** Blocking next sweep on purpose. |

---

## 3. Formal verification of the current workflow

To make remaining risks unmistakable before expert review, we modeled the November extraction workflow in TLA+ ([`WorkflowV3.tla`](statechart/WorkflowV3.tla)) and exhaustively model-checked all `23` reachable states and `37` transitions.

![Formally checked workflow state machine](../figures/formal_statechart.png)

- **Three properties proved across all `23` states.** `TypeOK` (all state variables remain well-typed), `NoSealedEntryRead` (`12` held-out entries never leave blocked state), and `OnlyQuoteCheckedInWorkbook` (only quote-verified rows enter the workbook).
- **Two expected gaps proved reachable.** `NoUncheckedConditionBinding` fails in `5` steps (the draft `.xlsx` can be built without checking whether solvent or stoichiometry matches each method, as seen in Barstar), and `NoReleaseWithoutExpertAndCoverage` fails in `6` steps (`988` earlier DOIs, `336` Kosmos rows, `168` early un-reread records, and `0` expert sign-off remain open). Exact counterexample traces are in [`statechart/stories.md`](statechart/stories.md).

---

## 4. Historical baseline: Release `0.1` (`21 October 2026`, `code/tools/`)

All scripts in [`code/tools/`](../code/tools/) implement the original `42`-protein **Release `0.1`** alternate APO pipeline (`13 yes`, `18 possible`, `11 unknown`), preserved intact alongside [`atlas/proteins/`](../atlas/README.md):

1. **Identity check.** Verified RelaxDB UniProt accession against entry sequence (`5` of `133` cards flagged).
2. **Four-channel search & screen.** Citation graph, BMRB, PDB primary citations, Europe PMC -> `A/B/C/X` abstract screen (`Always read source paper`).
3. **Read, dual re-read, adjudicate & judgment.** Codex read -> independent Codex + Claude re-reads -> adjudication on flagged or unverifiable rows -> judgment claim per `(protein, region, time window, condition)` under [`definitions.md`](definitions.md).
4. **Structures.** Superposed rigid cores across all downloaded PDB chains for the `10` CPMG entries (plus side-chain rotamers, `altlocs`, fused-peptide checks, and PDBe-KB comparison for CypA, RNase A, and K-Ras), stored in [`data/structures/`](../data/structures/).
