# Dynamics Atlas

**Dynamics Atlas** is an open, sentence-grounded database of experimental protein conformational dynamics and structural states extracted from published literature, built for biophysicists and ensemble-modeling benchmarks.

> **Expert review checkpoint (`review/expert-check-20261119`).**  
> We have drafted literature extraction across `104` of `131` open RelaxDB entries (`752` full-text papers, `19,958` printed numbers, `794` named PDB states), while keeping all `42` completed protein pages from Release `0.1` intact. **Nothing in the new draft has been reviewed by an NMR expert yet.** Start with the reading path below so you can inspect one full paper, audit our four biggest uncertainties, and approve rules before we process the remaining papers.

---

## Start here (15-minute review path for Gina and Soojung)

1. **[`REVIEW_GUIDE.md`](REVIEW_GUIDE.md)** gives the exact questions we need you to judge, ranking our four uncertain protein cases from riskiest to clearest.
2. **[`atlas/walkthrough_ets1.md`](atlas/walkthrough_ets1.md)** walks through one complete paper from raw text to extracted table rows (murine Ets-1, *Biochemistry* 2016), including a defect we spotted in our own sample card.
3. **[`atlas/v3_previews/README.md`](atlas/v3_previews/README.md)** shows 4 worked protein syntheses (`FKBP12`, `GR / DBD82`, `CheA`, `TEM-1 & Barstar`) that translate raw spreadsheet rows back into scientist-readable summaries.
4. **[`methods/how_it_is_built.md`](methods/how_it_is_built.md)** and **[`methods/bugs_and_fixes.md`](methods/bugs_and_fixes.md)** show how our workflow fuses external literature-mining methods (Bindwell, Elicit, PaperQA/Kosmos) onto deterministic checks, and expose five real bugs found during audit.

---

## How the pipeline fits together

![Dynamics Atlas, unified 7-step literature pipeline](figures/pipeline_architecture.png)

Rather than writing custom prompts from scratch, our design merges verified components from recent curation work onto a strict verification spine described in detail in [`methods/how_it_is_built.md`](methods/how_it_is_built.md).

- **Bindwell per-paper rubrics (`KEY_FORMAT`).** Before grading any automated extraction, we wrote gold answer keys for four papers (`arginine kinase`, `CRABP2`, `p38 gamma`, `IscU`) and recovered `85 / 86` core rates and populations (`102 / 102` Table 1 cells matching publisher XML on arginine kinase).
- **Elicit cited-cell pattern + table linearization.** Every kept measurement carries sample metadata, section locator, and an exact substring quote (`771 / 771` pass), with PMC XML tables flattened line by line and checked so no table can be falsely skipped as empty.
- **Edison / PaperQA as search probe only, never source of truth.** Published Kosmos evaluations showed `57.9%` accuracy on synthesis statements, so external retrieval tools feed candidate DOIs into Step 1 only.
- **Release `0.1` synthesis & structure overlay.** Our October 21 pipeline (`42` proteins, apo/holo PDB ensembles on `10` CPMG proteins, raw BMRB cross-checks) provides the per-protein summary layer we are now reconnecting to the scaled extraction data.

---

## Honest status across the `131` open RelaxDB proteins

We split RelaxDB's `143` proteins into `131` open development entries and `12` held-out test entries (physically blocked from all reading scripts). Here is what is done today, and what is intentionally paused pending expert review.

| Metric | Count | Plain status |
|---|---:|---|
| Open proteins with full text read (`>= 1` paper) | `104 / 131` | `752` unique full-text DOIs read (`771` entry-paper records), yielding `19,958` raw rows |
| Open proteins with `>= 1` printed rate or population | `38 / 131` | `82` have at least one numeric row; `22` read with `0` printable numbers (`Gaps` recorded) |
| Proteins with named PDB states / dynamic regions | `78` / `92` | `794` state PDB entries and `515` author-named dynamic residue sets captured |
| Duplicate twins & true unread open entries | `4` twins, `23` unread | `4` covered via identical UniProt twins; `22` unread plus `1` ID bug (`5687` `'x'` collapse) |
| Paused unread full-text backlog | `244` DOIs + `336` Kosmos | `988` earlier-search DOIs unread in this draft (`244` full text); Kosmos ZIP not yet pulled |
| Expert NMR verification (`Step 7`) | `0 / 131` | Model checks and blind second-model spot-checks ran; **zero expert review yet** |

