# Escherichia coli / Salmonella typhi thioredoxin-1 (TrxA; entry sequence UniProt P0AA29 without Met1

RelaxDB entry `TRX` · set RelaxDB-133 · Escherichia coli / Salmonella typhi thioredoxin-1 (TrxA; entry sequence UniProt P0AA29 without Met1, identical to E. coli P0AA25), wild type, 108 residues

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** cannot tell for NMR. The 1993 source states no exchange regime, prints no kex, population or Δω and reports no second peak set for either redox form; exchange is single-field model-free Rex above 1.5 Hz (reduced: G33, I38, I45, R73, G74, I75, W31 indole; oxidized: W31 indole, I45), which the authors call microsecond-millisecond mobility (TRX-J15, J51). The oxidized-form active-site millisecond motion of 1996 is a transient conformation in an abstract (TRX-J17). The 1989 urea-gradient abstract states slow (minute-scale) interconversion of cis and trans P76 forms in folded reduced thioredoxin with less than a few percent trans, but it is electrophoresis read from an abstract, not an NMR peak count, and the 1993 authors exclude P76 isomerisation as the source of the 73-75 broadening (TRX-J29).

Possible for both redox forms under the single-field Rex rule of 2026-10-20: exchange is detected in the reference state without a population. Reduced form (dithiol): the 1993 full text reports exchange broadening significantly above 1.5 Hz at G33, I38, I45, R73, G74, I75 and the W31 indole, read as microsecond-millisecond mobility propagated from I75 to R73-G74 and as greater flexibility around the active site in the reduced protein, explicitly not P76 cis-trans isomerisation (TRX-J15; E-r4); no kex, population or Δω. Oxidized form (C32-C35 disulfide): the same study finds broadening above 1.5 Hz only at the W31 indole and I45 (TRX-J51; E-r3) and none at R73-I75 (TRX-J16, no_evidence_in_window), while the 1996 13C/15N relaxation abstract reports millisecond motion at nuclei around the active-site disulfide interpreted as a strained transient disulfide conformation (TRX-J17; 101601-r5, abstract only). No CPMG, R1rho or CEST measurement exists for either form (TRX-J21). Supporting but not reference-state: the reassembled 1-73/74-108 solid-state construct loses G21, P40, T54 and R73 on cooling to 238 K (TRX-J12); the E101G crystal refines a 50/50 alternate backbone over 10-25, 77-91 and 95-107 (TRX-J35); wild-type MD makes persistent transitions at 13-18 (TRX-J38); native-state HX of oxidized wild type finds no partially unfolded form below global unfolding at 24 probes (TRX-J30).

## The free protein (reference state)

Wild-type thioredoxin-1 as deposited (108-residue mature sequence), free, no ligand. Redox form is a sample state: the RelaxDB card gives no BMRB id, no redox state and links only the oxidized human-E. coli chimera 1M7T, so the deposited form is unknown; the call is given for each form. The key solution study (Stone et al. 1993, doi:10.1021/bi00053a007, now full text) measured both forms at 308 K on a 500 MHz spectrometer (single field, 1.0 ms CPMG spacing); its main text does not state protein concentration, buffer, pH or solvent isotope fraction (TRX-J1, J2, J15, J16, J51 marked is_wt_apo).

| | |
|---|---|
| Where (residues) | Reduced: W31 indole, G33, I38, I45, R73, G74, I75 (Rex > 1.5 Hz; TRX-J15). Oxidized: W31 indole, I45 (TRX-J51); R73-I75 quiet (TRX-J16); G33 not measurable (TRX-J52). Oxidized 1996: nuclei around the active-site disulfide C32-C35, not enumerated in the abstract (TRX-J17). Solid-state reassembly (other construct, 238 K): G21, P40, T54, R73 lost; A19, D20, G21, R73 survive the T2' filter (TRX-J12). |
| Exchange rate kex | not reported for either redox form; Rex above 1.5 Hz (values figure-only, Figure 3E/F; W31 indole 4.0 ± 0.2 Hz oxidized and 2.8 ± 0.1 Hz reduced, W28 0.44 ± 0.02 Hz oxidized, Table I) at the sites listed, from single-field model-free fitting with a 1.0 ms CPMG spacing (TRX-J15, J51); the 1996 oxidized active-site millisecond motion is stated without values (TRX-J17, abstract) |
| Minor-state population pB | not reported for either redox form (TRX-J15, J51, J17) |
| Exchange regime | not stated in the 1993 full text; no Δω printed; the authors speak of microsecond-to-millisecond mobility and exclude P76 cis-trans isomerisation on timescale grounds. The oxidized-form 73-75 result is 'no significant exchange broadening' by the same Rex analysis (TRX-J16). |

