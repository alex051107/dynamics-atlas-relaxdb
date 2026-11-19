# K-Ras4B (`KRAS_CPMG`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P01116` · **RelaxDB deposited card:** T = `n/a`, field = `n/a` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`yes`)](../proteins/KRAS_CPMG.md) · [Release 0.1 PDB overlay table](../../data/structures/KRAS_CPMG.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `yes` (strict two-peak reading: `qualifies: Authors: 'moderately slow', 'intermediate-to-slow' (|Δω|/kex > 0.5); a second CEST dip for state 1 is seen in WT GTP·Mg at 298 K, and 31P γ1/γ2 are separate peaks at 278 K in a C118S background; no HSQC peak doubling for WT at 298 K is reported.`)
- **Reference state:** Wild-type K-Ras4B 1–169 with native GTP and Mg2+, no partner; 298 K, pH 7.0, 20 mM HEPES, 5 mM MgCl2 (GDP·Mg is listed under other_conditions)
- **Exchange rate (`kex`):** 400 ± 12 s-1 (KRAS-J1, KRAS-r1); 414 ± 3 s-1 (KRAS-J2, KRAS-r26); 404 ± 54 s-1 in PBS/EDTA (KRAS-J3, KRAS-r17)
- **Minor-state population (`pB`):** state 1: 10.15 ± 0.47% (KRAS-r1); 9.6 ± 0.1% (KRAS-r26); 7.8 ± 0.2% higher-energy state (pE) in PBS/EDTA, read as state 1 by the entry (KRAS-r17)
- **Exchanging region:** Switch I, Switch II and the P-loop; 45 residues with fitted |Δϖ| > 0.5 ppm (Source Data Fig. 3); T35, I36, E62, Y71 shown (KRAS-r1)
- **Caveats:** Ras has no nucleotide-free apo form, so the call depends on the nucleotide: yes for GTP·Mg, no_evidence for GDP·Mg in HEPES. The 31P two-peak observation is in a C118S background, not WT. No structure of WT state 1 with native GTP is solved (GDP-like shifts and random-coil-like Switch I only); open-Switch-I crystals exist only for mutants or analogue-bound protein, and state-1 mutants T35S and V29G show extra or faster processes, so state 1 may be heterogeneous. GMPPNP raises state 1, so analogue-loaded samples cannot stand in for native GTP.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/KRAS_CPMG.md`](../proteins/KRAS_CPMG.md) (11 key curated rows)

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
