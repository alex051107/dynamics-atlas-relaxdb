# Aquifex aeolicus adenylate kinase (Adk)

RelaxDB entry `AQADK_CPMG` · set CPMG-10 · Aquifex aeolicus adenylate kinase (Adk), wild type

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** does not. Authors call the 20 °C apo exchange fast with small amplitude; no regime stated at 10 °C, no apo Δω, and no minor-state peaks reported.

Free wild-type Adk shows µs–ms exchange in the hinges and parts of both lids. No pA/pB or Δω is reported for apo; the authors say the small amplitude of the dispersion profiles hampered characterization of the nature of the transition. A population (95 ± 2% closed, minor state more open) is measured only for the Mg-Ap5A-bound enzyme.

## The free protein (reference state)

Wild-type apo Adk, no ligand; 10 °C (perdeuterated) and 20 °C (protonated); pH 7.0, 40 mM MOPS, 50 mM NaCl (NMR buffer stated for the perdeuterated sample; the 20 °C protonated buffer is not stated separately)

| | |
|---|---|
| Where (residues) | Hinges and parts of both lids (AMP lid 30–71 and ATP lid 111–169 are the lid domains as defined for TLS refinement, AQADK-J5, not the exchanging region). Exchanging residues are shown only as a colour map at 10 °C (Fig. 3c) and as selected curves at 20 °C (Supplementary Fig. S6), with no residue list (AQADK-J1, AQADK-J2). |
| Exchange rate kex | 950 ± 150 s-1 at 10 °C (AQADK-J1, AQADK-r1); 2,000–7,000 s-1 compatible range at 20 °C, no unique fit (AQADK-J2, AQADK-r2) |
| Minor-state population pB | not reported for apo; the authors say the small dispersion amplitude hampered characterization of the nature of the transition (AQADK-J1) |
| Exchange regime | Not stated at 10 °C. At 20 °C the authors call the apo exchange fast, with small amplitude ('the rate of exchange was fast'; too fast to suppress Rex at the highest CPMG field) (AQADK-J2, AQADK-r2). No apo Δω is printed. |

Fallback statement: May have an alternate conformation differing at the hinges and parts of both lids (lid domains 30–71 and 111–169 as defined for TLS refinement), based on 15N TROSY CPMG relaxation dispersion of the apo enzyme plus PRE and smFRET on labelled constructs (doi:10.1038/nature06410).

## Matching structures

Deposited-structure comparison: The closed state appears only with ligand bound. The only apo crystal (2RH5, three chains) sits between open and 0.33 closed; its authors attribute the substates to crystal contacts. PDBe-KB clustering agrees. Table: [`data/structures/AQADK_CPMG.md`](../../data/structures/AQADK_CPMG.md).

What the papers relate to the states:

- **2RGX**: Closed Zn2+–Ap5A inhibitor complex. PRE from a spin label on the AMP lid of the apo Y52C construct broadens ATP-lid residues, which the authors read as closed-like distances when compared with the open apo substates and the inhibitor-bound structure. Labelled construct, no population or rate.
- **2RH5**: Apo crystal with three molecules (A, B, C) at different degrees of lid closure along the hinge path that the Ap5A complex completes. Crystal snapshots, no solution population or rate. The authors note the three substates seem to be stabilized by crystal contacts.

## Other conditions (not the reference state)

