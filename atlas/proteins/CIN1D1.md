# Venturia inaequalis cellophane-induced protein 1 (Cin1

RelaxDB entry `CIN1D1` · set RelaxDB-133 · Venturia inaequalis cellophane-induced protein 1 (Cin1, UniProt A8W3P3), repeat domain 1 (entry 1-65 = residues 1-65 of the 2LHT D1D2 construct)

## Answer

**Unknown: not measured, or the key paper is not readable in full.**

**Strict two-peak reading:** cannot tell. All rows are abstracts of longer constructs; none states an exchange regime or shows two peak sets.

The only relaxation study (D1D2, abstract) reports large-amplitude motion of a short inter-domain linker without residues or rates (CIN1D1-J1); SAXS of D1D2 and full-length Cin1 suggests inter-domain flexibility (CIN1D1-J2, CIN1D1-J3). Nothing measures µs-ms exchange (CIN1D1-J5, search_insufficient).

## The free protein (reference state)

Free isolated domain 1 (entry sequence, 65 residues); no row describes this sample, and the input card gives no BMRB id (the 2LHT D1D2 structure deposition lists pH 6.2, 298 K)

| | |
|---|---|
| Where (residues) | none; the mobile linker residues are not given and may lie outside the entry (CIN1D1-J1) |
| Exchange rate kex | not measured (CIN1D1-J5) |
| Minor-state population pB | not measured (CIN1D1-J5) |
| Exchange regime | Not stated (CIN1D1-J5). |

Fallback statement: No alternate-state annotation is possible for isolated Cin1 domain 1: the evidence describes inter-domain linker mobility and loose domain packing in longer constructs, from abstracts only (doi:10.1016/j.bbapap.2012.06.015).

## Matching structures

## Other conditions (not the reference state)

- Cin1-D1D2: short inter-domain linker with large-amplitude motion and reciprocal domain mobility (15N relaxation and SAXS, abstract; CIN1D1-J1, CIN1D1-J2).
- Full-length Cin1: loosely packed repeat domains, beads-on-a-string (SAXS, abstract; CIN1D1-J3).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| CIN1D1-r1 | [Structure, dynamics and domain organization of the repeat protein…](https://doi.org/10.1016/j.bbapap.2012.06.015) | nmr_spin_relaxation | Large-amplitude linker mobility associated with relative motion of the two domains; quantitative detection window unavailable. | abstract_only |
| CIN1D1-r2 | [Structure, dynamics and domain organization of the repeat protein…](https://doi.org/10.1016/j.bbapap.2012.06.015) | other | Interdomain flexibility inferred from a solution scattering envelope. | abstract_only |
| CIN1D1-r3 | [Structure, dynamics and domain organization of the repeat protein…](https://doi.org/10.1016/j.bbapap.2012.06.015) | other | Flexible organization of repeat domains inferred from loose packing in SAXS models. | abstract_only |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `CIN1D1`.

## Caveats

If the RelaxDB set is the domain-1 part of the D1D2 relaxation data, the D1D2 rows describe the deposited sample and the full text could change the call. The zero-hit method searches missed even the known Cin1 paper.

## Open questions

- Is the RelaxDB CIN1D1 set the domain-1 part (residues 1-65) of the D1D2 relaxation data of Mesarich et al. 2012 (2LHT)? If so, the D1D2 rows describe the deposited sample and the inter-domain linker may fall partly inside the entry.
- Can the full text of doi:10.1016/j.bbapap.2012.06.015 be obtained to identify the linker residues and any exchange-broadened domain-1 amides?

Judgments: CIN1D1-J1, CIN1D1-J2, CIN1D1-J3, CIN1D1-J4, CIN1D1-J5, CIN1D1-J6 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
