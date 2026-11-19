# Bugs found in audit and how we fix them

During our November 2026 audit of `771` checked extraction records across `131` open RelaxDB entries, we found five concrete failure modes. Every example below occurred on real papers and passed our basic verbatim-quote check without raising an error.

![Four real audit failures and the exact fixes planned for v4](../figures/known_bugs_and_fixes.png)

---

## Bug 1. Sample-condition misbinding passes substring quote checks

**Real failure.** In Barstar (`BARSTAR`, [`10.1021/jacs.0c00807`](https://doi.org/10.1021/jacs.0c00807), `PMC7304870`), the authors measured hyperpolarized-water (`HyperW`) HMQC at `50 °C` in buffered `D2O` (`pD 7`, resulting in `~1.8% H2O` after injection), lyophilized that sample to dryness, and reconstituted it in `90% H2O` (`pH 7`) for CLEANEX-PM amide exchange. Yet sample card `S1` collapsed both experiments into one row reading `pD 7 (HyperW, D2O); pH 7 (CLEANEX, ~1.8% H2O)`. A related weakness appeared in Ets-1 ([`walkthrough_ets1.md`](../atlas/walkthrough_ets1.md)), where `31 °C` backbone and `13 °C` arginine experiments shared one `temperature` field. Earlier in October, `~50` of `53` audited errors were similarly sample or condition misbindings. See [`atlas/v3_previews/16392_and_BARSTAR.md`](../atlas/v3_previews/16392_and_BARSTAR.md).

**Why current checks missed it.** Deterministic quote verification only checks whether quoted substrings appear inside the paper text. It does not test whether a solvent fraction, buffer, pH, temperature, or ligand stoichiometry belongs to the specific method row that points to it. Although an extra script caught `53` mixed-solvent / reconstitution warnings across the `305` Gemini papers, the earlier `466` Claude records never ran that scanner.

**Planned fix and verification test.**
1. Encode a hard rule in the next schema requiring **one experimental condition per `sample` ID** (splitting whenever `% H2O/% D2O`, `pH/pD`, temperature, salt, or ligand concentration changes).
2. Run the mixed-solvent / reconstitution check across **all** batches, blocking merged dual-condition sample strings in code.
3. Verify the gate using a planted condition-swap test (swapping `~1.8% H2O` onto `CLEANEX` must fail validation before the record can enter any table).

---

## Bug 2. Duplicate RelaxDB entries and placeholder UniProt collapse

**Real failure.** RelaxDB lists *E. coli* chemotaxis protein CheA (`P07363`) under two separate entry IDs, `CHEA` and `CHEAYBD` ([`CHEA_CHEAYBD.md`](../atlas/v3_previews/CHEA_CHEAYBD.md)). Seven overlapping papers extracted separately for both entries diverged sharply: on [`10.1073/pnas.2218467120`](https://doi.org/10.1073/pnas.2218467120), `CHEA` kept `11` HDX-MS rows while `CHEAYBD` kept `37`; on [`10.1007/s00723-018-1070-6`](https://doi.org/10.1007/s00723-018-1070-6), `CHEA` tagged *T. maritima* CheA as `homolog` while `CHEAYBD` tagged the same rows `same_protein_other_construct`; and the foundational `15N` linker dataset [`10.1021/bi951960e`](https://doi.org/10.1021/bi951960e) (`1,052` rows) sat only under `CHEA` while `CHEAYBD` missed it. Four more UniProt twin pairs exist (`BLAC_CPMG`/`27888`, `AQADK`/`AQADK_CPMG`, `ARGKIN`/`ARGKIN_CPMG`, `HTPDZ`/`HTPDZ_CPMG`). Worse, the workbook summary script grouped missing-UniProt placeholder string `'x'` as a real protein ID, falsely collapsing entry `5687` (`Four helix bundle`) onto `50332` (`Iron-compound ABC transporter`).

**Why current checks missed it.** Extraction keyed files by `(entry, DOI)` rather than canonical `UniProt` accession, and table generation did not reject placeholder strings like `'x'`.

**Planned fix and verification test.**
1. Canonicalize all paper ingestion and synthesis by verified `UniProt` accession (verified via sequence identity, as in Release `0.1`), carrying RelaxDB's `entry` and domain (`DBD` vs `LBD`; `YBD` vs full `CheA`) as metadata columns rather than duplicate extraction targets.
2. Add an explicit validator rejecting non-accession placeholders (`'x'`, blank, `'unknown'`) before summary grouping.

---

## Bug 3. Uncontrolled method names, scope drift, and un-reread earlier records

**Real failure.** In Glucocorticoid receptor ([`DBD82.md`](../atlas/v3_previews/DBD82.md)), `19` raw rows span target rat `DBD` ZZ-exchange, human `LBD` CPMG dispersion, MD clusters, live-cell FCS diffusion (`ms`), EMSA DNA dissociation (`min`), and COS-1 cell FRET. Across the full workbook (`19,958` rows), `method` uses free-text strings (`md_simulation` `49`, `molecular_dynamics` `25`, `FRET` `10` vs `fret` `3`, `epr_deer` / `epr_deer_distance` / `deer_epr_distance` / `epr_distance_deer`, and three X-ray strings). Meanwhile, prompt rules on figure captions, approximate prose values, and conformational state PDBs shifted three times during batch reading (`67/108` edited during human reread, adding `~139` of `204` final states), while `168` early records (`78` source papers + `90` early PMC records) were never re-read under those updated rules.

**Why current checks missed it.** Schema validation checked field presence, not a closed controlled vocabulary for `method` or domain/mechanism scope.

**Planned fix and verification test.**
1. Wait for Gina's ruling on [`REVIEW_GUIDE.md`](../REVIEW_GUIDE.md) (`Rank 1` and `Rank 2`), then encode an explicit `method` enum and scope enum into code validation (`ExperimentalDynamics` separated cleanly from `MD` and cellular/intermolecular `Auxiliary` kinetics).
2. Freeze **one** specification before extraction starts and re-process the `168` older records under it.

---

## Bug 4. Massive bulk SI tables drown rare mechanistic exchange parameters

**Real failure.** In TEM-1 β-lactamase (`16392`, [`16392_and_BARSTAR.md`](../atlas/v3_previews/16392_and_BARSTAR.md)), `1,879` per-residue SI spin-relaxation rows (`10.1021/bi060414q`, using construct numbering starting at `26` instead of Ambler numbering) represent `98.3%` of the protein's `1,912` rows, burying the `4` WT Ω-loop CEST rows (`1.05 ± 0.03%`, `kex = 98 ± 6 s−1`) and `13` `G238S` CPMG dispersion rows across `8` open/closed crystal structures.

**Why current checks missed it.** Row-level checks treat every extracted row identically, without distinguishing dense per-residue baseline arrays from fitted slow-exchange kinetic models.

**Planned fix and verification test.**
1. Separate `PerResidueRelaxation` (`R1/R2/NOE/S2/τe/Rex` per site) from `ExchangeProcesses` (`kex/kAB/pB/Δω` tied to conformational PDB states) and from `ProteinSummary` synthesis cards (restoring the Release `0.1` layout).
2. Add residue-number mapping from construct numbering to canonical UniProt sequence positions, plus BMRB numerical cross-checks as implemented for the `10` CPMG entries in `0.1`.

---

## Bug 5. Incomplete paper coverage and blind-check prevalence bias

**Real failure.** Across `131` open entries, `23` (`22` unread + `5687` `'x'` bug) have `0` papers read in the `v3` sweep, `988` DOIs from our November 12 candidate table (`244` marked full text, `205` with open PMC links) remain unread under the strict schema, and `336` Kosmos-reported full-text rows (`321` matched abstract-only candidates locally) remain undownloaded. Furthermore, `96.7%` (`295/305`) of the latest batch contained `0` in-scope numeric rows, meaning raw agreement metrics appear artificially high even though all `4` blind disagreements occurred inside the rare non-NMR valued subset (`DBD82`).

**Planned fix and verification test.**
1. Run a low-cost triage gate first to exclude clinical/cell/non-target papers before running full extraction on the unread `244` full-text DOIs and Kosmos package.
2. Report prevalence-adjusted agreement (`valuated-paper recall`, condition-binding error rate, and Gwet's `AC1`) separately on valued vs zero-row strata in [`quality.md`](quality.md).
