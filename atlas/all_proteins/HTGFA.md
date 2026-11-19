# Protransforming growth factor alpha (`HTGFA`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P01135` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`possible`)](../proteins/HTGFA.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `possible` (strict two-peak reading: `does not: the source states that the exchange broadening reflects interconversion between multiple protein conformations on the intermediate 15N chemical-exchange (microsecond) timescale, with an author-derived lifetime between about 1.25 µs and 2.5 ms; no kex or Δω is printed (the bounds assume two equal populations and a maximum 10 ppm shift difference), so no regime can be computed, and no second peak set is reported for the free ligand (HTGFA-J12; E-r2). The title's 'slow conformational exchange' means slower than molecular tumbling. The only other stated regime, fast exchange, concerns EGFR-ED binding (HTGFA-J7).`)
- **Reference state:** Entry construct as deposited (mature human TGF-alpha V1-A50), free, no ligand; the RelaxDB source sample (doi:10.1021/bi00008a003, full text): 2 mM 15N protein dissolved directly in 90% H2O/10% D2O with 1 mM NaN3, no buffer stated, pH 7.1 ± 0.1, 30 ± 0.5 °C, 500 MHz, single field (HTGFA-J11 to J15 marked is_wt_apo).
- **Exchange rate (`kex`):** not fitted: single-field Rex > 0.5 Hz at 23 amides (uncertainties about ±0.3-0.5 Hz); author bounds on the exchange lifetime of about 1.25 µs (from a 10 ppm maximum 15N shift difference and a 0.5 Hz detection limit) to about 2.5 ms (from non-refocusing at CPMG 2tau = 720 µs), assuming two equally populated states (HTGFA-J12)
- **Minor-state population (`pB`):** not measured; two equally populated states are an assumption of the lifetime bounds, and the '40%' or 'about half' figure is the fraction of amides with exchange broadening, not a population (HTGFA-J12)
- **Exchanging region:** Rex > 0.5 Hz: D7, C8, T13, F15, C16, F17, H18, T20, C21, R22, F23, L24, V25, Q26, E27, D28, K29, C32, V33, V39, G40, E44, H45 (Q14 unfitted; S36, C43 below threshold; D47 term rejected); > 1.5 Hz at D7, T13, F15, C16, C21, R22, F23, L24, V25, K29, C32, V33, V39, G40 (Table 3, cycle C; largest R22 4.93, V39 3.81, C21 3.50 s-1); interface residues F15-H18, C32-V33, V39-G40, E44-H45 (HTGFA-J12). Fast motion: L48-A50, D7-C8, F17-H18, E27-D28, V39-G40, F23, A31 (HTGFA-J11).
- **Structure comparison:** [{"pdb": "3E50", "what": "TGF-alpha bound to inactive IDE; aa 1-3 and 10-14 visible, D10-Q14 helix-to-strand versus free 1YUF. Partner-bound with possible incomplete occupancy, not an apo alternate state.", "evidence_row": "HTGFA-HTGFA_20261020092056-r7"}, {"pdb": "7SZ5, 7SZ7", "what": "TGF-alpha-bound full-length EGFR cryo-EM classes (tips separated, tips juxtaposed); the heterogeneity is in the receptor. Partner-bound, not an apo alternate state.", "evidence_row": "HTGFA-HTGFA_20261020092056-r12"}]
- **Caveats:** Call raised from unknown to possible on 2026-10-20 after the RelaxDB source paper (doi:10.1021/bi00008a003, Li and Montelione 1995) was read in full: exchange is detected in the reference state as single-field Rex at 23 of 36 analysed amides, and under the single-field Rex rule decided that night (ledger/redraft_notes.json, _RULE_single_field_rex) this counts as exchange detected without a population. Fixed caveat: single-field Rex can also come from anisotropic tumbling; a dispersion experiment would confirm. The authors themselves call the regime intermediate (microsecond) and give only lifetime bounds (1.25 µs to 2.5 ms) under an equal-population, 10 ppm assumption, so the state is not shown to be slow enough for separate peaks; literal_two_peak is 'does not'. The sample has no buffer (direct dissolution with NaN3), the Rex threshold of 0.5 Hz is the authors' operational cutoff with uncertainties of ±0.3-0.5 Hz, and Q26 lacks a reported error. Nine of the other rows are abstracts. The RelaxDB HTGFA source is still unconfirmed (no BMRB id). The abstract-only rows HTGFA-HTGFA_20261020145442-r1 and r2 are superseded and no longer cited. Built from cases V6_r6_HTGFA_20261020092056, S6_r6_HTGFA_20261020145442 and S6_r6_HTGFA_20261020201428.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/HTGFA.md`](../proteins/HTGFA.md) (11 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*229 rows total (229 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi00008a003`](https://doi.org/10.1021/bi00008a003) | `NMR_spin_relaxation_and_MF` | `target` | apo (free protein) | S2 (45), NOE (41), tau_e (37), R1 (36), R2 (36), Rex (26) | NOE = 0.28  (Phe-5) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **15N chemical-exchange line broadening (Rex > 0.5 Hz), microsecond-scale conformational exchange** ([`10.1021/bi00008a003`](https://doi.org/10.1021/bi00008a003), sample `S1`): Asp-7-Cys-8, Thr-13-His-18, Thr-20-Lys-29, Cys-32-Val-33, Val-39-Gly-40, Glu-44-His-45
- **large chemical-exchange broadening attributed to slow equilibrium between bound and free forms of first and second beta-strands** ([`10.1021/bi00008a003`](https://doi.org/10.1021/bi00008a003), sample `S1`): Asp-7-Cys-8 and Cys-21-Val-25
- **larger-amplitude sub-nanosecond motions (S2 < 0.8)** ([`10.1021/bi00008a003`](https://doi.org/10.1021/bi00008a003), sample `S1`): Asp-7, Cys-8 (N-terminal bend); Leu-48, Leu-49, Ala-50 (C-terminus)

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi00008a003`](https://doi.org/10.1021/bi00008a003) | 229 | 0 | 3 | 3 | Per-residue 15N R1, R2, HNOE (Table 2), final-cycle model-free S2, tau_e, Rex (Table 3, cycle C), and tau_m pe |

**Explicit figure-only, SI-only, or access gaps (3):**

- Cycle A and B (Table 3) fit values of S2, tau_e, Rex per residue ([`10.1021/bi00008a003`](https://doi.org/10.1021/bi00008a003)): deliberately not entered: intermediate cycles superseded by cycle C, the authors' final optimised set (cycle D for Asp-47)
- R2/R1 and R2corr/R1 columns of Table 2 and mean (R2/R1) column of Table 4 ([`10.1021/bi00008a003`](https://doi.org/10.1021/bi00008a003)): ratios derived from R1 and R2 printed in the same table, not independent measurements
- Figure 5-9 plots of R1, R2, HNOE, S2, Rex versus residue ([`10.1021/bi00008a003`](https://doi.org/10.1021/bi00008a003)): figure only

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
