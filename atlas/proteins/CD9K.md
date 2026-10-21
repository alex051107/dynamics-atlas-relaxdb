# Bovine calbindin D9k (protein S100-G

RelaxDB entry `CD9K` · set RelaxDB-133 · Bovine calbindin D9k (protein S100-G, UniProt P02633), 75 residues; the entry sequence is the P43G variant

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** cannot tell. For apo P43G the source states no exchange regime, prints no kex or Δω and shows no second peak set; exchange appears only as single-field model-free Rex at 14 amides, and the authors say further kinetic analysis is not possible (CD9K-J13, E-r4). P43G exists as a single isoform, so the two peak sets in slow exchange (3:1, 2D exchange) of native Pro43 calbindin in the Ca2+-loaded state (CD9K-J1; CD9K-r4, r9) do not exist in the entry construct.

Reference state: in the RelaxDB source sample (apo P43G, 300 K, pH 6.0, 11.74 T) 14 backbone amides need an exchange term, largest at A15 (2.39 s-1) and D19 (1.32 s-1) in the unoccupied site I loop and at K55 and V61 (1.11 s-1) in loop II, with E17 0.89, I73 0.65 and the rest 0.32-0.56 s-1; the authors attribute it to intrinsic conformational heterogeneity, excluding exchange with the below-0.5% Ca2+-loaded contaminant (koff below 20 s-1), and give no rate, population or substate structure (CD9K-J13, E-r4). Under the single-field Rex rule of 2026-10-20 this is exchange detected in the reference state without a population, so the call is 'possible'. Context from the same paper: with one Cd2+ in site II the unoccupied loop I broadens much more strongly (A14, K16, G18, D19, Q22; E17 and S24 lost), read as more frequent sampling of loop-I substates (CD9K-J15, E-r5), and the Ca2+-loaded protein shows no significant exchange (42 terms at or below 0.33 s-1; CD9K-J37, E-r6). No dispersion, R1rho or CEST study of apo P43G exists in the evidence; the millisecond R1rho exchange is reported only for Ca2+-loaded P43M (CD9K-J27, abstract).

## The free protein (reference state)

Ca2+-free (apo) calbindin D9k in the entry construct P43G (the entry sequence carries G43), as measured in the RelaxDB source paper (doi:10.1021/bi00088a039, full text): 4 mM uniformly 15N P43G, 300 K, pH 6.0 (HCl, no buffer), 95% H2O/5% D2O, 11.74 T, single field (CD9K-J12, J13 marked is_wt_apo). The paper states that all its studies use P43G.

| | |
|---|---|
| Where (residues) | Apo P43G (Table I Rex, s-1): G8 0.48, A14 0.44, A15 2.39, K16 0.40, E17 0.89, D19 1.32, L30 0.33, E35 0.56, E51 0.56, D54 0.33, K55 1.11, V61 1.11, V68 0.32, I73 0.65; Q75 R2 excluded for exchange (CD9K-J13). (Cd2+)1 P43G: A14, K16, G18, D19, Q22 substantial; E17, S24 undetected; A15, L23 unfittable; 21 numeric entries in all (CD9K-J15). |
| Exchange rate kex | not reported for apo P43G; Rex only, 0.32-2.39 s-1 at 14 residues (CD9K-J13, E-r4). The authors' 1 ms CPMG spacing argument (rates comparable to 2000 s-1) is an instrumental sensitivity statement, not a fitted rate. |
| Minor-state population pB | not reported for apo P43G (CD9K-J13); the only population-like numbers are contamination bounds (Ca2+-loaded below 0.5% in apo; Cd2-loaded fraction below 0.05 in (Cd2+)1). |
| Exchange regime | Not stated for apo P43G (CD9K-J13). No Δω printed. The authors state that the chemical shifts of the discrete substates cannot be determined, which is why no kinetic analysis follows. |

Fallback statement: May have alternate conformations of the unoccupied site I loop (A14-D19) and of loop II (D54-V61) in apo P43G calbindin D9k: single-field 15N model-free exchange terms of up to 2.39 s-1 (A15) at 300 K, pH 6.0, attributed by the authors to intrinsic conformational heterogeneity (doi:10.1021/bi00088a039); no rate, population or substate structure.

## Matching structures

