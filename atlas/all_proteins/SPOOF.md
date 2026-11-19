# Sporulation initiation phosphotransferase F (`SPOOF`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P06628` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*9 rows total (9 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1038/22357`](https://doi.org/10.1038/22357) | `NMR_spin_relaxation_and_MF` | `target` | apo | other (2), Rex (2), R1 (1), R2 (1), NOE (1), S2 (1) | R1 = 1:49 s-1 (all 108 analysed backbone amides (10…) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **slow-timescale conformational exchange term (model 3) in the previous study residues** ([`10.1038/22357`](https://doi.org/10.1038/22357), sample `S1`): D11 to G14, R16 to G27, T82, K94, T100 and F102
- **significant Rex terms matching alanine-scan functional residues** ([`10.1038/22357`](https://doi.org/10.1038/22357), sample `S1`): D11, Y13, I15, R16, L18, L19, M55, K56, M81, T82, I90, H101, F106
- **large Rex terms, slow ring exchange of H101** ([`10.1038/22357`](https://doi.org/10.1038/22357), sample `S1`): T82, G85, K94, T100, F102
- **b3-a3 loop flapping, Rex at extremities** ([`10.1038/22357`](https://doi.org/10.1038/22357), sample `S1`): M55, K56, D61
- **residues not fitting any model-free model** ([`10.1038/22357`](https://doi.org/10.1038/22357), sample `S1`): I17, H101, K104, F106
- **crystal disorder of the Spo0FB β4-α4 loop, helix α4 and part of the α4-β5 loop (non-phosphorylated-like copy)** ([`10.1371/journal.pbio.1000589`](https://doi.org/10.1371/journal.pbio.1000589), sample `S1`): Spo0FB 83–98

### Conformational and complex PDB states (`States`)

- [`1FSP`](https://www.rcsb.org/structure/1FSP): free (inactive) wild-type Spo0F ([`10.1016/j.febslet.2010.08.051`](https://doi.org/10.1016/j.febslet.2010.08.051))
- [`1PUX`](https://www.rcsb.org/structure/1PUX): BeF3 bound (active) Spo0F ([`10.1016/j.febslet.2010.08.051`](https://doi.org/10.1016/j.febslet.2010.08.051))
- [`2JVK`](https://www.rcsb.org/structure/2JVK): L66A mutant ([`10.1016/j.febslet.2010.08.051`](https://doi.org/10.1016/j.febslet.2010.08.051))
- [`2JVJ`](https://www.rcsb.org/structure/2JVJ): I90A mutant ([`10.1016/j.febslet.2010.08.051`](https://doi.org/10.1016/j.febslet.2010.08.051))
- [`2JVI`](https://www.rcsb.org/structure/2JVI): H101A mutant ([`10.1016/j.febslet.2010.08.051`](https://doi.org/10.1016/j.febslet.2010.08.051))
- [`2fsp`](https://www.rcsb.org/structure/2fsp): average solution structure of apo-Spo0F (earlier NMR structure, ref. 10) used to map te and Rex residues ([`10.1038/22357`](https://doi.org/10.1038/22357))
- [`1PEY`](https://www.rcsb.org/structure/1PEY): Spo0F bound to Mn2+ (reference conformation; RapH-bound Spo0F shows shifted beta4-alpha4 loop) ([`10.1371/journal.pbio.1000589`](https://doi.org/10.1371/journal.pbio.1000589))
- [`3Q15`](https://www.rcsb.org/structure/3Q15): RapH-Spo0F complex (new deposit; Spo0FA 'phosphorylated'-like and Spo0FB 'non-phosphorylated'-like conformations in the asymmetric unit) ([`10.1371/journal.pbio.1000589`](https://doi.org/10.1371/journal.pbio.1000589))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (4):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1038/22357`](https://doi.org/10.1038/22357) | 9 | 1 | 5 | 1 | Short Nature letter with no numbered tables. Printed dynamics numbers are mean R1, R2, NOE, R2/R1, S2, overall |
| [`10.1016/j.febslet.2010.08.051`](https://doi.org/10.1016/j.febslet.2010.08.051) | 0 | 5 | 0 | 1 | The paper solves NMR structures of three Spo0F mutants and probes dynamics only by tCONCOORD simulation and PC |
| [`10.1016/j.jmb.2010.03.001`](https://doi.org/10.1016/j.jmb.2010.03.001) | 0 | 0 | 0 | 0 | The paper reports urea-dependent folding and unfolding kinetics (CD, fluorescence, stopped-flow) and Go-model  |
| [`10.1371/journal.pbio.1000589`](https://doi.org/10.1371/journal.pbio.1000589) | 0 | 2 | 1 | 0 | X-ray crystallography paper (RapH-Spo0F complex, 2.20 A). It prints no NMR, HDX, FRET or other dynamics value  |

**Explicit figure-only, SI-only, or access gaps (2):**

- tCONCOORD motional propensity and PCA clusters for wild type and mutants ([`10.1016/j.febslet.2010.08.051`](https://doi.org/10.1016/j.febslet.2010.08.051)): figure only (Fig. 3, Supplementary Figs. S2, S3); no printed numbers
- Per-residue R1, R2, NOE, S2, te, Rex (108 residues) ([`10.1038/22357`](https://doi.org/10.1038/22357)): figure only (Figs 1, 2); numbers deposited in Supplementary Information / Indiana Dynamics Database, not in text

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
