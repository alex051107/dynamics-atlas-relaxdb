# Dynamics Atlas

**Dynamics Atlas** is an open, quote-grounded database of experimental protein conformational dynamics and structural states extracted from published literature. It is built for biophysicists and ensemble-modeling benchmarks.

> **Unified 131-Protein Atlas checkpoint (`review/expert-check-20261119`).**  
> Every open RelaxDB entry (`131 / 131`; `12` held-out benchmark entries remain excluded) now has a dedicated protein page in **[`atlas/ATLAS_131.md`](atlas/ATLAS_131.md)**. The atlas unifies Release `0.1` (`42` expert-reviewed pages), `v3` full-text extraction (`104` entries), and our `2026-11-19` bug fixes and open-access reads (`15451`, `5841`, `5687`, `CMTIV`, `7432`, and `BARSTAR` sample splitting). Coverage now stands at **`128 / 131` (`97.7%`)** via full text, Release `0.1`, or twin-UniProt links. Only **`3`** entries (`15795`, `18477`, `50734`) sit behind publisher paywalls with their DOIs and abstracts logged. All `v3` rows await NMR specialist sign-off before promotion to Release `0.2`.

---

## Current state at a glance

```mermaid
stateDiagram-v2
    [*] --> OpenPool: 143 RelaxDB proteins split
    OpenPool --> HeldOut: 12 entries blocked physically
    OpenPool --> UnifiedDraft: 131 open entries

    state UnifiedDraft {
        [*] --> DataFixed
        DataFixed: Concrete data bugs fixed (19 Nov)
        DataFixed: BARSTAR S1/S2 split, 5687 fixed, 9 method groups
        DataFixed --> Covered128: 128/131 covered (full text, R0.1, or twin)
        DataFixed --> Paywalled3: 3/131 paywalled BMRB dossiers logged
        Covered128 --> AtlasBuilt: 131 protein pages in ATLAS_131.md
        Paywalled3 --> AtlasBuilt
    }

    UnifiedDraft --> ExpertGate: Waiting on Gina (4 boundary rules)
    ExpertGate --> V4Sweep: Rules locked in schema
    V4Sweep --> Release02: Close 3 paywalled + 336 Kosmos + 168 early re-reads
```

---

## Start here (15-minute review path for Gina and Soojung)

1. **[`atlas/ATLAS_131.md`](atlas/ATLAS_131.md)** opens the complete **131-Protein Dynamics Atlas**. Entries are grouped into 4 evidence tiers with MD and cryo-X-ray separated from solution exchange.
2. **[`REVIEW_GUIDE.md`](REVIEW_GUIDE.md)** lists the 4 borderline scientific rules we need Gina to settle before running `v4`.
3. **[`atlas/walkthrough_ets1.md`](atlas/walkthrough_ets1.md)** walks through one full paper from raw text to extracted rows (murine Ets-1, *Biochemistry* 2016).
4. **[`atlas/v3_previews/README.md`](atlas/v3_previews/README.md)** shows 4 deep worked protein syntheses (`FKBP12`, `GR / DBD82`, `CheA`, `TEM-1 & Barstar`) illustrating those 4 rules.
5. **[`methods/how_it_is_built.md`](methods/how_it_is_built.md)** and **[`methods/bugs_and_fixes.md`](methods/bugs_and_fixes.md)** explain our 7-step architecture, compare external curation tools, and separate bugs **already fixed** from `v4` schema gates.

---

## How the pipeline fits together

![Dynamics Atlas, unified 7-step literature pipeline](figures/pipeline_architecture.png)

Our design merges verified curation patterns onto a deterministic verification spine. Full comparisons live in [`methods/how_it_is_built.md`](methods/how_it_is_built.md).

