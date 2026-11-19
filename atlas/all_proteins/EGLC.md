# Eglin C (`EGLC`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P01051` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500/600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

*1 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `population` | 3 % | unfolded protein, pH 3, 37 °C | `Biophysics_and_other` | `same_protein_other_construct` | apo (free); 37 °C; pH 3.0; 500 and 600 | `no` | [`10.1021/bi035015z`](https://doi.org/10.1021/bi035015z) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*16 rows total (15 spin-relaxation/model-free; 1 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi035015z`](https://doi.org/10.1021/bi035015z) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | apo (free) | tau_m (5), S2 (4), T1 (2), T2 (2), other (2) | tau_m = 4.62 ns (global) |
| [`10.1021/bi035015z`](https://doi.org/10.1021/bi035015z) | `Biophysics_and_other` | `same_protein_other_construct` | apo (free) | other (1) | other = 2.1 kcal/mol (free energy of unfolding at pH 3, 37…) |

## 3. Computational (MD/MSM) and cryo-structure (X-ray / cryo-EM) rows

*1 rows intentionally separated from experimental solution dynamics pending expert scope lock:*

| Method group | Quantity | Value | Residues / group | Paper |
|---|---|---|---|---|
| `MD_and_MSM` | `S2` | 0.012 | mean change in methyl Saxis2 from MD, pH 3 minus pH 7 | [`10.1021/bi035015z`](https://doi.org/10.1021/bi035015z) |

## 4. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **line broadening implying microsecond-millisecond conformational exchange** ([`10.1021/bi035015z`](https://doi.org/10.1021/bi035015z), sample `S1`): T1, G4, G40, L45
- **semiflexible binding (reactive site) loop** ([`10.1021/bi035015z`](https://doi.org/10.1021/bi035015z), sample `S1`): 39-49

### Conformational and complex PDB states (`States`)

- [`1EGL`](https://www.rcsb.org/structure/1EGL): NMR solution structure of eglin c (pH 3) used as MD starting structure ([`10.1021/bi035015z`](https://doi.org/10.1021/bi035015z))

## 5. Papers read and explicit gaps

**Checked `v3` / supplemental papers (3):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi035015z`](https://doi.org/10.1021/bi035015z) | 18 | 1 | 2 | 3 | No exchange rates or populations are printed. The paper prints global tau_m at pH 7 and 3, mean backbone S2, m |
| [`10.1002/prot.26750`](https://doi.org/10.1002/prot.26750) | 0 | 0 | 0 | 1 |  |
| [`10.1021/ja1003922`](https://doi.org/10.1021/ja1003922) | 0 | 0 | 0 | 2 | Zero rows. The paper measures amide hydrogen exchange of eglin c and mutants but prints no exchange rates, ope |

**Explicit figure-only, SI-only, or access gaps (6):**

- RMSD, RMSF and interaction-energy values of the bCTRA/CTRL-eglin C simulations ([`10.1002/prot.26750`](https://doi.org/10.1002/prot.26750)): in supplement not available (Table S3 is in the supplement; Figure 1 and Figure 4 are plots)
- per-residue T1, T1rho, NOE, S2, tau_e (backbone) and Saxis2 (methyl) at pH 7 and 3 ([`10.1021/bi035015z`](https://doi.org/10.1021/bi035015z)): figure only: Figures 4, 5, 6
- NMR versus MD order-parameter comparisons ([`10.1021/bi035015z`](https://doi.org/10.1021/bi035015z)): in supplement not available (Supporting Information Figures 1 and 2)
- pH-dependent unfolding curves, Figure 2 (25 and 37 C) ([`10.1021/bi035015z`](https://doi.org/10.1021/bi035015z)): figure only
- Per-residue HX-derived local stabilities (deltaG_HX), changes upon mutation (deltaDeltaG_HX) and site-specifically observed coupling free energies for all variants ([`10.1021/ja1003922`](https://doi.org/10.1021/ja1003922)): figure only (Figure 2, Figure 5, Figure S4 in the supplement); no printed numbers
- Per-residue exchange rates (kex), Molday factors, and exchange mechanism assignments for wild type and mutants ([`10.1021/ja1003922`](https://doi.org/10.1021/ja1003922)): in supplement not available (Figure S1, Table S1)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