## Other conditions (not the reference state)

- (Cd2+)1 P43G, 300 K, pH 6.0, 11.74 T (RelaxDB source paper, full text): possible. Strong single-field exchange broadening in the unoccupied site I loop (A14, K16, G18, D19, Q22; E17, S24 lost; A15, L23 unfittable), assigned to substates of the singly loaded protein rather than Cd2+ exchange (Cd2-loaded fraction below 0.05, koff 700 s-1, Rex uncorrelated with shift difference); no rate or population (CD9K-J15, E-r5).
- (Ca2+)2 P43G, single-field reanalysis of the 1992 data: no second peak set and no significant exchange, 42 fitted Rex terms all at or below 0.33 s-1 (CD9K-J37, E-r6; CD9K-J6 abstract).
- Native Pro43, Ca2+-loaded: yes for a literal two-peak state. Two folded forms, 3:1 trans:cis at the Gly42-Pro43 bond, interconvert slowly (cis-to-trans 0.2 s-1 at 25 °C, extrapolated from line shapes); abstracts only (CD9K-J1; CD9K-r4, CD9K-r9). This is proline isomerism in the linker, absent from the entry construct.
- Native Pro43, apo: cannot tell. The apo P43G assignment abstract says the wild type was set aside for conformational heterogeneity, but no row shows apo peak sets or a rate (CD9K-J7, CD9K-r11).
- P43M, dicalcium and Ca/La: possible lead only. Millisecond equilibria at S38, G42-S44, L46 and G18, D19 by R1rho, lost in 2 M GdmHCl (CD9K-J27 to CD9K-J29, abstracts).
- P43M and Q22N/P43M under crystallization conditions: domain-swapped dimers form over about 30 days, an intermolecular kinetic trap, not a monomer state (CD9K-J31).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| CD9K-CD9K_20261020211504-r1 | [Effects of ion binding on the backbone dynamics of calbindin D9k…](https://doi.org/10.1021/bi00088a039) | nmr_spin_relaxation | Picosecond-to-nanosecond backbone N-H fluctuations; enhanced loop-II and linker flexibility | full_text |
| CD9K-CD9K_20261020211504-r2 | [Effects of ion binding on the backbone dynamics of calbindin D9k…](https://doi.org/10.1021/bi00088a039) | nmr_spin_relaxation | Picosecond-to-nanosecond backbone motion with reduced loop-II fluctuation amplitudes relative to apo | full_text |
| CD9K-CD9K_20261020211504-r3 | [Effects of ion binding on the backbone dynamics of calbindin D9k…](https://doi.org/10.1021/bi00088a039) | nmr_spin_relaxation | Picosecond-to-nanosecond backbone flexibility; linker and terminal motions; loop-II restriction compared with apo | full_text |
| CD9K-CD9K_20261020211504-r4 | [Effects of ion binding on the backbone dynamics of calbindin D9k…](https://doi.org/10.1021/bi00088a039) | nmr_exchange_broadening | Slow conformational exchange contributing to transverse relaxation; atomic substates unidentified | full_text |
| CD9K-CD9K_20261020211504-r5 | [Effects of ion binding on the backbone dynamics of calbindin D9k…](https://doi.org/10.1021/bi00088a039) | nmr_exchange_broadening | Slow conformational exchange concentrated near unoccupied N-terminal binding site | full_text |
| CD9K-CD9K_20261020211504-r6 | [Effects of ion binding on the backbone dynamics of calbindin D9k…](https://doi.org/10.1021/bi00088a039) | nmr_exchange_broadening | No substantial slow-exchange contribution resolved under the analyzed conditions | full_text |
| CD9K-r4 | [Proline isomerism leads to multiple folded conformations of…](https://doi.org/10.1073/pnas.86.7.2195) | other | Proline cis-trans isomerization | abstract_only |
| CD9K-r5 | [Proline isomerism leads to multiple folded conformations of…](https://doi.org/10.1073/pnas.86.7.2195) | other | Test for resolved proline-related conformational heterogeneity | abstract_only |
| CD9K-r9 | [The rate and structural consequences of proline cis-trans…](https://doi.org/10.1021/bi00470a020) | nmr_exchange_broadening | Proline cis-trans exchange | abstract_only |
| CD9K-r10 | [The rate and structural consequences of proline cis-trans…](https://doi.org/10.1021/bi00470a020) | other | Resolved isoform comparison | abstract_only |
| CD9K-r11 | [1H NMR resonance assignments, secondary structure, and global fold…](https://doi.org/10.1021/bi00476a016) | other | Amide-solvent exchange and aromatic side-chain motion | abstract_only |
| CD9K-r22 | [A 15N NMR mobility study on the dicalcium P43M calbindin D9k and its…](https://doi.org/10.1021/bi015945n) | nmr_relaxation_dispersion | Slow conformational exchange detected with R1rho and transverse relaxation | abstract_only |
| CD9K-r23 | [A 15N NMR mobility study on the dicalcium P43M calbindin D9k and its…](https://doi.org/10.1021/bi015945n) | nmr_relaxation_dispersion | Slow conformational exchange detected with R1rho and transverse relaxation | abstract_only |
| CD9K-r39 | [Monitoring the early steps of unfolding of dicalcium and…](https://doi.org/10.1021/bi034638+) | nmr_spin_relaxation | Denaturant-dependent packing and transverse-relaxation changes | abstract_only |
| CD9K-r40 | [Monitoring the early steps of unfolding of dicalcium and…](https://doi.org/10.1021/bi034638+) | nmr_spin_relaxation | Denaturant-dependent packing and transverse-relaxation changes | abstract_only |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `CD9K`.

## Caveats

Call raised from unknown to possible on 2026-10-20 after the RelaxDB source paper (doi:10.1021/bi00088a039) was read in full: exchange is detected in the reference state (apo P43G, 300 K, pH 6.0) as single-field model-free Rex at 14 amides, and under the single-field Rex rule decided that night (ledger/redraft_notes.json, _RULE_single_field_rex) this counts as exchange detected without a population. Fixed caveat: single-field Rex can also come from anisotropic tumbling; a dispersion experiment would confirm. The construct question is settled (P43G for every sample in the paper), and P43G removes the Pro43 cis/trans two-isoform spectra, so no literal two-peak state exists in the entry construct. The apo sample has no buffer solute (pH set with HCl) and the Ca2+-loaded data are a reanalysis of a 1992 sample whose composition is not restated. Deamidation at N56 during urea preparation can create extra species that mimic a second conformer (CD9K-J26). The abstract-only rows CD9K-r2 and CD9K-r3 are superseded and no longer cited. the NMR collaborator is asked whether the RelaxDB set is the apo, (Cd2+)1 or Ca2+-loaded P43G sample.

## Open questions

- Resolved on 2026-10-20: the construct of the apo and (Cd2+)1 relaxation study is P43G (p. 9833 'All current studies are carried out on the P43G mutant'; Table I title), so J12-J15 now carry the entry construct; the abstract-only rows r2 and r3 ('variant not stated') are superseded.
- Native apo heterogeneity: the apo P43G assignment abstract (r11 source) says the wild type was not assigned because of conformational heterogeneity, which suggests cis/trans peak doubling also in the apo native protein, but no row shows apo peak sets or a rate.
- Linker response to ions: the one-field reanalysis of the Ca2+-saturated data gives different G42/G43/S44/Q75 parameters from the 1992 two-field fit, so whether the linker stiffens on ion binding is unresolved (J36 versus J16).
- Which sample is the RelaxDB CD9K entry: the apo P43G sample of the 1993 study (4 mM, 300 K, pH 6.0, 11.74 T), its (Cd2+)1 sample, or the 1992 Ca2+-loaded P43G data?
- The apo P43G sample shows single-field model-free Rex at 14 amides (A15 2.39 s-1, D19 1.32 s-1) with no rate or population; the authors themselves say further kinetic analysis is not possible. Does single-field Rex count as us-ms exchange for the alternate-APO call (applied here as 'possible' with the anisotropic-tumbling caveat), and should the P43G construct be the reference rather than native Pro43 calbindin with its cis/trans two-peak state?

Judgments: CD9K-J1, CD9K-J6, CD9K-J7, CD9K-J11, CD9K-J12, CD9K-J13, CD9K-J14, CD9K-J15, CD9K-J26, CD9K-J27, CD9K-J28, CD9K-J29, CD9K-J31, CD9K-J36, CD9K-J37 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
