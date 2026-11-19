# v3 Paper Extraction Draft (`18–19 November 2026`)

Machine-readable summary CSVs and the ten-tab Excel workbook from the `v3` paper-by-paper extraction sweep across the **131 open RelaxDB entries** (`12` held-out entries excluded).

Use this folder alongside the **worked protein synthesis previews** in [`atlas/v3_previews/`](../../atlas/v3_previews/README.md) and the **workflow Statechart** in [`methods/how_it_is_built.md`](../../methods/how_it_is_built.md). Unlike Release `0.1` (`21 October 2026`), which published protein-level state calls (`yes / possible / unknown`) for `42` proteins, this `v3` artifact is an **uncurated paper-to-table aggregation**. It has not yet been filtered by an NMR expert or synthesized into per-protein calls.

## Files in this folder

| File | Contents | Rows |
|---|---|---|
| [`RelaxDB_dynamics_from_papers_DRAFT_20261118.xlsx`](RelaxDB_dynamics_from_papers_DRAFT_20261118.xlsx) | Review-ready ten-tab workbook unifying `771` `v3` records + `5` verified `2026-11-19` reads (`776` total; `757` unique DOIs) and Release `0.1` calls | `19,989` measurements + `575` exchange highlights across `10` tabs |
| [`proteins_summary.csv`](proteins_summary.csv) | Exact CSV export of the workbook `Proteins` tab (sorted by richness, with `status`, `release_01_call`, `audit_flag`, and fixed `5687` & `BARSTAR`) | `131` data rows |
| [`coverage_gap_audit.csv`](coverage_gap_audit.csv) | Transparent accounting of unified `128 / 131` coverage, `3` paywalled BMRB entries, reconciled Nov-12 DOIs (`219 / 244` in Release `0.1`), Kosmos (`336`), and `168` early records | `13` metrics |
| [`supplemental_reads/supplemental_20261119.json`](supplemental_reads/supplemental_20261119.json) | Quote-verified (`55 / 55`) JSON of the `BARSTAR` `S1`/`S2` bug fix, newly read OA papers (`15451`, `5841`, `5687`, `CMTIV`, `7432`), and `3` paywalled BMRB dossiers (`15795`, `18477`, `50734`) | `5` new papers + `1` sample fix + `3` dossiers |

## Workbook tabs (`RelaxDB_dynamics_from_papers_DRAFT_20261118.xlsx`)

| Tab | Rows (excl. header) | What one row represents | Why it is structured this way |
|---|---|---|---|
| `Start_Here` | Formula dashboard | Live Excel formulas (`COUNTA` / `COUNTIF` / `SUM`) for coverage, `method_group` totals, 5-minute reading path, and known caveats | Replaces raw internal batch notes with a live, self-checking landing sheet |
| `Proteins` | `131` | One RelaxDB open entry (mirrors `proteins_summary.csv`) | Sorted so the `38` entries with printed exchange rates/populations appear at the top; adds `status` badges and `audit_flag` callouts; fixes the false `5687 -> 50332` `'x'` collapse |
| `Exchange_Highlights` | `567` | Filtered view of `Measurements` isolating `kex`, `kAB`, `kBA`, `kopen`, `kclose`, `k12`, `kct`, `pB`, `population`, `delta_omega`, `tau_ex`, and `phi_ex` across `38` proteins | Lets NMR experts scan conformational exchange in minutes without scrolling past `16,000+` bulk `R1/R2/NOE` rows; soft amber tint flags `MD`, `X-ray/Cryo-EM`, `Biophysics`, and `homolog` rows |
| `Measurements` | `19,958` | Lossless table of every printed dynamics number, range, or bound extracted from paper text, tables, or figure captions | Adds two controlled filter columns (`method_group` mapping all `85` raw method strings into `9` buckets, plus `row_tier`) while keeping every original column and clickable DOI intact |
| `States` | `794` | One author-named conformational or complex PDB state tied to the entry protein (or labeled `homolog`) | Clickable DOI links, `PDB`, `state`, `location in paper`, `quote` |
| `Residue_sets` | `515` | One author-named dynamic, exchange-broadened, flexible, or protected residue region without requiring printed rates | Clickable DOI links, `process`, `residues`, `sample`, `location in paper`, `quote` |
| `Samples` | `4,131` | One experimental or simulation condition block referenced by `Measurements` and `Residue_sets` via `sample` ID | `protein`, `construct`, `species relation`, `ligand state`, `temperature`, `pH`, `buffer`, `field (MHz)`, `same as deposit`, `note`, `quote` |
| `Papers` | `771` | One `(entry, DOI)` reading record across `B1` (`78`), `B2/B3` (`388`), and `B5` (`305`) | True integer count columns (`values kept`, `core values`, `states`, `residue sets`, `values not readable`), clickable DOIs, `tables excluded`, `overview`, `reader notes` |
| `Gaps` | `944` | Dynamics quantities mentioned in text as figure-only, BMRB-only, or in unavailable supplements | Explicit `kind`, `what`, `why` log instead of reading off plots |
| `Second_reader_only` | `35` | Candidate rows found only by an independent GPT spot-check reader on `11` papers; unmerged pending human arbitration | `quantity`, `value`, `unit`, `residues or group`, `quote`, `status` |

