# Expert Review Workbook (12 Tabs, Clickable Navigation)

Download the workbook directly from GitHub: **[`RelaxDB_expert_review_DRAFT.xlsx`](RelaxDB_expert_review_DRAFT.xlsx)** (3.7 MB).

This workbook reorganizes the frozen November 18 extraction baseline (`131` open RelaxDB entries, `771` entry-paper records, `752` distinct DOIs, `19,958 original` measurements; kept distinct from the `+ 31 = 19,989` November 19 supplemental branch rows) into a scientist-first, clickable Excel view. Every comparison row links via native Excel hyperlinks to its supporting observations, sample cards, and verbatim paper quotes. Independent expert trial reading by Gina is still pending.

## Sheet structure (12 tabs)

| Tab | Rows | Role |
|---|---:|---|
| `Start_Here` | Overview | One-page orientation, pilot jumps, and `physical_scope` definitions |
| `Protein_overview` | `131` | One row per open RelaxDB entry, separating direct evidence, same-UniProt twin leads, and unread entries, with clickable jumps to `Region_comparisons` |
| `Region_comparisons` | `109` | Question-driven comparisons (`Protein x Region x Window x Sample State`) with native hyperlinks to every listed observation |
| `Observations` | `396` | Atomic source-quoted evidence rows with explicit `physical_scope`, construct, buffer/T/pH/solvent conditions, `Samples` links, and DOI links |
| `Review_notes` | `9` | Documented issues, fixes applied, version boundary, and open expert rulings |
| `Measurements` | `19,958 original` | Lossless raw extraction table; leading-`=` quotes (`X3892`, `X11706`) restored as literal text (`0` formula cells) |
| `Samples` | `4,131 + 2` | Lossless raw sample cards plus `2` source-verified Barstar split cards (`S1_HyperW`, `S2_CLEANEX`) |
| `States` | `794` | Lossless raw conformational state PDB mappings |
| `Residue_sets` | `515` | Lossless raw author-named dynamic residue regions |
| `Papers` | `771` | Lossless raw per-paper audit summaries |
| `Gaps` | `944` | Lossless raw figure-only and missing-SI gaps |
| `Second_reader_only` | `35` | Lossless raw blind second-reader candidates |

## Six source-verified pilot and control walkthroughs (top rows of `Region_comparisons`)

1. **BARSTAR (`CMP_BARSTAR_01..02`)**: Separates HyperW NMR (`~1.8% H2O` in `D2O`, `pD 7`, `S1_HyperW`) from lyophilized and reconstituted CLEANEX-PM (`90% H2O`, `pH 7`, `S2_CLEANEX`) at `50 °C` while leaving the original raw `S1` row untouched.
2. **FKBP12 (`CMP_FKBP_01..03`)**: Separates `25 °C` WT NMR `Trp59` reorientation (`20%` NOE admixture, `tau_e = 1.5 ns`, `S2 = 0.63`) from `100 K` `C22V/G89P` crystal `4N19` (`0.29 / 0.71`, `crystal`) and CHARMM27 MD (`7.9%` WT / `59.6%` `V101I`, `simulation`), and labels the same-lab `80s`-loop `Gly89` series (`12%` WT / `67%` `G89A`, `C22V` ZZ-exchange) as `Single_lab_linked_series` (`n = 1` lab lineage).
3. **PLEXINB1 (`CMP_PLEXINB1_01..02`)**: Moves the `approximately 90%` dimer fraction (`10.1021/jp310142f`) out of conformational exchange into `association` while keeping `T83` `Rex = 7.0 s-1` in `solution_conformational_exchange`.
4. **TEM-1 / `16392` (`CMP_16392_01`)**: Positive control retaining genuine relaxation-dispersion values (`pB = 1.05%`, `kex = 98 s-1`) in `solution_conformational_exchange`.
5. **DmsD / `18257` & Murine vWFA2 / `50020` (`CMP_18257_01`, `CMP_50020_01`)**: Zero-numeric qualitative controls showing how entries with `0` printed numbers (`Fig. 1b` / `Fig. 2F` figure-only) still trace verified dynamic regions (`63` doubled peaks near helix 5 in DmsD; `N1133`/`T1208` ps-ns loop flexibility in vWFA2) back to source papers.

## Audit fixes verified before upload

- **Physical-scope cleanup (`396` observations)**: `solution_conformational_exchange` (`201`), `other_experimental` (`110`), `unresolved` (`30`), `association` (`28`, including `20` binding/unbinding and monomer-dimer kinetics rows moved out of exchange across `51416`, `50233`, `27888`, `CHEA`/`CHEAYBD`, `CSPA`, `CYPA_CPMG`, and `HTPDZ`), `simulation` (`20`), `crystal` (`7`).
- **No unverified multi-source claims**: `0` unverified rows claim `Direct_multi_source_support`; multi-DOI rows awaiting full PDF independence checks are tagged `Multi_DOI_pending_independence_audit` (`8`), and same-lab series are tagged `Single_lab_linked_series` (`2`).
- **Lossless export and determinism**: All `7` raw sheets preserve `100%` of original baseline rows (`0` missing/changed), leading-`=` quotes survive both `openpyxl` and LibreOffice Calc roundtrips as literal strings, and rebuilding twice from the same inputs produces `0` cell or hyperlink differences.
