# PI3-kinase regulatory alpha subunit (`PI3KSH2`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P27986` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `700` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*33 rows total (0 spin-relaxation/model-free; 33 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi902171d`](https://doi.org/10.1021/bi902171d) | `EPR_DEER` | `same_protein_other_construct` | apo (no p110α or phosphopeptide) | other (32) | other = 3.41 nm (spin labels at 448 and 330) |
| [`10.1021/bi902171d`](https://doi.org/10.1021/bi902171d) | `EPR_DEER` | `same_protein_other_construct` | apo | other (1) | other = 1.37 nm (intra-nSH2 spin labels 337 and 410) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **nSH2 helix protected in p110α complex; contact with kinase C-lobe released by pY** ([`10.1016/j.jbior.2012.09.005`](https://doi.org/10.1016/j.jbior.2012.09.005), sample `S1`): 339–347
- **BH domain peptide exposed on pY binding** ([`10.1016/j.jbior.2012.09.005`](https://doi.org/10.1016/j.jbior.2012.09.005), sample `S1`): 149–158
- **p85α peptides with increased exchange on PDGFR pY binding (candidate contact surface with p110δ)** ([`10.1016/j.str.2011.06.003`](https://doi.org/10.1016/j.str.2011.06.003), sample `S1`): 444–456 in the beginning of the iSH2 and 681–687 in the cSH2
- **p85α iSH2 regions with increased exchange in presence of lipid vesicles** ([`10.1016/j.str.2011.06.003`](https://doi.org/10.1016/j.str.2011.06.003), sample `S1`): 467–476 and 556–570
- **p85alpha iSH2 N- and C-terminal ends gain exchange upon membrane binding (C2-iSH2 interface)** ([`10.1038/s41467-023-35789-6`](https://doi.org/10.1038/s41467-023-35789-6), sample `S1`): p85α iSH2 470–476 and 556–570

### Conformational and complex PDB states (`States`)

- [`5UL1`](https://www.rcsb.org/structure/5UL1): inactive PI3Kα, collapsed a-loop with full density, nSH2 present ([`10.1016/j.jmb.2020.09.002`](https://doi.org/10.1016/j.jmb.2020.09.002))
- [`5DXH`](https://www.rcsb.org/structure/5DXH): active PI3Kα, extended a-loop, nSH2 absent ([`10.1016/j.jmb.2020.09.002`](https://doi.org/10.1016/j.jmb.2020.09.002))
- [`4L1B`](https://www.rcsb.org/structure/4L1B): inactive PI3Kα conformation ([`10.1016/j.jmb.2020.09.002`](https://doi.org/10.1016/j.jmb.2020.09.002))
- [`3HHM`](https://www.rcsb.org/structure/3HHM): PI3Kα H1047R mutant with nSH2, a-loop extended, kα11 OUT ([`10.1016/j.jmb.2020.09.002`](https://doi.org/10.1016/j.jmb.2020.09.002))
- [`3HIZ`](https://www.rcsb.org/structure/3HIZ): PI3Kα H1047R mutant with nSH2, a-loop extended, kα11 OUT ([`10.1016/j.jmb.2020.09.002`](https://doi.org/10.1016/j.jmb.2020.09.002))
- [`2RD0`](https://www.rcsb.org/structure/2RD0): nSH2 included but lacking full density; inactive conformation (collapsed a-loop, IN kα11) ([`10.1016/j.jmb.2020.09.002`](https://doi.org/10.1016/j.jmb.2020.09.002))
- [`4A55`](https://www.rcsb.org/structure/4A55): nSH2 included but lacking full density; inactive conformation (collapsed a-loop, IN kα11) ([`10.1016/j.jmb.2020.09.002`](https://doi.org/10.1016/j.jmb.2020.09.002))
- [`4OVU`](https://www.rcsb.org/structure/4OVU): inhibited WT p110alpha-p85alpha complex ([`10.1038/s41467-023-35789-6`](https://doi.org/10.1038/s41467-023-35789-6))
- [`3HHM`](https://www.rcsb.org/structure/3HHM): H1047R p110alpha/p85alpha structure with reoriented C-terminus ([`10.1038/s41467-023-35789-6`](https://doi.org/10.1038/s41467-023-35789-6))
- [`8DCP`](https://www.rcsb.org/structure/8DCP): p110α-p85α complex in the inhibited conformation (p85 iSH2 and nSH2 contacts) ([`10.1038/s42003-026-09540-y`](https://doi.org/10.1038/s42003-026-09540-y))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (10):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi902171d`](https://doi.org/10.1021/bi902171d) | 33 | 0 | 0 | 2 | DEER (EPR) distances between spin-label pairs across the nSH2 and iSH2 domains of p85ni: 16 pairs in Table 1,  |
| [`10.1016/j.jbior.2012.09.005`](https://doi.org/10.1016/j.jbior.2012.09.005) | 0 | 0 | 2 | 1 | The paper reports HDX-MS of p110/p85α complexes with and without a pY peptide. All deuteration levels are in f |
| [`10.1016/j.jmb.2020.09.002`](https://doi.org/10.1016/j.jmb.2020.09.002) | 0 | 7 | 0 | 0 | The paper is a comparative analysis of deposited PI3K crystal structures. It prints no rate, population, order |
| [`10.1016/j.str.2011.06.003`](https://doi.org/10.1016/j.str.2011.06.003) | 0 | 0 | 2 | 1 | The paper is an HDX-MS (DXMS) study. It prints deuterium-uptake differences in Da for peptides, no exchange ra |
| [`10.1021/acs.biochem.7b01130`](https://doi.org/10.1021/acs.biochem.7b01130) | 0 | 0 | 0 | 0 | The paper is an NMR and fluorescence binding study of calmodulin with the p85alpha cSH2 domain. It prints no k |
| [`10.1021/acsomega.3c09212`](https://doi.org/10.1021/acsomega.3c09212) | 0 | 0 | 0 | 0 | This medicinal-chemistry paper synthesizes and characterizes 16 2-aminobenzothiazole derivatives (OMS1–OMS16), |
| [`10.1038/s41467-023-35789-6`](https://doi.org/10.1038/s41467-023-35789-6) | 0 | 2 | 1 | 1 | HDX-MS paper on p110alpha/p85alpha. It prints peptide-level difference criteria and residue ranges but no rate |
| [`10.1038/s42003-026-09540-y`](https://doi.org/10.1038/s42003-026-09540-y) | 0 | 1 | 0 | 0 | No dynamics value is printed for the PI3K p85 regulatory subunit. The paper reports ITC thermodynamics, NMR ch |
| [`10.1042/bcj20240479`](https://doi.org/10.1042/bcj20240479) | 0 | 0 | 0 | 0 |  |
| [`10.2147/dddt.s494066`](https://doi.org/10.2147/dddt.s494066) | 0 | 0 | 0 | 0 | Zero dynamics rows, zero conformational state PDB entries, and zero residue sets are recorded for PI3KSH2 / PI |

**Explicit figure-only, SI-only, or access gaps (5):**

- Per-peptide percent deuteration at 3, 30, 300, 3000 s, +/- pY, for p85α ([`10.1016/j.jbior.2012.09.005`](https://doi.org/10.1016/j.jbior.2012.09.005)): in supplement not available (Fig. S3) and figures (Fig. 2, 3)
- Per-peptide deuterium uptake time courses ([`10.1016/j.str.2011.06.003`](https://doi.org/10.1016/j.str.2011.06.003)): figure only (Figures 2, 3, 5, 6C and Supplement Figures S3-S6, Table S1B)
- DEER traces and distance distribution plots, chi2 surfaces ([`10.1021/bi902171d`](https://doi.org/10.1021/bi902171d)): figure only
- Supplement (Fig. S2 and others) ([`10.1021/bi902171d`](https://doi.org/10.1021/bi902171d)): in supplement not available
- Peptide deuterium uptake per time point for p85alpha ([`10.1038/s41467-023-35789-6`](https://doi.org/10.1038/s41467-023-35789-6)): in source data file and Supplementary Fig. 5, not in the text

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
