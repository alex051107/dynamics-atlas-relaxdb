# Bovine pancreatic ribonuclease A (RNase A)

RelaxDB entry `RNASE_CPMG` · set CPMG-10 · Bovine pancreatic ribonuclease A (RNase A), wild type

## Answer

**Yes: a minor state is measured in the free protein.**

**Strict two-peak reading:** does not. Global and cluster motions are fast (buffer study: 'nearly all ... in the fast limit'); only R33 is slow, and 'no minor peak could be detected'.

Free RNase A shows µs–ms exchange that one global two-state fit per temperature describes, with a 90–93% major state. Later cluster fits split it into a loop 1/β1/β4 network around His48, loop 4 near His119, and Arg33 as a separate process, each with its own rate and population.

## The free protein (reference state)

Wild-type free RNase A, 293 K (RelaxDB label condition; also 283 and 298 K). Beach 2005: pH 6.3, 20 mM perdeuterated MES, 10 mM NaCl, 600 µM. Cluster fits (Khirich 2015): 5 mM MES, 7 mM NaCl, pH 6.4. Buffer-study reference: 5 mM MES, 400 µM.

| | |
|---|---|
| Where (residues) | Global fit at 293 K: Q11, S15, S16, T17, N44, F46, A64, K66, N71, D83, T100, Q101, H119 (43 residues pass the Rex screen); His48 cluster S15, S16, T17, F46, T82, D83, Q101; loop 4 A64, K66, T70, N71; R33 |
| Exchange rate kex | global 1,080 ± 80 / 1,390 ± 70 / 1,750 ± 130 s-1 at 283 / 293 / 298 K (RNASE-J1, RNASE-r1–r3); His48 cluster 2,650 s-1 at 25 °C, pH 6.4 (RNASE-J5, RNASE-r18); loop 4 1,610 s-1 at 25 °C, pooled pH 5.5–7.0 (RNASE-J6, RNASE-r19); R33 1,215 s-1 at 25 °C (RNASE-J7, RNASE-r68) |
| Minor-state population pB | reported as pA, so pB = 1 − pA: global fits pA 90–93% across 283–298 K (pB 7–10%), which Beach says reflects 'uncertainty in fitting for pa' (RNASE-J1); His48 cluster reported as pA = 92.5 ± 0.7% at pH 6.4 (pB 7.5 ± 0.7%; the ± is the spread of an average over temperature) (RNASE-J5); loop 4 reported as pA = 95.9 ± 0.9% at 25 °C (pB 4.1 ± 0.9%; the ± is the standard deviation over pH) (RNASE-J6); R33 reported as pA = 99.5% (pB 0.5%) (RNASE-J7, RNASE-r68); pA:pB 0.95:0.05 in the proton-inventory study (RNASE-J3, RNASE-r24) |
| Exchange regime | Beach 2005: no regime stated; the minor resonance is called 'invisible'. Buffer study: dispersion fit with the fast-exchange equation, 'nearly all of the MES-reference motions are in the fast limit' (RNASE-J9, RNASE-r10). Proton-inventory study, WT 298 K: Δω 510 s-1 (F46) and 356 s-1 (T100) with kex 1,657 s-1 (RNASE-J3, RNASE-r24). Cluster R1ρ data were 'assumed to be in fast exchange'; at pH 4.5 the His48 cluster leaves the CPMG window (13,400 s-1 by R1ρ at 25 °C on a deuterated sample, RNASE-J5). Only R33 is called slow: 'slow-exchange characteristics (kex/Δω ~ 0.75 at 500 MHz)', Δω 5.41 ± 0.30 ppm, and 'no minor peak could be detected' (RNASE-J7, RNASE-r68). |

Fallback statement: May have an alternate, ligand-bound-like conformation differing at loop 1/β1/β4 around His48 (S15, S16, T17, F46, T82, D83, Q101) and at loop 4 (A64, K66, T70, N71), based on 15N relaxation-compensated CPMG (Beach 2005, doi:10.1021/ja0514949; cluster fits doi:10.1021/acs.jpcb.5b00212).

