# Human CDNF C-terminal domain (entry = author 102–161

RelaxDB entry `CDNFCT` · set RelaxDB-133 · Human CDNF C-terminal domain (entry = author 102–161, 60 residues)

## Answer

**Unknown: not measured, or the key paper is not readable in full.**

**Strict two-peak reading:** cannot tell. The isolated domain is not measured; in full-length CDNF the authors attribute missing amides to millisecond exchange, called intermediate in the 2021 paper, with no dispersion and no second peak set.

No evidence row measures the isolated 60-residue domain. In full-length CDNF the amides of C132, R133 and K138 are broadened beyond detection, which the authors attribute to millisecond exchange, but no dispersion, rate or population exists and the dispersion search returned no hits.

## The free protein (reference state)

Isolated wild-type apo C-terminal domain; no evidence row measures it. Nearest sample: full-length mature CDNF (author 1–161) at 25 °C, pH 6, 20 mM phosphate, 1 mM EDTA

| | |
|---|---|
| Where (residues) | C132, R133, K138 (entry 31, 32, 37) in full-length CDNF; A134 also lacks an HN in the Methods list but is not named in the exchange text (CDNFCT-J5). |
| Exchange rate kex | not measured (CDNFCT-J5) |
| Minor-state population pB | not measured (CDNFCT-J5) |
| Exchange regime | Not measured for the domain. In full-length CDNF the authors attribute the missing amides to millisecond exchange (2015) and, citing that study, to millisecond intermediate exchange (2021) (CDNFCT-J5, CDNFCT-J6). |

Fallback statement: No alternate-state annotation for the isolated domain; in full-length CDNF, C132, R133 and K138 may undergo millisecond exchange, based on missing amide peaks (doi:10.1074/jbc.m115.662254).

## Matching structures

## Other conditions (not the reference state)

- Full-length CDNF, 25 °C, pH 6, phosphate/EDTA: unknown. C132, R133 and K138 are broadened beyond detection and attributed to millisecond exchange; the judgment leaves it unresolved because a missing peak cannot separate exchange from solvent exchange (CDNFCT-J5, CDNFCT-r2).
- Full-length CDNF in MES pH 7 (2021): some amides again undetectable, figure-only, no new kinetics (CDNFCT-J6, CDNFCT-r6).
- Full-length CDNF: the C-terminal domain reorients semi-independently of the N-terminal domain (no interdomain NOEs, lower R2/R1), a motion with no counterpart in the isolated domain (CDNFCT-J7, CDNFCT-r1, CDNFCT-r3).
- With α-synuclein: shift perturbations at V118, Q123 and S127; binding, no rate (CDNFCT-J8, CDNFCT-r5).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| CDNFCT-r1 | [The Solution Structure and Dynamics of Full-length Human Cerebral…](https://doi.org/10.1074/jbc.m115.662254) | nmr_spin_relaxation | Fast terminal/linker backbone flexibility, heterogeneous local motion, and semi-independent domain tumbling | full_text |
| CDNFCT-r2 | [The Solution Structure and Dynamics of Full-length Human Cerebral…](https://doi.org/10.1074/jbc.m115.662254) | nmr_exchange_broadening | Local conformational exchange inferred from line broadening near the C-terminal cysteine motif | full_text |
| CDNFCT-r3 | [The Solution Structure and Dynamics of Full-length Human Cerebral…](https://doi.org/10.1074/jbc.m115.662254) | other | Variable interdomain orientation with a well-folded C-terminal core | full_text |
| CDNFCT-r5 | [Cerebral dopamine neurotrophic factor reduces α-synuclein…](https://doi.org/10.1016/j.ymthe.2021.04.035) | other | Binding-associated local environment changes; proposed conformational switch remains unresolved | full_text |
| CDNFCT-r6 | [Cerebral dopamine neurotrophic factor reduces α-synuclein…](https://doi.org/10.1016/j.ymthe.2021.04.035) | nmr_exchange_broadening | Pre-existing intermediate-exchange broadening limits detection of partner effects | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `CDNFCT`.

## Caveats

Every evidence-bearing judgment is on full-length CDNF, so it bears on the entry only by inference; the NMR collaborator is asked whether full-length relaxation should count. PDB 2LPN (isolated C-terminal domain structure) is tied to no evidence row, so no structure is matched. The RelaxDB CDNFCT source is unknown (no BMRB id).

## Open questions

- Paralog claim versus target structure, not a same-protein conflict: the MANF abstract calls its C-terminus natively unfolded (r9), while full-length CDNF has a folded C-terminal domain with no large fast motion (r1, r3).
- Broadened-residue lists differ inside the 2015 paper: the Methods list of missing HN includes A134, the Results exchange text names only C132, R133 and K138 (r2).
- Which study supplied the RelaxDB CDNFCT relaxation set? The input lists no BMRB id, and PDB 2LPN (an isolated C-terminal domain structure) is tied to no evidence row.
- Should full-length CDNF relaxation (linker and domain context) count toward the isolated-domain entry, or only as inference?

Judgments: CDNFCT-J5, CDNFCT-J6, CDNFCT-J7, CDNFCT-J8, CDNFCT-J10 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
