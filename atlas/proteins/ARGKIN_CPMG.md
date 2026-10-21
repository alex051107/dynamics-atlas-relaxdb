# Limulus polyphemus arginine kinase

RelaxDB entry `ARGKIN_CPMG` · set CPMG-10 · Limulus polyphemus arginine kinase, recombinant wild type

## Answer

**Yes: a minor state is measured in the free protein.**

**Strict two-peak reading:** does not. Authors assign intermediate exchange (α 1.1–1.3) to the three L8 residues used for pB; the minor state is seen only through dispersion and no minor-state peaks are reported.

At 25 °C the free enzyme exchanges in four backbone regions. The 2009 collective 15N CPMG fits of the hinge, the NTD–CTD interface and loop L8 give a rate and a minor-state population, with the largest minor state in L8 (2.6 ± 0.6%). For dynamic domain 1 the text reports a collective fit with pB < 0.3% and 'unreasonably large Δω and errors', and the 2011 interface fit is indeterminate. A four-temperature fit and ILV methyl CPMG reproduce an L8 minor state of a few percent.

## The free protein (reference state)

Wild-type substrate-free arginine kinase, 25 °C (also 15–30 °C); pH 6.5, 10 mM sodium citrate, 50 mM KCl, 0.5 mM DTT; no nucleotide or Mg (2009/2011 samples). Methyl sample (2017): 10 mM potassium citrate, 50 mM KCl, pH not stated

| | |
|---|---|
| Where (residues) | NTD hinge D88, H90, G92; NTD–CTD interface D71, F136, N137, F270, C271, N274, G276, G332; dynamic domain 1 and hinge R126, C127, R129, V220, V222, R229, Q234; substrate-binding loop L8 I182–G209 (17 residues in the collective fit); methyls L170, L187, L219, I231, I210, L331 |
| Exchange rate kex | 25 °C collective fits: loop L8 790 ± 60 s-1; NTD hinge 1,930 ± 350 s-1; NTD–CTD interface 800 ± 100 s-1; dynamic domain 1 790 ± 70 s-1 (Table 1) or 990 ± 110 s-1 (text) (ARGKIN-J1–J4, ARGKIN-r1). L8 530 ± 80 to 1,080 ± 150 s-1 from 15 to 30 °C, 860 ± 120 s-1 at 25 °C (the rate paired with the 4.9% L8 population, ARGKIN-r6) (ARGKIN-J9, ARGKIN-r4–r7). L170/L187 methyls 970 ± 38 s-1 (ARGKIN-J10, ARGKIN-r11). |
| Minor-state population pB | L8 2.6 ± 0.6%; hinge 0.4 ± 0.1%; interface 1.1 ± 0.1%; dynamic domain 1 0.4 ± 0.1% (Table 1; text: < 0.3%) (ARGKIN-r1). L8 3.5 ± 0.3% to 5.7 ± 1.6% from 15 to 30 °C, 4.9 ± 0.5% at 25 °C (with kex 860 ± 120 s-1), from E190, D192, T206 only (ARGKIN-r4–r7). L170/L187 methyls 4.8 ± 0.3% (ARGKIN-r11). |
| Exchange regime | Intermediate for L8 residues E190, D192 and T206 at 25 °C (α = 1.15 ± 0.22, 1.33 ± 0.34 and 1.12 ± 0.21), the subset used for pB in the four-temperature fit (ARGKIN-J9, ARGKIN-r4–r7); interface α ill-defined; apo methyls span 'slow, intermediate, and fast' (2017, ARGKIN-r11). Δω: Table 1 (2009) prints per-residue 15N /Δω/ within the collective fits, hinge 3.2–4.4 ppm (D88, H90, G92), interface 0.9–3.8 ppm, dynamic domain 1 1.0–5.6 ppm, loop L8 0.6–2.4 ppm (ARGKIN-r1). |

Fallback statement: May have an alternate conformation differing at loop L8 (I182–G209), the NTD hinge (D88, H90, G92), the NTD–CTD interface and dynamic domain 1, based on 15N TROSY CPMG and ILV methyl CPMG relaxation dispersion (doi:10.1016/j.str.2009.08.014; doi:10.1021/bi101664u; doi:10.1021/jacs.7b00236).

## Matching structures

