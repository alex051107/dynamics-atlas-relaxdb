# Escherichia coli CheY

RelaxDB entry `CHEY_CPMG` · set CPMG-10 · Escherichia coli CheY, wild type, unphosphorylated

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** cannot tell. The authors state no regime and report no minor-state peak. Computed from their Table 2 local fits (PMC3552614, 1 mM EDTA, 15 °C): D64 kex 96 ± 16 s-1, Δω 9.4 ± 1 ppm, minor fraction 0.20 and R19 kex 180 ± 30 s-1, Δω 5.7 ± 1 ppm, minor fraction 0.04 give kex/Δω 0.03 and 0.08 at 600 MHz, i.e. slow exchange that predicts a resolved minor peak; none is reported, so either the peak exists unreported or these local fits are unreliable (computed by Claude 2026-10-20 after the night review). All other fitted residues are intermediate or fast (kex/Δω 1.0-12.9).

Without Mg2+, 13 active-site and FliM-face residues show µs–ms exchange, but no population of a defined minor state is reported. Per-residue two-state fits give local rates (96 to 2,440 s-1) and local fractions; group fitting eliminated all residues, and the authors state that CheY 'does not undergo a two-state concerted switch' and favour non-concerted, segmental switching.

## The free protein (reference state)

Wild-type unphosphorylated CheY without Mg2+ (1 mM EDTA), 15 °C; pH 7.0, 50 mM sodium phosphate, 0.02% NaN3; >80% 2H

| | |
|---|---|
| Where (residues) | R18, R19, A36, D38, N62, D64, E67, L68, L69, T87, N94, V107, L127 (Rex > 2 s-1); D13 too broad to fit |
| Exchange rate kex | per-residue local fits, no shared value: 96 ± 16 s-1 (D64) to 2,440 ± 570 s-1 (V107) (CHEY-J1, CHEY-r1) |
| Minor-state population pB | reported as per-residue major fraction pI = 0.67 ± 0.2 (N94) to 0.99 ± 0.01, so local minor fractions 1 − pI = 0.33 ± 0.2 to 0.01 ± 0.01; local fit parameters, not a shared population; N94 is ill-determined (kex 1,330 ± 800 s-1, Δω 0.27 ± 0.1 ppm) (CHEY-J1, CHEY-r1) |
| Exchange regime | not stated by the authors. Table 2 prints per-residue 15N Δω from 0.27 ± 0.1 ppm (N94) to 9.4 ± 1 ppm (D64) at 600/700 MHz alongside local rates of 96 to 2,440 s-1, so no single regime applies; no minor-state peaks are reported (CHEY-r1). |

Fallback statement: May have an alternate conformation differing at the active site and FliM-binding face (R18, R19, A36, D38, N62, D64, E67, L68, L69, T87, N94, V107, L127), based on 15N relaxation-compensated CPMG at 600 and 700 MHz (McDonald 2012, doi:10.1016/j.str.2012.05.008).

## Matching structures

Deposited-structure comparison: No apo crystal has the BeF3-activated backbone. 1CHN and 3RVQ show a flipped β4-α4 loop (not checked against their papers). Table: [`data/structures/CHEY_CPMG.md`](../../data/structures/CHEY_CPMG.md).

What the papers relate to the states:

- **3CHY**: Mg-free wild-type crystal (Volz 1991 abstract: three sulfate ions, seven side chains in dual conformations; CHEY-r19). McDonald 2012 describes Y106 'out' and 'in' rotamers in this structure, cites the populated 'in' rotamer as support for rapid Y106 switching, and notes M85 in two conformations (CHEY-r1); the crystal gives no rate or population. A 1.08 Å apo structure (PDB ID not given in the rows) shows two β4–α4 loop conformations correlated with the Y106 rotamers, one interpreted as meta-active (CHEY-r27).

## Other conditions (not the reference state)

