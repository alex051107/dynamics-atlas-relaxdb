# Chemotaxis protein CheA (`CHEAYBD`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P07363` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Worked deep walkthrough / review case](../v3_previews/CHEA_CHEAYBD.md)

> **Audit note:** Review case (Rank 4): duplicate UniProt P07363 with CHEA (cross-linked in Atlas)

> **Shared UniProt (`P07363`):** Also filed in RelaxDB under [`CHEA`](CHEA.md). Inspect both entries together when synthesizing canonical protein behavior.

## 1. Experimental conformational exchange (rates, populations, Δω)

*5 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `population` | 78 % | CheA-P1 (average S/N, tail residues removed): fraction bound to P | `NMR_other` | `same_protein_other_construct` | CheA-P1 with kinase-off signaling complexes (CF4E, CheA-P3P4P5, CheW); 22°C; pH pH 7. | `no` | [`10.1016/j.bpj.2026.05.001`](https://doi.org/10.1016/j.bpj.2026.05.001) |
| `population` | 90 % | CheA-P1 (average S/N, tail residues removed): fraction bound to P | `NMR_other` | `same_protein_other_construct` | CheA-P1 with kinase-on signaling complexes (CF4Q, CheA-P3P4P5, CheW); 22°C; pH pH 7.5 | `no` | [`10.1016/j.bpj.2026.05.001`](https://doi.org/10.1016/j.bpj.2026.05.001) |
| `kex` | ∼1250 s–1 100 | 360, 390–398, 400, 401, 403, 439 (amide 1H) and 391–395, 517, 518 | `NMR_exchange_and_dispersion` | `homolog` | apo; 50 °C; pH 7.4; 500 and 800 | `no` | [`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379) |
| `kex` | >1,000 s−1 | I5 (P1-CheY bound / unbound exchange) | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | CheY titration; 283 K and 303 K; pH not stated for titration; not stated | `no` | [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) |
| `population` | less than 10% % | P1-P4 interacting population in full-length CheA | `NMR_other` | `target` | free, or with non-labeled CheY in titrations; 303 K; pH 7.5; 500 | `no` | [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*66 rows total (2 spin-relaxation/model-free; 64 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1073/pnas.2218467120`](https://doi.org/10.1073/pnas.2218467120) | `HDX_NMR_and_MS` | `target` | apo, free in solution, 3 µM | other (15) | other = 24 % (1-131 (P1)) |
| [`10.1073/pnas.2218467120`](https://doi.org/10.1073/pnas.2218467120) | `HDX_NMR_and_MS` | `target` | in CF4E complexes with CheW on vesicles  | other (11) | other = 23 % (1-131 (P1)) |
| [`10.1073/pnas.2218467120`](https://doi.org/10.1073/pnas.2218467120) | `HDX_NMR_and_MS` | `target` | in CF4Q complexes with CheW on vesicles  | other (11) | other = 23 % (1-131 (P1)) |
| [`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328) | `EPR_DEER` | `homolog` | foldon complex, ADP-NO | other (6) | other = ~22 Å (ADP-NO (P4-P4)) |
| [`10.1021/acs.jpcb.8b05619`](https://doi.org/10.1021/acs.jpcb.8b05619) | `EPR_DEER` | `same_protein_other_construct` | bound to CheY (Cu2+-labelled) | other (5) | other = 52 Å (P2 residue 178 nitroxide to CheY Cu2…) |
| [`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328) | `EPR_DEER` | `homolog` | free kinase, ADP | other (5) | other = ~28 Å (E12C-R1 (P1-P1)) |
| [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) | `NMR_exchange_and_dispersion` | `target` | free, or with non-labeled CheY in titrat | other (4) | other = 0.5 μM (Kd, P2 domain of CheA with CheY) |
| [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) | `NMR_spin_relaxation_and_MF` | `target` | free, or with non-labeled CheY in titrat | tau_m (2) | tau_m = ~30 ns (P1 domain of CheA) |
| [`10.1007/s00723-018-1070-6`](https://doi.org/10.1007/s00723-018-1070-6) | `EPR_DEER` | `same_protein_other_construct` | apo, and with ADP-β-S-SL added | other (2) | other = 45 Å (E387C-SL, P4 domain to P4 domain in …) |
| [`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328) | `EPR_DEER` | `homolog` | ADP, foldon complex | other (2) | other = ~ 5 Å (E387C-R1 (P4-P4)) |
| [`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328) | `EPR_DEER` | `homolog` | free kinase, ADP-NO | other (2) | other = ~45 Å (E588C-R1 to ADP-NO (P5-P4)) |
| [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) | `NMR_other` | `target` | free, or with non-labeled CheY in titrat | other (1) | other = ~ 1 min−1 (CheA autophosphorylation rate withou…) |

## 3. Computational (MD/MSM) and cryo-structure (X-ray / cryo-EM) rows

*4 rows intentionally separated from experimental solution dynamics pending expert scope lock:*

| Method group | Quantity | Value | Residues / group | Paper |
|---|---|---|---|---|
| `MD_and_MSM` | `population` | 80% % | undipped CheA dimer state (first-listed cluster) | [`10.7554/elife.08419`](https://doi.org/10.7554/elife.08419) |
| `MD_and_MSM` | `population` | 10% % | dipped CheA dimer state (second-listed cluster) | [`10.7554/elife.08419`](https://doi.org/10.7554/elife.08419) |
| `MD_and_MSM` | `population` | 10% % | intermediate state 1 (third-listed cluster) | [`10.7554/elife.08419`](https://doi.org/10.7554/elife.08419) |
| `MD_and_MSM` | `population` | 2% % | intermediate state 2 (fourth-listed cluster) | [`10.7554/elife.08419`](https://doi.org/10.7554/elife.08419) |

## 4. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **microsecond to millisecond conformational exchange in P4l (CPMG dispersion)** ([`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379), sample `S1`): amide protons 360, 390–398, 400, 401, 403, and 439; amide nitrogens 391–395, 517, and 518
- **CheY-binding interface on the P1 domain (amide groups), P1-CheY bound state** ([`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x), sample `S1`): I43, H48-I50, G52, L68, D70, F91, and Q109
- **CheY-binding interface on the P1 domain (methyl groups), P1-CheY bound state** ([`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x), sample `S2`): I5, A42, and A54
- **P1/P1' dimer interface (very slow uptake)** ([`10.1073/pnas.2218467120`](https://doi.org/10.1073/pnas.2218467120), sample `S1`): 13 to 27 and 84 to 104

### Conformational and complex PDB states (`States`)

- [`1U0S`](https://www.rcsb.org/structure/1U0S): crystal structure of CheY in complex with the CheA P2 domain; one binding mode, matches the 52 Å major peak ([`10.1021/acs.jpcb.8b05619`](https://doi.org/10.1021/acs.jpcb.8b05619))
- [`1B3Q`](https://www.rcsb.org/structure/1B3Q): T. maritima CheA dimer (homolog) ([`10.1021/jasms.2c00262`](https://doi.org/10.1021/jasms.2c00262))
- [`6S1K`](https://www.rcsb.org/structure/6S1K): CheA/CheW/receptor-fragment signaling array model (cryo-ET-based) ([`10.1021/jasms.2c00262`](https://doi.org/10.1021/jasms.2c00262))
- [`2LP4`](https://www.rcsb.org/structure/2LP4): CheA P1 and P2 domain NMR structures ([`10.1021/jasms.2c00262`](https://doi.org/10.1021/jasms.2c00262))
- [`3JA6`](https://www.rcsb.org/structure/3JA6): T. maritima core signalling unit (CheA in receptor–CheW–CheA complex; homolog), compared to the E. coli CSU ([`10.1038/s41467-020-14350-9`](https://doi.org/10.1038/s41467-020-14350-9))
- [`2LP4`](https://www.rcsb.org/structure/2LP4): model of E. coli isolated P1-P2-CheY complex; relative orientation similar to the P1-CheY bound state ([`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x))
- [`1TQG`](https://www.rcsb.org/structure/1TQG): parallel P1 dimer (crystal structure of isolated T. maritima P1) compatible with the DEER P1 restraints ([`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328))
- [`4XIV`](https://www.rcsb.org/structure/4XIV): T. maritima CheA P3P4P5 crystal structure (homolog) ([`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328))
- [`3UR1`](https://www.rcsb.org/structure/3UR1): CheA P4P5 with CheW and receptor fragment (crystal) (homolog) ([`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328))
- [`6S1K`](https://www.rcsb.org/structure/6S1K): E. coli core complex (CheA, CheW, and receptor trimers of dimers) ([`10.1126/scisignal.abj1737`](https://doi.org/10.1126/scisignal.abj1737))
- [`4XIV`](https://www.rcsb.org/structure/4XIV): planar P3-P4 arrangement (T. maritima CheA.P3-P4 crystal structure) ([`10.1128/mbio.00793-23`](https://doi.org/10.1128/mbio.00793-23))
- [`3JA6`](https://www.rcsb.org/structure/3JA6): undipped CheA conformation ([`10.1128/mbio.00793-23`](https://doi.org/10.1128/mbio.00793-23))
- [`6S1K`](https://www.rcsb.org/structure/6S1K): undipped CheA conformation ([`10.1128/mbio.00793-23`](https://doi.org/10.1128/mbio.00793-23))
- [`4JPB`](https://www.rcsb.org/structure/4JPB): T. maritima (CheA.P5/CheW) ring crystal structure (homolog) ([`10.1128/mbio.00793-23`](https://doi.org/10.1128/mbio.00793-23))

## 5. Papers read and explicit gaps

**Checked `v3` / supplemental papers (18):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1073/pnas.2218467120`](https://doi.org/10.1073/pnas.2218467120) | 37 | 0 | 1 | 1 | HDX-MS study of E. coli CheA; no NMR relaxation or exchange rates. Rows are the Table 1 rapid-uptake fractions |
| [`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328) | 15 | 3 | 0 | 1 | No NMR or kinetic dynamics numbers are printed. The paper reports DEER distances for Thermotoga maritima CheA  |
| [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) | 9 | 1 | 2 | 3 | No table prints numbers. The text gives two TRACT total correlation times (P1 and P2 domains of full-length Ch |
| [`10.1021/acs.jpcb.8b05619`](https://doi.org/10.1021/acs.jpcb.8b05619) | 5 | 1 | 0 | 2 | The paper reports Cu2+-NO DEER distance distributions for the CheY41PyTyr:CheA P1P2 complex (T. maritima). Fiv |
| [`10.7554/elife.08419`](https://doi.org/10.7554/elife.08419) | 4 | 0 | 0 | 1 | No experimental dynamics measurement (NMR, HDX, FRET, EPR) is printed. The only dynamics numbers are four conf |
| [`10.1007/s00723-018-1070-6`](https://doi.org/10.1007/s00723-018-1070-6) | 2 | 0 | 0 | 1 |  |
| [`10.1016/j.bpj.2026.05.001`](https://doi.org/10.1016/j.bpj.2026.05.001) | 2 | 0 | 0 | 1 | CSP and peak-intensity mapping of CheA-P1 binding to P4 in free CheA and signaling complexes. The only printed |
| [`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379) | 1 | 0 | 1 | 2 | The paper prints one dynamics number: a global two-state kex for the T. maritima CheA P4l construct from CPMG  |
| [`10.1016/j.jmb.2012.05.023`](https://doi.org/10.1016/j.jmb.2012.05.023) | 0 | 0 | 0 | 0 | No dynamics value is printed for CheA. The paper is a chemical-shift-perturbation study of CheA P4P5 binding t |
| [`10.1021/acs.biochem.7b00698`](https://doi.org/10.1021/acs.biochem.7b00698) | 0 | 0 | 0 | 0 | The paper reports assembly, kinase activity, stoichiometry, ICP-OES and SEC-MALS of chemoreceptor arrays with  |
| [`10.1021/bi300147m`](https://doi.org/10.1021/bi300147m) | 0 | 0 | 0 | 1 | The paper builds a docked structural model of CheA P1 with CheY/P2 from NOEs and spin-label distances and meas |
| [`10.1021/bi501570n`](https://doi.org/10.1021/bi501570n) | 0 | 0 | 0 | 2 | The paper reports no NMR or other conformational-dynamics value for E. coli CheA. It prints enzyme-kinetic aut |
| [`10.1021/ja3056694`](https://doi.org/10.1021/ja3056694) | 0 | 0 | 0 | 0 | No experimental dynamics value is printed. The paper is REMD simulation plus ATPase, activation and swarm assa |
| [`10.1021/jasms.2c00262`](https://doi.org/10.1021/jasms.2c00262) | 0 | 3 | 0 | 0 | Covalent labeling mass spectrometry (DEPC) study of CheA in a chemoreceptor complex; it prints no NMR, HDX, FR |
| [`10.1038/s41467-020-14350-9`](https://doi.org/10.1038/s41467-020-14350-9) | 0 | 1 | 0 | 0 | The paper is a cryo-ET and subtomogram-averaging structure paper with a flexible-fitting MD step. It prints no |
| [`10.1038/s42003-019-0748-0`](https://doi.org/10.1038/s42003-019-0748-0) | 0 | 0 | 0 | 2 | Cryo-ET and all-atom MD paper on the E. coli chemotaxis core signaling unit. It prints no NMR, HDX, FRET or EP |
| [`10.1126/scisignal.abj1737`](https://doi.org/10.1126/scisignal.abj1737) | 0 | 1 | 0 | 5 | This paper investigates hexameric CheW rings in Escherichia coli chemoreceptor arrays using in vivo disulfide  |
| [`10.1128/mbio.00793-23`](https://doi.org/10.1128/mbio.00793-23) | 0 | 4 | 0 | 0 | Cryo-ET sub-tomogram averaging plus AlphaFold2 and all-atom MD of the E. coli core signaling unit. No NMR, FRE |

**Explicit figure-only, SI-only, or access gaps (22):**

- Relative populations of the 45 A and 35 A DEER peaks ([`10.1007/s00723-018-1070-6`](https://doi.org/10.1007/s00723-018-1070-6)): figure only, no printed number (Fig. 4)
- Per-residue CSPs, S/N values (Table S4) and per-residue ATP KD values (Table S2) ([`10.1016/j.bpj.2026.05.001`](https://doi.org/10.1016/j.bpj.2026.05.001)): in supplement not available
- Distance distributions P(r) and DEER traces for the CheY:CheA complexes (Figs 3, 4, S6-S8) ([`10.1021/acs.jpcb.8b05619`](https://doi.org/10.1021/acs.jpcb.8b05619)): figure only; Supplementary Figures not in the text
- CheY structure refinement statistics (Table S1) ([`10.1021/acs.jpcb.8b05619`](https://doi.org/10.1021/acs.jpcb.8b05619)): in supplement not available
- Kd of P1-CheY, about 5 mM (and ~4.5 mM average in Figure 4 legend) ([`10.1021/bi300147m`](https://doi.org/10.1021/bi300147m)): equilibrium affinity from chemical shift titration, not a dynamics quantity; recorded here only so the decision is visible
- Per-residue CPMG dispersion curves for P4l and P4 (Figures S5-S7) ([`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379)): figure only, in supplement not available
- Minor-state population ([`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379)): not defined by the authors: exchange is fast compared to the chemical shift difference, so no value is printed
- DEER spin-spin distance distributions P(r) for TarFO 4Q E389C-R1 and for T. maritima CheA P3P4P5 Q545C with Tm14 or TarFO 4Q ([`10.1021/bi501570n`](https://doi.org/10.1021/bi501570n)): figure only (Figures 5 and 10); the text prints a 28–35 Å range for Tar (a different protein) and only a relative ~7 Å increase for the T. maritima CheA homolog
- CheY-P formation and decay kinetics ([`10.1021/bi501570n`](https://doi.org/10.1021/bi501570n)): in supplement not available (Figure 2 of the Supporting Information); the text value k ~1.3 min–1 belongs to CheY-P decay, not CheA
- Equilibrium constants from MCMC at 283 K and 303 K (Fig. 4a,b), koff/kon ratios ([`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x)): figure only
- Cross-saturation reduction ratios per residue (Figs 6c,d and 7b,c) ([`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x)): figure only
- Supplementary Table S1/S2 and Supplementary Note values ([`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x)): in supplement not available
- *... plus 10 additional gap entries in the `Gaps` tab.*

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
