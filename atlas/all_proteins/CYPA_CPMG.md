# CypA (`CYPA_CPMG`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P62937` · **RelaxDB deposited card:** T = `n/a`, field = `n/a` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`yes`)](../proteins/CYPA_CPMG.md) · [Release 0.1 PDB overlay table](../../data/structures/CYPA_CPMG.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `yes` (strict two-peak reading: `does not: Authors: fast exchange limit for most amides, methyls intermediate; only 119–122, K91, H92, H126 and V128 reach the slow-exchange limit at 0/10 °C, with no population and no second peak set reported.`)
- **Reference state:** Wild-type free CypA, 10 °C (also 0, 20, 25 °C); pH 6.5, 50 mM sodium phosphate, 1–2 mM DTT (2009: 2 mM)
- **Exchange rate (`kex`):** 10 °C: group I (active site/core) 1,140 ± 200 s-1 and group II (65–84 loop) 2,260 ± 200 s-1 (CYPA-J1, CYPA-J2, CYPA-r1); one global process 2,200 ± 90 s-1 (CYPA-J3, CYPA-r38). 20 °C: per-residue about 1,000–6,000 s-1 (CYPA-J22, CYPA-r12).
- **Minor-state population (`pB`):** 2.0 ± 0.1% (CYPA-r38); 5% from simultaneous fits of methyl residues in intermediate exchange (CYPA-r2); upper limit about 7% for the WT minor conformation overall, from amide kex and Rex (CYPA-r1); poorly determined in the deuterated per-residue fits (CYPA-J4)
- **Exchanging region:** Group I: R55, S99, E120 amides and L39, I57, L98, A103 methyls (caption also lists 'Gly110'); group II: 65–84 loop (D66, F67, T68, N71, G74, K76, S77, K82 shown); 48 exchanging amides at 10 °C in deuterated data
- **Structure comparison:** [{"pdb": "3K0N", "what": "Room-temperature wild-type crystal with alternate side-chain rotamers for R55, M61, L98, S99 and F113. The rows tie the Ser99/Phe113 network to the millisecond group I process; crystal occupancies are not solution populations. The ID mapping (3K0N = WT, 3K0O = S99T) is taken from the 2024 paper (CYPA-r62).", "evidence_row": "CYPA-r7; CYPA-r62"}, {"pdb": "3K0O", "what": "S99T mutant crystal; the authors state the S99T major conformer recapitulates features of the WT minor conformer, which does not prove identical ensembles.", "evidence_row": "CYPA-r9; CYPA-r62"}]
- **Caveats:** The number of apo processes is disputed: two collective groups (r1), one global process (r38), or a continuum of per-residue rates (r10–r12). All apo NMR checked in the cached text was recorded in 50 mM sodium phosphate with no phosphate-free control. MD places Phe113 rotamer exchange at nanoseconds to microseconds, which leaves its assignment to the millisecond process open.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/CYPA_CPMG.md`](../proteins/CYPA_CPMG.md) (18 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

*16 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `kex` | 10,700 s-1 | K82, L98, N102, A103 | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `kex` | 14,800 s-1 | K82, L98, N102, A103 | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `kex` | 11,100 s21 | K82 | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `delta_omega` | 1450 s21 | K82 | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `delta_omega` | 3.8 ppm | K82 | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `kex` | 13,000 s-1 | R55 (trans substrate, koff) | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `kex` | 10,000 s-1 | R55 (cis substrate, koff) | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `kAB` | 9000 s-1 | R55 (kcat cis to trans) | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `kBA` | 5100 s-1 | R55 (kcat trans to cis) | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `delta_omega` | 440 s21 | R55 (E vs EStrans) | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `delta_omega` | 1.2 ppm | R55 (E vs EStrans) | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `delta_omega` | 640 s21 | R55 (EScis vs EStrans) | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `delta_omega` | 1.7 ppm | R55 (EScis vs EStrans) | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `kAB` | about 9000 s-1 | substrate isomerization step on the enzyme | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `kex` | about 13,000 s-1 | substrate release step (trans) | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |
| `population` | 0.67 fraction (pES) | bound state ES, highest substrate concentration | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala-Phe-Pro-Phe-4-NA, total substrate 0.04 to 2.8 | `unclear` | [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*5 rows total (0 spin-relaxation/model-free; 5 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) | `NMR_exchange_and_dispersion` | `target` | during catalysis with substrate Suc-Ala- | other (5) | other = 0.95 mM (K82, L98, N102, A103) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **catalysis-linked conformational exchange only during turnover** ([`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176), sample `S2`): R55, K82, L98, S99, A101, N102, A103, and G109
- **chemical exchange both with and without substrate** ([`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176), sample `S2`): F67, N71, G74, S77, and S110
- **exchange in absence of substrate that increases with substrate** ([`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176), sample `S2`): T68 and G72

### Conformational and complex PDB states (`States`)

- [`1RMH`](https://www.rcsb.org/structure/1RMH): CypA bound to cis form of Suc-Ala-Ala-Pro-Phe-4-NA (EScis model used for mapping) ([`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176) | 21 | 1 | 3 | 3 | Short Science report with no tables. Dynamics numbers: two-state fit ranges of KDobs and koff for K82, L98, N1 |

**Explicit figure-only, SI-only, or access gaps (3):**

- Per-residue R2 and Rex values for 160 backbone amides at each substrate concentration ([`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176)): figure only (Fig. 2), no numbers printed
- Per-residue fit parameters for L98, N102, A103 and other residues beyond the ranges and K82 and R55 values printed ([`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176)): figure only (Fig. 4) or not printed
- Complete R1 and {1H}-15N NOE data ([`10.1126/science.1066176`](https://doi.org/10.1126/science.1066176)): in supplement not available (Science Online)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
