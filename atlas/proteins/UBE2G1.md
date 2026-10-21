# Human E2 ubiquitin-conjugating enzyme G1 (UBE2G1

RelaxDB entry `UBE2G1` · set RelaxDB-133 · Human E2 ubiquitin-conjugating enzyme G1 (UBE2G1, UniProt P62253), full length 1-170

## Answer

**Unknown: not measured, or the key paper is not readable in full.**

**Strict two-peak reading:** cannot tell. The one study of free UBE2G1 fits no exchange term, states no regime and shows no second peak set; the only 'two-state exchange' in the evidence is ubiquitin attached to the Ube2r1 paralog (UBE2G1-r2, abstract only).

The relaxation set behind this entry is now identified and read: the 2015 study measures R1, R2 and NOE at 800 MHz and 30 °C and reads the acidic loop 97-109 and the termini as more flexible than the core, which tumbles with a correlation time of roughly 12-14 ns (UBE2G1-J3). It fits no order parameters, internal correlation times, exchange rates or populations, and no dispersion, CEST or R1rho experiment of UBE2G1 exists (UBE2G1-J4), so the single-field Rex rule has nothing to act on and the call stays unknown. The gaps in its assignment table are proline and glycine chemistry, not exchange (UBE2G1-J6). The only structural comparison is static and shows almost no backbone change on UbV.G1.1 binding (UBE2G1-J2), and the only other NMR row is an abstract about the acidic loop binding donor ubiquitin in a conjugate (UBE2G1-J1).

## The free protein (reference state)

Free full-length wild-type UBE2G1 as deposited (the entry sequence), no ubiquitin, UbV or E3. The 2015 NMR study (doi:10.1186/s40543-015-0068-z, now full text) measures exactly this: 0.8 mM perdeuterated 2H/13C/15N protein, M1-E170 after GST cleavage (two cloning residues G-2 and S-1 remain), 30 °C, pH 7.0, 50 mM HEPES, 100 mM NaCl, 5 mM DTT, 5% D2O, 800 MHz for relaxation and 900 MHz at 25 °C for the assignments (UBE2G1-J3, J4, J6 marked is_wt_apo).

| | |
|---|---|
| Where (residues) | none for us-ms. ps-ns flexibility in the acidic loop 97-109 (P97 and P107 have no amide, so the range is a regional annotation) and at the termini (UBE2G1-J3); Y102-G103-Y104 is named only as a donor-ubiquitin contact (UBE2G1-J1). Figure 3 of the 2015 paper shows uncommented R2 values of about 37 s-1 near residue 27 and about 42 s-1 near residue 126, with 128-131 elevated, against a 20-25 s-1 baseline; a lead for a dispersion measurement, not an exchange claim. |
| Exchange rate kex | not measured (UBE2G1-J4): the 2015 study reports no exchange term |
| Minor-state population pB | not measured (UBE2G1-J4) |
| Exchange regime | Not measured (UBE2G1-J4). No kex and no Delta-omega are printed, so no regime can be computed. |

Fallback statement: No apo alternate-state annotation is possible for UBE2G1: its relaxation data show only faster local motion in the acidic loop 97-109 and at the termini, with no exchange analysis (doi:10.1186/s40543-015-0068-z), and backside binding of an engineered ubiquitin variant leaves its crystal backbone almost unchanged (doi:10.1016/j.jmb.2019.09.024).

## Matching structures

What the papers relate to the states:

- **2AWF**: Apo UBE2G1 crystal (residues 8-160 plus tag), the reference for the UbV.G1.1-bound 6D68 superposition (RMSD 0.66 Å, 'virtually no differences'). A static ground-state structure, not a minor state.

## Other conditions (not the reference state)

