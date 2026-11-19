# VHR (PTP) (`VHR_CPMG`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P51452` · **RelaxDB deposited card:** T = `n/a`, field = `n/a` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`yes`)](../proteins/VHR_CPMG.md) · [Release 0.1 PDB overlay table](../../data/structures/VHR_CPMG.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `yes` (strict two-peak reading: `cannot tell: regime not stated by the authors; the 1.2% minor state is seen only through dispersion and no second peak set is reported.`)
- **Reference state:** Wild-type apo VHR, 25 °C; pH 6.5, 20 mM Bis-Tris propane, 100 mM NaCl, 1 mM TCEP, 1 mM EDTA, no phosphate added; CPMG sample 700 µM 2H/15N (Hahn-echo 700 or 965 µM)
- **Exchange rate (`kex`):** 1,530 ± 200 s-1, combined variable-insert + acid-loop fit, proposed by the authors as one concerted process on F-test grounds (p = 8.2 × 10−14) (VHR-J1, VHR-r1); the separate fits remain valid and give acid loop 1,400 ± 200 s-1 and variable insert 2,100 ± 460 s-1
- **Minor-state population (`pB`):** reported as pA = 98.8 ± 0.1% in the combined fit, so pB = 1.2 ± 0.1%; separate fits reported as pA = 98.9 ± 0.1% (acid loop, pB 1.1 ± 0.1%) and pA = 98.5 ± 0.4% (variable insert, pB 1.5 ± 0.4%) (VHR-r1)
- **Exchanging region:** Variable insert A63, R66, N72; acid loop K89, D92, E95, F96, L98, S99; Hahn-echo adds R36, Y78, R119, C124, G161, D164
- **Caveats:** Single temperature and one study. The coupling of the two loops rests on the authors' model choice (combined versus separate fits). The dissertation that RelaxDB cites as the data source was not read, so its equivalence to the 2020 data is unverified.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/VHR_CPMG.md`](../proteins/VHR_CPMG.md) (6 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

Quantitative exchange rates and populations are curated in the Release `0.1` synthesis above (no separate `v3` exchange rows added yet).

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Author-named dynamic regions and conformational PDB states

No author-named dynamic residue sets or conformational PDB states extracted in `v3` for this entry.

## 4. Papers read and explicit gaps

**Explicit figure-only, SI-only, or access gaps (1):**

- no full-text paper for this entry has been read with the v3 extractor (): no full text in hand, or not yet run

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