- **Bindwell per-paper rubrics (`KEY_FORMAT`).** We wrote gold answer keys for four papers (`arginine kinase`, `CRABP2`, `p38 gamma`, `IscU`) before grading extraction. The extractor recovered `85 / 86` core rates and populations (`102 / 102` Table 1 cells matching publisher XML on arginine kinase).
- **Elicit cited-cell pattern + table linearization.** Every kept measurement carries sample metadata, section locator, and a verbatim substring quote (`776 / 776` records pass). PMC XML tables are flattened line by line so no table can be skipped silently.
- **Edison / PaperQA as search probe only.** Published Kosmos evaluations showed `57.9%` accuracy on synthesis statements. External retrieval tools therefore feed candidate DOIs into Step 1 only and never write database rows directly.
- **Release `0.1` synthesis & structure overlay.** Our October 21 pipeline (`42` proteins, apo/holo PDB ensembles on `10` CPMG proteins, raw BMRB checks) is now reconnected to `v3` inside [`atlas/ATLAS_131.md`](atlas/ATLAS_131.md).

---

## Honest status across all `131` open RelaxDB proteins

RelaxDB holds `143` proteins. We block `12` held-out entries physically and report exact unified coverage across all `131` open entries below.

| Metric | Count | Plain status |
|---|---:|---|
| Open proteins with a Protein-Level Atlas page | `131 / 131` | [`atlas/ATLAS_131.md`](atlas/ATLAS_131.md) + `atlas/all_proteins/<entry>.md` unifying Release `0.1`, `v3`, and `2026-11-19` reads |
| Covered by full text, Release `0.1`, or twin UniProt | `128 / 131` | `108` with checked `v3`/supplemental papers (`757` unique DOIs, `19,989` rows) + `17` Release `0.1`-only + `3` twin UniProts |
| Atlas Tier 1 (experimental exchange rates or pops) | `42 / 131` | Solution NMR/HDX/EPR/FRET rates & pops (`575` rows on `Exchange_Highlights`) + Release `0.1` `yes` calls; MD/cryo-X-ray separated |
| Atlas Tier 2 (quantitative relaxation/HDX/DEER/FRET) | `57 / 131` | Includes newly read `15451` (`2JUO`, `τc`), `5841` (`1MZK`, `S2/τm/Rex`), and `CMTIV` (`abstract_only` `S2`) |
| Atlas Tier 3 (qualitative / Release `0.1` unknown / 0-row) | `29 / 131` | Includes newly read `5687` (`S-824`, PDB `1P68`, fixed from `'x'` bug) and `3` twin UniProt pointers |
| Atlas Tier 4 (paywalled BMRB source paper only) | `3 / 131` | `15795`, `18477`, `50734` (exact DOIs/PMIDs and BMRB/PubMed abstracts logged) |
| Remaining paused external backlog | `336` Kosmos + `168` early `v3` | `219` of the `244` Nov-12 full-text DOIs were already in Release `0.1`; IscU `PNAS 2011` (`7432`) added; Kosmos ZIP & early `168` re-reads paused |
| Expert NMR verification of `v3` rows (`Step 7`) | `42` R0.1 / `0` new `v3` | Release `0.1` (`42` proteins) had dual review; all `v3` rows await Gina's sign-off |

---

## Four scientific boundary rules we need Gina to settle

1. **Domain vs full-length protein indexing (`DBD82`, `CHEA`).** When a RelaxDB entry names one domain (`DBD82`, `CHEAYBD`), should papers on another domain (`GR LBD`) stay separate or merge under canonical `UniProt` ID with a `domain` tag?
2. **Inclusion line outside solution NMR (`DBD82`, `FKBP`).** Should `MD` simulations, `100 K` crystal dual occupancies, live-cell `FCS` diffusion, and `EMSA` DNA off-rates stay in a separate auxiliary tier rather than experimental exchange counts?
3. **Mandatory sample-splitting threshold (`BARSTAR`, `Ets-1`).** Confirm forcing a new `sample` ID whenever solvent isotopic fraction (`~1.8% H2O` vs `90% H2O`), `pH/pD`, temperature, or ligand ratio changes within one paper.
4. **Separating bulk relaxation arrays from exchange kinetics (`16392`).** Confirm keeping per-residue `R1/R2/NOE/S2` tables split from fitted `kex / pB` exchange tables (as previewed in `Exchange_Highlights` and `ATLAS_131.md`).

