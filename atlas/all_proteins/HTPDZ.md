# Serine protease HTRA2, mitochondrial (`HTPDZ`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `O43464` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

> **Audit note:** Twin UniProt O43464 (Release 0.1 page under HTPDZ_CPMG)

> **Shared UniProt (`O43464`):** Also filed in RelaxDB under [`HTPDZ_CPMG`](HTPDZ_CPMG.md). Inspect both entries together when synthesizing canonical protein behavior.

## 1. Experimental conformational exchange (rates, populations, Δω)

*7 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `pB` | 16.1 % | global minor state (283 K) | `NMR_exchange_and_dispersion` | `target` | apo; 298 K (283 K for part of CPMG); pH 7.4 (PBS, sample buffer for HtrA2-PDZ); 700, | `unclear` | [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) |
| `pB` | 15.2 % | global minor state (298 K) | `NMR_exchange_and_dispersion` | `target` | apo; 298 K (283 K for part of CPMG); pH 7.4 (PBS, sample buffer for HtrA2-PDZ); 700, | `unclear` | [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) |
| `pB` | 16.6 % ± 0.4 | methyl groups in a5-b15 and b16/a7 | `NMR_exchange_and_dispersion` | `target` | apo; 298 K; pH not stated (99.9% D2O based NMR buffer); 700 (16.4 T), 800 (18.8 T) fo | `unclear` | [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) |
| `kopen` | 84.3 s-1 ± 29 | Ca2+ koff, PDZ | `NMR_exchange_and_dispersion` | `target` | Ca2+ or Zn2+ titration; DD-PDZOpt titration; 298 K; pH 7.4 (PBS); not stated per titr | `no` | [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) |
| `kopen` | 52.8 s-1 ± 15.3 | Zn2+ koff, PDZ | `NMR_exchange_and_dispersion` | `target` | Ca2+ or Zn2+ titration; DD-PDZOpt titration; 298 K; pH 7.4 (PBS); not stated per titr | `no` | [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) |
| `kopen` | 48.5 s-1 ± 2.9 | DD-PDZOpt koff, PDZ | `NMR_exchange_and_dispersion` | `target` | Ca2+ or Zn2+ titration; DD-PDZOpt titration; 298 K; pH 7.4 (PBS); not stated per titr | `no` | [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) |
| `population` | ~20 % | I164 and I166 gauche(-) population increase on peptide binding | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | apo and bound to DD-PDZOpt peptide; 298 K; pH 8 (25 mM Tris-HCl pH 8, 0.1 M NaCl, 1 m | `no` | [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*23 rows total (17 spin-relaxation/model-free; 6 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | apo and bound to DD-PDZOpt peptide | S2 (6) | S2 = 38 ns (protease domain methyls (S2axis*tauC…) |
| [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) | `NMR_spin_relaxation_and_MF` | `target` | apo | S2 (2), tau_m (1), other (1), tau_s (1) | tau_m = 8.2 ns (whole domain (average)) |
| [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | apo and bound to DD-PDZOpt peptide | R2 (3), other (1) | R2 = 31.8 s-1 (MQ rate at 750 Hz, apo, average) |
| [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) | `NMR_exchange_and_dispersion` | `target` | apo | tau_e (3) | tau_e = 0.98 ms (global (residues with dispersion)) |
| [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) | `NMR_exchange_and_dispersion` | `target` | Ca2+ or Zn2+ titration; DD-PDZOpt titrat | other (3) | other = 4.1 mM (Ca2+ KD, PDZ) |
| [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) | `Biophysics_and_other` | `target` | apo / metal / peptide | other (2) | other = 13 mM (PDZ dimerization KD (lower limit)) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **micro- to millisecond exchange by 15N CPMG at 298 K** ([`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5), sample `S1`): amino-terminus, the α5 helix and the adjacent loop connecting to β15, as well as α7 and its preceding loop
- **methyl MQ CPMG exchange** ([`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5), sample `S2`): α5 to β15 region and β16/α7
- **elevated Rex** ([`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5), sample `S1`): β15 preceding linker region, α6, α7 and the linker between α7 and β17

### Conformational and complex PDB states (`States`)

- [`1LCY`](https://www.rcsb.org/structure/1LCY): crystal structure of the HtrA2-PDZ domain used for tensor fit and mapping ([`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5))
- [`5M3N`](https://www.rcsb.org/structure/5M3N): closed inactive state of HtrA2 ([`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5))
- [`2PZD`](https://www.rcsb.org/structure/2PZD): HtrA2 PDZ with related activating peptide (peptide-bound arrangement) ([`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5) | 30 | 3 | 3 | 3 | 30 rows: backbone and methyl dynamics of the isolated HtrA2-PDZ domain (tau_c, S2, global CPMG timescale and m |

**Explicit figure-only, SI-only, or access gaps (3):**

- Per-residue S2, Rex, tau_c, DeltaR2eff, S2axis*tauC values (Fig. 1e-g, 2a,b,d-f, Suppl. Figs. 4, 5, 17) ([`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5)): figure only; the numeric Source Data spreadsheet is appended to the text as unlabelled columns, not printed in the paper
- Per-residue dispersion profiles and fitted deltaomega ([`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5)): figure only, no printed number
- Rotamer population changes for I362, M366, I373, I397 ([`10.1038/s41467-024-48997-5`](https://doi.org/10.1038/s41467-024-48997-5)): figure only (Fig. 4f)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
