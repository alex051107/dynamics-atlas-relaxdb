# Escherichia coli RfaH C-terminal domain (entry native 111–162)

RelaxDB entry `RFAHTD` · set RelaxDB-133 · Escherichia coli RfaH C-terminal domain (entry native 111–162), studied as the isolated domain (native 101–162 or 102–162)

## Answer

**Yes: a minor state is measured in the free protein.**

**Strict two-peak reading:** qualifies. The largely unfolded state B is seen as its own peak set (CEST on both A and B peaks, zz-exchange) and exchanges on a 300 ms scale in the perdeuterated sample. B is the unfolded domain, not the α-hairpin; the sub-millisecond states A', B' and B'' are dark and seen only through CPMG and CEST.

The isolated wild-type CTD has two kinds of minor state. On the sub-millisecond scale, a joint 15N CPMG/CEST five-state fit over 35 residues finds the folded barrel exchanging with a dark state A' of about 0.35%, placed in the β1/β2 loop, while the unfolded state B exchanges with B' and B''. More slowly, the barrel unfolds and refolds: CEST gives a 5.5% unfolded-like state in protonated samples and about 25% in perdeuterated samples. None of these minor states is the NTD-bound α-hairpin.

## The free protein (reference state)

Wild-type isolated CTD (β-barrel), no partner, 25 °C, pH 6.5: perdeuterated 1.0 mM U-[15N/2H] sample in 25 mM potassium phosphate, 0.5 mM EDTA, 1 mM PMSF (PNAS 2025); protonated 0.7–1 mM 15N sample in 20 mM sodium phosphate, 100 mM NaCl, 1 mM EDTA (eLife)

| | |
|---|---|
| Where (residues) | 35 residues in the five-state fit (SI Tables S3–S6): T109, Y111, a G113–F123 subset, G125, Q127, I129, D134–E136, R138–I146, K148, I150, V154, K155, E158–R160, L162 (T109 lies outside the entry); A' proposed as a β1/β2-loop change (RFAHTD-J4). 45 sites with A and B CEST profiles, T109–L162 (RFAHTD-J6). B' and B'' differ in helix α5* of the unfolded ensemble (RFAHTD-J5). |
| Exchange rate kex | A'↔A τex about 500 µs (Results and Fig. 6; the abstract says about 1 ms) (RFAHTD-J4, RFAHTD-r9, RFAHTD-r13). B↔B' τex about 1.2–1.3 ms; B↔B'' about 800 µs (branched) or B'↔B'' about 1 ms (linear); linear-model kBB' 21.6 ± 2.4 s-1, kB'B 675 ± 25 s-1 (RFAHTD-J5, RFAHTD-r14). A↔B folding/unfolding: kex 14.80 ± 1.31 s-1 (kAB 0.82 ± 0.10, kBA 13.98 ± 1.24 s-1), protonated (RFAHTD-J7, RFAHTD-r5); kAB about 0.8 s-1, kBA about 2.4 s-1, τex about 300 ms, perdeuterated (RFAHTD-J6, RFAHTD-r8). |
| Minor-state population pB | A' about 0.35% (A about 76–77%); B' about 0.25–0.35%; B'' about 0.05% (RFAHTD-J4, RFAHTD-J5, RFAHTD-r9). Unfolded B: 5.53 ± 0.46% (reported with pA 94.47 ± 0.46%), protonated (RFAHTD-J7, RFAHTD-r5); about 25% (pA about 75%) by two-site CEST and about 23% in the five-state fit, perdeuterated (RFAHTD-J6, RFAHTD-r8, RFAHTD-r9). |
| Exchange regime | B is in slow exchange: separate A and B peaks with zz-exchange assignments, and CEST Δω(B−A) matches those assignments (RFAHTD-J6). A', B' and B'' are dark states seen only through dispersion and CEST; no Δω for them is printed in the rows (RFAHTD-J4, RFAHTD-J5). |

