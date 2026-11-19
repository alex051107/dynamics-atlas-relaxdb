# Inhibitor of trypsin and hageman factor (`CMTIV`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P19873` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

> **Audit note:** NEW 2026-11-19: PMC2143810 abstract_only S2 + PMC2249841 full text (1996 paper paywalled)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*6 rows total (6 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1002/pro.5560070114`](https://doi.org/10.1002/pro.5560070114) | `NMR_spin_relaxation_and_MF` | `target` | apo (intact) | S2 (3) | S2 = 0.83 dimensionless (backbone NH average (intact rCMTI-V;…) |
| [`10.1002/pro.5560070114`](https://doi.org/10.1002/pro.5560070114) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | cleaved (I*) | S2 (3) | S2 = 0.85 dimensionless (backbone NH average (cleaved rCMTI-V…) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **flexible protease-binding loop (sharply mobilized at P4-P1 upon Lys44-Asp45 hydrolysis)** ([`10.1002/pro.5560070114`](https://doi.org/10.1002/pro.5560070114), sample `S1`): P4-P1 and P1'-P4' around scissile bond Lys44-Asp45 (modulated by Arg50 and Arg52 hydrogen bonds)

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1002/pro.5560070114`](https://doi.org/10.1002/pro.5560070114) | 6 | 0 | 1 | 1 | PMC holds a scanned PDF without machine-readable body text; the official PMC abstract prints comparative avera |

**Explicit figure-only, SI-only, or access gaps (1):**

- Per-residue 15N T1, T2, NOE, and S2 for rCMTI-V and rCMTI-V* ([`10.1002/pro.5560070114`](https://doi.org/10.1002/pro.5560070114)): PMC2143810 is a scanned PDF without machine-readable body text; primary 1996 study (doi:10.1021/bi952466d) is behind ACS paywall

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
