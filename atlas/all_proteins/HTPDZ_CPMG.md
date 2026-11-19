# Serine protease HTRA2, mitochondrial (`HTPDZ_CPMG`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `O43464` · **RelaxDB deposited card:** T = `n/a`, field = `n/a` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`yes`)](../proteins/HTPDZ_CPMG.md) · [Release 0.1 PDB overlay table](../../data/structures/HTPDZ_CPMG.md)

> **Audit note:** Twin UniProt O43464 (Release 0.1 page; v3 read under HTPDZ)

> **Shared UniProt (`O43464`):** Also filed in RelaxDB under [`HTPDZ`](HTPDZ.md). Inspect both entries together when synthesizing canonical protein behavior.

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `yes` (strict two-peak reading: `cannot tell: No regime statement and no Δω printed; the authors report no minor-state peaks.`)
- **Reference state:** Isolated wild-type apo HtrA2 PDZ, 298 K and 283 K; PBS pH 7.4 (the PDZ sample buffer; the NMR buffer is not stated separately), no added divalent metal; 500 µM
- **Exchange rate (`kex`):** reported as τex, not kex: 0.42 ± 0.004 ms at 298 K and 0.98 ± 0.005 ms at 283 K (fit errors from a single experiment, n = 1); kex ≈ 1/τex is the row's assumption, giving about 2,400 s-1 (HTPDZ-J1) and about 1,020 s-1 (HTPDZ-J28); methyl τex 1.19 ± 0.07 ms at 298 K (HTPDZ-J3)
- **Minor-state population (`pB`):** 15.2% at 298 K (HTPDZ-r1); 16.1% at 283 K (HTPDZ-r2); the text says only 'decreasing from 16.1 to 15.2%', with no error given and the temperature assignment from Fig. 2c; methyl 16.6 ± 0.4% at 298 K (HTPDZ-r3)
- **Exchanging region:** N-terminus, helix α5 and the α5–β15 loop, helix α7 and its preceding loop; at 283 K also the β17–β18 loop. Per-residue ΔR2eff places exchange on 30 residues at 298 K and 35 at 283 K (30 passing plus 5 exchange-broadened) by the row's transcription rule (ΔR2eff ≥ 2 s-1; the authors give no threshold) (HTPDZ-J1, HTPDZ-J28); the residues entering the global fit are not listed
- **Caveats:** The minor state is not identified structurally. Backbone and methyl lifetimes at 298 K differ about three-fold in samples prepared differently ([U-15N,13C] backbone sample versus [U-2H] methyl-labelled sample in 99.9% D2O), although the authors call the two data sets 'indicative of the same underlying process'. All isolated-PDZ NMR was in PBS with no phosphate-free control, and the exchanging loops are where divalent cations bind.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/HTPDZ_CPMG.md`](../proteins/HTPDZ_CPMG.md) (7 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

Quantitative exchange rates and populations are curated in the Release `0.1` synthesis above (no separate `v3` exchange rows added yet).

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Author-named dynamic regions and conformational PDB states

No author-named dynamic residue sets or conformational PDB states extracted in `v3` for this entry.

## 4. Papers read and explicit gaps

**Explicit figure-only, SI-only, or access gaps (1):**

- same protein (UniProt O43464) read under entry HTPDZ; see that row (): RelaxDB has separate entries for the same protein

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
