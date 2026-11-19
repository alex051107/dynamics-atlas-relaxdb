# Plexin-B1 (`PLEXINB1`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `O43157` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600/800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

*1 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `population` | approximately 90% | fraction of protein in dimeric state | `NMR_spin_relaxation_and_MF` | `target` | apo dimer; 298K; pH 6.8; 14.1 and 18.8 T (600/800 MHz) | `yes` | [`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*2153 rows total (2153 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | free (apo), 15N labelled | R1 (226), R2 (226), NOE (226), other (111), Rex (110), tau_e (109) | R1 = 1.506 s-1 (Res 2) |
| [`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | bound to unlabelled Rac1.GMPPNP (C178S,  | R1 (212), NOE (212), R2 (206), other (100), Rex (98), S2 (97) | R1 = 1.896 s-1 (Res 2) |
| [`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f) | `NMR_spin_relaxation_and_MF` | `target` | apo dimer | other (4), R1 (2), R2 (2), NOE (2), tau_m (2), Rex (1) | R1 = 1.55 s−1 (secondary structure elements, averag…) |

## 3. Computational (MD/MSM) and cryo-structure (X-ray / cryo-EM) rows

*3 rows intentionally separated from experimental solution dynamics pending expert scope lock:*

| Method group | Quantity | Value | Residues / group | Paper |
|---|---|---|---|---|
| `MD_and_MSM` | `tau_e` | 0.2 to 1.8 ns | all N–H bonds (MD-derived range) | [`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f) |
| `MD_and_MSM` | `tau_e` | 1 – 3 ns | loops except L2, and terminal chain segments (MD) | [`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f) |
| `MD_and_MSM` | `tau_e` | 0.2 – 0.8 ns | secondary structure elements (MD) | [`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f) |

## 4. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **exchange contribution Rex needed in free RBD** ([`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081), sample `S1`): 82-83 and 92
- **flexible short region in loop L2 (S2 lower)** ([`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081), sample `S1`): 57-60 (residues 50, 54 and 62 also lower)
- **reduced fluctuations in S2 on binding, first region** ([`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081), sample `S2`): 77-84
- **reduced fluctuations in S2 on binding, second region (L2)** ([`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081), sample `S2`): 50-58, with 50, 54, 57 and 62 particularly affected
- **increased flexibility on binding, significant S2 changes** ([`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081), sample `S2`): 91, 93, 96 and 100
- **greater fluctuations in complex, long loop** ([`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081), sample `S2`): 85-87
- **dimerization (L4 loop)** ([`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f), sample `S1`): L77 – L89
- **exchange broadening, residue excluded from analysis** ([`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f), sample `S1`): T38
- **exchange-broadened resonances not detected** ([`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f), sample `S1`): large part of L4 loop and part of alpha2 helix

### Conformational and complex PDB states (`States`)

- [`2JPH`](https://www.rcsb.org/structure/2JPH): solution structure of the free plexin-B1 RBD, used to map S2 ([`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081))
- [`2JPH`](https://www.rcsb.org/structure/2JPH): NMR structure of the W90F RBD monomer mutant, used to build the dimer model ([`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f))
- [`2R2O`](https://www.rcsb.org/structure/2R2O): X-ray crystallographic structure of the RBD dimer (dimerization mini-β-sheet) ([`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f))
- [`2REX`](https://www.rcsb.org/structure/2REX): plexin-B1 RBD in complex with Rnd1 (homodimer in asymmetric unit) ([`10.1074/jbc.m110.197053`](https://doi.org/10.1074/jbc.m110.197053))
- [`2R2O`](https://www.rcsb.org/structure/2R2O): free plexin-B1 RBD ([`10.1074/jbc.m110.197053`](https://doi.org/10.1074/jbc.m110.197053))
- [`3HM6`](https://www.rcsb.org/structure/3HM6): Plexin-B1 apo structure, compared with the Rac1*-bound complex ([`10.1371/journal.pbio.1001134`](https://doi.org/10.1371/journal.pbio.1001134))

## 5. Papers read and explicit gaps

**Checked `v3` / supplemental papers (5):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081) | 2139 | 1 | 6 | 4 |  |
| [`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f) | 18 | 2 | 3 | 3 | The main text prints no per-residue dynamics table; all residue-level R1, R2, NOE, S2, tau_e and SRLS-MD fit v |
| [`10.1038/ncomms15831`](https://doi.org/10.1038/ncomms15831) | 0 | 0 | 0 | 2 | Zero-row cell-biology and optogenetics paper studying mouse Plexin-B1 (ortholog/homolog of human UniProt O4315 |
| [`10.1074/jbc.m110.197053`](https://doi.org/10.1074/jbc.m110.197053) | 0 | 2 | 0 | 0 | Crystallography, gel filtration and ITC paper; no NMR relaxation, kinetic, population or order-parameter value |
| [`10.1371/journal.pbio.1001134`](https://doi.org/10.1371/journal.pbio.1001134) | 0 | 1 | 0 | 0 |  |

**Explicit figure-only, SI-only, or access gaps (9):**

- Table S1 (d) residue 73: R1 0.972 +/- 0.038 and further numbers ([`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081)): garbled table, the line has 8 values for 12 columns and the blank cells cannot be assigned to R2/NOE/field
- Table S2 (b) residue 99, bound state tau_loc and Rex ([`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081)): garbled table, 14 values for 16 columns; bound tau_loc is blank so 7.38 cannot be assigned to tau_loc or Rex; S2 and Sf2 of this line are extracted
- Z-scores and delta S2 for individual residues (114 is Rac1) ([`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081)): in supplement not available in the text (Z-scores) or figure only (Fig. 4)
- Per-residue S2 plots in Fig. 2 and 4 ([`10.1016/j.jmb.2008.01.081`](https://doi.org/10.1016/j.jmb.2008.01.081)): figure only
- Per-residue R1, R2, NOE (Table S2), MF S2/tau_e/Rex (Table S3), SRLS-MD fit values (Tables S4, S5) ([`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f)): in supplement not available
- S2, tau_e, S02, S22, D2perp, D2par, Euler angle profiles (Figures 3-7) ([`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f)): figure only
- Monomer W90F values (tau_m 8.6 ± 0.4 ns) and Rac1 complex values ([`10.1021/jp310142f`](https://doi.org/10.1021/jp310142f)): cited from earlier work, other construct
- Supplementary Table 1 (CRISPR sgRNA and PCR screening sequences) and Supplementary Figs. 1–25 / Supplementary Movies 1–20 ([`10.1038/ncomms15831`](https://doi.org/10.1038/ncomms15831)): in supplement not available (Supplementary Information is not appended to 100.txt; main text indicates these contain cell-migration, fluorescence, and cloning data rather than molecular protein dynamics parameters, including Supplementary Fig. S4b cited in Fig. 6d for live-cell optoPlexin/RhoA indu…
- Quantitative plots in Figures 1–9 (migration separation, Cx index, TIRF fluorescence recruitment/clustering fold-changes, FRET biosensor activation ratios, protrusion/retraction angles and intensities) ([`10.1038/ncomms15831`](https://doi.org/10.1038/ncomms15831)): figure only (and represent cellular/optical signaling readouts rather than NMR or molecular protein dynamics parameters)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
