# Insulin receptor substrate 1 (`IRSPTB`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P35568` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*91 rows total (91 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi801096b`](https://doi.org/10.1021/bi801096b) | `NMR_spin_relaxation_and_MF` | `target` | bound to IL-4 receptor phosphopeptide LV | other (20), R1 (3), R2 (3), NOE (3), S2 (3), tau_e (3) | tau_m = 6.81 ns (diffusion tensor fit, τm (ns)) |
| [`10.1021/bi801096b`](https://doi.org/10.1021/bi801096b) | `NMR_spin_relaxation_and_MF` | `target` | apo, 200 µM | other (6), R1 (3), R2 (3), NOE (3), S2 (3), tau_e (3) | tau_m = 6.55 ns (diffusion tensor fit, τm (ns)) |
| [`10.1021/bi801096b`](https://doi.org/10.1021/bi801096b) | `NMR_spin_relaxation_and_MF` | `target` | apo, 400 µM | other (6), tau_m (1), R1 (1), R2 (1), NOE (1) | tau_m = 8.20 ns (diffusion tensor fit, τm (ns)) |
| [`10.1021/bi801096b`](https://doi.org/10.1021/bi801096b) | `NMR_spin_relaxation_and_MF` | `target` | bound to IL-4 receptor phosphopeptide LV | other (6), tau_m (1), R1 (1), R2 (1), NOE (1) | tau_m = 7.85 ns (diffusion tensor fit, τm (ns)) |
| [`10.1021/bi801096b`](https://doi.org/10.1021/bi801096b) | `NMR_spin_relaxation_and_MF` | `target` | bound, side chain methyl-labeled (13C, p | other (3), S2 (1), tau_e (1) | other = 0.080  (Val-163-γ2) |
| [`10.1021/bi801096b`](https://doi.org/10.1021/bi801096b) | `NMR_spin_relaxation_and_MF` | `target` | apo, side chain methyl-labeled (13C, par | S2 (1), tau_e (1) | S2 = 0.54  (side chain methyl groups, average) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **residues with significant change in backbone S2 on peptide binding** ([`10.1021/bi801096b`](https://doi.org/10.1021/bi801096b), sample `S4`): 163, 166, 167, 168, 169, 181, 184, 193, 204, 225, 241, 248, 255, 265
- **lack of well-defined electron density / no defined electrostatic interactions with specific acceptor residues in AP2M1-pS-IRS1 crystal structure** ([`10.1038/s41467-019-09318-3`](https://doi.org/10.1038/s41467-019-09318-3), sample `S3`): pS616

### Conformational and complex PDB states (`States`)

- [`1IRS`](https://www.rcsb.org/structure/1IRS): NMR average structure of IRS-PTB bound to IL-4 receptor phosphopeptide ([`10.1021/bi801096b`](https://doi.org/10.1021/bi801096b))
- [`6BNT`](https://www.rcsb.org/structure/6BNT): AP2M1 (residues 160-435) bound to pS616-IRS1 peptide (residues 607-620) ([`10.1038/s41467-019-09318-3`](https://doi.org/10.1038/s41467-019-09318-3))
- [`5WRK`](https://www.rcsb.org/structure/5WRK): Y608 peptide complex (rat AP2 C-μ2 bound to rat IRS-1 Y608 peptide GY(608)MPMSPG; homolog) ([`10.7554/elife.32893`](https://doi.org/10.7554/elife.32893))
- [`5WRL`](https://www.rcsb.org/structure/5WRL): Y628 peptide complex (rat AP2 C-μ2 bound to rat IRS-1 Y628 peptide DY(628)MPMSPK; homolog) ([`10.7554/elife.32893`](https://doi.org/10.7554/elife.32893))
- [`5WRM`](https://www.rcsb.org/structure/5WRM): Y658 peptide complex (rat AP2 C-μ2 bound to rat IRS-1 Y658 peptide GY(658)MMMSPS; homolog) ([`10.7554/elife.32893`](https://doi.org/10.7554/elife.32893))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (5):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi801096b`](https://doi.org/10.1021/bi801096b) | 91 | 1 | 1 | 1 | Fast (ps-ns) 15N backbone, Trp indole and methyl 2H relaxation of IRS-PTB apo and phosphopeptide-bound, 30 °C, |
| [`10.1038/s41467-019-09318-3`](https://doi.org/10.1038/s41467-019-09318-3) | 0 | 1 | 1 | 3 | This paper contains 0 expected_rows for IRS1 (P35568) because it reports no NMR relaxation/dispersion, HDX, FR |
| [`10.1038/s41467-022-32918-5`](https://doi.org/10.1038/s41467-022-32918-5) | 0 | 0 | 0 | 0 | The paper reports crystal structures of the SHP2 phosphatase domain with phosphopeptides (one derived from hum |
| [`10.1073/pnas.2401716121`](https://doi.org/10.1073/pnas.2401716121) | 0 | 0 | 0 | 4 | Zero IRS-1 dynamics rows, zero IRS-1 PDB conformational states, and zero IRS-1 dynamic residue sets are extrac |
| [`10.7554/elife.32893`](https://doi.org/10.7554/elife.32893) | 0 | 3 | 0 | 0 | This eLife study investigates how rat IRS-1 interacts with the clathrin adaptor AP2 complex via three YxxΦ mot |

**Explicit figure-only, SI-only, or access gaps (8):**

- per-residue R1, R2, NOE, S2, tau_e, Rex (backbone), methyl R1/R1rho/Saxis2/tau_e ([`10.1021/bi801096b`](https://doi.org/10.1021/bi801096b)): in supplement not available (Supporting Information); plotted in Figures 1-4
- Fig. 5e, f SHP2 dephosphorylation time-course and relative SHP2 activity quantification for pYMPMS and pYMPMpS IRS1 peptides ([`10.1038/s41467-019-09318-3`](https://doi.org/10.1038/s41467-019-09318-3)): figure only (plotted in Fig. 5e, f with no printed rate constants or numeric time-course values in text; also represents enzymatic peptide dephosphorylation rather than intrinsic conformational dynamics)
- Fig. 5c relative band intensities, Fig. 5d full ITC thermodynamic parameters beyond Kd, Fig. 4b/e cellular PM/IC ratios, and Fig. 8b mouse tissue IRS1 phosphorylation time-courses ([`10.1038/s41467-019-09318-3`](https://doi.org/10.1038/s41467-019-09318-3)): figure only (quantitative values plotted in figures without numerical tables in text; none are protein conformational dynamics measurements)
- Supplementary Information (Supplementary Table 1 primer list, Supplementary Figs. 1–8, and Source Data file) ([`10.1038/s41467-019-09318-3`](https://doi.org/10.1038/s41467-019-09318-3)): in supplement not available (Supplementary Information is not appended to 114.txt; main-text citations show primers, sequence alignments, cellular IR endocytosis assays, pull-downs, and mouse tissue blots)
- SPR association/dissociation kinetic sensorgrams (ka, kd) for PTB, PTB-PIR, PTB-4pSer, PTB-PIR 4E, PIR, and PIR Ser-to-Glu binding to pY972-IRK (SI Appendix, Fig. S4) ([`10.1073/pnas.2401716121`](https://doi.org/10.1073/pnas.2401716121)): in supplement not available
- Full ITC binding thermograms/data for IRS-1 PTB/PTB-PIR/EPL pSer/Ser-to-Glu constructs with IR pY972 peptide (SI Appendix, Fig. S1) ([`10.1073/pnas.2401716121`](https://doi.org/10.1073/pnas.2401716121)): in supplement not available
- HDX-MS deuterium exchange time-course curves (10 s, 10 min, 1 h, 3 h) in Fig. 6A (note: measured on binding partner pY972-IRK, not IRS-1) ([`10.1073/pnas.2401716121`](https://doi.org/10.1073/pnas.2401716121)): figure only
- Mean half-life (τ1/2) bar values of IR tyrosine phosphorylation during PTP1B dephosphorylation in Fig. 4C (note: enzymatic IR dephosphorylation, not IRS-1 conformational dynamics) ([`10.1073/pnas.2401716121`](https://doi.org/10.1073/pnas.2401716121)): figure only

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
