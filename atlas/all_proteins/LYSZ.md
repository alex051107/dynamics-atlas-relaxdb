# Lysozyme C (`LYSZ`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P00698` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*658 rows total (658 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi00012a023`](https://doi.org/10.1021/bi00012a023) | `NMR_spin_relaxation_and_MF` | `target` | apo (no ligand stated) | S2 (178), R2 (133), NOE (133), R1 (115), tau_e (44), Rex (43) | tau_m = 5.7 ns (100 main-chain 15N nuclei without fa…) |
| [`10.1007/s10858-015-0001-1`](https://doi.org/10.1007/s10858-015-0001-1) | `NMR_exchange_and_dispersion` | `target` | apo | tau_m (1) | tau_m = 10.5 ns (all protein protons (whole LYZ)) |
| [`10.1007/s10858-015-0001-1`](https://doi.org/10.1007/s10858-015-0001-1) | `Biophysics_and_other` | `target` | apo | tau_m (1) | tau_m = 10.9 ns (whole LYZ) |

## 3. Computational (MD/MSM) and cryo-structure (X-ray / cryo-EM) rows

*3 rows intentionally separated from experimental solution dynamics pending expert scope lock:*

| Method group | Quantity | Value | Residues / group | Paper |
|---|---|---|---|---|
| `Xray_and_CryoEM` | `population` | 46 % | Asn103 peptide-plane flip, loop conformation B (Lys97-Gly104) | [`10.1107/s2052252521001299`](https://doi.org/10.1107/s2052252521001299) |
| `Xray_and_CryoEM` | `population` | 38 % | Asn103 peptide-plane flip, loop conformation B (Lys97-Gly104) | [`10.1107/s2052252521001299`](https://doi.org/10.1107/s2052252521001299) |
| `Xray_and_CryoEM` | `population` | 33 % | Asn103 peptide-plane flip, loop conformation B (Lys97-Gly104) | [`10.1107/s2052252521001299`](https://doi.org/10.1107/s2052252521001299) |

## 4. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **Main-chain motions with S2 below 0.70 (long loop, C-D loop, C-terminal residue, residue 85)** ([`10.1021/bi00012a023`](https://doi.org/10.1021/bi00012a023), sample `S1`): long loop residues 65-75; short loop connecting C- and D-helices residues 101-104; C-terminal residue; residue 85
- **Same low-S2 set, second half of the sentence** ([`10.1021/bi00012a023`](https://doi.org/10.1021/bi00012a023), sample `S1`): residues 101-104 (loop between C- and D-helices)
- **Microsecond-to-millisecond exchange contribution (Rex)** ([`10.1021/bi00012a023`](https://doi.org/10.1021/bi00012a023), sample `S1`): region of the first 3io-helix and the D-helix
- **loop motion (backbone shift) at 200 us after T-jump, adjacent to the active site** ([`10.1038/s41557-023-01329-4`](https://doi.org/10.1038/s41557-023-01329-4), sample `S1`): 97–100
- **short-amplitude rotamer motion at 20 ns after T-jump** ([`10.1038/s41557-023-01329-4`](https://doi.org/10.1038/s41557-023-01329-4), sample `S1`): Tyr23
- **first aggregated residues in bulk solution (cross-peak intensity decrease 3 h after TCEP)** ([`10.1039/d4sc00560k`](https://doi.org/10.1039/d4sc00560k), sample `S1`): Gly (4, 26, 49, 102, 126), Ala (10, 11, 32, 122), Val (120), Ile(124) and Leu (129), as well as charged residues, such as Arg (5, 45, 125, 128) and Asp (18, 48, 52, 66, 87, 101, 119)
- **main-chain disorder from partial Asn103 peptide-plane flip** ([`10.1107/s2052252521001299`](https://doi.org/10.1107/s2052252521001299), sample `S2`): Lys97-Gly104

### Conformational and complex PDB states (`States`)

- [`1AKI`](https://www.rcsb.org/structure/1AKI): folded state (crystal structure, starting structure of the MD simulations) ([`10.1021/acsomega.8b01911`](https://doi.org/10.1021/acsomega.8b01911))
- [`9HRU`](https://www.rcsb.org/structure/9HRU): lysozyme–pctx complex (space group P3121) ([`10.1021/jacs.5c08121`](https://doi.org/10.1021/jacs.5c08121))
- [`6IRJ`](https://www.rcsb.org/structure/6IRJ): lysozyme (FT-SFX room-temperature crystal structure using nylon mesh) ([`10.1038/s41598-019-43485-z`](https://doi.org/10.1038/s41598-019-43485-z))
- [`6JB8`](https://www.rcsb.org/structure/6JB8): WT D3-L11 in complex with HEL ([`10.1038/s41598-019-50722-y`](https://doi.org/10.1038/s41598-019-50722-y))
- [`6JB2`](https://www.rcsb.org/structure/6JB2): Y102A D3-L11 in complex with HEL ([`10.1038/s41598-019-50722-y`](https://doi.org/10.1038/s41598-019-50722-y))
- [`6JB5`](https://www.rcsb.org/structure/6JB5): Y102A D3-L11 in complex with HEL ([`10.1038/s41598-019-50722-y`](https://doi.org/10.1038/s41598-019-50722-y))
- [`1ZVY`](https://www.rcsb.org/structure/1ZVY): D3-L11·HEL complex (previously reported crystal structure) ([`10.1038/s41598-019-50722-y`](https://doi.org/10.1038/s41598-019-50722-y))
- [`1VFB`](https://www.rcsb.org/structure/1VFB): Fv-lysozyme complex (mouse D1.3 Fv-bound hen egg white lysozyme reference crystal structure) ([`10.1084/jem.187.4.479`](https://doi.org/10.1084/jem.187.4.479))
- [`4wm4`](https://www.rcsb.org/structure/4wm4): Glu35 dual conformer (inward conformer appears) at 800 MPa ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))
- [`1e8l`](https://www.rcsb.org/structure/1e8l): NMR structure, inward (buried) Glu35 conformation ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))
- [`4wld`](https://www.rcsb.org/structure/4wld): HEWL crystal at 0.1 MPa (pressure series) ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))
- [`4wlt`](https://www.rcsb.org/structure/4wlt): HEWL crystal at 190 MPa (pressure series) ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))
- [`4wlx`](https://www.rcsb.org/structure/4wlx): HEWL crystal at 280 MPa (pressure series) ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))
- [`4wly`](https://www.rcsb.org/structure/4wly): HEWL crystal at 380 MPa (pressure series) ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))
- [`4wm1`](https://www.rcsb.org/structure/4wm1): HEWL crystal at 500 MPa (pressure series) ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))
- [`4wm2`](https://www.rcsb.org/structure/4wm2): HEWL crystal at 600 MPa (pressure series) ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))
- [`4wm3`](https://www.rcsb.org/structure/4wm3): HEWL crystal at 710 MPa (pressure series) ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))
- [`4wm5`](https://www.rcsb.org/structure/4wm5): HEWL crystal at 890 MPa (pressure series) ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))
- [`4wm6`](https://www.rcsb.org/structure/4wm6): HEWL crystal at 950 MPa (pressure series) ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))
- [`4xen`](https://www.rcsb.org/structure/4xen): HEWL with (GlcNAc)4 at 920 MPa (pressure series) ([`10.1107/s1399004715000292`](https://doi.org/10.1107/s1399004715000292))

## 5. Papers read and explicit gaps

**Checked `v3` / supplemental papers (44):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi00012a023`](https://doi.org/10.1021/bi00012a023) | 656 | 0 | 3 | 4 | One sample (hen lysozyme, 35 °C, pH 3.8), two methods. Rows: Table 1 side-chain S2, tau and Rex; Table 3 struc |
| [`10.1107/s2052252521001299`](https://doi.org/10.1107/s2052252521001299) | 3 | 0 | 1 | 2 | No NMR relaxation, exchange or HDX values are printed. The only dynamics-type numbers are three refined X-ray  |
| [`10.1007/s10858-015-0001-1`](https://doi.org/10.1007/s10858-015-0001-1) | 2 | 0 | 0 | 2 | This record extracts 2 printed tau_m (tau_rot) rows for chicken egg-white lysozyme (LYZ, P00698) at 65 mg/ml ( |
| [`10.1002/advs.75937`](https://doi.org/10.1002/advs.75937) | 0 | 0 | 0 | 0 | No NMR, HDX, FRET or other dynamics measurement of lysozyme is printed. The only lysozyme dynamics-related con |
| [`10.1002/marc.202500641`](https://doi.org/10.1002/marc.202500641) | 0 | 0 | 0 | 2 | This paper characterizes the synthesis and aqueous solution behavior of the zwitterionic polymer poly(iminopyr |
| [`10.1007/s10847-017-0706-8`](https://doi.org/10.1007/s10847-017-0706-8) | 0 | 0 | 0 | 4 | This paper synthesizes covalent mono-6-O-formyl-β-CD conjugates of chicken egg white lysozyme via solid-state  |
| [`10.1007/s10858-010-9457-1`](https://doi.org/10.1007/s10858-010-9457-1) | 0 | 0 | 0 | 0 |  |
| [`10.1007/s13361-011-0238-1`](https://doi.org/10.1007/s13361-011-0238-1) | 0 | 0 | 0 | 0 | Gas-phase ion mobility (TWIMS/MS) study of ubiquitin, cytochrome c, lysozyme and alpha-lactalbumin ions. It pr |
| [`10.1016/j.bioactmat.2025.11.045`](https://doi.org/10.1016/j.bioactmat.2025.11.045) | 0 | 0 | 0 | 0 | Biomaterials paper on lysozyme amyloid-mineral bone scaffolds. No NMR, HDX, FRET or EPR dynamics; the MD simul |
| [`10.1016/j.ejpb.2015.07.025`](https://doi.org/10.1016/j.ejpb.2015.07.025) | 0 | 0 | 0 | 0 | This paper investigates colloidal protein-protein interactions (osmotic second virial coefficients B22 and red |
| [`10.1016/j.fochx.2025.102678`](https://doi.org/10.1016/j.fochx.2025.102678) | 0 | 0 | 0 | 0 | This food/materials chemistry paper studies egg-white lysozyme (LYZ, 129 residues, 14.3 kDa; matching chicken  |
| [`10.1016/j.ijpharm.2017.09.044`](https://doi.org/10.1016/j.ijpharm.2017.09.044) | 0 | 0 | 0 | 0 | This pharmaceutics study evaluates solid-state ball milling (25 Hz and 50 Hz) and hot melt extrusion (HME) enc |
| [`10.1016/j.ultsonch.2026.108066`](https://doi.org/10.1016/j.ultsonch.2026.108066) | 0 | 0 | 0 | 0 | This paper investigates how ultrasonic pretreatment (360 W, 10 min) mitigates freeze-thaw-induced foaming dete |
| [`10.1021/acs.biomac.5c01601`](https://doi.org/10.1021/acs.biomac.5c01601) | 0 | 0 | 0 | 0 | Zero protein dynamics rows are extracted because this paper measures Li2CO3 and lysozyme crystallization kinet |
| [`10.1021/acs.inorgchem.0c00969`](https://doi.org/10.1021/acs.inorgchem.0c00969) | 0 | 0 | 0 | 0 | This paper uses ElectroSpray Ionization-Mass Spectrometry (ESI-MS) to characterize binding stoichiometries and |
| [`10.1021/acs.jpcb.1c08294`](https://doi.org/10.1021/acs.jpcb.1c08294) | 0 | 0 | 0 | 4 | This paper uses lysozyme (LYZ) as a model adsorbate to determine the specific surface area (~2600 m2/g) of gra |
| [`10.1021/acs.molpharmaceut.3c00403`](https://doi.org/10.1021/acs.molpharmaceut.3c00403) | 0 | 0 | 0 | 0 | No protein dynamics values. The paper reports DSC, TGA, sorption calorimetry and SAXS on freeze-dried lysozyme |
| [`10.1021/acsabm.0c01355`](https://doi.org/10.1021/acsabm.0c01355) | 0 | 0 | 0 | 4 | This paper uses isothermal titration calorimetry (ITC), ProtParam sequence analysis, and PyMOL/APBS surface el |
| [`10.1021/acsbiomaterials.2c01106`](https://doi.org/10.1021/acsbiomaterials.2c01106) | 0 | 0 | 0 | 2 | This paper synthesizes RAFT-derived poly(N,N-dimethylacrylamide) (pDMA/mpDMA) bearing amine-reactive, reductiv |
| [`10.1021/acsomega.4c11143`](https://doi.org/10.1021/acsomega.4c11143) | 0 | 0 | 0 | 0 | This paper synthesizes temperature-sensitive molecularly imprinted cryogels (MICs) templated with bovine serum |
| [`10.1021/acsomega.8b01911`](https://doi.org/10.1021/acsomega.8b01911) | 0 | 1 | 0 | 0 | The paper measures lysozyme activity, CD, fluorescence and MD simulations in urea and GdmCl. No NMR, HDX, FRET |
| [`10.1021/acsomega.9b02578`](https://doi.org/10.1021/acsomega.9b02578) | 0 | 0 | 0 | 0 | The paper studies noscapine binding to hen egg-white lysozyme by UV, steady-state and time-resolved fluorescen |
| [`10.1021/acsomega.9b04291`](https://doi.org/10.1021/acsomega.9b04291) | 0 | 0 | 0 | 0 | This paper investigates noncovalent binding of safranal to hen egg white lysozyme (UniProt P00698) using stead |
| [`10.1021/acssensors.2c00273`](https://doi.org/10.1021/acssensors.2c00273) | 0 | 0 | 0 | 0 | SPR methods paper on lysozyme binding to PEG brushes. It prints binding affinity and bounds on binding rate co |
| [`10.1021/jacs.2c11190`](https://doi.org/10.1021/jacs.2c11190) | 0 | 0 | 0 | 1 |  |

*Showing top 25 of 44 checked papers; see `Papers` tab for full list.*

**Explicit figure-only, SI-only, or access gaps (43):**

- Figure 4b ITC thermogram/plot of PIPY with lysozyme (LYZ) ([`10.1002/marc.202500641`](https://doi.org/10.1002/marc.202500641)): figure only
- Supporting Information (marc70093-sup-0001-SuppMat.pdf) containing experimental ITC parameters and any supplementary data ([`10.1002/marc.202500641`](https://doi.org/10.1002/marc.202500641)): in supplement not available
- Fig. 1 DLS intensity particle size distribution (dH in nm) and polydispersity of lysozyme and L-CD conjugates ([`10.1007/s10847-017-0706-8`](https://doi.org/10.1007/s10847-017-0706-8)): figure only; only qualitative statement ('slightly higher than those for unmodified protein') appears in text
- Fig. 2 DLS relative hydrodynamic diameter (dH/dH0) versus temperature curves for lysozyme and L-CD conjugates ([`10.1007/s10847-017-0706-8`](https://doi.org/10.1007/s10847-017-0706-8)): figure only; only melting temperatures TM (70, 70, and 61 °C) are printed in text, and TM reflects thermal unfolding/aggregation stability rather than protein dynamics
- Fig. 3 far- and near-UV circular dichroism spectra of lysozyme and L-CD conjugates ([`10.1007/s10847-017-0706-8`](https://doi.org/10.1007/s10847-017-0706-8)): figure only; qualitative secondary/tertiary structural comparison with no numerical CD values printed in text
- Supplementary material 1 (DOCX 1023 KB, including Figures S4 and S5) ([`10.1007/s10847-017-0706-8`](https://doi.org/10.1007/s10847-017-0706-8)): in supplement not available in text file; text specifies Figures S4 and S5 are 1H and 13C NMR of small-molecule mono-6-O-formyl-beta-CD
- ESM Table S1 and ESM Figs. S1–S6: all LYZ concentration-dependent fitted parameters (tau_int, tau_rot at higher concentrations, tau_S, E_int, E_rot, E_S, S_int^2, S_rot^2, and exact LYZ K_HH) across 65–260 g/L (4.5–18.2 mM) plus full dispersion and temperature-dependence curves ([`10.1007/s10858-015-0001-1`](https://doi.org/10.1007/s10858-015-0001-1)): in supplement not available
- Figures 3, 4(a–c), 5(a), and 6: LYZ FC-NMR magnetization decays, log-normal distribution width parameter sigma, 361 LYZ relaxation rate data points across frequencies/temperatures/concentrations, and concentration dependence of S_rot^2 and tau_S (including upper/lower limits at 65 g/L) ([`10.1007/s10858-015-0001-1`](https://doi.org/10.1007/s10858-015-0001-1)): figure only
- Figure 1A,B adsorption isotherm curves and Figures S1–S2 fit components (MB and LYZ uptake vs. equilibrium concentration across 5–30 min sonication) ([`10.1021/acs.jpcb.1c08294`](https://doi.org/10.1021/acs.jpcb.1c08294)): figure only / in supplement jp1c08294_si_001.pdf not available
- Figure 2A–B Stern–Volmer plot and double-log fluorescence quenching plots including individual apparent binding constants Kb,1 and Kb,2 at 18.0–23.5 °C ([`10.1021/acs.jpcb.1c08294`](https://doi.org/10.1021/acs.jpcb.1c08294)): figure only
- Figure 2C–D and Figures S3–S5 ATR-FTIR amide I spectral decomposition and quantitative secondary structure percentages (alpha-helix, beta-sheet, beta-turn, random coil) for native and GO-immobilized lysozyme ([`10.1021/acs.jpcb.1c08294`](https://doi.org/10.1021/acs.jpcb.1c08294)): figure only / in supplement jp1c08294_si_001.pdf not available
- Table S1 and supporting equations S9–S13 (literature MB adsorption capacities, K2/K1 vs. ultrasonication time, binding constant and van't Hoff derivations) ([`10.1021/acs.jpcb.1c08294`](https://doi.org/10.1021/acs.jpcb.1c08294)): in supplement jp1c08294_si_001.pdf not available
- *... plus 31 additional gap entries in the `Gaps` tab.*

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
