# Urokinase-type plasminogen activator, kringle domain (`ATFKR`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P00749` · **RelaxDB deposited card:** T = `303.0`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*451 rows total (450 spin-relaxation/model-free; 1 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi00255a023`](https://doi.org/10.1021/bi00255a023) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | apo (no ligand or receptor) | other (227), NOE (97), S2 (94), Rex (26), tau_m (6) | tau_m = 7.28 ns (growth factor domain (GFD), amides w…) |
| [`10.1021/bi00182a013`](https://doi.org/10.1021/bi00182a013) | `HDX_NMR_and_MS` | `same_protein_other_construct` | apo | other (1) | other = > 15 min min (50 slowly exchanging amides (not lis…) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **most flexible loop of the GFD (order parameters below 0.6), implicated in u-PA receptor binding** ([`10.1021/bi00255a023`](https://doi.org/10.1021/bi00255a023), sample `S1`): N22-I28 (printed N22—128)
- **lower order parameters in the turn between the two strands of the largest kringle beta-sheet (under 0.75)** ([`10.1021/bi00255a023`](https://doi.org/10.1021/bi00255a023), sample `S1`): V117-K120 (printed VI17—K120)
- **large Rex (conformational exchange) near the C50-C131 disulfide bond** ([`10.1021/bi00255a023`](https://doi.org/10.1021/bi00255a023), sample `S1`): amides near C50 and C131
- **large Rex at C126 with unaffected neighbours** ([`10.1021/bi00255a023`](https://doi.org/10.1021/bi00255a023), sample `S1`): C126

### Conformational and complex PDB states (`States`)

- [`1URK`](https://www.rcsb.org/structure/1URK): NMR solution structure of ATF (15 low energy structures) ([`10.1021/bi00182a013`](https://doi.org/10.1021/bi00182a013))
- [`7DZD`](https://www.rcsb.org/structure/7DZD): uPA-camostat complex (cleaved camostat / 4-guanidinobenzoic acid (GBA) covalently bound to Ser195; protease domain positions 159-411, same_protein_other_construct) ([`10.1128/jvi.00861-21`](https://doi.org/10.1128/jvi.00861-21))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (6):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi00255a023`](https://doi.org/10.1021/bi00255a023) | 450 | 0 | 4 | 2 | Hansen et al. 1994 measured 15N T1, T2 and heteronuclear NOE on uniformly 15N-labeled ATF (kringle + growth fa |
| [`10.1021/bi00182a013`](https://doi.org/10.1021/bi00182a013) | 1 | 1 | 0 | 2 | Structure paper; the only printed dynamics number is the amide H/D exchange cutoff (> 15 min) for 50 slowly ex |
| [`10.1016/j.jbc.2023.105179`](https://doi.org/10.1016/j.jbc.2023.105179) | 0 | 0 | 0 | 1 |  |
| [`10.1083/jcb.137.3.779`](https://doi.org/10.1083/jcb.137.3.779) | 0 | 0 | 0 | 0 | This study investigates in vivo phosphorylation of human pro-urokinase (pro-uPA, UniProt P00749) at Ser138 and |
| [`10.1128/jvi.00861-21`](https://doi.org/10.1128/jvi.00861-21) | 0 | 1 | 0 | 0 | Zero protein dynamics rows: the paper studies the serine protease domain of human uPA (positions 159 to 411; s |
| [`10.1371/journal.pone.0119207`](https://doi.org/10.1371/journal.pone.0119207) | 0 | 0 | 0 | 0 | This study maps the binding epitopes and functional inhibition profiles of two 2'-fluoropyrimidine RNA aptamer |

**Explicit figure-only, SI-only, or access gaps (5):**

- HDX-MS deuterium uptake plots for the protease domain ([`10.1016/j.jbc.2023.105179`](https://doi.org/10.1016/j.jbc.2023.105179)): figure only (Figs. 2 and 3); uptake values and peptide table (Table S1) are not printed in the text, and they concern the protease domain, not the kringle
- 15N spin-spin relaxation rates around C131 ([`10.1021/bi00182a013`](https://doi.org/10.1021/bi00182a013)): described only qualitatively as preliminary data; no numbers printed
- per-residue slowly exchanging amide identities ([`10.1021/bi00182a013`](https://doi.org/10.1021/bi00182a013)): figure only (Figure 4/ histogram)
- Per-residue S2 plot (Figure 7A) and Rex plot (Figure 7B), T1/T2/NOE plot (Figure 3), A versus angle (Figure 5), T1/T2 versus angle (Figure 6) ([`10.1021/bi00255a023`](https://doi.org/10.1021/bi00255a023)): figure only; the numbers are in the Supplementary Tables
- Rows for residues missing from Supplementary Table II (Y58, R59, A86) that have T1, T2, NOE but no S2 ([`10.1021/bi00255a023`](https://doi.org/10.1021/bi00255a023)): no printed S2 or Rex value in the text

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
