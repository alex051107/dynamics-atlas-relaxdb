# Escherichia coli ribonuclease HI

RelaxDB entry `RNASEHI` · set RelaxDB-133 · Escherichia coli ribonuclease HI (UniProt P0A7Y4), wild-type 155-residue sequence with C13, C63, C133 (1RCH:A); no BMRB id on the input card

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** cannot tell. The reference-state source (1995, full text) detects exchange only as a single-field model-free Δex term and states no exchange regime, prints no kex or Δω and shows no second peak set (RNASEHI-J52); the authors speak of 'exchange in the millisecond time scale' as the generic window of the Δex term. The 2019 methyl analysis of the cysteine-free handle exchange assumes the fast limit and the 2026 Rex comes from a B0-squared fit (RNASEHI-J47, J18), which would give 'does not' if those constructs counted; the only exchange-broadening regime statement concerns W85 of the Thermus homolog (RNASEHI-J14).

Reference state: in the RelaxDB source sample (free WT, 27 °C, pH 5.5, acetate, 600 MHz) 21 backbone amides need a model-free exchange term, concentrated in helices I (M50, A51, A52, A55, L56, L59) and IV (V101, D102, D103, W104, L107, A109, A110, L111) with I78, I82, W90 (2.61 Hz, largest), K91, N100, W118 and E135; mean Δex 0.71 Hz; the authors read it as millisecond exchange and a possibly cooperative motion of the two adjacent helices, with no rate, population or minor-state structure (RNASEHI-J52, E-r2). Under the single-field Rex rule of 2026-10-20 this is exchange detected in the reference state without a population, so the call is 'possible'. Supporting, other construct: the handle-region exchange in cysteine-free RNase HI* (V98, V101, L103 methyls broadened at 283-310 K; backbone Rex above 1 s-1 at 40 amides with G77 4.00 ± 0.38 s-1 at 900 MHz; RNASEHI-J47, J18) and the 1998 helix-I exchange abstract (J42). Solution RDCs and the V101 rotamer population fit open/closed averaging of the handle, and MD samples both handle states (RNASEHI-J11, J10).

## The free protein (reference state)

Free wild-type E. coli RNase HI (entry sequence, Cys-containing), no Mg2+ or nucleic acid. The RelaxDB source sample (doi:10.1021/bi00020a003, full text): about 1 mM 15N protein, 27 °C, pH 5.5, 100 mM deuterated sodium acetate, 600 MHz, single field (RNASEHI-J38, J51, J52). The other us-ms evidence is at 14.1 T, 283-310 K, pH 5.5 (2019 methyl study, cysteine-free) and from a multifield backbone reanalysis without restated conditions (2026, cysteine-free data set).

| | |
|---|---|
| Where (residues) | Reference state (1995, single-field Δex): M50, A51, A52, A55, L56, L59, I78, I82, W90, K91, N100, V101, D102, D103 (entry L103), W104, L107, A109, A110, L111, W118, E135 (RNASEHI-J52). Cysteine-free handle region: V98, V101, L103 methyls at all three temperatures, I78 and I82 at 283 K (RNASEHI-J47); G77 and 39 further amides with Rex above 1 s-1, figure only (RNASEHI-J18); helix I, no list (RNASEHI-J42, abstract); RDC probes W85, T92, V101 (RNASEHI-J11); simulated glycine-rich G15/N16 minor state (J9, MD only) |
| Exchange rate kex | not measured in the reference state: the 1995 paper gives Δex (Hz, line-width contribution) only, mean 0.71 Hz over 20 residues and 2.61 Hz at W90 (RNASEHI-J52). Other constructs: the 2019 study gives apparent activation energies of 45.4 ± 1.6 kJ/mol (V98), 23.7 ± 1.9 kJ/mol (V101) and 21.4 ± 3.0 kJ/mol (L103) from the temperature dependence of Delta-Rex under a fast-limit assumption, not kex (RNASEHI-J47); the 2026 reanalysis gives Rex, with G77 at 4.00 ± 0.38 s-1 at 900 MHz (RNASEHI-J18). |
| Minor-state population pB | not measured in the reference state (RNASEHI-J52); the fast-limit treatment of the cysteine-free handle exchange assumes a dominant state (RNASEHI-J47); V101 trans chi1 rotamer about 10% in WT and above 30% in V98A is a rotamer population, not the closed-handle population (RNASEHI-J11, RNASEHI-J12) |
| Exchange regime | Not stated for the reference state: single-field Δex with no Δω (RNASEHI-J52). Fast limit assumed by the 2019 analysis of cysteine-free protein (p1 much greater than p2) and implied by the B0-squared Rex fit of 2026; not independently determined. In the T. thermophilus homolog the W85 RDC could not be measured because of exchange broadening (RNASEHI-J14, homolog). |

