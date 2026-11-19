# Barstar (`BARSTAR`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P11540` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Worked deep walkthrough / review case](../v3_previews/16392_and_BARSTAR.md)

> **Audit note:** FIXED 2026-11-19: jacs.0c00807 S1 split into S1 (HyperW pD 7) & S2 (CLEANEX pH 7)

## 1. Experimental conformational exchange (rates, populations, Δω)

*4 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `population` | 4.4 % | P27 cis | `NMR_other` | `same_protein_other_construct` | apo; 270 K (cold-denatured state; CaCON spectrum panel a) | `unclear` | [`10.1002/anie.202006945`](https://doi.org/10.1002/anie.202006945) |
| `population` | 95.6 % | P27 trans | `NMR_other` | `same_protein_other_construct` | apo; 270 K (cold-denatured state; CaCON spectrum panel a) | `unclear` | [`10.1002/anie.202006945`](https://doi.org/10.1002/anie.202006945) |
| `population` | 11 % | P48 cis | `NMR_other` | `same_protein_other_construct` | apo; 270 K (cold-denatured state; CaCON spectrum panel a) | `unclear` | [`10.1002/anie.202006945`](https://doi.org/10.1002/anie.202006945) |
| `population` | 89 % | P48 trans | `NMR_other` | `same_protein_other_construct` | apo; 270 K (cold-denatured state; CaCON spectrum panel a) | `unclear` | [`10.1002/anie.202006945`](https://doi.org/10.1002/anie.202006945) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*3 rows total (0 spin-relaxation/model-free; 3 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/ja307606f`](https://doi.org/10.1021/ja307606f) | `Biophysics_and_other` | `target` | apo, 1.2 M GdnCl | other (3) | other = >0.8 dimensionless (degree of folding) (L20) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **Residues forming the partially solvent-excluded hydrophobic core in the folding intermediate** ([`10.1021/ja307606f`](https://doi.org/10.1021/ja307606f), sample `S1`): I5, H17, L20, L24, F74
- **high HyperW enhancement (fast amide–water exchange) in structured segments, beyond the loop/disordered regions** ([`10.1021/jacs.0c00807`](https://doi.org/10.1021/jacs.0c00807), sample `S1`): I13 and amides in helix-3 and helix-4
- **flexible loop involved in barnase binding** ([`10.1021/jacs.0c00807`](https://doi.org/10.1021/jacs.0c00807), sample `S1`): barnase-binding flexible loop (marked on the sequence in Figure 4A)

### Conformational and complex PDB states (`States`)

- [`1AB7`](https://www.rcsb.org/structure/1AB7): folded native state of barstar, residues colored by slow and fast kinetic phase ([`10.1002/anie.202006945`](https://doi.org/10.1002/anie.202006945))
- [`1AY7`](https://www.rcsb.org/structure/1AY7): native barstar with solvent exposed cisPro48 ([`10.1002/pro.4877`](https://doi.org/10.1002/pro.4877))
- [`1A19`](https://www.rcsb.org/structure/1A19): folded barstar, monomeric crystal structure used for SASA ([`10.1016/j.bbapap.2013.02.023`](https://doi.org/10.1016/j.bbapap.2013.02.023))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (8):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1002/anie.202006945`](https://doi.org/10.1002/anie.202006945) | 4 | 1 | 0 | 2 | Four proline cis/trans population rows (P27, P48) in the cold-denatured state from the CaCON experiment. The p |
| [`10.1021/ja307606f`](https://doi.org/10.1021/ja307606f) | 3 | 0 | 1 | 2 | Mass-spectrometry folding paper with no NMR, HDX, FRET or EPR data and no tables. The only printed per-residue |
| [`10.1002/pro.4877`](https://doi.org/10.1002/pro.4877) | 0 | 1 | 0 | 0 | The paper is a folding-kinetics and stability study of thioredoxin Trx1P (main subject) and pseudo wild-type b |
| [`10.1016/j.bbapap.2013.02.023`](https://doi.org/10.1016/j.bbapap.2013.02.023) | 0 | 1 | 0 | 0 |  |
| [`10.1021/jacs.0c00807`](https://doi.org/10.1021/jacs.0c00807) | 0 | 0 | 2 | 2 | The paper prints no per-residue or global dynamics number for barstar in its text. Barstar amide-water exchang |
| [`10.1038/s41598-017-06507-2`](https://doi.org/10.1038/s41598-017-06507-2) | 0 | 0 | 0 | 0 | The paper is a gas-phase mass spectrometry study of the barnase-barstar complex (CID, in-source H/D exchange,  |
| [`10.1371/journal.pone.0023050`](https://doi.org/10.1371/journal.pone.0023050) | 0 | 0 | 0 | 0 | Zero dynamics rows, samples, methods, states, or residue sets for Barstar (UniProt P11540). The supplied paper |
| [`10.3390/ijms23031867`](https://doi.org/10.3390/ijms23031867) | 0 | 0 | 0 | 0 | This paper compares the structures, catalytic activities, and barstar inhibition of homologous bacterial ribon |

**Explicit figure-only, SI-only, or access gaps (6):**

- Single- and double-exponential refolding rates per residue (Figure 3 A/B), SF-HMQC intermediate decay rates (Figure 4), state-correlated exchange peak intensities (Figure 6) ([`10.1002/anie.202006945`](https://doi.org/10.1002/anie.202006945)): figure only
- Supporting Information figures S1-S9 ([`10.1002/anie.202006945`](https://doi.org/10.1002/anie.202006945)): in supplement not available
- Time-dependent % modification curves and fitted exponential rates per residue (Figures 4-7) ([`10.1021/ja307606f`](https://doi.org/10.1021/ja307606f)): figure only
- Degree-of-folding plot for selected residues (Figure 8) ([`10.1021/ja307606f`](https://doi.org/10.1021/ja307606f)): figure only
- Per-residue amide proton exchange rates kHN from CLEANEX-PM for barstar ([`10.1021/jacs.0c00807`](https://doi.org/10.1021/jacs.0c00807)): figure only (Figure 5B plots kHN against residue; no values printed)
- Per-residue HyperW sensitivity enhancements for barstar ([`10.1021/jacs.0c00807`](https://doi.org/10.1021/jacs.0c00807)): figure only (Figure 4B); the text prints only the range <1x to >300x, an enhancement factor and not a dynamics value

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
