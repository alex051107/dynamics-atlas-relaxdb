# Human K-Ras4B G-domain (residues 1–169)

RelaxDB entry `KRAS_CPMG` · set CPMG-10 · Human K-Ras4B G-domain (residues 1–169), wild type

## Answer

**Yes: a minor state is measured in the free protein.**

**Strict two-peak reading:** qualifies. Authors: 'moderately slow', 'intermediate-to-slow' (|Δω|/kex > 0.5); a second CEST dip for state 1 is seen in WT GTP·Mg at 298 K, and 31P γ1/γ2 are separate peaks at 278 K in a C118S background; no HSQC peak doubling for WT at 298 K is reported.

Free GTP·Mg K-Ras exchanges between a dominant state 2 and a GDP-like, partly disordered state 1 across Switch I, Switch II and the P-loop, with kex about 400 s-1 and 8–10% state 1 in two HEPES laboratories and in PBS/EDTA. In 31P spectra of a C118S-background protein the two states give separate γ-phosphate peaks.

## The free protein (reference state)

Wild-type K-Ras4B 1–169 with native GTP and Mg2+, no partner; 298 K, pH 7.0, 20 mM HEPES, 5 mM MgCl2 (GDP·Mg is listed under other_conditions)

| | |
|---|---|
| Where (residues) | Switch I, Switch II and the P-loop; 45 residues with fitted /Δϖ/ > 0.5 ppm (Source Data Fig. 3); T35, I36, E62, Y71 shown (KRAS-r1) |
| Exchange rate kex | 400 ± 12 s-1 (KRAS-J1, KRAS-r1); 414 ± 3 s-1 (KRAS-J2, KRAS-r26); 404 ± 54 s-1 in PBS/EDTA (KRAS-J3, KRAS-r17) |
| Minor-state population pB | state 1: 10.15 ± 0.47% (KRAS-r1); 9.6 ± 0.1% (KRAS-r26); 7.8 ± 0.2% higher-energy state (pE) in PBS/EDTA, read as state 1 by the entry (KRAS-r17) |
| Exchange regime | Authors: exchange 'proceeded at a moderately slow rate', and residues entering the global fit are in the 'intermediate-to-slow regime with values of /Δω//kex > 0.5' (KRAS-J1, KRAS-r1). 15N CEST shows a second dip for state 1 directly in WT GTP·Mg at 298 K (e.g. T35, E62; KRAS-r1). 31P: γ1 (state 1) and γ2 (state 2) resonances are separate peaks in C118S-background K-Ras·GTP at 278 K, with no rate (KRAS-J25, KRAS-r38). Per-residue 15N /Δϖ/ are plotted (Fig. 3a, dashed line at 0.5 ppm) but not printed in the cached text. |

Fallback statement: May have an alternate conformation differing at Switch I, Switch II and the P-loop (a GDP-like state 1 with a random-coil-like Switch I), based on joint 15N CPMG, 1HN CPMG and 15N CEST (Hansen 2023, doi:10.1038/s41594-023-01070-z).

## Matching structures

Deposited-structure comparison: State 2 matches wild-type GppNHp-bound K-Ras (36OL). State 1 appears only in mutant or inhibitor-bound structures. Only the 150 newest of 556 structures were compared. Table: [`data/structures/KRAS_CPMG.md`](../../data/structures/KRAS_CPMG.md).

## Other conditions (not the reference state)