- 10 mM Mg2+ (about 86% Mg-bound), 15 °C: possible by the same logic; the authors state CheY does not switch in a concerted two-state way 'whether Mg2+ is present or absent'. 11 residues, kex 246 ± 31 to 3,620 ± 460 s-1, pI 0.91–0.99 (CHEY-J4, CHEY-r2); A88 may carry a second, faster process (CHEY-J5).
- 1 mM and 75 mM Mg2+: two-point Rex only; V107 Rex about 28 s-1 at 1 mM, no rate (CHEY-J8, CHEY-r3, CHEY-r4).
- BeFx + Mg2+ (phosphorylation mimic): possible. Small residual exchange redistributed toward the FliM interface, too few residues for rate fits (CHEY-J9, CHEY-r7).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| CHEY-r1 | [Segmental Motions, Not a Two-State Concerted Switch, Underlie…](https://doi.org/10.1016/j.str.2012.05.008) | nmr_relaxation_dispersion | Residue-local microsecond–millisecond conformational exchange | full_text |
| CHEY-r2 | [Segmental Motions, Not a Two-State Concerted Switch, Underlie…](https://doi.org/10.1016/j.str.2012.05.008) | nmr_relaxation_dispersion | Residue-local microsecond–millisecond conformational exchange | full_text |
| CHEY-r3 | [Segmental Motions, Not a Two-State Concerted Switch, Underlie…](https://doi.org/10.1016/j.str.2012.05.008) | nmr_relaxation_dispersion | Mg-dependent microsecond–millisecond exchange amplitude | full_text |
| CHEY-r4 | [Segmental Motions, Not a Two-State Concerted Switch, Underlie…](https://doi.org/10.1016/j.str.2012.05.008) | nmr_relaxation_dispersion | Mg-dependent microsecond–millisecond exchange amplitude | full_text |
| CHEY-r5 | [Segmental Motions, Not a Two-State Concerted Switch, Underlie…](https://doi.org/10.1016/j.str.2012.05.008) | nmr_exchange_broadening | Exchange broadening | full_text |
| CHEY-r7 | [Colocalization of Fast and Slow Timescale Dynamics in the Allosteric…](https://doi.org/10.1016/j.jmb.2013.04.029) | nmr_relaxation_dispersion | Residual and redistributed microsecond–millisecond exchange | full_text |
| CHEY-r19 | [Crystal structure of Escherichia coli CheY refined at 1.7-A resolution](https://doi.org/10.1016/s0021-9258(18)98646-1) | xray_multitemp_ensemble | Qualitative alternate-state or dynamics evidence | abstract_only |
| CHEY-r27 | [A Distinct Meta-active Conformation in the 1.1-Å Resolution…](https://doi.org/10.1074/jbc.c100295200) | xray_multitemp_ensemble | Qualitative alternate-state or dynamics evidence | abstract_only |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `CHEY_CPMG`.

## Caveats

The call is possible, not yes, because the data give per-residue local populations only and the authors argue against a single concerted inactive-active switch; linear shift trajectories across T87I, WT, A113P and BeFx states, which fit a two-state shift, are stated for Y106, V107 and E89 only. All NMR samples were in 50 mM sodium phosphate with no phosphate-free control, and the Mg-free crystal 3CHY has a sulfate next to N59 and K109 in the phosphorylation pocket.

## Open questions

- Exchange model for the same CPMG data (r1, r2): the authors' per-residue local fits, failed group fits and poor Δω-Δδ correlation argue against a concerted two-state inactive-active switch, while the linear chemical-shift trajectories of E89, Y106 and V107 (and nearly M85, A97, A98) across T87I, WT, A113P and BeFx states fit a classic two-state equilibrium shift; the authors reconcile them as segmental local switching.
- Two-state versus three-state at 10 mM Mg2+ (r2 source text): an F-test favours a three-state model for A36, T87 and E89, but the three-state fits were not robust and group three-state fitting gave no improvement; in EDTA no residue improved.
- Mg2+ effect on structure: the Mg-bound E. coli crystal shows displacements up to 10 Å at the α4 N terminus and preceding loop (r21), while McDonald 2012 solution chemical-shift perturbations on Mg2+ addition are small in the allosteric region (cited in r1/r2 paper).
- Residual exchange in BeFx-activated CheY (r7): authors leave open whether it is local return to the inactive state, motion among several active-like states, or motions slowed into the CPMG window.
- The RelaxDB source lead names Table 2 (Rex labels) and Figure 2 (missing-peak labels), i.e. the Mg-free 1 mM EDTA sample; the text names only D13 as too broad there, and Figure 2A marks too-broad residues only in the image. Which residues carry the missing-peak label, and should the 10 mM Mg2+ Table 1 set be kept out of the labels?
- All CPMG and relaxation samples used 50 mM sodium phosphate pH 7.0 with no phosphate-free control, and the Mg-free crystal 3CHY has a sulfate next to N59/K109 in the phosphorylation pocket; do you know of a buffer comparison for CheY, or should the active-site exchange (D13, D38, N62, D64) be flagged as untested for anion binding?

Judgments: CHEY-J1, CHEY-J2, CHEY-J3, CHEY-J4, CHEY-J5, CHEY-J8, CHEY-J9, CHEY-J18 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
