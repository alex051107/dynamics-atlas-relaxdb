# Chemotaxis protein CheA (`CHEA` + `CHEAYBD`): duplicate-entry conflict

**Protein.** *E. coli* Chemotaxis protein CheA (`UniProt P07363`).  
**RelaxDB twin entries.** `CHEA` (`23` papers read, `1,097` rows) **and** `CHEAYBD` (`18` papers read, `75` rows), **`41` records total**.  
**RelaxDB deposit cards.** Both list `298.5 K` (placeholder), `500 MHz`, pH blank (`42 no, 13 unclear` on `CHEA`; `51 no, 4 unclear` on `CHEAYBD`).

---

## 1. Why comparing `CHEA` and `CHEAYBD` exposes a structural pipeline flaw

RelaxDB filed two separate entries (`CHEA` and `CHEAYBD`, the CheY-binding P2 region) under the **same UniProt accession `P07363`**. Because our November sweep processed each `(entry, DOI)` pair separately without canonicalizing by UniProt first, **the same protein and the exact same papers produced conflicting row counts, conflicting species tags, and omitted backbone NMR data**.

### Concrete divergences across the two entries (`7` overlapping valued DOIs totaling `43 CHEA` vs `71 CHEAYBD` rows)

| DOI | `CHEA` extraction | `CHEAYBD` extraction | What actually diverged |
|---|---|---|---|
| [`10.1021/bi951960e`](https://doi.org/10.1021/bi951960e) *(Zhou et al., CheA `1–233` `15N` relaxation)* | **`1,052` rows** (`T1, T2, NOE, τm, S², τe` plus flexible linker `rsets`, `500 MHz, 30 °C, pH 6.3`) | **Absent (`0` records)** | Foundational `15N` NMR relaxation data on **CheA's P1 + P2 (`CheY-binding`) linker** sits only under `CHEA`, missing completely from `CHEAYBD`. |
| [`10.1073/pnas.2218467120`](https://doi.org/10.1073/pnas.2218467120) *(HDX-MS signaling complexes)* | **`11` rows** (`7` core; reader excluded Table 1's `30` domain rapid-uptake % rows as single-timepoint fractions) | **`37` rows** (`21` core; reader kept Table 1 rapid-uptake fractions as `other`) | **Opposite inclusion decisions on identical text** produced a `3.4×` row-count swing (`11` vs `37`). |
| [`10.1007/s00723-018-1070-6`](https://doi.org/10.1007/s00723-018-1070-6) *(ESR DEER nucleotide spin-label)* | `2` rows labeled **`homolog`** (*T. maritima* CheA `E387C-SL`: `45 Å` free vs `~35 Å` ADP-β-S-SL) | `2` rows labeled **`same_protein_other_construct`** | Identical *T. maritima* protein received **different `species_relation` tags**. |
| [`10.1038/s41598-017-16755-x`](https://doi.org/10.1038/s41598-017-16755-x) *(CheA–CheY TRACT and cross-saturation)* | **`5` rows**, `2` states (`2LP4`, `3KYJ`): TRACT `τm` (`~30 ns` P1, `~15 ns` P2), `kex > 1,000 s−1` (`I5`), `>80%` P2 bound, `<10%` P1–P4 | **`9` rows**, `1` state (`2LP4`) | Same paper yielded `5` vs `9` rows and `2` vs `1` state PDBs; `I5` labeled `target` in `CHEA` vs `same_protein_other_construct` in `CHEAYBD`. |
| [`10.1126/scisignal.abc1328`](https://doi.org/10.1126/scisignal.abc1328) *(*T. maritima* DEER at `60 K`)* | `15` `[homolog]` distance rows, `3` states (`1TQG`, `4XIV`, `3UR1`) | `15` `[homolog]` rows, `3` states *(manually synchronized on `2026-11-17`)* | Required manual copying between twins after initially disagreeing on `weight` across `3` rows. |
| [`10.1021/bi4012379`](https://doi.org/10.1021/bi4012379) *(*T. maritima* CPMG, `50 °C`)* | `kex ~1250 ± 100 s−1` (`[homolog]`, `500/800 MHz`) | `kex ~1250 ± 100 s−1` (`[homolog]`, `500/800 MHz`) | Consistent rate, slightly different residue notation (`517, 518` explicit vs `15N` tag). |
| [`10.7554/elife.08419`](https://doi.org/10.7554/elife.08419) *(MD array clusters)* | `0` rows (`1` residue set instead) | **`4` `md_simulation` population rows** (`80%, 10%, 10%, 2%` at `350 K`) | Identical MD study yielded `0` rows under `CHEA` vs `4` rows under `CHEAYBD`. |
| [`10.1016/j.bpj.2026.05.001`](https://doi.org/10.1016/j.bpj.2026.05.001) *(CheA-P1 CSP/intensity)* | `2` rows (`78%` off / `90%` on P1 bound to P4, `22 °C`, `600 MHz`) | `2` rows (`78%` / `90%`) | Consistent (`same_protein_other_construct`). |

Naively summing `CHEA` plus `CHEAYBD` across the `7` overlapping papers duplicates `41` measurement pairs on identical DOIs.

---

## 2. True picture for *E. coli* CheA (`P07363`) once deduplicated

When merged by protein identity and separated cleanly from thermophilic *T. maritima* homologs:
1. **Flexible P1–P2 linker (`10.1021/bi951960e`, `30 °C, 500 MHz, pH 6.3`).** Full per-residue `T1`, `T2`, `NOE`, `τm`, `S²`, `τe` table (`1,052` rows) quantifying independent tumbling (`τ1/τ2`) of domains P1 and P2 joined by the flexible linker.
2. **Inter-domain P1/P2/P4 kinetics (`10.1038/s41598-017-16755-x`, `10.1016/j.bpj.2026.05.001`).** `τm ~30 ns` (P1) and `~15 ns` (P2) in full-length CheA (`303 K`); P1–P4 contact `<10%` in free CheA vs `78%` (`CF4E` kinase-off) and `90%` (`CF4Q` kinase-on) inside signaling complexes; P1–CheY exchange **`kex > 1,000 s−1`**.
3. **Homolog separation (*T. maritima*).** `10.1021/bi4012379` (`kex ~1250 ± 100 s−1` by CPMG at `50 °C`) and `10.1126/scisignal.abc1328` (cryo DEER at `60 K`) measure thermophilic *T. maritima* CheA, not mesophilic *E. coli* `P07363`.

---

## 3. Question for Gina

Four other UniProt pairs (`BLAC_CPMG`/`27888`, `AQADK`/`AQADK_CPMG`, `ARGKIN_CPMG`/`ARGKIN`, `HTPDZ_CPMG`/`HTPDZ`) and two untouched pairs (`CIN1D1`/`CIN1D2`, `RNASE`/`RNASE_CPMG`) represent twin entries on the same protein in RelaxDB. In our next pass, confirm extracting and synthesizing once per **canonical UniProt accession** (keeping domain tags like `P2/YBD` vs full-length `CheA`) so identical papers never generate conflicting records.