## Matching structures

Deposited-structure comparison: Backbone differences follow crystal temperature, not ligand. Loop 1 is flipped in single chains of 8GC9, 8S96, 4MXF and 6XHD (not checked against their papers). Table: [`data/structures/RNASE_CPMG.md`](../../data/structures/RNASE_CPMG.md).

What the papers relate to the states:

- **1U1B**: pTppAp-bound crystal (the authors' own complex). Beach 2005 compares it crystal-to-crystal with apo 7RSA (backbone RMSD 0.69 Å) and describes an equilibrium between 'open and closed enzyme forms'. The minor state's resemblance to the bound form rests on 15N Δω sign agreement (17 of 20 residues); its structure is not determined.
- **7RSA**: Apo crystal structure, the apo comparison structure in the same analysis; 'apo-like/open comparison state' is the entry's gloss.

## Other conditions (not the reference state)

- pTppAp-bound (substrate mimic): yes. kex 1,316 ± 160 to 1,920 ± 250 s-1, major state 90–96% (RNASE-J16, RNASE-r4–r6).
- 5'-AMP or 3'-UMP bound: possible. Exchange reshaped (loop 4 687 ± 41 s-1 with 5'-AMP), no population (RNASE-J17, RNASE-s19, RNASE-s21).
- pH 4.5, 25 °C: the His48 cluster exchanges at 13,400 s-1 by R1rho on a deuterated sample, fitted assuming fast exchange, too fast for CPMG; loop 4 still disperses at 2,080 ± 340 s-1 (RNASE-J5, RNASE-J6, RNASE-r15, RNASE-r16).
- Heavy water: the His48 group slows (isotope effect 2.2 ± 0.3), loop 4 does not (RNASE-J3, RNASE-J4).
- 100 mM phosphate, 80 mM sulfate or 100 mM acetate: artefact suspected; anions change residue-specific dispersion (RNASE-J19).
- His48-network mutants: T17A and H48C-4MI keep exchange; H48C, H48G, T82A and the loop-1 chimera lose it there (RNASE-J23).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| RNASE-r1 | [Conservation of μs−ms Enzyme Motions in the Apo- and…](https://doi.org/10.1021/ja0514949) | nmr_relaxation_dispersion | microsecond–millisecond conformational exchange | full_text |
| RNASE-r2 | [Conservation of μs−ms Enzyme Motions in the Apo- and…](https://doi.org/10.1021/ja0514949) | nmr_relaxation_dispersion | microsecond–millisecond conformational exchange | full_text |
| RNASE-r3 | [Conservation of μs−ms Enzyme Motions in the Apo- and…](https://doi.org/10.1021/ja0514949) | nmr_relaxation_dispersion | microsecond–millisecond conformational exchange | full_text |
| RNASE-r4 | [Conservation of μs−ms Enzyme Motions in the Apo- and…](https://doi.org/10.1021/ja0514949) | nmr_relaxation_dispersion | microsecond–millisecond conformational exchange | full_text |
| RNASE-r5 | [Conservation of μs−ms Enzyme Motions in the Apo- and…](https://doi.org/10.1021/ja0514949) | nmr_relaxation_dispersion | microsecond–millisecond conformational exchange | full_text |
| RNASE-r6 | [Conservation of μs−ms Enzyme Motions in the Apo- and…](https://doi.org/10.1021/ja0514949) | nmr_relaxation_dispersion | microsecond–millisecond conformational exchange | full_text |
| RNASE-r9 | [Conservation of μs−ms Enzyme Motions in the Apo- and…](https://doi.org/10.1021/ja0514949) | pdb_structure_comparison | ligand-associated structural alternatives | full_text |
| RNASE-r10 | [What’s in Your Buffer? Solute Altered Millisecond Motions Detected…](https://doi.org/10.1021/bi400973e) | nmr_relaxation_dispersion | solute-dependent millisecond exchange | full_text |
| RNASE-r15 | [Complexity of Protein Energy Landscapes Studied by Solution NMR…](https://doi.org/10.1021/acs.jpcb.5b00212) | nmr_relaxation_dispersion | cluster-specific conformational exchange | full_text |
| RNASE-r16 | [Complexity of Protein Energy Landscapes Studied by Solution NMR…](https://doi.org/10.1021/acs.jpcb.5b00212) | nmr_relaxation_dispersion | cluster-specific conformational exchange | full_text |
| RNASE-r18 | [Complexity of Protein Energy Landscapes Studied by Solution NMR…](https://doi.org/10.1021/acs.jpcb.5b00212) | nmr_relaxation_dispersion | cluster-specific millisecond exchange | full_text |
| RNASE-r19 | [Complexity of Protein Energy Landscapes Studied by Solution NMR…](https://doi.org/10.1021/acs.jpcb.5b00212) | nmr_relaxation_dispersion | cluster-specific millisecond exchange | full_text |
| RNASE-r24 | [The mechanism of rate-limiting motions in enzyme function](https://doi.org/10.1073/pnas.0702551104) | nmr_relaxation_dispersion | hydrogen-bond-coupled conformational exchange | full_text |
| RNASE-r68 | [Complexity of Protein Energy Landscapes Studied by Solution NMR…](https://doi.org/10.1021/acs.jpcb.5b00212) | nmr_relaxation_dispersion | distinct R33 conformational exchange | full_text |
| RNASE-s1 | [Characterization of the Transition State of Functional Enzyme Dynamics](https://doi.org/10.1021/ja061435a) | nmr_relaxation_dispersion | global millisecond conformational exchange of loops and active-site residues; collective process shared by all exchanging residues | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `RNASE_CPMG`.

## Caveats

Whether this is one collective motion or several (His48 network, loop 4, R33) is disputed between papers, and 'cluster 1' means different regions in different papers. Free-WT samples were in MES (later also 1% DSS); the only buffer control is a stated, unshown MES-versus-unbuffered comparison. Of the 43 residues behind the RelaxDB labels, only 13 entered the 293 K global fit.

## Open questions

- Number of processes: Beach 2005 (r1-r3), Cole 2002 (r47) and Kovrigin 2006 (s1-s4, 'identical behavior is observed for all exchanging residues') fit one global process, while Watt 2007 (r24-r27) finds an isotope-sensitive His48 network and an isotope-insensitive loop 4 region, and JPCB 2015 (r14-r19, r68) separates cluster 1, cluster 2 and R33 with different pH and temperature dependence. All agree exchange exists; they disagree on whether it is one collective motion.
- Cluster labels are reversed between papers: 'cluster 1' is the loop 1/His48 network in Watt 2007, Doucet 2011 and JPCB 2015, but loop 4 in Gagne 2015 (s17-s22). Rows cannot be pooled by cluster number.
- Anion samples: whether the dispersion changes in phosphate, sulfate and acetate (J19) are altered intramolecular motion or free/anion-bound exchange is unresolved by the authors themselves.
- The RelaxDB curator note says the labels are residues with Rex > 3 Hz at 20 °C in 500 or 600 MHz data, recreating Beach 2005 Fig. 4B (43 residues, membership shown only in the figure), but only 13 of them entered the 1,390 s-1 global fit (r2). Should the atlas treat all 43 threshold residues as exchange-positive, and which label set is current (Hugging Face and the metadata sheet differ at 4 RNase positions; accession P61824 vs bovine P61823)?
- Every free-WT CPMG sample in the rows is in 5-20 mM MES with 7-10 mM NaCl (the 2013-2015 samples also carry 1% w/v DSS, a sulfonate), and the only control, MES versus unbuffered at pH 6.4, is stated as 'identical ms motions' without data. Is that enough to treat MES/DSS as inert for RNase A, given that phosphate, sulfate and acetate visibly change the dispersion?

Judgments: RNASE-J1, RNASE-J3, RNASE-J4, RNASE-J5, RNASE-J6, RNASE-J7, RNASE-J9, RNASE-J16, RNASE-J17, RNASE-J19, RNASE-J23 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
