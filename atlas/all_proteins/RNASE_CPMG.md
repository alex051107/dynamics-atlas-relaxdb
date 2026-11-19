# RNase A (`RNASE_CPMG`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P61824` · **RelaxDB deposited card:** T = `n/a`, field = `n/a` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`yes`)](../proteins/RNASE_CPMG.md) · [Release 0.1 PDB overlay table](../../data/structures/RNASE_CPMG.md)

> **Shared UniProt (`P61824`):** Also filed in RelaxDB under [`RNASE`](RNASE.md). Inspect both entries together when synthesizing canonical protein behavior.

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `yes` (strict two-peak reading: `does not: Global and cluster motions are fast (buffer study: 'nearly all ... in the fast limit'); only R33 is slow, and 'no minor peak could be detected'.`)
- **Reference state:** Wild-type free RNase A, 293 K (RelaxDB label condition; also 283 and 298 K). Beach 2005: pH 6.3, 20 mM perdeuterated MES, 10 mM NaCl, 600 µM. Cluster fits (Khirich 2015): 5 mM MES, 7 mM NaCl, pH 6.4. Buffer-study reference: 5 mM MES, 400 µM.
- **Exchange rate (`kex`):** global 1,080 ± 80 / 1,390 ± 70 / 1,750 ± 130 s-1 at 283 / 293 / 298 K (RNASE-J1, RNASE-r1–r3); His48 cluster 2,650 s-1 at 25 °C, pH 6.4 (RNASE-J5, RNASE-r18); loop 4 1,610 s-1 at 25 °C, pooled pH 5.5–7.0 (RNASE-J6, RNASE-r19); R33 1,215 s-1 at 25 °C (RNASE-J7, RNASE-r68)
- **Minor-state population (`pB`):** reported as pA, so pB = 1 − pA: global fits pA 90–93% across 283–298 K (pB 7–10%), which Beach says reflects 'uncertainty in fitting for pa' (RNASE-J1); His48 cluster reported as pA = 92.5 ± 0.7% at pH 6.4 (pB 7.5 ± 0.7%; the ± is the spread of an average over temperature) (RNASE-J5); loop 4 reported as pA = 95.9 ± 0.9% at 25 °C (pB 4.1 ± 0.9%; the ± is the standard deviation over pH) (RNASE-J6); R33 reported as pA = 99.5% (pB 0.5%) (RNASE-J7, RNASE-r68); pA:pB 0.95:0.05 in the proton-inventory study (RNASE-J3, RNASE-r24)
- **Exchanging region:** Global fit at 293 K: Q11, S15, S16, T17, N44, F46, A64, K66, N71, D83, T100, Q101, H119 (43 residues pass the Rex screen); His48 cluster S15, S16, T17, F46, T82, D83, Q101; loop 4 A64, K66, T70, N71; R33
- **Structure comparison:** [{"pdb": "1U1B", "what": "pTppAp-bound crystal (the authors' own complex). Beach 2005 compares it crystal-to-crystal with apo 7RSA (backbone RMSD 0.69 Å) and describes an equilibrium between 'open and closed enzyme forms'. The minor state's resemblance to the bound form rests on 15N Δω sign agreement (17 of 20 residues); its structure is not determined.", "evidence_row": "RNASE-r1; RNASE-r2; RNASE-r3; RNASE-r9"}, {"pdb": "7RSA", "what": "Apo crystal structure, the apo comparison structure in the same analysis; 'apo-like/open comparison state' is the entry's gloss.", "evidence_row": "RNASE-r2; RNASE-r9"}]
- **Caveats:** Whether this is one collective motion or several (His48 network, loop 4, R33) is disputed between papers, and 'cluster 1' means different regions in different papers. Free-WT samples were in MES (later also 1% DSS); the only buffer control is a stated, unshown MES-versus-unbuffered comparison. Of the 43 residues behind the RelaxDB labels, only 13 entered the 293 K global fit.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/RNASE_CPMG.md`](../proteins/RNASE_CPMG.md) (17 key curated rows)

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
