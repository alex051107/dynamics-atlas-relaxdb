# Mercuric transport protein periplasmic component (merP) (`MERP`)

**Atlas tier:** Tier 3 · Qualitative regions / PDB states / Release 0.1 unknown / twin link / 0-numeric full text  
**UniProt:** `P04129` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **conformational exchange (Rex term needed in fit; slow-timescale loop motion in reduced form)** ([`10.1021/bi9631632`](https://doi.org/10.1021/bi9631632), sample `S1`): 11-18
- **some evidence of mobility (long T1), loop B3 to helix 2** ([`10.1021/bi9631632`](https://doi.org/10.1021/bi9631632), sample `S1`): 51-53
- **fast-timescale mobility (low S2, low NOE, high T1 and T2)** ([`10.1021/bi9631632`](https://doi.org/10.1021/bi9631632), sample `S1`): 1, 2, and 72

### Conformational and complex PDB states (`States`)

- [`1AFI`](https://www.rcsb.org/structure/1AFI): coordinates of the reduced and mercury-bound forms (assignment of each id to a form not stated in text) ([`10.1021/bi9631632`](https://doi.org/10.1021/bi9631632))
- [`1AFJ`](https://www.rcsb.org/structure/1AFJ): coordinates of the reduced and mercury-bound forms (assignment of each id to a form not stated in text) ([`10.1021/bi9631632`](https://doi.org/10.1021/bi9631632))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (2):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi9631632`](https://doi.org/10.1021/bi9631632) | 0 | 2 | 3 | 2 | Structure paper; the dynamics section prints no numeric relaxation values (T1, T2, NOE, S2, Rex all appear onl |
| [`10.3389/fbioe.2024.1407874`](https://doi.org/10.3389/fbioe.2024.1407874) | 0 | 0 | 0 | 0 | A perfect extraction for this paper contains 0 expected_rows, 0 expected_states, and 0 expected_residue_sets.  |

**Explicit figure-only, SI-only, or access gaps (2):**

- Per-residue 15N T1, T2, heteronuclear NOE, fitted S2 and Rex for reduced and mercury-bound merP ([`10.1021/bi9631632`](https://doi.org/10.1021/bi9631632)): figure only (Figure 7)
- Chemical shift assignments ([`10.1021/bi9631632`](https://doi.org/10.1021/bi9631632)): in supplement not available (Supporting Information tables)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
