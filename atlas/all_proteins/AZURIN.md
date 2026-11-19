# Azurin (`AZURIN`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P00282` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`yes`)](../proteins/AZURIN.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `yes` (strict two-peak reading: `qualifies: the source states that the His35 process is slow on the chemical-shift timescale at both pH 7.0 and pH 5.5 and shows two resolved peak sets for the protons and nitrogens around His35 in jump-return HMQC spectra between pH 6.3 and 7.6, connected by EXSY/ROESY cross-peaks at pH 7.0 (AZURIN-J38; D-r4, D-r5). Computed regime (E-033): kex = kAB + kBA = 2k = 90 ± 12 s-1 at pH 7.0 and 120 ± 60 s-1 at pH 5.5; 15N delta-omega 340 Hz (G37) to about 400 Hz (G88, G90) at 60.8 MHz, i.e. 2136-2513 rad/s; kex/delta-omega = 0.04 (pH 7.0) and 0.06 (pH 5.5), slow exchange, matching the authors' wording. At the reference pH 5.5 the minor form is only 2-4%, so the second peak set is documented near pH 7, not shown at pH 5.5.`)
- **Reference state:** The RelaxDB sample: wild-type Pseudomonas aeruginosa azurin with its copper reduced to Cu(I) (dithionite), 2 mM, 20 mM potassium phosphate, pH 5.5, 41 °C, 600 MHz (doi:10.1021/bi990624l, full text; AZURIN-J37, J41-J43 marked is_wt_apo). Changed on 2026-10-20 from copper-free apo, which stays in the table as another sample state (AZURIN-J18 to J26). Reduced Cu(I) holo azurin is the deposited construct's native metal state; the alternate state here is still a metal-bound, protonation-coupled one.
- **Exchange rate (`kex`):** Reference state, pH 5.5: k = 60 ± 30 s-1 printed as (kAB + kBA)/2, so kex = 120 ± 60 s-1, tau_ex 8 ± 4 ms (model estimate from line broadening of G37, G88, G90; AZURIN-J43, D-r3). pH 7.0 EXSY: k = 45 ± 6 s-1 (average rate at the pKa, kAB = kBA), kex = 90 ± 12 s-1, tau_ex 11 ± 2 ms (AZURIN-J38, D-r4). 2003 Cu(I) CPMG at 44.8 °C, pH about 5, 50 mM phosphate: forward rates kA 11.7 ± 2.4 s-1 (H35 region, keq 254 ± 31) and 4.1 ± 0.1 s-1 (copper loops, keq 222 ± 7), total kex not printed (AZURIN-J12, J13; keq values from Table 3 of that paper, not in a row). Not measured for Cu(II) or apo.
- **Minor-state population (`pB`):** Reference state, pH 5.5: deprotonated form 0.02-0.04, estimated from the His35 pKa 7.0 ± 0.1, not fitted (D-r3). pH 7.0: 0.5 (equal populations at the pKa, stated by the authors; D-r4). 2003 Cu(I) CPMG: 0.39 ± 0.07% (H35 region) and 0.45 ± 0.02% (copper loops) at 44.8 °C (J12, J13). Not measured for Cu(II) or apo.
- **Exchanging region:** Reference state Cu(I), pH 5.5: N10, D11, G37, G45, G88, S89, G90 around His35 (Rex 2-9.5 Hz) and F114 in the copper loop (mechanism unassigned); pH 7.0 EXSY: His35 C-epsilon1 H and the amides of G9, G37, G88, E91; the crystal comparison names G9-Q12, P36-G37, M44-G45, G88-E91 (J43, J38, J44). 2003 Cu(I) CPMG: D11, G37, G88-G90 (near H35) and N47, W48, F111-T113, G116, H117, L120, K122 (near copper) (J12, J13). Apo: A1-C3, G9-D11, N18, H35-L39, G45, H46, G88-E91 missing, dispersion at M44 and I87 (J18, J19).
- **Structure comparison:** [{"pdb": "not given (oxidised Cu(II) crystals at pH 5.5 and pH 9.0, Nar et al.)", "what": "The authors' model of the two exchanging forms: at low pH the P36 carbonyl accepts a hydrogen bond from protonated His35 N-delta1-H; at high pH the P36-G37 peptide bond flips and G37 HN hydrogen-bonds His35 N-delta1, with loops 9-12 and 88-91 adjusting. Oxidised crystals compared with reduced solution data; no solution structure of either form.", "evidence_row": "AZURIN-AZURIN_20261020202618-r6"}]
- **Caveats:** Call raised from possible to yes on 2026-10-20 after the RelaxDB source paper (doi:10.1021/bi990624l) was read in full and the reference state was reset to its sample, reduced Cu(I) azurin at pH 5.5 and 41 °C (ledger/redraft_notes.json; adjudication ledger/adjudication_AZURIN_pdf.json). Two caveats for the NMR collaborator: (1) the alternate state is protonation-coupled, a pH-dependent chemical equilibrium of His35 with a local peptide flip, and its 2-4% population at pH 5.5 is estimated from the pKa rather than fitted; (2) the reference state is metal-bound (Cu(I) holo), so this is not a ligand-free alternate conformation in the strict sense. The pH 5.5 rate comes from single-field line broadening with an equal-population equation corrected for unequal populations (k = 60 ± 30 s-1); the two-peak evidence and the EXSY rate come from pH 7.0 samples, where the populations are equal. The 2003 three-field CPMG model of the same Cu(I) H35 process (pB 0.39%, kA 11.7 s-1, kex in the thousands per second) is not reconciled with the 1999 rates. The abstract-only rows of the 1999 paper (AZURIN-AZURIN_20261020143153-r1, r2) are superseded and no longer cited. Only the selected papers were searched, all in phosphate or Tris.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/AZURIN.md`](../proteins/AZURIN.md) (23 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

*6 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `kex` | 45 s-1 ( 6 | His35 C1H and amide protons G9, G37, G88, E91 (10 cross-peaks, fi | `NMR_exchange_and_dispersion` | `target` | not stated (nonlabeled azurin); 41 °C; pH 7.0; 600 | `no` | [`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l) |
| `kex` | 60 s-1 ( 30 | G37, G88, G90 | `NMR_spin_relaxation_and_MF` | `target` | Cu(I) (reduced) azurin prepared; relaxation measured at pH 5.5; 41 °C; pH 5.5; 600 | `no` | [`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l) |
| `population` | 0.96-0.98 fraction protonated form (pH 5.5) null | His35 protonated form | `NMR_spin_relaxation_and_MF` | `target` | Cu(I) (reduced) azurin prepared; relaxation measured at pH 5.5; 41 °C; pH 5.5; 600 | `no` | [`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l) |
| `population` | 0.04 fraction deprotonated form (pH 5.5), upper end of printed range 0.02-0.04 null | His35 deprotonated form | `NMR_spin_relaxation_and_MF` | `target` | Cu(I) (reduced) azurin prepared; relaxation measured at pH 5.5; 41 °C; pH 5.5; 600 | `no` | [`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l) |
| `delta_omega` | 340 Hz (15N shift difference between forms) null | G37 | `NMR_spin_relaxation_and_MF` | `target` | Cu(I) (reduced) azurin prepared; relaxation measured at pH 5.5; 41 °C; pH 5.5; 600 | `no` | [`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l) |
| `delta_omega` | about 400 Hz (15N shift difference between forms) null | G88 and G90 | `NMR_spin_relaxation_and_MF` | `target` | Cu(I) (reduced) azurin prepared; relaxation measured at pH 5.5; 41 °C; pH 5.5; 600 | `no` | [`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*25 rows total (22 spin-relaxation/model-free; 3 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l) | `NMR_spin_relaxation_and_MF` | `target` | Cu(I) (reduced) azurin prepared; relaxat | S2 (6), T2 (4), NOE (3), T1 (3), tau_m (2), other (2) | tau_m = 4.7 ns (whole protein) |
| [`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l) | `NMR_exchange_and_dispersion` | `target` | not stated (nonlabeled azurin) | other (2) | other = 11 ms (tau_ex = 1/(kAB+kBA)) (His35 exchange process) |
| [`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l) | `NMR_other` | `target` | not stated (nonlabeled azurin) | pKa (1) | pKa = 7.0  (His35) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **fast internal motion (tau_e needed)** ([`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l), sample `S1`): 74, 105, 107, 127, and 128
- **chemical exchange, Rex > 2 Hz, linked to His-35 deprotonation** ([`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l), sample `S1`): 10, 11, 37, 45, 88-90, and 114
- **low heteronuclear NOE (more than 2 SD below average)** ([`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l), sample `S1`): 105, 107, 108, and the C-terminal residue 128
- **exchange broadening cluster around His-35 side chain, T2 much shorter than average** ([`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l), sample `S1`): 10, 11, 37, 45, 88-90 and 114

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l) | 31 | 0 | 4 | 3 | Single-field 15N T1/T2/NOE model-free study of P. aeruginosa azurin plus a 1H EXSY exchange rate for His-35 de |

**Explicit figure-only, SI-only, or access gaps (3):**

- per-residue T1, T2, NOE, S2, Rex, tau_e, SSE for ~113 residues ([`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l)): figure only (Figures 1 and 3) and supplement not available (Supporting Information tables)
- Rex values of the eight residues with Rex 2-9.5 Hz other than G45 ([`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l)): figure only (Figure 3)
- EXSY cross-peak volume time course ([`10.1021/bi990624l`](https://doi.org/10.1021/bi990624l)): figure only (Figure 4)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
