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
| `Exchange_Highlights` | `575` | Filtered view of `Measurements` isolating `kex`, `kAB`, `kBA`, `kopen`, `kclose`, `k12`, `kct`, `pB`, `population`, `delta_omega`, `tau_ex`, and `phi_ex` across `38` proteins | Lets NMR experts scan conformational exchange in minutes without scrolling past `18,000+` bulk `R1/R2/NOE` rows; soft amber tint flags `MD`, `X-ray/Cryo-EM`, `Biophysics`, and `homolog` rows |
| `Measurements` | `19,989` | Lossless table of all `19,958 original` rows + `31` newly verified `2026-11-19` rows (`100%` quote-checked) | Adds two controlled filter columns (`method_group` mapping all `85` raw method strings into `9` buckets, plus `row_tier`) while keeping every original column and clickable DOI intact |
| `States` | `798` | One author-named conformational or complex PDB state tied to the entry protein (or labeled `homolog`) | Clickable DOI links, `PDB`, `state`, `location in paper`, `quote` (added `2JUO`, `1MZK`, `1P68`, `3LVL`) |
| `Residue_sets` | `523` | One author-named dynamic, exchange-broadened, flexible, or protected residue region without requiring printed rates | Clickable DOI links, `process`, `residues`, `sample`, `location in paper`, `quote` |
| `Samples` | `4,142` | One experimental or simulation condition block referenced by `Measurements` and `Residue_sets` via `sample` ID | `BARSTAR` `10.1021/jacs.0c00807` conflated `S1` fixed (split into `S1` HyperW and `S2` CLEANEX) plus `10` new sample cards |
| `Papers` | `776` | One `(entry, DOI)` reading record across `B1` (`78`), `B2/B3` (`388`), `B5` (`305`), and `2026-11-19` supplemental reads (`5`) | True integer count columns (`values kept`, `core values`, `states`, `residue sets`, `values not readable`), clickable DOIs, `tables excluded`, `overview`, `reader notes` |
| `Gaps` | `946` | Dynamics quantities mentioned in text as figure-only, BMRB-only, or in unavailable supplements | Explicit `kind`, `what`, `why` log instead of reading off plots (stale unread rows removed for newly read entries) |
| `Second_reader_only` | `35` | Candidate rows found only by an independent GPT spot-check reader on `11` papers; unmerged pending human arbitration | `quantity`, `value`, `unit`, `residues or group`, `quote`, `status` |

Notice a small provenance difference between the raw JSON files and the workbook. The `771` original `v3` JSON records held `19,952` `expected_rows` (`CRABP2__10.1021_acs.biochem.9b00672` contributed `14` workbook rows vs `8` in its main JSON, yielding `19,958 original` rows). Adding the `31` verified rows from `2026-11-19` brings `Measurements` to `19,989` rows.

## Schema columns in `proteins_summary.csv`

`entry, protein, status, release_01_call, audit_flag, UniProt, deposited temperature (K), deposited field (MHz), deposited pH, papers read, dynamics values, values by quantity, rates and populations as printed, state PDB ids, dynamic regions named by authors, samples vs deposit (yes/no/unclear), gap`

## Known drift, fixes applied, and filtering cautions

1. **Condition-binding errors are not caught automatically (`BARSTAR` fixed on 19 Nov).** Deterministic checks verify that every quote string appears in the source paper, not that a sample's solvent, pH, temperature, or ligand ratio belongs to the right experiment. We fixed the `BARSTAR` `10.1021/jacs.0c00807` HyperW/CLEANEX conflation in `Samples` (`S1` and `S2`), and upstream `v4` schema enforcement awaits Gina's sign-off.
2. **Duplicate RelaxDB entries and `'x'` placeholder collapse (`5687` fixed on 19 Nov).**
   - Entry `5687` (`Four helix bundle`, UniProt `x`) is separated from `50332` and read (`10.1073/pnas.1835644100`, PDB `1P68`).
   - All shared-UniProt pairs (`CHEA`/`CHEAYBD`, `BLAC_CPMG`/`27888`, `AQADK`/`AQADK_CPMG`, `ARGKIN`/`ARGKIN_CPMG`, `HTPDZ`/`HTPDZ_CPMG`, `CIN1D1`/`CIN1D2`, `RNASE`/`RNASE_CPMG`) are cross-linked in `Proteins` and `atlas/all_proteins/`.
3. **Controlled method filtering (`85 -> 9` buckets).** The raw `method` column preserves all `85` free-text strings losslessly. Filter on `method_group` (`9` buckets) and `row_tier` (`Experimental_exchange_rate_or_pop` `541`, `Spin_relaxation_bulk` `18,241`, `Other_experimental_dynamics` `1,118`, `MD_or_structure` `89` across all `19,989` rows) instead of raw strings.
4. **Known RelaxDB card mismatches carried over from Release 0.1.** `HGMCSF` is labeled `GM-CSF` in RelaxDB but its UniProt (`P09919`) and deposited paper are **G-CSF** (`654` rows read as G-CSF). `5991` points to mouse `Ets-1` (`P27577`), so human `ETS1` studies (`30` rows) are tagged `homolog`. See [`../relaxdb_data_issues.md`](../relaxdb_data_issues.md) for the earlier sequence-identity audit.
5. **Deposited-condition mismatches are common.** Across `19,989` rows, many paper conditions differ from RelaxDB's deposited temperature, pH, or ligand state, and several RelaxDB cards carry `298.5 K` as a placeholder temperature. Check `same sample as deposit` before pooling values with BMRB entries.
