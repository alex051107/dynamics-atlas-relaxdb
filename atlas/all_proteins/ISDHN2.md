# Iron-regulated surface determinant protein H, N2 domain (`ISDHN2`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `Q2FG07` · **RelaxDB deposited card:** T = `310.0`, field = `800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

*1 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `population` | less than 5% % | LN3 portion of IsdHN2N3 (fraction of Hb-bound receptors engaging  | `NMR_other` | `same_protein_other_construct` | apo and titrated with Hb0.1 in CO form (0:1 to 10:1 Hb:IsdH); 310 K; pH 7.5; 500 and | `unclear` | [`10.1016/j.jmb.2019.12.023`](https://doi.org/10.1016/j.jmb.2019.12.023) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*7 rows total (7 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1016/j.jmb.2015.02.008`](https://doi.org/10.1016/j.jmb.2015.02.008) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | apo (Hb-free, hemin binding disrupted) | tau_c (3), R2 (2), NOE (2) | tau_c = 16.3 ns (whole N2-linker-N3 (IsdH N2N3)) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **HDX-MS regions with faster deuterium exchange in heme-free than heme-bound linker-NEAT3 (more flexible)** ([`10.1016/j.jbc.2022.101995`](https://doi.org/10.1016/j.jbc.2022.101995), sample `S2`): Lys587-Leu597 (region 1), Ala524-Phe534 (region 2), Ile632-Gln653 (region 3), and Ser557-Gly567 (region 4)
- **micro- to millisecond exchange broadening (unassignable residues) in the N2 Hb-binding surface** ([`10.1016/j.jmb.2015.02.008`](https://doi.org/10.1016/j.jmb.2015.02.008), sample `S1`): N358-D359, Q364-T370, K397-F399, A422, S439-S440, and Y451-T454
- **N2-linker hinge point for N2 domain reorientation** ([`10.1016/j.jmb.2015.02.008`](https://doi.org/10.1016/j.jmb.2015.02.008), sample `S1`): N465-D468
- **hinge for N2-to-LN3 domain reorientation in the Hb-bound receptor** ([`10.1016/j.jmb.2019.12.023`](https://doi.org/10.1016/j.jmb.2019.12.023), sample `S1`): Asn465-Glu472

### Conformational and complex PDB states (`States`)

- [`7W81`](https://www.rcsb.org/structure/7W81): linker-NEAT3 with heme bound (this paper's deposit; IsdH, same UniProt as the entry, NEAT3 region not NEAT2) ([`10.1016/j.jbc.2022.101995`](https://doi.org/10.1016/j.jbc.2022.101995))
- [`4XS0`](https://www.rcsb.org/structure/4XS0): human Hb in complex with NEAT2-linker-NEAT3 Y642A ([`10.1016/j.jbc.2022.101995`](https://doi.org/10.1016/j.jbc.2022.101995))
- [`4IJ2`](https://www.rcsb.org/structure/4IJ2): Hb-bound IsdH N2N3 (crystal structure of IsdH N2N3:Hb complex, chain G); compact bound form versus apo NMR model ([`10.1016/j.jmb.2015.02.008`](https://doi.org/10.1016/j.jmb.2015.02.008))
- [`4XS0`](https://www.rcsb.org/structure/4XS0): crystal structure of the Hb:αIsdH complex, with Hb-N2 and Hb-LN3 interfaces both formed ([`10.1016/j.jmb.2019.12.023`](https://doi.org/10.1016/j.jmb.2019.12.023))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (5):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1016/j.jmb.2015.02.008`](https://doi.org/10.1016/j.jmb.2015.02.008) | 7 | 1 | 2 | 2 |  |
| [`10.1016/j.jmb.2019.12.023`](https://doi.org/10.1016/j.jmb.2019.12.023) | 1 | 1 | 1 | 0 |  |
| [`10.1016/j.jbc.2022.101995`](https://doi.org/10.1016/j.jbc.2022.101995) | 0 | 2 | 1 | 3 | The paper reports no NMR, MD or FRET dynamics for IsdH NEAT2. Only heme binding rates (kon, koff) from ITC for |
| [`10.1016/j.jmb.2022.167623`](https://doi.org/10.1016/j.jmb.2022.167623) | 0 | 0 | 0 | 1 | The paper is an MD/Markov-model and stopped-flow study. Its only NMR work is 15N-1H HSQC spectra used to show  |
| [`10.1016/j.yjsbx.2025.100138`](https://doi.org/10.1016/j.yjsbx.2025.100138) | 0 | 0 | 0 | 0 |  |

**Explicit figure-only, SI-only, or access gaps (6):**

- HDX-MS deuterium uptake per peptide (Tables S4, S5) and uptake time courses ([`10.1016/j.jbc.2022.101995`](https://doi.org/10.1016/j.jbc.2022.101995)): in supplement not available; main text shows only Figure 2 plots
- Heme transfer kfast and kslow from Hb to full-length IsdH (Table S7) ([`10.1016/j.jbc.2022.101995`](https://doi.org/10.1016/j.jbc.2022.101995)): in supplement not available
- DSC melting temperatures and enthalpies in Table S6 ([`10.1016/j.jbc.2022.101995`](https://doi.org/10.1016/j.jbc.2022.101995)): in supplement not available (thermal stability, not dynamics)
- Per-residue R1, R2 and heteronuclear NOE values for 155/142/238 amides ([`10.1016/j.jmb.2015.02.008`](https://doi.org/10.1016/j.jmb.2015.02.008)): figure only (Fig. S1, supplement not in text)
- Ensemble Ne=4 N2 domain population weights and ~10 Å excursion ([`10.1016/j.jmb.2015.02.008`](https://doi.org/10.1016/j.jmb.2015.02.008)): figure only; the ~10 Å is a structural excursion, not a rate or population
- Eyring and hemin-transfer tables (Table S1, S2) ([`10.1016/j.jmb.2022.167623`](https://doi.org/10.1016/j.jmb.2022.167623)): in supplement not available

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
