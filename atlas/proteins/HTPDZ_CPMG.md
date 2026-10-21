# Human HtrA2 PDZ domain

RelaxDB entry `HTPDZ_CPMG` · set CPMG-10 · Human HtrA2 PDZ domain, isolated (author residues 349–458)

## Answer

**Yes: a minor state is measured in the free protein.**

**Strict two-peak reading:** cannot tell. No regime statement and no Δω printed; the authors report no minor-state peaks.

The isolated apo PDZ shows µs–ms exchange in the N-terminus, helix α5 with its loop to β15, and helix α7 with its preceding loop, fitted globally as one two-site process with a 15.2% minor state at 298 K. Methyl MQ CPMG gives a similar 16.6% minor state, which the authors call 'indicative of the same underlying process'. SEC-MALS gives a dimerization KD lower limit of 13 ± 1.65 mM; the authors do not link dimerization to the CPMG minor state.

## The free protein (reference state)

Isolated wild-type apo HtrA2 PDZ, 298 K and 283 K; PBS pH 7.4 (the PDZ sample buffer; the NMR buffer is not stated separately), no added divalent metal; 500 µM

| | |
|---|---|
| Where (residues) | N-terminus, helix α5 and the α5–β15 loop, helix α7 and its preceding loop; at 283 K also the β17–β18 loop. Per-residue ΔR2eff places exchange on 30 residues at 298 K and 35 at 283 K (30 passing plus 5 exchange-broadened) by the row's transcription rule (ΔR2eff ≥ 2 s-1; the authors give no threshold) (HTPDZ-J1, HTPDZ-J28); the residues entering the global fit are not listed |
| Exchange rate kex | reported as τex, not kex: 0.42 ± 0.004 ms at 298 K and 0.98 ± 0.005 ms at 283 K (fit errors from a single experiment, n = 1); kex ≈ 1/τex is the row's assumption, giving about 2,400 s-1 (HTPDZ-J1) and about 1,020 s-1 (HTPDZ-J28); methyl τex 1.19 ± 0.07 ms at 298 K (HTPDZ-J3) |
| Minor-state population pB | 15.2% at 298 K (HTPDZ-r1); 16.1% at 283 K (HTPDZ-r2); the text says only 'decreasing from 16.1 to 15.2%', with no error given and the temperature assignment from Fig. 2c; methyl 16.6 ± 0.4% at 298 K (HTPDZ-r3) |
| Exchange regime | not stated by the authors; no Δω printed. The 2 kHz spin-lock control gives mainly planar R2(R1ρ), so no faster (< 80 µs) contribution is seen; this is not a regime assignment (HTPDZ-J4). |

Fallback statement: May have an alternate conformation differing at the N-terminus, helix α5 and the α5–β15 loop, and helix α7 with its preceding loop, based on 15N BEST-TROSY CPMG at 298 and 283 K and methyl MQ CPMG (doi:10.1038/s41467-024-48997-5).

## Matching structures

Deposited-structure comparison: No apo structure of the isolated PDZ domain exists. The α5 region differs by 4-11 Å in the BIRC6 complex 8E2K (not checked against its paper). Table: [`data/structures/HTPDZ_CPMG.md`](../../data/structures/HTPDZ_CPMG.md).

## Other conditions (not the reference state)

- Peptide-bound isolated PDZ: unknown, not measured in the rows (HTPDZ-J8).
- Isolated PDZ with Ca2+ or Zn2+: unknown; methyl CPMG exists in the source but has no evidence row (HTPDZ-J9).
- Full-length S306A trimer, 313 K, apo: exchange in helix α5 among other regions, two-point data only, mutant construct (HTPDZ-J11, HTPDZ-r10).
- Full-length trimer, 40 °C: a PDZ hexamer-interface contribution and interface exchange when neighbours are held open; oligomerization, not intradomain exchange (HTPDZ-J12, HTPDZ-J13, HTPDZ-r14, HTPDZ-r15).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| HTPDZ-r1 | [Structural basis of substrate recognition and allosteric activation…](https://doi.org/10.1038/s41467-024-48997-5) | nmr_relaxation_dispersion | microsecond-to-millisecond conformational exchange | full_text |
| HTPDZ-r2 | [Structural basis of substrate recognition and allosteric activation…](https://doi.org/10.1038/s41467-024-48997-5) | nmr_relaxation_dispersion | microsecond-to-millisecond conformational exchange | full_text |
| HTPDZ-r3 | [Structural basis of substrate recognition and allosteric activation…](https://doi.org/10.1038/s41467-024-48997-5) | nmr_relaxation_dispersion | microsecond-to-millisecond conformational exchange | full_text |
| HTPDZ-r4 | [Structural basis of substrate recognition and allosteric activation…](https://doi.org/10.1038/s41467-024-48997-5) | nmr_spin_relaxation | ps–ns backbone flexibility and separately fitted exchange contribution | full_text |
| HTPDZ-r10 | [Structural basis of substrate recognition and allosteric activation…](https://doi.org/10.1038/s41467-024-48997-5) | nmr_relaxation_dispersion | microsecond-to-millisecond exchange | full_text |
| HTPDZ-r14 | [Dissecting the role of interprotomer cooperativity in the activation…](https://doi.org/10.1073/pnas.2111257118) | nmr_relaxation_dispersion | microsecond-to-millisecond interprotomer allosteric exchange | full_text |
| HTPDZ-r15 | [Dissecting the role of interprotomer cooperativity in the activation…](https://doi.org/10.1073/pnas.2111257118) | nmr_relaxation_dispersion | microsecond-to-millisecond interprotomer allosteric exchange | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `HTPDZ_CPMG`.

## Caveats

The minor state is not identified structurally. Backbone and methyl lifetimes at 298 K differ about three-fold in samples prepared differently ([U-15N,13C] backbone sample versus [U-2H] methyl-labelled sample in 99.9% D2O), although the authors call the two data sets 'indicative of the same underlying process'. All isolated-PDZ NMR was in PBS with no phosphate-free control, and the exchanging loops are where divalent cations bind.

## Open questions

- Backbone versus methyl lifetime at 298 K: 15N CPMG gives τex 0.42 ± 0.004 ms (15.2%, r1) while methyl MQ CPMG gives 1.19 ± 0.07 ms (16.6 ± 0.4%, r3); the authors call it one underlying process, but the samples differ (protonated in H2O versus deuterated ALVIT in 99.9% D2O) and the lifetimes differ about three-fold.
- The 298 K and 283 K global fits use different residue sets: Source Data sheet 2a has ΔR2eff for 37 residues at 298 K and 50 at 283 K, and the exchanging sets differ (J1, J28); the residues entering each global fit are still not listed (r1, r2).
- Which sample produced the RelaxDB HTPDZ_CPMG labels: 15N CPMG at 298 K or 283 K (700/900 MHz), and which construct (entry 352-458 plus LE, paper construct 349-458, BMRB 51320 entity of 156 residues)?
- All isolated-PDZ NMR was in PBS pH 7.4 with no phosphate-free control, and the exchanging α5-β15 and pre-α7 loops are where divalent cations bind; should the exchange be flagged as untested for phosphate binding?

Judgments: HTPDZ-J1, HTPDZ-J28, HTPDZ-J3, HTPDZ-J4, HTPDZ-J8, HTPDZ-J9, HTPDZ-J11, HTPDZ-J12, HTPDZ-J13 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
