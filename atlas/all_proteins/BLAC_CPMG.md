# BLAC (`BLAC_CPMG`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P9WKD3` · **RelaxDB deposited card:** T = `n/a`, field = `n/a` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`possible`)](../proteins/BLAC_CPMG.md) · [Release 0.1 PDB overlay table](../../data/structures/BLAC_CPMG.md)

> **Audit note:** Twin UniProt P9WKD3 (Release 0.1 page; v3 read under 27888)

> **Shared UniProt (`P9WKD3`):** Also filed in RelaxDB under [`27888`](27888.md). Inspect both entries together when synthesizing canonical protein behavior.

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `possible` (strict two-peak reading: `cannot tell: Δω and pB of the 860 s-1 process are undetermined; the authors call the four broadened amides 'intermediate to fast'; WT shows no peak doubling (doubling only in G132N and the clavulanate adduct).`)
- **Reference state:** Wild-type resting-state (free) BlaC, 298 K; pH 6.4, 94 mM sodium MES, 6% D2O, no phosphate
- **Exchange rate (`kex`):** (8.6 ± 0.6) x 10^2 s-1 at 298 K, two-state model assumed, two-field (14.1 and 20.0 T) group fit of eight amides (BLAC-J1, BLAC-r1, BLAC-r4)
- **Minor-state population (`pB`):** not determined with any accuracy (authors; BLAC-J1, BLAC-r1); the authors' own Bloch-McConnell estimate is that pB must exceed 15% (with Δω > 0.1 ppm 1H and/or 1 ppm 15N at 20 T) if the four broadened amides share the 860 s-1 process (BLAC-J2)
- **Exchanging region:** Group fit: F68, C69, T71, E166, E168, N170, T215, A218 (named in Elings 2021 SI Table S3, doi:10.1128/aac.02628-20; BLAC-J1); broadened beyond detection: Ser70, Ser130, Thr235, Thr237 (Ambler numbering; entry 43, 101, 210, 212 by the project's alignment)
- **Caveats:** Whether the four broadened anion-site amides and the 860 s-1 process are one process or two is unresolved. In every BlaC crystal published as of 2020 those four side chains hydrogen-bond a ligand or a buffer anion, and MES (a sulfonate) was never compared with another buffer. Mutant NMR from 2024-2025 used phosphate, which binds the active site, so it is not like-for-like with the WT MES data. A cached SAXS study proposing an open apo shape has no evidence row and was not used.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/BLAC_CPMG.md`](../proteins/BLAC_CPMG.md) (11 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Author-named dynamic regions and conformational PDB states

No author-named dynamic residue sets or conformational PDB states extracted in `v3` for this entry.

## 4. Papers read and explicit gaps

**Explicit figure-only, SI-only, or access gaps (1):**

- same protein (UniProt P9WKD3) read under entry 27888; see that row (): RelaxDB has separate entries for the same protein

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
