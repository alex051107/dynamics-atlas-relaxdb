# S100 calcium-binding protein G (`CD9K`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P02633` · **RelaxDB deposited card:** T = `300.0`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`possible`)](../proteins/CD9K.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `possible` (strict two-peak reading: `cannot tell: for apo P43G the source states no exchange regime, prints no kex or Δω and shows no second peak set; exchange appears only as single-field model-free Rex at 14 amides, and the authors say further kinetic analysis is not possible (CD9K-J13, E-r4). P43G exists as a single isoform, so the two peak sets in slow exchange (3:1, 2D exchange) of native Pro43 calbindin in the Ca2+-loaded state (CD9K-J1; CD9K-r4, r9) do not exist in the entry construct.`)
- **Reference state:** Ca2+-free (apo) calbindin D9k in the entry construct P43G (the entry sequence carries G43), as measured in the RelaxDB source paper (doi:10.1021/bi00088a039, full text): 4 mM uniformly 15N P43G, 300 K, pH 6.0 (HCl, no buffer), 95% H2O/5% D2O, 11.74 T, single field (CD9K-J12, J13 marked is_wt_apo). The paper states that all its studies use P43G.
- **Exchange rate (`kex`):** not reported for apo P43G; Rex only, 0.32-2.39 s-1 at 14 residues (CD9K-J13, E-r4). The authors' 1 ms CPMG spacing argument (rates comparable to 2000 s-1) is an instrumental sensitivity statement, not a fitted rate.
- **Minor-state population (`pB`):** not reported for apo P43G (CD9K-J13); the only population-like numbers are contamination bounds (Ca2+-loaded below 0.5% in apo; Cd2-loaded fraction below 0.05 in (Cd2+)1).
- **Exchanging region:** Apo P43G (Table I Rex, s-1): G8 0.48, A14 0.44, A15 2.39, K16 0.40, E17 0.89, D19 1.32, L30 0.33, E35 0.56, E51 0.56, D54 0.33, K55 1.11, V61 1.11, V68 0.32, I73 0.65; Q75 R2 excluded for exchange (CD9K-J13). (Cd2+)1 P43G: A14, K16, G18, D19, Q22 substantial; E17, S24 undetected; A15, L23 unfittable; 21 numeric entries in all (CD9K-J15).
- **Caveats:** Call raised from unknown to possible on 2026-10-20 after the RelaxDB source paper (doi:10.1021/bi00088a039) was read in full: exchange is detected in the reference state (apo P43G, 300 K, pH 6.0) as single-field model-free Rex at 14 amides, and under the single-field Rex rule decided that night (ledger/redraft_notes.json, _RULE_single_field_rex) this counts as exchange detected without a population. Fixed caveat: single-field Rex can also come from anisotropic tumbling; a dispersion experiment would confirm. The construct question is settled (P43G for every sample in the paper), and P43G removes the Pro43 cis/trans two-isoform spectra, so no literal two-peak state exists in the entry construct. The apo sample has no buffer solute (pH set with HCl) and the Ca2+-loaded data are a reanalysis of a 1992 sample whose composition is not restated. Deamidation at N56 during urea preparation can create extra species that mimic a second conformer (CD9K-J26). The abstract-only rows CD9K-r2 and CD9K-r3 are superseded and no longer cited. the NMR collaborator is asked whether the RelaxDB set is the apo, (Cd2+)1 or Ca2+-loaded P43G sample.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/CD9K.md`](../proteins/CD9K.md) (19 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*801 rows total (801 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039) | `NMR_spin_relaxation_and_MF` | `target` | apo | S2 (78), R1 (72), R2 (72), NOE (72), tau_e (70), other (18) | S2 = 0.71 dimensionless (S02) |
| [`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039) | `NMR_spin_relaxation_and_MF` | `target` | (Cd2+)1: one cadmium ion bound in site I | S2 (74), R1 (70), NOE (70), R2 (68), tau_e (55), Rex (21) | S2 = 0.71 dimensionless (S02) |
| [`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039) | `NMR_spin_relaxation_and_MF` | `target` | (Ca2+)2: calcium ion bound in each site | other (10), tau_e (10), S2 (7), tau_m (2), R1 (1), R2 (1) | other = 0.80 dimensionless (G42) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **lower picosecond-nanosecond order parameters in the apo state than in the metal-bound states (C-terminal ion-binding loop II)** ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039), sample `S1`): G57, D58, G59, E60
- **substantial Rex terms (slower conformational exchange), unoccupied loop I of the (Cd2+)1 state** ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039), sample `S2`): A14, K16, G18, D19, Q22
- **exchange broadening in the 15N dimension, loop I of the (Cd2+)1 state (A15, L23 significantly; others slightly)** ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039), sample `S2`): significantly: A15, L23; slightly: A14, K16, G18, D19, Q22
- **cross-peaks not detected because of severe exchange broadening in the 1H dimension, loop I of the (Cd2+)1 state** ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039), sample `S2`): E17, S24 (printed El7)
- **two internal time scales needed (extended model-free), apo state** ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039), sample `S1`): K41, G42, G43, S44, G57, D58, G59, Q75
- **two internal time scales needed (extended model-free), (Cd2+)1 state** ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039), sample `S2`): K41, G42, G43, Q75
- **two internal time scales needed (extended model-free), (Ca2+)2 state** ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039), sample `S3`): G42, G43, S74, Q75
- **faster amide proton exchange with solvent in the (Cd2+)1 state than in the apo state, linked by the authors to conformational exchange** ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039), sample `S2`): A15, K16, D19, N21

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039) | 801 | 0 | 8 | 4 | 801 one-value rows: Table I (per-residue S2, tau_e, Rex for apo and (Cd2+)1), Table II (Sf2, Ss2, tau_e for ex |

**Explicit figure-only, SI-only, or access gaps (4):**

- Per-residue R1, R2, NOE of the (Ca2+)2 state at 11.74 T and the (Ca2+)2 ranges of these rates ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039)): in the earlier paper (Kordel et al. 1992), not in this text
- Order parameters and tau_e values shown only as plots (Figures 3 and 4) for residues not in Tables I and II ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039)): figure only
- Table I Rex cells marked 'ex' (A15, L23 in (Cd2+)1: exchange too fast to optimize) ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039)): no number printed
- Table I S2 and tau_e of (Ca2+)2 per residue ([`10.1021/bi00088a039`](https://doi.org/10.1021/bi00088a039)): not printed in this paper; only Tables II and III give (Ca2+)2 values

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
