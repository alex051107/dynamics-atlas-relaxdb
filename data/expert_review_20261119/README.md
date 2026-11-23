# Expert Review Workbook (16 Tabs) & Queryable SQLite Database

Download directly from GitHub:
- **16-tab clickable Excel workbook**: **[`RelaxDB_expert_review_DRAFT.xlsx`](RelaxDB_expert_review_DRAFT.xlsx)** (4.9 MiB)
- **Companion strict-typed SQLite database**: **[`RelaxDB_expert_review_DRAFT.sqlite`](RelaxDB_expert_review_DRAFT.sqlite)** (25.8 MiB)
- **Zero-dependency query CLI**: **[`query_atlas.py`](query_atlas.py)** (Python standard library only)

This package reorganizes the frozen November 18 extraction baseline (`131` open RelaxDB entries, `771` entry-paper records, `752` distinct DOIs, `19,958 original` measurements; kept distinct from the `+ 31 = 19,989` November 19 supplemental branch rows) into both a clickable Excel view and a queryable relational + full-text database. Independent expert trial reading by Gina is still pending.

## Query the database in 1 command (Soojung's 3 target questions)

```bash
# 1. All experimental evidence at one protein + residue (with offset warnings, scopes, gaps & live BMRB values)
python3 data/expert_review_20261119/query_atlas.py residue FKBP 59
python3 data/expert_review_20261119/query_atlas.py residue 50020 1133

# 2. Cross-protein conformational exchange (excludes association/crystal/MD & quarantined rows)
python3 data/expert_review_20261119/query_atlas.py exchange --min-kex 50 --limit 20

# 3. Measurements & exact sample conditions supporting a transition for one protein
python3 data/expert_review_20261119/query_atlas.py transition FKBP

# 4. Direct BMRB relaxation values, full-text quote/note search, and executive quality audit
python3 data/expert_review_20261119/query_atlas.py bmrb 27888
python3 data/expert_review_20261119/query_atlas.py search "precipitated AND elevated AND temperature"
python3 data/expert_review_20261119/query_atlas.py audit
```

## Sheet structure (16 tabs)

| Tab | Rows | Role |
|---|---:|---|
| `Start_Here` | Overview | One-page orientation, pilot jumps, quality/BMRB/SI/figure shortcuts, and `physical_scope` definitions |
| `Protein_overview` | `131` | One row per open RelaxDB entry, now with numbering-offset warnings, phosphate-only flags, Dyna-1 missing-peak counts, BMRB recoveries, quarantined rows, and figure-only gaps |
| `Region_comparisons` | `109` | Question-driven comparisons (`Protein x Region x Window x Sample State`) with native hyperlinks to every listed observation |
| `Observations` | `396` | Atomic source-quoted evidence rows with `physical_scope`, `signal_class`, `verification_tier`, ECO evidence codes, `data_validity_flag`, `Samples` links, DOI links, and `139` clickable public NIH S3 figure/PDF links |
| `Data_quality_audit` | `16` | Audit ledger (`DQA_01` through `DQA_16`) documenting every automated quarantine, offset, phosphate, Dyna-1, BMRB, and SI check |
| `BMRB_recovered` | `68` | Full-atlas live BMRB v2 API recovery: `62 / 68` entries with `37,131` per-residue values (`10,426` NOE, `10,944` T1, `11,179` T2, `168` T1rho, `2,826` S2, `1,588` Rex with `983` positive `Rex > 0`), standardized `R1/R2`, `33` `Auth-Seq` offsets, and `16` deposit-anomaly flags |
| `SI_S3_inventory` | `386` | Tier-2 public NIH AWS Open Data PMC S3 inventory across all `386` distinct gap DOIs (`346` OA PMCIDs, `242` S3 asset-ready, `43` direct SI spreadsheets) with direct clickable S3 PDF (`236`), spreadsheet (`63`), and figure (`242`) URLs plus SPDX license tags |
| `Figure_S3_links` | `2,114` | Direct clickable public NIH AWS S3 figure URLs (`s3://pmc-oa-opendata`, no AWS key required) across `242` OA DOIs, enriched from local JATS XML with `1,719` figure labels, caption previews, and SPDX license tags |
| `Review_notes` | `10` | Documented issues, fixes applied, 3-tier figure/SI/BMRB recovery policy (`RN_10`), version boundary, and open expert rulings |
| `Measurements` | `19,958 original` | Lossless raw extraction table (`0` formula cells) plus 7 appended columns, including the validity comment (`17,864` clean + `2,094` quarantined with blank clean-numeric cells so Excel never averages quarantined rows) |
| `Samples` | `4,131 + 2` | Lossless raw sample cards plus `2` Barstar split cards (`S1_HyperW`, `S2_CLEANEX`) and rightmost phosphate, superseded, and dynamics-reference flags |
| `States` | `794` | Lossless raw conformational state PDB mappings |
| `Residue_sets` | `515` | Lossless raw author-named dynamic residue regions plus rightmost Dyna-1 `signal_class` (`74` `EXCHANGE_BROADENED_MISSING_PEAK`) |
| `Papers` | `771` | Lossless raw per-paper audit summaries |
| `Gaps` | `944` | Lossless raw figure-only and missing-SI gaps plus rightmost 3-tier triage, detected BMRB ID, resolved PMCID, and S3 SI asset status |
| `Second_reader_only` | `35` | Lossless raw blind second-reader candidates |

