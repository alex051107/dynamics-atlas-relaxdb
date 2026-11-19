# v3 Paper Extraction Draft (`18 November 2026`)

Machine-readable summary CSVs and the nine-sheet Excel workbook from the `v3` paper-by-paper extraction sweep across the **131 open RelaxDB entries** (`12` held-out entries excluded).

Use this folder alongside the **worked protein synthesis previews** in [`atlas/v3_previews/`](../../atlas/v3_previews/README.md) and the **workflow Statechart** in [`methods/how_it_is_built.md`](../../methods/how_it_is_built.md). Unlike Release `0.1` (`21 October 2026`), which published protein-level state calls (`yes / possible / unknown`) for `42` proteins, this `v3` artifact is an **uncurated paper-to-table aggregation**. It has not yet been filtered by an NMR expert or synthesized into per-protein calls.

## Files in this folder

| File | Contents | Rows |
|---|---|---|
| [`RelaxDB_dynamics_from_papers_DRAFT_20261118.xlsx`](RelaxDB_dynamics_from_papers_DRAFT_20261118.xlsx) | Multi-sheet workbook built from `771` checked entry-paper JSON records (`752` unique DOIs) | `19,958` measurements across `9` tabs |
| [`proteins_summary.csv`](proteins_summary.csv) | Exact CSV export of the workbook `Proteins` tab (one row per open RelaxDB entry) | `131` data rows |
| [`coverage_gap_audit.csv`](coverage_gap_audit.csv) | Transparent accounting of open entries, duplicate-UniProt pairs, unread Nov-12 DOIs (`988`), Kosmos (`336`), and un-reread early batches (`168`) | `15` metrics |

## Workbook tabs (`RelaxDB_dynamics_from_papers_DRAFT_20261118.xlsx`)

| Tab | Rows (excl. header) | What one row represents | Key new or high-signal columns vs Release 0.1 |
|---|---|---|---|
| `README` | `15` | Scope notes, accuracy benchmarks, known card problems, batch provenance | Plain-text orientation note inside the workbook |
| `Proteins` | `131` | One RelaxDB open entry (mirrors `proteins_summary.csv`) | `rates and populations as printed` (with `[homolog]` tags), `state PDB ids`, `dynamic regions named by authors`, `samples vs deposit`, `gap` |
| `Measurements` | `19,958` | One printed dynamics number, range, or bound extracted from paper text, tables, or figure captions | `sample` (`S1..Sn`), `buffer`, `species relation`, `weight` (`core` / `minor`), `same sample as deposit`, `location in paper`, `quote`, `record` |
| `States` | `794` | One author-named conformational or complex PDB state tied to the entry protein (or labeled `homolog`) | `PDB`, `state`, `location in paper`, `quote` |
| `Residue_sets` | `515` | One author-named dynamic, exchange-broadened, flexible, or protected residue region without requiring printed rates | `process`, `residues`, `sample`, `location in paper`, `quote` |
| `Samples` | `4,131` | One experimental or simulation condition block referenced by `Measurements` and `Residue_sets` via `sample` ID | `protein`, `construct`, `species relation`, `ligand state`, `temperature`, `pH`, `buffer`, `field (MHz)`, `same as deposit`, `note`, `quote` |
| `Papers` | `771` | One `(entry, DOI)` reading record across `B1` (`78`), `B2/B3` (`388`), and `B5` (`305`) | `values kept`, `core values`, `tables excluded`, `overview`, `reader notes (why no value, conflicts, corrections)` |
| `Gaps` | `944` | Dynamics quantities mentioned in text as figure-only, BMRB-only, or in unavailable supplements | `kind`, `what`, `why` |
| `Second_reader_only` | `35` | Candidate rows found only by an independent GPT spot-check reader on `11` papers; unmerged pending human arbitration | `quantity`, `value`, `unit`, `residues or group`, `quote`, `status` |

Notice a small provenance quirk between the raw JSON files and the workbook: `78` (`B1`) + `388` (`B2/B3`) + `305` (`B5`) JSON records contain `19,952` `expected_rows`, while `Measurements` holds `19,958` rows because `CRABP2__10.1021_acs.biochem.9b00672` contributed `14` workbook rows vs `8` in its main JSON.

