# Cold shock protein CspA (`CSPA`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P0A9X9` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

*6 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `kAB` | 2.0×104 s−1 | F to I step of three-state model, Tf 77 °C | `Biophysics_and_other` | `target` | apo; T-jump final 70-77 °C (see rows); equilibrium melts 9 °C upward; pH pH* 7 | `no` | [`10.1021/bi301296y`](https://doi.org/10.1021/bi301296y) |
| `kAB` | 4.4×103 s−1 | I to U step of three-state model, Tf 77 °C | `Biophysics_and_other` | `target` | apo; T-jump final 70-77 °C (see rows); equilibrium melts 9 °C upward; pH pH* 7 | `no` | [`10.1021/bi301296y`](https://doi.org/10.1021/bi301296y) |
| `kex` | 550 ± 30 s−1 ± 30 | CspA amide sites with flat dispersion profiles in free form (glob | `NMR_exchange_and_dispersion` | `target` | bound to/exchanging with ACB RNA; 20°C; pH 6.5; not stated | `unclear` | [`10.1093/nar/gkx044`](https://doi.org/10.1093/nar/gkx044) |
| `population` | 5.4 ± 0.8 % ± 0.8 | free CspA (minor state) | `NMR_other` | `target` | bound to/exchanging with ACB RNA; 20°C; pH 6.5; not stated | `unclear` | [`10.1093/nar/gkx044`](https://doi.org/10.1093/nar/gkx044) |
| `kex` | ≈ 1000 s−1 | free/ACB-bound CspA exchange | `NMR_other` | `target` | free and bound to ACB RNA; 45°C; pH 6.5; not stated | `no` | [`10.1093/nar/gkx044`](https://doi.org/10.1093/nar/gkx044) |
| `population` | ∼18 % | free CspA in exchange with complex | `NMR_exchange_and_dispersion` | `target` | free and bound to ACB RNA; 45°C; pH 6.5; not stated | `no` | [`10.1093/nar/gkx044`](https://doi.org/10.1093/nar/gkx044) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*346 rows total (333 spin-relaxation/model-free; 13 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j) | `NMR_spin_relaxation_and_MF` | `target` | apo | R1 (60), R2 (60), NOE (60), S2 (59), tau_e (44), Rex (34) | R1 = 2.39 s-1 (average over 59 N-H sites) |
| [`10.1021/bi301296y`](https://doi.org/10.1021/bi301296y) | `Biophysics_and_other` | `target` | apo | other (4) | other = 50 μs (global (whole protein, 1634 cm-1 fas…) |
| [`10.1021/bi301296y`](https://doi.org/10.1021/bi301296y) | `FRET_and_fluorescence` | `target` | apo | other (4) | other = 56 μs (global (Trp11 fluorescence fast phas…) |
| [`10.1021/bi301296y`](https://doi.org/10.1021/bi301296y) | `FRET_and_fluorescence` | `same_protein_other_construct` | apo | other (4) | other = 22 μs (global fast phase (τobs1), T-jump 58…) |
| [`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j) | `HDX_NMR_and_MS` | `target` | apo | other (1) | other = 2 h  (nearly all amide proton sites) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **Rex > 2 Hz (13 N-H sites)** ([`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j), sample `S1`): Gly-3, Lys-10, Trp-11, Phe-12, Asn-13, Phe-18, Gly-19, Phe-31, His-33, Lys-43, Asp-46, Thr-54, Lys-60
- **R2 > 10 s-1** ([`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j), sample `S1`): Lys-10-Asn-13, Phe-31, His-33, Thr-54, Lys-60
- **HNOE < 0.5 (fast sub-nanosecond motion)** ([`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j), sample `S1`): Gly-3, Asn-39-Lys-43, Asp-46, Gly-58-Gly-61
- **low S2, large-amplitude sub-ns motion** ([`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j), sample `S1`): Gly-3, Asn-39-Lys-43, Asp-46, Ser-57-Gly-61, Leu-70
- **fit only by multiple-time-scale model 5 (text list)** ([`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j), sample `S1`): Met-5, Gly-17, Gly-41, Leu-70
- **slowest-exchanging amide protons** ([`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j), sample `S2`): Val-9, Ile-21, Thr-22, Val-30, Val-32, Val-51
- **extensive line broadening on ACB binding** ([`10.1093/nar/gkx044`](https://doi.org/10.1093/nar/gkx044), sample `S2`): 11–14, 16–20, 31–39, 42–44, 63, 69
- **conformational exchange by relaxation dispersion** ([`10.1093/nar/gkx044`](https://doi.org/10.1093/nar/gkx044), sample `S1`): 11–13, 18–21, 30–31, 35, 42–43, 53–56, 66–68
- **free-form exchange quenched in RNA-bound form** ([`10.1093/nar/gkx044`](https://doi.org/10.1093/nar/gkx044), sample `S2`): I21, E56, V67

### Conformational and complex PDB states (`States`)

- [`2MEF`](https://www.rcsb.org/structure/2MEF): refined solution NMR structure of CspA (16 conformers) deposited with this paper ([`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j))
- [`1MJC`](https://www.rcsb.org/structure/1MJC): E. coli CspA structure (ribbon representation) ([`10.1093/nar/gkx044`](https://doi.org/10.1093/nar/gkx044))
- [`3PF4`](https://www.rcsb.org/structure/3PF4): B. subtilis CspB (homolog) in complex with an eptanucleotide RNA oligo (GUCUUUA) ([`10.3389/fmicb.2023.1118329`](https://doi.org/10.3389/fmicb.2023.1118329))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (6):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j) | 334 | 1 | 6 | 3 |  |
| [`10.1021/bi301296y`](https://doi.org/10.1021/bi301296y) | 14 | 0 | 0 | 2 | Optical T-jump folding kinetics (IR and Trp fluorescence) of CspA at 70-77 °C; no NMR dynamics measured. 6 tim |
| [`10.1093/nar/gkx044`](https://doi.org/10.1093/nar/gkx044) | 4 | 1 | 3 | 2 |  |
| [`10.1007/s10858-023-00414-7`](https://doi.org/10.1007/s10858-023-00414-7) | 0 | 0 | 0 | 3 | This record has 0 dynamics rows (expected_rows: []), 0 conformational states (expected_states: []), and 0 dyna |
| [`10.1186/1756-0500-6-248`](https://doi.org/10.1186/1756-0500-6-248) | 0 | 0 | 0 | 0 | This paper yields 0 expected dynamics rows, 0 conformational states, and 0 dynamic residue sets because it is  |
| [`10.3389/fmicb.2023.1118329`](https://doi.org/10.3389/fmicb.2023.1118329) | 0 | 1 | 0 | 0 | Zero protein-dynamics rows (expected_rows = []): this paper investigates how Escherichia coli CspA stimulates  |

**Explicit figure-only, SI-only, or access gaps (10):**

- Table S2 (CspA 4ΔN(ND) isotope shifts in ppb; chemical-shift isotope splittings rather than dynamics parameters) ([`10.1007/s10858-023-00414-7`](https://doi.org/10.1007/s10858-023-00414-7)): in supplement not available
- Table S4 (44 CspA 3ΔC’(ND) isotope shifts in ppb; chemical-shift isotope splittings rather than dynamics parameters) ([`10.1007/s10858-023-00414-7`](https://doi.org/10.1007/s10858-023-00414-7)): in supplement not available
- Fig. 2A, 2B, 2D and Fig. 3C, 3D plotted per-residue CspA 4ΔN(ND) and 3ΔC’(ND) isotope shift values (non-dynamics chemical-shift splittings) ([`10.1007/s10858-023-00414-7`](https://doi.org/10.1007/s10858-023-00414-7)): figure only
- Arrhenius rates of fast and slow phases vs temperature ([`10.1021/bi301296y`](https://doi.org/10.1021/bi301296y)): figure only (Figure 6)
- NMR relaxation of CspA (Trp11 and beta3-beta4 loop motions) ([`10.1021/bi301296y`](https://doi.org/10.1021/bi301296y)): cited from earlier work (refs 27, 32), no values printed
- Table S1 NMR data collection parameters (spectral widths, points) ([`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j)): acquisition settings, not dynamics values
- Residue-level hydrogen-exchange half-lives ([`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j)): figure only (Figure 3 symbols for t1/2 > 3 min, < 30 min, > 30 min); no numbers per residue
- Figure 7 S2, tau_e, Rex profiles ([`10.1021/bi980269j`](https://doi.org/10.1021/bi980269j)): values are printed in Table S4, so the figure adds nothing
- Per-residue CPMG dispersion curves and fitted parameters for CspA at 20°C, 15N R2/HETNOE at 45°C ([`10.1093/nar/gkx044`](https://doi.org/10.1093/nar/gkx044)): Supplementary Figure S5 and Figure 7 only; no printed numbers, supplement not in text
- Temperature dependence of Kd and ΔS for CspA-ACB ([`10.1093/nar/gkx044`](https://doi.org/10.1093/nar/gkx044)): Kd and ΔS are thermodynamic binding values, not dynamics; per-temperature Kd values not in text

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
