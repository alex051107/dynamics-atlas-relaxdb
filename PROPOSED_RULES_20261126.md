# Proposed Boundary Rules for Expert Sign-Off (26 November 2026)

> **Status: PROPOSED (awaiting NMR expert sign-off).** None of these rules has been signed off by Gina yet. Until she rules, our extraction contract runs under strict-abstain defaults (`STATUS: PROPOSED 2026-11-26, default strict-abstain` in [`atlas_pipeline/ACTIVE_EXTRACTION_PROMPT.md`](atlas_pipeline/ACTIVE_EXTRACTION_PROMPT.md)). If no ruling arrives within one week after Thanksgiving, Batch 1 runs under strict-abstain defaults and stays marked `abstain` (not signed off) until she reviews.

No need to re-read the 16-tab workbook. Below are three concrete pilot cases with verbatim paper quotes and a proposed default rule for each. Reply one line per case with **`keep`**, **`re-scope`**, or **`insufficient`**.

---

## Case 1. Ligand-state condition isolation (`AQADK`, *Nature* 2007)

**Observed paper evidence ([`doi:10.1038/nature06410`](https://doi.org/10.1038/nature06410)).** The same paper reports unbound (`apo`) CPMG rates at `10 °C` and ligand-bound (`Mg2+.Ap5A`) CPMG rates, closed-state population, and per-residue chemical-shift differences at `20 °C`.

> Apo quote: `"most of the exchanging residues can be fit with a single exchange rate of 950 6 150 s21 (mean 6 standard deviation (s.d.))"` (PDF Symbol font renders `±` as `6` and `s^-1` as `s21`).

> Bound quote: `"reveal conformational fluctuations with a rate of 300 6 150 s21 (mean 6 s.d.)"` and `"the calculated relative populations are highly skewed towards the closed state (95 6 2%)"`.

Comparing the `46` bound per-residue rows directly against `50` unbound RelaxDB exchange-positive labels yields only `17 / 50` overlap because the ligand state differs.

**Proposed rule (P1).** Keep ligand-bound (`holo`) observations strictly separate and non-comparable (`abstain`) against unbound (`apo`) RelaxDB labels. Never grade bound rows as agreeing or disagreeing with unbound labels.

**Your ruling:** `keep` / `re-scope` / `insufficient`

---

## Case 2. Oligomerization fraction vs conformational state population (`Plexin-B1`, *J. Phys. Chem. B* 2012)

**Observed paper evidence ([`doi:10.1021/jp310142f`](https://doi.org/10.1021/jp310142f)).** The same study reports a monomer-dimer equilibrium fraction alongside a residue-specific conformational exchange term.

> Dimer quote: `"Since approximately 90% of the protein is in its dimeric state"`.

> Exchange quote: `"A conformational exchange contribution (to R2), Rex, of 7.0 s−1 was required for residue T83"`.

Earlier automated passes placed `90%` in the conformational population column while passing verbatim quote checks.

**Proposed rule (P2).** Route dimeric and oligomeric fractions (`~90%` dimeric state) and intermolecular binding off-rates into `oligomer_or_association`. Never allow them in conformational `pB` or `population`. Keep true intramolecular exchange (`T83 Rex = 7.0 s^-1`) in `conformational_exchange`.

**Your ruling:** `keep` / `re-scope` / `insufficient`

---

## Case 3. Experimental cryptic or transient pockets vs non-pocket broadening (`TEM-1 beta-lactamase` vs `BRD4`)

**Observed paper evidence.** Two open studies illustrate the boundary between an experimentally measured transient pocket and ligand-driven broadening inside a binding pocket.

- **TEM-1 beta-lactamase ([`doi:10.1073/pnas.2106473118`](https://doi.org/10.1073/pnas.2106473118)).** CEST NMR detects a minor excited state linked to Omega-loop pocket opening across `L169, N170, G236, E240, G242, S243` (construct numbering offset `+25` relative to RelaxDB).
  > `"The population of the excited state was determined to be 1.05 ± 0.03% (kex = 98 ± 6 s−1)"`
- **BRD4 bromodomain ([`doi:10.1021/acs.jmedchem.4c01128`](https://doi.org/10.1021/acs.jmedchem.4c01128)).** Methyl line broadening near the binding pocket reflects ligand mobility rather than intrinsic protein pocket opening.
  > `"This suggests that the broadening experienced by Ile146 and Leu94 is not due to the global dynamics of the protein but rather the residual mobility of the ligands"`

**Proposed rule (P3).** Record only direct experimental exchange or excited-state measurements of pocket opening (such as TEM-1 Omega-loop CEST) with `evidence_level = experimental` in `qualitative_observations`. Keep author pocket interpretations, MD predictions, and ligand-mobility broadening (such as BRD4 `Ile146` and `Leu94`) in `author_interpretation` or `simulation_or_prediction`, separate from experimental pocket counts.

**Your ruling:** `keep` / `re-scope` / `insufficient`
