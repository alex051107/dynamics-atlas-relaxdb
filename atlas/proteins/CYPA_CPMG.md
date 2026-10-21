# Human cyclophilin A (CypA)

RelaxDB entry `CYPA_CPMG` · set CPMG-10 · Human cyclophilin A (CypA), wild type

## Answer

**Yes: a minor state is measured in the free protein.**

**Strict two-peak reading:** does not. Authors: fast exchange limit for most amides, methyls intermediate; only 119–122, K91, H92, H126 and V128 reach the slow-exchange limit at 0/10 °C, with no population and no second peak set reported.

At 10 °C free CypA exchanges on the µs–ms scale in an active-site/core network and in the 65–84 loop. A combined CPMG/R1rho fit gives one process with a 2.0 ± 0.1% excited state; methyl CPMG of residues in intermediate exchange gives a 5% minor state, and about 7% is an upper limit for the WT minor conformation overall.

## The free protein (reference state)

Wild-type free CypA, 10 °C (also 0, 20, 25 °C); pH 6.5, 50 mM sodium phosphate, 1–2 mM DTT (2009: 2 mM)

| | |
|---|---|
| Where (residues) | Group I: R55, S99, E120 amides and L39, I57, L98, A103 methyls (caption also lists 'Gly110'); group II: 65–84 loop (D66, F67, T68, N71, G74, K76, S77, K82 shown); 48 exchanging amides at 10 °C in deuterated data |
| Exchange rate kex | 10 °C: group I (active site/core) 1,140 ± 200 s-1 and group II (65–84 loop) 2,260 ± 200 s-1 (CYPA-J1, CYPA-J2, CYPA-r1); one global process 2,200 ± 90 s-1 (CYPA-J3, CYPA-r38). 20 °C: per-residue about 1,000–6,000 s-1 (CYPA-J22, CYPA-r12). |
| Minor-state population pB | 2.0 ± 0.1% (CYPA-r38); 5% from simultaneous fits of methyl residues in intermediate exchange (CYPA-r2); upper limit about 7% for the WT minor conformation overall, from amide kex and Rex (CYPA-r1); poorly determined in the deuterated per-residue fits (CYPA-J4) |
| Exchange regime | fast-to-intermediate for the 1,000–2,000 s-1 process: 'fast exchange limit for most resonances' with the chemical-shift difference 'not known' (2005), methyls in the 'intermediate time regime' (α < 1.5, 2005), most residues 'intermediate-fast exchange at all temperatures' (2009). Residues 119–122, K91, H92, H126 and V128 exchange on the 'intermediate-slow' timescale at 20 °C and are 'at the slow-exchange limit' at 10 and 0 °C only (2009); Table I gives only kA for residues 91, 92, 96, 119, 120 and 122, 0.85–2.74 s-1 at 10 °C and 0.54–1.85 s-1 at 0 °C (CYPA-J4, CYPA-J21; CYPA-r10, CYPA-r11). |

Fallback statement: May have an alternate conformation differing in the 65–84 loop (D66, F67, T68, N71, G74, K76, S77, K82), based on 15N CPMG (doi:10.1038/nature04105) and combined CPMG/R1rho (doi:10.1039/c9sc04696h); fast-to-intermediate exchange, no second peak set observed. For the active-site side, a minor-state model is proposed from crystal alternates (3K0N/3K0O), not observed in solution.

## Matching structures

Deposited-structure comparison: The one clear match. The minor Phe113 rotamer (with Leu98 and Ser99) appears only in apo crystals measured at 240 K or above, with occupancy rising from 0.11 to 0.49; it is absent in cryo and in all ligand-bound chains. Table: [`data/structures/CYPA_CPMG.md`](../../data/structures/CYPA_CPMG.md).

What the papers relate to the states:

- **3K0N**: Room-temperature wild-type crystal with alternate side-chain rotamers for R55, M61, L98, S99 and F113. The rows tie the Ser99/Phe113 network to the millisecond group I process; crystal occupancies are not solution populations. The ID mapping (3K0N = WT, 3K0O = S99T) is taken from the 2024 paper (CYPA-r62).
- **3K0O**: S99T mutant crystal; the authors state the S99T major conformer recapitulates features of the WT minor conformer, which does not prove identical ensembles.

## Other conditions (not the reference state)

