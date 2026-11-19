# Ribonuclease (`BINASE`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P00648` · **RelaxDB deposited card:** T = `303.0`, field = `500/800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*8 rows total (8 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f) | `NMR_spin_relaxation_and_MF` | `target` | apo | R1 (4), other (3), tau_m (1) | tau_m = 6.1 ns (whole protein) |

## 3. Computational (MD/MSM) and cryo-structure (X-ray / cryo-EM) rows

*6 rows intentionally separated from experimental solution dynamics pending expert scope lock:*

| Method group | Quantity | Value | Residues / group | Paper |
|---|---|---|---|---|
| `MD_and_MSM` | `S2` | 0.934 dimensionless | residue 10 | [`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f) |
| `MD_and_MSM` | `tau_e` | 1.9 ps | residue 10 | [`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f) |
| `MD_and_MSM` | `S2` | 0.736 dimensionless | residue 37 | [`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f) |
| `MD_and_MSM` | `tau_e` | 57.1 ps | residue 37 | [`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f) |
| `MD_and_MSM` | `S2` | 0.486 dimensionless | residue 68 | [`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f) |
| `MD_and_MSM` | `tau_e` | 47.8 ps | residue 68 | [`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f) |

## 4. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **residues with extensive conformational exchange (Rex) in Modelfree fit** ([`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f), sample `S1`): Gln 28, Ala 103, and Phe 105
- **residues that could not be fitted into any of the five models** ([`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f), sample `S1`): Ser 30, Ala 31, Ala 42, Asp 100, and Thr 104
- **residues not detected in any experiment (exchange broadening)** ([`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f), sample `S1`): 66 and 67

## 5. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f) | 14 | 0 | 3 | 2 | The paper prints almost no per-residue numbers; they are in figures (Fig 4, 5, 7, 9, 10). Printed values: rota |

**Explicit figure-only, SI-only, or access gaps (2):**

- Per-residue 15N R1, R2 (CPMG and echo), NOE, eta_xy at two fields; Modelfree S2, Rex, tau_e; 13CO-13CA S2; MD S2 and R1 ([`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f)): figure only (Figures 4, 5, 7, 9, 10); no tables in the text
- Conformational exchange rate 3000 s-1 and 300 us site-opening time ([`10.1021/bi011657f`](https://doi.org/10.1021/bi011657f)): cited from the authors' earlier paper (ref 13), not measured here

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
