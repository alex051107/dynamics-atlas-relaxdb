# BLVRB (`BLVRB_CPMG`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P30043` · **RelaxDB deposited card:** T = `n/a`, field = `n/a` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`yes`)](../proteins/BLVRB_CPMG.md) · [Release 0.1 PDB overlay table](../../data/structures/BLVRB_CPMG.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `yes` (strict two-peak reading: `does not: Authors: exchange on the fast NMR timescale for the fittable residues; the minor state is seen only through dispersion and no second peak set is reported.`)
- **Reference state:** Wild-type apo human BLVRB, 20 °C (also 10, 5, 0 °C); pH 6.5, 50 mM Bis-Tris, 50 mM NaCl, 1 mM DTT; refolded, coenzyme removed by reverse-phase chromatography (Resource 15RPC, 2018 methods; the step is not stated for the 2023 samples)
- **Exchange rate (`kex`):** Group II 1,088 ± 180 s-1 and Group III 3,797 ± 800 s-1 at 20 °C, slowing to 181 ± 66 and 850 ± 178 s-1 at 0 °C (BLVRB-J3, BLVRB-J4, BLVRB-r15–r18); per-residue S111 1,200 ± 300 s-1 and L125 2,200 ± 540 s-1 at 20 °C (BLVRB-J1, BLVRB-r1)
- **Minor-state population (`pB`):** reported as pA: 2023 Table 2 prints major fractions 97.8 ± 0.2% (Group II) and 98.8 ± 0.1% (Group III) at 20 °C, so pB = 2.2 ± 0.2% and 1.2 ± 0.1%; at 0 °C reported as pA = 95.5 ± 1.5% and 97.8 ± 0.3%, so pB = 4.5 ± 1.5% and 2.2 ± 0.3% (the 0 °C Group II cell prints no unit) (BLVRB-r15, BLVRB-r18); not separable in the 2018 fast-exchange fits (BLVRB-r1)
- **Exchanging region:** Active-site loops 10–15, 76–82 and 109–114 (more than 30 residues at 20 °C); Group II L74, T77, C109, S111, Q126; Group III I154, G155, T164, I176, Y205
- **Structure comparison:** [{"pdb": "1HDO", "what": "NADP+-bound (holo) crystal. The authors report that apo and holo crystals differ at R35, R39 and the R78 clamp. Separately, apo CPMG shift differences show 'at least several weak correlations' with apo-to-holo CSPs (2023), so the apo enzyme may sample holo-like states; I176 and Y205, both in this row's residue list, do not. The holo-like reading comes from shifts, not from 1HDO coordinates; not a solved minor state.", "evidence_row": "BLVRB-r37"}]
- **Caveats:** The population is model-dependent: not separable (2018 per-residue fits), about 1-2% (2023 grouped Arrhenius fits), or poorly determined in the 2024 per-residue refit, whose SI Table S1 prints pA from 50% to 99.8% with errors up to about ±22% and several values at exactly 50%, possibly a fit bound (our reading; BLVRB-r38). Without the reverse-phase step 1-3% of the enzyme stayed coenzyme-bound (authors, data not shown); that this fraction is similar in size to the fitted apo minor states is our inference. Rates in the 2023 and 2024 tables are printed in 'Hz' and are carried as s-1 without conversion.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/BLVRB_CPMG.md`](../proteins/BLVRB_CPMG.md) (8 key curated rows)

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
