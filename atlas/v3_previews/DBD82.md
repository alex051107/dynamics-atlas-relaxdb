# Glucocorticoid receptor (`DBD82`): domain and method boundaries

**Protein.** Glucocorticoid receptor (`UniProt P06536`, rat GR full length; entry name `DBD82`, DNA-binding domain).  
**Workbook coverage.** `23` papers read (`6` with numeric rows, `17` zero-row papers with exclusions), **`19` raw rows**, **`24` state rows (`19` distinct PDB IDs)**, **`20` residue sets**.  
**RelaxDB deposit card.** `298.5 K` (placeholder), `500 MHz`, pH blank (`234 no, 2 unclear, 1 yes` across sample comparisons).

---

## 1. Why `DBD82` is our highest-uncertainty boundary case

Across `23` papers matching `DBD82`, only **two NMR relaxation studies** probe conformational exchange directly, and they measure **different domains in different species**: the **target rat DNA-binding domain (`DBD`)** versus the **human ligand-binding domain (`LBD`)**. Both sit inside one RelaxDB entry (`DBD82`). Meanwhile, four non-NMR papers add atomistic MD cluster overlaps, live-cell FCS diffusion times, EMSA DNA off-rates, and cell-FRET monomer fractions.

| Layer and domain | Method and construct | What was actually measured (`19` raw rows split by layer) | Source DOI |
|---|---|---|---|
| **Layer A. Target rat GR `DBD` NMR ZZ-exchange** | `15N` ZZ-exchange (`35 °C`, `pH 6.7`, `800 MHz`), WT rat `DBD (440–525)` on `GBS` dsDNA | **`Gly470` conformational exchange `kex = 4.36 s−1` and `3.10 s−1`** (two orders of magnitude faster than DNA dissociation `0.03 s−1` in SI). `2` core rows. | [`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595) |
| **Layer B. Human GR `LBD` NMR CPMG dispersion** | `13C`/`15N` CPMG (`298 K`, `pH 7.5`, `14.1 / 18.8 / 20.0 T`), `GRF602S` and `GRwt` LBD + TIF2 + dex/cortisol/pred/dibC | Global minor state **`kex = 1147 ± 82 s−1`**, **`pm = 19 ± 7%`**, `15N Δω = 0.5 to 1.2 ppm`; **`M752` `pm/pM` allosteric coupling ratio `0.1` (`dibC/cortisol`) vs `0.2` (`dex/pred`)**. Mapped onto `4UDC`. Three rows are tagged `same_protein_other_construct` (`GRF602S`) while two `M752` `GRwt` rows are tagged `target`, even though they measure human `LBD` rather than rat `DBD`. | [`10.1126/sciadv.abb5277`](https://doi.org/10.1126/sciadv.abb5277) |
| **Layer C. Atomistic MD conformational clustering (`DBD`)** | Amber16 `2 × 1.0 μs` MD (`300 K`), `DBD (421–490)` apo and DNA-bound | Lever-arm (`450–456`) cluster overlap of **`~40%`** shared between `GBS1` and `GBS2` monomers; **`at least 10%`** across `3` clusters shared between apo molecule C (`6CFN`) and low-affinity `IR-GBS2` (`4HN5`). `2` rows (`MD`). | [`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9) |
| **Layer D. Non-NMR cellular and biochemical kinetics (downgraded to `minor`)** | Live-cell spFCS/tfCCC (`10.1016/j.bbagen.2025.130809`), EMSA DNA-off kinetics (`pone.0013279`), COS-1 cell FRET (`pone.0064831`) | Live-cell FCS (`25 °C`) cytoplasmic `τD = 1.8 ± 0.6 ms` (`mStayGold-GR`), `1.0 ± 0.3 ms` (`eGFP-GR`), Dex nuclear transport `10–20 s`. EMSA (`RT`, `pH 8`, BHK21 homolog) `t1/2 = 0.56 ± 0.05 min` (`Dex`) to `2.33 ± 0.56 min` (`RU486`), measuring **DNA unbinding kinetics rather than internal exchange**. Cell FRET (`37 °C`) pre-Dex monomer fraction `"roughly two thirds"` dropping to `"around one third"`. | [`10.1016/j.bbagen.2025.130809`](https://doi.org/10.1016/j.bbagen.2025.130809), [`10.1371/journal.pone.0013279`](https://doi.org/10.1371/journal.pone.0013279), [`10.1371/journal.pone.0064831`](https://doi.org/10.1371/journal.pone.0064831) |

---

## 2. Structural states mix `DBD` and `LBD` in `States`

The `24` state rows (`19` distinct PDB IDs) under `DBD82` similarly span both domains:
- **DBD states (`apo` and DNA-bound).** `6CFN` (DNA-free GR DBD crystal), `1GDC` / `1RGD` / `2GDA` (apo GR DBD NMR ensembles), `3G99` / `3G6U` / `3G9J` / `3G9M` / `3FYL` / `4HN5` / `5VA7` / `5VA0` (DNA-bound DBD dimers).
- **LBD states (different domain).** `1M2Z` (`GR:DEX:TIF2` active helix 12), `4UDC` (`DEX-TIF2`), `4P6X` (cortisol-bound), `5NFP`, `1NHZ` / `1H52` / `3H52` (antagonist-bound or partially unfolded helix 12).

---

## 3. What blind cross-model verification exposed here

On `DBD82`, blind cross-family checking (`Gemini` vs `Claude Sonnet 5.5`) agreed **`100%` on experimental NMR vs zero-NMR classification**, but disagreed on all **4 non-NMR papers** (`bbagen.2025.130809`, `s41598-018-31812-9`, `pone.0013279`, `pone.0064831`) because our prompt lacked an explicit rule separating intramolecular conformational dynamics from live-cell FCS diffusion, EMSA DNA off-rates, and cellular dimer stoichiometry. Adjudication downgraded those `10` non-NMR kinetic and FRET rows from `core` to `minor`, **which still leaves an inconsistency against earlier batches that excluded similar papers with `0` rows**.

## 4. Two questions for Gina

1. **Domain vs full-length identity.** Should domain-named entries (`DBD82`, `CHEAYBD`) restrict `target` to that **domain**, tagging papers on another domain (`GR LBD` in `sciadv.abb5277`) separately, or should the Atlas index strictly by canonical **UniProt (`P06536`)** with a required `domain` column?
2. **Non-NMR kinetic rows.** Should translational diffusion (`FCS ms`), intermolecular DNA dissociation (`EMSA t1/2`), cell FRET stoichiometry, and MD clusters stay out of `Measurements` so the primary table contains only intramolecular conformational exchange and spin relaxation?
