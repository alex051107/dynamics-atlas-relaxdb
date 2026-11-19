# PTS system glucose-specific EIICBA component (`GPIIA`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P20166` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*43 rows total (38 spin-relaxation/model-free; 5 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi00133a003`](https://doi.org/10.1021/bi00133a003) | `NMR_spin_relaxation_and_MF` | `target` | apo (unphosphorylated) | tau_e (12), S2 (11), other (7), NOE (3), tau_m (2), Rex (2) | S2 = 0.03  (I2 (printed '12')) |
| [`10.1021/bi00242a013`](https://doi.org/10.1021/bi00242a013) | `HDX_NMR_and_MS` | `target` | apo | other (5) | other = 1.75 10^-5 s^-1 (amide NH solvent exchange rate constant km, D |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **highly disordered N-terminal tail** ([`10.1021/bi00133a003`](https://doi.org/10.1021/bi00133a003), sample `S1`): 1-13
- **negative NOE (high mobility) residues** ([`10.1021/bi00133a003`](https://doi.org/10.1021/bi00133a003), sample `S1`): I2-G11 and Q32
- **more mobile region near the active site** ([`10.1021/bi00133a003`](https://doi.org/10.1021/bi00133a003), sample `S1`): D31-D41
- **mobile C-terminal loop region** ([`10.1021/bi00133a003`](https://doi.org/10.1021/bi00133a003), sample `S1`): A146 to V150

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (2):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi00133a003`](https://doi.org/10.1021/bi00133a003) | 38 | 0 | 4 | 3 | One sample (B. subtilis IIAGlc, 308 K, pH 6.6, 500 MHz), 15N T1/T2/NOE and model-free analysis. Printed number |
| [`10.1021/bi00242a013`](https://doi.org/10.1021/bi00242a013) | 5 | 0 | 0 | 2 |  |

**Explicit figure-only, SI-only, or access gaps (5):**

- Per-residue T1, T2, NOE, S2, tau_e and Rex for all 137 residues ([`10.1021/bi00133a003`](https://doi.org/10.1021/bi00133a003)): figure only (Figures 4 and 5) and supplementary table not in the text
- tau_e of A3 (283 with garbled uncertainty and unit, from Figure 5 caption) ([`10.1021/bi00133a003`](https://doi.org/10.1021/bi00133a003)): garbled figure caption text; unit and uncertainty unreadable
- Dynamics parameters of L136 ([`10.1021/bi00133a003`](https://doi.org/10.1021/bi00133a003)): paper says the double time scale analysis gave no realistic parameters
- Exchange rate constants of the other ~73 of the 78 slowly exchanging amide NH groups ([`10.1021/bi00242a013`](https://doi.org/10.1021/bi00242a013)): figure only: plotted as -log km vs residue in Figure 8B; no printed values
- Classes of amide NH by km (10^-3 < km < 10^-2 s^-1 open circles; km < 10^-3 s^-1 solid circles) per residue in Figure 7 ([`10.1021/bi00242a013`](https://doi.org/10.1021/bi00242a013)): figure only

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
