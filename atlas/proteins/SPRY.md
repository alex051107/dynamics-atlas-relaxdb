# Mouse SPRY domain-containing SOCS box protein 2 (SPSB2/SSB-2

RelaxDB entry `SPRY` · set RelaxDB-133 · Mouse SPRY domain-containing SOCS box protein 2 (SPSB2/SSB-2, UniProt O88838), SPRY domain construct 12-224 (226 residues, 2AFJ:A)

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** does not. The authors attribute the missing loop-CD amides H119-G125 to intermediate-timescale exchange; no second peak set is reported, and CPMG shows no dispersion in the observable amides.

Seven loop-CD amides (H119-G125, entry 114-120) are absent at 5, 15 and 22 °C and at 500-800 MHz, and CLEANEX recovers none, so the authors attribute the loss to intermediate conformational exchange (SPRY-J4). 15N CPMG at 600 MHz, 22 °C finds no dispersion among observable amides (SPRY-J3), and apparent Modelfree Rex terms may be tensor bias (SPRY-J5). There is no rate, population, delta omega or minor-state structure.

## The free protein (reference state)

Free wild-type SSB-2 (12-224), no peptide or inhibitor; 22 °C, pH 7.0, 10 mM sodium phosphate, 50 mM NaCl, 2 mM EDTA, 0.02% NaN3; the input card gives no BMRB id

| | |
|---|---|
| Where (residues) | loop CD H119-G125 (entry 114-120) (SPRY-J4); fast ps-ns motion separately in loop DE I135-E165 (SPRY-J1) |
| Exchange rate kex | not measured (SPRY-J4); no dispersion at nuCPMG 20-1000 Hz in observable amides (SPRY-J3, SPRY-r2) |
| Minor-state population pB | not measured (SPRY-J4) |
| Exchange regime | Intermediate exchange, the authors' reading of absent cross-peaks after temperature, field and CLEANEX controls (SPRY-J4, SPRY-r3 to SPRY-r6); no dispersion was possible for these amides. |

Fallback statement: May have an alternate conformation of loop CD (H119-G125) relative to the beta-sandwich core, based on amide cross-peaks missing at all tested temperatures and fields that the authors attribute to intermediate exchange in the free SPRY domain (doi:10.1110/ps.062477806); no rate or population.

## Matching structures

## Other conditions (not the reference state)

