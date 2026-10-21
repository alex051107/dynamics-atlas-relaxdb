# Human biliverdin IX-beta reductase (BLVRB)

RelaxDB entry `BLVRB_CPMG` · set CPMG-10 · Human biliverdin IX-beta reductase (BLVRB), wild type

## Answer

**Yes: a minor state is measured in the free protein.**

**Strict two-peak reading:** does not. Authors: exchange on the fast NMR timescale for the fittable residues; the minor state is seen only through dispersion and no second peak set is reported.

Apo BLVRB shows µs–ms exchange at more than 30 residues around the three active-site loops and in the C-terminal lobe; the authors call the exchange fast for the residues they could fit (e.g. S111, L125). The 2023 grouped multi-temperature (0–20 °C, Arrhenius-constrained) fits give a rate and a minor-state population for two residue groups (about 2.2% and 1.2% at 20 °C), although the 2018 analysis found the population not separable in that regime and the 2023 authors call two-site fits 'an over-simplification'.

## The free protein (reference state)

Wild-type apo human BLVRB, 20 °C (also 10, 5, 0 °C); pH 6.5, 50 mM Bis-Tris, 50 mM NaCl, 1 mM DTT; refolded, coenzyme removed by reverse-phase chromatography (Resource 15RPC, 2018 methods; the step is not stated for the 2023 samples)

| | |
|---|---|
| Where (residues) | Active-site loops 10–15, 76–82 and 109–114 (more than 30 residues at 20 °C); Group II L74, T77, C109, S111, Q126; Group III I154, G155, T164, I176, Y205 |
| Exchange rate kex | Group II 1,088 ± 180 s-1 and Group III 3,797 ± 800 s-1 at 20 °C, slowing to 181 ± 66 and 850 ± 178 s-1 at 0 °C (BLVRB-J3, BLVRB-J4, BLVRB-r15–r18); per-residue S111 1,200 ± 300 s-1 and L125 2,200 ± 540 s-1 at 20 °C (BLVRB-J1, BLVRB-r1) |
| Minor-state population pB | reported as pA: 2023 Table 2 prints major fractions 97.8 ± 0.2% (Group II) and 98.8 ± 0.1% (Group III) at 20 °C, so pB = 2.2 ± 0.2% and 1.2 ± 0.1%; at 0 °C reported as pA = 95.5 ± 1.5% and 97.8 ± 0.3%, so pB = 4.5 ± 1.5% and 2.2 ± 0.3% (the 0 °C Group II cell prints no unit) (BLVRB-r15, BLVRB-r18); not separable in the 2018 fast-exchange fits (BLVRB-r1) |
| Exchange regime | fast NMR timescale for the residues that could be fit to the Carver–Richards equations (2018), with populations that 'cannot be accurately deconvoluted under such an exchange regime' (BLVRB-J1, BLVRB-r1). Δω: the 2024 per-residue refit prints ΔωN from 0.54 ± 0.11 ppm (D80) to 9.49 ± 0.96 ppm (G76) (SI Table S1, BLVRB-r38). |

Fallback statement: May have an alternate conformation differing at the active-site loops (residues 10–15, 76–82, 109–114) and the C-terminal lobe (I154, G155, T164, I176, Y205), based on 15N TROSY CPMG relaxation dispersion at 0–20 °C (doi:10.1016/j.jmb.2018.06.015; doi:10.3389/fmolb.2023.1244587).

## Matching structures

Deposited-structure comparison: Apo and NADP+-bound backbones differ by less than 1 Å; the literature contrast is in side chains. The 7ER series differs at residues 36-45 (not checked against its paper). Table: [`data/structures/BLVRB_CPMG.md`](../../data/structures/BLVRB_CPMG.md).

What the papers relate to the states:

- **1HDO**: NADP+-bound (holo) crystal. The authors report that apo and holo crystals differ at R35, R39 and the R78 clamp. Separately, apo CPMG shift differences show 'at least several weak correlations' with apo-to-holo CSPs (2023), so the apo enzyme may sample holo-like states; I176 and Y205, both in this row's residue list, do not. The holo-like reading comes from shifts, not from 1HDO coordinates; not a solved minor state.

## Other conditions (not the reference state)

