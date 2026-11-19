# Olfactory marker protein (`OMP`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P08523` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600/800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*1051 rows total (1051 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi050149t`](https://doi.org/10.1021/bi050149t) | `NMR_spin_relaxation_and_MF` | `target` | apo (no Bex peptide) | NOE (274), R1 (270), R2 (270), S2 (139), tau_e (42), Rex (38) | R1 = 1.350 s-1 (Gln9) |
| [`10.1021/bi050149t`](https://doi.org/10.1021/bi050149t) | `NMR_spin_relaxation_and_MF` | `target` | apo | tau_m (5) | tau_m = 13.26 ns (global) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **Residues with conformational exchange in helix 1 (plot of 1DNH versus T1/T2)** ([`10.1021/bi050149t`](https://doi.org/10.1021/bi050149t), sample `S1`): L21, T22, K23, Q24, M25, V29, and S31
- **Residues in loop 1 with exchange contributions to T2 (1DNH versus T1/T2)** ([`10.1021/bi050149t`](https://doi.org/10.1021/bi050149t), sample `S1`): R35, K39, L44, L45, L46, R47
- **Residues in loop 3 (omega loop) with exchange contributions to T2 (1DNH versus T1/T2)** ([`10.1021/bi050149t`](https://doi.org/10.1021/bi050149t), sample `S1`): S84, N86, T87, D90, L94, T96, L99
- **Loop residues with fast R2 or missing, indicative of millisecond exchange (Rex)** ([`10.1021/bi050149t`](https://doi.org/10.1021/bi050149t), sample `S1`): loop 1 E43-A49; omega loop majority of 84-99; loop 4 F145, G146, E150
- **Residues given fast internal motion (model with tau_e) in model-free analysis** ([`10.1021/bi050149t`](https://doi.org/10.1021/bi050149t), sample `S1`): Q9-Q10; loop 1 R35-D41; loop 2 F57-H67; Q162

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi050149t`](https://doi.org/10.1021/bi050149t) | 1051 | 0 | 5 | 2 | No exchange kinetics are printed. The paper gives per-residue 15N R1, R2 and NOE at 600 and 800 MHz (Table 1s, |

**Explicit figure-only, SI-only, or access gaps (2):**

- Per-residue Rex values at 81 MHz and per-residue values plotted in Figures 2-5 ([`10.1021/bi050149t`](https://doi.org/10.1021/bi050149t)): figure only
- Model-free parameters from X-ray coordinates ([`10.1021/bi050149t`](https://doi.org/10.1021/bi050149t)): Table 2s gives only the model number for the X-ray column

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
