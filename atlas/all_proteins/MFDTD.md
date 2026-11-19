# Transcription-repair-coupling factor (`MFDTD`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P30958` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `700/800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

*8 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `population` | 52 % | Cy5-labeled transcript, short-lived species (transcript loss) | `FRET_and_fluorescence` | `target` | ATP 1 mM; room temperature (24°C); pH 8.0; not applicable (single-molecule TIRF, no N | `no` | [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) |
| `population` | 35 % | low-FRET states (nucleotide incorporation) after pre-incubation w | `FRET_and_fluorescence` | `target` | ATPɣS 0.5 mM; room temperature (24°C); pH 8.0; not applicable (single-molecule TIRF, | `no` | [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) |
| `population` | 49 % | trajectories with observable transitions | `FRET_and_fluorescence` | `target` | no nucleotide; room temperature (24°C); pH 8.0; not applicable (single-molecule TIRF, | `no` | [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) |
| `population` | 24 % | dynamic trajectories, high-mid FRET class | `FRET_and_fluorescence` | `target` | no nucleotide; room temperature (24°C); pH 8.0; not applicable (single-molecule TIRF, | `no` | [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) |
| `population` | 44 % | trajectories exhibiting dynamics | `FRET_and_fluorescence` | `target` | ATPɣS 0.5 mM; room temperature (24°C); pH 8.0; not applicable (single-molecule TIRF, | `no` | [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) |
| `population` | 58 % | trajectories exhibiting dynamics | `FRET_and_fluorescence` | `target` | ATP 1 mM; room temperature (24°C); pH 8.0; not applicable (single-molecule TIRF, no N | `no` | [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) |
| `population` | 63 % | static trajectories | `FRET_and_fluorescence` | `same_protein_other_construct` | ATP 1 mM; room temperature (24°C); pH 8.0; not applicable (single-molecule TIRF, no N | `no` | [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) |
| `population` | 33 % | dynamic trajectories (high-mid, high-low, mid-low together) | `FRET_and_fluorescence` | `same_protein_other_construct` | ATP 1 mM; room temperature (24°C); pH 8.0; not applicable (single-molecule TIRF, no N | `no` | [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*20 rows total (5 spin-relaxation/model-free; 15 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) | `FRET_and_fluorescence` | `target` | ATPɣS 0.5 mM | other (3), tau_e (2) | tau_e = 6.1 s (EC in mid-FRET (catalytically poised…) |
| [`10.1038/s41467-020-15179-y`](https://doi.org/10.1038/s41467-020-15179-y) | `FRET_and_fluorescence` | `target` | in vivo, DNA-bound; 20 Jm−2 UVC irradiat | other (5) | other = 12.0 s (whole protein (DNA-bound Mfd-YPet bi…) |
| [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) | `FRET_and_fluorescence` | `target` | ATPɣS 0.5 mM or ATP 1 mM | other (3) | other = 0.6 FRET efficiency (Mfd-ATPɣS-bound primed DNA, high-FRE…) |
| [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) | `FRET_and_fluorescence` | `target` | ATP 1 mM | tau_e (2) | tau_e = 6.2 s (EC in mid-FRET (catalytically poised…) |
| [`10.1038/s41467-018-03790-z`](https://doi.org/10.1038/s41467-018-03790-z) | `FRET_and_fluorescence` | `same_protein_other_construct` | in live cells, bound to RNAP in stalled/ | other (2) | other = 0.056 s−1 (Mfd-YPet foci (koff, dissociation fr…) |
| [`10.1038/s41467-018-03790-z`](https://doi.org/10.1038/s41467-018-03790-z) | `FRET_and_fluorescence` | `same_protein_other_construct` | in live cells, no UvrA | other (2) | other = 0.035 s−1 (Mfd-YPet foci (koff, dissociation fr…) |
| [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) | `FRET_and_fluorescence` | `target` | no nucleotide | tau_e (1) | tau_e = 7.1 s (EC in mid-FRET (catalytically poised…) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **D3 module is mobile; ~47 Å displacement on DNA binding, enabled by flanking flexible linkers** ([`10.1038/s41467-020-17457-1`](https://doi.org/10.1038/s41467-020-17457-1), sample `S1`): D3 domain and its linkers to D1b and D4
- **partially disordered D3–D4 linker** ([`10.1038/s41467-020-17457-1`](https://doi.org/10.1038/s41467-020-17457-1), sample `S1`): D3–D4 linker
- **TRG helices and hook described as mobile, proposed pawl during translocation** ([`10.1038/s41467-020-17457-1`](https://doi.org/10.1038/s41467-020-17457-1), sample `S1`): TRG helices and hook (C-terminal to the helical hairpin)
- **hooking template-strand ssDNA overhang** ([`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449), sample `S5`): R953
- **contact with non-template strand in dsDNA translocation (TRG motif)** ([`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449), sample `S3`): R953, R929, Q963
- **flexible MfdN-MfdC linker** ([`10.1093/nar/gkp680`](https://doi.org/10.1093/nar/gkp680), sample `S2`): Gly 451–Asn473
- **disordered residues in MfdN crystal** ([`10.1093/nar/gkp680`](https://doi.org/10.1093/nar/gkp680), sample `S1`): 451 through 470

### Conformational and complex PDB states (`States`)

- [`2EYQ`](https://www.rcsb.org/structure/2EYQ): apo, auto-inhibited Mfd ([`10.1038/s41467-020-15182-3`](https://doi.org/10.1038/s41467-020-15182-3))
- [`2EYQ`](https://www.rcsb.org/structure/2EYQ): nucleotide-free E. coli Mfd ([`10.1038/s41467-020-17457-1`](https://doi.org/10.1038/s41467-020-17457-1))
- [`6XEO`](https://www.rcsb.org/structure/6XEO): DNA-bound Mfd (ADP-AlFx) from this study ([`10.1038/s41467-020-17457-1`](https://doi.org/10.1038/s41467-020-17457-1))
- [`6AXC`](https://www.rcsb.org/structure/6AXC): M. smegmatis Mfd bound to ADP and Pi (homolog) ([`10.1038/s41467-020-17457-1`](https://doi.org/10.1038/s41467-020-17457-1))
- [`2B2N`](https://www.rcsb.org/structure/2B2N): E. coli Mfd D1aD2D1b truncation, nucleotide-free ([`10.1038/s41467-020-17457-1`](https://doi.org/10.1038/s41467-020-17457-1))
- [`3HJH`](https://www.rcsb.org/structure/3HJH): E. coli Mfd D1aD2D1bD3 truncation, nucleotide-free ([`10.1038/s41467-020-17457-1`](https://doi.org/10.1038/s41467-020-17457-1))
- [`6XEO`](https://www.rcsb.org/structure/6XEO): E. coli Mfd bound to double-stranded DNA (UvrA-binding domain unmasked) ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6))
- [`4DFC`](https://www.rcsb.org/structure/4DFC): E. coli UvrA-Mfd core interaction complex ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6))
- [`7SSG`](https://www.rcsb.org/structure/7SSG): Mfd motor domain (residues 575-956) on primed DNA with ADP-AlFx, TRG motif dropped into the dsDNA path (cryo-EM model) ([`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449))
- [`2EYQ`](https://www.rcsb.org/structure/2EYQ): apo Mfd, TRG helices almost orthogonal ([`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449))
- [`6X43`](https://www.rcsb.org/structure/6X43): ATP-bound Mfd on upstream dsDNA, TRG helices parallel ([`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449))
- [`6X4W`](https://www.rcsb.org/structure/6X4W): ADP-bound Mfd on upstream dsDNA, TRG helices parallel ([`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449))
- [`6X26`](https://www.rcsb.org/structure/6X26): L1 (previous 4.1 Å model, starting model for the new L1) ([`10.1093/nar/gkag698`](https://doi.org/10.1093/nar/gkag698))
- [`6X2F`](https://www.rcsb.org/structure/6X2F): L2 ([`10.1093/nar/gkag698`](https://doi.org/10.1093/nar/gkag698))
- [`2EYQ`](https://www.rcsb.org/structure/2EYQ): apo crystal structure of E. coli Mfd (obtained in the absence of nucleotides; open TRG motif helical hairpin; D7 packing between D2 and D4) ([`10.1093/nar/gkm019`](https://doi.org/10.1093/nar/gkm019))
- [`2EYQ`](https://www.rcsb.org/structure/2EYQ): apo-Mfd, compact dormant closed form ([`10.1093/nar/gkp680`](https://doi.org/10.1093/nar/gkp680))
- [`3HJH`](https://www.rcsb.org/structure/3HJH): MfdN structure, domains 1-3 independent of MfdC ([`10.1093/nar/gkp680`](https://doi.org/10.1093/nar/gkp680))
- [`2EYQ`](https://www.rcsb.org/structure/2EYQ): apo-Mfd, compact repressed conformation (crystal structure) ([`10.7554/elife.62117`](https://doi.org/10.7554/elife.62117))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (14):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449) | 19 | 4 | 2 | 2 | Single-molecule FRET, SPR, cryo-EM and 2AP fluorescence study of E. coli Mfd on RNAP elongation complexes and  |
| [`10.1038/s41467-020-15179-y`](https://doi.org/10.1038/s41467-020-15179-y) | 5 | 0 | 0 | 1 | Live-cell single-molecule interval imaging of E. coli UvrA-YPet, with Mfd-YPet measured only after UV. Mfd (th |
| [`10.1038/s41467-018-03790-z`](https://doi.org/10.1038/s41467-018-03790-z) | 4 | 0 | 0 | 1 | In-cell single-molecule imaging paper, no NMR. Four rows: koff and residence time of Mfd-YPet foci in uvrA+ an |
| [`10.1016/j.cell.2017.11.017`](https://doi.org/10.1016/j.cell.2017.11.017) | 0 | 0 | 0 | 0 | Single-molecule optical-trap paper; no NMR, HDX, FRET or EPR dynamics values are printed for Mfd, so zero rows |
| [`10.1016/j.jmb.2010.12.004`](https://doi.org/10.1016/j.jmb.2010.12.004) | 0 | 0 | 0 | 0 | The paper maps limited-proteolysis cleavage sites of repressed wt-TRCF and derepressed mutants on SDS-PAGE gel |
| [`10.1038/nature11430`](https://doi.org/10.1038/nature11430) | 0 | 0 | 0 | 0 |  |
| [`10.1038/s41467-020-15182-3`](https://doi.org/10.1038/s41467-020-15182-3) | 0 | 1 | 0 | 1 | Live-cell single-molecule imaging of Mfd-YPet in E. coli; the only kinetic numbers are DNA-bound lifetimes (Ta |
| [`10.1038/s41467-020-17457-1`](https://doi.org/10.1038/s41467-020-17457-1) | 0 | 5 | 3 | 1 | Cryo-EM and biochemical paper on E. coli Mfd; it prints no NMR, HDX, FRET or EPR dynamics values, so zero rows |
| [`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6) | 0 | 2 | 0 | 4 | This paper investigates the in vivo role, RNAP recruitment kinetics, and structural alignment model of Escheri |
| [`10.1093/nar/gkag698`](https://doi.org/10.1093/nar/gkag698) | 0 | 2 | 0 | 0 | Cryo-EM structure paper on E. coli Mfd bound to stalled RNAP elongation complexes with ATP and BeF3-. It print |
| [`10.1093/nar/gkm019`](https://doi.org/10.1093/nar/gkm019) | 0 | 1 | 0 | 3 | This study investigates autoinhibition of Escherichia coli transcription-repair coupling factor Mfd (full-leng |
| [`10.1093/nar/gkp680`](https://doi.org/10.1093/nar/gkp680) | 0 | 2 | 2 | 0 | The paper reports ATPase rates, CD melting midpoints and a crystal structure of MfdN; it prints no NMR, HDX, F |
| [`10.1093/nar/gks775`](https://doi.org/10.1093/nar/gks775) | 0 | 0 | 0 | 0 |  |
| [`10.7554/elife.62117`](https://doi.org/10.7554/elife.62117) | 0 | 1 | 0 | 2 | Cryo-EM structural paper on E. coli Mfd bound to an RNAP elongation complex. It prints no NMR, HDX, smFRET or  |

**Explicit figure-only, SI-only, or access gaps (15):**

- Supplementary Tables 4-6 (residence-time distributions and fit results per tau_tl) ([`10.1038/s41467-018-03790-z`](https://doi.org/10.1038/s41467-018-03790-z)): in supplement not available
- Mfd-YPet lifetimes per time window in Fig. 5d and Supplementary Fig. 7 ([`10.1038/s41467-020-15179-y`](https://doi.org/10.1038/s41467-020-15179-y)): figure only / supplement not available
- Bootstrap fit details in Supplementary Table 4 and Supplementary Figs. 1-4 ([`10.1038/s41467-020-15182-3`](https://doi.org/10.1038/s41467-020-15182-3)): in supplement not available
- Kd values and ATPase rates are in Supplementary Table 1, not in the text ([`10.1038/s41467-020-17457-1`](https://doi.org/10.1038/s41467-020-17457-1)): in supplement not available
- Fig. 1d: relative fold-change time course of Mfd-3X-FLAG co-purified with RNAP-6xHis post-UV in wt, ΔuvrA, and Mfd(R165A-R181A-F185A) cells ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6)): figure only
- Extended Data Fig. 2b: quantitative MS abundance of RNAP-associated Mfd normalized to NusA-containing RNAPs prior to genotoxic stress ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6)): figure only
- Fig. 4a, Fig. 5b-m, Extended Data Figs. 1, 8a-b, 12a-h, 13a-b, 17b: global/local DNA repair curves, UvrAB ChIP-qPCR occupancy, and UV/BCM survival plots for wt vs Δmfd and pMfd overexpression ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6)): figure only
- Supplementary Tables 1-3 (XLMS crosslinks, strains/plasmids & UvrD-CTD crystallographic tables, qPCR oligonucleotides) ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6)): in supplement not available
- State lifetimes for every condition (Supplemental Table S2), ATP-concentration series, TDP data, Supplemental Notes 2-5 ([`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449)): in supplement not available
- EC-alone and NusG FRET percentages and lifetimes ([`10.1093/nar/gkac449`](https://doi.org/10.1093/nar/gkac449)): figure-only or belong to the RNAP elongation complex without Mfd; not Mfd dynamics
- Figures 3B, 3D, 4, 5, and 6 time-course data points (% TFO displaced and % stalled elongation complex remaining over 0–60 min) ([`10.1093/nar/gkm019`](https://doi.org/10.1093/nar/gkm019)): figure only (plotted percentages only; no fitted rate constants or numeric time-course values are printed in text, and these represent biochemical displacement curves rather than structural dynamics parameters)
- Supplementary Figures 1 and 2 (Supplementary Data available at NAR Online) ([`10.1093/nar/gkm019`](https://doi.org/10.1093/nar/gkm019)): in supplement not available (referenced in Results for MfdΔD7 TFO displacement on circular supercoiled pSRTB1 and under RNAP displacement reaction conditions, but not included in 182.txt)
- *... plus 3 additional gap entries in the `Gaps` tab.*

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
