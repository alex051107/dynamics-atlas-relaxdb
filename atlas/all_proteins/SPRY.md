# SPRY domain-containing SOCS box protein 2 (`SPRY`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `O88838` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`possible`)](../proteins/SPRY.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `possible` (strict two-peak reading: `does not: The authors attribute the missing loop-CD amides H119-G125 to intermediate-timescale exchange; no second peak set is reported, and CPMG shows no dispersion in the observable amides.`)
- **Reference state:** Free wild-type SSB-2 (12-224), no peptide or inhibitor; 22 °C, pH 7.0, 10 mM sodium phosphate, 50 mM NaCl, 2 mM EDTA, 0.02% NaN3; the input card gives no BMRB id
- **Exchange rate (`kex`):** not measured (SPRY-J4); no dispersion at nuCPMG 20-1000 Hz in observable amides (SPRY-J3, SPRY-r2)
- **Minor-state population (`pB`):** not measured (SPRY-J4)
- **Exchanging region:** loop CD H119-G125 (entry 114-120) (SPRY-J4); fast ps-ns motion separately in loop DE I135-E165 (SPRY-J1)
- **Caveats:** The call rests on missing peaks, not dispersion; the NMR collaborator is asked whether that counts as µs-ms detection. Peptide- and inhibitor-bound states are kept out of the apo call. All mouse NMR is in phosphate/EDTA with no buffer control. No PDB entry is shown in the rows as a loop-CD alternate conformer, so no structure is matched.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/SPRY.md`](../proteins/SPRY.md) (15 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **intermediate conformational exchange (no backbone assignment)** ([`10.1038/nsmb1034`](https://doi.org/10.1038/nsmb1034), sample `S1`): 119–125 in the CD loop
- **flexible on ps-ns timescales (15N relaxation)** ([`10.1038/nsmb1034`](https://doi.org/10.1038/nsmb1034), sample `S1`): loop DE (135-165)

### Conformational and complex PDB states (`States`)

- [`2AFJ`](https://www.rcsb.org/structure/2AFJ): NMR structure ensemble of SSB-2 (12-224), 20 structures; not tied to a named conformational state ([`10.1038/nsmb1034`](https://doi.org/10.1038/nsmb1034))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1038/nsmb1034`](https://doi.org/10.1038/nsmb1034) | 0 | 1 | 2 | 2 | The paper prints no numeric dynamics value for SSB-2 in its text. 15N R1, R2 and heteronuclear NOE (Fig. 2) an |

**Explicit figure-only, SI-only, or access gaps (2):**

- Per-residue 15N R1, R2 and steady-state NOE values ([`10.1038/nsmb1034`](https://doi.org/10.1038/nsmb1034)): figure only (Figure 2)
- Slow and fast amide exchange per residue ([`10.1038/nsmb1034`](https://doi.org/10.1038/nsmb1034)): figure only (Figure 2)

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