Fallback statement: May have an alternate conformation involving helices I (N44-A58) and IV (V101-A110), which carry single-field exchange terms in the free wild-type enzyme at 27 °C, pH 5.5 (mean Δex 0.71 Hz, W90 2.61 Hz; doi:10.1021/bi00020a003), and of the substrate-binding handle region (residues 81-101, closed versus open) measured in cysteine-free RNase HI*: methyl exchange broadening at V98, V101 and L103 across 283-310 K (doi:10.1007/s10858-019-00240-w), backbone Rex at G77 and 39 further amides (doi:10.1021/jacs.6c05843), and solution RDCs and valine rotamer populations interpreted with MD (doi:10.1021/acs.biochem.0c00500); no rate or population measured.

## Matching structures

## Other conditions (not the reference state)

- Free WT (entry sequence), 27 °C, pH 5.5, 100 mM acetate, 600 MHz single field (1995 RelaxDB source, full text): possible. Model-free Δex at 21 amides in helices I and IV, W90 largest; fast motion at the termini and five loops, rigid secondary structure (RNASEHI-J52, J38, J51; E-r1, E-r2).
- Free cysteine-free RNase HI* (construct not stated in the 2019 paper; same pAED4 line), 14.1 T, pH 5.5, 283/300/310 K (2019 methyl Hahn echo): handle methyls V98, V101, L103 exchange-broadened at all temperatures, I78/I82 at 283 K; apparent activation energies only; fast-limit assumed (RNASEHI-J47, RNASEHI-RNASEHI_20261020150655-r13 to r16).
- Free cysteine-free RNase HI* (stated for the 2025 data set), 500/700/900 MHz backbone reanalysis, conditions not restated (2026): Rex above 1 s-1 at 40 amides, G77 4.00 ± 0.38 s-1 (RNASEHI-J18, RNASEHI-RNASEHI_20261020150655-r19).
- Free WT, 1998 abstract: exchange contribution in helix I, reduced in the quintuple mutant; the mutant gains exchange at the protrusion junction (RNASEHI-J42, J43).
- Mg2+-bound WT, pD 6.2: possible. Active-site side chains broaden by 13C R1rho in two groups (N44, E57, D102 and D10, E48, D70, D134), but the broadening tracks the apo-to-Mg shift difference and cannot be separated from Mg2+ binding exchange (RNASEHI-J20).
- Cysteine-free RNase HI*, about 298 K, pH 5.5 acetate: possible. Model-free Rex at the example residues V54 and G77, no dispersion or rate (RNASEHI-J19).
- V98A mutant: handle shifted toward closed conformations (V101 trans rotamer above 30%), no rate (RNASEHI-J12, J13).
- Mg2+ and Zn2+ crystal forms: metal positions and H124 coordination differ between crystal forms (7VSA, 7VSC, 7VSD; 7VSB, 7VSE), static and without timescale (RNASEHI-J26, J27).
- Refolding from urea, cysteine-free protein: folding intermediates with phases of 120 mus and 3.1 ms, a 0.78 s-1 Icore-to-native step, and pulsed-labeling HX-MS protection of helix A before helix D; not native-state alternate states (RNASEHI-J21 to J23, J50).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| RNASEHI-r2 | [Side chain dynamics of carboxyl and carbonyl groups in the catalytic…](https://doi.org/10.1021/ja409479y) | nmr_exchange_broadening | Metal-coupled μs–ms exchange broadening | full_text |
| RNASEHI-r12 | [Conformational preferences underlying reduced activity of a…](https://doi.org/10.1016/j.jmb.2014.11.023) | md_simulation | Simulated loop and side-chain conformational ensembles | full_text |
| RNASEHI-r18 | [Quantifying the Relationship between Conformational Dynamics and…](https://doi.org/10.1021/acs.biochem.0c00500) | nmr_ensemble_restraints | Ensemble-averaged handle opening/closure | full_text |
| RNASEHI-r19 | [Quantifying the Relationship between Conformational Dynamics and…](https://doi.org/10.1021/acs.biochem.0c00500) | nmr_ensemble_restraints | Ensemble-averaged handle opening/closure | full_text |
| RNASEHI-r20 | [Quantifying the Relationship between Conformational Dynamics and…](https://doi.org/10.1021/acs.biochem.0c00500) | nmr_ensemble_restraints | Ensemble-averaged handle opening/closure | full_text |
| RNASEHI-r21 | [Quantifying the Relationship between Conformational Dynamics and…](https://doi.org/10.1021/acs.biochem.0c00500) | nmr_ensemble_restraints | Ensemble-averaged handle opening/closure | full_text |
| RNASEHI-r22 | [Quantifying the Relationship between Conformational Dynamics and…](https://doi.org/10.1021/acs.biochem.0c00500) | md_simulation | Simulated handle conformational distributions | full_text |
| RNASEHI-r23 | [Quantifying the Relationship between Conformational Dynamics and…](https://doi.org/10.1021/acs.biochem.0c00500) | md_simulation | Simulated handle conformational distributions | full_text |
| RNASEHI-r27 | [A steady-state approach for analysis of high-resolution relaxometry.](https://doi.org/10.1016/j.jmr.2025.107989) | nmr_exchange_broadening | Model-inferred chemical-exchange broadening | full_text |
| RNASEHI-r74 | [Non-native structure appears in microseconds during the folding of…](https://doi.org/10.1016/j.jmb.2014.10.003) | other | Nonequilibrium folding intermediates monitored by Trp fluorescence lifetime | full_text |
| RNASEHI-r78 | [Non-native structure appears in microseconds during the folding of…](https://doi.org/10.1016/j.jmb.2014.10.003) | other | Nonequilibrium folding intermediates monitored by Trp fluorescence lifetime | full_text |
| RNASEHI-r80 | [Pivotal role of a conserved histidine in Escherichia coli…](https://doi.org/10.1107/s2059798322000870) | pdb_structure_comparison | Metal-linked structural heterogeneity | full_text |
| RNASEHI-r81 | [Pivotal role of a conserved histidine in Escherichia coli…](https://doi.org/10.1107/s2059798322000870) | pdb_structure_comparison | Metal-linked structural heterogeneity | full_text |
| RNASEHI-r82 | [Pivotal role of a conserved histidine in Escherichia coli…](https://doi.org/10.1107/s2059798322000870) | pdb_structure_comparison | Metal-linked structural heterogeneity | full_text |
| RNASEHI-r83 | [Pivotal role of a conserved histidine in Escherichia coli…](https://doi.org/10.1107/s2059798322000870) | pdb_structure_comparison | Metal-linked structural heterogeneity | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `RNASEHI`.

## Caveats

Call set to possible on 2026-10-20 after the RelaxDB source paper (doi:10.1021/bi00020a003) was read in full: exchange is detected in the reference state (free WT, 27 °C, pH 5.5) as a single-field model-free Δex term at 21 amides, and under the single-field Rex rule decided that night (ledger/redraft_notes.json, _RULE_single_field_rex) author-reported Rex in the reference state counts as exchange detected without a population. Fixed caveat: single-field Rex can also come from anisotropic tumbling; a dispersion experiment would confirm. The 1995 analysis gives no kex, population, Δω or second peak set, so whether the exchanging state is slow enough for separate peaks is untested. The handle-region evidence with temperature dependence (2019, 2026) is from cysteine-free RNase HI* (the 2026 reanalysis uses the 2025 relaxometry data set, which its paper states is cysteine-free; the 2019 sample's construct is not stated) and stays other-construct support. The earlier 15N handle-exchange studies cited as refs 54-56 of the 2019 paper are still not in the evidence. The paper prints Ala131, Asp103, Tyr71, Asn43 and Asp92 where the entry has E131, L103, S71, T43, T92; kept as printed and mapped by number. Second-read adjudication B was used for r20, r21, r38-r42, r69 and r80; the PDF adjudication (ledger/adjudication_pdf_batch1.json) filled positions 131 and 103 in E-r1/E-r2 and resolved the duplicate position 43 in E-r3. Homolog and ancestral-folding rows are kept out of the call. The abstract-only rows of the 1995 paper (RNASEHI-RNASEHI_20261020150655-r1, r2) are superseded and no longer cited.

## Open questions

- Catalytic side-chain S2: NMR 0.64-0.75 at D10, E48, D70, D134 (pD 6.2) versus MD 0.76-0.85 (r1 versus r3); the authors attribute the gap to protonation averaging near the D10 pKa and force-field limits.
- The 2013 paper names N44 in the Mg2+ group-1 broadening set and N45 in the conservation text (r2 versus r1); kept as printed.
- Construct identity of the us-ms evidence: the 2019 methyl, 2024 JCTC and 2026 JACS articles (D-r9 to r19) are labelled 'target' in the evidence but never restate the cysteine content of the sample, while the same laboratory's 2018 methyl sample (r25) is called cysteine-free by the 2025 paper (r26); if these samples are RNase HI*, J18, J44, J45 and J47 become inference_from_mutant and the wt_apo_answer drops to the earlier 'not established'.
- Residue 71 in the 1995 abstract (D-r1): the abstract writes Asp70-Tyr71 while the entry sequence has S71 and Y73; both second readers flagged the row, the corrected row keeps Tyr71 as printed, and J38 maps D70 only.
- Residue letters in the 1995 paper: Ala131 and Asp103 (p. 6591, class lists; Glu131 on p. 6599), Tyr71 (flexible-loop text; Ser71 in the class III list) and Asn43/Asp92 (MD discussion) differ from the entry E131, L103, S71, T43, T92; the rows keep the printed letters and map by number (adjudication ledger/adjudication_pdf_batch1.json).
- Which sample is the RelaxDB RNASEHI R1/R2/NOE set, and are the Palmer-laboratory samples in the 2019 methyl-exchange, 2024 JCTC and 2026 JACS papers the Cys-containing wild type (the entry sequence) or the cysteine-free RNase HI*? The answer decides whether the us-ms handle exchange (J47, J18) counts as reference-state evidence.
- The 1995 source paper (full text) detects exchange only as a single-field model-free Δex term at 21 amides (helices I and IV, W90 largest), with no rate or population. Does single-field Rex count as us-ms exchange for the alternate-APO call (applied here as 'possible' with the anisotropic-tumbling caveat), and should the earlier 15N handle-exchange studies cited as refs 54-56 of the 2019 paper be added in full?

Judgments: RNASEHI-J9, RNASEHI-J10, RNASEHI-J11, RNASEHI-J12, RNASEHI-J13, RNASEHI-J14, RNASEHI-J18, RNASEHI-J19, RNASEHI-J20, RNASEHI-J21, RNASEHI-J23, RNASEHI-J26, RNASEHI-J27, RNASEHI-J42, RNASEHI-J43, RNASEHI-J47, RNASEHI-J50, RNASEHI-J38, RNASEHI-J51, RNASEHI-J52, RNASEHI-J53 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
