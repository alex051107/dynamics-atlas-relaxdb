# Interleukin-1 beta (IL-1b) (`IL1B`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P01584` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

*2 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `pB` | 8 % | minor form of hIL-1β (global) | `NMR_exchange_and_dispersion` | `target` | apo; 309 K (minor-form population); 296 K (assay conditions); pH 7.4; 800 | `no` | [`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0) |
| `kex` | 22 s−1 | minor/major exchange (global) | `NMR_exchange_and_dispersion` | `target` | apo; 309 K (minor-form population); 296 K (assay conditions); pH 7.4; 800 | `no` | [`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*10 rows total (0 spin-relaxation/model-free; 10 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0) | `NMR_exchange_and_dispersion` | `target` | titrated with (S)-1 / fragment 1 | other (4) | other = 1.2 × 105 M−1 s−1 (ligand binding (kon), fragment 1) |
| [`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0) | `Biophysics_and_other` | `same_protein_other_construct` | binding (S)-2 by SPR | other (2) | other = 1.2 × 105 M−1 s−1 (ligand binding (kon), (S)-2) |
| [`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0) | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | titrated with (S)-1 | other (2) | other = 0.81 × 106 M−1 s−1 (ligand binding (kon), (S)-1) |
| [`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0) | `NMR_exchange_and_dispersion` | `target` | apo | other (1) | other = 11.3 dimensionless (K = [major]/[minor]) (whole protein exchan |
| [`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0) | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | apo | other (1) | other = 3.4 dimensionless (K = [major]/[minor]) (whole protein exchang |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **minor-form (conformational exchange) region, WT** ([`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0), sample `S1`): N-terminus, loop β4–5 and loop β7–8
- **minor-form residues forming binding site** ([`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0), sample `S1`): Val47, Gln48, Lys92, Lys94
- **residues still two-state in V47A** ([`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0), sample `S2`): Ala47, Gln48, Asn89, Tyr90
- **fast-exchanging amides with WT-like protection in all permutants (native-state HDX)** ([`10.1371/journal.pone.0038512`](https://doi.org/10.1371/journal.pone.0038512), sample `S2`): Q15, E25, V40, V41, M44, V47, I56, A59, K77, L80, V85, I106, K109, N129, and D145
- **amides with faster exchange in PM65 and PM76 (hairpin cap and cap-barrel interface)** ([`10.1371/journal.pone.0038512`](https://doi.org/10.1371/journal.pone.0038512), sample `S2`): L60, L62, C71, Q116, I122, S123, and L134
- **early backbone amide protection in the WT refolding intermediate (pulse labeling)** ([`10.1371/journal.pone.0038512`](https://doi.org/10.1371/journal.pone.0038512), sample `S1`): V40, F42, S43, V58, L60, L67, Y68, L69, S70, C71, V72, T79, Q81, E83, V85, V100, F101, N102, K103, I104, L110, E111, E113, S114, A115, Q116, F117, W120, Y121, I122, S123

### Conformational and complex PDB states (`States`)

- [`4DEP`](https://www.rcsb.org/structure/4DEP): hIL-1β in the ternary signaling complex with IL-1R1 and IL-1RAcP (receptor-bound, loop β4–5 closed state) ([`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0))
- [`5R8Q`](https://www.rcsb.org/structure/5R8Q): C-terminal mature domain (117–269 aa, IL-1β) co-crystal structure with small-molecule ligand JGY (Z2643472210); also used as HTVS docking receptor ([`10.1038/s41467-025-65220-1`](https://doi.org/10.1038/s41467-025-65220-1))
- [`7Z4T`](https://www.rcsb.org/structure/7Z4T): AAL160 Fab complex with IL-1b ([`10.1038/s42003-023-05369-x`](https://doi.org/10.1038/s42003-023-05369-x))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (10):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0) | 12 | 1 | 3 | 2 |  |
| [`10.1021/ja104983t`](https://doi.org/10.1021/ja104983t) | 0 | 0 | 0 | 1 |  |
| [`10.1038/nsmb.2260`](https://doi.org/10.1038/nsmb.2260) | 0 | 0 | 0 | 3 | This paper reports the 3.1 Å X-ray crystal structure of human IL-1β in a ternary signaling complex with the ex |
| [`10.1038/s41467-025-65220-1`](https://doi.org/10.1038/s41467-025-65220-1) | 0 | 1 | 0 | 4 | This cancer cell biology study investigates a cleavage-independent moonlighting role of intracellular Pro-IL-1 |
| [`10.1038/s42003-023-05369-x`](https://doi.org/10.1038/s42003-023-05369-x) | 0 | 1 | 0 | 0 | Zero-row paper for human IL-1β (IL1B, P01584): this antibody-engineering and X-ray crystallography study redir |
| [`10.1186/s12906-026-05459-3`](https://doi.org/10.1186/s12906-026-05459-3) | 0 | 0 | 0 | 0 |  |
| [`10.1371/journal.pone.0038512`](https://doi.org/10.1371/journal.pone.0038512) | 0 | 0 | 3 | 4 | The paper reports equilibrium stability, folding kinetics (chevron plots), and native-state and pulse-labeling |
| [`10.1371/journal.pone.0195335`](https://doi.org/10.1371/journal.pone.0195335) | 0 | 0 | 0 | 0 | Zero protein dynamics rows: this burn-injury immunology paper investigates endogenous human and mouse plasma/m |
| [`10.1371/journal.ppat.1003536`](https://doi.org/10.1371/journal.ppat.1003536) | 0 | 0 | 0 | 0 | This PLoS Pathogens study investigates how the HPV16 E6 oncoprotein suppresses pro-IL-1β (UniProt P01584) leve |
| [`10.3389/fphar.2026.1962620`](https://doi.org/10.3389/fphar.2026.1962620) | 0 | 0 | 0 | 0 |  |

**Explicit figure-only, SI-only, or access gaps (14):**

- 15N R1, R2, heteronuclear NOE and Lipari-Szabo S2 per residue for IL1β-R2 ([`10.1021/ja104983t`](https://doi.org/10.1021/ja104983t)): figure only (Figure 8); the text prints no numbers, only that loop-LBT residues G1-Y17 have lower S2 than the β-sheet core
- Supplementary Table 1 (crystallographic data collection and refinement statistics, and any PDB accession code) ([`10.1038/nsmb.2260`](https://doi.org/10.1038/nsmb.2260)): in supplement not available
- Supplementary Methods (expression constructs, purification, and crystallization buffer/pH/temperature conditions) ([`10.1038/nsmb.2260`](https://doi.org/10.1038/nsmb.2260)): in supplement not available
- Supplementary Discussion and Supplementary Figs. 1–3 ([`10.1038/nsmb.2260`](https://doi.org/10.1038/nsmb.2260)): in supplement not available
- per-residue CEST exchange parameters (Supplementary Tables 3 and 4), Fig. 5b CEST profiles ([`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0)): in supplement not available / figure only
- Fig. 6c / Supplementary Fig. 13 lineshape fits beyond printed values ([`10.1038/s41467-023-41190-0`](https://doi.org/10.1038/s41467-023-41190-0)): figure only
- CETSA melting curves for Pro-IL-1β with or without Q3MG (Fig. 7C, Supplementary Fig. S25D) ([`10.1038/s41467-025-65220-1`](https://doi.org/10.1038/s41467-025-65220-1)): figure only (no numerical Tm or ΔTm values printed in the text; Supplementary Fig. S25D not in text)
- Docking hydrogen-bond distances in the Pro-IL-1β–RACK1 complex (Fig. 4A) and top 50 HTVS docking scores (Supplementary Data 2, Supplementary Data 7, Supplementary Fig. S24) ([`10.1038/s41467-025-65220-1`](https://doi.org/10.1038/s41467-025-65220-1)): figure only / supplement not available (and computational docking scores/bond lengths, not experimental protein dynamics)
- RACK1 pulse-chase protein half-life curves upon Pro-IL-1β silencing or overexpression (Supplementary Fig. S18C) ([`10.1038/s41467-025-65220-1`](https://doi.org/10.1038/s41467-025-65220-1)): in supplement not available and figure only (also measures RACK1, a different protein)
- Supplementary Figs. S1–S27 and Supplementary Data 1–7 ([`10.1038/s41467-025-65220-1`](https://doi.org/10.1038/s41467-025-65220-1)): in supplement not available in 125.txt
- Native-state HDX protection factors for WT and permutants ([`10.1371/journal.pone.0038512`](https://doi.org/10.1371/journal.pone.0038512)): in supplement not available (Table S1, .doc, not in text)
- Pulse-labeling protected amides per permutant ([`10.1371/journal.pone.0038512`](https://doi.org/10.1371/journal.pone.0038512)): in supplement not available (Table S2)
- *... plus 2 additional gap entries in the `Gaps` tab.*

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
