# Human cellular retinoic acid-binding protein 2 (CRABP2

RelaxDB entry `CRABP2` · set RelaxDB-133 · Human cellular retinoic acid-binding protein 2 (CRABP2, UniProt P29373), residues P1-E137

## Answer

**Yes: a minor state is measured in the free protein.**

**Strict two-peak reading:** does not. The authors describe the free-protein exchange as intermediate-timescale ('intermediate conformational exchange'), with broadened, unassignable amides near the exchanging residues; no second peak set is reported. The slow-exchange statement in the paper concerns atRA binding, not the apo state.

Free wild-type CRABP2 shows microsecond-millisecond exchange across the portal and gap regions by two-field 15N CPMG, and a core group of residues fits one two-state process with a measured rate and a large minor-state population. The CPMG shifts do not match the atRA-bound shifts, so the minor state is a distinct apo conformation, not the holo structure. Other residues exchange at similar rates without sharing the fit, and atRA quenches the process.

## The free protein (reference state)

Entry construct as deposited (human CRABP2 P1-E137, wild type), free, no retinoid; measured at 298 K, pH 7.4, 20 mM sodium phosphate, 150 mM NaCl, 5 mM DTT, 10% D2O, 1.0 mM, Thio6His6 tag removed by TEV (2019 paper)

| | |
|---|---|
| Where (residues) | Core group K8, L19, L22, K30, I31, A32, R59, E73, Q74, V76, T114, T131, Y134, plus 'Thr51-Ile53' which does not map to the entry sequence (Y51-I52-K53) and is left out (CRABP2-J1). Further dispersing residues are shown only in Fig. 5B (CRABP2-J2); 14 amides broadened beyond assignment: E13, E16, R29, A34-A36, K38, V41, T56-V58, T60, N115, V133 (CRABP2-J3). |
| Exchange rate kex | 320 ± 40 s-1 (core-group global Carver-Richards fit, 298 K, 800 and 900 MHz) (CRABP2-J1, CRABP2-r5) |
| Minor-state population pB | 0.2 ± 0.03 (CRABP2-J1, CRABP2-r5) |
| Exchange regime | Intermediate, as stated by the authors; per-residue delta omega is in Table S1, which was not retrieved, so the regime cannot be checked against kex. |

Fallback statement: May have an alternate apo conformation involving the portal (alpha1-loop-alpha2, betaC-betaD and betaE-betaF loops) and gap (betaD, betaE) regions, based on 15N CPMG relaxation dispersion of the free protein (doi:10.1021/acs.biochem.9b00672); the 1998 apo NMR ensemble with a widened ligand entrance (doi:10.1021/bi9808924, abstract only) is a candidate but is not tied to the CPMG state.

## Matching structures

What the papers relate to the states:

- **2FR3**: atRA-bound crystal structure. The authors find the CPMG-derived shifts do not agree with the apo-to-holo CSPs, so the minor state is structurally distinct from the atRA complex; not a match.
- **2FS6**: Apo crystal structure; pocket near-identical to 2FR3, so it shows the dominant conformer, not the CPMG minor state.

## Other conditions (not the reference state)