Fallback statement: May have alternate states of the isolated CTD: a sub-millisecond β1/β2-loop state (about 0.35%) and a slowly exchanging, largely unfolded state (5.5% to about 25% depending on the sample), based on 15N CPMG and CEST (doi:10.1073/pnas.2506441122; doi:10.7554/elife.76630).

## Matching structures

What the papers relate to the states:

- **2OUG**: Full-length RfaH crystal with the CTD as an α-hairpin packed on the NTD, the other fold of the same sequence (the isolated barrel is 2LCL). It does not match any isolated-CTD minor state: the minor ensemble resembles the urea-unfolded CTD with residual structure, not the α-hairpin, and free full-length RfaH does not visit the β state above 0.2%.

## Other conditions (not the reference state)

- Full-length autoinhibited RfaH, 16 °C, pH 6.5, 50 mM sodium phosphate, 5% glycerol, 1 bar: yes. kAB 16.3 ± 1.2, kBA 319 ± 20 s-1 (τex about 3 ms), pB 4.9 ± 0.5%, mostly NTD β3/β4 with small Δω in the CTD helices (RFAHTD-J16, RFAHTD-r26).
- Same sample at 2.5 kbar: yes. kAB 8.4 ± 0.4, kBA 202 ± 9 s-1, pB 4.0 ± 0.1% by CEST; CPMG curves are flat (RFAHTD-J17, RFAHTD-r27, RFAHTD-r28).
- Full-length RfaH, 288 K, pH 7.5: no_evidence at CTD F123, G135, M140 and L145 by 15N CPMG, nuCPMG 30–2000 Hz (RFAHTD-J18, RFAHTD-r18).
- Full-length RfaH, 298 K: no_evidence for the β-barrel CTD state above 0.2% at 20–200 s-1 by CEST (RFAHTD-J19, RFAHTD-r17).
- ops-paused elongation complex bound: the tethered CTD converts from α to β and returns toward α on competitive release; titration endpoints, no rate (RFAHTD-J12, RFAHTD-r20, RFAHTD-r21).
- Homolog V. cholerae RfaH-KOW, 25 °C: yes (homolog). pB 0.43 ± 0.01% (pA 99.57 ± 0.01%), kex 74.57 ± 3.18 s-1 (RFAHTD-J31, RFAHTD-r7).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| RFAHTD-r3 | [An α helix to β barrel domain switch transforms the transcription…](https://doi.org/10.1016/j.cell.2012.05.042) | pdb_structure_comparison | Context-dependent α-hairpin/β-barrel fold switching | full_text |
| RFAHTD-r5 | [Structural and thermodynamic analyses of the β-to-α transformation…](https://doi.org/10.7554/elife.76630) | nmr_relaxation_dispersion | β-barrel A exchanging with predominantly unfolded ensemble B | full_text |
| RFAHTD-r7 | [Structural and thermodynamic analyses of the β-to-α transformation…](https://doi.org/10.7554/elife.76630) | nmr_relaxation_dispersion | Homolog β-barrel exchange with largely unfolded minor species | full_text |
| RFAHTD-r8 | [Unraveling structural transitions and kinetics along the…](https://doi.org/10.1073/pnas.2506441122) | nmr_relaxation_dispersion | Slow β-roll A ↔ largely unfolded B exchange | full_text |
| RFAHTD-r9 | [Unraveling structural transitions and kinetics along the…](https://doi.org/10.1073/pnas.2506441122) | nmr_relaxation_dispersion | Slow A↔B exchange plus fast A↔A′ and B/B′/B″ exchange | full_text |
| RFAHTD-r13 | [Unraveling structural transitions and kinetics along the…](https://doi.org/10.1073/pnas.2506441122) | nmr_exchange_broadening | Additional exchange broadening beyond slow A↔B exchange | full_text |
| RFAHTD-r14 | [Unraveling structural transitions and kinetics along the…](https://doi.org/10.1073/pnas.2506441122) | nmr_exchange_broadening | Additional exchange broadening beyond slow A↔B exchange | full_text |
| RFAHTD-r17 | [Reversible fold-switching controls the functional cycle of the…](https://doi.org/10.1038/s41467-019-08567-6) | nmr_relaxation_dispersion | No detected slow exchange into the known β CTD state | full_text |
| RFAHTD-r18 | [Reversible fold-switching controls the functional cycle of the…](https://doi.org/10.1038/s41467-019-08567-6) | nmr_relaxation_dispersion | No significant dispersion at the selected sites in this experiment | full_text |
| RFAHTD-r20 | [Reversible fold-switching controls the functional cycle of the…](https://doi.org/10.1038/s41467-019-08567-6) | other | Partner-associated α-to-β CTD conversion | full_text |
| RFAHTD-r21 | [Reversible fold-switching controls the functional cycle of the…](https://doi.org/10.1038/s41467-019-08567-6) | other | Reversible β-to-α CTD return after release | full_text |
| RFAHTD-r26 | [A Transient, Excited Species of the Autoinhibited α-State of the…](https://doi.org/10.1021/acs.biochem.4c00258) | nmr_relaxation_dispersion | Millisecond exchange within the autoinhibited α ensemble | full_text |
| RFAHTD-r27 | [A Transient, Excited Species of the Autoinhibited α-State of the…](https://doi.org/10.1021/acs.biochem.4c00258) | nmr_relaxation_dispersion | Pressure-dependent reduction of excited-state access | full_text |
| RFAHTD-r28 | [A Transient, Excited Species of the Autoinhibited α-State of the…](https://doi.org/10.1021/acs.biochem.4c00258) | nmr_relaxation_dispersion | No resolved CPMG dispersion at high pressure despite CEST-detected exchange | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `RFAHTD`.

## Caveats

The unfolded-state population differs between the protonated (5.5%) and perdeuterated (about 25%) samples, which also differ in buffer and construct start; kAB agrees but kBA does not, and the rows do not say which difference causes it. The A' lifetime is printed as about 500 µs and about 1 ms in the same paper. Linear and branched five-state schemes fit equally well. The judgments place the folding/unfolding exchange in the slower-than-ms window. The RelaxDB R1/R2/NOE sample is unidentified (the likely Tudor-domain paper was read as abstract only).

## Open questions

- Unfolded-state population of the isolated CTD at 25 °C, pH 6.5: 5.53 ± 0.46% with kex 14.8 s-1 (r5; protonated, native 101-162, 20 mM sodium phosphate with 100 mM NaCl) versus about 25% with tauex about 300 ms (r8, r9; perdeuterated, native 102-162, 25 mM potassium phosphate, no NaCl). kAB agrees (about 0.8 s-1) but kBA differs (14 versus 2.4-2.8 s-1); the rows do not say which sample difference causes it.
- A'↔A lifetime: about 500 µs in the PNAS Results and Fig. 6, about 1 ms in its abstract (r9).
- Full-length autoinhibited RfaH: CPMG is flat at CTD F123, G135, M140, L145 at 288 K, pH 7.5 in 10 mM phosphate (r18), while at 16 °C, pH 6.5 in 50 mM phosphate with glycerol 32 residues disperse with small Δω inside the CTD helices (r26). Temperatures nearly match but pH, buffer and probes differ, and r26's CTD residue list is in an inaccessible SI table; treated as a condition difference, not a conflict.
- Which sample supplied the RelaxDB RFAHTD R1/R2/NOE set? The input links 2LCL (Cell 2012, isolated CTD 101-162) and no BMRB id; the Tudor-domain model-free paper (r30) is a likely source but was read only as an abstract.
- For the WT apo answer, should the A↔B folding/unfolding exchange (kex 3-15 s-1, tauex 70-300 ms) count as slower_than_ms as done here, and which isolated-CTD sample (protonated pB 5.5% or perdeuterated pB 25%) should RelaxDB labels be compared with?

Judgments: RFAHTD-J4, RFAHTD-J5, RFAHTD-J6, RFAHTD-J7, RFAHTD-J10, RFAHTD-J12, RFAHTD-J16, RFAHTD-J17, RFAHTD-J18, RFAHTD-J19, RFAHTD-J31 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
