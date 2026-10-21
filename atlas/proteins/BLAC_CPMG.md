# Mycobacterium tuberculosis β-lactamase BlaC

RelaxDB entry `BLAC_CPMG` · set CPMG-10 · Mycobacterium tuberculosis β-lactamase BlaC, wild type

## Answer

**Possible: exchange is detected in the free protein, but no population is measured.**

**Strict two-peak reading:** cannot tell. Δω and pB of the 860 s-1 process are undetermined; the authors call the four broadened amides 'intermediate to fast'; WT shows no peak doubling (doubling only in G132N and the clavulanate adduct).

Free wild-type BlaC shows active-site millisecond exchange at about 860 s-1, but the authors could not determine the excited-state population or shift difference 'with any accuracy'. Four anion-site amides are broadened beyond detection; the authors calculate that the same process would need a minor state above 15% to do this, which is an estimate rather than a measured population.

## The free protein (reference state)

Wild-type resting-state (free) BlaC, 298 K; pH 6.4, 94 mM sodium MES, 6% D2O, no phosphate

| | |
|---|---|
| Where (residues) | Group fit: F68, C69, T71, E166, E168, N170, T215, A218 (named in Elings 2021 SI Table S3, doi:10.1128/aac.02628-20; BLAC-J1); broadened beyond detection: Ser70, Ser130, Thr235, Thr237 (Ambler numbering; entry 43, 101, 210, 212 by the project's alignment) |
| Exchange rate kex | (8.6 ± 0.6) x 10^2 s-1 at 298 K, two-state model assumed, two-field (14.1 and 20.0 T) group fit of eight amides (BLAC-J1, BLAC-r1, BLAC-r4) |
| Minor-state population pB | not determined with any accuracy (authors; BLAC-J1, BLAC-r1); the authors' own Bloch-McConnell estimate is that pB must exceed 15% (with Δω > 0.1 ppm 1H and/or 1 ppm 15N at 20 T) if the four broadened amides share the 860 s-1 process (BLAC-J2) |
| Exchange regime | No regime stated for the 860 s-1 process (Δω not determined). For the four anion-site amides broadened beyond detection the authors write that 'an intermediate to fast exchange process may be present in the active site' (2020; BLAC-r1, BLAC-J2). |

Fallback statement: Shows millisecond exchange in the active site (kex ≈ 860 s-1, 15N TROSY CPMG at 14.1 and 20.0 T; group-fit residues F68, C69, T71, E166, E168, N170, T215, A218); minor-state population, shifts and structure not determined; no minor-state peaks observed. Ser70, Ser130, Thr235 and Thr237 are broadened beyond detection, by the same or a separate process (Elings 2020, doi:10.1128/aac.02025-19).

## Matching structures

Deposited-structure comparison: Wild-type apo crystals stay within 0.8 Å of 2GDN in the active site. A flipped Ω loop appears only in the P167S mutant (8OE1, 8OE5); its paper was not read. Table: [`data/structures/BLAC_CPMG.md`](../../data/structures/BLAC_CPMG.md).

## Other conditions (not the reference state)

- WT CEST at 288 and 298 K: no_evidence for exchange at 20–200 s-1 (BLAC-J3, BLAC-r2).
- G132N mutant, 298 K, MES: yes. Doubled peaks, kex 88 ± 6 s-1, state B 40 ± 2%; the G132N crystal (PDB 7A74, grown with 100 mM sodium phosphate added, while the NMR was phosphate-free) shows double conformations, and the authors write that the X-ray and NMR observations 'may thus represent the same phenomenon' (BLAC-J14, BLAC-J17, BLAC-r6, BLAC-r9).
- K234R mutant: no_evidence by 15N CPMG at 298 K (BLAC-J12, BLAC-r5).
- Avibactam adduct: possible. kex (3.4 ± 0.2) x 10^3 s-1 from a single-field fit, no population (BLAC-J7, BLAC-r3).
- Clavulanate adduct: unresolved. At least 21 amides split into peaks at relative occupancy 42 ± 3%; exchange between them was not measured, and the authors infer kex < 100 s-1 from the doubling (BLAC-J9, BLAC-r3).
- Directed-evolution mutants in 100 mM phosphate: peak doubling read as slow exchange well below 50 s-1 (authors: '<<50 s−1'), populations not quantified (BLAC-J19, BLAC-r10); I105Y-S130G and I105G-G132N in phosphate: no_evidence by CPMG (BLAC-J21, BLAC-J22, BLAC-r12).

## Key evidence

| Row | Paper | Method | What it shows | Read |
|---|---|---|---|---|
| BLAC-r1 | [beta-Lactamase of Mycobacterium tuberculosis Shows Dynamics in the…](https://doi.org/10.1128/aac.02025-19) | nmr_relaxation_dispersion | low-millisecond conformational exchange in the active site | full_text |
| BLAC-r2 | [beta-Lactamase of Mycobacterium tuberculosis Shows Dynamics in the…](https://doi.org/10.1128/aac.02025-19) | nmr_spin_relaxation | pico- to nanosecond backbone flexibility; also no high-millisecond process | full_text |
| BLAC-r3 | [beta-Lactamase of Mycobacterium tuberculosis Shows Dynamics in the…](https://doi.org/10.1128/aac.02025-19) | nmr_exchange_broadening | inhibitor-coupled increase of active-site exchange; extra slower process for the clavulanic acid adduct | full_text |
| BLAC-r4 | [Two beta-Lactamase Variants with Reduced Clavulanic Acid Inhibition…](https://doi.org/10.1128/aac.02628-20) | nmr_relaxation_dispersion | low-millisecond exchange centred on the active site | full_text |
| BLAC-r5 | [Two beta-Lactamase Variants with Reduced Clavulanic Acid Inhibition…](https://doi.org/10.1128/aac.02628-20) | nmr_relaxation_dispersion | loss of millisecond active-site exchange | full_text |
| BLAC-r6 | [Two beta-Lactamase Variants with Reduced Clavulanic Acid Inhibition…](https://doi.org/10.1128/aac.02628-20) | nmr_relaxation_dispersion | slow two-state exchange over a broad region around the active site | full_text |
| BLAC-r7 | [Two beta-Lactamase Variants with Reduced Clavulanic Acid Inhibition…](https://doi.org/10.1128/aac.02628-20) | nmr_exchange_broadening | intermediate-timescale exchange broadening beyond detection around the active site and the phosphate site | full_text |
| BLAC-r9 | [Two beta-Lactamase Variants with Reduced Clavulanic Acid Inhibition…](https://doi.org/10.1128/aac.02628-20) | pdb_structure_comparison | alternate side-chain and loop conformations, cis-peptide isomerisation | full_text |
| BLAC-r10 | [Directed evolution of a beta-lactamase samples a wide variety of…](https://doi.org/10.1002/pro.70322) | nmr_exchange_broadening | micro- to millisecond exchange of the omega loop plus slow exchange between two or more global states | full_text |
| BLAC-r12 | [Phosphate ions modulate enzyme activity and epistatic effects in two…](https://doi.org/10.1002/pro.70325) | nmr_relaxation_dispersion | absence of detectable slow and millisecond exchange in solution | full_text |
| BLAC-r18 | [Phosphate Promotes the Recovery of Mycobacterium tuberculosis…](https://doi.org/10.1021/acs.biochem.7b00556) | nmr_exchange_broadening | intermediate exchange broadening of the four amides lining the active-site anion site; slow or no exchange between free and adduct states | full_text |

All rows for this protein: [`data/evidence.csv`](../../data/evidence.csv), filter `Protein (RelaxDB entry)` = `BLAC_CPMG`.

## Caveats

Whether the four broadened anion-site amides and the 860 s-1 process are one process or two is unresolved. In every BlaC crystal published as of 2020 those four side chains hydrogen-bond a ligand or a buffer anion, and MES (a sulfonate) was never compared with another buffer. Mutant NMR from 2024-2025 used phosphate, which binds the active site, so it is not like-for-like with the WT MES data. A cached SAXS study proposing an open apo shape has no evidence row and was not used.

## Open questions

- Origin of the four missing anion-site amides: Elings 2020 links them to the 860 s-1 process via a Bloch-McConnell estimate (pB above 15% with delta omega above 0.1 ppm 1H and/or 1 ppm 15N), while the same paper cannot determine pB from dispersion and Elings 2021 says only that 'another process' than phosphate exchange is responsible (J1 vs J2); one process or two is unresolved.
- Functional role: Elings 2020 suggests the 860 s-1 exchange may matter for catalysis because it exceeds kcat 111 s-1; Elings 2021 finds no dispersion in the active K234R mutant and concludes millisecond dynamics are not required (J1 vs J12).
- Open versus closed apo state: a cached SAXS study of free BlaC (Sagar 2017, sources_cache/BLAC_CPMG/PMC5524718.txt) proposes an open apo shape, while Elings 2020 finds tau_c matching the closed crystal structure and no evidence for an open state (J5); the SAXS study has no evidence row, so the conflict is recorded but not judged.
- Crystal alternates versus solution: G132N crystal double conformations match NMR state populations (J17 vs J14), but I105Y-S130G crystal double conformations have no NMR counterpart (J23 vs J21).
- Which data set produced the RelaxDB BLAC_CPMG labels ('Rex > 2 Hz from 850 Hz data')? Elings 2020 free-state relaxation data are BMRB 27888 (94 mM MES pH 6.4, 298 K), but the papers use Rex thresholds of 3 s-1 (2020) and 5 s-1 (2021), and the four anion-site amides cannot carry labels; is 27888 the source?
- The wild-type NMR evidence is all in MES (20 mM pH 6.0 in 2017; 94 mM pH 6.4 in 2020/2021), while every 2024-2025 mutant study used 100 mM phosphate, which binds the active site (KD 27 ± 11 mM). Should mutant-versus-WT dispersion comparisons across these buffers be treated as not comparable, and is MES itself (a sulfonate anion) a concern for the anion-site broadening?

Judgments: BLAC-J1, BLAC-J2, BLAC-J3, BLAC-J7, BLAC-J9, BLAC-J12, BLAC-J14, BLAC-J17, BLAC-J19, BLAC-J21, BLAC-J22 in [`data/judgments.jsonl`](../../data/judgments.jsonl).