- Free full-length UBE2G1, 30 °C, pH 7.0, 50 mM HEPES, 100 mM NaCl, 5 mM DTT, 0.8 mM, 800 MHz (2015 study, full text): unknown. Acidic loop 97-109 and termini more flexible, tau_c roughly 12-14 ns, no exchange term fitted (UBE2G1-J3, J4).
- Same protein at 25 °C and 900 MHz (TROSY assignments): the table gaps are proline and glycine chemistry, not exchange (UBE2G1-J6).
- UbV.G1.1-bound full-length UBE2G1 (6D68, 2:2 strand-exchanged complex), crystal at 20 °C, pH 8.0: backbone RMSD 0.66 A to apo 2AWF; static, no rate (UBE2G1-J2, UBE2G1-r4).
- Ubiquitin K48R oxyester conjugates of wild-type and Y102G/Y104G Ube2g1: NMR implicates the acidic loop in donor-ubiquitin binding; abstract only, no exchange parameters (UBE2G1-J1, UBE2G1-r1).
- E1 charging and discharge assays of wild type and S26R with UbV.G1.1 (30 °C, pH 7.5, HEPES, Mg/ATP; discharge with EDTA and apyrase): product kinetics, not conformational exchange; not judged (UBE2G1-r5 to UBE2G1-r8).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| UBE2G1-r1 | [Differential ubiquitin binding by the acidic loops of Ube2g1 and…](https://doi.org/10.1074/jbc.m114.624809) | other | Donor-ubiquitin interaction with acidic loop; target motion not established | abstract_only |
| UBE2G1-r4 | [Structural and Functional Analysis of Ubiquitin-based Inhibitors…](https://doi.org/10.1016/j.jmb.2019.09.024) | pdb_structure_comparison | Near-identical crystallographic backbone conformations; temporal motion not measured | full_text |
| UBE2G1-UBE2G1_20261020224441-r1 | [Comparative studies on manual and automatic backbone chemical shift…](https://doi.org/10.1186/s40543-015-0068-z) | nmr_spin_relaxation | Enhanced local backbone flexibility of the acidic loop and terminal regions; spin relaxation is sensitive to fast internal motion and… | full_text |
| UBE2G1-UBE2G1_20261020224441-r2 | [Comparative studies on manual and automatic backbone chemical shift…](https://doi.org/10.1186/s40543-015-0068-z) | other | Unassigned resonances; an additional conformational-exchange process is not established. | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `UBE2G1`.

## Caveats

Call stays unknown after the 2015 NMR paper (doi:10.1186/s40543-015-0068-z) was read in full on 2026-10-20. That paper supplies what the RelaxDB card was missing, an R1/R2/NOE set on free full-length UBE2G1 at 800 MHz and 30 °C, but it fits no exchange term and runs no dispersion experiment, so there is no author-reported Rex for the single-field Rex rule to act on and the us-ms window stays a search gap rather than a negative result. Its protein is the entry sequence plus two cloning residues (G-2, S-1) left by GST cleavage, and it is treated here as the entry construct. All relaxation values are read from Figure 3, a plot; the uncommented R2 outliers near residues 27 and 126 are recorded as a lead and are not counted as exchange. The protein runs at an apparent 25 kDa against a 20 kDa sequence mass, with no quantitative test for oligomerisation. The RelaxDB card still carries no BMRB id, so the identification is by matching conditions and content, not by accession. Ube2r1 rows (UBE2G1-r2, UBE2G1-r3) describe a paralog and were not used; the 2015 JBC paper remains an abstract.

## Open questions

- The 2015 assignment paper (doi:10.1186/s40543-015-0068-z) measures 800 MHz R1, R2 and NOE at 30 °C on full-length Ube2g1 and matches the entry's relaxation set; can it be confirmed as the RelaxDB source, since the card carries no BMRB id?
- Its Figure 3 shows uncommented R2 values of about 37 s-1 near residue 27 and about 42 s-1 near residue 126 against a 20-25 s-1 baseline: should these be flagged as candidate exchange sites for a dispersion measurement, or does the RelaxDB label already use them?

Judgments: UBE2G1-J1, UBE2G1-J2, UBE2G1-J3, UBE2G1-J4, UBE2G1-J5, UBE2G1-J6 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
