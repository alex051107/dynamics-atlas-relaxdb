# Pancreatic trypsin inhibitor (`BPTI`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P00974` · **RelaxDB deposited card:** T = `298.0`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

*10 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `kex` | > 103 s−1 | F22 ring flip at 300 MPa, room temperature | `NMR_exchange_and_dispersion` | `target` | apo; 5°C to 65°C; reference point 20°C; pH 7.0; 600 (14.1 T); 800 (18.8 T) at 5°C and | `unclear` | [`10.1002/cbic.70442`](https://doi.org/10.1002/cbic.70442) |
| `delta_omega` | 1.53 ppm | Y23ε | `NMR_exchange_and_dispersion` | `target` | apo; 5°C to 65°C; reference point 20°C; pH 7.0; 600 (14.1 T); 800 (18.8 T) at 5°C and | `unclear` | [`10.1002/cbic.70442`](https://doi.org/10.1002/cbic.70442) |
| `delta_omega` | 2.21 ppm | Y35ε | `NMR_exchange_and_dispersion` | `target` | apo; 5°C to 65°C; reference point 20°C; pH 7.0; 600 (14.1 T); 800 (18.8 T) at 5°C and | `unclear` | [`10.1002/cbic.70442`](https://doi.org/10.1002/cbic.70442) |
| `delta_omega` | 1.90 ppm | F45δ | `NMR_exchange_and_dispersion` | `target` | apo; 5°C to 65°C; reference point 20°C; pH 7.0; 600 (14.1 T); 800 (18.8 T) at 5°C and | `unclear` | [`10.1002/cbic.70442`](https://doi.org/10.1002/cbic.70442) |
| `delta_omega` | 0.49 ppm | F45ε | `NMR_exchange_and_dispersion` | `target` | apo; 5°C to 65°C; reference point 20°C; pH 7.0; 600 (14.1 T); 800 (18.8 T) at 5°C and | `unclear` | [`10.1002/cbic.70442`](https://doi.org/10.1002/cbic.70442) |
| `population` | 0.5 | two ring-flip states (p1 = p2) | `NMR_exchange_and_dispersion` | `target` | apo; 5°C to 65°C; reference point 20°C; pH 7.0; 600 (14.1 T); 800 (18.8 T) at 5°C and | `unclear` | [`10.1002/cbic.70442`](https://doi.org/10.1002/cbic.70442) |
| `kex` | (6.2 ± 2.1) × 103 s−1 ± 2.1 × 103 (one SD, Monte-Carlo) | Y23 13Cε | `NMR_exchange_and_dispersion` | `target` | apo; 55 °C; pH 7.1; 11.7 T | `no` | [`10.1007/s10858-014-9826-2`](https://doi.org/10.1007/s10858-014-9826-2) |
| `delta_omega` | 1.43 ppm ± 0.09 | Y23 13Cε | `NMR_exchange_and_dispersion` | `target` | apo; 55 °C; pH 7.1; 11.7 T | `no` | [`10.1007/s10858-014-9826-2`](https://doi.org/10.1007/s10858-014-9826-2) |
| `delta_omega` | 1.50 ppm | Y23 13Cε | `NMR_exchange_and_dispersion` | `target` | apo; 5 and 15 °C; pH not stated; not stated | `unclear` | [`10.1007/s10858-014-9826-2`](https://doi.org/10.1007/s10858-014-9826-2) |
| `population` | 32 % | whole protein (global) | `HDX_NMR_and_MS` | `target` | apo; 25 °C; pH pD 7.43 | `unclear` | [`10.3390/biomimetics9080485`](https://doi.org/10.3390/biomimetics9080485) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*30 rows total (0 spin-relaxation/model-free; 30 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1002/cbic.70442`](https://doi.org/10.1002/cbic.70442) | `NMR_exchange_and_dispersion` | `target` | apo | other (30) | other = 52.4 kJ mol−1 (F22 ring flip (activation free energ…) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **slow aromatic ring flips studied via chemical shift-mediated exchange broadening** ([`10.1002/cbic.70442`](https://doi.org/10.1002/cbic.70442), sample `S1`): F22, Y23, Y35, F45

### Conformational and complex PDB states (`States`)

- [`5pti`](https://www.rcsb.org/structure/5pti): crystal structure used for Voronoi ground-state ring volumes and structure figure ([`10.1002/cbic.70442`](https://doi.org/10.1002/cbic.70442))
- [`1pit`](https://www.rcsb.org/structure/1pit): free BPTI, NMR solution structure ([`10.3390/biomimetics9080485`](https://doi.org/10.3390/biomimetics9080485))
- [`4y0y`](https://www.rcsb.org/structure/4y0y): BPTI in trypsin-BPTI complex (crystal) ([`10.3390/biomimetics9080485`](https://doi.org/10.3390/biomimetics9080485))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (7):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1002/cbic.70442`](https://doi.org/10.1002/cbic.70442) | 36 | 1 | 1 | 1 | BPTI aromatic ring flips (F22, Y23, Y35, F45) from 13C CPMG/R1rho dispersion at 0.1-300 MPa and 5-65 C. The pr |
| [`10.1007/s10858-014-9826-2`](https://doi.org/10.1007/s10858-014-9826-2) | 3 | 0 | 0 | 1 | Method paper. The only BPTI dynamics numbers are the Y23 ring-flip fit (kex, delta-omega in ppm) from L-TROSY  |
| [`10.3390/biomimetics9080485`](https://doi.org/10.3390/biomimetics9080485) | 1 | 2 | 0 | 1 | TAP is the subject; BPTI appears as a comparison protein in global HDX-MS (Figure 4). The only printed BPTI dy |
| [`10.1016/j.jmb.2008.07.063`](https://doi.org/10.1016/j.jmb.2008.07.063) | 0 | 0 | 0 | 1 | The paper reports hydrolysis rates, binding thermodynamics and crystal structures of BPTI Cys14/Cys38 variants |
| [`10.1016/j.redox.2025.103534`](https://doi.org/10.1016/j.redox.2025.103534) | 0 | 0 | 0 | 0 |  |
| [`10.1039/c4sc03227f`](https://doi.org/10.1039/c4sc03227f) | 0 | 0 | 0 | 0 | The paper reports synthesis, CD thermal stability, trypsin inhibition and crystal structures of BPTI P1 varian |
| [`10.1039/c8sc01110a`](https://doi.org/10.1039/c8sc01110a) | 0 | 0 | 0 | 0 | The paper reports oxidative folding kinetics (HPLC), reductive unfolding, chymotrypsin inhibition, CD and crys |

**Explicit figure-only, SI-only, or access gaps (4):**

- per-condition kflip values for F22, Y23, Y35, F45 at each pressure and temperature (Tables S1-S4, Figures S1-S4) ([`10.1002/cbic.70442`](https://doi.org/10.1002/cbic.70442)): in supplement not available
- R1rho and CPMG dispersion profiles of Y23 ([`10.1007/s10858-014-9826-2`](https://doi.org/10.1007/s10858-014-9826-2)): figure only (Fig. 2)
- Crystallographic B-value profiles of inhibitor and trypsin backbone atoms (Figure 9) ([`10.1016/j.jmb.2008.07.063`](https://doi.org/10.1016/j.jmb.2008.07.063)): figure only
- %D time course for BPTI (10 s to 1 h) ([`10.3390/biomimetics9080485`](https://doi.org/10.3390/biomimetics9080485)): figure only (Figure 4C)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
