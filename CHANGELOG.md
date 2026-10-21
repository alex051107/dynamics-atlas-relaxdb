# Changelog

## 0.1 — 21 October 2026

First release organised as an atlas: one page for each protein, machine-readable tables and separate method pages.

- 42 proteins in slice 1 (alternate APO states): 13 yes, 18 possible, 11 unknown.
- We read 11 RelaxDB source papers in full. Before: 12 yes, 11 possible, 19 unknown.
  - Azurin moved to yes. The full text gives the sample: reduced Cu(I) azurin, pH 5.5, 41 °C. It also gives an EXSY rate of 45 ± 6 s⁻¹ for the His35 exchange.
  - Seven proteins moved from unknown to possible: RNase HI, calbindin D9k, thioredoxin, TGF-α, an anti-digoxin VL domain, the TTF-1 homeodomain and SilB.
  - VcPth moved to possible because of the single-field Rex rule, not new evidence.
- Deposited-structure comparison for all 10 CPMG proteins, with side chains and alternate conformers for CypA, RNase A and K-Ras.
- Pipeline fixes:
  - Rows that both readers cannot verify go to adjudication.
  - The worker receives the accessions with an identical sequence.
  - A failed re-read cannot inherit an old file.
  - The structure comparison detects fused peptides.

## 0.0 — 20 October 2026

First public push: the calls for 42 proteins, judgments, evidence rows, structure tables for 7 proteins and the pipeline code.
