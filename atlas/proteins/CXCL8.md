# Human interleukin-8 (CXCL8

RelaxDB entry `CXCL8` · set RelaxDB-133 · Human interleukin-8 (CXCL8, UniProt P10145), entry construct CXCL8(1-66), the C-terminally truncated monomer (5WDZ sequence); no BMRB id on the input card

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** cannot tell. Only a slow-limit fit at one residue (V62), no minor peak, rate or population (batch-3 review)

In the free 1-66 monomer at 25 °C only two amides disperse in 15N CPMG at 600 and 800 MHz: K23 (800 MHz only, fast-limit fit) and V62 in the C-terminal helix (slow-limit fit); I10, S14, E63 and all other amides are flat although model-free Rex exceeded 1 s-1 at I10, S14 and E63 (CXCL8-J7, CXCL8-J8). No kex, population, shift difference or minor-state structure is printed.

## The free protein (reference state)

Free CXCL8(1-66) monomer, no receptor peptide or glycosaminoglycan; 100 µM (>99% monomer, KM-D about 20 mM), 25 °C, pH 6.0, 50 mM sodium phosphate, 1 mM sodium azide, 10% 2H2O (2018 relaxation and CPMG sample); a second free sample is in 20 mM HEPES pH 7.3 at 40 and 15 °C (2017)

| | |
|---|---|
| Where (residues) | K23 (beta1 region) and V62 (C-terminal helix) (CXCL8-J7) |
| Exchange rate kex | not reported for the free monomer (CXCL8-J7); CPMG range 33.3-2000 Hz, 60 ms constant time |
| Minor-state population pB | not reported for the free monomer (CXCL8-J7) |
| Exchange regime | V62 slow limit (kex << delta-omega) and K23 fast limit (kex >> delta-omega), each selected by AICc between the two limiting two-state models (CXCL8-J7, CXCL8-r15). No delta omega printed. |

Fallback statement: May have an alternate conformation near V62 in the C-terminal helix and at K23, based on 15N CPMG relaxation dispersion of the free CXCL8(1-66) monomer at 600 and 800 MHz (doi:10.3390/molecules23112825); no rate, population or structure reported.

## Matching structures

## Other conditions (not the reference state)

- Bound to the CXCR1 N-domain peptide 1-29, 25 °C, pH 6.0: yes. T12, Y13, S14, V41, E48, C50 exchange with kex 900-2000 s-1 and a 1-2% minor state of unknown structure (fast-limit fits); F17 is flat and peptide on-off exchange is faster (koff 2400-6500 s-1) (CXCL8-J12, J13, J15).
- Full-length 1-72 WT dimer, 25 °C, pH 7.0 HEPES: possible. H(S/M)QC exchange shifts at R26 and C50 with flat 600 MHz CPMG, placed in the microsecond range by the authors; no rate (CXCL8-J23, J24).
- 1-66 at 900 µM: separate slowly exchanging dimer peaks and raised R2 from self-association, not an alternate monomer state (CXCL8-J9).
- Monomer-biased L25Y/V27R mutant at 1 mM: kex 130 ± 30 s-1 with 7% dimer, self-association (CXCL8-J28).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| CXCL8-r5 | [The dynamics of interleukin-8 and its interaction with human CXC…](https://doi.org/10.1002/pro.2430) | nmr_exchange_broadening | Chemical exchange; author-inferred microsecond mobility | full_text |
| CXCL8-r6 | [The dynamics of interleukin-8 and its interaction with human CXC…](https://doi.org/10.1002/pro.2430) | nmr_relaxation_dispersion | No detectable dispersion in this CPMG window | full_text |
| CXCL8-r7 | [The dynamics of interleukin-8 and its interaction with human CXC…](https://doi.org/10.1002/pro.2430) | nmr_relaxation_dispersion | Concentration-dependent self-association exchange | full_text |
| CXCL8-r8 | [The dynamics of interleukin-8 and its interaction with human CXC…](https://doi.org/10.1002/pro.2430) | nmr_relaxation_dispersion | Concentration-dependent self-association exchange | full_text |
| CXCL8-r13 | [Dynamics-Derived Insights into Complex Formation between the CXCL8…](https://doi.org/10.3390/molecules23112825) | nmr_spin_relaxation | Fast backbone flexibility and anisotropic global tumbling | full_text |
| CXCL8-r15 | [Dynamics-Derived Insights into Complex Formation between the CXCL8…](https://doi.org/10.3390/molecules23112825) | nmr_relaxation_dispersion | Site-selective microsecond–millisecond exchange | full_text |
| CXCL8-r16 | [Dynamics-Derived Insights into Complex Formation between the CXCL8…](https://doi.org/10.3390/molecules23112825) | nmr_relaxation_dispersion | Binding-associated internal conformational exchange | full_text |
| CXCL8-r17 | [Dynamics-Derived Insights into Complex Formation between the CXCL8…](https://doi.org/10.3390/molecules23112825) | nmr_relaxation_dispersion | No detectable F17 dispersion in the measured CPMG window | full_text |
| CXCL8-r19 | [Dynamics-Derived Insights into Complex Formation between the CXCL8…](https://doi.org/10.3390/molecules23112825) | nmr_exchange_broadening | Receptor-peptide association/dissociation exchange | full_text |
| CXCL8-r20 | [Dynamics-Derived Insights into Complex Formation between the CXCL8…](https://doi.org/10.3390/molecules23112825) | nmr_spin_relaxation | Concentration-dependent self-association contribution to R2 | full_text |
| CXCL8-r21 | [Dynamics-Derived Insights into Complex Formation between the CXCL8…](https://doi.org/10.3390/molecules23112825) | nmr_spin_relaxation | Concentration-dependent self-association contribution to R2 | full_text |
| CXCL8-r22 | [Dynamics-Derived Insights into Complex Formation between the CXCL8…](https://doi.org/10.3390/molecules23112825) | nmr_spin_relaxation | Concentration-dependent self-association contribution to R2 | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `CXCL8`.

## Caveats

The call rests on two residues with dispersion and no fitted rate or population in the text; the V62 slow-limit label is a model choice between two limiting fits, not an observed minor peak. All 1-66 CPMG data are in phosphate at one temperature. Monomer-dimer exchange (1-66 at 900 µM, the mutant, the full-length dimer with GAGs) is self-association and is kept out of the call. Second read raised no flags for this case.

## Open questions

- Model-free Rex above 1 s-1 at I10, S14 and E63 (r13) is not confirmed by CPMG on the same sample, which disperses only at K23 and V62 (r15); the authors attribute small Rex to tumbling anisotropy or fitting.
- Full-length dimer: H(S/M)QC shift differences report exchange at R26 and C50 (r5) while 600 MHz CPMG is flat (r6); the authors reconcile this by placing the process in the microsecond range, which no row measures.
- Is the RelaxDB CXCL8 set the 2018 free 1-66 monomer data (100 µM, 25 °C, pH 6.0 phosphate, 600 and 800 MHz; doi:10.3390/molecules23112825)? The input card has no BMRB id.
- Should the single-residue slow-limit CPMG fit at V62 (AICc-selected, no rate or population printed) count as an alternate-APO candidate, or does that need a fitted kex and pB?

Judgments: CXCL8-J7, CXCL8-J8, CXCL8-J9, CXCL8-J12, CXCL8-J13, CXCL8-J15, CXCL8-J23, CXCL8-J24, CXCL8-J28 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
