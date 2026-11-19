# Peptidyl-tRNA hydrolase (`VCPTH`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P0A7D1` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `700` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`possible`)](../proteins/VCPTH.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `possible` (strict two-peak reading: `does not: The only stated regime is the authors' reading of the missing N118 amide as intermediate exchange; no dispersion was recorded and no second peak set is reported.`)
- **Reference state:** Wild-type apo (no substrate), 298 K, pH 6.5, 20 mM NaH2PO4, 50 mM NaCl, 1 mM DTT, 0.1% NaN3, 0.5 mM 15N; 700 MHz, single field
- **Exchange rate (`kex`):** not measured (VCPTH-J3, VCPTH-J12)
- **Minor-state population (`pB`):** not measured (VCPTH-J3, VCPTH-J4)
- **Exchanging region:** Rex at T22 (next to catalytic H24), A79, base loop G115–H117 at the helix α3 N-terminus, lid D147 and H192 in the C-terminal hairpin (VCPTH-J3); missing amides N118 (helix α3 N-cap) and K146 (lid flap) (VCPTH-J4).
- **Structure comparison:** [{"pdb": "5IMB; 5B6J", "what": "N14D and H24N mutant crystals in which H24 hydrogen-bonds N14. The authors propose that wild-type side chains switch between the N14 and N118 bonds in solution; no experiment shows the wild type interconverting.", "evidence_row": "VCPTH-r7"}, {"pdb": "5IKE; 4Z86", "what": "D97N and N118D mutant crystals in which H24 hydrogen-bonds N118/D118, the other half of the proposed switch. Static mutant structures, no rate.", "evidence_row": "VCPTH-r7"}]
- **Caveats:** Call changed from unknown to possible on 2026-10-20 by the single-field Rex rule (ledger/redraft_notes.json, _RULE_single_field_rex), not by new evidence: the judgments (VCPTH-J3, J4) stay unresolved, and the only us-ms evidence is still the single-field model-free Rex and the missing N118/K146 amides of the 2017 paper. Fixed caveat: single-field Rex can also come from anisotropic tumbling; a dispersion experiment would confirm. the NMR collaborator is asked whether single-field model-free Rex should count as us-ms detection. The input card pairs the V. cholerae sequence and 2MJL with UniProt P0A7D1 (E. coli Pth); V. cholerae Pth is treated as the entry. All VcPth NMR uses phosphate, which could occupy the basic 5'-phosphate clamp, with no control. One 2017 paper supplies every VcPth row.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/VCPTH.md`](../proteins/VCPTH.md) (7 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*1310 rows total (1310 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | apo (no ligand stated) | NOE (302), R1 (295), R2 (293) | R1 = 1.5705 s-1 (residue 1) |
| [`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116) | `NMR_spin_relaxation_and_MF` | `target` | apo (no ligand stated) | R1 (140), R2 (140), NOE (140) | R1 = 1.4967 s-1 (residue 1) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **slow time scale motion with Rex term, wt-VcPth (model-free)** ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116), sample `S1`): T22, A79, G115-H117, D147, H192
- **fast time scale motion with tau_e term, wt-VcPth (model-free)** ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116), sample `S1`): L42, F49, N58, S59, Y85, H145
- **increased fast motion in H24N beyond wt** ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116), sample `S2`): A13, M71, N72, G116, N118
- **slow motion in H24N, hinge residues** ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116), sample `S2`): G139, L154
- **slow motion from R2/R1 ratios, wt-VcPth: region next to H24, hinge of lid loop** ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116), sample `S1`): H24 region, G139, V153
- **fast motion from R2/R1 ratios, wt-VcPth** ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116), sample `S1`): N58, N72, H145, D147

### Conformational and complex PDB states (`States`)

- [`2MJL`](https://www.rcsb.org/structure/2MJL): wt-VcPth solution structure (NMR ensemble of 10 conformers) ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116))
- [`4ZXP`](https://www.rcsb.org/structure/4ZXP): wt-VcPth crystal structure with bound citrate, two molecules in the asymmetric unit ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116))
- [`5VGZ`](https://www.rcsb.org/structure/5VGZ): wt-VcPth crystal structure without citrate, one molecule in the asymmetric unit ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116) | 1310 | 3 | 6 | 4 |  |

**Explicit figure-only, SI-only, or access gaps (4):**

- Model-free S2, tau_e and Rex per residue for wt, H24N, N118D ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116)): figure only (Figure 5); no printed values
- MD RMSF per residue for wt and four mutants ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116)): figure only (Figure 6); simulation, not NMR dynamics
- R2/R1 ratio profiles ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116)): figure only (Supplemental Figure S5)
- Relaxation entries marked with dashes in Supplemental Table S5 (for example residues 4, 5, 9, 13, 15-17 in some columns) ([`10.1261/rna.057620.116`](https://doi.org/10.1261/rna.057620.116)): the paper states these could not be calculated (no assignment, overlap or weak intensity); no value printed

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
