# Human transforming growth factor alpha

RelaxDB entry `HTGFA` · set RelaxDB-133 · Human transforming growth factor alpha, mature 50-residue domain (V1-A50, UniProt P01135)

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** does not. The source states that the exchange broadening reflects interconversion between multiple protein conformations on the intermediate 15N chemical-exchange (microsecond) timescale, with an author-derived lifetime between about 1.25 µs and 2.5 ms; no kex or Δω is printed (the bounds assume two equal populations and a maximum 10 ppm shift difference), so no regime can be computed, and no second peak set is reported for the free ligand (HTGFA-J12; E-r2). The title's 'slow conformational exchange' means slower than molecular tumbling. The only other stated regime, fast exchange, concerns EGFR-ED binding (HTGFA-J7).

Reference state: in the RelaxDB source sample (free hTGF-alpha, pH 7.1, 30 °C, 500 MHz) 23 of 36 analysed backbone amides carry single-field exchange broadening above 0.5 Hz (D7-C8, T13-H18, T20-K29, C32-V33, V39-G40, E44-H45; fourteen above 1.5 Hz, largest R22 4.93 ± 0.74 s-1), concentrated at the interface between the N- and C-terminal subdomains and in the first-strand region; the authors read this as interconversion between multiple backbone conformations with a lifetime between about 1.25 µs and 2.5 ms and propose first-strand dissociation from the core sheet, inter-subdomain hinge bending and/or disulfide isomerisation, without resolving their contributions; a BPTI control showed little broadening except near its disulfide (HTGFA-J12, E-r2). Under the single-field Rex rule of 2026-10-20 this is exchange detected in the reference state without a population, so the call is 'possible'. No fitted rate, population, shift difference, dispersion series or second peak set exists; the authors say CPMG field-strength measurements were in progress. Fast motion is confined to the C-terminal tail and the N-terminal bend (HTGFA-J11, J13), and the C8-F15 loop disorder of the NMR ensemble is attributed partly to exchange broadening (HTGFA-J15). The other free-ligand evidence is abstract-level: flexible termini, a pH-dependent interconversion with no rate or regime, and partial disorder at pH 3.5 and 30 °C, a different sample state from pH 6.5.

## The free protein (reference state)

Entry construct as deposited (mature human TGF-alpha V1-A50), free, no ligand; the RelaxDB source sample (doi:10.1021/bi00008a003, full text): 2 mM 15N protein dissolved directly in 90% H2O/10% D2O with 1 mM NaN3, no buffer stated, pH 7.1 ± 0.1, 30 ± 0.5 °C, 500 MHz, single field (HTGFA-J11 to J15 marked is_wt_apo).

| | |
|---|---|
| Where (residues) | Rex > 0.5 Hz: D7, C8, T13, F15, C16, F17, H18, T20, C21, R22, F23, L24, V25, Q26, E27, D28, K29, C32, V33, V39, G40, E44, H45 (Q14 unfitted; S36, C43 below threshold; D47 term rejected); > 1.5 Hz at D7, T13, F15, C16, C21, R22, F23, L24, V25, K29, C32, V33, V39, G40 (Table 3, cycle C; largest R22 4.93, V39 3.81, C21 3.50 s-1); interface residues F15-H18, C32-V33, V39-G40, E44-H45 (HTGFA-J12). Fast motion: L48-A50, D7-C8, F17-H18, E27-D28, V39-G40, F23, A31 (HTGFA-J11). |
| Exchange rate kex | not fitted: single-field Rex > 0.5 Hz at 23 amides (uncertainties about ±0.3-0.5 Hz); author bounds on the exchange lifetime of about 1.25 µs (from a 10 ppm maximum 15N shift difference and a 0.5 Hz detection limit) to about 2.5 ms (from non-refocusing at CPMG 2tau = 720 µs), assuming two equally populated states (HTGFA-J12) |
| Minor-state population pB | not measured; two equally populated states are an assumption of the lifetime bounds, and the '40%' or 'about half' figure is the fraction of amides with exchange broadening, not a population (HTGFA-J12) |
| Exchange regime | Authors: intermediate 15N chemical-exchange (microsecond) timescale; lifetime bounded between about 1.25 µs and 2.5 ms; no kex or Δω printed, so no computed regime (HTGFA-J12). Not stated for the pH-dependent interconversion (HTGFA-J2, HTGFA-J3). EGFR-ED binding is in the fast-exchange limit (HTGFA-J7, binding kinetics). |

