# Core-binding factor subunit beta (`CBFB`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `Q08024` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*11 rows total (11 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi010713+`](https://doi.org/10.1021/bi010713+) | `NMR_spin_relaxation_and_MF` | `target` | apo | tau_m (4), other (4), Rex (3) | tau_m = 10.00 ns (98 selected NH vectors) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **increased mu s-ms timescale dynamics upon AI-4-57 binding** ([`10.1016/j.ebiom.2016.04.032`](https://doi.org/10.1016/j.ebiom.2016.04.032), sample `S2`): Arg131
- **increased ps-ns timescale dynamics upon AI-4-57 binding** ([`10.1016/j.ebiom.2016.04.032`](https://doi.org/10.1016/j.ebiom.2016.04.032), sample `S2`): Asn104
- **lower order parameters (nanosecond-scale internal motion)** ([`10.1021/bi010713+`](https://doi.org/10.1021/bi010713+), sample `S1`): the long loop and the C-terminal α-helix

### Conformational and complex PDB states (`States`)

- [`4N9F`](https://www.rcsb.org/structure/4N9F): Vif-CBC-CUL5NTD subcomplex (X-ray structure; CBFβ bound to Vif, EloB, EloC, and Cul5NTD; used for cross-link mapping and modeling template) ([`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132))
- `PDBDEV_00000090`: A3G-Vif-CRL5-CBFβ complex integrative structure deposited at PDB-Dev (one of two deposited ensemble models; main text does not distinguish rigid vs flexible between PDBDEV_00000090 and PDBDEV_0000009… ([`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132))
- `PDBDEV_00000091`: A3G-Vif-CRL5-CBFβ complex integrative structure deposited at PDB-Dev (one of two deposited ensemble models; main text does not distinguish rigid vs flexible between PDBDEV_00000090 and PDBDEV_0000009… ([`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132))
- [`1ILF`](https://www.rcsb.org/structure/1ILF): apo-CBFβ solution structure (this study) ([`10.1021/bi010713+`](https://doi.org/10.1021/bi010713+))
- [`1E50`](https://www.rcsb.org/structure/1E50): RD-bound CBFβ (CBFβ-RD complex, X-ray) ([`10.1021/bi010713+`](https://doi.org/10.1021/bi010713+))
- [`2JHB`](https://www.rcsb.org/structure/2JHB): apo-CBFβ NMR ensemble from another lab ([`10.1021/bi010713+`](https://doi.org/10.1021/bi010713+))
- [`1CL3`](https://www.rcsb.org/structure/1CL3): apo-CBFβ NMR ensemble from another lab ([`10.1021/bi010713+`](https://doi.org/10.1021/bi010713+))
- [`4N9F`](https://www.rcsb.org/structure/4N9F): VCBC-Cul5 pentameric complex (homolog) ([`10.1128/mbio.03332-24`](https://doi.org/10.1128/mbio.03332-24))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (8):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi010713+`](https://doi.org/10.1021/bi010713+) | 11 | 4 | 1 | 2 | Single 600 MHz 15N R1/R2/NOE data set at 24 C, model-free analysis. Printed dynamics numbers: global tau_m and |
| [`10.1016/j.ebiom.2016.04.032`](https://doi.org/10.1016/j.ebiom.2016.04.032) | 0 | 0 | 2 | 1 | The paper reports 15N R1 and R2 relaxation of CBFbeta(1-141) with and without AI-4-57 but prints no dynamics n |
| [`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132) | 0 | 3 | 0 | 8 | This paper applies DSSO cross-linking mass spectrometry (LC-MS3) and IMP/PMI integrative structure modeling to |
| [`10.1093/nar/gkp728`](https://doi.org/10.1093/nar/gkp728) | 0 | 0 | 0 | 0 | This paper yields 0 protein dynamics rows, 0 conformational PDB states, and 0 dynamic residue sets for CBFβ. I |
| [`10.1126/sciadv.abj8002`](https://doi.org/10.1126/sciadv.abj8002) | 0 | 0 | 0 | 1 | This paper is a breast cancer epithelial-to-mesenchymal transition (EMT) cell-biology, multiomics (RNA-seq/ATA |
| [`10.1126/science.aaa0314`](https://doi.org/10.1126/science.aaa0314) | 0 | 0 | 0 | 2 | This paper develops small-molecule inhibitors (including AI-4-57 and bivalent AI-10-49) targeting the oncogeni |
| [`10.1128/mbio.03332-24`](https://doi.org/10.1128/mbio.03332-24) | 0 | 1 | 0 | 1 | Zero quantitative protein dynamics rows (expected_rows: []) are reported for CBFB (human CBF-beta, studied as  |
| [`10.1136/jitc-2026-016242`](https://doi.org/10.1136/jitc-2026-016242) | 0 | 0 | 0 | 1 | This leukemia immunology study investigates how the CBFB-MYH11 (CBFβ-SMMHC) fusion oncogene drives immune evas |

**Explicit figure-only, SI-only, or access gaps (16):**

- Per-residue R1*R2 differences, R1, R2 for free and AI-4-57-bound CBFbeta ([`10.1016/j.ebiom.2016.04.032`](https://doi.org/10.1016/j.ebiom.2016.04.032)): figure only (Fig. 3c and Supplementary Fig. 5; no supplement in text)
- Supplemental Table S1 (replicates 1-A to 3-A, 1-B, 2-B, complex preparations, and DSSO molar ratios) ([`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132)): in supplement not available
- Supplemental Tables S2–S6 (132 high-confidence cross-links, redundant dead-end, interlinked, and loop-linked peptides, and subunit scores) ([`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132)): in supplement not available
- Supplemental Tables S7–S8 (IMP/PMI rigid-body/flexible-bead subunit representations including missing X-ray segments and sampling statistics) ([`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132)): in supplement not available
- Supplemental Tables S9–S10 (mutagenesis mapping, contact frequencies, and Bayesian cross-link uncertainty estimates) ([`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132)): in supplement not available
- SI Methods, SI Results, and Supplemental Figures S1–S13 (including Fig. S6 Vif/CBFβ-Cul5 cross-links and Fig. S12B–C Vif-CBC-Cul5NTD RMSD/rotations) ([`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132)): in supplement not available
- Supplemental FASTA and search setup files (PN.RMK_LAIVif_HisCBFB.fasta, PA.SwissProt.PN.RMK.A3GVifCRL5.fasta.random.concat, SwissProt.Human.2016.01.11.fasta.random.concat) ([`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132)): in supplement not available
- Fig. 2A–B (per-subunit sequence coverage % Cov, XL Count, and embedded table of redundant cross-links per subunit including CBFβ) ([`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132)): figure only
- Fig. 5C (pairwise rigid-body RMSD matrix across complex rigid bodies) ([`10.1016/j.mcpro.2021.100132`](https://doi.org/10.1016/j.mcpro.2021.100132)): figure only
- Per-residue S2, tau_e and Rex values for 102 fitted residues (Figure 4); R1, R2 and NOE per residue (Figure 3) ([`10.1021/bi010713+`](https://doi.org/10.1021/bi010713+)): figure only
- Local tau_m range 9.58 to 10.65 ns and counts of residues per model-free model (38, 52, 9, 2, 1) ([`10.1021/bi010713+`](https://doi.org/10.1021/bi010713+)): derived or bookkeeping numbers, not left as rows
- Supplementary material: Tables S1 to S3 and Figs. S1 to S6 ([`10.1126/sciadv.abj8002`](https://doi.org/10.1126/sciadv.abj8002)): in supplement not available
- *... plus 4 additional gap entries in the `Gaps` tab.*

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