- GDP·Mg in HEPES without EDTA, 298 K: no_evidence. No significantly populated millisecond state by 15N CEST on ten Switch I/II residues (KRAS-J6, KRAS-r10).
- GDP·Mg methyls, 25 °C: possible. Methyl CPMG flat, but adiabatic dispersion detects faster effector-lobe exchange at I36 and I55 (KRAS-J7, KRAS-r83).
- GDP·Mg in PBS with 10 mM EDTA: minor state 2.8 ± 0.2% (CPMG kex 164 ± 28 s-1) or 3.8 ± 0.1% (CEST kex 267 ± 20 s-1) with Mg2+-free-like shifts, which the authors read as a pre-formed Mg2+-free-like state; the entry suspects an EDTA versus Mg artefact (KRAS-J4, KRAS-J5, KRAS-r13, KRAS-r21).
- GTP·Mg + B-Raf RBD (equimolar): no_evidence; RBD quenches the exchange (KRAS-J12).
- GTP·Mg mutants G12C, G12D, Q61R: yes. Same process with lower state 1 (G12C 6.97 ± 0.17%, G12D 9.00 ± 0.44%, Q61R 1.8%) (KRAS-J14, KRAS-J20, KRAS-r2, KRAS-r3, KRAS-r27).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| KRAS-r1 | [Excited-state observation of active K-Ras reveals differential…](https://doi.org/10.1038/s41594-023-01070-z) | nmr_relaxation_dispersion | conformational heterogeneity | full_text |
| KRAS-r2 | [Excited-state observation of active K-Ras reveals differential…](https://doi.org/10.1038/s41594-023-01070-z) | nmr_relaxation_dispersion | conformational heterogeneity | full_text |
| KRAS-r3 | [Excited-state observation of active K-Ras reveals differential…](https://doi.org/10.1038/s41594-023-01070-z) | nmr_relaxation_dispersion | conformational heterogeneity | full_text |
| KRAS-r10 | [Excited-state observation of active K-Ras reveals differential…](https://doi.org/10.1038/s41594-023-01070-z) | nmr_relaxation_dispersion | conformational heterogeneity | full_text |
| KRAS-r13 | [The Importance of Mg 2+ ‐Free State in Nucleotide Exchange of…](https://doi.org/10.1002/chem.202201449) | nmr_relaxation_dispersion | conformational heterogeneity | full_text |
| KRAS-r17 | [The Importance of Mg 2+ ‐Free State in Nucleotide Exchange of…](https://doi.org/10.1002/chem.202201449) | nmr_relaxation_dispersion | conformational heterogeneity | full_text |
| KRAS-r21 | [The Importance of Mg 2+ ‐Free State in Nucleotide Exchange of…](https://doi.org/10.1002/chem.202201449) | nmr_relaxation_dispersion | conformational heterogeneity | full_text |
| KRAS-r26 | [Dynamic conformational equilibria in the active states of KRAS and…](https://doi.org/10.1039/d4cb00233d) | nmr_relaxation_dispersion | microsecond–millisecond exchange | full_text |
| KRAS-r27 | [Dynamic conformational equilibria in the active states of KRAS and…](https://doi.org/10.1039/d4cb00233d) | nmr_relaxation_dispersion | microsecond–millisecond exchange | full_text |
| KRAS-r38 | [Revealing the mechanism of action of a first-in-class covalent…](https://doi.org/10.1016/j.jbc.2024.105650) | other | conformational heterogeneity | full_text |
| KRAS-r83 | [Insights into the Cross Talk between Effector and Allosteric Lobes…](https://doi.org/10.1021/jacs.2c00007) | nmr_relaxation_dispersion | GDP-bound: little or no methyl CPMG dispersion (<3 s-1; MQ-CPMG also flat); faster, diverse exchange seen only by adiabatic relaxation… | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `KRAS_CPMG`.

## Caveats

Ras has no nucleotide-free apo form, so the call depends on the nucleotide: yes for GTP·Mg, no_evidence for GDP·Mg in HEPES. The 31P two-peak observation is in a C118S background, not WT. No structure of WT state 1 with native GTP is solved (GDP-like shifts and random-coil-like Switch I only); open-Switch-I crystals exist only for mutants or analogue-bound protein, and state-1 mutants T35S and V29G show extra or faster processes, so state 1 may be heterogeneous. GMPPNP raises state 1, so analogue-loaded samples cannot stand in for native GTP.

## Open questions

- CPMG versus CEST on the same PBS/EDTA GDP samples: kex 164 vs 267 s-1 (WT), 99 vs 214 (G12C), 345 vs 668 (G12D), 172 vs 492 (G12V); the authors call them in fair agreement and read one dominant process, but the rates differ by up to about threefold (r13-r16, r21-r24).
- GTP-state exchange model: amide data are fitted as one global two-state process (r1, r17, r26), while GMPPNP methyl data show a synchronized effector-lobe cluster plus allosteric methyls with non-uniform temperature dependence (r84), and state-1 mutants T35S and V29G retain extra or faster processes (r28, r86, r87); whether free WT has more than one process is not settled by these rows.
- The RelaxDB KRAS_CPMG labels match the Hansen 2023 WT K-Ras·GTP·Mg sample (20 mM HEPES pH 7.0, 298 K, 600/850 MHz): the seven unlabelled non-proline residues ('.' at Y64; N at Y32, I55, S65, M72, T87, N116) are exactly the seven non-proline residues without a per-residue Δϖ in that paper's WT GTP source data, and all 45 residues with |Δϖ| > 0.5 ppm are labelled exchange (145 of 158 residues agree at 0.5 ppm, 154 of 158 at 0.4 ppm). The GDP samples fit worse (Pálfy 2022 GDP CPMG fit set: 119 of 158 agree; Hansen 2023 GDP shows no millisecond exchange and is fully assigned), and the Pálfy 2022 GTP sample lacks Switch II assignments that the labels carry. Can you confirm the labels come from Hansen 2023 WT GTP, and should GTP·Mg then be the headline reference state?
- We mark the Palfy 2022 GDP minor state (Mg2+-free-like shifts, PBS with 10 mM EDTA) as a suspected EDTA vs Mg artefact because HEPES samples without EDTA show no millisecond state for GDP; do you agree, or do you know of a measurement that shows it in Mg2+-saturated K-Ras-GDP?

Judgments: KRAS-J1, KRAS-J2, KRAS-J3, KRAS-J4, KRAS-J5, KRAS-J6, KRAS-J7, KRAS-J12, KRAS-J14, KRAS-J20, KRAS-J25 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
