# Chemotaxis protein CheA (`CHEA`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P07363` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Worked deep walkthrough / review case](../v3_previews/CHEA_CHEAYBD.md)

> **Audit note:** Review case (Rank 4): duplicate UniProt P07363 with CHEAYBD (cross-linked in Atlas)

> **Shared UniProt (`P07363`):** Also filed in RelaxDB under [`CHEAYBD`](CHEAYBD.md). Inspect both entries together when synthesizing canonical protein behavior.

## 1. Experimental conformational exchange (rates, populations, Δω)

*6 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `population` | 78% % | CheA-P1 (average S/N, tail residues removed) | `NMR_other` | `same_protein_other_construct` | P1 with kinase-off signaling complexes (CF4E, CheA-P3P4P5, CheW); 22°C; pH 7.5; 600 | `no` | [`10.1016/j.bpj.2026.05.001`](https://doi.org/10.1016/j.bpj.2026.05.001) |
| `population` | 90% % | CheA-P1 (average S/N, tail residues removed) | `NMR_other` | `same_protein_other_construct` | P1 with kinase-on signaling complexes (CF4Q, CheA-P3P4P5, CheW); 22°C; pH 7.5; 600 | `no` | [`10.1016/j.bpj.2026.05.001`](https://doi.org/10.1016/j.bpj.2026.05.001) |
| `kex` | ∼1250 s–1 100 | 360, 390–398, 400, 401, 403, 439, 517, 518 | `NMR_exchange_and_dispersion` | `homolog` | apo; 50 °C; pH 7.4; 500 and 800 | `no` | [`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379) |
| `kex` | >1,000 s−1 | I5 (P1-CheY unbound / bound exchange) | `NMR_exchange_and_dispersion` | `target` | titrated with non-labeled CheY; 283 K; pH not stated for this titration; not stated | `no` | [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) |
| `population` | > 80% % | P2 domain of CheA bound to CheY at stoichiometric CheY | `NMR_exchange_and_dispersion` | `target` | free CheA for TRACT; with non-labeled CheY in titrations; 303 K; pH 7.5; 500 | `unclear` | [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) |
| `population` | less than 10% % | P1-P4 interacting population of full-length CheA | `NMR_other` | `target` | with CheY; not stated; pH 6.5; 600 or 800 | `unclear` | [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*1090 rows total (1054 spin-relaxation/model-free; 36 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi951960e`](https://doi.org/10.1021/bi951960e) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | apo | other (415), S2 (244), tau_m (154), NOE (121), tau_e (118) | other = 767 ms (residues 10-129 (P1 domain, well-def…) |
| [`10.1021/acs.jpcb.8b05619`](https://doi.org/10.1021/acs.jpcb.8b05619) | `EPR_DEER` | `same_protein_other_construct` | bound to CheY41PyTyr-Cu2+ | other (7) | other = 52 Å (CheY Cu2+ (PyTyr41) to nitroxide at …) |
| [`10.1073/pnas.2218467120`](https://doi.org/10.1073/pnas.2218467120) | `HDX_NMR_and_MS` | `target` | apo | other (7) | other = 2 h (P1 dimer interface peptide 91-104 (E…) |
| [`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328) | `EPR_DEER` | `homolog` | foldon complex, ADP-NO | other (6) | other = ~22 Å (ADP-NO (P4-P4)) |
| [`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328) | `EPR_DEER` | `homolog` | free kinase, ADP | other (5) | other = ~28 Å (E12C-R1 (P1-P1)) |
| [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) | `NMR_spin_relaxation_and_MF` | `target` | free CheA for TRACT; with non-labeled Ch | tau_m (2) | tau_m = ~30 ns (P1 domain) |
| [`10.1073/pnas.2218467120`](https://doi.org/10.1073/pnas.2218467120) | `HDX_NMR_and_MS` | `target` | CF4Q complexes (kinase-on) | other (2) | other = >16 h (P1 dimer interface peptide (EX2 t1/2…) |
| [`10.1073/pnas.2218467120`](https://doi.org/10.1073/pnas.2218467120) | `HDX_NMR_and_MS` | `target` | CF4E complexes (partially kinase-off) | other (2) | other = 3 min (P3 interface peptide (EX1 t1/2)) |
| [`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328) | `EPR_DEER` | `homolog` | ADP, foldon complex | other (2) | other = ~ 5 Å (E387C-R1 (P4-P4)) |
| [`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328) | `EPR_DEER` | `homolog` | free kinase, ADP-NO | other (2) | other = ~45 Å (E588C-R1 to ADP-NO (P5-P4)) |
| [`10.1007/s00723-018-1070-6`](https://doi.org/10.1007/s00723-018-1070-6) | `EPR_DEER` | `homolog` | apo (no ADP-β-S-SL) | other (1) | other = 45 Å (E387C-SL to E387C-SL across the two …) |
| [`10.1007/s00723-018-1070-6`](https://doi.org/10.1007/s00723-018-1070-6) | `EPR_DEER` | `homolog` | bound to ADP-β-S-SL | other (1) | other = 35 Å (E387C-SL to ADP-β-S-SL bound on P4 (…) |
| [`10.1186/1471-2180-11-222`](https://doi.org/10.1186/1471-2180-11-222) | `Biophysics_and_other` | `same_protein_other_construct` | in vivo, at receptor clusters, low recep | other (1) | other = ~15 min (whole protein (YFP-CheAΔ258 at recep…) |

## 3. Computational (MD/MSM) and cryo-structure (X-ray / cryo-EM) rows

*1 rows intentionally separated from experimental solution dynamics pending expert scope lock:*

| Method group | Quantity | Value | Residues / group | Paper |
|---|---|---|---|---|
| `MD_and_MSM` | `population` | ~23% % of total ensemble | cluster 3 (inter-domain arrangement of P3, P4, P5) | [`10.1021/ja3056694`](https://doi.org/10.1021/ja3056694) |

## 4. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **amide proton dispersion (microsecond to millisecond exchange)** ([`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379), sample `S1`): 360, 390–398, 400, 401, 403, and 439
- **amide nitrogen dispersion (microsecond to millisecond exchange)** ([`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379), sample `S1`): 391–395, 517, and 518
- **P1 domain residues used in the isotropic/global overall-motion fit** ([`10.1021/bi951960e`](https://doi.org/10.1021/bi951960e), sample `S1`): 13-126
- **linker residues with highly flexible motion (negative 15N{1H} NOE)** ([`10.1021/bi951960e`](https://doi.org/10.1021/bi951960e), sample `S1`): S136-S158
- **P4-P5 linker mutated residues (inter-domain dynamics)** ([`10.1021/ja3056694`](https://doi.org/10.1021/ja3056694), sample `S2`): L507A, T508A, L509A
- **P3-P4 linker mutated residues (inter-domain dynamics)** ([`10.1021/ja3056694`](https://doi.org/10.1021/ja3056694), sample `S2`): M322A, R325D, M326A
- **CheY-binding interface on the CheA P1 domain in the P1-CheY bound state (cross-saturation)** ([`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x), sample `S3`): I43, H48-I50, G52, L68, D70, F91, Q109 (amide); I5, A42, A54 (methyl)
- **P4 domain rigid-body rotation (undipped/dipped interconversion) in GSA sampling** ([`10.1038/s42003-019-0748-0`](https://doi.org/10.1038/s42003-019-0748-0), sample `S1`): 326-328
- **P4 dipped-state stabilizing salt bridges (T. maritima MD)** ([`10.7554/elife.08419`](https://doi.org/10.7554/elife.08419), sample `S2`): R297/E397 and E390/R379

### Conformational and complex PDB states (`States`)

- [`1U0S`](https://www.rcsb.org/structure/1U0S): CheY in complex with the P2 domain of CheA (single binding mode in crystal) ([`10.1021/acs.jpcb.8b05619`](https://doi.org/10.1021/acs.jpcb.8b05619))
- [`1B3Q`](https://www.rcsb.org/structure/1B3Q): T. maritima CheA dimer (homolog) ([`10.1021/jasms.2c00262`](https://doi.org/10.1021/jasms.2c00262))
- [`6S1K`](https://www.rcsb.org/structure/6S1K): CheA/CheW/receptor-fragment signaling array model (cryo-ET-based) ([`10.1021/jasms.2c00262`](https://doi.org/10.1021/jasms.2c00262))
- [`2LP4`](https://www.rcsb.org/structure/2LP4): CheA P1 and P2 domain NMR structures ([`10.1021/jasms.2c00262`](https://doi.org/10.1021/jasms.2c00262))
- [`3JA6`](https://www.rcsb.org/structure/3JA6): T. maritima core signalling unit (CheA in receptor–CheW–CheA complex; homolog), compared to the E. coli CSU ([`10.1038/s41467-020-14350-9`](https://doi.org/10.1038/s41467-020-14350-9))
- [`2LP4`](https://www.rcsb.org/structure/2LP4): model of the E. coli isolated P1 domain-CheY complex, used as the reference for the P1-CheY bound state ([`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x))
- [`3KYJ`](https://www.rcsb.org/structure/3KYJ): R. sphaeroides CheA3 P1-CheY6 crystal structure (homolog), compared with the P1-CheY bound state ([`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x))
- [`1TQG`](https://www.rcsb.org/structure/1TQG): parallel P1 dimer (crystal structure of isolated T. maritima P1) compatible with the DEER P1 restraints ([`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328))
- [`4XIV`](https://www.rcsb.org/structure/4XIV): T. maritima CheA P3P4P5 crystal structure (homolog) ([`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328))
- [`3UR1`](https://www.rcsb.org/structure/3UR1): CheA P4P5 with CheW and receptor fragment (crystal) (homolog) ([`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328))
- [`6S1K`](https://www.rcsb.org/structure/6S1K): E. coli core complex ([`10.1126/scisignal.abj1737`](https://doi.org/10.1126/scisignal.abj1737))
- [`4XIV`](https://www.rcsb.org/structure/4XIV): planar P3-P4 arrangement (T. maritima CheA.P3-P4 crystal structure) ([`10.1128/mbio.00793-23`](https://doi.org/10.1128/mbio.00793-23))
- [`3JA6`](https://www.rcsb.org/structure/3JA6): undipped CheA conformation ([`10.1128/mbio.00793-23`](https://doi.org/10.1128/mbio.00793-23))
- [`6S1K`](https://www.rcsb.org/structure/6S1K): undipped CheA conformation ([`10.1128/mbio.00793-23`](https://doi.org/10.1128/mbio.00793-23))
- [`4JPB`](https://www.rcsb.org/structure/4JPB): T. maritima (CheA.P5/CheW) ring crystal structure (homolog) ([`10.1128/mbio.00793-23`](https://doi.org/10.1128/mbio.00793-23))

## 5. Papers read and explicit gaps

**Checked `v3` / supplemental papers (23):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi951960e`](https://doi.org/10.1021/bi951960e) | 1052 | 0 | 2 | 3 | 15N backbone relaxation (T1, T2, 15N{1H} NOE at 500 MHz, pH 6.3, 30 C) of CheA1-233. Main text gives domain-av |
| [`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328) | 15 | 3 | 0 | 1 | No NMR or kinetic dynamics numbers are printed. The paper reports DEER distances for Thermotoga maritima CheA  |
| [`10.1073/pnas.2218467120`](https://doi.org/10.1073/pnas.2218467120) | 11 | 0 | 0 | 1 | HDX-MS study of E. coli CheA. The only printed dynamics rates are bimodal EX1/EX2 uptake half-lives for one P1 |
| [`10.1021/acs.jpcb.8b05619`](https://doi.org/10.1021/acs.jpcb.8b05619) | 7 | 1 | 0 | 1 | The paper prints Cu2+-NO and Cu2+-Cu2+ DEER distances for the CheA P1P2 / CheY41PyTyr complex (two nitroxide p |
| [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) | 5 | 2 | 1 | 3 |  |
| [`10.1007/s00723-018-1070-6`](https://doi.org/10.1007/s00723-018-1070-6) | 2 | 0 | 0 | 1 | The paper is a spin-label method paper. The only dynamics-type numbers are two DEER distance peaks for T. mari |
| [`10.1016/j.bpj.2026.05.001`](https://doi.org/10.1016/j.bpj.2026.05.001) | 2 | 0 | 0 | 1 | The paper is a CSP and S/N study of CheA-P1 binding; it prints no rate, Rex, order parameter or relaxation val |
| [`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379) | 1 | 0 | 2 | 2 | One dynamics number is printed: a global CPMG kex of ~1250 +/- 100 s-1 for T. maritima CheA P4l. Populations a |
| [`10.1021/ja3056694`](https://doi.org/10.1021/ja3056694) | 1 | 0 | 2 | 1 | Computational (REMD) plus biochemical paper; no NMR or other experimental dynamics measurement. One MD-derived |
| [`10.1186/1471-2180-11-222`](https://doi.org/10.1186/1471-2180-11-222) | 1 | 0 | 0 | 1 | In-vivo FRAP study of cluster exchange in E. coli chemotaxis. The only printed number for CheA is the approxim |
| [`10.1016/j.jmb.2012.05.023`](https://doi.org/10.1016/j.jmb.2012.05.023) | 0 | 0 | 0 | 1 | The paper is a methyl-TROSY chemical-shift-perturbation study of CheA P4P5 binding to a chemoreceptor fragment |
| [`10.1021/bi300147m`](https://doi.org/10.1021/bi300147m) | 0 | 0 | 0 | 0 | The paper builds a docked structural model of the E. coli CheA P1 domain with CheY/P2 from intermolecular NOEs |
| [`10.1021/bi501570n`](https://doi.org/10.1021/bi501570n) | 0 | 0 | 0 | 2 | No NMR relaxation or exchange data. The paper measures CheA autophosphorylation kinetics (Table 2), SAXS, MALS |
| [`10.1021/bi900641c`](https://doi.org/10.1021/bi900641c) | 0 | 0 | 0 | 0 | No NMR, HDX, FRET or EPR dynamics value is printed for CheA. The paper measures stability of membrane-bound re |
| [`10.1021/jasms.2c00262`](https://doi.org/10.1021/jasms.2c00262) | 0 | 3 | 0 | 0 | The paper is a DEPC covalent-labeling mass spectrometry study of CheA binding to CheW and CF4Q on vesicles. It |
| [`10.1038/msb.2008.77`](https://doi.org/10.1038/msb.2008.77) | 0 | 0 | 0 | 1 | In vivo FRET interaction map of E. coli chemotaxis proteins. No NMR, MD or structural dynamics value for CheA  |
| [`10.1038/s41467-020-14350-9`](https://doi.org/10.1038/s41467-020-14350-9) | 0 | 1 | 0 | 0 | Cryo-ET and subtomogram averaging paper on the chemosensory array core signalling unit, with an MD-flexible-fi |
| [`10.1038/s42003-019-0748-0`](https://doi.org/10.1038/s42003-019-0748-0) | 0 | 0 | 1 | 0 |  |
| [`10.1111/mmi.12309`](https://doi.org/10.1111/mmi.12309) | 0 | 0 | 0 | 1 | Electron cryotomography and protease-sensitivity paper. It prints no dynamics rate, population, order paramete |
| [`10.1126/scisignal.abj1737`](https://doi.org/10.1126/scisignal.abj1737) | 0 | 1 | 0 | 2 | This paper yields 0 CheA protein dynamics rows (expected_rows is empty) because it investigates E. coli chemor |
| [`10.1128/mbio.00793-23`](https://doi.org/10.1128/mbio.00793-23) | 0 | 4 | 0 | 0 | Cryo-ET/sub-tomogram averaging, AlphaFold2 and MD structure paper. It prints no NMR, HDX, FRET or other dynami |
| [`10.7554/elife.08419`](https://doi.org/10.7554/elife.08419) | 0 | 0 | 1 | 0 |  |
| [`10.7554/elife.27455`](https://doi.org/10.7554/elife.27455) | 0 | 0 | 0 | 0 | Zero rows. The paper measures in vivo single-cell FRET between CheY and CheZ as a readout of whole-network kin |

**Explicit figure-only, SI-only, or access gaps (22):**

- DEER distance distributions P(r), widths and relative populations of the 45 Å and 35 Å peaks ([`10.1007/s00723-018-1070-6`](https://doi.org/10.1007/s00723-018-1070-6)): figure only (Fig. 4)
- Per-residue CSPs, S/N values and ATP KD list (Tables S1-S4) ([`10.1016/j.bpj.2026.05.001`](https://doi.org/10.1016/j.bpj.2026.05.001)): in supplement not available
- Chemical shift change magnitudes for Ile563/Ile566 and receptor residues ([`10.1016/j.jmb.2012.05.023`](https://doi.org/10.1016/j.jmb.2012.05.023)): figure only (methyl TROSY spectra in Figs 1 and 2); and they are binding shifts, not dynamics values
- Full distance distributions P(r) for the P2 and P1 complexes, modulation depths, and time-domain traces ([`10.1021/acs.jpcb.8b05619`](https://doi.org/10.1021/acs.jpcb.8b05619)): figure only (Figs. 3, 4, S6-S8); the Cu2+-Cu2+ modulation depth is only given as a range for fully occupied sites
- Dispersion curves for P4l and the damped profiles of P4 (Figures 2, S5, S6, S7) ([`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379)): figure only; no values printed
- Minor-state population and delta-omega ([`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379)): paper states the population could not be defined; none printed
- DEER distance distributions for T. maritima CheA Q545C and TarFO E389C ([`10.1021/bi501570n`](https://doi.org/10.1021/bi501570n)): figure only; the text gives only a ~7 A shift (a difference, and a homolog) and Tar distances (a different protein)
- CheY-P formation and decay kinetics ([`10.1021/bi501570n`](https://doi.org/10.1021/bi501570n)): in supplement not available
- tau_e of residue 91 in Table S2 ([`10.1021/bi951960e`](https://doi.org/10.1021/bi951960e)): garbled table: printed as 0.T160E-06, value not recoverable
- Per-residue fit deviations and error(%) columns in Table S2 ([`10.1021/bi951960e`](https://doi.org/10.1021/bi951960e)): fit-quality columns, not dynamics values; not extracted
- Figure 5 T1, T2, tau_m and S2 profiles for CheA1-134 versus CheA1-233; NOE profile ([`10.1021/bi951960e`](https://doi.org/10.1021/bi951960e)): figure only; the numbers for CheA1-233 are in Table S2
- Cα RMSD and per-residue RMSF of the simulations, angle distributions ([`10.1021/ja3056694`](https://doi.org/10.1021/ja3056694)): figure only (Figures 1, S2, S3) or in supplement not available
- *... plus 10 additional gap entries in the `Gaps` tab.*

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
