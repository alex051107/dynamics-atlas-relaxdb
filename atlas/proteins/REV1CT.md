# Human REV1 C-terminal domain (Rev1-CT

RelaxDB entry `REV1CT` · set RelaxDB-133 · Human REV1 C-terminal domain (Rev1-CT, 1157–1251, G1157 remnant after TEV cleavage)

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** cannot tell. No regime is stated for the free domain and no apo Δω is printed; F1165 and S1223 are broadened beyond detection, and no second peak set is reported.

15N CPMG at 11.7 T shows millisecond exchange at the RIR-binding pocket, with dispersion at G1161, L1171, W1175 and D1186, and model-free Rex in the H1–H2 and H3–H4 loops. No apo rate or population was fitted. The only fitted rate and population come from the 89%-bound pol η RIR complex and may include peptide on–off exchange.

## The free protein (reference state)

Free wild-type Rev1-CT, no peptide, 15 °C, pH 7.0, 50 mM NaH2PO4, 100 mM NaCl, 0.25 mM EDTA, 5 mM DTT, 0.9 mM 15N/13C; 11.7 T

| | |
|---|---|
| Where (residues) | RIR-binding pocket: G1161, L1171, W1175, D1186 (entry 5, 15, 19, 30), author-listed examples; the figure-only exchange map (Fig. 5C) also marks the β-hairpin, the last two turns of H1, the H1–H2 loop and the first two turns of H2 (REV1CT-J3). F1165 and S1223 not detected (REV1CT-J4). |
| Exchange rate kex | not fitted for the free domain (REV1CT-J3, REV1CT-r2) |
| Minor-state population pB | not fitted for the free domain (REV1CT-J3); 5.9 ± 0.4% only in the pol η RIR complex (REV1CT-J7, REV1CT-r5) |
| Exchange regime | Not stated. Dispersion plateaus near 500 Hz at the example residues (REV1CT-J3); the 500 Hz CPMG R2 used for model-free Rex suppresses slow exchange, so that Rex reports the faster part of the exchange (buffer note). |

Fallback statement: May have an alternate conformation at the pol η RIR-binding pocket (β-hairpin, helices H1 and H2), based on 15N CPMG relaxation dispersion and model-free Rex of the free domain (doi:10.1021/bi300566z).

## Matching structures

## Other conditions (not the reference state)

- Pol η RIR complex, about 89% bound, 15 °C: possible. Two-field global fit kex 585 ± 23 s-1, pB 5.9 ± 0.4%, which mixes peptide binding with possible intramolecular exchange (about twice the 300 s-1 on–off upper bound; Δω mostly matches free–bound differences) (REV1CT-J7, REV1CT-r5); model-free Rex at 1175–1179 (REV1CT-J6, REV1CT-r4); F1165, S1223 and V1224 missing (REV1CT-J8, REV1CT-r6).
- Half-saturated pol η RIR titration: separate free and bound L1171 peaks; binding kinetics with kon[L] and koff below about 33 s-1, not conformational exchange (REV1CT-J9, REV1CT-r7).
- PolD3 and fluorinated XRCC1 RIR peptides: slow free/bound exchange, no rate, binding only (REV1CT-J10, REV1CT-r9; REV1CT-J11, REV1CT-r17).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| REV1CT-r1 | [NMR structure and dynamics of the C-terminal domain from human Rev1…](https://doi.org/10.1021/bi300566z) | nmr_spin_relaxation | Restricted backbone ps–ns mobility with flexible C terminus and H3–H4 loop; faster μs–ms Rex contributions | full_text |
| REV1CT-r2 | [NMR structure and dynamics of the C-terminal domain from human Rev1…](https://doi.org/10.1021/bi300566z) | nmr_relaxation_dispersion | μs–ms conformational exchange at the RIR-binding interface | full_text |
| REV1CT-r3 | [NMR structure and dynamics of the C-terminal domain from human Rev1…](https://doi.org/10.1021/bi300566z) | nmr_exchange_broadening | Presumed μs–ms exchange broadening | full_text |
| REV1CT-r4 | [NMR structure and dynamics of the C-terminal domain from human Rev1…](https://doi.org/10.1021/bi300566z) | nmr_spin_relaxation | Restricted backbone ps–ns mobility with flexible C terminus and H3–H4 loop; faster μs–ms Rex contributions | full_text |
| REV1CT-r5 | [NMR structure and dynamics of the C-terminal domain from human Rev1…](https://doi.org/10.1021/bi300566z) | nmr_relaxation_dispersion | μs–ms conformational exchange at the RIR-binding interface | full_text |
| REV1CT-r6 | [NMR structure and dynamics of the C-terminal domain from human Rev1…](https://doi.org/10.1021/bi300566z) | nmr_exchange_broadening | Presumed μs–ms exchange broadening | full_text |
| REV1CT-r7 | [NMR structure and dynamics of the C-terminal domain from human Rev1…](https://doi.org/10.1021/bi300566z) | nmr_exchange_broadening | Slow-on-chemical-shift-scale binding exchange | full_text |
| REV1CT-r8 | [NMR structure and dynamics of the C-terminal domain from human Rev1…](https://doi.org/10.1021/bi300566z) | pdb_structure_comparison | Comparison of mean structures; no kinetic window | full_text |
| REV1CT-r9 | [Interaction between the Rev1 C-Terminal Domain and the PolD3 Subunit…](https://doi.org/10.1021/acs.biochem.5b01282) | nmr_exchange_broadening | Binding exchange slow relative to chemical-shift separation | full_text |
| REV1CT-r17 | [XRCC1 interaction with the REV1 C-terminal domain suggests a role in…](https://doi.org/10.1016/j.dnarep.2013.08.015) | nmr_exchange_broadening | Slow free/bound ligand exchange | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `REV1CT`.

## Caveats

The apo dispersion is single-field and its full residue map is figure-only. No structure is matched: the free (2LSY) and pol η-bound (2LSK) NMR structures show a preformed pocket and an unchanged bundle, which says nothing about an apo minor state (REV1CT-J12, REV1CT-r8). The RelaxDB REV1CT sample is unidentified (no BMRB id in the input).

## Open questions

- Pol eta RIR complex: the fitted kex of 585 s-1 is about twice the authors' 300 s-1 upper bound for on-off exchange, yet the dispersion Δω mostly matches free-bound shift differences (r5); the rows cannot split binding from intramolecular exchange.
- The Rev7-complex paper gives the tail as 1246-1251 but its NOE text names K1259, beyond the 1251 C-terminus (r14, r16); kept unmapped.
- Is the RelaxDB REV1CT R1/R2/NOE set the 15 °C, 11.7 T free-domain data of the 2LSY/2LSK paper (r1)? The input lists no BMRB id.
- Should the free-domain us-ms answer rest on 11.7 T dispersion examples without a fitted apo kex, or wait for the full figure-only exchange map (Fig. 5C)?

Judgments: REV1CT-J3, REV1CT-J4, REV1CT-J6, REV1CT-J7, REV1CT-J8, REV1CT-J9, REV1CT-J10, REV1CT-J11, REV1CT-J12 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