Fallback statement: May have an alternate apo conformation around the active site: in the reduced (dithiol) form single-field 15N exchange broadening above 1.5 Hz at G33, I38, I45, R73, G74, I75 and the W31 indole at 308 K, and in the oxidized form at the W31 indole and I45 (doi:10.1021/bi00053a007, full text); in the oxidized form also millisecond motion around the C32-C35 disulfide interpreted as a strained transient disulfide conformation (doi:10.1021/ja960877r, abstract only). The alternative conformers of the wild-type crystal 2TRX and the E101G crystal 5HR0 are candidates without a rate or population.

## Matching structures

What the papers relate to the states:

- **2TRX**: Oxidized wild-type crystal (1.68 Å) with ten unnamed residues in two alternative conformations and differences between the two independent molecules that may reflect crystal contacts; residues 29-37 form a surface protrusion. A crystal alternative, not a solved minor state.
- **5HR0**: E101G mutant crystal: chain B refines as two complete backbone conformers (Ba/Bb, 50% each) over D10-V25, T77-V91 and S95-L107, read by the authors as members of the native-like ensemble. Mutant, Cu(II)/ethanol crystal, no solution population; not tied to the 73-75 or active-site exchange.
- **1M7T**: Oxidized human-E. coli chimera linked by the RelaxDB card; its 15N relaxation gives S2 0.88 with mobile loops 72-74 and 92-94 (chimera numbering). A homolog construct, not the entry sequence and not a minor state.

## Other conditions (not the reference state)

