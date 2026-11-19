# Acyl-CoA-binding protein (`ACBP`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P07107` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*10 rows total (2 spin-relaxation/model-free; 8 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/ja302528z`](https://doi.org/10.1021/ja302528z) | `FRET_and_fluorescence` | `same_protein_other_construct` | apo | other (8) | other = 48 µs (ACBP 17-88 W55F (FRET pair)) |
| [`10.1021/bi00251a006`](https://doi.org/10.1021/bi00251a006) | `NMR_spin_relaxation_and_MF` | `target` | apo | tau_m (1) | tau_m = 6.26 ns (whole protein) |
| [`10.1021/bi00251a006`](https://doi.org/10.1021/bi00251a006) | `NMR_spin_relaxation_and_MF` | `target` | holo, bound to palmitoyl-coenzyme A | tau_m (1) | tau_m = 6.35 ns (whole protein) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **exchange contribution to T2 on a time scale slower than 1 ms (effect of shorter CPMG period), apo-ACBP** ([`10.1021/bi00251a006`](https://doi.org/10.1021/bi00251a006), sample `S1`): Ile27 and His30

### Conformational and complex PDB states (`States`)

- [`1HB6`](https://www.rcsb.org/structure/1HB6): native state crystal structure used as simulation starting point and RMSD reference ([`10.1021/ja302528z`](https://doi.org/10.1021/ja302528z))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (2):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/ja302528z`](https://doi.org/10.1021/ja302528z) | 8 | 1 | 0 | 2 | No NMR relaxation or exchange data are printed. The paper gives microsecond refolding relaxation times from FR |
| [`10.1021/bi00251a006`](https://doi.org/10.1021/bi00251a006) | 2 | 0 | 1 | 2 | Two printed dynamics numbers: overall tumbling times for apo- and holo-ACBP from the T1/T2 ratio. Per-residue  |

**Explicit figure-only, SI-only, or access gaps (4):**

- Per-residue 15N T1, T2 and NOE for apo and holo ACBP ([`10.1021/bi00251a006`](https://doi.org/10.1021/bi00251a006)): figure only (Figures 1-3); no tables in the paper
- Supplementary Figure S1, T2 of apo-ACBP with 0.2 and 1.0 ms CPMG periods ([`10.1021/bi00251a006`](https://doi.org/10.1021/bi00251a006)): figure only
- smFRET efficiencies, Rg values and kR, kD+ versus GuHCl curves, diffusion coefficient versus denaturant ([`10.1021/ja302528z`](https://doi.org/10.1021/ja302528z)): figure only
- Fit details of FRET traces, Trp-Cys quenching and gamma factors ([`10.1021/ja302528z`](https://doi.org/10.1021/ja302528z)): in supplement not available

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
