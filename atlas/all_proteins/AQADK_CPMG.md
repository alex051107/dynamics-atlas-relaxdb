# AqAdK (`AQADK_CPMG`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `O66490` · **RelaxDB deposited card:** T = `n/a`, field = `n/a` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`possible`)](../proteins/AQADK_CPMG.md) · [Release 0.1 PDB overlay table](../../data/structures/AQADK_CPMG.md)

> **Audit note:** Twin UniProt O66490 (shared with AQADK)

> **Shared UniProt (`O66490`):** Also filed in RelaxDB under [`AQADK`](AQADK.md). Inspect both entries together when synthesizing canonical protein behavior.

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `possible` (strict two-peak reading: `does not: Authors call the 20 °C apo exchange fast with small amplitude; no regime stated at 10 °C, no apo Δω, and no minor-state peaks reported.`)
- **Reference state:** Wild-type apo Adk, no ligand; 10 °C (perdeuterated) and 20 °C (protonated); pH 7.0, 40 mM MOPS, 50 mM NaCl (NMR buffer stated for the perdeuterated sample; the 20 °C protonated buffer is not stated separately)
- **Exchange rate (`kex`):** 950 ± 150 s-1 at 10 °C (AQADK-J1, AQADK-r1); 2,000–7,000 s-1 compatible range at 20 °C, no unique fit (AQADK-J2, AQADK-r2)
- **Minor-state population (`pB`):** not reported for apo; the authors say the small dispersion amplitude hampered characterization of the nature of the transition (AQADK-J1)
- **Exchanging region:** Hinges and parts of both lids (AMP lid 30–71 and ATP lid 111–169 are the lid domains as defined for TLS refinement, AQADK-J5, not the exchanging region). Exchanging residues are shown only as a colour map at 10 °C (Fig. 3c) and as selected curves at 20 °C (Supplementary Fig. S6), with no residue list (AQADK-J1, AQADK-J2).
- **Structure comparison:** [{"pdb": "2RGX", "what": "Closed Zn2+–Ap5A inhibitor complex. PRE from a spin label on the AMP lid of the apo Y52C construct broadens ATP-lid residues, which the authors read as closed-like distances when compared with the open apo substates and the inhibitor-bound structure. Labelled construct, no population or rate.", "evidence_row": "AQADK-r4; AQADK-r8"}, {"pdb": "2RH5", "what": "Apo crystal with three molecules (A, B, C) at different degrees of lid closure along the hinge path that the Ap5A complex completes. Crystal snapshots, no solution population or rate. The authors note the three substates seem to be stabilized by crystal contacts.", "evidence_row": "AQADK-r7; AQADK-r8"}]
- **Caveats:** The closed-like identity of the apo minor state comes from labelled constructs (Y52C PRE, Y52C/V145C smFRET), so it is mutant-based inference; the PDB entries are crystal endpoints, not a solved minor state. the NMR collaborator is asked which sample the RelaxDB labels come from (10 °C apo, 20 °C apo or 20 °C Mg-ADP turnover). Homolog rows (E. coli, P. profundum, G. stearothermophilus Adk) were not used for the call.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/AQADK_CPMG.md`](../proteins/AQADK_CPMG.md) (12 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

*63 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `kex` | 950 s21 150 (s.d.) | most exchanging residues | `NMR_exchange_and_dispersion` | `target` | apo (ligand-free); 10 uC (CPMG); 20 uC (R2 eff profiles too fast, Supplementary Fig. | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kex` | 300 s21 150 (s.d.) | exchanging residues (Mg2+.Ap5A-bound) | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `population` | 95 % 2 | closed state population (Mg2+.Ap5A-bound) | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kex` | 2,000–7,000 s21 | apo exchanging residues, 20 uC | `NMR_exchange_and_dispersion` | `target` | apo (ligand-free); 10 uC (CPMG); 20 uC (R2 eff profiles too fast, Supplementary Fig. | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kex` | 2000 and 7000 s-1 | kopen + kclose, apo, 20 uC | `NMR_exchange_and_dispersion` | `target` | apo (ligand-free); 10 uC (CPMG); 20 uC (R2 eff profiles too fast, Supplementary Fig. | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kex` | 600 s-1 300 (s.d.) | FRET-labelled Mg2+.Ap5A Adk, 30 uC | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | Mg2+.Ap5A-bound; 30 uC (CPMG); pH not stated for NMR; not stated | `no` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kex` | about 300 s-1 | wild-type Mg2+.Ap5A-bound Adk, 20 uC (restated in SI) | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kopen` | 6,500 s21 500 (s.d.) | ligand-free Adk | `FRET_and_fluorescence` | `same_protein_other_construct` | apo (ligand-free); room temperature; pH 7.0; not applicable | `no` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kclose` | 2,000 s21 200 (s.d.) | ligand-free Adk | `FRET_and_fluorescence` | `same_protein_other_construct` | apo (ligand-free); room temperature; pH 7.0; not applicable | `no` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kex` | 7,000 s21 2,000 (s.d.) | overall opening/closing rate, ligand-free Adk | `FRET_and_fluorescence` | `same_protein_other_construct` | apo (ligand-free); room temperature; pH 7.0; not applicable | `no` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kex` | 7,000 s–1 1,500 (s.d.) | overall opening/closing rate, ligand-free Adk | `FRET_and_fluorescence` | `same_protein_other_construct` | apo (ligand-free); room temperature; pH 7.0; not applicable | `no` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kex` | 8,500 s–1 700 (s.d.) | overall opening+closing rate from state analysis, ligand-free Adk | `FRET_and_fluorescence` | `same_protein_other_construct` | apo (ligand-free); room temperature; pH 7.0; not applicable | `no` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kex` | about 8,500 s–1 | opening/closing rate at room temperature, ligand-free | `FRET_and_fluorescence` | `same_protein_other_construct` | apo (ligand-free); room temperature; pH 7.0; not applicable | `no` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kopen` | 40 s -1 20 (s.d.) | Mg2+.Ap5A-bound Adk | `FRET_and_fluorescence` | `same_protein_other_construct` | Mg2+.Ap5A-bound (4 mM Ap5A, 2 mM MgCl2); room temperature; pH 7.0; not applicable | `no` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kclose` | 350 s -1 200 (s.d.) | Mg2+.Ap5A-bound Adk | `FRET_and_fluorescence` | `same_protein_other_construct` | Mg2+.Ap5A-bound (4 mM Ap5A, 2 mM MgCl2); room temperature; pH 7.0; not applicable | `no` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kex` | about 1000 s-1 | overall opening/closing rate, Mg2+.Ap5A-bound Adk | `FRET_and_fluorescence` | `same_protein_other_construct` | Mg2+.Ap5A-bound (4 mM Ap5A, 2 mM MgCl2); room temperature; pH 7.0; not applicable | `no` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `kex` | about 390 s-1 | lid opening/closing, smFRET room temperature | `FRET_and_fluorescence` | `same_protein_other_construct` | Mg2+.Ap5A-bound (4 mM Ap5A, 2 mM MgCl2); room temperature; pH 7.0; not applicable | `no` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.75 ppm 0.20 | residue 17 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.75 ppm 0.20 | residue 21 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.55 ppm 0.20 | residue 27 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.30 ppm 0.15 | residue 40 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.35 ppm 0.20 | residue 52 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.40 ppm 0.20 | residue 80 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.45 ppm 0.20 | residue 81 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 1.20 ppm 0.25 | residue 117 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 1.10 ppm 0.25 | residue 126 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.40 ppm 0.20 | residue 127 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.70 ppm 0.20 | residue 133 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.30 ppm 0.15 | residue 134 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.65 ppm 0.20 | residue 151 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.50 ppm 0.20 | residue 154 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.70 ppm 0.20 | residue 159 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.45 ppm 0.20 | residue 162 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.50 ppm 0.20 | residue 6 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.55 ppm 0.20 | residue 7 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.35 ppm 0.20 | residue 28 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.30 ppm 0.15 | residue 29 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.95 ppm 0.25 | residue 33 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.35 ppm 0.20 | residue 34 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.85 ppm 0.20 | residue 37 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.20 ppm 0.10 | residue 38 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.40 ppm 0.20 | residue 39 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.45 ppm 0.20 | residue 53 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.70 ppm 0.20 | residue 109 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.70 ppm 0.20 | residue 111 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 1.50 ppm 0.30 | residue 112 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.85 ppm 0.20 | residue 122 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.90 ppm 0.25 | residue 124 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.40 ppm 0.20 | residue 135 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.25 ppm 0.15 | residue 139 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 1.10 ppm 0.25 | residue 149 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.35 ppm 0.20 | residue 153 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 1.05 ppm 0.25 | residue 169 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 1.15 ppm 0.25 | residue 185 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.40 ppm 0.20 | residue 187 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.20 ppm 0.20 | residue 188 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.25 ppm 0.15 | residue 192 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.25 ppm 0.15 | residue 26 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.35 ppm 0.20 | residue 66 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |
| `delta_omega` | 0.35 ppm 0.20 | residue 160 | `NMR_exchange_and_dispersion` | `target` | Mg2+.Ap5A-bound (saturating); 20 uC; pH 7.0; not stated per experiment | `unclear` | [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) |

*Showing first 60 of 63 experimental exchange rows; see `Exchange_Highlights` tab in the workbook for all rows and verbatim quotes.*

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*2 rows total (1 spin-relaxation/model-free; 1 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) | `NMR_exchange_and_dispersion` | `target` | apo (ligand-free) | R2 (1) | R2 = between 15 s–1 and 23 s–1 s–1 (R20 of non-exchanging residues) |
| [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) | `FRET_and_fluorescence` | `same_protein_other_construct` | Mg2+.Ap5A-bound (4 mM Ap5A, 2 mM MgCl2) | other (1) | other = 0.83 Et (major FRET population, Mg2+.Ap5A-bou…) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **residues with conformational exchange in apo Adk are in hinge regions and parts of both lids** ([`10.1038/nature06410`](https://doi.org/10.1038/nature06410), sample `S1`): hinge regions and parts of both lids (no residue numbers printed)

### Conformational and complex PDB states (`States`)

- [`2RH5`](https://www.rcsb.org/structure/2RH5): apo Aquifex Adk, three molecules A, B, C in asymmetric unit (open, partly closed substates) ([`10.1038/nature06410`](https://doi.org/10.1038/nature06410))
- [`2RGX`](https://www.rcsb.org/structure/2RGX): Zn.Ap5A-bound Aquifex Adk (closed) ([`10.1038/nature06410`](https://doi.org/10.1038/nature06410))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1038/nature06410`](https://doi.org/10.1038/nature06410) | 65 | 2 | 1 | 4 | Henzler-Wildman 2007: lid-motion kinetics of Aquifex Adk by 15N CPMG (apo 950 s-1 at 10 C; Ap5A-bound 300 s-1  |

**Explicit figure-only, SI-only, or access gaps (4):**

- Per-residue R2eff vs nuCPMG dispersion profiles (apo 10 uC, Ap5A 20 uC) ([`10.1038/nature06410`](https://doi.org/10.1038/nature06410)): figure only (Fig. 3a,b; Figs S6a, S7)
- PRE-derived distances from Y52C spin label to amide protons ([`10.1038/nature06410`](https://doi.org/10.1038/nature06410)): figure only (Fig. 3e)
- Observed rates in Fig. S15 (10 W vs 30 W lifetime fits) and Fig. S17 simulation/experiment rates ([`10.1038/nature06410`](https://doi.org/10.1038/nature06410)): values are labels inside figure graphics, not caption text, or simulated
- Per-residue apo CPMG fit parameters (Rex, pB, dw) ([`10.1038/nature06410`](https://doi.org/10.1038/nature06410)): not printed in the text

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