- Reassembled 1-73/74-108 E. coli thioredoxin, hydrated PEG-4000 precipitate, 288 K to 238 K, MAS NMR: possible. Cooling removes G21, P40, T54 and R73 and broadens most other peaks (10-100 microsecond interference, static heterogeneity not excluded); G21 shows CSA averaging faster than about 100 microseconds (TRX-J11, TRX-J12; 101601-r8, r9, r10).
- Reassembled construct by DARR below -15 °C: intermediate-timescale motion reported without residues (TRX-J13; 101601-r31, abstract).
- Fragment complex TRX1-93 + TRX94-108: elevated R2 at 43-50 and 74-89 attributed to peptide-modulated exchange, no rate (TRX-J18; 101601-r19, abstract).
- L78K core mutant: greater exchange contribution than wild type, no values (TRX-J19; 101601-r34, abstract).
- Oxidized wild type, 25 °C, pH 7, 30 mM phosphate, 0.1 M KCl, native-state HX: no partially unfolded form at 24 probes; delta-G of opening 4.7-9.9 kcal/mol (TRX-J30; 101601-r28, r29).
- Wild type reduced, 20 °C, pH 7.0, Tris, 1 mM DTT, 600 MHz: R1/R2/NOE profile figure only, no exchange analysis (TRX-J9; TRX-r40).
- Wild type, both redox forms, urea-gradient electrophoresis at 2 and 25 °C: two compact forms assigned to cis/trans I75-P76; in the folded reduced form they interconvert slowly on the minute time scale with less than a few percent trans without urea, the oxidized form is essentially all cis (TRX-J29; 101601-r21, r22, r27, abstracts; not NMR, no rate constant). The 1993 relaxation paper states that the 73-75 broadening cannot be P76 isomerisation because that would be much slower.

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| TRX-TRX_20261020101601-r5 | [Dynamical Mapping of E. coli Thioredoxin via 13C NMR Relaxation…](https://doi.org/10.1021/ja960877r) | nmr_exchange_broadening | Millisecond motion around active site | abstract_only |
| TRX-TRX_20261020101601-r8 | [Dynamics of Reassembled Thioredoxin Studied by Magic Angle Spinning…](https://doi.org/10.1021/ja9037802) | other | Motional averaging of backbone chemical shift anisotropy | full_text |
| TRX-TRX_20261020101601-r9 | [Dynamics of Reassembled Thioredoxin Studied by Magic Angle Spinning…](https://doi.org/10.1021/ja9037802) | nmr_spin_relaxation | Submillisecond backbone mobility selected by proton transverse dephasing | full_text |
| TRX-TRX_20261020101601-r10 | [Dynamics of Reassembled Thioredoxin Studied by Magic Angle Spinning…](https://doi.org/10.1021/ja9037802) | nmr_exchange_broadening | Intermediate-timescale motion interfering with MAS/decoupling | full_text |
| TRX-TRX_20261020101601-r19 | [Recognition between a short unstructured peptide and a partially…](https://doi.org/10.1002/prot.24043) | nmr_exchange_broadening | Possible peptide-modulated interfacial exchange | abstract_only |
| TRX-TRX_20261020101601-r21 | [Escherichia coli thioredoxin folds into two compact forms of…](https://doi.org/10.1021/bi00434a015) | other | Slow folding-coupled proline peptide isomerization | abstract_only |
| TRX-TRX_20261020101601-r22 | [Escherichia coli thioredoxin folds into two compact forms of…](https://doi.org/10.1021/bi00434a015) | other | Slow folding-coupled proline peptide isomerization | abstract_only |
| TRX-TRX_20261020101601-r27 | [Conformational transitions of thioredoxin in guanidine hydrochloride.](https://doi.org/10.1021/bi00317a003) | other | Multiphase refolding and putative proline isomerization | abstract_only |
| TRX-TRX_20261020101601-r28 | [Folding subdomains of thioredoxin characterized by native-state…](https://doi.org/10.1110/ps.0239503) | other | Local opening and global unfolding sampled under equilibrium native conditions | full_text |
| TRX-TRX_20261020101601-r29 | [Folding subdomains of thioredoxin characterized by native-state…](https://doi.org/10.1110/ps.0239503) | other | Opening equilibrium inferred under EX2 exchange | full_text |
| TRX-TRX_20261020101601-r31 | [Magic angle spinning NMR spectroscopy of thioredoxin reassemblies.](https://doi.org/10.1002/mrc.2092) | nmr_exchange_broadening | Intermediate-timescale motions influencing DARR signals | abstract_only |
| TRX-TRX_20261020101601-r34 | [NMR studies of structure, hydrogen exchange, and main-chain dynamics…](https://doi.org/10.1002/pro.5560051218) | nmr_exchange_broadening | Increased slow exchange | abstract_only |
| TRX-r36 | [Structural variability of E. coli thioredoxin captured in the…](https://doi.org/10.1038/srep42343) | pdb_structure_comparison | Crystallographic backbone conformational heterogeneity | full_text |
| TRX-r40 | [Structural variability of E. coli thioredoxin captured in the…](https://doi.org/10.1038/srep42343) | nmr_spin_relaxation | No detectable mutant-induced change in fast backbone dynamics | full_text |
| TRX-r41 | [Structural variability of E. coli thioredoxin captured in the…](https://doi.org/10.1038/srep42343) | md_simulation | Backbone fluctuations and local conformational transitions | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `TRX`.

## Caveats

Call raised from unknown to possible on 2026-10-20 after the RelaxDB source paper (doi:10.1021/bi00053a007, Stone et al. 1993) was read in full: exchange is detected in the reference state in both redox forms as single-field model-free Rex above 1.5 Hz, and under the single-field Rex rule decided that night (ledger/redraft_notes.json, _RULE_single_field_rex) this counts as exchange detected without a population. Fixed caveat: single-field Rex can also come from anisotropic tumbling; a dispersion experiment would confirm. The two forms give different site lists (reduced: G33, I38, I45, R73-I75, W31; oxidized: W31, I45 only), and the RelaxDB card does not say which form was deposited, so the call is 'possible' for each form and the atlas needs the deposited form. The 1993 main text omits protein concentration, buffer, pH and solvent, and its Rex values are figure-only except the W31 indole; the Monte Carlo uncertainties may be underestimated. LeMaster 1996 (oxidized active-site ms motion) remains abstract-only. The solid-state evidence is from a cleaved reassembly in a PEG precipitate at 238 K, the crystal alternatives come from a Cu(II)-containing wild-type crystal and an E101G mutant crystal, and the MD transitions are simulation only. No dispersion experiment was found, and the structured dispersion searches were restricted to Salmonella typhi terms. The abstract-only rows TRX-TRX_20261020101601-r1, r2, r3 are superseded and no longer cited. Built from cases V6_r6_TRX_20261020101601, V6_r6_TRX_20261020104151, V6_r6_TRX_20261020105420, S6_r6_TRX_20261020155442, S6_r6_TRX_20261020160402 and S6_r6_TRX_20261020212514.

## Open questions

- Redox form of the RelaxDB sample is unknown from the card; the us-ms answer differs between reduced (Rex at G33, I38, I45, R73-I75, W31) and oxidized (W31 and I45 only, none at 73-75; plus the abstract-only 1996 active-site ms motion), so J15/J51/J16/J17 are kept as separate sample states rather than a conflict.
- Identity: the card's PDB link 1M7T is the human-E. coli chimera (human 1-66, E. coli 67-106), while the entry sequence is full-length E. coli/S. typhi TrxA; the chimera relaxation (J8) is treated as homolog inference.
- Which sample produced the RelaxDB TRX relaxation set: reduced or oxidized E. coli thioredoxin (the 1993 Stone et al. data set, 308 K, 500 MHz, which measured both), or the oxidized 1M7T chimera that the card links? The us-ms answer differs between the two forms.
- The 1993 paper (now full text) detects exchange only as single-field model-free Rex above 1.5 Hz (reduced: G33, I38, I45, R73-I75, W31 indole; oxidized: W31, I45), with no rate or population. Does single-field Rex count as us-ms exchange for the alternate-APO call (applied here as 'possible' with the anisotropic-tumbling caveat), and can the full text of LeMaster 1996 (10.1021/ja960877r) still be obtained for the oxidized active-site motion?

Judgments: TRX-J9, TRX-J11, TRX-J12, TRX-J13, TRX-J15, TRX-J16, TRX-J17, TRX-J18, TRX-J19, TRX-J21, TRX-J29, TRX-J30, TRX-J34, TRX-J35, TRX-J38, TRX-J1, TRX-J2, TRX-J51, TRX-J52 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
