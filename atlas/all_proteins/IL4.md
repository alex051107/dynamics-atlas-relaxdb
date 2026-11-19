# Interleukin-4 (IL-4) (`IL4`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P05112` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*729 rows total (729 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi00158a003`](https://doi.org/10.1021/bi00158a003) | `NMR_spin_relaxation_and_MF` | `target` | apo | NOE (219), S2 (133), R1 (113), R2 (113), other (32), Rex (30) | R1 = 2.06 not printed (column 1/T1) (I11) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **residues key to the DARPin-induced conformational change** ([`10.1002/prot.24815`](https://doi.org/10.1002/prot.24815), sample `S1`): Arg53, Trp91 and Leu96
- **slow (ms) conformational exchange broadening, T1/T2 > 5.2 and Aex > 0.5 Hz, near the 24-65 and 46-99 disulfides or the beta-sheet** ([`10.1021/bi00158a003`](https://doi.org/10.1021/bi00158a003), sample `S1`): 22, 24, 99, 103, 104 (loop residues with exchange and large-amplitude subnanosecond motion); BC loop 59-61, 63, 67 (large exchange line widths)

### Conformational and complex PDB states (`States`)

- [`4YDY`](https://www.rcsb.org/structure/4YDY): IL-4 bound to DARPin_44 (induced conformation: Trp91 and Leu96 buried) ([`10.1002/prot.24815`](https://doi.org/10.1002/prot.24815))
- [`2B8U`](https://www.rcsb.org/structure/2B8U): unbound IL-4 reference conformation ([`10.1002/prot.24815`](https://doi.org/10.1002/prot.24815))
- [`3BPL`](https://www.rcsb.org/structure/3BPL): human IL-4 (hIL-4) crystal structure complexed with receptors ([`10.1126/sciadv.adw9755`](https://doi.org/10.1126/sciadv.adw9755))
- [`3BPN`](https://www.rcsb.org/structure/3BPN): human IL-4 (hIL-4) crystal structure complexed with receptors ([`10.1126/sciadv.adw9755`](https://doi.org/10.1126/sciadv.adw9755))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (10):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi00158a003`](https://doi.org/10.1021/bi00158a003) | 729 | 0 | 1 | 1 | Single-sample 15N relaxation study (35 C, pH 5.6, 50.7 MHz T1/T2, NOE at 50.7 and 36.5 MHz). Rows: per-residue |
| [`10.1002/prot.24815`](https://doi.org/10.1002/prot.24815) | 0 | 2 | 1 | 0 | Crystallography paper with no NMR, HDX, FRET or EPR dynamics measurement. Zero dynamics rows; two PDB states o |
| [`10.1016/j.mtbio.2025.102365`](https://doi.org/10.1016/j.mtbio.2025.102365) | 0 | 0 | 0 | 0 | Zero protein dynamics rows, zero conformational states, and zero dynamic residue sets: this paper is a biomate |
| [`10.1016/j.mtbio.2025.102401`](https://doi.org/10.1016/j.mtbio.2025.102401) | 0 | 0 | 0 | 0 | This paper is a biomaterials and bone-regeneration study investigating sequential release of interleukin-4 (IL |
| [`10.1021/acsami.5c23172`](https://doi.org/10.1021/acsami.5c23172) | 0 | 0 | 0 | 0 | Off-topic biomaterials and bone tissue engineering paper investigating a 3D-printed PCL/nHA gyroid scaffold in |
| [`10.1038/nchembio.1096`](https://doi.org/10.1038/nchembio.1096) | 0 | 0 | 0 | 0 |  |
| [`10.1038/s41551-023-01050-0`](https://doi.org/10.1038/s41551-023-01050-0) | 0 | 0 | 0 | 2 | This paper investigates IL4-induced trained immunity and engineers an apoA1–IL4 fusion protein (and murine chi |
| [`10.1126/sciadv.adw9755`](https://doi.org/10.1126/sciadv.adw9755) | 0 | 2 | 0 | 2 | This paper reports chemical synthesis of wild-type mouse IL-4 (smIL-4, 41% sequence identity to human IL-4 P05 |
| [`10.1186/1741-7007-4-13`](https://doi.org/10.1186/1741-7007-4-13) | 0 | 0 | 0 | 0 | Crystallography and BIAcore binding study of IL-4 super-agonist variants. The paper prints no NMR, HDX, FRET o |
| [`10.1186/s12903-025-06999-9`](https://doi.org/10.1186/s12903-025-06999-9) | 0 | 0 | 0 | 0 | Zero expected protein dynamics rows, zero PDB conformational states, and zero dynamic residue sets. This denta |

**Explicit figure-only, SI-only, or access gaps (5):**

- Figure 2B-D per-residue NOE, T1/T2 and S2 plots ([`10.1021/bi00158a003`](https://doi.org/10.1021/bi00158a003)): figure only; the same per-residue values are tabulated in the appended SI tables
- Supplementary Tables 1–5 (stimuli, pharmacological inhibitors, antibodies/viability dyes, ChIP-qPCR primers, and Supplementary Table 5) ([`10.1038/s41551-023-01050-0`](https://doi.org/10.1038/s41551-023-01050-0)): in supplement not available (cited in Methods and Supplementary information line 185, not included in 130.txt; context indicates reagents/primers rather than protein dynamics)
- Fig. 3f and Extended Data Fig. 3a SPR sensorgram association/dissociation kinetic traces, and Fig. 5b/e 89Zr construct blood half-life pharmacokinetic decay curves ([`10.1038/s41551-023-01050-0`](https://doi.org/10.1038/s41551-023-01050-0)): figure only (no numerical association/dissociation rate constants kon/koff are printed in text; blood half-lives in Fig. 5b/e are in vivo pharmacokinetic clearance curves rather than protein conformational dynamics)
- Supplementary material (Figs. S1 to S49, Supplementary Text, NMR spectra), including SPR binding data (figs. S5 and S6), full dose-response pSTAT EC50 curves (figs. S2 to S4), and competition assay plots (fig. S7) ([`10.1126/sciadv.adw9755`](https://doi.org/10.1126/sciadv.adw9755)): in supplement not available
- Figure-only plots in main text: CD spectrum of smIL-4 7 (Fig. 3E), pSTAT dose-response plots (Fig. 3F, Fig. 4D-F, Fig. 5E), and splenic neutrophil counts (Fig. 6B) ([`10.1126/sciadv.adw9755`](https://doi.org/10.1126/sciadv.adw9755)): figure only

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
