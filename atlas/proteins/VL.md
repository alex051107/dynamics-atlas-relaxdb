# Mouse anti-digoxin antibody 26-10 light-chain variable domain (VL

RelaxDB entry `VL` · set RelaxDB-133 · Mouse anti-digoxin antibody 26-10 light-chain variable domain (VL, Ig kappa chain V-II region 26-10, UniProt P01631), isolated, 113 residues (1MAJ/1MAK chain A)

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** does not. The source reports no second set of backbone NH resonances and states explicitly that slow motions between well-populated substates would be evidenced by multiple resonances, which are not observed for the backbone NH groups of the 26-10 VL domain; the exchange is bounded only between about 10-6 s and the 10-3 s CPMG refocusing period, and no kex or Delta-omega is printed, so no regime can be computed (VL-J4; E-r2, p. 304).

Reference state: in the RelaxDB source sample (free isolated VL, 30 °C, pH 5.5, acetate, 600 MHz) 24 of the 89 analysed backbone amides carry a significant exchange contribution to R2, from 0.36 to 7.56 s-1, with the largest at Thr-96 (7.56 +/- 3.11), Ser-61 (6.00 +/- 0.01), Gly-104 (5.28 +/- 1.28), Trp-40 (4.56 +/- 0.01) and Gln-6 (4.44 +/- 0.02); eight of them lie in CDR1 (Ser-26, Ser-32, Asn-35), CDR2 (Asn-58, Ser-61) and CDR3 (Thr-96, Thr-97, His-98). The authors place the motion between about 10-6 and 10-3 s, give no rate, population or chemical-shift difference, and suggest for Cys-23, Arg-24, Trp-40, Gln-43 and Phe-92 that nearby aromatic rings repack rather than the NH vector moving (VL-J4, E-r2). Under the single-field Rex rule of 2026-10-20 this is exchange detected in the reference state without a population, so the call is 'possible'. Context from the same paper: tau_r 8.45 ns, 15 amides with a nanosecond internal motion (tau_s 0.81-6.49 ns) and 15 with a picosecond one, the other 59 described by S2 alone between 0.72 and 1.00 (VL-J3, J6); six further residues with R2ex comparable to the error in R2 are set aside as possibly artifactual (VL-J7); amide 1H-2H exchange spans 3.7 x 10-6 to about 3 x 10-2 min-1 and follows hydrogen bonding and burial, not the relaxation-active motions (VL-J5).

## The free protein (reference state)

Free isolated 26-10 VL as deposited (the entry sequence), no VH partner and no digoxin. The RelaxDB source sample (doi:10.1002/prot.340150307, now full text): about 3.4 mM 15N protein in 0.50 ml, 30 °C, pH 5.5, 50 mM deuterated sodium acetate with 0.001% NaN3, 90% H2O/10% D2O, 599.95 MHz, single field, CPMG refocusing fixed at 0.9 ms (VL-J3, J4, J6, J7 marked is_wt_apo). The amide 1H-2H exchange of the same paper is a different sample state: 22 °C in nominally 100% D2O (VL-J5). At this concentration the domain is in a rapid monomer/dimer equilibrium (Kd 2.5 +/- 0.7 mM) (1994 abstract; the 1993 paper calls the sample predominantly monomeric by size exclusion).

| | |
|---|---|
| Where (residues) | us-ms exchange (R2ex, s-1): Val-3 1.20, Met-4 0.72, Thr-5 1.44, Gln-6 4.44, Thr-7 2.04, Cys-23 1.94, Arg-24 3.36, Ser-26 1.08, Ser-32 0.72, Asn-35 1.80, Trp-40 4.56, Gln-43 4.08, Ser-48 4.20, Lys-50 2.76, Asn-58 1.80, Ser-61 6.00, Phe-67 0.72, Asp-87 1.91, Phe-92 1.20, Thr-96 7.56, Thr-97 1.56, His-98 0.84, Gly-104 5.28, Gly-105 4.08 (VL-J4); possibly artifactual: Ser-25, Thr-36, Ser-57, Val-63, Glu-84, Ile-90 (VL-J7). Nanosecond motion: Val-2, Ser-10, Leu-11, Ala-19, Ala-45, Gly-46, Leu-51, Phe-60, Gly-73, Leu-78, Lys-79, Gly-89, Lys-108, Lys-112, Arg-113 (VL-J3). Entry numbering equals the paper's numbering. |
| Exchange rate kex | not measured: the paper gives exchange contributions R2ex in s-1 only (0.36-7.56 s-1 at 24 residues), and states that extracting temporal information would need the chemical-shift differences between environments, which are unknown (VL-J4) |
| Minor-state population pB | not measured (VL-J4); the dimer fraction is not given either, only Kd 2.5 +/- 0.7 mM for the monomer/dimer equilibrium (VL-J1) |
| Exchange regime | Not stated and not computable: no kex and no Delta-omega are printed, so the E-033 computation cannot be made. The authors bound the process between a lower limit of about 10-6 s, set by the population difference, the shift difference and the uncertainty in R2, and an upper limit comparable to the 10-3 s CPMG refocusing period, and note a general blind region between about 10-8 and 10-6 s (VL-J4). The monomer/dimer equilibrium is called rapid (VL-J1). |

