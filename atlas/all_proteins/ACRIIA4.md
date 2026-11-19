# anti-CRISPR protein AcrIIA4 (`ACRIIA4`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `A0A247D711` · **RelaxDB deposited card:** T = `n/a`, field = `800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*1 rows total (1 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1038/s41598-018-22177-0`](https://doi.org/10.1038/s41598-018-22177-0) | `NMR_spin_relaxation_and_MF` | `target` | free (apo) | tau_c (1) | tau_c = 6.2 ns (ordered region) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **fast ps-ns motion, low NOE** ([`10.1038/s41598-018-22177-0`](https://doi.org/10.1038/s41598-018-22177-0), sample `S1`): beta1-beta2 loop (Gly21-Ile27)
- **us-ms conformational exchange from increased R2** ([`10.1038/s41598-018-22177-0`](https://doi.org/10.1038/s41598-018-22177-0), sample `S1`): Thr22, Asn23, Ser26 (beta1-beta2); Asn48, Ser50 (beta3-alpha2); Gly62, Glu68 (alpha2-alpha3)
- **exchange broadening beyond detection** ([`10.1038/s41598-018-22177-0`](https://doi.org/10.1038/s41598-018-22177-0), sample `S1`): Ser20, Ser24, Thr28, Gln29; Glu47; Gln65

### Conformational and complex PDB states (`States`)

- [`5XBL`](https://www.rcsb.org/structure/5XBL): AcrIIA4 in AcrIIA4-SpyCas9-sgRNA complex crystal structure ([`10.1038/s41598-018-22177-0`](https://doi.org/10.1038/s41598-018-22177-0))
- [`5VW1`](https://www.rcsb.org/structure/5VW1): AcrIIA4 in AcrIIA4-SpyCas9-sgRNA complex crystal structure ([`10.1038/s41598-018-22177-0`](https://doi.org/10.1038/s41598-018-22177-0))
- [`5VW1`](https://www.rcsb.org/structure/5VW1): in complex with Cas9 ([`10.1093/nar/gkae1052`](https://doi.org/10.1093/nar/gkae1052))
- [`5VZL`](https://www.rcsb.org/structure/5VZL): Cas9-sgRNA-AcrIIA4 complex ([`10.1126/sciadv.1701620`](https://doi.org/10.1126/sciadv.1701620))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (4):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1038/s41598-018-22177-0`](https://doi.org/10.1038/s41598-018-22177-0) | 1 | 2 | 3 | 2 | One scalar dynamics value is printed (tau_c 6.2 ns); all per-residue R1, R2 and NOE data are in Fig. 2 only. T |
| [`10.1093/nar/gkae1052`](https://doi.org/10.1093/nar/gkae1052) | 0 | 1 | 0 | 4 | This paper presents an E. coli CRISPRi Flow-seq deep mutational scanning (DMS) pipeline applied to AcrIIA4 (an |
| [`10.1126/sciadv.1701620`](https://doi.org/10.1126/sciadv.1701620) | 0 | 1 | 0 | 1 | Zero-row structural, biochemical, biophysical, and cellular inhibition study of the 87-amino-acid anti-CRISPR  |
| [`10.1126/sciadv.aay0187`](https://doi.org/10.1126/sciadv.aay0187) | 0 | 0 | 0 | 3 | This study investigates CRISPR-Cas9 genome-editing specificity regulated by coexpressed or covalently fused an |

**Explicit figure-only, SI-only, or access gaps (10):**

- Per-residue 15N R1, R2 and heteronuclear NOE ([`10.1038/s41598-018-22177-0`](https://doi.org/10.1038/s41598-018-22177-0)): figure only (Fig. 2)
- Intensity ratios Ibound/Ifree upon 10% Cas9 binding ([`10.1038/s41598-018-22177-0`](https://doi.org/10.1038/s41598-018-22177-0)): figure only (Fig. 5)
- Far-UV CD spectra (190-250 nm) and thermal denaturation curves (ellipticity at 220 nm from 20-90°C) for AcrIIA4 WT, N25G, G38C, Y67K, E70D, and E70T ([`10.1093/nar/gkae1052`](https://doi.org/10.1093/nar/gkae1052)): in supplement not available (Supplementary Figure S7; no numerical Tm or ellipticity values printed in main text)
- BLI Cas9 RNP binding affinities and association/dissociation kinetics for AcrIIA4 WT, N25G, G38C, Y67K, E70D, and E70T ([`10.1093/nar/gkae1052`](https://doi.org/10.1093/nar/gkae1052)): figure only and in supplement not available (plotted in Figure 7A and Supplementary Figure S8; no numerical Kd, kon, or koff values printed in text)
- Per-mutant AcrIIA4 DMS predicted log mean fluorescence activities, standard deviations, 16 benchmark mutant identities, SDS-PAGE expression gel, and individual HEK293T luciferase/TIDE indel values ([`10.1093/nar/gkae1052`](https://doi.org/10.1093/nar/gkae1052)): figure only and in supplement not available (Figures 4A-C, 5A-D, 7B-D; Supplementary Figures S2-S6, S9; Supplementary data 2-6)
- Supplementary Tables T1-T4 (plasmids, sgRNA target sequences, transformation efficiency and library complexity) ([`10.1093/nar/gkae1052`](https://doi.org/10.1093/nar/gkae1052)): in supplement not available (non-dynamics cloning/library metadata; no table captions or bodies present in main text)
- table S1 (cryo-EM data collection and PHENIX real-space/atomic displacement parameter refinement statistics for SpyCas9-sgRNA-AcrIIA4) ([`10.1126/sciadv.1701620`](https://doi.org/10.1126/sciadv.1701620)): in supplement not available
- Table S7 (Parameter estimates and confidence intervals of the cellular ODE models, including kinh,CascAID, relative inhibition factors γj for Cas-Acr wt/Ins. 5/N39A/D14A/G38A, kdeg,C, Kd,gRNA, koff,target,i, and kon,target) ([`10.1126/sciadv.aay0187`](https://doi.org/10.1126/sciadv.aay0187)): in supplement not available (body resides in external supplementary PDF at http://advances.sciencemag.org/cgi/content/full/6/6/eaay0187/DC1; also macroscopic cellular gene-editing ODE parameters rather than biophysical protein conformational dynamics)
- Table S1, Table S2, Table S3, Table S4, Table S5, Table S6, Data file S1, and Data file S2 (Cas9 and Cas-Acr ODE equations, AcrIIA4-LOV2 hybrid overview, plasmid list including all 10 prescreened Cas-Acr constructs, sgRNA target sites, PCR primers, GenBank vector files, and MATLAB simulation script… ([`10.1126/sciadv.aay0187`](https://doi.org/10.1126/sciadv.aay0187)): in supplement not available (only listed by title under SUPPLEMENTARY MATERIALS in 196.txt)
- Fig. 1D–F, Fig. 2B–G, Fig. 3, Fig. 4B–F, and figs. S1–S12 (plotted InDel % genome-editing efficiencies, cellular Cas9-GFP / mCherry-AcrIIA4 molecule numbers, and ODE model simulation/fit curves) ([`10.1126/sciadv.aay0187`](https://doi.org/10.1126/sciadv.aay0187)): figure only (main-text plots have no printed numerical data tables; figs. S1–S12 are in the unavailable supplement; additionally these measure cellular genome editing and protein copy-number expression rather than conformational dynamics)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
