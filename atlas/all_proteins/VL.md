# Ig kappa chain V-II region 26-10 (`VL`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P01631` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `600` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`possible`)](../proteins/VL.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `possible` (strict two-peak reading: `does not: the source reports no second set of backbone NH resonances and states explicitly that slow motions between well-populated substates would be evidenced by multiple resonances, which are not observed for the backbone NH groups of the 26-10 VL domain; the exchange is bounded only between about 10-6 s and the 10-3 s CPMG refocusing period, and no kex or Delta-omega is printed, so no regime can be computed (VL-J4; E-r2, p. 304).`)
- **Reference state:** Free isolated 26-10 VL as deposited (the entry sequence), no VH partner and no digoxin. The RelaxDB source sample (doi:10.1002/prot.340150307, now full text): about 3.4 mM 15N protein in 0.50 ml, 30 °C, pH 5.5, 50 mM deuterated sodium acetate with 0.001% NaN3, 90% H2O/10% D2O, 599.95 MHz, single field, CPMG refocusing fixed at 0.9 ms (VL-J3, J4, J6, J7 marked is_wt_apo). The amide 1H-2H exchange of the same paper is a different sample state: 22 °C in nominally 100% D2O (VL-J5). At this concentration the domain is in a rapid monomer/dimer equilibrium (Kd 2.5 +/- 0.7 mM) (1994 abstract; the 1993 paper calls the sample predominantly monomeric by size exclusion).
- **Exchange rate (`kex`):** not measured: the paper gives exchange contributions R2ex in s-1 only (0.36-7.56 s-1 at 24 residues), and states that extracting temporal information would need the chemical-shift differences between environments, which are unknown (VL-J4)
- **Minor-state population (`pB`):** not measured (VL-J4); the dimer fraction is not given either, only Kd 2.5 +/- 0.7 mM for the monomer/dimer equilibrium (VL-J1)
- **Exchanging region:** us-ms exchange (R2ex, s-1): Val-3 1.20, Met-4 0.72, Thr-5 1.44, Gln-6 4.44, Thr-7 2.04, Cys-23 1.94, Arg-24 3.36, Ser-26 1.08, Ser-32 0.72, Asn-35 1.80, Trp-40 4.56, Gln-43 4.08, Ser-48 4.20, Lys-50 2.76, Asn-58 1.80, Ser-61 6.00, Phe-67 0.72, Asp-87 1.91, Phe-92 1.20, Thr-96 7.56, Thr-97 1.56, His-98 0.84, Gly-104 5.28, Gly-105 4.08 (VL-J4); possibly artifactual: Ser-25, Thr-36, Ser-57, Val-63, Glu-84, Ile-90 (VL-J7). Nanosecond motion: Val-2, Ser-10, Leu-11, Ala-19, Ala-45, Gly-46, Leu-51, Phe-60, Gly-73, Leu-78, Lys-79, Gly-89, Lys-108, Lys-112, Arg-113 (VL-J3). Entry numbering equals the paper's numbering.
- **Caveats:** Call raised from unknown to possible on 2026-10-20 after the RelaxDB source paper (doi:10.1002/prot.340150307, Constantine et al. 1993) was read in full from the rendered pages and the OCR text (sources_cache/10.1002_prot.340150307_ocr.txt; the PDF has no usable text layer, so Tables I-III were read from the page images): exchange is detected in the reference state as single-field model-free R2ex at 24 of 89 analysed amides, and under the single-field Rex rule decided that night (ledger/redraft_notes.json, _RULE_single_field_rex) author-reported Rex in the reference state counts as exchange detected without a population. Fixed caveat: single-field Rex can also come from anisotropic tumbling; a dispersion experiment would confirm. literal_two_peak is 'does not' because the authors state that multiple resonances, which slow exchange between well-populated substates would produce, are not observed for the backbone NH groups. Three further limits sit on the exchange list: the authors themselves attribute five sites to aromatic-ring repacking, six more residues have R2ex within the error of R2 and are set aside, and the 3.4 mM sample is in a rapid monomer/dimer equilibrium (Kd 2.5 mM) that can add to R2. Hydrogen exchange was measured on a different sample (22 °C, 100% D2O) and reports hydrogen replacement. The abstract-only rows VL-VL_20261020152957-r1 and r2 are superseded and no longer cited; the 1994 structure rows VL-r1 and VL-r2 remain abstracts. Built from cases S6_r6_VL_20261020152957 and S6_r6_VL_20261020213928.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/VL.md`](../proteins/VL.md) (6 key curated rows)

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