Notice a small provenance quirk between the raw JSON files and the workbook: `78` (`B1`) + `388` (`B2/B3`) + `305` (`B5`) JSON records contain `19,952` `expected_rows`, while `Measurements` holds `19,958` rows because `CRABP2__10.1021_acs.biochem.9b00672` contributed `14` workbook rows vs `8` in its main JSON.

## Schema columns in `proteins_summary.csv`

`entry, protein, status, audit_flag, UniProt, deposited temperature (K), deposited field (MHz), deposited pH, papers read, dynamics values, values by quantity, rates and populations as printed, state PDB ids, dynamic regions named by authors, samples vs deposit (yes/no/unclear), gap`

## Known drift, bugs, and filtering cautions (important for expert review)

1. **Condition-binding errors are not caught automatically.** Deterministic checks verify that every quote string appears in the source paper, not that a sample's solvent, pH, temperature, or ligand ratio belongs to the right experiment (see the `BARSTAR` `10.1021/jacs.0c00807` HyperW/CLEANEX conflation in [`atlas/v3_previews/16392_and_BARSTAR.md`](../../atlas/v3_previews/16392_and_BARSTAR.md)).
2. **Duplicate RelaxDB entries and `'x'` placeholder collapse.**
   - Four pairs (`BLAC_CPMG` / `27888`, `AQADK` / `AQADK_CPMG`, `ARGKIN_CPMG` / `ARGKIN`, `HTPDZ_CPMG` / `HTPDZ`) share a real UniProt accession where only one twin was extracted in `v3`.
   - Entry `5687` (`Four helix bundle`, UniProt `x`) was falsely grouped onto `50332` (`Iron-compound ABC transporter`, UniProt `x`) in the original builder because both cards carry placeholder `'x'`. That label is now fixed in `Proteins` and `proteins_summary.csv`, making unread open entries `23` (`4` covered via real twin UniProt).
   - `CHEA` and `CHEAYBD` (`P07363`) were both extracted independently with overlapping DOIs and conflicting interpretations (`10.1073/pnas.2218467120`: `11` vs `37` rows; `10.1007/s00723-018-1070-6`: `homolog` vs `same_protein_other_construct`; see [`atlas/v3_previews/CHEA_CHEAYBD.md`](../../atlas/v3_previews/CHEA_CHEAYBD.md)).
   - Two pairs (`CIN1D1`/`CIN1D2` on `A8W3P3`; `RNASE`/`RNASE_CPMG` on `P61824`) have `0` papers read on both twins.
3. **Cross-batch scope drift (`B1` vs `B2/B3` vs `B5`).** The raw `method` column preserves `85` free-text strings across batches. Use the derived `method_group` (`9` buckets) and `row_tier` (`4` tiers: `Experimental_exchange_rate_or_pop` `533`, `Spin_relaxation_bulk` `18,218`, `Other_experimental_dynamics` `1,118`, `MD_or_structure` `89`) to filter cleanly without losing source provenance. Across the `19,958` rows, `17,280` are `minor`, `2,677` are `core` (`1` missing weight on `ISDHN2`), `11,841` are `target`, `7,810` are `same_protein_other_construct`, and `307` are `homolog`.
4. **Known RelaxDB card mismatches carried over from Release 0.1.** `HGMCSF` is labeled `GM-CSF` in RelaxDB but its UniProt (`P09919`) and deposited paper are **G-CSF** (`654` rows read as G-CSF). `5991` points to mouse `Ets-1` (`P27577`), so human `ETS1` studies (`30` rows) are tagged `homolog`. See [`../relaxdb_data_issues.md`](../relaxdb_data_issues.md) for the earlier sequence-identity audit.
5. **Deposited-condition mismatches dominate.** Across `19,958` rows, `7,637` have `same sample as deposit = no`, `6,449` `unclear`, and `5,872` `yes` (largely driven by multi-hundred-row `B1` relaxation SI tables matching the source paper). Many cards list `298.5 K` as a placeholder temperature.