---

## Four concrete questions we need Gina to settle

1. **Domain vs full-length protein indexing (`DBD82`, `CHEA`).** When a RelaxDB entry names one domain (`DBD82`, `CHEAYBD`), should papers on another domain (`GR LBD`) stay separate or merge under canonical `UniProt` ID with a `domain` tag?
2. **Inclusion line outside solution NMR (`DBD82`, `FKBP`).** Should `MD` simulations, `100 K` crystal dual occupancies, live-cell `FCS` diffusion, and `EMSA` DNA off-rates leave the main measurement table or stay in a separate auxiliary tier?
3. **Sample-splitting rule (`BARSTAR`, `Ets-1`).** Confirm requiring separate sample blocks whenever solvent isotopic fraction (`~1.8% H2O` vs `90% H2O`), `pH/pD`, temperature, or ligand ratio changes within one paper.
4. **Separating bulk baseline arrays from exchange kinetics (`16392`).** Should per-residue `R1/R2/NOE/S2` lists sit in their own linked sheet so rare `kex / pB` exchange measurements and PDB states remain easy to inspect?

---

## Repository map

| Path | Contents | Status |
|---|---|---|
| [`REVIEW_GUIDE.md`](REVIEW_GUIDE.md) | 15-minute expert checklist and 4 ranked borderline decisions | New (19 Nov 2026) |
| [`atlas/walkthrough_ets1.md`](atlas/walkthrough_ets1.md) | End-to-end single-paper audit of murine Ets-1 (`doi:10.1021/acs.biochem.6b00460`) | New (19 Nov 2026) |
| [`atlas/v3_previews/`](atlas/v3_previews/README.md) | Four worked protein syntheses (`FKBP`, `DBD82`, `CHEA/CHEAYBD`, `16392 & BARSTAR`) | New (19 Nov 2026) |
| [`figures/`](figures/) | Four centered 2x-DPI architecture, walkthrough, bug, and statechart figures | New (19 Nov 2026) |
| [`methods/how_it_is_built.md`](methods/how_it_is_built.md) | Literature comparison (Bindwell, Elicit, PaperQA/Kosmos), 7-step map, and formal statechart | Updated (19 Nov 2026) |
| [`methods/bugs_and_fixes.md`](methods/bugs_and_fixes.md) | Five real audit failure modes, root causes, and planned validation tests | New (19 Nov 2026) |
| [`methods/changes_since_v01.md`](methods/changes_since_v01.md) | Timeline from Sept 29 / Oct 21 to Nov 19 and roadmap to Release `0.3` | New (19 Nov 2026) |
| [`methods/quality.md`](methods/quality.md) | Full batch metrics, answer-key scores, blind checks, and prevalence caveats | Updated (19 Nov 2026) |
| [`data/v3_draft_20261118/`](data/v3_draft_20261118/README.md) | Nine-tab Excel workbook (`19,958` rows), `proteins_summary.csv`, `coverage_gap_audit.csv` | Draft (18 Nov 2026) |
| [`atlas/README.md`](atlas/README.md) & [`atlas/proteins/`](atlas/README.md) | **Release `0.1` (`21 Oct 2026`).** `42` alternate APO synthesis pages (`13 yes, 18 possible, 11 unknown`) | Preserved intact |
| [`data/*.csv`, `data/structures/`](data/DATA_DICTIONARY.md) | **Release `0.1` (`21 Oct 2026`).** Slice 1 tables, RelaxDB data issues, `10` CPMG structure overlays | Preserved intact |
| [`code/`](code/README.md) | **Release `0.1` (`21 Oct 2026`).** Alternate APO pipeline scripts (November extraction scripts live in the external run ledger) | Unchanged |
| [`CHANGELOG.md`](CHANGELOG.md) | Release log across `0.0`, `0.1`, and `0.2-draft` | Updated (19 Nov 2026) |

This repository never stores copyrighted full texts, private keys, or the `12` held-out test ground truths.
