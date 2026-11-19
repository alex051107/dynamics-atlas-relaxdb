# Villin-1 D6 domain (`VILD6`)

**Atlas tier:** Tier 3 · Qualitative regions / PDB states / Release 0.1 unknown / twin link / 0-numeric full text  
**UniProt:** `P02640` · **RelaxDB deposited card:** T = `298.0`, field = `750` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`unknown`)](../proteins/VILD6.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `unknown` (strict two-peak reading: `cannot tell: nothing measures the calcium-free isolated domain. In calcium-bound D6-HP the authors attribute the missing P68-D72 and E85 amides to intermediate exchange on the NMR timescale, which would not qualify, and no second peak set is reported (VILD6-J7).`)
- **Reference state:** Calcium-free wild-type isolated V6 (the 107-residue entry sequence); no evidence row measures it. The RelaxDB source paper measured D6-HP (208 residues) in 5 mM calcium at 25 °C, pH 7.0, a different construct and ligand state.
- **Exchange rate (`kex`):** not measured (VILD6-J3); the D6-HP missing peaks carry no rate (VILD6-J7)
- **Minor-state population (`pB`):** not measured (VILD6-J3); 'one quarter of D6 amides' on calcium removal is a count of affected peaks, not a population (VILD6-J8)
- **Exchanging region:** none measured in the reference state. Calcium-bound D6-HP: P68-D72 and E85 missing (intermediate exchange proposed), A60-E62 missing and unexplained, F84 mobile on the ps-ns scale (VILD6-J5, J7); calcium-free D6-HP: first 80 residues affected, no list (VILD6-J8)
- **Structure comparison:** [{"pdb": "2LLF", "what": "Calcium-bound NMR structure of isolated V6 with an extended long helix. A ligand-bound form, not an apo minor state; the gelsolin-like straightening pathway is proposed, not experimentally resolved.", "evidence_row": "VILD6-r26"}]
- **Caveats:** The RelaxDB VILD6 relaxation set appears to come from D6-HP in 5 mM calcium (doi:10.1021/bi700110v, case S6_r6_VILD6_20261020153804, read in full on 2026-10-20), while the entry sequence is the isolated 107-residue D6; if the NMR collaborator sets the reference state to calcium-bound D6 within D6-HP, the call rises to possible on the missing P68-D72 and E85 amides. BMRB 18046 (cross-referenced by 2LLF) deposits no relaxation lists. Villin headpiece rows (VILD6-r1 to r25) are a separate domain and were not used.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/VILD6.md`](../proteins/VILD6.md) (4 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

No quantitative spin-relaxation, HDX, DEER, or FRET rows extracted in `v3` for this entry.

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **structured regions versus disordered linker (relaxation)** ([`10.1021/bi700110v`](https://doi.org/10.1021/bi700110v), sample `S1`): 1-105 and 145-206 structured; 105-145 disordered
- **intermediate structural exchange (weak or unassigned resonances)** ([`10.1021/bi700110v`](https://doi.org/10.1021/bi700110v), sample `S1`): Pro68 to Asp72; Ala60-Gln61-Glu62; Glu85

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi700110v`](https://doi.org/10.1021/bi700110v) | 0 | 0 | 2 | 2 | The paper prints no numeric dynamics values in the text: R1, R2, heteronuclear NOE and S2 are shown only in Fi |

**Explicit figure-only, SI-only, or access gaps (2):**

- Per-residue R1, R2, {1H-15N}-NOE and S2 for 144 residues ([`10.1021/bi700110v`](https://doi.org/10.1021/bi700110v)): figure only (Figure 4); the text prints no values; the note on the title page says values were deposited in BMRB, not in the text
- Phe84 NOE 'well below 0.6' ([`10.1021/bi700110v`](https://doi.org/10.1021/bi700110v)): an upper bound in prose, not a measured value; the value is in Figure 4C

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