Deposited-structure comparison: The only apo crystal (3M10) is open (closure 0-0.07); all 12 ligand-bound structures are closed (0.91-1.0). PDBe-KB clustering agrees. Table: [`data/structures/ARGKIN_CPMG.md`](../../data/structures/ARGKIN_CPMG.md).

What the papers relate to the states:

- **1M15**: Transition-state-analogue (closed) crystal structure. Apo solution RDCs and shifts fit a mixture of the 3M10 apo and 1M15 TSA endpoints with an apo fraction of about 0.5 (shifts) to 0.7 (RDCs), and the authors conclude that solution apo enzyme contains substrate-bound-like features. Static-average and dynamic-mixture models give very similar Q-values, so RDCs alone cannot tell them apart; relaxation dispersion gives an apo fraction > 0.97. Separately, the 2009 CPMG paper speculates that the L8 motion may sample the closed-form configuration (ARGKIN-r1).
- **3M10**: Refined apo crystal structure, the open endpoint of the same RDC mixture. The RDC paper's Methods name the deposited model 3M15 once; elsewhere the paper uses 3M10.

## Other conditions (not the reference state)

- 15–30 °C, same buffer: yes. Interface 570 ± 120 to 1,440 ± 310 s-1 (population indeterminate) and L8 530–1,080 s-1 with 3.5–5.7% minor state (ARGKIN-J8, ARGKIN-J9, ARGKIN-r4–r7).
- Michaelis complex analogue (arginine + Mg·AMPPNP), imidazole/Mg buffer: yes. kex 914 ± 15 s-1, excited state 3.10 ± 0.04% with TSA-like methyl shifts (ARGKIN-J17, ARGKIN-r12).
- Transition-state analogue (arginine + Mg·ADP + nitrate): yes. Backbone 2,300–2,750 s-1 with domain 4 pB 1.3 ± 0.1% and domain 5 pB 1.8 ± 0.1% (ARGKIN-J20, ARGKIN-J21, ARGKIN-r15); methyls 4,247 ± 72 s-1 with pB 2.75 ± 0.05%, conditional on an assumed slope (ARGKIN-J18, ARGKIN-r13).
- Product complex analogue (pAIE + Mg·ADP): possible. kex 4,690 ± 119 s-1, no population (ARGKIN-J19, ARGKIN-r14).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| ARGKIN-r1 | [Intrinsic domain and loop dynamics commensurate with catalytic…](https://doi.org/10.1016/j.str.2009.08.014) | nmr_relaxation_dispersion | Intrinsic microsecond–millisecond domain/loop exchange | full_text |
| ARGKIN-r4 | [Rate-Limiting Domain and Loop Motions in Arginine Kinase](https://doi.org/10.1021/bi101664u) | nmr_relaxation_dispersion | Thermally activated intrinsic domain and loop exchange | full_text |
| ARGKIN-r5 | [Rate-Limiting Domain and Loop Motions in Arginine Kinase](https://doi.org/10.1021/bi101664u) | nmr_relaxation_dispersion | Thermally activated intrinsic domain and loop exchange | full_text |
| ARGKIN-r6 | [Rate-Limiting Domain and Loop Motions in Arginine Kinase](https://doi.org/10.1021/bi101664u) | nmr_relaxation_dispersion | Thermally activated intrinsic domain and loop exchange | full_text |
| ARGKIN-r7 | [Rate-Limiting Domain and Loop Motions in Arginine Kinase](https://doi.org/10.1021/bi101664u) | nmr_relaxation_dispersion | Thermally activated intrinsic domain and loop exchange | full_text |
| ARGKIN-r8 | [Arginine Kinase: Joint Crystallographic and NMR RDC Analyses Link…](https://doi.org/10.1016/j.jmb.2010.11.007) | nmr_ensemble_restraints | Orientational averaging consistent with partially closed solution conformations | full_text |
| ARGKIN-r9 | [Arginine Kinase: Joint Crystallographic and NMR RDC Analyses Link…](https://doi.org/10.1016/j.jmb.2010.11.007) | nmr_ensemble_restraints | Orientational averaging consistent with partially closed solution conformations | full_text |
| ARGKIN-r10 | [Arginine Kinase: Joint Crystallographic and NMR RDC Analyses Link…](https://doi.org/10.1016/j.jmb.2010.11.007) | pdb_structure_comparison | Domain closure and beta-sheet flexing | full_text |
| ARGKIN-r11 | [The Michaelis Complex of Arginine Kinase Samples the Transition…](https://doi.org/10.1021/jacs.7b00236) | nmr_relaxation_dispersion | Heterogeneous intrinsic methyl exchange | full_text |
| ARGKIN-r12 | [The Michaelis Complex of Arginine Kinase Samples the Transition…](https://doi.org/10.1021/jacs.7b00236) | nmr_relaxation_dispersion | MCA-to-TSA-like excited-state exchange | full_text |
| ARGKIN-r13 | [The Michaelis Complex of Arginine Kinase Samples the Transition…](https://doi.org/10.1021/jacs.7b00236) | nmr_relaxation_dispersion | TSA-to-MCA/apo-like conformational exchange | full_text |
| ARGKIN-r14 | [The Michaelis Complex of Arginine Kinase Samples the Transition…](https://doi.org/10.1021/jacs.7b00236) | nmr_relaxation_dispersion | Fast microsecond–millisecond exchange with unidentified excited-state structure | full_text |
| ARGKIN-r15 | [Elevated μs-ms timescale backbone dynamics in the transition state…](https://doi.org/10.1016/j.jsb.2017.05.002) | nmr_relaxation_dispersion | Widespread TSA backbone microsecond–millisecond exchange | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `ARGKIN_CPMG`.

## Caveats

The L8 population depends on the residue subset (2.6% from all 17 residues versus 4.9% from three residues at 25 °C). Dynamic domain 1 has two inconsistent fits in the same paper, and its methyls exchange at 3,890 ± 29 s-1 (pB 0.56%), so methyls may report a different process; I210 suggests three or more states. All apo samples were in citrate with no citrate-free control, and bound samples switched to imidazole/Mg, so ligand and buffer change together. The RDC match to 1M15 cannot separate exchange from a static average.

## Open questions

- Loop L8 population at 25 °C, apo (model/subset difference, not a data conflict): the 2009 collective fit of all 17 L8 residues gives pB 2.6 ± 0.6% (r1), while the 2011 fit takes pB from only the three slow-intermediate residues E190, D192, T206 and gives 4.9 ± 0.5% (r6; reused as the apo row of the 2017 JACS Table 1). The kex values agree within error (790 ± 60 versus 860 ± 120 s-1).
- Dynamic domain 1 and hinge, apo 25 °C: Table 1 of the 2009 paper gives kex 790 ± 70 s-1, pB 0.4 ± 0.1%, while its text reports a collective fit of 990 ± 110 s-1 with pB < 0.3% and calls the result semi-quantitative (r1). The apo methyls in the same region (L219, I231) give 3,890 ± 29 s-1, pB 0.56% (r11).
- Number of apo processes: backbone data are fitted as four concerted cluster motions (r1, r4-r7), while the methyl study reports heterogeneous per-site rates and a possible three-state residue (I210), and says methyl timescales are not completely consistent with the backbone (r11).
- TSA complex at 25 °C: backbone groups give 2,300-2,750 s-1 (r15) and methyls 4,247 s-1 (r13); the samples differ in ligand concentrations (60 mM Arg/6 mM ADP versus 100 mM Arg/20 mM ADP) and in KCl/Mg, so probe and sample are confounded.
- Which threshold and data produced the RelaxDB ARGKIN_CPMG labels? The curator note cites Fig. 3 (Rex > 2 SD = 5 s-1, 17 residues, TROSY/anti-TROSY experiment), while the 2009 CPMG Table 1 uses ΔR2eff > 2 s-1 (34 residues), and the 2011 counts vary with temperature (33, 23, 34, 28 residues at 15-30 °C).
- Every apo NMR sample used 10 mM sodium or potassium citrate at pH 6.5 with no citrate-free control, while all bound samples switched to imidazole plus 8-30 mM MgCl2. Should apo exchange be flagged as untested for citrate binding at the anionic substrate sites, and should apo-versus-bound comparisons be treated as buffer-confounded?

Judgments: ARGKIN-J1, ARGKIN-J2, ARGKIN-J3, ARGKIN-J4, ARGKIN-J8, ARGKIN-J9, ARGKIN-J10, ARGKIN-J11, ARGKIN-J12, ARGKIN-J15, ARGKIN-J17, ARGKIN-J18, ARGKIN-J19, ARGKIN-J20, ARGKIN-J21 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
