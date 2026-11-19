# Calcium-dependent protein kinase 3 (`CDK3`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `Q9NJU9` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

*12 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `kex` | 860 s-1 90 | residues with dynamics, mainly N- and C-termini | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | bound to calcium (10 mM CaCl2, 4 mM TCEP); forms dimers; 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |
| `pB` | 1.7 % 0.1 | residues with dynamics, mainly N- and C-termini | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | bound to calcium (10 mM CaCl2, 4 mM TCEP); forms dimers; 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |
| `kex` | 1640 s-1 70 | almost all residues | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | bound to calcium (10 mM CaCl2); 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |
| `pB` | 1.13 % 0.04 | almost all residues | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | bound to calcium (10 mM CaCl2); 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |
| `delta_omega` | 2.1 ppm 1 | average over residues | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | bound to calcium (10 mM CaCl2); 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |
| `delta_omega` | 4.4 ppm | L428 | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | bound to calcium (10 mM CaCl2); 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |
| `delta_omega` | 5.1 ppm | I438 | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | bound to calcium (10 mM CaCl2); 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |
| `delta_omega` | 5.9 ppm | I479 | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | bound to calcium (10 mM CaCl2); 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |
| `kex` | 6900 s-1 | cluster of 8 residues (n = 8), mostly calcium binding loops | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | apo; 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |
| `kex` | 15400 s-1 | cluster of 20 residues (n = 20), mostly helices 1 and 4 | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | apo; 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |
| `kex` | 30800 s-1 | cluster of 8 residues (n = 8) | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | apo; 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |
| `kex` | 57100 s-1 | cluster of 3 residues (n = 3) | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | apo; 25°C; pH 7.1; 500 and 600 | `unclear` | [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*4 rows total (4 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | apo | tau_m (1) | tau_m = 5.3 ns (whole domain) |
| [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | bound to calcium (10 mM CaCl2) | tau_m (1) | tau_m = 5.9 ns (whole domain) |
| [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | bound to calcium (10 mM CaCl2, 4 mM TCEP | tau_m (1) | tau_m = 15.0 ns (whole domain) |
| [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | apo | Rex (1) | Rex = 19 s-1 (39 residues with exchange, average) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **no 15N CPMG exchange in N-lobe Ca (assigned residues without dynamics)** ([`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721), sample `S2`): K422, L452, G469, S470, G471 and D484
- **largest \|ΔϖCPMG\| in N-lobe Ca** ([`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721), sample `S2`): L428, I438, I479
- **1HN R1rho dispersions above 100 s-1 in N-lobe apo** ([`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721), sample `S1`): K435 and I473

### Conformational and complex PDB states (`States`)

- [`3K21`](https://www.rcsb.org/structure/3K21): calcium bound CAD, activated state with the two lobes side by side ([`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721) | 16 | 1 | 3 | 3 | Printed dynamics values are in the Results text and figure captions; the paper has no tables. Rows: three tumb |

**Explicit figure-only, SI-only, or access gaps (3):**

- Per-residue 15N R1, R2 and {1H}-15N NOE for all three samples ([`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721)): figure only (Fig 5)
- Per-residue CPMG and R1rho dispersion fits (kex, phi_ex per residue) ([`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721)): in supplement not available (S2-S4 Figs, figures)
- Per-residue 13CO dispersion results for 21 N-lobe Ca residues ([`10.1371/journal.pone.0181721`](https://doi.org/10.1371/journal.pone.0181721)): figure only (Fig 8B)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
