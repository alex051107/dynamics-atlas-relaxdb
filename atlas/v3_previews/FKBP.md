# FKBP12 (`FKBP`): multi-timescale NMR and crystal/MD boundary

**Protein.** Peptidyl-prolyl cis-trans isomerase FKBP1A (`UniProt P62942`).  
**Workbook coverage.** `30` papers read (`6` with printed dynamics rows, `24` zero-row papers with exclusions), `391` raw rows (`373` NMR and HX rows, `15` `molecular_dynamics` rows, and `3` `x_ray_crystallography` occupancy rows; `195 core` and `196 minor`), `50` state rows (`34` distinct PDB IDs), and `37` residue sets.  
**RelaxDB deposit card.** `298.5 K` (placeholder), `500 MHz`, pH blank. Matched `0/323` paper sample cards (`302 no`, `21 unclear`).

---

## 1. Biological summary across timescales

Human FKBP12 is rigid across most of the backbone on the ps–ns timescale, yet shows two localized slower equilibria around the active site (`Trp59`) and the `80's` / `β4–β5` loop (`Gly89`).

| Timescale and process | Construct and condition | Key measured numbers (verbatim sources) | Source DOI |
|---|---|---|---|
| **ps–ns backbone relaxation** | Apo WT FKBP12, `303 K`, `pH 7.0`, `500 MHz` | Global `τm = 9.18 ± 0.17 ns` (`9.5 ± 0.5 ns` on `29` core residues); `R1 = 1.65 ± 0.14 s−1`; mean `R2 = 11.97 ± 0.58 s−1` (range `10.90–32.98 s−1`); mean `NOE = 0.82 ± 0.1`; `331` total rows including per-residue Table I `S²`, `τe`, `Rex`, and qualitative HDX classes | [`10.1021/bi00086a004`](https://doi.org/10.1021/bi00086a004) |
| **ns `Trp59` ring flip and μs–ms loop exchange** | WT, `G89A`, `C22V/G89P`, `25 °C` (`298 K`), `pH 6.50`, `600 / 900 MHz` | `Trp59 Nε1` model-free `R1 = 1.50 s−1`, `R2 = 5.56 s−1`, `NOE = 0.634`, `S² = 0.63`, `τe = 1.5 ns`, `τm = 5.8 ns` (ordered backbone). NOE admixture fits **80% / 20%** (`2PPN` canonical vs perpendicular `G89P`-like conformer; `82/18%` and `79/21%` under alternative distance models; simple jump `S² = 0.53`). Crystal `4N19` (`1.20 Å`, `100 K`) resolves dual `Trp59` occupancies (`0.29 / 0.71`) and `Glu60` minor (`0.34`). | [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |
| **Slow cis–trans `Gly89` isomerization (`s` timescale)** | WT and `C22V`, `G89A`; `25 °C` (HSQC) and `43 / 48 °C` (`zz-exchange`), `600/800/900 MHz` | WT minor population **`pB = 12%`** across `31` doubled backbone resonances (`τm = 5.8 ns` at `25 °C`; `R2` at `600/800 MHz`); **`zz-exchange` lifetime `3.0 s` (`43 °C`) and `1.8 s` (`48 °C`)**. `G89A` shifts the cis-Ala89 minor-like state to **`67%`** (`6.7 kJ/mol` stability change). Exchange line-broadening in residues `39, 42, 44` drops `3-fold` on mutation. | [`10.1042/bj20130276`](https://doi.org/10.1042/bj20130276), [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |
| **Hydrogen exchange (`β4–β5` loop allostery)** | WT, `G89A`, `I76C/Y80V`, `H87V`, `25 °C`, `600 MHz` CLEANEX-PM and TROSY H/D | Transient-state HX fit **`pT(G89A) = 3.7%`** across `β4–β5` (`80, 81, 83, 90, 94, 95`; central `83/90/94 = 2.0%`, stem `80/81/95 = 6.9%`); `7.4 ± 0.1`-fold ratio over WT; `Phe36` `log kOH− = 5.09` (`I76C/Y80V`) vs `4.32` (`H87V`); slowest core cluster (`23–25, 64–76, 98–104`) time constant `>9 days` at `pH 6.82`. | [`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990) |
| **NOESY plus MD indole allostery (`V101I`)** | `V101I` vs WT at `25 °C`, `pH 6.50`, `600 MHz` plus `1.14 μs` (`298 K`) CHARMM27 MD | NMR NOESY shows flipped `Trp59` population **reduced `10-fold`** in `V101I`. MD predicts canonical `Trp59` drops from **`59.6%` (`V101I`) to `7.9%` (WT)** (`17-fold` / `7.0 kJ/mol` shift; `57` vs `63` `χ1` transitions, `20 ns` WT residence time vs `1.5 ns` `Glu60`, coupling ratio `63` / `10.3 kJ/mol`). | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| **Ubiquitylation fold destabilization** | Free vs ubiquitylated FKBP12 NMR relaxation | Mean spectral density **`J(0)` increases from `4.2 ± 1.3 ns` (free) to `11.4 ± 5.2 ns` (ubiquitylated)**. | [`10.1038/srep39453`](https://doi.org/10.1038/srep39453) |

---

## 2. Structural states named in literature (`States`)

Key PDB entries tied to conformations in the extracted texts include `2PPN` (`E60A` / canonical WT indole reference conformation, `0.92 Å` X-ray), `2PPO` (`WT`), `2PPP` (`E60Q`), `4N19` (`C22V/G89P` crystal resolving dual `Trp59` conformers), `1FKB` (FKBP12–rapamycin), `1FAP` (FKBP12/rapamycin/FRB ternary complex), and `5HUA` (FKBP1A structure in later studies).

---

## 3. Audit findings on FKBP12

1. **High experimental recall.** Blind cross-family checks matched **`10/10` core HX numbers** in `10.1016/j.bbapap.2023.140990` and **`13/13` newly measured NMR and crystal values** in `10.1042/bj20131429`. The reader also properly excluded the cited `12%` WT baseline in `bj20131429` because that primary experiment is already extracted from [`10.1042/bj20130276`](https://doi.org/10.1042/bj20130276).
2. **Mixed-method counts without domain filtering.** Out of `391` raw rows, `15` are CHARMM27 MD values (`bpc.2014.06.004`), `3` are `100 K` cryo-crystal occupancies (`bj20131429`), and `4` ratio or fold-change entries (`reduced 10-fold`, `17-fold`, etc.) had to be repaired from `population` to `other` / `minor` during adjudication.
3. **Deposit-card mismatch.** RelaxDB lists `298.5 K, 500 MHz` with blank pH, whereas the `500 MHz` Cheng dataset (`bi00086a004`) ran at `303 K, pH 7.0`, and the slow-exchange/NOESY papers (`298 K / 25 °C`) ran at `600/800/900 MHz`.

## 4. Questions for Gina

1. For `FKBP`, should **`Trp59` `100 K` crystal dual-conformer occupancies (`0.29/0.71` in `4N19`)** sit alongside solution NMR populations (`12%` slow state at `25 °C`, `80/20%` NOE fit), or stay strictly in `States`?
2. Should **`MD` simulation percentages (`7.9%` vs `59.6%`)** live in a dedicated computational sheet instead of mixing into `Measurements`?
