# TEM-1 (`16392`) and Barstar (`BARSTAR`): two quality traps

These two entries spotlight **the two sharpest failure modes in the raw November workbook**: massive per-residue SI relaxation tables burying rare exchange parameters, and sample-condition conflation that passes deterministic quote checks without error.

---

## Part A. TEM-1 β-lactamase (`16392`, `UniProt P62594`): bulk relaxation drowning rare exchange rates

- **Workbook coverage.** `18` papers read (`4` with numeric rows), **`1,912` raw rows**, **`22` state rows (`19` distinct PDB IDs)**, **`14` residue sets**, deposited card `303.15 K, 500/600/800 MHz, pH 6.6`.
- **Why raw row counts deceive.** `98.3%` of all rows (`1,879 / 1,912`) come from one multi-field model-free SI table ([`10.1021/bi060414q`](https://doi.org/10.1021/bi060414q), `30 °C, pH 6.6, 500/600/800 MHz`, `τm = 12.41 ± 0.01 ns`, per-residue `R1/R2/NOE/S²/τe/Rex` using construct numbering starting at `26` rather than Ambler numbering).

### Where the mechanistic pocket-opening exchange actually sits (`17` rows across `2` papers)

| Process and construct | Key rates, populations, and states | Condition | Source DOI |
|---|---|---|---|
| **WT Ω-loop cryptic-pocket opening (CEST plus variants)** | WT CEST excited state **`population = 1.05 ± 0.03%`**, **`kex = 98 ± 6 s−1`** (`L169, N170, G236, E240, G242, S243`, closed reference **`1XPB`**). Variant thiol-labeling open populations: `4 ± 1%` (`E240D`, EXX regime) and `0.19 ± 0.01%` (`E240D/R241P`, EX2 regime). | Apo, temperature/pH/field not printed in text excerpt | [`10.1073/pnas.2106473118`](https://doi.org/10.1073/pnas.2106473118) |
| **`G238S` evolutionary CPMG dispersion and structural states** | `G238S` (`30 °C`, `pH 6.4`, `600/850 MHz`): `τm = 12.7 ns`; active-site **`kex < 500 s−1`** vs scaffold **`kex > 2500 s−1`** (map `500–3000 s−1`); population shifts **`42%`** (`E104K/G238S -> A42G/E104K/G238S`) and **`~40–50%`** (`α2/β3/Ω/SDN/216` walls). Contrasts **`8` PDB conformations**: `1ZG4` (closed `238/Ω`), `4OPR` / `4OP8` (`G238S` open `238-loop`), `1HTZ` (`TEM-52`), `3P98` (`TEM-72`), `1JWV` (`G238A`), `1PZO` (open allosteric site), `4IBX`. | Mutant `same_protein_other_construct`; per-residue dispersion table (`Table S2`) absent from main XML (`Gaps`) | [`10.1038/s41467-026-68620-z`](https://doi.org/10.1038/s41467-026-68620-z) |
| **Chimera `cTEM-17m` spin relaxation** | `16` rows (`τm = 12.2 ns`, Table 4/5 averages at `31.5 °C`, `pH 6.7`, `500/600 MHz`), plus `1` unmerged second-reader candidate (`S² ≥ 0.9` in active site). | Engineered chimera (`17` substitutions); WT values cited only | [`10.1371/journal.pone.0052283`](https://doi.org/10.1371/journal.pone.0052283) |

**What this shows for `16392`.** Numbering shifts across papers (construct numbering starting at `26` in `bi060414q` vs Ambler numbering elsewhere), so aligning residue coordinates onto UniProt `P62594` and splitting bulk `R1/R2/S2` arrays from exchange kinetics is essential before protein summaries become usable.

---

## Part B. Barstar (`BARSTAR`, `UniProt P11540`): condition-binding and target-mismatch traps

- **Workbook coverage.** `8` papers read (`2` valued, `6` zero-row), **`7` rows** (`0` native solution-NMR relaxation or exchange rates), `3` PDB states (`1AB7`, `1AY7`, `1A19`), `3` residue sets, `16` sample rows (`11 no`, `5 unclear` vs deposited card `298.5 K` placeholder, `600 MHz`, pH blank).

### What the `7` rows actually measure
1. **Cold-denatured state proline cis/trans populations (`4` core rows).** `P27 cis 4.4% / trans 95.6%`, `P48 cis 11% / trans 89%` measured by `CaCON` NMR **at `270 K` in the cold-denatured state**, not native folded Barstar ([`10.1002/anie.202006945`](https://doi.org/10.1002/anie.202006945)).
2. **FPOP mass-spectrometry folding intermediate (`3` minor rows).** `L20 >0.8`, `I5 0.57`, `F74 0.29` dimensionless degree of folding at **`2 ms` after `0 °C` -> RT laser T-jump** in `1.2 M GdnCl` ([`10.1021/ja307606f`](https://doi.org/10.1021/ja307606f)).

### Two real pipeline failure modes caught inside Barstar's zero-row papers

1. **Gap 1. Condition misbinding passes all substring quote checks ([`10.1021/jacs.0c00807`](https://doi.org/10.1021/jacs.0c00807), `PMC7304870`).**
   - *What the paper actually did.* Hyperpolarized-water (`HyperW`) `1H–15N` HMQC injected H2O/glycerol into `D2O`-reconstituted Barstar (`C40A/C82A`, `50 mM` sodium phosphate, **`pD 7`**, post-injection **`~1.8% H2O`**). Then that post-dissolution sample was lyophilized to dryness and **reconstituted in `90% H2O` (`pH 7`)** for `CLEANEX-PM` amide–water exchange (`kHN` plotted in Fig. 5B only, yielding `0` numeric rows plus `2` residue sets `I13/helix-3/helix-4` and `barnase-binding flexible loop`).
   - *What our extractor recorded.* One blended sample `S1` reading `pH = "pD 7 (HyperW, D2O); pH 7 (CLEANEX, ~1.8% H2O)"`, **wrongly binding `~1.8% H2O` onto `CLEANEX` (`90% H2O`)**. Automated checks passed with `0` errors because each phrase appeared somewhere in the source text. This concrete case defines **Gap 1 (`NoUncheckedConditionBinding`)** in [`methods/bugs_and_fixes.md`](../../methods/bugs_and_fixes.md).
2. **Upstream DOI false match rejected at full-text read (`10.1371/journal.pone.0023050`).** Matched to Barstar during upstream candidate triage, though the full text studies purely *E. coli* thioredoxin (properly rejected with `0` rows once read).

## Questions for Gina

1. For `16392`-style proteins where `1,000+` per-residue SI `R1/R2/S²` values coexist with `4–15` CPMG/CEST pocket parameters, confirm placing those two data types into **separate linked tables (`PerResidueRelaxation` vs `ExchangeProcesses`)**.
2. On **`BARSTAR` (`10.1021/jacs.0c00807`)**, confirm whether requiring distinct `HyperW (~1.8% H2O, pD 7)` and `CLEANEX (90% H2O, pH 7)` sample rows reflects your standard for NMR sample provenance.
