# Quality

This page says how far to trust the atlas, with numbers, separating **Release 0.2-draft (`v3` paper extraction)** from the **Release 0.1 (`21 October 2026`)** baseline.

## Release 0.2-draft (18–19 November 2026): v3 Paper-by-Paper Extraction Checks

### Coverage & batch provenance (`771` records, `752` unique DOIs, `19,958` rows)

| Batch | Reader model(s) | Records read | Zero-row records | Measurement rows | State PDB rows | Residue-set rows | Verification applied |
|---|---|---|---|---|---|---|---|
| **B1 (`v3_sonnet`)** | Claude Sonnet | `78` | `12` (`15.4%`) | `18,811` | `87` | `241` | Deterministic quote & table checks (`100%` of records); **not re-read under Nov-17 state/scope rules** |
| **B2 + B3 (`v3_sonnet_b2`)** | Claude Sonnet | `388` | `280` (`72.2%`) | `1,077` | `417` | `198` | Quote & table checks; main-session reread of all `108` `B3` records (`67/108` edited, `~139` of `204` final states added after reader); `90` early `B2` records **not re-read under Nov-17 rules** |
| **B5 (`v3_b5`)** | Gemini (`248 pro`, `57 flash`) | `305` | `295` (`96.7%`) | `64` *(across `10` papers)* | `290` | `74` | Deterministic quote/table/identity/condition checks (`0` hard failures; `53` `W1_RECONSTITUTION_CHECK` warnings, `3` `W_EMPTY_SAMPLES`, `3` `W_DEPOSIT_PDB_CHECK`) + stratified `30`-paper blind `Claude Sonnet 5.5` check |

*(Note: summing raw JSON `expected_rows` gives `18,811 + 1,077 + 64 = 19,952`; the workbook `Measurements` tab holds `19,958` rows because `CRABP2__10.1021_acs.biochem.9b00672` contributed `14` workbook rows vs `8` in its main JSON.)*

### Answer-key and cross-model consistency checks in `v3`

| Check | What it measured | Observed result | Critical limit / caveat |
|---|---|---|---|
| **4 hand-built paper keys** (`arginine kinase`, `CRABP2`, `p38 gamma`, `IscU`) | Recall & precision on core printed rates/populations | **`85 / 86` core values**, `0` invented values outside keys | Tested on `4` NMR-rich benchmark papers only; does not test condition binding across multi-experiment methods sections |
| **Independent GPT spot-check (`1 + 8 + 2` papers)** | Cross-model recall vs main reader | `163 / 165` on arginine kinase (`102 / 102` Table 1 cells vs XML); `203 / 213` values and `8 / 8` states on `8` papers; `35` GPT-only candidate rows logged in `Second_reader_only` | Does not verify sample-condition binding; `35` `Second_reader_only` rows remain unmerged pending human arbitration |
| **B3 blind Haiku check (`13` records, `2026-11-17`)** | All `7` valued `B3` records (`CHEAYBD` skipped as identical to `CHEA`) + `6` zero-row records | Found **`2` real record errors** (`1` missed `tau_m = 14.8 ns` in `5991`, fixed; `1` unsupported state `1CLL` added during main-session reread of `17881`, removed) vs `4` Haiku false-alarm values and `2` false-alarm states | Did **not** diff sample/condition fields (`samples` list was not compared), `residue_sets`, `out_of_reach`, or the other `95` `B3` records; state-PDB rule changed three times during `B3` (`67/108` edited afterward) |
| **B5 stratified blind check (`30` papers with `Claude Sonnet 5.5`, `2026-11-18`)** | All `10` valued `B5` papers + `10` keyword zero-row + `10` general zero-row | **`29 / 29`** newly printed non-cited Claude values matched; **`100%`** Claude state recall (`+46` verified Gemini states); **`20 / 20`** Stratum 2+3 zero-row agreement; **`30 / 30`** experimental NMR/HDX/relaxometry agreement; **`26 / 30`** raw zero-vs-valued agreement | **Prevalence-bias warning.** Because `96.7%` (`295/305`) of `B5` papers are non-valued (`mostly clinical/cellular/binding`), high overall zero-row agreement is easy to achieve by saying zero. Disagreements concentrated in **4 non-NMR `DBD82` papers** (`FCS`, `MD`, `EMSA t1/2`, `cell FRET`), showing prompt ambiguity outside NMR (`4` B5 records repaired after adjudication: downgraded non-NMR kinetics to `minor` and fixed `4` fold/ratio rows in `FKBP` `bpc.2014.06.004`) |

### What `v3` checks still DO NOT guarantee (why this is a draft, not a validated release)