- Murine SPSB2 bound to human Par-4(59-77), 295 K, pH 6.7: chemical-shift changes around the ELNNN site including loop D; a bound-state environment change, not an alternate state (SPRY-J10, SPRY-r15).
- Human SPSB2 with VASA, iNOS, RGD and TAT peptides: crystal and SPR data only; modest rearrangements except W207, ligand binding kinetics and biphasic TAT dissociation, none a protein conformational exchange (SPRY-J11 to SPRY-J14).
- Docked human SPSB2-CIGB-814 complex, one 100 ns MD run: fluctuating contacts, no alternate state (SPRY-J15).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| SPRY-r1 | [Dynamics of the SPRY domain-containing SOCS box protein 2:…](https://doi.org/10.1110/ps.062477806) | nmr_spin_relaxation | picosecond-to-nanosecond backbone flexibility, strongest in loop DE | full_text |
| SPRY-r2 | [Dynamics of the SPRY domain-containing SOCS box protein 2:…](https://doi.org/10.1110/ps.062477806) | nmr_relaxation_dispersion | No resolved submillisecond-to-millisecond exchange in observable resonances under these conditions | full_text |
| SPRY-r3 | [Dynamics of the SPRY domain-containing SOCS box protein 2:…](https://doi.org/10.1110/ps.062477806) | nmr_exchange_broadening | Missing amide cross-peaks consistent with intermediate exchange; process unquantified | full_text |
| SPRY-r4 | [Dynamics of the SPRY domain-containing SOCS box protein 2:…](https://doi.org/10.1110/ps.062477806) | nmr_exchange_broadening | Missing amide cross-peaks consistent with intermediate exchange; process unquantified | full_text |
| SPRY-r5 | [Dynamics of the SPRY domain-containing SOCS box protein 2:…](https://doi.org/10.1110/ps.062477806) | nmr_exchange_broadening | Missing amide cross-peaks consistent with intermediate exchange; process unquantified | full_text |
| SPRY-r6 | [Dynamics of the SPRY domain-containing SOCS box protein 2:…](https://doi.org/10.1110/ps.062477806) | nmr_exchange_broadening | Missing amide cross-peaks consistent with intermediate exchange; process unquantified | full_text |
| SPRY-r7 | [Dynamics of the SPRY domain-containing SOCS box protein 2:…](https://doi.org/10.1110/ps.062477806) | nmr_spin_relaxation |  | full_text |
| SPRY-r8 | [Dynamics of the SPRY domain-containing SOCS box protein 2:…](https://doi.org/10.1110/ps.062477806) | other | Predicted collective loop displacements and local elasticity | full_text |
| SPRY-r15 | [Structural basis for Par-4 recognition by the SPRY domain- and SOCS…](https://doi.org/10.1016/j.jmb.2010.06.017) | other |  | full_text |
| SPRY-r16 | [Structural basis for Par-4 recognition by the SPRY domain- and SOCS…](https://doi.org/10.1016/j.jmb.2010.06.017) | pdb_structure_comparison | Static ligand-associated side-chain and loop differences; exchange kinetics unresolved | full_text |
| SPRY-r21 | [Overcoming Ligand Discovery Challenges: Developing Peptide-Based…](https://doi.org/10.1021/acschembio.5c00702) | other | Ligand association/dissociation kinetics, not internal conformational exchange | full_text |
| SPRY-r22 | [Overcoming Ligand Discovery Challenges: Developing Peptide-Based…](https://doi.org/10.1021/acschembio.5c00702) | other | Ligand association/dissociation kinetics, not internal conformational exchange | full_text |
| SPRY-r23 | [Overcoming Ligand Discovery Challenges: Developing Peptide-Based…](https://doi.org/10.1021/acschembio.5c00702) | other | Ligand association/dissociation kinetics, not internal conformational exchange | full_text |
| SPRY-r24 | [Overcoming Ligand Discovery Challenges: Developing Peptide-Based…](https://doi.org/10.1021/acschembio.5c00702) | other | Ligand association/dissociation kinetics, not internal conformational exchange | full_text |
| SPRY-r32 | [PEARL: novel protein targets recommendation model via heterogeneous…](https://doi.org/10.1093/bib/bbag551) | md_simulation | Simulated local fluctuations around one docked complex | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `SPRY`.

## Caveats

The call rests on missing peaks, not dispersion; the NMR collaborator is asked whether that counts as µs-ms detection. Peptide- and inhibitor-bound states are kept out of the apo call. All mouse NMR is in phosphate/EDTA with no buffer control. No PDB entry is shown in the rows as a loop-CD alternate conformer, so no structure is matched.

## Open questions

- Apparent Modelfree Rex terms in the 600 MHz relaxation fit (r1) versus flat CPMG dispersion at 20-1000 Hz (r2); the authors attribute the Rex terms to possible diffusion-tensor bias, which is plausible but not tested.
- Should the loop-CD amides missing at every tested temperature and field (with a CLEANEX control but no dispersion) count as WT apo µs-ms detection, as done here with indirect strength?
- The input card gives no BMRB id; is the RelaxDB SPRY set the 600 MHz, 22 °C relaxation data of Yao et al. 2006 (doi:10.1110/ps.062477806)?

Judgments: SPRY-J1, SPRY-J3, SPRY-J4, SPRY-J5, SPRY-J10, SPRY-J11, SPRY-J12, SPRY-J13, SPRY-J14, SPRY-J15 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
