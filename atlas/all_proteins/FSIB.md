# Fibroblast growth factor 8 (`FSIB`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P55075` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `700` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*952 rows total (952 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1007/s12104-023-10132-8`](https://doi.org/10.1007/s12104-023-10132-8) | `NMR_spin_relaxation_and_MF` | `target` | apo | other (321), NOE (140), R1 (140), R2 (140), S2 (140), tau_e (52) | NOE = -2.656 dimensionless (ratio) (M21) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **nanosecond mobility (Te) loop** ([`10.1007/s12104-023-10132-8`](https://doi.org/10.1007/s12104-023-10132-8), sample `S1`): D91-S95
- **S2 plateau, partially restricted mobility, gN region not formed** ([`10.1007/s12104-023-10132-8`](https://doi.org/10.1007/s12104-023-10132-8), sample `S1`): 33-45

### Conformational and complex PDB states (`States`)

- [`2FDB`](https://www.rcsb.org/structure/2FDB): FGF8b in complex with FGFR2c, gN helix formed ([`10.1007/s12104-023-10132-8`](https://doi.org/10.1007/s12104-023-10132-8))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1007/s12104-023-10132-8`](https://doi.org/10.1007/s12104-023-10132-8) | 952 | 1 | 2 | 2 | 15N T1, T2, heteronuclear NOE and TENSOR2 model-free results (S2, Te, exchange term, S2f) per residue from the |

**Explicit figure-only, SI-only, or access gaps (2):**

- RCI-S2 order parameters per residue (Fig. 2) ([`10.1007/s12104-023-10132-8`](https://doi.org/10.1007/s12104-023-10132-8)): figure only
- T1/T2 ratio and duplicated NOE columns in the supplement table ([`10.1007/s12104-023-10132-8`](https://doi.org/10.1007/s12104-023-10132-8)): derived or duplicate columns of values already listed; not extracted as separate rows

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
