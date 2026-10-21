# Chicken (Gallus gallus) villin-1 domain 6 (V6)

RelaxDB entry `VILD6` · set RelaxDB-133 · Chicken (Gallus gallus) villin-1 domain 6 (V6), isolated, 107 residues (2LLF chain A)

## Answer

**Unknown: not measured, or the key paper is not readable in full.**

**Strict two-peak reading:** cannot tell. Nothing measures the calcium-free isolated domain. In calcium-bound D6-HP the authors attribute the missing P68-D72 and E85 amides to intermediate exchange on the NMR timescale, which would not qualify, and no second peak set is reported (VILD6-J7).

No evidence row measures dynamics of calcium-free isolated D6 in any window (VILD6-J2 to J4). The RelaxDB source paper (doi:10.1021/bi700110v, read in full) is on the larger D6-HP construct in 5 mM calcium: the D6 region 1-105 is structured on the ps-ns scale apart from F84 (VILD6-J5, J6); the P68-D72 loop and E85 are missing from the HSQC with intermediate exchange proposed and no rate or population (VILD6-J7); calcium removal makes a quarter of D6 amides disappear or shift in the first 80 residues, confounded by aggregation (VILD6-J8). Exchange seen only in another construct and bound state is not exchange in the reference state, so the call stays unknown.

## The free protein (reference state)

Calcium-free wild-type isolated V6 (the 107-residue entry sequence); no evidence row measures it. The RelaxDB source paper measured D6-HP (208 residues) in 5 mM calcium at 25 °C, pH 7.0, a different construct and ligand state.

| | |
|---|---|
| Where (residues) | none measured in the reference state. Calcium-bound D6-HP: P68-D72 and E85 missing (intermediate exchange proposed), A60-E62 missing and unexplained, F84 mobile on the ps-ns scale (VILD6-J5, J7); calcium-free D6-HP: first 80 residues affected, no list (VILD6-J8) |
| Exchange rate kex | not measured (VILD6-J3); the D6-HP missing peaks carry no rate (VILD6-J7) |
| Minor-state population pB | not measured (VILD6-J3); 'one quarter of D6 amides' on calcium removal is a count of affected peaks, not a population (VILD6-J8) |
| Exchange regime | Not measured for the reference state (VILD6-J3). Calcium-bound D6-HP: 'intermediate structural exchange on the NMR time scale' proposed for P68-D72 and E85 (VILD6-J7). |

Fallback statement: No apo alternate-state annotation is possible for isolated V6. In the D6-HP construct with 5 mM calcium the D6 loop P68-D72 and E85 are broadened out, which the authors propose reflects intermediate exchange (doi:10.1021/bi700110v); isolated V6 changes conformation on calcium binding, centred on the long helix (doi:10.1021/bi400699s, abstract only).

## Matching structures

What the papers relate to the states:

- **2LLF**: Calcium-bound NMR structure of isolated V6 with an extended long helix. A ligand-bound form, not an apo minor state; the gelsolin-like straightening pathway is proposed, not experimentally resolved.

## Other conditions (not the reference state)

- D6-HP in 5 mM CaCl2, 25 °C, pH 7.0, 20 mM PIPES (RelaxDB source paper): D6 structured on the ps-ns scale except F84 (low R2, NOE below 0.6); P68-D72 and E85 missing from the HSQC, intermediate exchange proposed; no rate or population (VILD6-J5 to J7, VILD6-VILD6_20261020153804-r1, r2).
- D6-HP without calcium: about one quarter of D6 amide peaks disappear or shift, in the first 80 residues; calcium-poor D6-HP aggregates within hours, so exchange, unfolding and oligomerisation cannot be separated (VILD6-J8, VILD6-VILD6_20261020153804-r3).
- Calcium titration of isolated V6 (micromolar to millimolar): the long helix and its neighbours respond most to micromolar calcium, with tryptophan-fluorescence Kd values of 22 µM and 2.8 mM; an equilibrium, ligand-driven change with no rate, population or residue list (VILD6-J1, VILD6-r26).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| VILD6-r26 | [Gelsolin-like activation of villin: calcium sensitivity of the long…](https://doi.org/10.1021/bi400699s) | other | Calcium-linked conformational response of the long helix | abstract_only |
| VILD6-VILD6_20261020153804-r1 | [The Isolated Sixth Gelsolin Repeat and Headpiece Domain of Villin…](https://doi.org/10.1021/bi700110v) | nmr_spin_relaxation | Fast backbone flexibility and flexible interdomain tether; local mobility at F84 | full_text |
| VILD6-VILD6_20261020153804-r2 | [The Isolated Sixth Gelsolin Repeat and Headpiece Domain of Villin…](https://doi.org/10.1021/bi700110v) | nmr_exchange_broadening | Possible intermediate structural exchange in D6; missing assignments are not a kinetic measurement | full_text |
| VILD6-VILD6_20261020153804-r3 | [The Isolated Sixth Gelsolin Repeat and Headpiece Domain of Villin…](https://doi.org/10.1021/bi700110v) | nmr_exchange_broadening | Calcium-dependent D6 destabilization or conformational change, confounded by aggregation | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `VILD6`.

## Caveats

The RelaxDB VILD6 relaxation set appears to come from D6-HP in 5 mM calcium (doi:10.1021/bi700110v, case S6_r6_VILD6_20261020153804, read in full on 2026-10-20), while the entry sequence is the isolated 107-residue D6; if the NMR collaborator sets the reference state to calcium-bound D6 within D6-HP, the call rises to possible on the missing P68-D72 and E85 amides. BMRB 18046 (cross-referenced by 2LLF) deposits no relaxation lists. Villin headpiece rows (VILD6-r1 to r25) are a separate domain and were not used.

## Open questions

- Not a conflict but a construct and state gap: the entry sequence is the 107-residue isolated D6, while the RelaxDB source paper measured relaxation only on the 208-residue D6-HP construct in 5 mM calcium; every new judgment is therefore other-construct, calcium-bound evidence.
- The RelaxDB VILD6 relaxation set appears to come from D6-HP (208 residues) in 5 mM CaCl2 at 25 °C, pH 7.0 (doi:10.1021/bi700110v), while the entry sequence is the isolated 107-residue D6: should the entry's reference state be calcium-bound D6 within D6-HP rather than calcium-free isolated V6?
- Should calcium-free and calcium-bound D6 be carried as separate sample states, given that calcium removal from D6-HP changes a quarter of the D6 amide peaks and the protein then aggregates within hours?

Judgments: VILD6-J1, VILD6-J2, VILD6-J3, VILD6-J4, VILD6-J5, VILD6-J6, VILD6-J7, VILD6-J8 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
