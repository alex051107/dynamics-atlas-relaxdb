# Peptidyl-prolyl cis-trans isomerase FKBP1A (`FKBP`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P62942` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Worked deep walkthrough / review case](../v3_previews/FKBP.md)

> **Audit note:** Review case (Rank 2): NMR exchange + 15 MD rows + 3 cryo-X-ray (100 K) rows

## 1. Experimental conformational exchange (rates, populations, Δω)

*12 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `population` | 3.7 % | six residues of the β4-β5 loop (80, 81, 83, 90, 94, 95) | `HDX_NMR_and_MS` | `same_protein_other_construct` | apo; 25°C; pH not printed; 600 MHz | `no` | [`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990) |
| `population` | 2.0 % | 83, 90, and 94 | `HDX_NMR_and_MS` | `same_protein_other_construct` | apo; 25°C; pH not printed; 600 MHz | `no` | [`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990) |
| `population` | 6.9 % | 80, 81, and 95 | `HDX_NMR_and_MS` | `same_protein_other_construct` | apo; 25°C; pH not printed; 600 MHz | `no` | [`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990) |
| `population` | 12 % | minor slow-exchange state, 31 doubled residues | `NMR_other` | `target` | apo; 25°C; pH 6.5; 600, 800, 900 | `unclear` | [`10.1042/bj20130276`](https://doi.org/10.1042/bj20130276) |
| `population` | ~0.2 % | minor state upper limit, 31 doubled residues | `NMR_other` | `same_protein_other_construct` | apo; 25°C; pH 6.5; 600 | `no` | [`10.1042/bj20130276`](https://doi.org/10.1042/bj20130276) |
| `population` | 67 % | G89A slow-exchange cis-Ala89 conformational state (analogous to W | `NMR_other` | `same_protein_other_construct` | apo; 25°C; pH 6.50; 600 MHz and 900 MHz | `no` | [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |
| `population` | 80 % | Trp59 indole side chain (canonical wild-type PDB 2PPN conformatio | `NMR_spin_relaxation_and_MF` | `target` | apo; not printed; pH 6.50; not printed | `no` | [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |
| `population` | 20 % | Trp59 indole side chain (perpendicular G89P-like conformation) | `NMR_spin_relaxation_and_MF` | `target` | apo; not printed; pH 6.50; not printed | `no` | [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |
| `population` | 82 % | Trp59 indole side chain (canonical wild-type PDB 2PPN conformatio | `NMR_spin_relaxation_and_MF` | `target` | apo; not printed; pH 6.50; not printed | `no` | [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |
| `population` | 18 % | Trp59 indole side chain (perpendicular G89P-like conformation) | `NMR_spin_relaxation_and_MF` | `target` | apo; not printed; pH 6.50; not printed | `no` | [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |
| `population` | 79 % | Trp59 indole side chain (canonical wild-type PDB 2PPN conformatio | `NMR_spin_relaxation_and_MF` | `target` | apo; not printed; pH 6.50; not printed | `no` | [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |
| `population` | 21 % | Trp59 indole side chain (perpendicular G89P-like conformation) | `NMR_spin_relaxation_and_MF` | `target` | apo; not printed; pH 6.50; not printed | `no` | [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*361 rows total (252 spin-relaxation/model-free; 109 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1021/bi00086a004`](https://doi.org/10.1021/bi00086a004) | `NMR_spin_relaxation_and_MF` | `target` | apo (uncomplexed) | S2 (88), Rex (75), tau_e (68), tau_m (3), R2 (2), R1 (1) | tau_m = 9.18 ns (whole protein) |
| [`10.1021/bi00086a004`](https://doi.org/10.1021/bi00086a004) | `HDX_NMR_and_MS` | `target` | apo | other (93) | other = + qualitative class (-) fast, (+) slow, (++) slowest (Q3) |
| [`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990) | `HDX_NMR_and_MS` | `same_protein_other_construct` | apo | other (9) | other = 7.4 ratio (six residues of the β4-β5 loop (80, …) |
| [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) | `NMR_spin_relaxation_and_MF` | `target` | apo | S2 (2), R1 (1), R2 (1), NOE (1), tau_m (1), tau_e (1) | R1 = 1.50 s−1 (Trp59 Nε1) |
| [`10.1042/bj20130276`](https://doi.org/10.1042/bj20130276) | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | apo | other (4) | other = 3.0 s (Trp59 indole HNe1, major-minor excha…) |
| [`10.1042/bj20130276`](https://doi.org/10.1042/bj20130276) | `NMR_spin_relaxation_and_MF` | `target` | apo | R2 (2), tau_m (1) | tau_m = 5.8 ns (global, residues without exchange br…) |
| [`10.1042/bj20130276`](https://doi.org/10.1042/bj20130276) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | apo | other (2) | other = ~35 % (Glu54, Val55, Gly58 decrease of conf…) |
| [`10.1038/srep39453`](https://doi.org/10.1038/srep39453) | `NMR_spin_relaxation_and_MF` | `target` | apo (non-ubiquitylated) | other (1) | other = 4.2 ns (non-ubiquitylated FKBP12 backbone am…) |
| [`10.1038/srep39453`](https://doi.org/10.1038/srep39453) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | covalently ubiquitylated | other (1) | other = 11.4 ns (ubiquitylated FKBP12 backbone amides…) |
| [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) | `NMR_other` | `same_protein_other_construct` | apo | other (1) | other = reduced 10-fold fold change relative to wild type (Trp 59 (det |
| [`10.1042/bj20130276`](https://doi.org/10.1042/bj20130276) | `NMR_other` | `target` | apo | other (1) | other = 14 % (minor/major peak volume ratio, resol…) |
| [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) | `NMR_other` | `same_protein_other_construct` | apo | other (1) | other = 6.7 kJ/mol (G89A slow-exchange conformational eq…) |

## 3. Computational (MD/MSM) and cryo-structure (X-ray / cryo-EM) rows

*18 rows intentionally separated from experimental solution dynamics pending expert scope lock:*

| Method group | Quantity | Value | Residues / group | Paper |
|---|---|---|---|---|
| `MD_and_MSM` | `population` | 7.9 % | Trp 59 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `population` | 59.6 % | Trp 59 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 17-fold fold equilibrium shift vs wild type | Trp 59 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 7.0 kJ/mol | Trp 59 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 57 χ1 rotamer transitions over 1.14 μs | Trp 59 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 63 χ1 rotamer transitions over 1.14 μs | Trp 59 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 20 ns | Trp 59 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 1.5 ns | Glu 60 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 63 dimensionless coupling ratio | Trp 59, Glu 60 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 10.3 kJ/mol | Trp 59, Glu 60 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 3 ps to 5 ps ps | Glu 60 O – Ala 64 HN | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 17.6-fold fold range across (59g−,60t) to (59t,60t) | Glu 60 O – Ala 64 HN | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 92 5-ps transitions over 1.14 μs | Trp 59 (trans), Glu 60, Ala 64 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `other` | 25233/114417 state sample count ratio | Trp 59 (trans), Glu 60, Ala 64 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `MD_and_MSM` | `population` | 96.6 % | Ile 101 | [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) |
| `Xray_and_CryoEM` | `population` | 0.29 occupancy | Trp59 (minor WT-like conformer) | [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |
| `Xray_and_CryoEM` | `population` | 0.34 occupancy | Glu60 (minor WT-like conformer) | [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |
| `Xray_and_CryoEM` | `population` | 0.71 occupancy | Trp59 (major perpendicular conformer) | [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) |

## 4. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **weak differential exchange linebroadening in WT vs H87V FKBP12** ([`10.1007/s10858-016-0064-7`](https://doi.org/10.1007/s10858-016-0064-7), sample `S1`): Asp 37, Trp 59, Glu 60, Ile 76, Phe 99, Val 101
- **central β4-β5 loop localized conformational transition (Pro 88–Gly 89 region; 4-fold HX enhancement in G89A)** ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990), sample `S3`): 83, 90, and 94
- **terminal/stem β4-β5 loop second localized conformational transition (nearly 14-fold HX enhancement in G89A)** ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990), sample `S3`): 80, 81, and 95
- **proline residues lacking amide protons and unquantified conformational exchange linebroadening positions in G89A** ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990), sample `S3`): 88, 92, and 93 (and several broadened residue positions)
- **enhanced conformational exchange linebroadening precluding hydrogen exchange quantitation in G89A** ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990), sample `S3`): Gly 58
- **altered local conformational flexibility induced by A81G substitution** ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990), sample `S4`): Ala 81 to Gly 83
- **selective log kOH− variation from loss of Tyr 80 phenol ring shielding in FKBP12.6-like I76C/Y80V** ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990), sample `S6`): Val 2 and Gln 3
- **active-site cleft rim separation between α-helix and β4-β5 loop stem (high HX dispersion across loop mutations)** ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990), sample `S1`): Gly 58 and Tyr 80
- **propagated conformational flexibility and transient inhibitor-binding transition in β2-β3a hairpin** ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990), sample `S1`): Gly 28 – Asp 37 (Phe 36, Gly 28, and Asp 37)
- **increased dynamical linebroadening in the SAFit2-bound state of I76C/Y80V** ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990), sample `S15`): L74
- **most slowly exchanging global stability core residues (predominately EX1 exchange-in kinetics across all six β4-β5 loop variants)** ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990), sample `S7`): 23–25, 64–76, and 98–104
- **Statistically coupled local conformational transitions (Trp 59 χ1 indole flip, Glu 60 χ1 rotamer transition, and Glu 60 O–Ala 64 HN hydrogen bond switching)** ([`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004), sample `S3`): Trp 59, Glu 60, Ala 64
- **Two conformational transitions centered in the β4-β5 (80's) loop causing NMR resonance doubling and conformational exchange linebroadening (cited prior work)** ([`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004), sample `S1`): long β4-β5 loop (or 80’s loop)
- **slightly lower picosecond order (S2 below average 0.88) in N and C termini and loops** ([`10.1021/bi00086a004`](https://doi.org/10.1021/bi00086a004), sample `S1`): 2, 17, 35-36, 39, 44, 52, 83, 86-87, 94-95, and 106-107
- **R1 smaller than average by one SD or more (loop regions)** ([`10.1021/bi00086a004`](https://doi.org/10.1021/bi00086a004), sample `S1`): V2, K35, F36, K44, K47, K52, G83, G86, H87, and A95
- **ms-us exchange (Rex above 3.0 Hz) in core of beta-strand 97-103** ([`10.1021/bi00086a004`](https://doi.org/10.1021/bi00086a004), sample `S1`): 100-101
- **low S2 and high Rex, possible conformational averaging** ([`10.1021/bi00086a004`](https://doi.org/10.1021/bi00086a004), sample `S1`): 35
- **picosecond mobility greatest (flap region)** ([`10.1021/bi00086a004`](https://doi.org/10.1021/bi00086a004), sample `S1`): 84-87
- **considerably higher backbone mobility than other regions (loops that contact ligand)** ([`10.1021/bi00086a004`](https://doi.org/10.1021/bi00086a004), sample `S1`): 36-45 and 78-95 loops
- **largest nonzero tau_e values** ([`10.1021/bi00086a004`](https://doi.org/10.1021/bi00086a004), sample `S1`): 33 and loop 53 to 56
- *... plus 17 additional region notes in the `Residue_sets` tab.*

### Conformational and complex PDB states (`States`)

- [`2PPO`](https://www.rcsb.org/structure/2PPO): WT (apo wild-type FKBP12) ([`10.1002/prot.22176`](https://doi.org/10.1002/prot.22176))
- [`2PPP`](https://www.rcsb.org/structure/2PPP): E60Q (apo E60Q mutant FKBP12) ([`10.1002/prot.22176`](https://doi.org/10.1002/prot.22176))
- [`2PPN`](https://www.rcsb.org/structure/2PPN): E60A (apo E60A mutant FKBP12) ([`10.1002/prot.22176`](https://doi.org/10.1002/prot.22176))
- [`1FKB`](https://www.rcsb.org/structure/1FKB): FKBP12-rapamycin binary complex ([`10.1007/s10858-012-9623-8`](https://doi.org/10.1007/s10858-012-9623-8))
- [`1FAP`](https://www.rcsb.org/structure/1FAP): FKBP12/rapamycin/FRB ternary complex ([`10.1007/s10858-012-9623-8`](https://doi.org/10.1007/s10858-012-9623-8))
- [`2PPN`](https://www.rcsb.org/structure/2PPN): canonical 2PPN structure of FKBP12 ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990))
- [`5HUA`](https://www.rcsb.org/structure/5HUA): FKBP1A–FK506 complex ([`10.1021/acs.analchem.2c03122`](https://doi.org/10.1021/acs.analchem.2c03122))
- [`9DCW`](https://www.rcsb.org/structure/9DCW): binary complex of FKBP12 with molecular glue 1a (FL), theta_lig = -35.06 deg (also used as initial MD coordinates) ([`10.1021/jacs.6c12127`](https://doi.org/10.1021/jacs.6c12127))
- [`9CO5`](https://www.rcsb.org/structure/9CO5): ternary complex of FKBP12, molecular glue 1a, and MAPRE1 (FLM), theta_lig = 32.63 deg (also used as initial MD coordinates) ([`10.1021/jacs.6c12127`](https://doi.org/10.1021/jacs.6c12127))
- [`8CHL`](https://www.rcsb.org/structure/8CHL): FKBP12 (C22V) cocrystal structure in complex with sulfonamide 1 ([`10.1021/jacsau.3c00241`](https://doi.org/10.1021/jacsau.3c00241))
- [`8CHM`](https://www.rcsb.org/structure/8CHM): FKBP12 (C22V) cocrystal structure in complex with R-sulfinamide 4b ([`10.1021/jacsau.3c00241`](https://doi.org/10.1021/jacsau.3c00241))
- [`8CHI`](https://www.rcsb.org/structure/8CHI): FKBP12 (C22V) cocrystal structure in complex with N-methyl sulfonimidamide 6a ([`10.1021/jacsau.3c00241`](https://doi.org/10.1021/jacsau.3c00241))
- [`1FAP`](https://www.rcsb.org/structure/1FAP): FKBP12·rapamycin·FRB (wild type) ([`10.1038/s41592-020-0913-x`](https://doi.org/10.1038/s41592-020-0913-x))
- [`9CO5`](https://www.rcsb.org/structure/9CO5): ternary complex FKBP12 : R,S-SLF-1a : MAPRE1 (2 : 2 : 2) ([`10.1039/d4cb00279b`](https://doi.org/10.1039/d4cb00279b))
- [`4IPX`](https://www.rcsb.org/structure/4IPX): H87V variant structure, closely similar to the major form of wild-type FKBP12 ([`10.1042/bj20130276`](https://doi.org/10.1042/bj20130276))
- [`4N19`](https://www.rcsb.org/structure/4N19): C22V,G89P variant of FKBP12 at 1.20 A resolution (cis-Pro88-Pro89 linkage, negative phi89, dual conformers for Trp59 and Glu60) ([`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429))
- [`2PPN`](https://www.rcsb.org/structure/2PPN): wild-type FKBP12 at 0.92 A resolution (trans-Gly89 with +103° phi torsion angle, canonical Trp59 indole orientation; also used as MR search model and NOE/SPARTA+ input) ([`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429))
- [`2PPP`](https://www.rcsb.org/structure/2PPP): E60Q variant of FKBP12 (perpendicular Trp59 indole ring orientation and shifted active-site alpha-helix) ([`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429))
- [`2PPO`](https://www.rcsb.org/structure/2PPO): E60A variant of FKBP12 (perpendicular Trp59 indole ring orientation and shifted active-site alpha-helix) ([`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429))
- [`6OQA`](https://www.rcsb.org/structure/6OQA): FKBP12–WDB002–CEP25011.4 ternary complex (heterotetramer with C2 symmetry; homodimeric CEP25011.4 coiled coil bound to two FKBP12–WDB002 complexes) ([`10.1073/pnas.2006560117`](https://doi.org/10.1073/pnas.2006560117))
- [`7U8D`](https://www.rcsb.org/structure/7U8D): Rapa*-3Z bound to FKBP12 V55G ([`10.1073/pnas.2204083119`](https://doi.org/10.1073/pnas.2204083119))
- [`1FKB`](https://www.rcsb.org/structure/1FKB): rapamycin bound to FKBP12 (published structure, also used as MR search model) ([`10.1073/pnas.2204083119`](https://doi.org/10.1073/pnas.2204083119))
- [`7U0T`](https://www.rcsb.org/structure/7U0T): human FKBP12-FK520-CaN complex ([`10.1073/pnas.2419883121`](https://doi.org/10.1073/pnas.2419883121))
- [`6VCU`](https://www.rcsb.org/structure/6VCU): human FKBP12-APX879 complex ([`10.1073/pnas.2419883121`](https://doi.org/10.1073/pnas.2419883121))
- [`7U0U`](https://www.rcsb.org/structure/7U0U): A. fumigatus FKBP12-FK506-CaN complex (homolog) ([`10.1073/pnas.2419883121`](https://doi.org/10.1073/pnas.2419883121))
- *... plus additional state citations in the `States` tab (50 total rows).*

## 5. Papers read and explicit gaps

**Checked `v3` / supplemental papers (30):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1021/bi00086a004`](https://doi.org/10.1021/bi00086a004) | 331 | 0 | 8 | 2 | One 15N spin-relaxation study of apo human FKBP-12 at 303 K and 500 MHz. Table I gives per-residue model-free  |
| [`10.1042/bj20131429`](https://doi.org/10.1042/bj20131429) | 18 | 4 | 4 | 2 | This paper investigates slow cis-trans Gly89 isomerization, microsecond-to-millisecond 80's loop dynamics, and |
| [`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004) | 16 | 0 | 2 | 6 | Extraction for FKBP12 (FKBP1A, P62942) covering 4 samples (WT and V101I NMR samples at 600 MHz / 25°C / pH 6.5 |
| [`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990) | 12 | 1 | 10 | 7 | This paper measures amide hydrogen exchange in six human FKBP12 constructs (wild-type, H87V, G89A, A81G, H94G, |
| [`10.1042/bj20130276`](https://doi.org/10.1042/bj20130276) | 12 | 1 | 2 | 3 | Human FKBP12 slow exchange between a major and a 12% minor state (zz-exchange lifetime 3.0 s at 43 C on the C2 |
| [`10.1038/srep39453`](https://doi.org/10.1038/srep39453) | 2 | 0 | 0 | 6 | This record extracts the backbone NMR dynamics measurements and experimental sample/method metadata for human  |
| [`10.1002/prot.22176`](https://doi.org/10.1002/prot.22176) | 0 | 3 | 0 | 0 | This paper reports high-resolution X-ray crystal structures of wild-type (2PPO), E60Q (2PPP), and E60A (2PPN)  |
| [`10.1007/s10858-012-9623-8`](https://doi.org/10.1007/s10858-012-9623-8) | 0 | 2 | 0 | 0 | Zero protein-dynamics rows (expected_rows: []) and zero dynamic residue sets (expected_residue_sets: []) exist |
| [`10.1007/s10858-016-0064-7`](https://doi.org/10.1007/s10858-016-0064-7) | 0 | 0 | 1 | 1 | The paper measures 15N T1, T1rho and NOE of FKBP12 (WT and H87V) at 500-900 MHz to derive residue-specific 15N |
| [`10.1007/s12104-019-09878-x`](https://doi.org/10.1007/s12104-019-09878-x) | 0 | 0 | 0 | 0 | This Biomolecular NMR Assignments paper reports 1H, 15N, and 13C backbone and sidechain resonance assignments  |
| [`10.1016/j.isci.2020.101533`](https://doi.org/10.1016/j.isci.2020.101533) | 0 | 0 | 0 | 7 | This paper develops single-chain Tb(III)-to-EGFP time-gated luminescence (TGL) LRET biosensors incorporating 1 |
| [`10.1016/j.jsb.2018.12.007`](https://doi.org/10.1016/j.jsb.2018.12.007) | 0 | 0 | 0 | 2 | This paper reanalyzes three previously published single-particle cryo-EM reconstructions of rabbit RyR1 with a |
| [`10.1021/acs.analchem.2c03122`](https://doi.org/10.1021/acs.analchem.2c03122) | 0 | 1 | 0 | 2 | This paper constructs and characterizes a recombinant HisTag-TEV-FKBP1A-GGGS-EmGFP fusion protein as a fluoror |
| [`10.1021/jacs.6c12127`](https://doi.org/10.1021/jacs.6c12127) | 0 | 2 | 0 | 7 | Zero expected dynamics rows: this study investigates macrocyclic molecular glues for FKBP12-MAPRE1 using conve |
| [`10.1021/jacsau.3c00241`](https://doi.org/10.1021/jacsau.3c00241) | 0 | 3 | 2 | 5 | This paper yields zero quantitative protein dynamics rows (expected_rows is empty) for human Peptidyl-prolyl c |
| [`10.1038/s41419-020-02746-w`](https://doi.org/10.1038/s41419-020-02746-w) | 0 | 0 | 0 | 0 | This paper is a medicinal-chemistry and autophagy cell-biology study on fluorescent thiazole–pyrazoline deriva |
| [`10.1038/s41467-024-49739-3`](https://doi.org/10.1038/s41467-024-49739-3) | 0 | 0 | 0 | 0 | This study characterizes SP3N (SLF-PEG3-NH2) as an alkylamine-tethered degrader precursor that is metabolized  |
| [`10.1038/s41592-020-0913-x`](https://doi.org/10.1038/s41592-020-0913-x) | 0 | 1 | 0 | 0 | This paper develops a rapamycin-inducible hetero-trimerization (CIT) system from split FRB and split human FKB |
| [`10.1038/s44320-025-00182-6`](https://doi.org/10.1038/s44320-025-00182-6) | 0 | 0 | 0 | 2 | 0 expected dynamics rows, 0 expected conformational states, and 0 expected residue sets. The paper uses endoge |
| [`10.1039/d4cb00279b`](https://doi.org/10.1039/d4cb00279b) | 0 | 1 | 0 | 2 | Zero dynamics rows are extracted for FKBP12 because 151.txt reports protein-array screening, TR-FRET binary bi |
| [`10.1073/pnas.2006560117`](https://doi.org/10.1073/pnas.2006560117) | 0 | 1 | 1 | 4 | This paper characterizes X1-cluster natural products (WDB001–WDB003) and the semisynthetic analog WDB011 bindi |
| [`10.1073/pnas.2204083119`](https://doi.org/10.1073/pnas.2204083119) | 0 | 2 | 1 | 1 | Zero dynamics rows (expected_rows = []). This chemical-genetics and X-ray crystallography study develops the b |
| [`10.1073/pnas.2419883121`](https://doi.org/10.1073/pnas.2419883121) | 0 | 6 | 0 | 2 | Zero quantitative protein dynamics rows are reported in this paper (expected_rows = []). The study combines XP |
| [`10.1074/jbc.m112.365932`](https://doi.org/10.1074/jbc.m112.365932) | 0 | 1 | 0 | 0 | This paper solves the 2.35 Å X-ray crystal structure of the human ALK2 GS and kinase domains (residues 172–499 |
| [`10.1080/14756366.2019.1667342`](https://doi.org/10.1080/14756366.2019.1667342) | 0 | 0 | 0 | 3 | This paper investigates how FKBP12 (FKBP1A, UniProt P62942) accelerates α-synuclein aggregation into dendritic |

*Showing top 25 of 30 checked papers; see `Papers` tab for full list.*

**Explicit figure-only, SI-only, or access gaps (83):**

- Per-residue Delta(R2-R1/2)900/600 and DeltaDelta values for FKBP12 ([`10.1007/s10858-016-0064-7`](https://doi.org/10.1007/s10858-016-0064-7)): figure only (Figs 2-4), no printed numbers
- Table S1: pH values for CLEANEX-PM pH series and calibrated pH values for 1H exchange-in samples ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990)): in supplement not available
- Table S2: per-residue log kOH− values and individual statistical uncertainties across 54 residues for the six FKBP12 variants ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990)): in supplement not available
- Table S3: per-residue amide isotope exchange-in log kex rates for the β4-β5 loop variants ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990)): in supplement not available
- Fig. 1: observed and predicted transient-state log kOH− plots for WT, H87V, and G89A across six β4-β5 loop residues ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990)): figure only
- Fig. 2B: per-residue log kOH− profiles for WT, H87V, A81G, H94G, G89A, and I76C/Y80V ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990)): figure only
- Fig. 8: per-residue amide isotope exchange-in log kex profiles for all six FKBP12 variants ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990)): figure only
- Fig. 6 and Fig. 7: 2D HSQC crosspeak intensities for SAFit2 inhibitor binding competition ([`10.1016/j.bbapap.2023.140990`](https://doi.org/10.1016/j.bbapap.2023.140990)): figure only
- Full 8-state transition matrix elements and bottom-row state population averages for WT FKBP12 (Fig. 5) ([`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004)): figure only
- Free energy diagram values (kJ/mol) for gauche- and trans χ1 rotamer states of Trp 59 and Glu 60 in WT FKBP12 (Fig. 6) ([`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004)): figure only
- Hydrogen-bond free energy differentials between Glu 60 O and Ala 64 HN across the four Trp 59 / Glu 60 χ1 rotamer states in WT FKBP12 (Fig. 7) ([`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004)): figure only
- Free energy diagram values (kJ/mol) for Trp 59 and Glu 60 χ1 rotamer states in V101I FKBP12 (Fig. 8A, 8B) ([`10.1016/j.bpc.2014.06.004`](https://doi.org/10.1016/j.bpc.2014.06.004)): figure only
- *... plus 71 additional gap entries in the `Gaps` tab.*

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