- Cyclosporin A-bound: possible. More than 98% major state, residual exchange in the 65–78 loop and near 108–110, no rate (CYPA-J6, CYPA-r4, CYPA-r37).
- Substrate turnover (Suc-AFPF-pNA or FGP peptide): possible. kex 2,730 ± 220 s-1 at 10 °C or about 1,500 s-1, no population; binding and release alone can produce dispersion (CYPA-J7, CYPA-J8, CYPA-J9, CYPA-r3, CYPA-r35, CYPA-r36).
- S99T mutant, 10 °C: yes. CEST kex 188.3 ± 9.5 s-1, pB 1.22 ± 0.03% (CYPA-J10, CYPA-r22).
- S99T rescue mutants: yes, with a second minor state (pB 1.93 / 4.32%, pC 0.31 / 0.73%) (CYPA-J11, CYPA-r23, CYPA-r24).
- D66A mutant: yes, near the detection threshold. kex 2,000 ± 350 s-1, pB 0.5 ± 0.1%; the authors say D66A stabilizes a conformation resembling the WT excited state (CYPA-J12, CYPA-r39).
- Cryogenic crystals (180 K and below): most network alternates disappear, a crystal temperature effect (CYPA-J18).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| CYPA-r1 | [Intrinsic dynamics of an enzyme underlies catalysis](https://doi.org/10.1038/nature04105) | nmr_relaxation_dispersion | microsecond–millisecond conformational exchange | full_text |
| CYPA-r2 | [Intrinsic dynamics of an enzyme underlies catalysis](https://doi.org/10.1038/nature04105) | nmr_relaxation_dispersion | microsecond–millisecond conformational exchange | full_text |
| CYPA-r3 | [Intrinsic dynamics of an enzyme underlies catalysis](https://doi.org/10.1038/nature04105) | nmr_relaxation_dispersion | microsecond–millisecond conformational exchange | full_text |
| CYPA-r4 | [Intrinsic dynamics of an enzyme underlies catalysis](https://doi.org/10.1038/nature04105) | nmr_relaxation_dispersion | microsecond–millisecond conformational exchange | full_text |
| CYPA-r7 | [Hidden alternative structures of proline isomerase essential for…](https://doi.org/10.1038/nature08615) | xray_multitemp_ensemble | crystalline conformational heterogeneity | full_text |
| CYPA-r9 | [Hidden alternative structures of proline isomerase essential for…](https://doi.org/10.1038/nature08615) | nmr_relaxation_dispersion | slow conformational exchange of group-I network | full_text |
| CYPA-r10 | [Characterizing and controlling the inherent dynamics of cyclophilin-A](https://doi.org/10.1002/pro.89) | nmr_relaxation_dispersion | heterogeneous microsecond–millisecond exchange | full_text |
| CYPA-r11 | [Characterizing and controlling the inherent dynamics of cyclophilin-A](https://doi.org/10.1002/pro.89) | nmr_relaxation_dispersion | heterogeneous microsecond–millisecond exchange | full_text |
| CYPA-r12 | [Characterizing and controlling the inherent dynamics of cyclophilin-A](https://doi.org/10.1002/pro.89) | nmr_relaxation_dispersion | heterogeneous microsecond–millisecond exchange | full_text |
| CYPA-r22 | [Rescue of conformational dynamics in enzyme catalysis by directed…](https://doi.org/10.1038/s41467-018-03562-9) | nmr_relaxation_dispersion | slow conformational exchange | full_text |
| CYPA-r23 | [Rescue of conformational dynamics in enzyme catalysis by directed…](https://doi.org/10.1038/s41467-018-03562-9) | nmr_relaxation_dispersion | slow conformational exchange | full_text |
| CYPA-r24 | [Rescue of conformational dynamics in enzyme catalysis by directed…](https://doi.org/10.1038/s41467-018-03562-9) | nmr_relaxation_dispersion | slow conformational exchange | full_text |
| CYPA-r35 | [Determination of the Full Catalytic Cycle among Multiple Cyclophilin…](https://doi.org/10.1021/acs.biochem.5b00746) | nmr_relaxation_dispersion | microsecond–millisecond exchange | full_text |
| CYPA-r36 | [Determination of the Full Catalytic Cycle among Multiple Cyclophilin…](https://doi.org/10.1021/acs.biochem.5b00746) | nmr_relaxation_dispersion | microsecond–millisecond exchange | full_text |
| CYPA-r37 | [Determination of the Full Catalytic Cycle among Multiple Cyclophilin…](https://doi.org/10.1021/acs.biochem.5b00746) | nmr_relaxation_dispersion | microsecond–millisecond exchange | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `CYPA_CPMG`.

## Caveats

The number of apo processes is disputed: two collective groups (r1), one global process (r38), or a continuum of per-residue rates (r10–r12). All apo NMR checked in the cached text was recorded in 50 mM sodium phosphate with no phosphate-free control. MD places Phe113 rotamer exchange at nanoseconds to microseconds, which leaves its assignment to the millisecond process open.

## Open questions

- Apo exchange model: two collective processes (group I/II global fits, Eisenmesser 2005, r1) versus a single global two-state process (kex 2,200 ± 90 s-1, pB 2.0 ± 0.1%, combined CPMG/R1rho, r38) versus a segmental continuum of per-residue rates (Schlegel 2009, Holliday 2017, r10-r12, s1); all three are apo WT at 10 °C, all agree exchange exists, and they disagree on how many processes.
- Turnover rate meaning: Eisenmesser 2005 equates the 2,730 s-1 turnover kex with on-enzyme isomerization (r3); Holliday 2015 shows binding/release alone gives CPMG exchange (TA-peptide about 300 s-1, r36) and challenges that inference for weak-binding tetrapeptides.
- Phe113 network timescale: NMR and crystallography tie Ser99/Phe113 to the millisecond group-I process (r9, r7), while MD finds the Phe113 rotamers interconverting in nanoseconds (r29); different windows, so not a formal conflict, but the assignment is unresolved.
- Which sample and conditions produced the RelaxDB CYPA_CPMG R2eff labels (source lead EZE/MWC): protonated 15N at 600 MHz and 10 °C (Eisenmesser 2005) or deuterated 600/900 MHz at 0/10/20 °C (Schlegel 2009, Holliday 2015/2017)? The number of exchanging residues differs (fewer than 30 versus 48 at 10 °C).
- All apo NMR data (2002, 2005, 2009, 2015) were recorded in 50 mM sodium phosphate pH 6.5 with no phosphate-free control; do you know of a buffer comparison for CypA, or should the exchange be flagged as untested for phosphate binding? (Separately: is 'Gly110' in the 2005 Fig. 1 caption Ser110 or Gly109?)

Judgments: CYPA-J1, CYPA-J2, CYPA-J3, CYPA-J4, CYPA-J6, CYPA-J7, CYPA-J8, CYPA-J9, CYPA-J10, CYPA-J11, CYPA-J12, CYPA-J17, CYPA-J18, CYPA-J21, CYPA-J22 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