- atRA-bound, same buffer, 298 K, 1.0 mM: core exchange not detected by CPMG (CRABP2-J4, CRABP2-r7); residual faster fluctuation at I10-S12, L19, K38, T122-T124, R132, unresolved because four of these residues lie on the dimer interface (CRABP2-J5, CRABP2-r8).
- atRA-bound, pH 6.8, 10-800 μM: weak self-association, apparent Kd about 1.0 ± 0.2 mM; intermolecular, not an alternate state (CRABP2-J12, CRABP2-r10).
- His6-tagged CRABP2 on an SPR chip, 25 °C, Tween 20: atRA kon (6.92 ± 2.32) x 10^5 M-1 s-1, koff (4.01 ± 1.08) x 10^-3 s-1; binding kinetics (CRABP2-J13, CRABP2-r11).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| CRABP2-r1 | [NMR solution structure of type II human cellular retinoic acid…](https://doi.org/10.1021/bi9808924) | nmr_exchange_broadening | Ligand-pocket dynamic disorder inferred from weak or absent resonances | abstract_only |
| CRABP2-r2 | [NMR solution structure of type II human cellular retinoic acid…](https://doi.org/10.1021/bi9808924) | pdb_structure_comparison | Structural heterogeneity and ligand-entrance differences | abstract_only |
| CRABP2-r3 | [Retinoic Acid Binding Leads to CRABP2 Rigidification and Dimerization.](https://doi.org/10.1021/acs.biochem.9b00672) | nmr_spin_relaxation | Fast backbone flexibility and global rotational diffusion | full_text |
| CRABP2-r5 | [Retinoic Acid Binding Leads to CRABP2 Rigidification and Dimerization.](https://doi.org/10.1021/acs.biochem.9b00672) | nmr_relaxation_dispersion | Microsecond-to-millisecond conformational exchange | full_text |
| CRABP2-r6 | [Retinoic Acid Binding Leads to CRABP2 Rigidification and Dimerization.](https://doi.org/10.1021/acs.biochem.9b00672) | nmr_relaxation_dispersion | Additional apo exchange heterogeneity | full_text |
| CRABP2-r7 | [Retinoic Acid Binding Leads to CRABP2 Rigidification and Dimerization.](https://doi.org/10.1021/acs.biochem.9b00672) | nmr_relaxation_dispersion | Suppression of the principal apo-like exchange in the CPMG window | full_text |
| CRABP2-r8 | [Retinoic Acid Binding Leads to CRABP2 Rigidification and Dimerization.](https://doi.org/10.1021/acs.biochem.9b00672) | nmr_relaxation_dispersion | Residual faster exchange distinct from principal apo process | full_text |
| CRABP2-r9 | [Retinoic Acid Binding Leads to CRABP2 Rigidification and Dimerization.](https://doi.org/10.1021/acs.biochem.9b00672) | nmr_exchange_broadening | Exchange-associated broadening near dispersing regions | full_text |
| CRABP2-r10 | [Retinoic Acid Binding Leads to CRABP2 Rigidification and Dimerization.](https://doi.org/10.1021/acs.biochem.9b00672) | nmr_exchange_broadening | Concentration-dependent self-association and interface broadening | full_text |
| CRABP2-r11 | [Retinoic Acid Binding Leads to CRABP2 Rigidification and Dimerization.](https://doi.org/10.1021/acs.biochem.9b00672) | other | Ligand association and dissociation kinetics | full_text |
| CRABP2-r12 | [Retinoic Acid Binding Leads to CRABP2 Rigidification and Dimerization.](https://doi.org/10.1021/acs.biochem.9b00672) | pdb_structure_comparison | Limited static structural difference despite solution exchange | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `CRABP2`.

## Caveats

One paper, one temperature (298 K), phosphate buffer without a phosphate-free control, 1.0 mM protein; the supplement (Table S1, Figs. S4, S6) was not retrieved, so per-residue delta omega and the CPMG-versus-CSP comparison could not be checked. The core list contains a residue range that does not fit the entry sequence. A minor-state population of 0.2 is large for a CPMG fit and has no second method behind it. The RelaxDB CRABP2 source sample is unknown (no BMRB id). Built from case V6_r6_CRABP2_20261020094132; replaces the empty search_insufficient judgment of the crashed first search.

## Open questions

- Apo pocket structure: the 1998 abstract reports a disordered apo NMR ensemble (A32-P39, T57-E62) with a wider ligand entrance than the holo crystal (r2), while the 2019 paper finds the apo 2FS6 and holo 2FR3 crystal pockets near-identical (r12); the restraint-scarcity reading of the 1998 ensemble is a row caveat, not a statement of either paper. Not a conflict of judgments (different methods, no rate), but the structure of the exchanging state stays open.
- Core-group numbering: the 2019 text lists 'Thr51-Ile53' (betaC), but entry positions 51-53 are Y51-I52-K53 (T54 follows); Table S1 was not retrieved, so these positions are left out of J1 and J4 (r5, r7).
- Which sample is the RelaxDB CRABP2 entry: the 2019 Biochemistry R1/R2/NOE set (900 MHz, 298 K, pH 7.4 phosphate, 1.0 mM apo), or another deposition? The input lists no BMRB id.
- Which three residues does 'Thr51-Ile53' in the 2019 core group mean? No Thr-x-Ile stretch exists near betaC in the entry sequence (D48-T49-F50-Y51-I52-K53-T54); Table S1 of that paper would settle it.

Judgments: CRABP2-J1, CRABP2-J2, CRABP2-J3, CRABP2-J4, CRABP2-J5, CRABP2-J10, CRABP2-J11, CRABP2-J12, CRABP2-J13 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
