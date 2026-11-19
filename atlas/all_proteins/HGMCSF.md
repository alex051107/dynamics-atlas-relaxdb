# Granulocyte-macrophage colony-stimulating factor (`HGMCSF`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P09919` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

> **Audit note:** Card mismatch: labeled GM-CSF, but UniProt P09919 & papers are G-CSF

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*654 rows total (643 spin-relaxation/model-free; 11 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi00194a009`](https://doi.org/10.1021/bi00194a009) | `NMR_spin_relaxation_and_MF` | `target` | apo | Rex (154), S2 (153), T1 (117), T2 (97), NOE (90), tau_e (24) | other = 988 ms (mean over 138 residues with T1) |
| [`10.1021/acs.molpharmaceut.3c01211`](https://doi.org/10.1021/acs.molpharmaceut.3c01211) | `HDX_NMR_and_MS` | `target` | excipient: none (control) | other (3) | other = 2.7 % of max exchangeable peptide protons (all peptides (total |
| [`10.1021/acs.molpharmaceut.3c01211`](https://doi.org/10.1021/acs.molpharmaceut.3c01211) | `HDX_NMR_and_MS` | `target` | excipient: mannitol | other (3) | other = 7.6 % of max exchangeable peptide protons (all peptides (total |
| [`10.1021/acs.molpharmaceut.3c01211`](https://doi.org/10.1021/acs.molpharmaceut.3c01211) | `HDX_NMR_and_MS` | `target` | excipient: phenylalanine | other (3) | other = 9.0 % of max exchangeable peptide protons (all peptides (total |
| [`10.1021/acs.molpharmaceut.3c01211`](https://doi.org/10.1021/acs.molpharmaceut.3c01211) | `HDX_NMR_and_MS` | `target` | excipient: sucrose | other (2) | other = 7.2 % of max exchangeable peptide protons (all peptides (total |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **increased backbone mobility (lower order parameters) at pH 4.0** ([`10.1021/acsomega.0c04692`](https://doi.org/10.1021/acsomega.0c04692), sample `S1`): 126–145 (CD-loop)
- **long CD loop with fast internal motion (low NOE, long T2, low S2)** ([`10.1021/bi00194a009`](https://doi.org/10.1021/bi00194a009), sample `S1`): 126 to 144
- **region where anisotropic motion shows opposite T1 and T2 trends** ([`10.1021/bi00194a009`](https://doi.org/10.1021/bi00194a009), sample `S1`): 127-136

### Conformational and complex PDB states (`States`)

- [`1GNC`](https://www.rcsb.org/structure/1GNC): Three-dimensional structure of Met-G-CSF ([`10.1371/journal.pone.0042511`](https://doi.org/10.1371/journal.pone.0042511))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (15):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi00194a009`](https://doi.org/10.1021/bi00194a009) | 643 | 0 | 2 | 4 |  |
| [`10.1021/acs.molpharmaceut.3c01211`](https://doi.org/10.1021/acs.molpharmaceut.3c01211) | 11 | 0 | 0 | 2 | The paper measures solid-state HDX-MS on lyophilized human G-CSF, a different protein from GM-CSF (P09919). No |
| [`10.1007/s40268-024-00471-9`](https://doi.org/10.1007/s40268-024-00471-9) | 0 | 0 | 0 | 1 |  |
| [`10.1016/j.csbj.2022.03.012`](https://doi.org/10.1016/j.csbj.2022.03.012) | 0 | 0 | 0 | 0 | Zero rows. The paper studies granulocyte colony-stimulating factor (GCSF, filgrastim), not GM-CSF, and prints  |
| [`10.1021/acs.molpharmaceut.2c00398`](https://doi.org/10.1021/acs.molpharmaceut.2c00398) | 0 | 0 | 0 | 0 |  |
| [`10.1021/acsomega.0c04692`](https://doi.org/10.1021/acsomega.0c04692) | 0 | 0 | 1 | 4 | The text prints no numeric dynamics value for this protein. Order parameters, T1, T2 and hetNOE sit in Figures |
| [`10.1038/s41598-020-59346-z`](https://doi.org/10.1038/s41598-020-59346-z) | 0 | 0 | 0 | 4 | This paper studies human G-CSF (UniProt P09919) as pegfilgrastim (~20 kDa PEG covalently conjugated to the N-t |
| [`10.1038/s41598-025-29790-w`](https://doi.org/10.1038/s41598-025-29790-w) | 0 | 0 | 0 | 0 |  |
| [`10.1038/srep32201`](https://doi.org/10.1038/srep32201) | 0 | 0 | 0 | 0 | This paper demonstrates an NMR higher-order structure (HOS) biosimilarity comparability workflow on human G-CS |
| [`10.1039/d6cb00019c`](https://doi.org/10.1039/d6cb00019c) | 0 | 0 | 0 | 4 | The paper reports NMR T1, T2, NOE and CPMG relaxation dispersion for WT and His mutants of GM-CSF only as corr |
| [`10.1084/jem.185.11.1939`](https://doi.org/10.1084/jem.185.11.1939) | 0 | 0 | 0 | 0 | This paper studies human granulocyte/macrophage colony-stimulating factor (GM-CSF) and its receptor subunits G |
| [`10.1371/journal.pone.0042511`](https://doi.org/10.1371/journal.pone.0042511) | 0 | 1 | 0 | 0 | Zero-row biophysical stability and aggregation characterization paper (0 expected_rows, 1 expected_state for P |
| [`10.22074/cellj.2020.6158`](https://doi.org/10.22074/cellj.2020.6158) | 0 | 0 | 0 | 1 |  |
| [`10.3390/ijms25010030`](https://doi.org/10.3390/ijms25010030) | 0 | 0 | 0 | 0 | This paper fabricates and evaluates chitosan/TPP-crosslinked Ligasano polyurethane foam wound dressings loaded |
| [`10.3390/ijms26062689`](https://doi.org/10.3390/ijms26062689) | 0 | 0 | 0 | 0 | This paper prepares and characterizes soy phosphatidylcholine liposomes encapsulating human granulocyte colony |

**Explicit figure-only, SI-only, or access gaps (20):**

- HDX deuterium uptake of pegfilgrastim peptides (Fig. 4) ([`10.1007/s40268-024-00471-9`](https://doi.org/10.1007/s40268-024-00471-9)): figure only
- per-peptide ssHDX-MS deuterium uptake / differential exchange of lyophilized G-CSF per excipient (120 min) ([`10.1021/acs.molpharmaceut.3c01211`](https://doi.org/10.1021/acs.molpharmaceut.3c01211)): figure only (Figure 2); no printed per-peptide values
- peptide-level fractional exchange plots for all time points up to 420 min, and arginine/glycine uptake comparison ([`10.1021/acs.molpharmaceut.3c01211`](https://doi.org/10.1021/acs.molpharmaceut.3c01211)): in supplement not available (Supporting Information Figures S2, S3); B3 text has no SI
- Per-residue order parameters at pH 4.0, 5.0 and 6.0 ([`10.1021/acsomega.0c04692`](https://doi.org/10.1021/acsomega.0c04692)): figure only (Figure S3, supplement not in text)
- Structural-element averaged order parameters at three pH values ([`10.1021/acsomega.0c04692`](https://doi.org/10.1021/acsomega.0c04692)): figure only (Figure 4A, no printed numbers)
- Order parameters at 0 and 793 mM sorbitol, and rotational diffusion tensors ([`10.1021/acsomega.0c04692`](https://doi.org/10.1021/acsomega.0c04692)): figure only (Figure 7A) or in supplement not available (Figures S5, S6)
- T1, T2 and hetNOE for polysorbate-80, polysorbate-20 and sorbitol samples ([`10.1021/acsomega.0c04692`](https://doi.org/10.1021/acsomega.0c04692)): in supplement not available (Figures S1, S2, S4)
- TABLE IIS residues 1-28 (T1, T2, NOE) ([`10.1021/bi00194a009`](https://doi.org/10.1021/bi00194a009)): garbled table: residue numbers are detached from the values on the first page, so values cannot be bound to residues
- TABLE IVS residues 1-28 (anisotropic Rex, S2, tau_e) ([`10.1021/bi00194a009`](https://doi.org/10.1021/bi00194a009)): garbled table: residue numbers are misaligned with the value rows on the first page
- Individual table cells with OCR errors, for example NOE of residue 90 printed 'C.90', NOE of residue 91 printed '0 88', residue 68 printed '6*', tau_e printed '4.54e-l 1' ([`10.1021/bi00194a009`](https://doi.org/10.1021/bi00194a009)): garbled table cell; skipped
- Fit error column of TABLES IVS and VS, S2 and tau_e plots of Figures 8 and 1S-2S ([`10.1021/bi00194a009`](https://doi.org/10.1021/bi00194a009)): fit error is not a dynamics value; plots are figure only
- Real-time 1D 1H NMR amide-region and PEG peak spectra and intensity changes at 1 h, 20 h, and 43 h (over 48 h time course) in formulation buffer, 0.5 × PBS, and DMEM ([`10.1038/s41598-020-59346-z`](https://doi.org/10.1038/s41598-020-59346-z)): figure only (Figure 3); no numerical NMR peak intensities, linewidths, or decay rates are printed in the text
- *... plus 8 additional gap entries in the `Gaps` tab.*

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
