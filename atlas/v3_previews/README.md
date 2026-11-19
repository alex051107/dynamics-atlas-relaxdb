# Worked protein synthesis previews (`19 November 2026`)

In Release `0.1` (`21 October 2026`), every protein became a structured synthesis page like [`CYPA_CPMG.md`](../proteins/CYPA_CPMG.md), with one verdict, reference versus perturbed conditions, structure comparison, verbatim quotes, and open questions.

In our scaled November literature sweep (`104` of `131` open entries, `19,958` printed numbers), extraction stopped at the per-paper table level. A `19,958`-row spreadsheet is easy for software to check against quotes, **but impossible for an NMR expert to review quickly**.

These **four worked previews** restore that protein-level view. Together with [`walkthrough_ets1.md`](../walkthrough_ets1.md), they translate raw workbook rows back into readable pages and isolate the borderline questions we ask Gina to decide before running `v4`.

| Preview | RelaxDB entry (UniProt) | Decision it tests for expert review | Workbook scale |
|---|---|---|---|
| [`FKBP.md`](FKBP.md) | `FKBP` (`P62942`, human FKBP12) | **Multi-timescale NMR plus crystal/MD boundary.** Spans ps–ns backbone relaxation (`331` rows), ms `Trp59` ring flip, slow `Gly89` `zz-exchange`, HX reactivity, `15` MD rows, and `3` cryo-crystal dual conformer occupancies. | `30` papers (`6` valued), `391` rows, `50` state rows (`34` distinct PDBs) |
| [`DBD82.md`](DBD82.md) | `DBD82` (`P06536`, glucocorticoid receptor) | **Domain and method boundary.** Mixes rat `GR DBD` ZZ-exchange, human `GR LBD` CPMG dispersion, MD clusters, live-cell FCS diffusion, EMSA DNA off-rates, and cell FRET. | `23` papers (`6` valued), `19` rows, `24` state rows (`19` distinct PDBs) |
| [`CHEA_CHEAYBD.md`](CHEA_CHEAYBD.md) | `CHEA` + `CHEAYBD` (`P07363`, *E. coli* CheA) | **Duplicate-entry conflict.** Two RelaxDB entries share one UniProt and `7` valued DOIs, yet diverge on row counts (`11` vs `37`), species tags, and omit `1,052` backbone rows from `CHEAYBD`. | `41` records (`23 + 18`), `1,172` un-deduplicated rows |
| [`16392_and_BARSTAR.md`](16392_and_BARSTAR.md) | `16392` (`P62594`, TEM-1) and `BARSTAR` (`P11540`) | **Bulk SI swamp plus silent sample conflation.** TEM-1 buries `4` Ω-loop CEST rows under `1,879` SI rows; Barstar exposes a `90% H2O` CLEANEX vs `~1.8% H2O` HyperW conflation that passed substring checks. | `18` papers (`1,912` rows, `22` state rows) and `8` papers (`7` rows, `3` state rows) |

## Four choices we ask Gina to confirm on these previews

1. **Aggregation unit (`FKBP`, `DBD82`, `CHEA`).** Should extraction and summaries index by canonical full-length `UniProt` ID with a required `domain` tag, rather than keeping separate domain entries like `DBD82` or `CHEAYBD`?
2. **Inclusion cutoff (`DBD82`, `FKBP`).** Should `MD` simulations, `100 K` crystal dual occupancies, live-cell `FCS` diffusion, and intermolecular `EMSA` DNA off-rates leave the main measurement table or stay in a separate auxiliary sheet?
3. **Sample-splitting rule (`BARSTAR`, [`walkthrough_ets1.md`](../walkthrough_ets1.md)).** Confirm forcing separate sample cards whenever solvent isotope ratio (`% H2O` vs `% D2O`), `pH/pD`, temperature, or ligand stoichiometry changes inside one paper.
4. **Sheet layout (`16392`).** Should per-residue `R1/R2/NOE/S2` lists sit in their own sheet separated from fitted `kex / pB / Δω` exchange parameters?