- NADP+-bound, 20 °C: possible. Exchange quenched in the apo-exchanging loops except S111 and T164, and new exchange at D36, S37, R39, with no rate or population (BLVRB-J16, BLVRB-J17, BLVRB-r2).
- NADPH- or NADP+-bound, 0–10 °C: yes. Grouped fits give rates and 1–5% minor states for Groups I–III, with population errors as large as the minor fraction for some NADPH groups (BLVRB-J19–J24).
- NADP+ + bilirubin (commercial isomer mixture), 0–10 °C: Group II no_evidence; Groups I and III exchange (BLVRB-J25–J27).
- Mutants R78A, T164A, T164I, T164S, S111A: exchange changes but persists (BLVRB-J33, BLVRB-J35–J39).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| BLVRB-r1 | [Biliverdin Reductase B Dynamics Are Coupled to Coenzyme Binding](https://doi.org/10.1016/j.jmb.2018.06.015) | nmr_relaxation_dispersion | μs–ms conformational exchange | full_text |
| BLVRB-r2 | [Biliverdin Reductase B Dynamics Are Coupled to Coenzyme Binding](https://doi.org/10.1016/j.jmb.2018.06.015) | nmr_relaxation_dispersion | μs–ms exchange redistributed upon binding | full_text |
| BLVRB-r15 | [Identifying structural and dynamic changes during the Biliverdin…](https://doi.org/10.3389/fmolb.2023.1244587) | nmr_relaxation_dispersion | μs–ms exchange; different groups and ligand states | full_text |
| BLVRB-r16 | [Identifying structural and dynamic changes during the Biliverdin…](https://doi.org/10.3389/fmolb.2023.1244587) | nmr_relaxation_dispersion | μs–ms exchange; different groups and ligand states | full_text |
| BLVRB-r17 | [Identifying structural and dynamic changes during the Biliverdin…](https://doi.org/10.3389/fmolb.2023.1244587) | nmr_relaxation_dispersion | μs–ms exchange; different groups and ligand states | full_text |
| BLVRB-r18 | [Identifying structural and dynamic changes during the Biliverdin…](https://doi.org/10.3389/fmolb.2023.1244587) | nmr_relaxation_dispersion | μs–ms exchange; different groups and ligand states | full_text |
| BLVRB-r37 | [Identifying structural and dynamic changes during the Biliverdin…](https://doi.org/10.3389/fmolb.2023.1244587) | pdb_structure_comparison | ligand-dependent alternative structural arrangements | full_text |
| BLVRB-r38 | [Evolutionary Adaptations in Biliverdin Reductase B: Insights into…](https://doi.org/10.3390/ijms252413233) | nmr_relaxation_dispersion | μs–ms conformational exchange | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `BLVRB_CPMG`.

## Caveats

The population is model-dependent: not separable (2018 per-residue fits), about 1-2% (2023 grouped Arrhenius fits), or poorly determined in the 2024 per-residue refit, whose SI Table S1 prints pA from 50% to 99.8% with errors up to about ±22% and several values at exactly 50%, possibly a fit bound (our reading; BLVRB-r38). Without the reverse-phase step 1-3% of the enzyme stayed coenzyme-bound (authors, data not shown); that this fraction is similar in size to the fitted apo minor states is our inference. Rates in the 2023 and 2024 tables are printed in 'Hz' and are carried as s-1 without conversion.

## Open questions

- Apo exchange model at 20 °C (same human data or same lab): per-residue Carver-Richards fits with populations declared inseparable (2018, r1: S111 1,200 ± 300, L125 2,200 ± 540 s-1) versus a per-residue GUARDD refit at 600/900 MHz (2024 SI Table S1, r38: S111 1,420 ± 100, L125 2,670 ± 500, T164 8,070 ± 3,600 s-1, populations degenerate near 50 ± 20%) versus grouped two-site Arrhenius fits (2023 Table 2, r15: Group II 1,088 ± 180, Group III 3,797 ± 800 with 97.8% and 98.8% major states) versus the 2021 global fit of 125-127/H132/K178/Y205 (2,020 ± 230 s-1, SI Table S4, no evidence row). All agree exchange exists; they disagree on whether it is one, two or many processes and whether the population is measurable.
- Human T164S distal effect: 2021 reports lower dispersion amplitudes for residues 125-127, H132, K178, Y205 (r12), while 2024 states that both position-164 swaps induce higher dispersion at distant residues or no effect (r39); both are apo, 20 °C, 900 MHz.
- T164 in WT apo: 2018 describes a linear dispersion not suppressed at the highest νCPMG, with no fit (r1), whereas 2023 places T164 in Group III with 3,797 ± 800 and 2024 fits 8,070 ± 3,600; different models for a dispersion that may not reach its plateau.
- The RelaxDB BLVRB_CPMG curator note says the data are private EZE data with Rex labels from R2(50 Hz) - mean(R2 at 900 and 1000 Hz) > 2 and assignments from BMRB 27462 (apo). Is this the 2018 apo WT 20 °C, 900 MHz TROSY CPMG set (Paukovich 2018), and is the 20 °C apo set in the 2023 Table 2 fit the same recording or a new one?
- For the apo minor state, should the atlas carry the 2023 grouped populations (about 1-2% at 20 °C), or leave pB undetermined as the 2018 two-field analysis concluded for fast exchange (the 2024 per-residue refit returns PA near 50 ± 20% for many residues)?

Judgments: BLVRB-J1, BLVRB-J2, BLVRB-J3, BLVRB-J4, BLVRB-J14, BLVRB-J16, BLVRB-J17, BLVRB-J19, BLVRB-J20, BLVRB-J21, BLVRB-J22, BLVRB-J23, BLVRB-J24, BLVRB-J25, BLVRB-J26, BLVRB-J27, BLVRB-J33, BLVRB-J35, BLVRB-J36, BLVRB-J37, BLVRB-J38, BLVRB-J39 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
