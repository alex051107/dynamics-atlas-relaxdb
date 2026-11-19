# Thioesterase 1 (`TEPI`)

**Atlas tier:** Tier 3 · Qualitative regions / PDB states / Release 0.1 unknown / twin link / 0-numeric full text  
**UniProt:** `P0ADA1` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500/600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **regions with increased mobility in MD simulations (B factor at or above mean plus one standard deviation)** ([`10.1021/acscatal.7b00408`](https://doi.org/10.1021/acscatal.7b00408), sample `S1`): L11-A19, Q32-S33, G44-D45, N73, I107-R115 and D153-I156
- **switch loop that changes conformation with acyl chain length (on/off)** ([`10.1021/acscatal.7b00408`](https://doi.org/10.1021/acscatal.7b00408), sample `S1`): loop75-80 (G75 to Q80)

### Conformational and complex PDB states (`States`)

- [`9GE8`](https://www.rcsb.org/structure/9GE8): ATP analogue (AMP-PNP)-bound YbbAP-TesA(Ser36Ala) complex ([`10.1371/journal.pbio.3003427`](https://doi.org/10.1371/journal.pbio.3003427))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (2):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/acscatal.7b00408`](https://doi.org/10.1021/acscatal.7b00408) | 0 | 0 | 2 | 2 | Computational enzyme redesign paper with in vivo fatty acid profiles, crystal structures and MD simulations. N |
| [`10.1371/journal.pbio.3003427`](https://doi.org/10.1371/journal.pbio.3003427) | 0 | 1 | 0 | 5 | Zero expected dynamics rows: this paper identifies Escherichia coli TesA (Thioesterase 1, P0ADA1) as the perip |

**Explicit figure-only, SI-only, or access gaps (7):**

- MD-derived B factors per residue and RMSD versus position plots ([`10.1021/acscatal.7b00408`](https://doi.org/10.1021/acscatal.7b00408)): figure only; no numeric values printed in the text
- Crystallography and MD tables (Tables S1 to S6) ([`10.1021/acscatal.7b00408`](https://doi.org/10.1021/acscatal.7b00408)): in supplement not available in the text
- S1 Methods extended sample preparation, cryo-EM grid/imaging, in vivo/PaTesA assay conditions, and MD setup details ([`10.1371/journal.pbio.3003427`](https://doi.org/10.1371/journal.pbio.3003427)): in supplement not available
- S1 Table coevolving residue pairs predicted between YbbA, YbbP, and TesA ([`10.1371/journal.pbio.3003427`](https://doi.org/10.1371/journal.pbio.3003427)): in supplement not available
- S2 Table cryo-EM data collection and model refinement statistics (including PDB 9GE8) ([`10.1371/journal.pbio.3003427`](https://doi.org/10.1371/journal.pbio.3003427)): in supplement not available
- S3 Table antibiotic susceptibility testing for TesA and YbbP knockout and YbbAP-TesA overexpression strains ([`10.1371/journal.pbio.3003427`](https://doi.org/10.1371/journal.pbio.3003427)): in supplement not available
- Fig 4A-E, Fig 5A, and S5B-C Fig enzymatic hydrolysis curves and PaTesA single-exponential rate fit (S4 Data-S9 Data, S12 Data-S13 Data) ([`10.1371/journal.pbio.3003427`](https://doi.org/10.1371/journal.pbio.3003427)): figure only; underlying data in supplement not available

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
