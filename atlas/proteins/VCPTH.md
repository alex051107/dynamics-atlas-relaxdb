# Vibrio cholerae peptidyl-tRNA hydrolase (VcPth)

RelaxDB entry `VCPTH` · set RelaxDB-133 · Vibrio cholerae peptidyl-tRNA hydrolase (VcPth), full length with His tag (pET-NH6)

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** does not. The only stated regime is the authors' reading of the missing N118 amide as intermediate exchange; no dispersion was recorded and no second peak set is reported.

Single-field model-free fits need exchange terms at T22, A79, G115–H117, D147 and H192, and the N118 and K146 amides are missing in the wild type but N118 returns in active-site mutants. The judgments leave both unresolved: single-field Rex cannot be separated from anisotropic tumbling, and a missing peak gives no rate. Under the single-field Rex rule of 2026-10-20 (author-reported Rex in the reference state from a full-text relaxation analysis counts as exchange detected without a population) the call is 'possible'; no new evidence was added. No relaxation-dispersion study was found, but the dispersion queries used E. coli Pth terms, so this is a search gap.

## The free protein (reference state)

Wild-type apo (no substrate), 298 K, pH 6.5, 20 mM NaH2PO4, 50 mM NaCl, 1 mM DTT, 0.1% NaN3, 0.5 mM 15N; 700 MHz, single field

| | |
|---|---|
| Where (residues) | Rex at T22 (next to catalytic H24), A79, base loop G115–H117 at the helix α3 N-terminus, lid D147 and H192 in the C-terminal hairpin (VCPTH-J3); missing amides N118 (helix α3 N-cap) and K146 (lid flap) (VCPTH-J4). |
| Exchange rate kex | not measured (VCPTH-J3, VCPTH-J12) |
| Minor-state population pB | not measured (VCPTH-J3, VCPTH-J4) |
| Exchange regime | Not measured. The authors read the missing N118 amide as intermediate exchange from transient N118–H24 contact; solvent exchange was argued against, not tested (VCPTH-J4, VCPTH-r4). At pH 6.0 and below (visible on lowering from 6.5 to 6.0; assigned at pH 5.2) the N118 peak returns, which fits either H24 protonation or slower base-catalysed solvent exchange (VCPTH-J5, VCPTH-r5). |

Fallback statement: May have slow motion near the catalytic H24, at the helix α3 N-cap and in the lid, based on single-field 15N relaxation and missing amide peaks of the free enzyme (doi:10.1261/rna.057620.116); no dispersion data exist.

## Matching structures

What the papers relate to the states:

- **5IMB; 5B6J**: N14D and H24N mutant crystals in which H24 hydrogen-bonds N14. The authors propose that wild-type side chains switch between the N14 and N118 bonds in solution; no experiment shows the wild type interconverting.
- **5IKE; 4Z86**: D97N and N118D mutant crystals in which H24 hydrogen-bonds N118/D118, the other half of the proposed switch. Static mutant structures, no rate.

## Other conditions (not the reference state)

- H24N: unknown. The single-field exchange term moves from the H24 region to the lid hinge G139 and L154; no rate (VCPTH-J7, VCPTH-r2).
- N118D: unknown. Larger slow-motion terms near H24, residues figure-only, no rate (VCPTH-J8, VCPTH-r3).
- E. coli Pth homolog crystals: the lid loop–helix α4 has high B-factors and differs between free 2PTH and tRNA-fragment-bound 3VJR, which may reflect packing (VCPTH-J11, VCPTH-r8).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| VCPTH-r1 | [Unraveling the stereochemical and dynamic aspects of the catalytic…](https://doi.org/10.1261/rna.057620.116) | nmr_spin_relaxation | slow (us-ms) exchange contribution Rex near catalytic H24, base loop and lid; ps-ns internal motion (tau_e) at listed loop residues | full_text |
| VCPTH-r2 | [Unraveling the stereochemical and dynamic aspects of the catalytic…](https://doi.org/10.1261/rna.057620.116) | nmr_spin_relaxation | mutation-redistributed motion: added ps-ns flexibility near N14/helix alpha2/alpha3 tip; Rex appears at lid hinge, lost near residue 24 | full_text |
| VCPTH-r3 | [Unraveling the stereochemical and dynamic aspects of the catalytic…](https://doi.org/10.1261/rna.057620.116) | nmr_spin_relaxation | enhanced slow (us-ms) exchange near catalytic H24 | full_text |
| VCPTH-r4 | [Unraveling the stereochemical and dynamic aspects of the catalytic…](https://doi.org/10.1261/rna.057620.116) | nmr_exchange_broadening | intermediate-exchange line broadening of the helix alpha3 N-cap amide (N118); also missing lid-flap K146 | full_text |
| VCPTH-r5 | [Unraveling the stereochemical and dynamic aspects of the catalytic…](https://doi.org/10.1261/rna.057620.116) | nmr_exchange_broadening | pH-dependent reappearance of the broadened N118 amide | full_text |
| VCPTH-r7 | [Unraveling the stereochemical and dynamic aspects of the catalytic…](https://doi.org/10.1261/rna.057620.116) | pdb_structure_comparison | side-chain rearrangement of the N14/N118-H24-D97 network across mutants; loop differences between solution and crystal | full_text |
| VCPTH-r8 | [Structural basis for the substrate recognition and catalysis of…](https://doi.org/10.1093/nar/gks790) | pdb_structure_comparison | tRNA-bound vs free loop differences; elevated B-factors (plasticity) in the lid loop–helix α4 | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `VCPTH`.

## Caveats

Call changed from unknown to possible on 2026-10-20 by the single-field Rex rule (ledger/redraft_notes.json, _RULE_single_field_rex), not by new evidence: the judgments (VCPTH-J3, J4) stay unresolved, and the only us-ms evidence is still the single-field model-free Rex and the missing N118/K146 amides of the 2017 paper. Fixed caveat: single-field Rex can also come from anisotropic tumbling; a dispersion experiment would confirm. the NMR collaborator is asked whether single-field model-free Rex should count as us-ms detection. The input card pairs the V. cholerae sequence and 2MJL with UniProt P0A7D1 (E. coli Pth); V. cholerae Pth is treated as the entry. All VcPth NMR uses phosphate, which could occupy the basic 5'-phosphate clamp, with no control. One 2017 paper supplies every VcPth row.

## Open questions

- N118 peak recovery below pH 6 (r5): protonation of H24 altering N118 conformational exchange, or slower base-catalysed amide-solvent exchange; no CLEANEX or dispersion separates them.
- Gate-lid coupling: an earlier cross-species crystal proposal held that gate opening goes with lid closing; the VcPth wild-type and mutant structures show no inverse correlation (r7). Both rest on static crystals.
- The input card pairs the V. cholerae Pth sequence and NMR structure 2MJL with UniProt P0A7D1 (E. coli Pth); the fill worker set the target by sequence. Is RelaxDB VCPTH the V. cholerae data of the 2017 paper (r1)?
- Should single-field model-free Rex count as us-ms detection for the WT apo answer, or stay unresolved until dispersion data exist?

Judgments: VCPTH-J3, VCPTH-J4, VCPTH-J5, VCPTH-J7, VCPTH-J8, VCPTH-J10, VCPTH-J11, VCPTH-J12 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
