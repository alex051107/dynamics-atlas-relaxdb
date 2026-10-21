# Human mitochondrial import protein MIA40/CHCHD4

RelaxDB entry `MIA40` · set RelaxDB-133 · Human mitochondrial import protein MIA40/CHCHD4 (UniProt Q8N4Q1), folded CHCH domain 41-106 (entry 1-66 = author 41-106)

## Answer

**Unknown: not measured, or the key paper is not readable in full.**

**Strict two-peak reading:** cannot tell. No row states an exchange regime or shows a second peak set for MIA40 in any redox or binding state.

No row reports MIA40 relaxation, dispersion or exchange broadening (MIA40-J2 to MIA40-J4, search_insufficient). The 2009 structure paper, read as an abstract, calls the N-terminal lid rigid without a stated window (MIA40-J1). All other rows are bound-state shift maps, redox chemistry or construct comparisons without a MIA40 rate.

## The free protein (reference state)

Free entry folded domain (41-106), oxidised with two structural disulfides, no substrate or partner; no BMRB id and no row describes this sample (the 2K3J structure deposition of full-length MIA40 lists 298 K, pH 7.0)

| | |
|---|---|
| Where (residues) | none for exchange; bound-state perturbations at C55, V88, F91 (entry 15, 48, 51; MIA40-J5) and SPS/AIA-A perturbations at F68, F72, F91 (entry 28, 32, 51; MIA40-J11) |
| Exchange rate kex | not measured (MIA40-J3) |
| Minor-state population pB | not measured (MIA40-J3) |
| Exchange regime | Not stated (MIA40-J3). |

Fallback statement: No alternate-state annotation is possible for the free oxidised MIA40 folded domain: no exchange measurement exists, and the reported changes come from bound, mutant or truncated constructs (doi:10.1038/s44318-024-00360-6; doi:10.1073/pnas.1010095107).

## Matching structures

What the papers relate to the states:

- **2L0Y**: C53S MIA40 disulfide-trapped with Cox17 C26/36/55S. MIA40 secondary structure is unchanged against free 2K3J; the CPC and hydrophobic cleft shift and the substrate folds a helix. A bound endpoint, not an apo alternate state.

## Other conditions (not the reference state)

- Reduced-CPC MIA40 with ALR, 298 K: redox conversion to the oxidised spectrum (long-form ALR) or partial conversion (short-form ALR); chemistry, not conformational exchange (MIA40-J7, MIA40-J8).
- Substrate- or partner-bound C53S MIA40 (Cox17, Tim9 ITS peptide, CRAC sf-ALR adducts): cleft and CPC chemical-shift changes, MIA40 fold unchanged; no rate (MIA40-J5, MIA40-J6, MIA40-J9).
- Inactive SPS full length versus ΔN-SPS and AIA-A-SPS: the N-terminal AIF-interaction region shields the active site; its removal or mutation shifts core resonances and the AIA-A mutant is more extended by SAXS at 10 °C; construct comparisons, no population (MIA40-J10 to MIA40-J12).
- AIF-CHCHD4(1-45) fusion: SAXS-restrained MD allows an unengaged N-terminal fragment in a minor model; md_only, fragment outside the entry except 41-45 (MIA40-J13).
- Redox-active ΔN-CHCHD4: persistent intermolecular disulfide self-association, an artefact lead for truncated CPC-intact samples (MIA40-J14).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| MIA40-r1 | [MIA40 is an oxidoreductase that catalyzes oxidative protein folding…](https://doi.org/10.1038/nsmb.1553) | other | Structural description of folded core and rigid lid; relaxation window unverified | abstract_only |
| MIA40-r2 | [Molecular chaperone function of Mia40 triggers consecutive induced…](https://doi.org/10.1073/pnas.1010095107) | pdb_structure_comparison | Substrate-induced folding with localized MIA40 chemical-environment changes; no quantified MIA40 exchange | full_text |
| MIA40-r3 | [Molecular chaperone function of Mia40 triggers consecutive induced…](https://doi.org/10.1073/pnas.1010095107) | other | Binding-induced local chemical-environment changes in MIA40; peptide folds | full_text |
| MIA40-r4 | [Molecular recognition and substrate mimicry drive the…](https://doi.org/10.1073/pnas.1014542108) | other | Enzymatic redox-state conversion; conformational exchange not resolved | full_text |
| MIA40-r5 | [Molecular recognition and substrate mimicry drive the…](https://doi.org/10.1073/pnas.1014542108) | other | Enzymatic redox-state conversion; conformational exchange not resolved | full_text |
| MIA40-r6 | [Molecular recognition and substrate mimicry drive the…](https://doi.org/10.1073/pnas.1014542108) | other | Partner-binding chemical-environment changes in MIA40 | full_text |
| MIA40-r7 | [Molecular recognition and substrate mimicry drive the…](https://doi.org/10.1073/pnas.1014542108) | other | Partner-binding chemical-environment changes in MIA40 | full_text |
| MIA40-r9 | [NADH-bound AIF activates the mitochondrial CHCHD4/MIA40 chaperone by…](https://doi.org/10.1038/s44318-024-00360-6) | other | Perturbation-linked intramolecular contact change; no measured exchange timescale | full_text |
| MIA40-r10 | [NADH-bound AIF activates the mitochondrial CHCHD4/MIA40 chaperone by…](https://doi.org/10.1038/s44318-024-00360-6) | other | N-terminal regulation of core contact surface; proposed CPC-lid hinge reorientation | full_text |
| MIA40-r11 | [NADH-bound AIF activates the mitochondrial CHCHD4/MIA40 chaperone by…](https://doi.org/10.1038/s44318-024-00360-6) | other | Expanded solution conformation upon N-terminal interface disruption | full_text |
| MIA40-r12 | [NADH-bound AIF activates the mitochondrial CHCHD4/MIA40 chaperone by…](https://doi.org/10.1038/s44318-024-00360-6) | md_simulation | Model-dependent bound/unengaged N-terminal CHCHD4 conformations and flexible linkers | full_text |
| MIA40-r13 | [NADH-bound AIF activates the mitochondrial CHCHD4/MIA40 chaperone by…](https://doi.org/10.1038/s44318-024-00360-6) | other | Redox-dependent self-association as a confound for apparent loss of chaperone function | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `MIA40`.

## Caveats

Oxidised, reduced and substrate-bound states are kept apart; none has an exchange measurement. The source of the RelaxDB MIA40 relaxation set is not identified (no BMRB id), and the entry construct lacks the N-terminal region that the 2025 paper shows packing against the active site, so the free entry domain may differ from full-length MIA40. Rows r8, r14 (in-cell redox state), r15 (negative binding control) and r16 (ITC) were not used.

## Open questions

- The input card gives no BMRB id; is the RelaxDB MIA40 set the folded-domain part (41-106) of a full-length MIA40 relaxation measurement from Banci et al. 2009 (2K3J), and in which CPC redox state?
- Should the bound-state chemical-shift maps (Cox17, Tim9 peptide, ALR adducts) and the SPS/AIA-A construct comparisons be counted as alternate-state evidence at all, given that none measures a MIA40 rate?

Judgments: MIA40-J1, MIA40-J2, MIA40-J3, MIA40-J4, MIA40-J5, MIA40-J6, MIA40-J7, MIA40-J8, MIA40-J9, MIA40-J10, MIA40-J11, MIA40-J12, MIA40-J13, MIA40-J14 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
