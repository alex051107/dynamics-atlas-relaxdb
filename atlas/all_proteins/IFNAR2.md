# Interferon alpha/beta receptor 2 (`IFNAR2`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P48551` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500/800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*82 rows total (82 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi049606g`](https://doi.org/10.1021/bi049606g) | `NMR_spin_relaxation_and_MF` | `target` | apo (free) | S2 (28), R1 (12), R2 (12), NOE (12), other (9), tau_e (4) | R1 = 1.01 s-1 (core residues (NOE cutoff, well-defi…) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **hinge region (rigid)** ([`10.1021/bi049606g`](https://doi.org/10.1021/bi049606g), sample `S1`): 16-22, 104-111, 183, 185, 194 and 196
- **residues with exchange contribution Rex in the hinge** ([`10.1021/bi049606g`](https://doi.org/10.1021/bi049606g), sample `S1`): S17, R22, E108
- **model 5 in unstructured termini** ([`10.1021/bi049606g`](https://doi.org/10.1021/bi049606g), sample `S1`): 3-10 and 206-212
- **model 5 in CC'N loop of binding site** ([`10.1021/bi049606g`](https://doi.org/10.1021/bi049606g), sample `S1`): 50-52
- **model 5 in EFN loop of binding site** ([`10.1021/bi049606g`](https://doi.org/10.1021/bi049606g), sample `S1`): E77, A78
- **HN cross-peak signal attenuation upon IFNα2 binding** ([`10.1021/bi100041f`](https://doi.org/10.1021/bi100041f), sample `S2`): residues 187–198 (S13–S14 loop of the C-domain of IFNAR2)
- **flexible N-terminal residues** ([`10.1021/ja205480v`](https://doi.org/10.1021/ja205480v), sample `S1`): R2S1-R2C12
- **flexible C-terminal residues** ([`10.1021/ja205480v`](https://doi.org/10.1021/ja205480v), sample `S1`): R2P204-R2S212

### Conformational and complex PDB states (`States`)

- [`1N6V`](https://www.rcsb.org/structure/1N6V): free (unliganded) solution structure of IFNAR2-EC, used for the inertia tensor ([`10.1021/bi049606g`](https://doi.org/10.1021/bi049606g))
- [`1N6U`](https://www.rcsb.org/structure/1N6U): free IFNAR2 (published NMR structure used as starting structure for docking) ([`10.1021/bi100041f`](https://doi.org/10.1021/bi100041f))
- [`1N6U`](https://www.rcsb.org/structure/1N6U): free IFNAR2 (published starting structure for docking) ([`10.1021/ja205480v`](https://doi.org/10.1021/ja205480v))
- [`2LAG`](https://www.rcsb.org/structure/2LAG): IFNAR2/IFNα2 complex (new docking model) ([`10.1021/ja205480v`](https://doi.org/10.1021/ja205480v))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (5):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi049606g`](https://doi.org/10.1021/bi049606g) | 82 | 1 | 5 | 2 | 15N R1, R2, NOE and model-free order parameters of IFNAR2-EC at 500 and 800 MHz, printed only as domain averag |
| [`10.1016/j.cell.2011.06.048`](https://doi.org/10.1016/j.cell.2011.06.048) | 0 | 0 | 0 | 6 | This structural and functional study reports crystal structures of human IFNAR2 (apo IFNAR2-D2 at 2.6 Å, the I |
| [`10.1021/bi100041f`](https://doi.org/10.1021/bi100041f) | 0 | 1 | 1 | 2 | This paper applies asymmetric reverse-protonation on a deuterated 15N background with 2D homonuclear NOESY (al |
| [`10.1021/bi901313x`](https://doi.org/10.1021/bi901313x) | 0 | 0 | 0 | 0 | Zero-row extraction for IFNAR2 (UniProt P48551): the paper records 2D [1H,15N]-TROSY-HSQC spectra on uniformly |
| [`10.1021/ja205480v`](https://doi.org/10.1021/ja205480v) | 0 | 2 | 2 | 0 | Zero quantitative dynamics rows (expected_rows is empty): this paper introduces a 2D homonuclear 1H-1H double- |

**Explicit figure-only, SI-only, or access gaps (10):**

- Table S1 (crystallographic data collection/refinement statistics and PDB accession codes for newly solved IFNAR2-D2, IFNα2(HEQ)-IFNAR2, IFNα2(YNS) ternary, and IFNω(N80Q) ternary structures) ([`10.1016/j.cell.2011.06.048`](https://doi.org/10.1016/j.cell.2011.06.048)): in supplement not available
- Table S2 (SPR binding affinities and mutational energetic maps for IFNAR2 and IFNα2/IFNω interface mutants) ([`10.1016/j.cell.2011.06.048`](https://doi.org/10.1016/j.cell.2011.06.048)): in supplement not available
- Figure S2 and Figure S3 (electron density maps, conformational changes between free and bound states, and IFNAR1 SD4 modeling) ([`10.1016/j.cell.2011.06.048`](https://doi.org/10.1016/j.cell.2011.06.048)): in supplement not available
- Figure S4 (double mutant cycle thermodynamic coupling analyses between Glu77 of IFNAR2 and Lys152 of IFNω) ([`10.1016/j.cell.2011.06.048`](https://doi.org/10.1016/j.cell.2011.06.048)): in supplement not available
- Figure 8C (surface IFNAR2 expression levels on Ramos cells 5 min after IFN stimulation; only summary values 60% and ~50% appear in prose, and this measures cellular receptor endocytosis rather than molecular protein dynamics) ([`10.1016/j.cell.2011.06.048`](https://doi.org/10.1016/j.cell.2011.06.048)): figure only
- Figure 8D (time course of decrease of p-STAT3 activation after IFN stimulation; cellular signaling kinetics) ([`10.1016/j.cell.2011.06.048`](https://doi.org/10.1016/j.cell.2011.06.048)): figure only
- Per-residue R1, R2, NOE, S2, tau_i, Rex at 11.74 and 18.79 T ([`10.1021/bi049606g`](https://doi.org/10.1021/bi049606g)): in supplement not available (Supplements 1-4) and plotted in Figures 1, 3, 4 only
- Table 2 theta and phi angles of the diffusion axis, and Table 3 model-assignment counts ([`10.1021/bi049606g`](https://doi.org/10.1021/bi049606g)): orientation angles and model counts, not dynamics amplitudes; left out as rows (see notes)
- Attempted RDC measurements of IFNAR2/IFNα2 in negatively charged polyacrylamide gel ([`10.1021/bi100041f`](https://doi.org/10.1021/bi100041f)): figure only / unprinted in text: spectra exhibited low S/N yielding only a small number of RDCs mostly for residues in flexible regions, omitted from structure calculation and not numerically printed in 083.txt (line 92).
- Supporting Information Figures 1S and 2S and main-text Figures 1–9 ([`10.1021/bi100041f`](https://doi.org/10.1021/bi100041f)): in supplement not available / figure only: figure images, NMR spectra, and figure captions are absent from 083.txt (only Supplementary Material 1_si_001 Tables 1–4 are included).

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