## Units, asset permissions and related entries

The clean table keeps the 218 IL4 NOE ratios dimensionless and the 506 verified FSIB and IL4 relaxation rates in inverse seconds. See audit entries `DQA_10` to `DQA_16` for raw and clean counts. No printed rate was inverted.

Each figure and supplementary record has separate retrieval, external-model and public-release fields. A retrieval category does not mean the file is available. Missing license tags remain blank in the source column.

| License bucket | Figures | Distinct figure DOIs | All inventory DOIs |
|---|---:|---:|---:|
| CC0 | 22 | 2 | 2 |
| CC-BY | 1,578 | 174 | 175 |
| CC-BY-NC | 163 | 22 | 22 |
| CC-BY-NC-SA | 4 | 1 | 1 |
| CC-BY-NC-ND | 201 | 25 | 26 |
| publisher_oa | 125 | 15 | 104 |
| untagged (including blank) | 21 | 3 | 56 |
| Total | 2,114 | 242 | 386 |

The 56 untagged inventory DOIs include 42 blank tags. `Protein_overview` and `proteins` link 14 entries in seven pairs without combining their measurements. The 131 entries have 123 distinct raw UniProt labels, including `x` on two entries. The canonical accession stays empty for those two entries; neither is linked to the other.

## What this upgrade fixed and proved

1. **ChEMBL-style non-destructive cleaning and SQLite quarantine (`19,958 original` exact partition)**: `17,864` clean numeric rows (`69` ranges like `AQADK 2,000-7,000` and `15` flattened scientific strings like `CI2 (31±2)x102 -> 3100` rescued) plus `2,094` quarantined rows (`1,875` contradictory other-construct deposit flags blocked by a SQLite `CHECK` constraint, `12` PDF exponent traps like Ubiquitin `6470` `'104' ps`, `195` non-numeric strings, and `12` quantity/unit mismatches (5 relaxation times and 7 time-valued order-parameter products)).
2. **Full-atlas Tier-1 BMRB recovery (`37,131` exact values across `62 / 68` entries)**: Recovers `55 / 55` numeric open RelaxDB entries (including all `22` zero-numeric entries and all `3` paywalled entries `15795`, `18477`, `50734`) and exposes `16` upstream BMRB deposit traps (`18477` copy-pasted `R2` as `NOE`, `18257` raw unnormalized NOE intensities, `17701`/`50734` ms mislabeled as `s`, `5154`/`7056`/`18758` inverted `s`/`s-1`).
3. **Tier-2 AWS S3 SI harvest proof (`386` gap DOIs)**: `346 / 386` (`89.6%`) resolve to Open Access PMCIDs, `242` (`62.7%`) have directly downloadable assets on AWS S3, and `43` carry machine-readable SI spreadsheets. Parsing `20 / 20` prioritized spreadsheets recovered `12` real dynamics tables (`HTPDZ` `PMC11535027` with `10` NMR relaxation/CPMG sheets, `UVRDTD` `PMC7585439` with `7` NMR sheets, `FSIB` `PMC10232571` with `140` `HetNOE/T1/T2` rows, plus `6` HDX-MS and `3` NMR CSP spreadsheets).
4. **Tier-3 honest figure rule (`RN_10`)**: Live inspection of `50020` (`PMC7137805` Fig. 2F) and `BARSTAR` (`PMC7304870` Fig. 5B) confirmed that vision models accurately read isolated outliers (`N1133 ~0.16` vs exact `0.160`) and qualitative ranges (`BARSTAR` `kHN ~0.2-30 s-1`), but misread dense unlabelled log-scale scatter plots (`±1-3` residues, `8-15%` log-Y error). Dense per-residue coordinates are therefore fetched from Tier 1 BMRB or Tier 2 SI spreadsheets first, with axis-calibrated `WebPlotDigitizer` reserved strictly for prioritized true figure-only targets.
5. **Lossless export and determinism**: `check_expert_review.py delivery` passes (`0` lost rows across all `7` raw sheets, `0` formula cells in `Measurements`), and rebuilding twice produces `0` XML byte differences across all `16` sheets.