- **Zero expert NMR sign-off.** Neither the `v3` workbook rows nor the `4` synthesis previews have been reviewed by an NMR expert yet.
- **No automated sample-condition binding check (`Gap 1`).** Substring checks pass whenever quotes exist anywhere in the paper, even if two experiments (`BARSTAR` `10.1021/jacs.0c00807` `~1.8% H2O` HyperW vs `90% H2O` CLEANEX) were collapsed into one sample row, or when construct tags diverge across identical papers (`CHEA` vs `CHEAYBD`). Although `audit_b5_all.py` raised `53` `W1_RECONSTITUTION_CHECK` warnings in `B5`, the earlier `466` `B1–B3` records were never scanned by it.
- **Incomplete literature coverage (`Gap 2`).** `22` open entries (`+1` entry `5687` falsely collapsed onto `50332` via placeholder `'x'`) have `0` papers read in `v3`, **`988` DOIs from the `12 Nov` draft (`244` marked full text)** and **`336` Kosmos rows** remain unread, and **`168` early `B1/B2` records** have not been re-read under Nov-17 rules.
- **Cross-batch inclusion inconsistency.** Non-NMR kinetics (`FCS ms`, `EMSA` DNA-off `t1/2`, cell-`FRET`) and MD clusters were kept in some `B5`/`B3` records (`minor` or `md_simulation` / `molecular_dynamics`) while omitted in earlier records. Furthermore, `method` labels lack a controlled vocabulary (`md_simulation` vs `molecular_dynamics`, `FRET` vs `fret`, four `EPR/DEER` variants, and three X-ray crystallography strings), reinforcing why `v4` needs a strict schema enum.
- **No raw BMRB / chemical-shift cross-validation.** Unlike the BMRB readbacks logged in [`../data/relaxdb_data_issues.md`](../data/relaxdb_data_issues.md) during `0.1`, `v3` text rows have not been compared against raw BMRB `R1/R2/NOE/CPMG` tables.

---

## Release 0.1 (21 October 2026): Pre-registered Alternate APO Checks

### Pre-registered test on 20 proteins

Before we ran 20 RelaxDB-133 proteins, we wrote down seven checks and their limits. We did not change the limits after the results.

| Check | Limit | Result | Pass? |
|---|---|---|---|
| Proteins that reach a reviewed call | 18 of 20 | 20 of 20 | yes |
| Rows corrected after the double re-read | 15 per 100 rows | 18.9 per 100 rows | no |
| Planted errors that the re-read catches | 70% | 13 of 20 (65%) | no |
| Machine time per protein | median 45 minutes | median 24 minutes | yes |
| External NMR papers that the search finds | 70% | 11 of 15 (73%) | at the limit |
| Number or sample errors that the final review finds | 1 per protein | 0.55 per protein | yes |
| Proteins with a call other than unknown | report only | 6 of 20 | report only |

Two checks failed:

- **Corrections.** 110 of the 153 corrections are in one protein, thioredoxin. Most come from one error: E. coli thioredoxin has the entry's exact sequence, but the worker labelled it a homolog. The worker now receives the accessions with an identical sequence. A test re-read of two papers gave 30 rows and no homolog labels.
- **Planted errors.** The 7 missed errors were all marked "cannot verify" by both readers, so they never reached adjudication. Such rows now go to adjudication when the paper was read in full. On a new set of 20 planted errors, the re-read caught 20 of 20. It also flagged 1 of 38 rows that had no planted error.

Two limits on these numbers:

- The search result is partly circular. PDB citations are both a search channel and part of the reference list. Without the RelaxDB source papers as seeds, the search found 10 of 15.
- The first set of planted errors was used to find the fix. It can no longer serve as an independent test.

## Reviews of the overnight records

On 20 to 21 October we re-read 11 RelaxDB source papers in full and rewrote 12 records. Two independent reviews checked them. They found 0.33 and 0.83 verified errors per protein. Each error was fixed. One review reversed a call: for one SH3 domain (entry 7036) the authors report no exchange, so the call went back to unknown.

## Errors in the pipeline

[`error_log.json`](error_log.json) lists every error that we found, with the evidence, the fix and the status. The most important kinds:

| What went wrong | Fix |
|---|---|
| 5 RelaxDB cards had a wrong UniProt accession | Identity check before any search |
| The RelaxDB source paper was screened out because its abstract did not mention dynamics | Source papers are always read |
| E. coli thioredoxin was labelled a homolog of the entry | The worker receives accessions with an identical sequence |
| Rows that both readers could not verify never reached adjudication | Those rows now go to adjudication |
| A failed re-read could inherit the file of the previous reader | Each reader starts with no file and must read every row |
| The exchange regime came from the authors' adjectives | When kex and Δω are printed, we compute the regime |
| A T1/T2 subscript was lost in the PDF text, and one sentence was read reversed | Statements that depend on subscripts or tables are read from the page image |

## What the checks do not cover

- All readers and reviewers so far are language models. No expert has checked the records.
- A row can match its paper while the experiment itself is wrong. We record buffers, controls and author caveats, but we do not filter experiments yet.
- The readers share the same source text, so they can miss the same figure or supplementary table.