---

## Repository map

| Path | Contents | Status |
|---|---|---|
| [`atlas/ATLAS_131.md`](atlas/ATLAS_131.md) & `atlas/all_proteins/` | Complete **131-Protein Dynamics Atlas** (one page per open entry, unifying Release `0.1` + `v3` + `2026-11-19` reads) | New (19 Nov 2026) |
| [`REVIEW_GUIDE.md`](REVIEW_GUIDE.md) | 15-minute expert checklist, decision routing chart, and 4 ranked borderline calls | Updated (19 Nov 2026) |
| [`atlas/walkthrough_ets1.md`](atlas/walkthrough_ets1.md) | End-to-end single-paper audit of murine Ets-1 (`doi:10.1021/acs.biochem.6b00460`) | New (19 Nov 2026) |
| [`atlas/v3_previews/`](atlas/v3_previews/README.md) | Four deep worked protein syntheses (`FKBP`, `DBD82`, `CHEA/CHEAYBD`, `16392 & BARSTAR`) | New (19 Nov 2026) |
| [`figures/`](figures/) | Four centered 2x-DPI architecture, walkthrough, bug, and statechart figures | New (19 Nov 2026) |
| [`methods/how_it_is_built.md`](methods/how_it_is_built.md) | Literature comparison (Bindwell, Elicit, PaperQA/Kosmos), 7-step map, and formal statechart | Updated (19 Nov 2026) |
| [`methods/bugs_and_fixes.md`](methods/bugs_and_fixes.md) | Five real audit failure modes, fixes already applied in this branch, and `v4` schema gates | Updated (19 Nov 2026) |
| [`methods/changes_since_v01.md`](methods/changes_since_v01.md) | Timeline from Sept 29 / Oct 21 to Nov 19 and roadmap to Release `0.3` | Updated (19 Nov 2026) |
| [`methods/quality.md`](methods/quality.md) | Full batch metrics, answer-key scores, blind checks, and prevalence caveats | Updated (19 Nov 2026) |
| [`methods/check_review_consistency.py`](methods/check_review_consistency.py) | Deterministic gate checking counts, links, path leaks, sealed entries, Mermaid syntax, and prose clarity | New (19 Nov 2026) |
| [`data/v3_draft_20261118/`](data/v3_draft_20261118/README.md) | Ten-tab Excel workbook (`Start_Here`, `Proteins`, `Exchange_Highlights` [`575` rows], lossless `Measurements` [`19,989` rows]), `supplemental_reads/`, `proteins_summary.csv`, `coverage_gap_audit.csv` | Draft (updated 19 Nov 2026) |
| [`atlas/README.md`](atlas/README.md) & [`atlas/proteins/`](atlas/README.md) | **Release `0.1` (`21 Oct 2026`).** `42` alternate APO synthesis pages (`13 yes, 18 possible, 11 unknown`) | Preserved intact |
| [`data/*.csv`, `data/structures/`](data/DATA_DICTIONARY.md) | **Release `0.1` (`21 Oct 2026`).** Slice 1 tables, RelaxDB data issues, `10` CPMG structure overlays | Preserved intact |
| [`code/`](code/README.md) | **Release `0.1` (`21 Oct 2026`).** Alternate APO pipeline scripts | Unchanged |
| [`CHANGELOG.md`](CHANGELOG.md) | Release log across `0.0`, `0.1`, and `0.2-draft` | Updated (19 Nov 2026) |

This repository never stores copyrighted full texts, private keys, or the `12` held-out test ground truths.
