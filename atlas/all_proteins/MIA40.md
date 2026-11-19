# Mitochondrial intermembrane space import and assembly protein 40 (`MIA40`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `Q8N4Q1` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`unknown`)](../proteins/MIA40.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `unknown` (strict two-peak reading: `cannot tell: No row states an exchange regime or shows a second peak set for MIA40 in any redox or binding state.`)
- **Reference state:** Free entry folded domain (41-106), oxidised with two structural disulfides, no substrate or partner; no BMRB id and no row describes this sample (the 2K3J structure deposition of full-length MIA40 lists 298 K, pH 7.0)
- **Exchange rate (`kex`):** not measured (MIA40-J3)
- **Minor-state population (`pB`):** not measured (MIA40-J3)
- **Exchanging region:** none for exchange; bound-state perturbations at C55, V88, F91 (entry 15, 48, 51; MIA40-J5) and SPS/AIA-A perturbations at F68, F72, F91 (entry 28, 32, 51; MIA40-J11)
- **Structure comparison:** [{"pdb": "2L0Y", "what": "C53S MIA40 disulfide-trapped with Cox17 C26/36/55S. MIA40 secondary structure is unchanged against free 2K3J; the CPC and hydrophobic cleft shift and the substrate folds a helix. A bound endpoint, not an apo alternate state.", "evidence_row": "MIA40-r2"}]
- **Caveats:** Oxidised, reduced and substrate-bound states are kept apart; none has an exchange measurement. The source of the RelaxDB MIA40 relaxation set is not identified (no BMRB id), and the entry construct lacks the N-terminal region that the 2025 paper shows packing against the active site, so the free entry domain may differ from full-length MIA40. Rows r8, r14 (in-cell redox state), r15 (negative binding control) and r16 (ITC) were not used.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/MIA40.md`](../proteins/MIA40.md) (12 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*1 rows total (1 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1038/nsmb.1553`](https://doi.org/10.1038/nsmb.1553) | `NMR_spin_relaxation_and_MF` | `target` | apo, reduced CPC (2S-S), 2 mM DTT | tau_m (1) | tau_m = 10.6 ns (whole molecule) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **highly flexible regions (low R2/R1, NOE below 0.5)** ([`10.1038/nsmb.1553`](https://doi.org/10.1038/nsmb.1553), sample `S1`): 1-41 and 107-142

### Conformational and complex PDB states (`States`)

- [`2K3J`](https://www.rcsb.org/structure/2K3J): solution structure of MIA402S-S ([`10.1038/nsmb.1553`](https://doi.org/10.1038/nsmb.1553))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1038/nsmb.1553`](https://doi.org/10.1038/nsmb.1553) | 1 | 1 | 1 | 1 | The paper is a structure and redox paper. Dynamics content is one printed number (the tumbling correlation tim |

**Explicit figure-only, SI-only, or access gaps (1):**

- per-residue 15N R1, R2 and NOE values (Fig. 4b, Supplementary Fig. 1) ([`10.1038/nsmb.1553`](https://doi.org/10.1038/nsmb.1553)): figure only

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
