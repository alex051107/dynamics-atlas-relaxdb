# Cerebral dopamine neurotrophic factor, saposin-like domain (`CDNFSP`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `Q49AH0` · **RelaxDB deposited card:** T = `298.0`, field = `800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*5 rows total (5 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1074/jbc.m115.662254`](https://doi.org/10.1074/jbc.m115.662254) | `NMR_spin_relaxation_and_MF` | `target` | apo | other (4), NOE (1) | other = 30 Hz (N-terminal domain structured residue…) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **extreme amide 1H line broadening, millisecond-scale chemical exchange** ([`10.1074/jbc.m115.662254`](https://doi.org/10.1074/jbc.m115.662254), sample `S1`): 11-16, 68-73, 88, 99-101, 132-133, 138
- **pico- to nanosecond fluctuations, N and C termini** ([`10.1074/jbc.m115.662254`](https://doi.org/10.1074/jbc.m115.662254), sample `S1`): N-terminal 4-9 and C-terminal 158-161
- **pico- to nanosecond fluctuations, decreased NOE** ([`10.1074/jbc.m115.662254`](https://doi.org/10.1074/jbc.m115.662254), sample `S1`): Ser-33, Leu-34, Thr-48, Leu-55, Ala-66
- **nano- to millisecond motions (R2/R1 variation, normal NOE)** ([`10.1074/jbc.m115.662254`](https://doi.org/10.1074/jbc.m115.662254), sample `S1`): Leu-41, Cys-45, Leu-46, Gly-60, Asp-112, Leu-125, Tyr-141, Tyr-152, Ala-154, Thr-155
- **flexible interdomain linker, NOE below average** ([`10.1074/jbc.m115.662254`](https://doi.org/10.1074/jbc.m115.662254), sample `S1`): 103-113
- **dynamic surface patch 1 on N-terminal domain** ([`10.1074/jbc.m115.662254`](https://doi.org/10.1074/jbc.m115.662254), sample `S1`): Ser-33, Leu-34, Gly-60, Ala-66, Lys-68, Ile-69, Leu-70, Ser-71, Glu-72

### Conformational and complex PDB states (`States`)

- [`4BIT`](https://www.rcsb.org/structure/4BIT): solution NMR structure of full-length CDNF (20 conformers, two semi-independent domains) ([`10.1074/jbc.m115.662254`](https://doi.org/10.1074/jbc.m115.662254))
- [`2W50`](https://www.rcsb.org/structure/2W50): earlier X-ray structure of the N-terminal domain (residues 1-107), dimer under crystallization conditions ([`10.1074/jbc.m115.662254`](https://doi.org/10.1074/jbc.m115.662254))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (7):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1074/jbc.m115.662254`](https://doi.org/10.1074/jbc.m115.662254) | 5 | 2 | 6 | 1 | One full-length CDNF sample; dynamics are reported as averages (1H line width, R2/R1) and one overall NOE mean |
| [`10.1016/j.ymthe.2021.04.035`](https://doi.org/10.1016/j.ymthe.2021.04.035) | 0 | 0 | 0 | 1 | The paper prints no dynamics value for CDNF. NMR is used only for chemical shift perturbation on binding alpha |
| [`10.1038/s41467-024-52478-0`](https://doi.org/10.1038/s41467-024-52478-0) | 0 | 0 | 0 | 0 | The paper is a SAXS/binding study. Its only NMR experiment is a methyl HSQC titration of Ala-labeled C-CDNF wi |
| [`10.1093/brain/awad087`](https://doi.org/10.1093/brain/awad087) | 0 | 0 | 0 | 0 | This preclinical neurobiology study tests exogenous human CDNF (and tracks 125I-labelled CDNF diffusion and en |
| [`10.1371/journal.pone.0073928`](https://doi.org/10.1371/journal.pone.0073928) | 0 | 0 | 0 | 0 | Zero protein dynamics measurements (0 expected rows, 0 PDB states, 0 dynamic residue sets): this paper studies |
| [`10.1523/eneuro.0117-16.2017`](https://doi.org/10.1523/eneuro.0117-16.2017) | 0 | 0 | 0 | 0 | This paper tests the neurorestorative and ER-stress signaling effects of full-length human recombinant CDNF an |
| [`10.3390/ijms23169489`](https://doi.org/10.3390/ijms23169489) | 0 | 0 | 0 | 0 | This paper investigates human CDNF constructs (full-length wild type, C135S/C134S and ΔKTEL mutants, SH-tagged |

**Explicit figure-only, SI-only, or access gaps (2):**

- Residues without backbone amide signals due to intermediate conformational dynamics (black dots in Figure 2C) ([`10.1016/j.ymthe.2021.04.035`](https://doi.org/10.1016/j.ymthe.2021.04.035)): figure only; no residue list or exchange rate printed
- Per-residue 1H line widths, R2/R1, 15N{1H}-NOE and local displacements ([`10.1074/jbc.m115.662254`](https://doi.org/10.1074/jbc.m115.662254)): figure only (Fig. 2A-D), no printed numbers

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
