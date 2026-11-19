# Protein PCF11 second N-terminal domain (`PCF11`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P39081` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `700` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*8 rows total (8 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1261/rna.058354.116`](https://doi.org/10.1261/rna.058354.116) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | Zn2+ bound | NOE (3) | NOE = >0.76 dimensionless (residues in the secondary structures) |
| [`10.1038/nsmb.1893`](https://doi.org/10.1038/nsmb.1893) | `NMR_spin_relaxation_and_MF` | `homolog` | free | tau_m (1) | tau_m = 10 ns (whole protein) |
| [`10.1038/nsmb.1893`](https://doi.org/10.1038/nsmb.1893) | `NMR_spin_relaxation_and_MF` | `homolog` | bound to 2-repeat Ser2abP peptide | tau_m (1) | tau_m = 12 ns (whole complex) |
| [`10.1038/nsmb.1893`](https://doi.org/10.1038/nsmb.1893) | `NMR_spin_relaxation_and_MF` | `homolog` | bound to 4-repeat Ser2P peptide (2:1 com | tau_m (1) | tau_m = 16 ns (whole complex) |
| [`10.1038/nsmb.1893`](https://doi.org/10.1038/nsmb.1893) | `NMR_spin_relaxation_and_MF` | `homolog` | bound to 4-repeat Ser2P peptide (1:1) | tau_m (1) | tau_m = 13.3 ns (whole complex) |
| [`10.1038/nsmb.1893`](https://doi.org/10.1038/nsmb.1893) | `NMR_spin_relaxation_and_MF` | `target` | bound to Ser2P CTD peptides | other (1) | other = 50 % percent increase (whole complex) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **conformationally disordered residues outside the folded zinc-binding core; N- and C-terminal residues could not be assigned** ([`10.1093/nar/gkx674`](https://doi.org/10.1093/nar/gkx674), sample `S1`): Pcf11 530-626 outside G548-T603 (N- and C-terminal residues)
- **ps/ns flexibility (low Het-NOE)** ([`10.1261/rna.058354.116`](https://doi.org/10.1261/rna.058354.116), sample `S1`): P554 to A561 (petal 1), E578 and E581 (β4β5 petal 2)
- **µs/ms conformational exchange (larger R2)** ([`10.1261/rna.058354.116`](https://doi.org/10.1261/rna.058354.116), sample `S1`): V583

### Conformational and complex PDB states (`States`)

- [`5M9Z`](https://www.rcsb.org/structure/5M9Z): solution structure ensemble of the second zinc-binding domain (residues 548-603) ([`10.1093/nar/gkx674`](https://doi.org/10.1093/nar/gkx674))
- [`2NAX`](https://www.rcsb.org/structure/2NAX): earlier solution structure of Pcf11 residues 538-608 (same fold, compared to 5M9Z) ([`10.1093/nar/gkx674`](https://doi.org/10.1093/nar/gkx674))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (8):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1038/nsmb.1893`](https://doi.org/10.1038/nsmb.1893) | 5 | 0 | 0 | 1 |  |
| [`10.1261/rna.058354.116`](https://doi.org/10.1261/rna.058354.116) | 3 | 0 | 2 | 1 | The paper measures 15N R1, R2 and Het-NOE on the C-terminal zinc finger ScPcf11 538–608 at 600 MHz, 25°C. Only |
| [`10.1016/j.molcel.2008.12.007`](https://doi.org/10.1016/j.molcel.2008.12.007) | 0 | 0 | 0 | 2 | Zero dynamics rows (expected_rows = []), zero PDB states, and zero dynamic residue lists. This paper studies c |
| [`10.1038/nsmb.2126`](https://doi.org/10.1038/nsmb.2126) | 0 | 0 | 0 | 0 | Zero-row paper: this study investigates how S. cerevisiae Yra1 competes with Clp1 for binding to Pcf11 and reg |
| [`10.1093/nar/gkl1010`](https://doi.org/10.1093/nar/gkl1010) | 0 | 0 | 0 | 0 | Crystal structure paper (2NPI, 2.95 A) of S. cerevisiae Clp1 with Pcf11 454-563. No NMR, HDX, FRET or other dy |
| [`10.1093/nar/gkr801`](https://doi.org/10.1093/nar/gkr801) | 0 | 0 | 0 | 0 | This paper contains 0 dynamics rows, 0 PDB conformational states, 0 dynamic residue sets, and 0 tables. Rather |
| [`10.1093/nar/gkx674`](https://doi.org/10.1093/nar/gkx674) | 0 | 2 | 1 | 0 | The paper reports a solution structure (PDB 5M9Z) of the second zinc-binding domain of Pcf11 plus biochemical  |
| [`10.1101/gad.251470.114`](https://doi.org/10.1101/gad.251470.114) | 0 | 0 | 0 | 0 | This paper (Grzechnik et al., Genes & Development 2015) is a yeast functional genomics, genetics, and molecula |

**Explicit figure-only, SI-only, or access gaps (4):**

- Supplementary methods, Tables 1 and 2 (plasmids and yeast strains), and Supplementary material: 01, 02 (including Figs. S1-S4) ([`10.1016/j.molcel.2008.12.007`](https://doi.org/10.1016/j.molcel.2008.12.007)): in supplement not available
- Main-text Figures 1-7 legends and plotted/gel quantification values ([`10.1016/j.molcel.2008.12.007`](https://doi.org/10.1016/j.molcel.2008.12.007)): figure only
- Pcf11-CID rotational correlation times ([`10.1038/nsmb.1893`](https://doi.org/10.1038/nsmb.1893)): not obtainable: the text says Pcf11-CID partially dimerizes at NMR concentrations and accurate values were not measured; data not shown
- Per-residue R1, R2 and Het-NOE ([`10.1261/rna.058354.116`](https://doi.org/10.1261/rna.058354.116)): figure only (Figure 3E), no printed numbers

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
