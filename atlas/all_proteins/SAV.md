# Subtilisin Savinase (`SAV`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P29600` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*2 rows total (0 spin-relaxation/model-free; 2 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408) | `HDX_NMR_and_MS` | `target` | apo | other (1) | other = 40% % exchangeable hydrogens replaced by deuterium at 60 min ( |
| [`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408) | `HDX_NMR_and_MS` | `same_protein_other_construct` | bound to PMSF | other (1) | other = 42% % exchangeable hydrogens replaced by deuterium at 60 min ( |

## 3. Computational (MD/MSM) and cryo-structure (X-ray / cryo-EM) rows

*2 rows intentionally separated from experimental solution dynamics pending expert scope lock:*

| Method group | Quantity | Value | Residues / group | Paper |
|---|---|---|---|---|
| `Xray_and_CryoEM` | `population` | 73% % occupancy | Ser-215 side chain, rotamer 1 | [`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408) |
| `Xray_and_CryoEM` | `population` | 27% % occupancy | Ser-215 side chain, rotamer 2 | [`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408) |

## 4. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **almost fully exchanged within 15 s (flexible, HDX-MS)** ([`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408), sample `S2`): 123-133
- **almost no exchange within 60 min (HDX-MS)** ([`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408), sample `S2`): 119-122 and 217-227
- **significantly reduced HDX upon PMSF binding** ([`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408), sample `S3`): 147-168 and 184-190/191
- **alternative main-chain conformation in cryo crystal** ([`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408), sample `S4`): 128-132
- **alternative conformations in both RT and cryo crystals** ([`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408), sample `S4`): 103-104
- **14 residues with significant curvature in 1HN shift vs T (NMR)** ([`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408), sample `S1`): 14 residues scattered over the protein (identities in Fig. S1)

## 5. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408) | 4 | 0 | 6 | 4 | The paper prints no NMR relaxation or exchange rate for Savinase. It prints global HDX-MS deuteration fraction |

**Explicit figure-only, SI-only, or access gaps (4):**

- per-residue 1HN temperature coefficients (dδ/dT) ([`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408)): figure only (Fig. 1B), no printed numbers
- local HDX uptake per peptide and time point ([`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408)): in supplement not available (Table S1, Table S2, Fig. S3)
- list of residues with alternative conformations in RT and cryo crystals ([`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408)): in supplement not available (Table S4)
- identities of the 14 residues with curved shift vs T ([`10.7717/peerj.9408`](https://doi.org/10.7717/peerj.9408)): figure only (Fig. S1), supplement not available

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
