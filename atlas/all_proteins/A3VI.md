# Collagen alpha-3(VI) chain (`A3VI`)

**Atlas tier:** Tier 3 · Qualitative regions / PDB states / Release 0.1 unknown / twin link / 0-numeric full text  
**UniProt:** `P12111` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **C-terminal residues with poorer electron density precluding unambiguous model building (WT crystal disorder)** ([`10.1016/j.str.2013.06.028`](https://doi.org/10.1016/j.str.2013.06.028), sample `S1`): S1220–G1224
- **C-terminal extension less ordered than core VWA domain by Cα atom B factors (plasticity in N5-N4 domain pair)** ([`10.1016/j.str.2013.06.028`](https://doi.org/10.1016/j.str.2013.06.028), sample `S1`): N1206–G1224 (C-terminal extension)
- **C-terminal extension residues with poor electron density precluding unambiguous assignment in R1061Qm mutant crystal** ([`10.1016/j.str.2013.06.028`](https://doi.org/10.1016/j.str.2013.06.028), sample `S2`): K2014–G2024
- **conformational heterogeneity / alternative disulphide bond conformations** ([`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3), sample `S1`): α3 Cys2390
- **flexible N-terminal vWA domains (extra diffuse density at higher/lower thresholds)** ([`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3), sample `S7`): α3 chain N2-N9 domains
- **interdomain flexibility / diffuse density for unresolved vWA domains** ([`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3), sample `S1`): interdomain linkers and the other three vWA domains (α1 C1, α1 C2, α2 C1)
- **mobile C1 vWA domains absent from cryoEM density map** ([`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3), sample `S1`): α1 and α2 chain C1 domains
- **mobile domain in mini-collagen VI heterotrimer (resolved upon tetramer packing in tissue microfibril)** ([`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3), sample `S1`): α1 C2 domain
- **conformational flexibility preventing high-resolution cryoEM reconstruction** ([`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3), sample `S2`): α1α2α3C1 heterotrimer (C1 domains)
- **flexibility along the microfibril bead / fibre axis observed in 3D variability analysis** ([`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3), sample `S7`): bovine microfibril bead

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (7):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1002/advs.202502436`](https://doi.org/10.1002/advs.202502436) | 0 | 0 | 0 | 0 | Zero protein dynamics rows are present in this study; the paper investigates melanocyte maintenance and hair p |
| [`10.1016/j.str.2013.06.028`](https://doi.org/10.1016/j.str.2013.06.028) | 0 | 0 | 3 | 2 | Zero dynamics rows (expected_rows: []) because this paper reports 1.2 Å X-ray crystal structures of wild-type  |
| [`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3) | 0 | 0 | 7 | 4 | Zero quantitative dynamics rows (expected_rows: []) are extractable because this paper is a cryoEM, BioSAXS, S |
| [`10.1172/jci189197`](https://doi.org/10.1172/jci189197) | 0 | 0 | 0 | 2 | This JCI 2025 study investigates lysyl hydroxylase 2 (LH2) GGT-domain glucosylation of collagen VI (Col6/Col6a |
| [`10.1186/s13287-026-04940-7`](https://doi.org/10.1186/s13287-026-04940-7) | 0 | 0 | 0 | 2 | This cell and mechanobiology paper investigates human iPSC-derived chondrocytes carrying a heterozygous COL6A3 |
| [`10.3389/fonc.2026.1711079`](https://doi.org/10.3389/fonc.2026.1711079) | 0 | 0 | 0 | 0 | This paper investigates COL6A3 as a colorectal cancer transcriptomic biomarker and Embelin-modulated gene targ |
| [`10.3390/ijms24044095`](https://doi.org/10.3390/ijms24044095) | 0 | 0 | 0 | 0 | This is a zero-row paper (0 expected_rows, 0 expected_states, 0 expected_residue_sets). It investigates pre- v |

**Explicit figure-only, SI-only, or access gaps (10):**

- PDB accession codes for the WT and R1061Qm mutant murine collagen VI α3N5 crystal structures determined in this study ([`10.1016/j.str.2013.06.028`](https://doi.org/10.1016/j.str.2013.06.028)): accession/deposition paragraph is absent from the PMC XML text (text ends at Graphical Representation of Structures)
- Per-residue Cα atom B-factor values comparing the C-terminal extension and core VWA domain ([`10.1016/j.str.2013.06.028`](https://doi.org/10.1016/j.str.2013.06.028)): explicitly marked '(data not shown)' in Results and Discussion
- Supplementary Table 1 (BioSAXS data collection parameters referenced in Methods - Small-angle X-ray scattering (SAXS)) ([`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3)): in supplement not available
- Supplementary Table 2 (cryoEM data collection parameters and model validation metrics, including deposited PDB/EMDB details, referenced in Methods) ([`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3)): in supplement not available
- Deposited PDB and EMDB accession IDs (Methods - Chain identification, model building and refinement states maps and models were deposited to EMDB and PDB, with Data Availability / Supplementary Table 2 absent from 123.txt) ([`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3)): in supplement not available
- Supplementary Fig. 1 (α1α2α3FL construct details and characterization referenced in Results) ([`10.1038/s41467-025-62923-3`](https://doi.org/10.1038/s41467-025-62923-3)): in supplement not available
- Supplemental Table 1 (4,379 LC-MS proteins), Supplemental Table 2 (PGGHG deglucosylation efficiency on Col6a3 sites), Supplemental Table 3 (glycosylated collagen residues), Supplemental Figures 1-12, and Supplemental Videos 1-2 ([`10.1172/jci189197`](https://doi.org/10.1172/jci189197)): in supplement not available
- Figure 6C and 6E focal adhesion disassembly T1/2 values in parental, Col6-KR, and LH2-WA 344SQ cells ([`10.1172/jci189197`](https://doi.org/10.1172/jci189197)): figure only (no numeric T1/2 values printed in text; additionally measures cellular focal adhesion disassembly kinetics rather than molecular protein dynamics of Col6a3)
- Supplementary Material 1–5 (including Table S1A–C, Table S2A–C, Table S3A–D, Table S4A–D, and Fig. S1–S3) ([`10.1186/s13287-026-04940-7`](https://doi.org/10.1186/s13287-026-04940-7)): in supplement not available (Supplementary Material 1–5 are not included in 231.txt; described in the text as RNA-seq DEG lists and chondrogenesis/gene-expression supplements rather than protein dynamics data)
- Fig. 2D (COL6 microfibril periodicity), Fig. 2F–G (PCM and ECM AFM elastic moduli), and Fig. 4F–G (PER2 and BMAL1 circadian period and phase) ([`10.1186/s13287-026-04940-7`](https://doi.org/10.1186/s13287-026-04940-7)): figure only (plotted without printed numerical values in the text; also represent fibril repeat spacing, matrix stiffness, and cellular circadian oscillation rather than molecular protein dynamics)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