- Mg-Ap5A-bound WT, 20 °C: yes. kex 300 ± 150 s-1 with 95 ± 2% closed and a more open minor state; 46 residues carry fitted ΔωN (AQADK-J11, AQADK-r3).
- Mg-ADP turnover, 20 °C: possible. kex 1,615 ± 100 s-1 (kclose 1,571, kopen 44 s-1), no population reported (AQADK-J8, AQADK-r9).
- Mg-AMPPNP + AMP, 20 °C: possible. kex 1,410 ± 100 s-1; peak splitting at partial ligand saturation shows the slow opening step (AQADK-J10, AQADK-r10, AQADK-r12).
- Mg-ADP turnover, 50 °C: exchange faster than 10,000 s-1 (lower bound, data not shown) (AQADK-J9, AQADK-r11).
- Mg-free nucleotide-bound WT: no_evidence by CPMG; the authors state lid opening is too slow for the window, with no conditions or data given (AQADK-J13, AQADK-r19).
- Apo Y52C/V145C dye-labelled construct (35% of WT activity), room temperature, smFRET: switching between open-like and closed-like distances, kopen 6,500 ± 500 s-1, kclose 2,000 ± 200 s-1 (AQADK-J7, AQADK-r5).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| AQADK-r1 | [Intrinsic motions along an enzymatic reaction trajectory](https://doi.org/10.1038/nature06410) | nmr_relaxation_dispersion | microsecond-to-millisecond exchange | full_text |
| AQADK-r2 | [Intrinsic motions along an enzymatic reaction trajectory](https://doi.org/10.1038/nature06410) | nmr_relaxation_dispersion | exchange detected but too fast for accurate analysis (authors); 2,000-7,000 s-1 compatible with the data | full_text |
| AQADK-r3 | [Intrinsic motions along an enzymatic reaction trajectory](https://doi.org/10.1038/nature06410) | nmr_relaxation_dispersion | inhibitor-bound opening/closing exchange | full_text |
| AQADK-r4 | [Intrinsic motions along an enzymatic reaction trajectory](https://doi.org/10.1038/nature06410) | nmr_ensemble_restraints | transient closed-like proximity | full_text |
| AQADK-r5 | [Intrinsic motions along an enzymatic reaction trajectory](https://doi.org/10.1038/nature06410) | fret | single-molecule lid-distance fluctuations | full_text |
| AQADK-r7 | [Intrinsic motions along an enzymatic reaction trajectory](https://doi.org/10.1038/nature06410) | xray_multitemp_ensemble | crystallographic conformational heterogeneity | full_text |
| AQADK-r8 | [Intrinsic motions along an enzymatic reaction trajectory](https://doi.org/10.1038/nature06410) | pdb_structure_comparison | alternative lid orientations | full_text |
| AQADK-r9 | [Linkage between dynamics and catalysis in a thermophilic-mesophilic…](https://doi.org/10.1038/nsmb821) | nmr_relaxation_dispersion | turnover-associated lid opening/closing | full_text |
| AQADK-r10 | [Linkage between dynamics and catalysis in a thermophilic-mesophilic…](https://doi.org/10.1038/nsmb821) | nmr_relaxation_dispersion | lid motions in absence of chemical conversion | full_text |
| AQADK-r11 | [Linkage between dynamics and catalysis in a thermophilic-mesophilic…](https://doi.org/10.1038/nsmb821) | nmr_relaxation_dispersion | exchange faster than quantitative CPMG window | full_text |
| AQADK-r12 | [Linkage between dynamics and catalysis in a thermophilic-mesophilic…](https://doi.org/10.1038/nsmb821) | nmr_exchange_broadening | slow-exchange peak splitting during ligand titration; splitting absent at 70 C (opening accelerated); 31P splitting of the AMP resonance… | full_text |
| AQADK-r19 | [The energy landscape of adenylate kinase during catalysis](https://doi.org/10.1038/nsmb.2941) | nmr_relaxation_dispersion | lid opening too slow for 15N-CPMG (author statement citing a general NMR review; no data shown) | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `AQADK_CPMG`.

## Caveats

The closed-like identity of the apo minor state comes from labelled constructs (Y52C PRE, Y52C/V145C smFRET), so it is mutant-based inference; the PDB entries are crystal endpoints, not a solved minor state. the NMR collaborator is asked which sample the RelaxDB labels come from (10 °C apo, 20 °C apo or 20 °C Mg-ADP turnover). Homolog rows (E. coli, P. profundum, G. stearothermophilus Adk) were not used for the call.

## Open questions

- Which sample does the RelaxDB AQADK_CPMG R2eff/νCPMG set come from: the 10 °C perdeuterated apo data (kex 950 s-1), the 20 °C protonated apo data, or the 20 °C Mg-ADP turnover data of Wolf-Watz 2004 (kex 1,615 s-1)?
- For the WT apo minor state, should the atlas leave pB undetermined (NMR amplitudes too small), or carry the closed-like assignment from the labelled PRE/smFRET constructs as inference_from_mutant?

Judgments: AQADK-J1, AQADK-J2, AQADK-J5, AQADK-J6, AQADK-J7, AQADK-J8, AQADK-J9, AQADK-J10, AQADK-J11, AQADK-J13 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
