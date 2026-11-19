# Glutaredoxin 1 (`GXN`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P68688` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

*2 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `population` | 62% % | monomer fraction | `NMR_spin_relaxation_and_MF` | `target` | apo, oxidized, 0.48 mM, 62% monomer; 25 °C; pH 6.5; 500 | `unclear` | [`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g) |
| `population` | 37% % | monomer fraction | `NMR_spin_relaxation_and_MF` | `target` | apo, oxidized (disulfide Cys11-Cys14), 2.3 mM, monomer-dimer mixture; 25 °C; pH 6.5; | `unclear` | [`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*997 rows total (996 spin-relaxation/model-free; 1 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g) | `NMR_spin_relaxation_and_MF` | `target` | apo, reduced (5 mM DTT), 2.3 mM, monomer | T1 (76), T2 (76), NOE (76), S2 (75), tau_e (25), Rex (19) | S2 = 0.811  (Gln2) |
| [`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g) | `NMR_spin_relaxation_and_MF` | `target` | apo, oxidized (disulfide Cys11-Cys14), 2 | T1 (72), T2 (72), NOE (72), S2 (70), tau_e (15), Rex (10) | S2 = 0.795  (Gln2) |
| [`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g) | `NMR_spin_relaxation_and_MF` | `target` | apo, oxidized, 0.48 mM, 62% monomer | S2 (78), T1 (74), T2 (73), NOE (73), tau_e (9), Rex (6) | S2 = 0.824  (Gln2) |
| [`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g) | `Biophysics_and_other` | `target` | apo, oxidized (disulfide Cys11-Cys14), 2 | other (1) | other = 1025 M (whole protein) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **residues needing a two time-scale spectral density function (model 5), 2.3 mM oxidized** ([`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g), sample `S1`): Gln2, Ile5, Asp30, Phe31, Gln32, Gln34, and Val56
- **residues needing a two time-scale spectral density function (model 5), 0.48 mM oxidized** ([`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g), sample `S3`): Asp30, Gln32, Val56, and Leu83
- **residues needing a two time-scale spectral density function (model 5), reduced** ([`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g), sample `S2`): Ile5, Gly7, Asp30, Gln32, Gln34, Asp37, Ile43, Thr44, and Gly71

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g) | 999 | 0 | 3 | 2 | Three 15N relaxation data sets (2.3 mM oxidized, reduced, 0.48 mM oxidized) at 500 MHz, 25 C. Table 1 prints p |

**Explicit figure-only, SI-only, or access gaps (2):**

- Figure 2-5 per-residue values and difference plots (T1, T2, NOE, S2, tau_e, Rex differences) ([`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g)): figure only
- Sedimentation data for each concentration ('data not shown') ([`10.1021/bi962181g`](https://doi.org/10.1021/bi962181g)): not in the text

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
