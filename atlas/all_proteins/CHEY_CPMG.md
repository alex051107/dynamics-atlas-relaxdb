# CheY (`CHEY_CPMG`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P0AE67` · **RelaxDB deposited card:** T = `n/a`, field = `n/a` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`possible`)](../proteins/CHEY_CPMG.md) · [Release 0.1 PDB overlay table](../../data/structures/CHEY_CPMG.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `possible` (strict two-peak reading: `cannot tell: the authors state no regime and report no minor-state peak. Computed from their Table 2 local fits (PMC3552614, 1 mM EDTA, 15 °C): D64 kex 96 ± 16 s-1, Δω 9.4 ± 1 ppm, minor fraction 0.20 and R19 kex 180 ± 30 s-1, Δω 5.7 ± 1 ppm, minor fraction 0.04 give kex/Δω 0.03 and 0.08 at 600 MHz, i.e. slow exchange that predicts a resolved minor peak; none is reported, so either the peak exists unreported or these local fits are unreliable (computed by Claude 2026-10-20 after the night review). All other fitted residues are intermediate or fast (kex/Δω 1.0-12.9).`)
- **Reference state:** Wild-type unphosphorylated CheY without Mg2+ (1 mM EDTA), 15 °C; pH 7.0, 50 mM sodium phosphate, 0.02% NaN3; >80% 2H
- **Exchange rate (`kex`):** per-residue local fits, no shared value: 96 ± 16 s-1 (D64) to 2,440 ± 570 s-1 (V107) (CHEY-J1, CHEY-r1)
- **Minor-state population (`pB`):** reported as per-residue major fraction pI = 0.67 ± 0.2 (N94) to 0.99 ± 0.01, so local minor fractions 1 − pI = 0.33 ± 0.2 to 0.01 ± 0.01; local fit parameters, not a shared population; N94 is ill-determined (kex 1,330 ± 800 s-1, Δω 0.27 ± 0.1 ppm) (CHEY-J1, CHEY-r1)
- **Exchanging region:** R18, R19, A36, D38, N62, D64, E67, L68, L69, T87, N94, V107, L127 (Rex > 2 s-1); D13 too broad to fit
- **Structure comparison:** [{"pdb": "3CHY", "what": "Mg-free wild-type crystal (Volz 1991 abstract: three sulfate ions, seven side chains in dual conformations; CHEY-r19). McDonald 2012 describes Y106 'out' and 'in' rotamers in this structure, cites the populated 'in' rotamer as support for rapid Y106 switching, and notes M85 in two conformations (CHEY-r1); the crystal gives no rate or population. A 1.08 Å apo structure (PDB ID not given in the rows) shows two β4–α4 loop conformations correlated with the Y106 rotamers, one interpreted as meta-active (CHEY-r27).", "evidence_row": "CHEY-r1; CHEY-r19; CHEY-r27"}]
- **Caveats:** The call is possible, not yes, because the data give per-residue local populations only and the authors argue against a single concerted inactive-active switch; linear shift trajectories across T87I, WT, A113P and BeFx states, which fit a two-state shift, are stated for Y106, V107 and E89 only. All NMR samples were in 50 mM sodium phosphate with no phosphate-free control, and the Mg-free crystal 3CHY has a sulfate next to N59 and K109 in the phosphorylation pocket.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/CHEY_CPMG.md`](../proteins/CHEY_CPMG.md) (8 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Author-named dynamic regions and conformational PDB states

No author-named dynamic residue sets or conformational PDB states extracted in `v3` for this entry.

## 4. Papers read and explicit gaps

**Explicit figure-only, SI-only, or access gaps (1):**

- no full-text paper for this entry has been read with the v3 extractor (): no full text in hand, or not yet run

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