Fallback statement: May have alternate conformations involving the N-terminal strand region (Val-3 to Thr-7), the strand-B/C positions Cys-23, Arg-24, Trp-40 and Gln-43 and all three CDRs (Ser-26, Ser-32, Asn-35; Asn-58, Ser-61; Thr-96, Thr-97, His-98) of the free isolated 26-10 VL: single-field 15N exchange contributions of 0.36-7.56 s-1 at 24 amides at 30 °C, pH 5.5, placed by the authors between about 10-6 and 10-3 s, with motions of nearby aromatic rings proposed for five of the sites (doi:10.1002/prot.340150307); no rate, population or second peak set, and the 3.4 mM sample is partly dimeric.

## Matching structures

## Other conditions (not the reference state)

- Free isolated VL, 30 °C, pH 5.5, 50 mM deuterated acetate, 3.4 mM, 600 MHz single field (1993 RelaxDB source, full text): possible. Exchange contributions at 24 amides, nanosecond motion at 15, picosecond at 15, S2 alone for 59 (VL-J3, J4, J6, J7; E-r1, E-r2).
- Same protein at 22 °C in nominally 100% D2O, pH* 5.5 (amide 1H-2H exchange): rates from (3.7 +/- 0.6) x 10-6 min-1 (Tyr-91) to bounds near 3 x 10-2 min-1, Trp-40 indole (2.6 +/- 0.1) x 10-5 min-1; hydrogen replacement, no conformational opening rate (VL-J5, VL-r3).
- VL inside the 26-10 Fab, native and digoxin-bound crystals: regional B-factor differences read as flexibility changes on VL:VH association or ligand binding, including a more mobile site away from the binding surface; static, no rate (VL-J8, VL-r4).
- VL paired with VH in the Fab/digoxin crystal versus the isolated solution structure: fold kept, subtle differences in CDR2, CDR3 and strands A, F and G; abstract only (VL-J2, VL-r2).
- Isolated VL at NMR concentrations: monomer/dimer equilibrium, Kd 2.5 +/- 0.7 mM, called rapid; binding kinetics, not a conformational state (VL-J1, VL-r1).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| VL-r1 | [Solution structure of an isolated antibody VL domain.](https://doi.org/10.1006/jmbi.1994.1137) | other | Reversible intermolecular monomer/dimer association; rapid equilibrium reported qualitatively. | abstract_only |
| VL-r2 | [Solution structure of an isolated antibody VL domain.](https://doi.org/10.1006/jmbi.1994.1137) | pdb_structure_comparison | Condition-dependent structural variation; independent exchange kinetics not established. | abstract_only |
| VL-r3 | [Characterization of the backbone dynamics of an anti‐digoxin…](https://doi.org/10.1002/prot.340150307) | other | Solvent exchange/protection associated with hydrogen bonding, burial and rare accessible conformers; not HDX-MS. | full_text |
| VL-r4 | [Characterization of the backbone dynamics of an anti‐digoxin…](https://doi.org/10.1002/prot.340150307) | pdb_structure_comparison | Ligand- and assembly-associated differences in crystallographic displacement parameters; underlying dynamics versus static disorder… | full_text |
| VL-VL_20261020213928-r1 | [Characterization of the backbone dynamics of an anti‐digoxin…](https://doi.org/10.1002/prot.340150307) | nmr_spin_relaxation | Low-amplitude fast backbone librations with additional nanosecond internal motions in a subset. | full_text |
| VL-VL_20261020213928-r2 | [Characterization of the backbone dynamics of an anti‐digoxin…](https://doi.org/10.1002/prot.340150307) | nmr_exchange_broadening | Exchange among different chemical environments; backbone conformational exchange and nearby aromatic/solvent motions are not uniquely… | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `VL`.

## Caveats

Call raised from unknown to possible on 2026-10-20 after the RelaxDB source paper (doi:10.1002/prot.340150307, Constantine et al. 1993) was read in full from the rendered pages and the OCR text (sources_cache/10.1002_prot.340150307_ocr.txt; the PDF has no usable text layer, so Tables I-III were read from the page images): exchange is detected in the reference state as single-field model-free R2ex at 24 of 89 analysed amides, and under the single-field Rex rule decided that night (ledger/redraft_notes.json, _RULE_single_field_rex) author-reported Rex in the reference state counts as exchange detected without a population. Fixed caveat: single-field Rex can also come from anisotropic tumbling; a dispersion experiment would confirm. literal_two_peak is 'does not' because the authors state that multiple resonances, which slow exchange between well-populated substates would produce, are not observed for the backbone NH groups. Three further limits sit on the exchange list: the authors themselves attribute five sites to aromatic-ring repacking, six more residues have R2ex within the error of R2 and are set aside, and the 3.4 mM sample is in a rapid monomer/dimer equilibrium (Kd 2.5 mM) that can add to R2. Hydrogen exchange was measured on a different sample (22 °C, 100% D2O) and reports hydrogen replacement. The abstract-only rows VL-VL_20261020152957-r1 and r2 are superseded and no longer cited; the 1994 structure rows VL-r1 and VL-r2 remain abstracts. Built from cases S6_r6_VL_20261020152957 and S6_r6_VL_20261020213928.

## Open questions

- The 1993 source paper measures the free isolated VL at 3.4 mM, where the domain is partly dimeric (Kd 2.5 +/- 0.7 mM): should the atlas treat the R2 exchange contributions as a property of the monomer, or flag them as possibly raised by self-association?
- The authors assign five of the 24 exchange sites (Cys-23, Arg-24, Trp-40, Gln-43, Phe-92) to motions of nearby aromatic rings rather than of the NH vector; should such side-chain-driven Rex count as backbone conformational exchange in the atlas?

Judgments: VL-J1, VL-J2, VL-J3, VL-J4, VL-J5, VL-J6, VL-J7, VL-J8 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
