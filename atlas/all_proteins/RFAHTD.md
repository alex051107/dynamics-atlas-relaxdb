# Transcription antitermination protein RfaH (`RFAHTD`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P0AFW0` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `700/800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`yes`)](../proteins/RFAHTD.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `yes` (strict two-peak reading: `qualifies: The largely unfolded state B is seen as its own peak set (CEST on both A and B peaks, zz-exchange) and exchanges on a 300 ms scale in the perdeuterated sample. B is the unfolded domain, not the α-hairpin; the sub-millisecond states A', B' and B'' are dark and seen only through CPMG and CEST.`)
- **Reference state:** Wild-type isolated CTD (β-barrel), no partner, 25 °C, pH 6.5: perdeuterated 1.0 mM U-[15N/2H] sample in 25 mM potassium phosphate, 0.5 mM EDTA, 1 mM PMSF (PNAS 2025); protonated 0.7–1 mM 15N sample in 20 mM sodium phosphate, 100 mM NaCl, 1 mM EDTA (eLife)
- **Exchange rate (`kex`):** A'↔A τex about 500 µs (Results and Fig. 6; the abstract says about 1 ms) (RFAHTD-J4, RFAHTD-r9, RFAHTD-r13). B↔B' τex about 1.2–1.3 ms; B↔B'' about 800 µs (branched) or B'↔B'' about 1 ms (linear); linear-model kBB' 21.6 ± 2.4 s-1, kB'B 675 ± 25 s-1 (RFAHTD-J5, RFAHTD-r14). A↔B folding/unfolding: kex 14.80 ± 1.31 s-1 (kAB 0.82 ± 0.10, kBA 13.98 ± 1.24 s-1), protonated (RFAHTD-J7, RFAHTD-r5); kAB about 0.8 s-1, kBA about 2.4 s-1, τex about 300 ms, perdeuterated (RFAHTD-J6, RFAHTD-r8).
- **Minor-state population (`pB`):** A' about 0.35% (A about 76–77%); B' about 0.25–0.35%; B'' about 0.05% (RFAHTD-J4, RFAHTD-J5, RFAHTD-r9). Unfolded B: 5.53 ± 0.46% (reported with pA 94.47 ± 0.46%), protonated (RFAHTD-J7, RFAHTD-r5); about 25% (pA about 75%) by two-site CEST and about 23% in the five-state fit, perdeuterated (RFAHTD-J6, RFAHTD-r8, RFAHTD-r9).
- **Exchanging region:** 35 residues in the five-state fit (SI Tables S3–S6): T109, Y111, a G113–F123 subset, G125, Q127, I129, D134–E136, R138–I146, K148, I150, V154, K155, E158–R160, L162 (T109 lies outside the entry); A' proposed as a β1/β2-loop change (RFAHTD-J4). 45 sites with A and B CEST profiles, T109–L162 (RFAHTD-J6). B' and B'' differ in helix α5* of the unfolded ensemble (RFAHTD-J5).
- **Structure comparison:** [{"pdb": "2OUG", "what": "Full-length RfaH crystal with the CTD as an α-hairpin packed on the NTD, the other fold of the same sequence (the isolated barrel is 2LCL). It does not match any isolated-CTD minor state: the minor ensemble resembles the urea-unfolded CTD with residual structure, not the α-hairpin, and free full-length RfaH does not visit the β state above 0.2%.", "evidence_row": "RFAHTD-r3; RFAHTD-r5; RFAHTD-r17"}]
- **Caveats:** The unfolded-state population differs between the protonated (5.5%) and perdeuterated (about 25%) samples, which also differ in buffer and construct start; kAB agrees but kBA does not, and the rows do not say which difference causes it. The A' lifetime is printed as about 500 µs and about 1 ms in the same paper. Linear and branched five-state schemes fit equally well. The judgments place the folding/unfolding exchange in the slower-than-ms window. The RelaxDB R1/R2/NOE sample is unidentified (the likely Tudor-domain paper was read as abstract only).
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/RFAHTD.md`](../proteins/RFAHTD.md) (14 key curated rows)

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
