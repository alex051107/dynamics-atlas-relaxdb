# Cellular retinoic acid-binding protein 2 (`CRABP2`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P29373` · **RelaxDB deposited card:** T = `298.0`, field = `900` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`yes`)](../proteins/CRABP2.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `yes` (strict two-peak reading: `does not: the authors describe the free-protein exchange as intermediate-timescale ('intermediate conformational exchange'), with broadened, unassignable amides near the exchanging residues; no second peak set is reported. The slow-exchange statement in the paper concerns atRA binding, not the apo state.`)
- **Reference state:** Entry construct as deposited (human CRABP2 P1-E137, wild type), free, no retinoid; measured at 298 K, pH 7.4, 20 mM sodium phosphate, 150 mM NaCl, 5 mM DTT, 10% D2O, 1.0 mM, Thio6His6 tag removed by TEV (2019 paper)
- **Exchange rate (`kex`):** 320 ± 40 s-1 (core-group global Carver-Richards fit, 298 K, 800 and 900 MHz) (CRABP2-J1, CRABP2-r5)
- **Minor-state population (`pB`):** 0.2 ± 0.03 (CRABP2-J1, CRABP2-r5)
- **Exchanging region:** Core group K8, L19, L22, K30, I31, A32, R59, E73, Q74, V76, T114, T131, Y134, plus 'Thr51-Ile53' which does not map to the entry sequence (Y51-I52-K53) and is left out (CRABP2-J1). Further dispersing residues are shown only in Fig. 5B (CRABP2-J2); 14 amides broadened beyond assignment: E13, E16, R29, A34-A36, K38, V41, T56-V58, T60, N115, V133 (CRABP2-J3).
- **Structure comparison:** [{"pdb": "2FR3", "what": "atRA-bound crystal structure. The authors find the CPMG-derived shifts do not agree with the apo-to-holo CSPs, so the minor state is structurally distinct from the atRA complex; not a match.", "evidence_row": "CRABP2-r5; CRABP2-r12"}, {"pdb": "2FS6", "what": "Apo crystal structure; pocket near-identical to 2FR3, so it shows the dominant conformer, not the CPMG minor state.", "evidence_row": "CRABP2-r12"}]
- **Caveats:** One paper, one temperature (298 K), phosphate buffer without a phosphate-free control, 1.0 mM protein; the supplement (Table S1, Figs. S4, S6) was not retrieved, so per-residue delta omega and the CPMG-versus-CSP comparison could not be checked. The core list contains a residue range that does not fit the entry sequence. A minor-state population of 0.2 is large for a CPMG fit and has no second method behind it. The RelaxDB CRABP2 source sample is unknown (no BMRB id). Built from case V6_r6_CRABP2_20261020094132; replaces the empty search_insufficient judgment of the crashed first search.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/CRABP2.md`](../proteins/CRABP2.md) (11 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

*2 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `kex` | 320 s-1 ± 40 | 16-residue core group (Lys8, Leu19, Leu22, Lys30-Ala32, Thr51-Ile | `NMR_exchange_and_dispersion` | `target` | apo; 298 K; pH 7.4; 900 and 800 | `yes` | [`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672) |
| `pB` | 0.2  ± 0.03 | core group | `NMR_exchange_and_dispersion` | `target` | apo; 298 K; pH 7.4; 900 and 800 | `yes` | [`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*12 rows total (8 spin-relaxation/model-free; 4 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672) | `NMR_spin_relaxation_and_MF` | `target` | apo | tau_m (1), NOE (1), R2 (1), R1 (1) | tau_m = 10.4 ns (global, mean of secondary-structure …) |
| [`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672) | `NMR_spin_relaxation_and_MF` | `target` | bound to all-trans retinoic acid (atRA) | tau_m (1), NOE (1), R2 (1), R1 (1) | tau_m = 15.1 ns (global, mean of secondary-structure …) |
| [`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672) | `Biophysics_and_other` | `same_protein_other_construct` | binding of atRA | other (3) | other = (6.92 ± 2.32) × 10 5 M-1 s-1 (whole protein (kon of atRA bindi |
| [`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672) | `NMR_other` | `target` | atRA:CRABP2 complex titrated 10 to 800 u | other (1) | other = 1.0 mM (atRA:CRABP2 dimer, residues mediatin…) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **microsecond-millisecond exchange, core group fit to one set of parameters (apo)** ([`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672), sample `S1`): Lys8 (β A), Leu19 (α 1), Leu22 (α 1), Lys30– Ala32 (α 2), Thr51–Ile53 (β C), Arg59 (β C− β D), Glu73 and Gln74 (β E), Val76 (β E− β F), Thr114 (β H− β I), Thr131 (β J), and Tyr134 (β J)
- **fast fluctuation in the atRA complex, distinct from the main process** ([`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672), sample `S2`): Ile10– Ser12 (β A), Leu19 (α 1), Lys38 (α 2− β B), Thr122–Thr124 (β I), Arg132 (β J)
- **largest CSPs on atRA:CRABP2 self-association (dimer interface)** ([`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672), sample `S3`): Val26, Leu28, Val58 (≥3 δ); Ile10, Lys20, Asn25, Lys30, Ile31, Val33, Ala35, Arg59, Asn115 (≥0.25 δ)
- **largest intensity decrease on self-association** ([`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672), sample `S3`): Ile10, Arg11, Asn115, Thr131 (≤2 δ)
- **residues whose quenched fast-time scale dynamics follow atRA binding** ([`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672), sample `S2`): Arg59-Glu62 (β C-β D loop), Val76 and Asp77 (β E-β F loop)
- **residues with unassigned resonances due to line broadening, near intermediate exchange** ([`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672), sample `S1`): Glu13, Glu16, Arg29, Ala34–Ala36, Lys38, Val41, Thr56–Val58, Thr60, Asn115, Val133

### Conformational and complex PDB states (`States`)

- [`2FS6`](https://www.rcsb.org/structure/2FS6): free (apo) CRABP2 crystal structure, 1.35 Å ([`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672))
- [`2FR3`](https://www.rcsb.org/structure/2FR3): atRA-bound CRABP2 crystal structure, 1.48 Å; monomeric asymmetric unit used to model the crystallographic dimer ([`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672) | 14 | 2 | 6 | 2 |  |

**Explicit figure-only, SI-only, or access gaps (2):**

- Per-residue kex, pB, delta-omega and Rex from the CPMG fits (Table S1) ([`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672)): in supplement not available
- Per-residue R1, R2, NOE (Figure 3), R2eff (Figure 5), CSP and intensity ratios (Figures 2, 4) ([`10.1021/acs.biochem.9b00672`](https://doi.org/10.1021/acs.biochem.9b00672)): figure only

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
