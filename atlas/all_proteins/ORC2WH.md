# Origin recognition complex subunit 2 (`ORC2WH`)

**Atlas tier:** Tier 3 · Qualitative regions / PDB states / Release 0.1 unknown / twin link / 0-numeric full text  
**UniProt:** `Q13416` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `700` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Computational (MD/MSM) and cryo-structure (X-ray / cryo-EM) rows

*2 rows intentionally separated from experimental solution dynamics pending expert scope lock:*

| Method group | Quantity | Value | Residues / group | Paper |
|---|---|---|---|---|
| `Xray_and_CryoEM` | `population` | ~40% % particles | ORC2-WHD State I | [`10.1038/s41421-020-00232-3`](https://doi.org/10.1038/s41421-020-00232-3) |
| `Xray_and_CryoEM` | `population` | ~60% % particles | ORC2-WHD State II | [`10.1038/s41421-020-00232-3`](https://doi.org/10.1038/s41421-020-00232-3) |

## 4. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **dynamic, unresolved ORC3 region near the ATP site** ([`10.7554/elife.58622`](https://doi.org/10.7554/elife.58622), sample `S1`): 86–94
- **dynamic ORC2 loop wrapping around ORC3, unresolved** ([`10.7554/elife.58622`](https://doi.org/10.7554/elife.58622), sample `S1`): aa250-267

### Conformational and complex PDB states (`States`)

- [`5UJ8`](https://www.rcsb.org/structure/5UJ8): HsORC2/3 subcomplex (6.0 Å apo crystal structure; truncated HsORC2 residues 231-577 bound to HsORC3; WHD unplaced) ([`10.7554/elife.20818`](https://doi.org/10.7554/elife.20818))
- [`5UJM`](https://www.rcsb.org/structure/5UJM): active form of HsORC1-5 complex (docked ~20 Å cryo-EM model in EMD-8541, ATPγS-prepared active state containing full-length HsORC2) ([`10.7554/elife.20818`](https://doi.org/10.7554/elife.20818))
- [`4XGC`](https://www.rcsb.org/structure/4XGC): inactive / collapsed DmORC complex state (homolog; DmORC2 WHD in collapsed placement closing central channel to ~15 Å; also used as MR/homology modeling template) ([`10.7554/elife.20818`](https://doi.org/10.7554/elife.20818))

## 5. Papers read and explicit gaps

**Checked `v3` / supplemental papers (4):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1038/s41421-020-00232-3`](https://doi.org/10.1038/s41421-020-00232-3) | 2 | 0 | 0 | 1 | Cryo-EM paper with no NMR, HDX or FRET data and no tables. The only dynamics numbers for ORC2 are the two part |
| [`10.1093/narcan/zcab044`](https://doi.org/10.1093/narcan/zcab044) | 0 | 0 | 0 | 2 | Zero dynamics rows (expected_rows: []), zero PDB conformational states, and zero named dynamic residue sets. T |
| [`10.7554/elife.20818`](https://doi.org/10.7554/elife.20818) | 0 | 3 | 0 | 0 | This structural and biochemical study determines X-ray crystal structures of the HsORC1/4/5 motor module (3.4  |
| [`10.7554/elife.58622`](https://doi.org/10.7554/elife.58622) | 0 | 0 | 2 | 1 |  |

**Explicit figure-only, SI-only, or access gaps (4):**

- Table S1 and Supplementary Figs. S3, S7 (2D class averages, classification trees) ([`10.1038/s41421-020-00232-3`](https://doi.org/10.1038/s41421-020-00232-3)): in supplement not available
- Figure 5A, 5B, 5C, and 5F immunoblot band intensities for ORC2 (PAR-IP capture, PARP1-BirA streptavidin-IP proximity biotinylation, and ORC2-KO / PAR accumulation) ([`10.1093/narcan/zcab044`](https://doi.org/10.1093/narcan/zcab044)): figure only
- Supplementary Methods and Supplementary Tables S1-S3 (cell line media details, primary/secondary antibodies including anti-ORC2 antibody, sgRNA target sequences, and detailed BioID/PAR-IP protocols; zcab044_Supplemental_File) ([`10.1093/narcan/zcab044`](https://doi.org/10.1093/narcan/zcab044)): in supplement not available
- Per-class particle fractions and multibody eigenvector contributions ([`10.7554/elife.58622`](https://doi.org/10.7554/elife.58622)): figure only (Figure 3 and its supplement; Supplementary file 1 not in the text)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
