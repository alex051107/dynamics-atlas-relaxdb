# Survival motor neuron protein (`SMNTD`)

**Atlas tier:** Tier 3 · Qualitative regions / PDB states / Release 0.1 unknown / twin link / 0-numeric full text  
**UniProt:** `Q16637` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `700/800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **mobile disordered loop with long 15N T2** ([`10.1042/bj20120241`](https://doi.org/10.1042/bj20120241), sample `S1`): Gemin2 residues 150–175
- **disordered SMN N-terminal residues** ([`10.1042/bj20120241`](https://doi.org/10.1042/bj20120241), sample `S1`): SMN residues 26–32

### Conformational and complex PDB states (`States`)

- [`4QQ6`](https://www.rcsb.org/structure/4QQ6): SMN-Cmpd 1 (SMN Tudor domain in complex with compound 1) ([`10.1038/s41467-022-33229-5`](https://doi.org/10.1038/s41467-022-33229-5))
- [`7W2P`](https://www.rcsb.org/structure/7W2P): SMN-Cmpd 4 (SMN Tudor domain in complex with compound 4) ([`10.1038/s41467-022-33229-5`](https://doi.org/10.1038/s41467-022-33229-5))
- [`7W30`](https://www.rcsb.org/structure/7W30): SMN-Cmpd 6 (SMN Tudor domain in complex with compound 6) ([`10.1038/s41467-022-33229-5`](https://doi.org/10.1038/s41467-022-33229-5))
- [`3S6N`](https://www.rcsb.org/structure/3S6N): SMN–Gemin2 bound to the Sm pentamer (crystal structure), compared with the NMR structure of the complex ([`10.1042/bj20120241`](https://doi.org/10.1042/bj20120241))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (5):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1038/ncomms1873`](https://doi.org/10.1038/ncomms1873) | 0 | 0 | 0 | 0 | No molecular dynamics values for SMN. The paper reports force-induced FRET ratio changes and mechanical phase  |
| [`10.1038/s41467-022-33229-5`](https://doi.org/10.1038/s41467-022-33229-5) | 0 | 3 | 0 | 0 | This paper reports small-molecule antagonist discovery, isothermal titration calorimetry (ITC) binding affinit |
| [`10.1042/bj20120241`](https://doi.org/10.1042/bj20120241) | 0 | 1 | 2 | 2 | The paper is a structure and binding study. The only dynamics measurement is a 15N T2 profile shown in Figure  |
| [`10.1371/journal.pone.0030375`](https://doi.org/10.1371/journal.pone.0030375) | 0 | 0 | 0 | 0 | Zero dynamics rows for SMN (Survival motor neuron protein, UniProt Q16637). The paper characterizes peptide-bi |
| [`10.1371/journal.pone.0178519`](https://doi.org/10.1371/journal.pone.0178519) | 0 | 0 | 0 | 0 | Computational analysis of deposited SMN structures (salt bridges, hydrogen bonds, SASA from PDB entries, mostl |

**Explicit figure-only, SI-only, or access gaps (2):**

- Per-residue 15N T2 values of Gemin2 and SMN peptide at 750 MHz ([`10.1042/bj20120241`](https://doi.org/10.1042/bj20120241)): figure only (Figure 2C); the text states only that T2 is relatively long in the 150–175 loop
- SAXS geometric parameters ([`10.1042/bj20120241`](https://doi.org/10.1042/bj20120241)): in supplement not available (Supplementary Figure S3); not dynamics values

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
