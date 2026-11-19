# Thioredoxin 1 (`TRX`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P0AA29` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Release 0.1 expert-reviewed page (`possible`)](../proteins/TRX.md)

## Release 0.1 expert-reviewed synthesis (`21 Oct 2026`)

- **Alternate APO state call:** `possible` (strict two-peak reading: `cannot tell for NMR: the 1993 source states no exchange regime, prints no kex, population or Δω and reports no second peak set for either redox form; exchange is single-field model-free Rex above 1.5 Hz (reduced: G33, I38, I45, R73, G74, I75, W31 indole; oxidized: W31 indole, I45), which the authors call microsecond-millisecond mobility (TRX-J15, J51). The oxidized-form active-site millisecond motion of 1996 is a transient conformation in an abstract (TRX-J17). The 1989 urea-gradient abstract states slow (minute-scale) interconversion of cis and trans P76 forms in folded reduced thioredoxin with less than a few percent trans, but it is electrophoresis read from an abstract, not an NMR peak count, and the 1993 authors exclude P76 isomerisation as the source of the 73-75 broadening (TRX-J29).`)
- **Reference state:** Wild-type thioredoxin-1 as deposited (108-residue mature sequence), free, no ligand. Redox form is a sample state: the RelaxDB card gives no BMRB id, no redox state and links only the oxidized human-E. coli chimera 1M7T, so the deposited form is unknown; the call is given for each form. The key solution study (Stone et al. 1993, doi:10.1021/bi00053a007, now full text) measured both forms at 308 K on a 500 MHz spectrometer (single field, 1.0 ms CPMG spacing); its main text does not state protein concentration, buffer, pH or solvent isotope fraction (TRX-J1, J2, J15, J16, J51 marked is_wt_apo).
- **Exchange rate (`kex`):** not reported for either redox form; Rex above 1.5 Hz (values figure-only, Figure 3E/F; W31 indole 4.0 ± 0.2 Hz oxidized and 2.8 ± 0.1 Hz reduced, W28 0.44 ± 0.02 Hz oxidized, Table I) at the sites listed, from single-field model-free fitting with a 1.0 ms CPMG spacing (TRX-J15, J51); the 1996 oxidized active-site millisecond motion is stated without values (TRX-J17, abstract)
- **Minor-state population (`pB`):** not reported for either redox form (TRX-J15, J51, J17)
- **Exchanging region:** Reduced: W31 indole, G33, I38, I45, R73, G74, I75 (Rex > 1.5 Hz; TRX-J15). Oxidized: W31 indole, I45 (TRX-J51); R73-I75 quiet (TRX-J16); G33 not measurable (TRX-J52). Oxidized 1996: nuclei around the active-site disulfide C32-C35, not enumerated in the abstract (TRX-J17). Solid-state reassembly (other construct, 238 K): G21, P40, T54, R73 lost; A19, D20, G21, R73 survive the T2' filter (TRX-J12).
- **Structure comparison:** [{"pdb": "2TRX", "what": "Oxidized wild-type crystal (1.68 Å) with ten unnamed residues in two alternative conformations and differences between the two independent molecules that may reflect crystal contacts; residues 29-37 form a surface protrusion. A crystal alternative, not a solved minor state.", "evidence_row": "TRX-TRX_20261020104151-r1"}, {"pdb": "5HR0", "what": "E101G mutant crystal: chain B refines as two complete backbone conformers (Ba/Bb, 50% each) over D10-V25, T77-V91 and S95-L107, read by the authors as members of the native-like ensemble. Mutant, Cu(II)/ethanol crystal, no solution population; not tied to the 73-75 or active-site exchange.", "evidence_row": "TRX-r36"}, {"pdb": "1M7T", "what": "Oxidized human-E. coli chimera linked by the RelaxDB card; its 15N relaxation gives S2 0.88 with mobile loops 72-74 and 92-94 (chimera numbering). A homolog construct, not the entry sequence and not a minor state.", "evidence_row": "TRX-r45"}]
- **Caveats:** Call raised from unknown to possible on 2026-10-20 after the RelaxDB source paper (doi:10.1021/bi00053a007, Stone et al. 1993) was read in full: exchange is detected in the reference state in both redox forms as single-field model-free Rex above 1.5 Hz, and under the single-field Rex rule decided that night (ledger/redraft_notes.json, _RULE_single_field_rex) this counts as exchange detected without a population. Fixed caveat: single-field Rex can also come from anisotropic tumbling; a dispersion experiment would confirm. The two forms give different site lists (reduced: G33, I38, I45, R73-I75, W31; oxidized: W31, I45 only), and the RelaxDB card does not say which form was deposited, so the call is 'possible' for each form and the atlas needs the deposited form. The 1993 main text omits protein concentration, buffer, pH and solvent, and its Rex values are figure-only except the W31 indole; the Monte Carlo uncertainties may be underestimated. LeMaster 1996 (oxidized active-site ms motion) remains abstract-only. The solid-state evidence is from a cleaved reassembly in a PEG precipitate at 238 K, the crystal alternatives come from a Cu(II)-containing wild-type crystal and an E101G mutant crystal, and the MD transitions are simulation only. No dispersion experiment was found, and the structured dispersion searches were restricted to Salmonella typhi terms. The abstract-only rows TRX-TRX_20261020101601-r1, r2, r3 are superseded and no longer cited. Built from cases V6_r6_TRX_20261020101601, V6_r6_TRX_20261020104151, V6_r6_TRX_20261020105420, S6_r6_TRX_20261020155442, S6_r6_TRX_20261020160402 and S6_r6_TRX_20261020212514.
- **Full Release 0.1 narrative & judgments:** [`atlas/proteins/TRX.md`](../proteins/TRX.md) (22 key curated rows)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*38 rows total (38 spin-relaxation/model-free; 0 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi00053a007`](https://doi.org/10.1021/bi00053a007) | `NMR_spin_relaxation_and_MF` | `target` | apo, oxidized | S2 (6), T1 (2), T2 (2), NOE (2), other (2), tau_e (2) | T1 = 0.51 s (W28 side-chain NH) |
| [`10.1021/bi00053a007`](https://doi.org/10.1021/bi00053a007) | `NMR_spin_relaxation_and_MF` | `target` | apo, reduced | S2 (5), T1 (2), T2 (2), NOE (2), other (2), tau_e (2) | T1 = 0.501 s (W28 side-chain NH) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **picosecond-nanosecond mobility (S2 statistically lower than average in both forms)** ([`10.1021/bi00053a007`](https://doi.org/10.1021/bi00053a007), sample `S1`): K3, I4, T14, D20, G21, A22, R73, G74, A93, L94, and A108
- **microsecond-millisecond exchange (Rex significantly above 1.5 Hz), oxidized and reduced** ([`10.1021/bi00053a007`](https://doi.org/10.1021/bi00053a007), sample `S2`): W31 side chain, I45 backbone (both forms); G33, I38, R73, G74, I75 (reduced form)

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (1):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi00053a007`](https://doi.org/10.1021/bi00053a007) | 38 | 0 | 2 | 2 | Printed numbers are Table I (Trp indole NH and backbone NH of W28 and W31, oxidized and reduced, 8 parameters) |

**Explicit figure-only, SI-only, or access gaps (2):**

- per-residue backbone T1, T2, NOE, T1/T2, S2, te, Rex for oxidized and reduced thioredoxin ([`10.1021/bi00053a007`](https://doi.org/10.1021/bi00053a007)): figure only (Figures 2 and 3); the two supplementary tables with these values are listed as available supplementary material and are not in the text
- Rex values of R73, G74, I75 (reduced) and G33, I38, I45 ([`10.1021/bi00053a007`](https://doi.org/10.1021/bi00053a007)): figure only (Figure 3E,F); the text names the residues but prints no value

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