Fallback statement: May have alternate backbone conformations involving the interface between the N- and C-terminal subdomains (F15-H18, C32-V33, V39-G40, E44-H45) and the first beta-strand region (D7-C8, C21-V25): single-field 15N exchange broadening above 0.5 Hz at 23 amides of free TGF-alpha at pH 7.1, 30 °C, lifetime between about 1.25 µs and 2.5 ms, candidate mechanisms first-strand dissociation, subdomain hinge bending or disulfide isomerisation (doi:10.1021/bi00008a003); no rate or population; the pH-dependent interconversion is known only from an abstract (doi:10.1111/j.1432-1033.1991.tb16050.x).

## Matching structures

What the papers relate to the states:

- **3E50**: TGF-alpha bound to inactive IDE; aa 1-3 and 10-14 visible, D10-Q14 helix-to-strand versus free 1YUF. Partner-bound with possible incomplete occupancy, not an apo alternate state.
- **7SZ5, 7SZ7**: TGF-alpha-bound full-length EGFR cryo-EM classes (tips separated, tips juxtaposed); the heterogeneity is in the receptor. Partner-bound, not an apo alternate state.

## Other conditions (not the reference state)

- pH 7.1 ± 0.1, 30 ± 0.5 °C, no buffer, 500 MHz, free ligand (1995 RelaxDB source, full text): possible. Single-field Rex > 0.5 Hz at 23 amides (interface and first-strand region), lifetime 1.25 µs to 2.5 ms, intermediate-exchange wording; fast motion at L48-A50 and D7-C8; water-saturation artefact shown for the presaturated HNOE reference (HTGFA-J11 to J15; E-r1 to r4).
- pH 3.5, 30 °C versus pH 6.5, 10 or 30 °C: partially disordered at acidic pH with most hydrogen-bonded backbone intact; condition comparison from an abstract, no rate (HTGFA-J3, HTGFA-HTGFA_20261020092056-r9).
- pH 3.5: amide exchange much faster than mouse EGF (HTGFA-J4, HTGFA-HTGFA_20261020092056-r1).
- EGFR-ED bound: C terminus and interior immobilised, N terminus mobile; binding in fast exchange (HTGFA-J6, HTGFA-J7, HTGFA-HTGFA_20261020092056-r3).
- Dried film after D2O vapour (ATR-FTIR), pH 7.4 HEPES/NaCl before drying: class H/D exchange rates 0.91, 0.27 and 1.41 x 10-4 min-1, not residue-resolved (HTGFA-J5, HTGFA-HTGFA_20261020092056-r10).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| HTGFA-HTGFA_20261020092056-r1 | [Sequence-specific 1H-NMR assignments and identification of two small…](https://doi.org/10.1073/pnas.86.5.1519) | other | Solvent exchange/protection differences | abstract_only |
| HTGFA-HTGFA_20261020092056-r2 | [The solution structure of human transforming growth factor alpha.](https://doi.org/10.1111/j.1432-1033.1991.tb16050.x) | other | pH-dependent conformational interconversion | abstract_only |
| HTGFA-HTGFA_20261020092056-r3 | [Interaction of transforming growth factor alpha with the epidermal…](https://doi.org/10.1021/bi00255a009) | nmr_spin_relaxation | Ligand-dependent regional mobility and fast binding exchange | abstract_only |
| HTGFA-HTGFA_20261020092056-r7 | [Molecular basis for the recognition and cleavages of IGF-II,…](https://doi.org/10.1016/j.jmb.2009.10.072) | pdb_structure_comparison | Binding-associated substrate structural rearrangement | full_text |
| HTGFA-HTGFA_20261020092056-r9 | [Solution structure of human type-alpha transforming growth factor…](https://doi.org/10.1021/bi00080a003) | pdb_structure_comparison | Condition-dependent partial disorder; exchange process unresolved | abstract_only |
| HTGFA-HTGFA_20261020092056-r10 | [The kinetics of the hydrogen/deuterium exchange of epidermal growth…](https://doi.org/10.1529/biophysj.107.125856) | other | Solvent exchange and heterogeneous motif-level protection | full_text |
| HTGFA-HTGFA_20261020092056-r12 | [A molecular mechanism for the generation of ligand-dependent…](https://doi.org/10.7554/elife.73218) | pdb_structure_comparison | Ligand-bound receptor conformational heterogeneity and differential Domain IV leg order | full_text |
| HTGFA-HTGFA_20261020201428-r1 | [Human type-alpha transforming growth factor undergoes slow…](https://doi.org/10.1021/bi00008a003) | nmr_spin_relaxation | Fast backbone flexibility, especially the C-terminal tail and several bends; slower internal components in some model-free fits. | full_text |
| HTGFA-HTGFA_20261020201428-r2 | [Human type-alpha transforming growth factor undergoes slow…](https://doi.org/10.1021/bi00008a003) | nmr_exchange_broadening | Conformational exchange detected through additional 15N line broadening; atomic mechanism unresolved. | full_text |
| HTGFA-HTGFA_20261020201428-r3 | [Human type-alpha transforming growth factor undergoes slow…](https://doi.org/10.1021/bi00008a003) | nmr_spin_relaxation | Amide–water proton exchange perturbs apparent HNOE; confounded readout of backbone flexibility. | full_text |
| HTGFA-HTGFA_20261020201428-r4 | [Human type-alpha transforming growth factor undergoes slow…](https://doi.org/10.1021/bi00008a003) | pdb_structure_comparison | Structural ensemble heterogeneity compared with fast flexibility and slower exchange; cause of loop heterogeneity not uniquely resolved. | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `HTGFA`.

## Caveats

Call raised from unknown to possible on 2026-10-20 after the RelaxDB source paper (doi:10.1021/bi00008a003, Li and Montelione 1995) was read in full: exchange is detected in the reference state as single-field Rex at 23 of 36 analysed amides, and under the single-field Rex rule decided that night (ledger/redraft_notes.json, _RULE_single_field_rex) this counts as exchange detected without a population. Fixed caveat: single-field Rex can also come from anisotropic tumbling; a dispersion experiment would confirm. The authors themselves call the regime intermediate (microsecond) and give only lifetime bounds (1.25 µs to 2.5 ms) under an equal-population, 10 ppm assumption, so the state is not shown to be slow enough for separate peaks; literal_two_peak is 'does not'. The sample has no buffer (direct dissolution with NaN3), the Rex threshold of 0.5 Hz is the authors' operational cutoff with uncertainties of ±0.3-0.5 Hz, and Q26 lacks a reported error. Nine of the other rows are abstracts. The RelaxDB HTGFA source is still unconfirmed (no BMRB id). The abstract-only rows HTGFA-HTGFA_20261020145442-r1 and r2 are superseded and no longer cited. Built from cases V6_r6_HTGFA_20261020092056, S6_r6_HTGFA_20261020145442 and S6_r6_HTGFA_20261020201428.

## Open questions

- H/D exchange paper (r10): the prose says TGF-alpha beta-sheet exchange is ten orders of magnitude slower than EGF, while Table 1 gives 1.41 x 10-4 versus 1.88 x 10-3 min-1, about one order. Table values are used.
- Within the 1995 paper the iterative-cycle text says 25 sites required an exchange term while the final analysis reports 23 (D47's model-6 term rejected; threshold 0.5 Hz); the final 23 are used (J12). The title says 'slow conformational exchange' while the abstract and Results call the regime intermediate 15N chemical exchange on the microsecond timescale; 'slow' there means slower than tumbling, not slow on the chemical-shift timescale.
- The RelaxDB HTGFA set is presumably Li and Montelione 1995 (doi:10.1021/bi00008a003, pH 7.1, 30 °C, 500 MHz, no buffer; now full text). It detects exchange only as single-field Rex at 23 amides with lifetime bounds of 1.25 µs to 2.5 ms and calls the regime intermediate (microsecond): does single-field Rex count as us-ms exchange for the alternate-APO call (applied here as 'possible' with the anisotropic-tumbling caveat), given that the authors' wording argues against separate peaks?
- Does the pH-dependent conformational interconversion in the 1991 structure paper (r2) show two peak sets at one pH, or a shift between pH values? Only the abstract was readable.

Judgments: HTGFA-J1, HTGFA-J2, HTGFA-J3, HTGFA-J4, HTGFA-J5, HTGFA-J7, HTGFA-J8, HTGFA-J9, HTGFA-J11, HTGFA-J12, HTGFA-J13, HTGFA-J14, HTGFA-J15 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
