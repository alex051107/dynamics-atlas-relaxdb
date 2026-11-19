# Arginine Kinase (`ARGKIN_CPMG`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P51541` · **RelaxDB deposited card:** T = `n/a`, field = `n/a` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`yes`)](../proteins/ARGKIN_CPMG.md) · [Release 0.1 PDB overlay table](../../data/structures/ARGKIN_CPMG.md)

> **Audit note:** Twin UniProt P51541 (Release 0.1 page; v3 read under ARGKIN)

> **Shared UniProt (`P51541`):** Also filed in RelaxDB under [`ARGKIN`](ARGKIN.md). Inspect both entries together when synthesizing canonical protein behavior.

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `yes` (strict two-peak reading: `does not: Authors assign intermediate exchange (α 1.1–1.3) to the three L8 residues used for pB; the minor state is seen only through dispersion and no minor-state peaks are reported.`)
- **Reference state:** Wild-type substrate-free arginine kinase, 25 °C (also 15–30 °C); pH 6.5, 10 mM sodium citrate, 50 mM KCl, 0.5 mM DTT; no nucleotide or Mg (2009/2011 samples). Methyl sample (2017): 10 mM potassium citrate, 50 mM KCl, pH not stated
- **Exchange rate (`kex`):** 25 °C collective fits: loop L8 790 ± 60 s-1; NTD hinge 1,930 ± 350 s-1; NTD–CTD interface 800 ± 100 s-1; dynamic domain 1 790 ± 70 s-1 (Table 1) or 990 ± 110 s-1 (text) (ARGKIN-J1–J4, ARGKIN-r1). L8 530 ± 80 to 1,080 ± 150 s-1 from 15 to 30 °C, 860 ± 120 s-1 at 25 °C (the rate paired with the 4.9% L8 population, ARGKIN-r6) (ARGKIN-J9, ARGKIN-r4–r7). L170/L187 methyls 970 ± 38 s-1 (ARGKIN-J10, ARGKIN-r11).
- **Minor-state population (`pB`):** L8 2.6 ± 0.6%; hinge 0.4 ± 0.1%; interface 1.1 ± 0.1%; dynamic domain 1 0.4 ± 0.1% (Table 1; text: < 0.3%) (ARGKIN-r1). L8 3.5 ± 0.3% to 5.7 ± 1.6% from 15 to 30 °C, 4.9 ± 0.5% at 25 °C (with kex 860 ± 120 s-1), from E190, D192, T206 only (ARGKIN-r4–r7). L170/L187 methyls 4.8 ± 0.3% (ARGKIN-r11).
- **Exchanging region:** NTD hinge D88, H90, G92; NTD–CTD interface D71, F136, N137, F270, C271, N274, G276, G332; dynamic domain 1 and hinge R126, C127, R129, V220, V222, R229, Q234; substrate-binding loop L8 I182–G209 (17 residues in the collective fit); methyls L170, L187, L219, I231, I210, L331
- **Structure comparison:** [{"pdb": "1M15", "what": "Transition-state-analogue (closed) crystal structure. Apo solution RDCs and shifts fit a mixture of the 3M10 apo and 1M15 TSA endpoints with an apo fraction of about 0.5 (shifts) to 0.7 (RDCs), and the authors conclude that solution apo enzyme contains substrate-bound-like features. Static-average and dynamic-mixture models give very similar Q-values, so RDCs alone cannot tell them apart; relaxation dispersion gives an apo fraction > 0.97. Separately, the 2009 CPMG paper speculates that the L8 motion may sample the closed-form configuration (ARGKIN-r1).", "evidence_row": "ARGKIN-r8; ARGKIN-r9; ARGKIN-r1"}, {"pdb": "3M10", "what": "Refined apo crystal structure, the open endpoint of the same RDC mixture. The RDC paper's Methods name the deposited model 3M15 once; elsewhere the paper uses 3M10.", "evidence_row": "ARGKIN-r8; ARGKIN-r10"}]
- **Caveats:** The L8 population depends on the residue subset (2.6% from all 17 residues versus 4.9% from three residues at 25 °C). Dynamic domain 1 has two inconsistent fits in the same paper, and its methyls exchange at 3,890 ± 29 s-1 (pB 0.56%), so methyls may report a different process; I210 suggests three or more states. All apo samples were in citrate with no citrate-free control, and bound samples switched to imidazole/Mg, so ligand and buffer change together. The RDC match to 1M15 cannot separate exchange from a static average.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/ARGKIN_CPMG.md`](../proteins/ARGKIN_CPMG.md) (13 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

Quantitative exchange rates and populations are curated in the Release `0.1` synthesis above (no separate `v3` exchange rows added yet).

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Author-named dynamic regions and conformational PDB states

No author-named dynamic residue sets or conformational PDB states extracted in `v3` for this entry.

## 4. Papers read and explicit gaps

**Explicit figure-only, SI-only, or access gaps (1):**

- same protein (UniProt P51541) read under entry ARGKIN; see that row (): RelaxDB has separate entries for the same protein

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
