# Human VHR (Vaccinia H1-related) phosphatase

RelaxDB entry `VHR_CPMG` · set CPMG-10 · Human VHR (Vaccinia H1-related) phosphatase, full-length wild type

## Answer

**Yes: a minor state is measured in the free protein.**

**Strict two-peak reading:** cannot tell. Regime not stated by the authors; the 1.2% minor state is seen only through dispersion and no second peak set is reported.

At 25 °C nine amides in the variable insert and the acid loop fit one shared process with a minor state of about 1.2% (reported as pA = 98.8 ± 0.1%). CPMG |ΔωN| is several-fold larger than the apo-to-tungstate shift (e.g. A63 930 vs 260 s-1), and the authors say the interconverting structures 'remain unclear'.

## The free protein (reference state)

Wild-type apo VHR, 25 °C; pH 6.5, 20 mM Bis-Tris propane, 100 mM NaCl, 1 mM TCEP, 1 mM EDTA, no phosphate added; CPMG sample 700 µM 2H/15N (Hahn-echo 700 or 965 µM)

| | |
|---|---|
| Where (residues) | Variable insert A63, R66, N72; acid loop K89, D92, E95, F96, L98, S99; Hahn-echo adds R36, Y78, R119, C124, G161, D164 |
| Exchange rate kex | 1,530 ± 200 s-1, combined variable-insert + acid-loop fit, proposed by the authors as one concerted process on F-test grounds (p = 8.2 × 10−14) (VHR-J1, VHR-r1); the separate fits remain valid and give acid loop 1,400 ± 200 s-1 and variable insert 2,100 ± 460 s-1 |
| Minor-state population pB | reported as pA = 98.8 ± 0.1% in the combined fit, so pB = 1.2 ± 0.1%; separate fits reported as pA = 98.9 ± 0.1% (acid loop, pB 1.1 ± 0.1%) and pA = 98.5 ± 0.4% (variable insert, pB 1.5 ± 0.4%) (VHR-r1) |
| Exchange regime | not stated by the authors. Combined-fit /ΔωN/ for A63, R66, N72, K89, D92, E95, F96, L98 and S99: 930 ± 100, 1340 ± 170, 1810 ± 290, 1030 ± 80, 840 ± 160, 1740 ± 320, 1150 ± 120, 1610 ± 240 and 700 ± 90 s-1 (units as printed) (VHR-r1). |

Fallback statement: May have an alternate conformation differing at the variable insert (A63, R66, N72) and the acid loop (K89, D92, E95, F96, L98, S99), based on 15N relaxation-compensated CPMG at 600, 700 and 800 MHz (doi:10.1021/acs.biochem.0c00245).

## Matching structures

Deposited-structure comparison: The spread among apo crystals (about 1.2 Å) equals the shift caused by a bound fragment; no structure matches the 1.2% minor state. Table: [`data/structures/VHR_CPMG.md`](../../data/structures/VHR_CPMG.md).

## Other conditions (not the reference state)

- Tungstate-bound WT: possible. Hahn-echo exchange profile similar to apo, no rate (VHR-J3, VHR-r3).
- N74A mutant, apo and tungstate-bound: most variable-insert and acid-loop residues 'remain exchange broadened', read by the authors as retained or enhanced ms motion, no rate (VHR-J4, VHR-J5).
- Apo crystals 8TK6 and 9DJ9 at 100 K: no_evidence; they are superposed in SI Fig. S6 with no author comment on loop differences, which cannot exclude a 1.2% solution state (VHR-J8, VHR-r10, VHR-r11).
- Fragment F17 complex (8TK2): the variable-insert E-loop A63–N72 shifts by up to 1.4 Å, which the authors attribute to F17 binding ('likely to accommodate F17 binding'); not the CPMG minor state (VHR-J9, VHR-r9).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| VHR-r1 | [Allosteric Impact of the Variable Insert Loop in Vaccinia H1-Related…](https://doi.org/10.1021/acs.biochem.0c00245) | nmr_relaxation_dispersion | Coupled millisecond conformational exchange of variable insert and acid loop | full_text |
| VHR-r2 | [Allosteric Impact of the Variable Insert Loop in Vaccinia H1-Related…](https://doi.org/10.1021/acs.biochem.0c00245) | nmr_exchange_broadening | Millisecond-sensitive exchange contribution to transverse relaxation | full_text |
| VHR-r3 | [Allosteric Impact of the Variable Insert Loop in Vaccinia H1-Related…](https://doi.org/10.1021/acs.biochem.0c00245) | nmr_exchange_broadening | Millisecond-sensitive exchange contribution to transverse relaxation | full_text |
| VHR-r9 | [Fragment Screening Identifies Novel Allosteric Binders and Binding…](https://doi.org/10.1021/acsomega.4c10321) | pdb_structure_comparison | Ligand-associated local conformational differences | full_text |
| VHR-r10 | [Fragment Screening Identifies Novel Allosteric Binders and Binding…](https://doi.org/10.1021/acsomega.4c10321) | pdb_structure_comparison | Apo reference crystal structure; superposition only, no conformational difference or dynamics claimed in the Fig. S6 caption | full_text |
| VHR-r11 | [Fragment Screening Identifies Novel Allosteric Binders and Binding…](https://doi.org/10.1021/acsomega.4c10321) | pdb_structure_comparison | Apo reference crystal structure; superposition only, no conformational difference or dynamics claimed in the Fig. S6 caption | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `VHR_CPMG`.

## Caveats

Single temperature and one study. The coupling of the two loops rests on the authors' model choice (combined versus separate fits). The dissertation that RelaxDB cites as the data source was not read, so its equivalence to the 2020 data is unverified.

## Open questions

- Same apo 25 °C CPMG data, two models: separate fits give acid loop kex 1400 ± 200 s-1, pA 98.9 ± 0.1% and VI kex 2100 ± 460 s-1, pA 98.5 ± 0.4%, while the authors prefer one combined fit (kex 1530 ± 200 s-1, pA 98.8 ± 0.1%) on AIC/F-test grounds (r1); the coupling claim rests on that model choice.
- Same apo sample, two exchange methods: Hahn-echo Rex agrees with CPMG Rex within error for seven of eight shared residues but not for D92, and Hahn-echo flags six residues (R36, Y78, R119, C124, G161, D164) that were not in the CPMG fit (r1, r2).
- CPMG constant relaxation time for the same 2020 experiment: 40 ms in the publisher PDF (Methods) versus 30 ms in the cached PMC author-manuscript text; r1 now records both.
- Which data set is the RelaxDB VHR_CPMG entry: the 2020 paper's 700 μM deuterated apo sample at 25 °C (600/700/800 MHz), or a different dissertation sample (Table 7.10.3, 800 MHz only)? If different, what temperature and buffer did it use?
- Should the atlas carry the combined VI + acid-loop fit (kex 1530 s-1) as the WT apo answer, or keep the separate acid-loop (1400 s-1) and VI (2100 s-1) fits as equally valid until a second temperature or method tests the coupling?

Judgments: VHR-J1, VHR-J2, VHR-J3, VHR-J4, VHR-J5, VHR-J8, VHR-J9, VHR-J12 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