## Schema columns in `proteins_summary.csv`

`entry, protein, UniProt, deposited temperature (K), deposited field (MHz), deposited pH, papers read, dynamics values, values by quantity, rates and populations as printed, state PDB ids, dynamic regions named by authors, samples vs deposit (yes/no/unclear), gap`

## Known drift, bugs, and filtering cautions (important for expert review)

1. **Condition-binding errors are not caught automatically.** Deterministic checks verify that every quote string appears in the source paper, not that a sample's solvent, pH, temperature, or ligand ratio belongs to the right experiment (see the `BARSTAR` `10.1021/jacs.0c00807` HyperW/CLEANEX conflation in [`atlas/v3_previews/16392_and_BARSTAR.md`](../../atlas/v3_previews/16392_and_BARSTAR.md)).
2. **Duplicate RelaxDB entries and `'x'` placeholder collapse.**
   - Four pairs (`BLAC_CPMG` / `27888`, `AQADK` / `AQADK_CPMG`, `ARGKIN_CPMG` / `ARGKIN`, `HTPDZ_CPMG` / `HTPDZ`) share a real UniProt accession where only one twin was extracted in `v3`.
   - Entry `5687` (`Four helix bundle`, UniProt `x`) was falsely grouped onto `50332` (`Iron-compound ABC transporter`, UniProt `x`) by the workbook builder because both cards carry placeholder `'x'`, making effective unread open entries `23` rather than `22`.
   - `CHEA` and `CHEAYBD` (`P07363`) were both extracted independently with overlapping DOIs and conflicting interpretations (`10.1073/pnas.2218467120`: `11` vs `37` rows; `10.1007/s00723-018-1070-6`: `homolog` vs `same_protein_other_construct`; see [`atlas/v3_previews/CHEA_CHEAYBD.md`](../../atlas/v3_previews/CHEA_CHEAYBD.md)).
   - Two pairs (`CIN1D1`/`CIN1D2` on `A8W3P3`; `RNASE`/`RNASE_CPMG` on `P61824`) have `0` papers read on both twins.
3. **Cross-batch scope drift (`B1` vs `B2/B3` vs `B5`).** Filtering `Measurements` by `weight = core` and excluding `method = md_simulation` (`49` rows), `molecular_dynamics` (`25` rows), `emsa_dissociation_kinetics`, `fluorescence_correlation_spectroscopy`, `FRET`, and `fret` is necessary before aggregating rates across entries. In addition, `method` uses uncontrolled free-text strings across batches (`epr_deer`, `epr_deer_distance`, `deer_epr_distance`, `epr_distance_deer`; `FRET` vs `fret`; `x_ray_crystallography` vs `xray_multiconformer` vs `x-ray crystallography (atomic resolution)`). In `B5` (`305` Gemini records), non-NMR kinetics (`DBD82` live-cell FCS, EMSA DNA off-rates, cell FRET) were preserved as `weight = minor` while NMR/HDX/exchange numbers stayed `core`; earlier batches mostly excluded non-NMR kinetics. Across the `19,958` rows, `17,280` are `minor`, `2,677` are `core` (`1` missing weight), `11,841` are `target`, `7,810` are `same_protein_other_construct`, and `307` are `homolog`.
4. **Known RelaxDB card mismatches carried over from Release 0.1.** `HGMCSF` is labeled `GM-CSF` in RelaxDB but its UniProt (`P09919`) and deposited paper are **G-CSF** (`654` rows read as G-CSF). `5991` points to mouse `Ets-1` (`P27577`), so human `ETS1` studies (`30` rows) are tagged `homolog`. See [`../relaxdb_data_issues.md`](../relaxdb_data_issues.md) for the earlier sequence-identity audit.
5. **Deposited-condition mismatches dominate.** Across `19,958` rows, `7,637` have `same sample as deposit = no`, `6,449` `unclear`, and `5,872` `yes` (largely driven by multi-hundred-row `B1` relaxation SI tables matching the source paper). Many cards list `298.5 K` as a placeholder temperature.
