# Viral macrophage inflammatory protein 2 (`VMIPII`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `Q98157` · **RelaxDB deposited card:** T = `n/a`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*24 rows total (24 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi9812726`](https://doi.org/10.1021/bi9812726) | `NMR_spin_relaxation_and_MF` | `target` | apo | S2 (8), other (8), tau_m (4), tau_e (2), T1 (1), T2 (1) | tau_m = 4.7 ns (global (34 rigid residues)) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **conformational exchange identified by eq 1 (T1/T2 criterion)** ([`10.1021/bi9812726`](https://doi.org/10.1021/bi9812726), sample `S1`): Asn25-Leu27, Asn36, Cys38, and Ala55
- **conformational exchange, ordered turn** ([`10.1021/bi9812726`](https://doi.org/10.1021/bi9812726), sample `S1`): 25-28
- **Rex term required (model II), 20 residues** ([`10.1021/bi9812726`](https://doi.org/10.1021/bi9812726), sample `S1`): Leu16-Lys20, Gln25-Leu28, Thr34, Gln36-Lys40, Ile44, Lys48, Val53, Ala55, Lys57
- **exchange with T1/T2 above 4.6 (additional to eq 1)** ([`10.1021/bi9812726`](https://doi.org/10.1021/bi9812726), sample `S1`): Leu37 and Ser39
- **model III (fast and intermediate time scales), 14 residues** ([`10.1021/bi9812726`](https://doi.org/10.1021/bi9812726), sample `S1`): Gly1-Arg10, Asp12, Lys13, Ala73, Arg74

### Conformational and complex PDB states (`States`)

- [`1CM9`](https://www.rcsb.org/structure/1CM9): CC-type dimer (crystal structure of wild type vMIP-II) ([`10.1021/bi100549y`](https://doi.org/10.1021/bi100549y))
- [`1VMP`](https://www.rcsb.org/structure/1VMP): monomeric vMIP-II (docking model) ([`10.1021/bi100549y`](https://doi.org/10.1021/bi100549y))
- [`2FHT`](https://www.rcsb.org/structure/2FHT): vMIP-II dimer (CC chemokine dimer stabilized by beta-sheet) ([`10.1126/science.1261064`](https://doi.org/10.1126/science.1261064))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (10):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi9812726`](https://doi.org/10.1021/bi9812726) | 24 | 0 | 5 | 2 |  |
| [`10.1007/s00345-010-0556-0`](https://doi.org/10.1007/s00345-010-0556-0) | 0 | 0 | 0 | 0 | Zero-row paper: an in vivo Fischer 344-to-Lewis rat kidney allograft transplantation study testing recombinant |
| [`10.1016/j.ejmech.2019.03.056`](https://doi.org/10.1016/j.ejmech.2019.03.056) | 0 | 0 | 0 | 0 | The paper designs CXCR4-binding peptides (AR5, AR6) from a vMIP-II N-terminal fragment (DV3) linked to a gp120 |
| [`10.1021/bi100549y`](https://doi.org/10.1021/bi100549y) | 0 | 2 | 0 | 0 | The paper maps heparin disaccharide and heparin-column binding of vMIP-II and its L13F dimer variant. It print |
| [`10.1021/bi2016712`](https://doi.org/10.1021/bi2016712) | 0 | 0 | 0 | 0 |  |
| [`10.1084/jem.191.1.171`](https://doi.org/10.1084/jem.191.1.171) | 0 | 0 | 0 | 0 | Zero dynamics rows (expected_rows = []), zero conformational PDB states (expected_states = []), and zero dynam |
| [`10.1126/science.1261064`](https://doi.org/10.1126/science.1261064) | 0 | 1 | 0 | 0 | Crystal structure paper; the text prints no NMR, HDX, FRET or other dynamics value for vMIP-II. Zero rows. |
| [`10.1161/atvbaha.120.315053`](https://doi.org/10.1161/atvbaha.120.315053) | 0 | 0 | 0 | 1 | This paper is a preclinical PET and fluorescence imaging study in murine atherosclerosis using three conjugate |
| [`10.1177/0963689718784957`](https://doi.org/10.1177/0963689718784957) | 0 | 0 | 0 | 0 | This paper investigates two synthetic D-amino-acid peptides derived from the N-terminus of vMIP-II—monomeric D |
| [`10.3390/ijms18081778`](https://doi.org/10.3390/ijms18081778) | 0 | 0 | 0 | 0 |  |

**Explicit figure-only, SI-only, or access gaps (3):**

- per-residue T1, T2, NOE, S2, tau_e, Rex values and HN exchange rates ([`10.1021/bi9812726`](https://doi.org/10.1021/bi9812726)): figure only (Figures 1 and 2)
- backbone chemical shifts ([`10.1021/bi9812726`](https://doi.org/10.1021/bi9812726)): in supplement not available (Table S1)
- Supplemental methods and Supplemental Figures I–V (including Supplemental Figure IVF–G for in vitro CXCR4/CXCR7 binding curves of fluorescence-conjugated vMIP-II) ([`10.1161/atvbaha.120.315053`](https://doi.org/10.1161/atvbaha.120.315053)): in supplement not available (supplement text is not included in 215.txt; note these assays measure tracer imaging, flow cytometry, and receptor binding rather than intramolecular protein dynamics)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
