# Glucocorticoid receptor (`DBD82`)

**Atlas tier:** Tier 1 · Experimental conformational exchange rates or populations  
**UniProt:** `P06536` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `500` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md) · [Worked deep walkthrough / review case](../v3_previews/DBD82.md)

> **Audit note:** Review case (Rank 1): mixes rat DBD & human LBD + MD/FCS/EMSA/FRET rows

## 1. Experimental conformational exchange (rates, populations, Δω)

*8 source-grounded experimental rows (MD simulations and cryo-X-ray/cryo-EM occupancies are separated in Section 3).*

| Quantity | Value | Residues / group | Method group | Species | Ligand & conditions | Deposit match | Paper |
|---|---|---|---|---|---|---|---|
| `kex` | 4.36 s−1 | Gly470 | `NMR_exchange_and_dispersion` | `target` | bound to GBS dsDNA (~33% excess DNA, ~300 μM dimer complex; specific GBS for Fig. 6b | `no` | [`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595) |
| `kex` | 3.10 s−1 | Gly470 | `NMR_exchange_and_dispersion` | `target` | bound to GBS dsDNA (~33% excess DNA, ~300 μM dimer complex; specific GBS for Fig. 6b | `no` | [`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595) |
| `kex` | 1147 s−1 ± 82 | global (13C and 15N probes) | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | bound to dex and TIF2 peptide; 298 K; pH 7.5; 14.1 and 18.8 T | `unclear` | [`10.1126/sciadv.abb5277`](https://doi.org/10.1126/sciadv.abb5277) |
| `population` | 19 % ± 7 | global, minor-state population pm | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | bound to dex and TIF2 peptide; 298 K; pH 7.5; 14.1 and 18.8 T | `unclear` | [`10.1126/sciadv.abb5277`](https://doi.org/10.1126/sciadv.abb5277) |
| `delta_omega` | 0.5 to 1.2 ppm | 15N backbone residues (residue-specific range) | `NMR_exchange_and_dispersion` | `same_protein_other_construct` | bound to dex and TIF2 peptide; 298 K; pH 7.5; 14.1 and 18.8 T | `unclear` | [`10.1126/sciadv.abb5277`](https://doi.org/10.1126/sciadv.abb5277) |
| `population` | roughly two thirds fraction of receptors | full-length hGRα (CFP-GRwt/YFP-GRwt, monomer state prior to DEX s | `FRET_and_fluorescence` | `homolog` | apo (prior to DEX stimulation); 37°C; pH not printed; not printed | `no` | [`10.1371/journal.pone.0064831`](https://doi.org/10.1371/journal.pone.0064831) |
| `population` | around one third fraction of receptors | full-length hGRα (CFP-GRwt/YFP-GRwt, monomer state prior to DEX s | `FRET_and_fluorescence` | `homolog` | apo (prior to DEX stimulation); 37°C; pH not printed; not printed | `no` | [`10.1371/journal.pone.0064831`](https://doi.org/10.1371/journal.pone.0064831) |
| `population` | around one third fraction of receptors | full-length hGRα (CFP-GRwt/YFP-GRwt, monomer state prior to DEX s | `FRET_and_fluorescence` | `homolog` | apo (prior to DEX stimulation); 37°C; pH not printed; not printed | `no` | [`10.1371/journal.pone.0064831`](https://doi.org/10.1371/journal.pone.0064831) |

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*9 rows total (0 spin-relaxation/model-free; 9 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1016/j.bbagen.2025.130809`](https://doi.org/10.1016/j.bbagen.2025.130809) | `FRET_and_fluorescence` | `same_protein_other_construct` | apo / untreated (sham treatment with Flu | other (2) | other = 1.8 ms (full-length human GRα (mStayGold-GR)) |
| [`10.1126/sciadv.abb5277`](https://doi.org/10.1126/sciadv.abb5277) | `NMR_exchange_and_dispersion` | `target` | bound to dex, cortisol, pred, AZ938 or d | other (2) | other = 0.1 pm/pM (M752, GRwt-dibC-TIF2 and GRwt-cortis…) |
| [`10.1016/j.bbagen.2025.130809`](https://doi.org/10.1016/j.bbagen.2025.130809) | `FRET_and_fluorescence` | `same_protein_other_construct` | bound to 500 nM dexamethasone (Dex, 15 m | other (1) | other = 10–20 s (full-length human GRα (mStayGold-GR)) |
| [`10.1371/journal.pone.0013279`](https://doi.org/10.1371/journal.pone.0013279) | `Biophysics_and_other` | `homolog` | bound to 10 nM Dex and 33-bp MMTV GRE ol | other (1) | other = 0.56 min (endogenous GR (full-length; GR-Dex/D…) |
| [`10.1371/journal.pone.0013279`](https://doi.org/10.1371/journal.pone.0013279) | `Biophysics_and_other` | `homolog` | bound to 1 µM RU486 and 33-bp MMTV GRE o | other (1) | other = 2.33 min (endogenous GR (full-length; GR-RU486…) |
| [`10.1371/journal.pone.0013279`](https://doi.org/10.1371/journal.pone.0013279) | `Biophysics_and_other` | `homolog` | bound to 10 µM 21OH-6,19OP and 33-bp MMT | other (1) | other = 0.96 min (endogenous GR (full-length; GR-21OH-…) |
| [`10.1371/journal.pone.0013279`](https://doi.org/10.1371/journal.pone.0013279) | `Biophysics_and_other` | `homolog` | bound to 10 µM 21HS-6,19OP and 33-bp MMT | other (1) | other = 1.02 min (endogenous GR (full-length; GR-21HS-…) |

## 3. Computational (MD/MSM) and cryo-structure (X-ray / cryo-EM) rows

*2 rows intentionally separated from experimental solution dynamics pending expert scope lock:*

| Method group | Quantity | Value | Residues / group | Paper |
|---|---|---|---|---|
| `MD_and_MSM` | `population` | ~40 % | lever arm (residues 450–456), shared between GBS1 and GBS2 monome | [`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9) |
| `MD_and_MSM` | `population` | at least 10 % | lever arm (residues 450–456), three clusters shared between DNA-f | [`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9) |

## 4. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **split peaks suggesting conformational exchange or distinct monomer environments** ([`10.1038/ncomms12621`](https://doi.org/10.1038/ncomms12621), sample `S1`): G458, C460 and K461
- **Slow conformational exchange of DNA-bound GR dimer partners (ZZ-exchange NMR)** ([`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595), sample `S3`): Gly470 and Ile484
- **GBS-dependent conformational sampling across seven GBS complexes (chemical shift variance, reduced in A477T)** ([`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595), sample `S4`): recognition helix and lever arm, Arg466
- **Spacer-dependent D-loop conformational shift (15N-HSQC CSP)** ([`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595), sample `S4`): Ala477 and Gly478
- **partial disorder / alternative orientation of C-terminal helix H3 in one monomer of each crystal dimer** ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9), sample `S1`): C-terminal helix (H3) following the core DBD
- **conformational flexibility and multiple monomer conformations in the DNA-free crystal** ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9), sample `S1`): lever arm region (residues 450–456)
- **side-chain mobility / alternate packed ('in') vs flipped ('out') conformation in crystal electron density (alternate conformation in 4 of 8 monomers)** ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9), sample `S1`): His453
- **highly dynamic solvent-exposed side chains unresolved in DNA-free crystal, becoming ordered upon DNA contact** ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9), sample `S1`): residues in direct contact with DNA (in the DNA-binding helix)
- **highest backbone Cα RMSF flexibility in MD simulations (lever arm residues 450–456 and D-loop residues 457–465; D-loop stabilized in GBS head-to-head dimer S3 relative to free S2 and IR-GBS S4)** ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9), sample `S2`): lever arm and D-loop
- **rapid MD conformational flipping between 'out' and 'in' states (psi dihedral angle switching in Fig. 6C across simulated systems)** ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9), sample `S2`): His453
- **Des-CIC-specific correlated-motion pathway between Q642 and the SRC-2 peptide (MD)** ([`10.1093/pnasnexus/pgae573`](https://doi.org/10.1093/pnasnexus/pgae573), sample `S1`): Q642 to SRC-2 peptide via h5-h6
- **15N relaxation dispersion in helix 12** ([`10.1126/sciadv.abb5277`](https://doi.org/10.1126/sciadv.abb5277), sample `S1`): E751, L753, I756
- **15N relaxation dispersion in helix 1 (tau2)** ([`10.1126/sciadv.abb5277`](https://doi.org/10.1126/sciadv.abb5277), sample `S1`): S534, V538, E542, L544
- **15N relaxation dispersion next to K579** ([`10.1126/sciadv.abb5277`](https://doi.org/10.1126/sciadv.abb5277), sample `S1`): A580, I581
- **methionine methyl and tryptophan side chains showing exchange** ([`10.1126/sciadv.abb5277`](https://doi.org/10.1126/sciadv.abb5277), sample `S1`): M565, M601, M752, W577, W600
- **Two distinct orientations and chain B conformational heterogeneity of H472 and the lever arm** ([`10.1126/science.1164265`](https://doi.org/10.1126/science.1164265), sample `S3`): H472; chain B lever arm (residues 469 to 474 per line 11)
- **Higher crystallographic B factors (less well-defined structure) and discrete alternate conformations in composite omit maps of the chain B lever arm** ([`10.1126/science.1164265`](https://doi.org/10.1126/science.1164265), sample `S3`): chain B lever arm (residues 469 to 474 per line 11)
- **Substantial lever arm conformational heterogeneity across crystallization conditions (contrasted with invariant GR-DBD:Sgk)** ([`10.1126/science.1164265`](https://doi.org/10.1126/science.1164265), sample `S1`): lever arm (residues 469 to 474 per line 11)
- **RU486-induced helix H12 destabilization and two-stage conformational transition in 30 ns MD (0-3.5 ns abrupt RMSD rise, 3.5-15 ns average RMSD 1.61 Å, 15-20 ns transition, 20-30 ns stable conformatio…** ([`10.1371/journal.pone.0013279`](https://doi.org/10.1371/journal.pone.0013279), sample `S21`): H12 (751–766)
- **reversible loss (5-15 ns) and recovery (last 10 ns) of helical motif around Ile756 to accommodate bulky RU486 moiety** ([`10.1371/journal.pone.0013279`](https://doi.org/10.1371/journal.pone.0013279), sample `S21`): 756–757

### Conformational and complex PDB states (`States`)

- [`1M2Z`](https://www.rcsb.org/structure/1M2Z): GR:DEX active conformation (AF-2 helix positioned in an active conformation) ([`10.1016/j.bbrc.2012.03.084`](https://doi.org/10.1016/j.bbrc.2012.03.084))
- [`3G9J`](https://www.rcsb.org/structure/3G9J): GR DBD crystal structure, two monomers (chains A and B) ([`10.1038/ncomms12621`](https://doi.org/10.1038/ncomms12621))
- [`3G99`](https://www.rcsb.org/structure/3G99): GR DBD – Pal-F (prior crystal structure complex with Pal-F GBS; aligned and analyzed by Curves+) ([`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595))
- [`3G6U`](https://www.rcsb.org/structure/3G6U): GR DBD – Fkbp5 (prior crystal structure complex with Fkbp5 GBS; aligned/analyzed by Curves+ and used as NMR CSP mapping scaffold) ([`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595))
- [`6CFN`](https://www.rcsb.org/structure/6CFN): DNA-free (apo) GR DBD crystal structure (monomer / four Cys431 disulfide-linked dimers in asymmetric unit) ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9))
- [`3G99`](https://www.rcsb.org/structure/3G99): DNA-bound GR DBD dimer in complex with palindromic 16-nt GBS DNA (GBS1 chain A and GBS2 chain B) ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9))
- [`4HN5`](https://www.rcsb.org/structure/4HN5): DNA-bound GR DBD two monomers in complex with palindromic IR-GBS DNA (IR-GBS1 high-affinity and IR-GBS2 low-affinity; chain A also used as MR search model) ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9))
- [`3G9J`](https://www.rcsb.org/structure/3G9J): DNA-bound GR DBD dimer in complex with 18-nt GBS DNA ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9))
- [`1GDC`](https://www.rcsb.org/structure/1GDC): DNA-free (apo) GR DBD NMR solution structure ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9))
- [`1RGD`](https://www.rcsb.org/structure/1RGD): DNA-free (apo) GR DBD NMR solution structure ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9))
- [`2GDA`](https://www.rcsb.org/structure/2GDA): DNA-free (apo) GR DBD NMR solution structure ([`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9))
- [`5VA7`](https://www.rcsb.org/structure/5VA7): GR DBD:IL11 TRE complex ([`10.1093/nar/gkx509`](https://doi.org/10.1093/nar/gkx509))
- [`5VA0`](https://www.rcsb.org/structure/5VA0): GR DBD:VCAM1 TRE complex ([`10.1093/nar/gkx509`](https://doi.org/10.1093/nar/gkx509))
- [`4hn5`](https://www.rcsb.org/structure/4hn5): GR DBD:IR-GBS complex (also used as MR phasing model) ([`10.1093/nar/gkx509`](https://doi.org/10.1093/nar/gkx509))
- [`3FYL`](https://www.rcsb.org/structure/3FYL): GR DBD-GBS crystal structure (canonical GBS complex) ([`10.1093/nar/gkx509`](https://doi.org/10.1093/nar/gkx509))
- [`4UDC`](https://www.rcsb.org/structure/4UDC): DEX-bound GR LBD ([`10.1093/pnasnexus/pgae573`](https://doi.org/10.1093/pnasnexus/pgae573))
- [`5NFP`](https://www.rcsb.org/structure/5NFP): starting structure for all other ligand states (ligand stripped and used for docking) ([`10.1093/pnasnexus/pgae573`](https://doi.org/10.1093/pnasnexus/pgae573))
- [`4UDC`](https://www.rcsb.org/structure/4UDC): GR-dex-TIF2, structure on which exchanging residues are mapped ([`10.1126/sciadv.abb5277`](https://doi.org/10.1126/sciadv.abb5277))
- [`1M2Z`](https://www.rcsb.org/structure/1M2Z): active conformation; GR LBD-Dex complex bound to TIF2 peptide (homolog) ([`10.1371/journal.pone.0013279`](https://doi.org/10.1371/journal.pone.0013279))
- [`1NHZ`](https://www.rcsb.org/structure/1NHZ): GR LBD bound to RU486, helix 12 not completely resolved (homolog) ([`10.1371/journal.pone.0013279`](https://doi.org/10.1371/journal.pone.0013279))
- [`1H52`](https://www.rcsb.org/structure/1H52): GR LBD bound to RU486, partially unfolded (homolog) ([`10.1371/journal.pone.0013279`](https://doi.org/10.1371/journal.pone.0013279))
- [`3G9M`](https://www.rcsb.org/structure/3G9M): rat GR DBD homodimer (3g9mAB; monomer template 3G9MA) ([`10.1371/journal.pone.0227520`](https://doi.org/10.1371/journal.pone.0227520))
- [`4P6X`](https://www.rcsb.org/structure/4P6X): cortisol-bound GR LBD (homolog, template for rat GR LBD homology model) ([`10.1371/journal.pone.0227520`](https://doi.org/10.1371/journal.pone.0227520))
- [`3H52`](https://www.rcsb.org/structure/3H52): open antagonist-bound form of GR LBD (homolog, template for rat GR LBD homology model) ([`10.1371/journal.pone.0227520`](https://doi.org/10.1371/journal.pone.0227520))

## 5. Papers read and explicit gaps

**Checked `v3` / supplemental papers (23):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1126/sciadv.abb5277`](https://doi.org/10.1126/sciadv.abb5277) | 5 | 1 | 4 | 5 | The text prints one global two-state fit (kex, pm, 15N delta-omega range) for GRF602S-dex-TIF2 and approximate |
| [`10.1371/journal.pone.0013279`](https://doi.org/10.1371/journal.pone.0013279) | 4 | 3 | 2 | 8 | This paper reports no NMR relaxation experiments (no 500 MHz field and no 298.5 K sample) and instead investig |
| [`10.1016/j.bbagen.2025.130809`](https://doi.org/10.1016/j.bbagen.2025.130809) | 3 | 0 | 0 | 5 | Live-cell fluorescence correlation spectroscopy (spFCS, mpFCS) and two-foci cross-correlation (tfCCC) study of |
| [`10.1371/journal.pone.0064831`](https://doi.org/10.1371/journal.pone.0064831) | 3 | 0 | 0 | 5 | This cell-culture pharmacology and imaging study measures concentration-dependent ligand-independent dimerizat |
| [`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595) | 2 | 2 | 3 | 6 | This study investigates rat glucocorticoid receptor (GR) DNA binding domain (DBD, residues 440–525; WT and A47 |
| [`10.1038/s41598-018-31812-9`](https://doi.org/10.1038/s41598-018-31812-9) | 2 | 7 | 6 | 6 | This paper reports the 2.5 Å X-ray crystal structure of DNA-free glucocorticoid receptor DNA-binding domain (G |
| [`10.1016/j.bbrc.2012.03.084`](https://doi.org/10.1016/j.bbrc.2012.03.084) | 0 | 1 | 0 | 0 |  |
| [`10.1016/j.freeradbiomed.2025.09.008`](https://doi.org/10.1016/j.freeradbiomed.2025.09.008) | 0 | 0 | 0 | 0 | Zero-row extraction (expected_rows: []): this paper studies glucocorticoid receptor (GR)-mediated transcriptio |
| [`10.1016/j.jpain.2025.105473`](https://doi.org/10.1016/j.jpain.2025.105473) | 0 | 0 | 0 | 0 | Zero expected dynamics rows, zero conformational PDB states, and zero dynamic residue sets. Despite 'dynamics' |
| [`10.1038/ncomms12621`](https://doi.org/10.1038/ncomms12621) | 0 | 1 | 1 | 1 | No dynamics value is printed for the GR DBD. The NMR data are chemical shift perturbations and split peaks sho |
| [`10.1038/s41467-021-21063-0`](https://doi.org/10.1038/s41467-021-21063-0) | 0 | 0 | 0 | 0 | Zero dynamics rows, zero conformational PDB states, and zero dynamic residue sets exist for Glucocorticoid rec |
| [`10.1073/pnas.2528760123`](https://doi.org/10.1073/pnas.2528760123) | 0 | 0 | 0 | 0 | This paper designs, synthesizes, photophysically characterizes, and evaluates light-switchable PROTAC degrader |
| [`10.1093/nar/gkx509`](https://doi.org/10.1093/nar/gkx509) | 0 | 4 | 0 | 0 | This paper reports zero protein dynamics rows (expected_rows is empty): it studies direct Glucocorticoid recep |
| [`10.1093/pnasnexus/pgae573`](https://doi.org/10.1093/pnasnexus/pgae573) | 0 | 2 | 1 | 1 |  |
| [`10.1111/febs.70137`](https://doi.org/10.1111/febs.70137) | 0 | 0 | 0 | 1 | No experimental dynamics values for GR. The paper's only GR content is a computational model (PDB 1m2z, GR wit |
| [`10.1126/sciadv.abl7295`](https://doi.org/10.1126/sciadv.abl7295) | 0 | 0 | 0 | 5 | This paper investigates the conformational dynamics and allosteric network of yeast Hsp90 (Hsp82) and uses a s |
| [`10.1126/science.1164265`](https://doi.org/10.1126/science.1164265) | 0 | 0 | 3 | 3 | Available main text (200.txt; no supplement, no tables, and no figure legends) contains 0 quantitative protein |
| [`10.1159/000553135`](https://doi.org/10.1159/000553135) | 0 | 0 | 0 | 0 | No experimental dynamics value (NMR, HDX, FRET, EPR) is printed for GR. The paper docks four phytochemicals in |
| [`10.1186/s12943-026-02630-9`](https://doi.org/10.1186/s12943-026-02630-9) | 0 | 0 | 0 | 0 | This paper is an ovarian cancer cell biology and transcriptomics study of endogenous human glucocorticoid rece |
| [`10.1371/journal.pone.0048385`](https://doi.org/10.1371/journal.pone.0048385) | 0 | 0 | 0 | 1 | This paper characterizes the non-steroidal selective glucocorticoid receptor modulator (SGRM) Org 214007-0 com |
| [`10.1371/journal.pone.0227520`](https://doi.org/10.1371/journal.pone.0227520) | 0 | 3 | 0 | 7 | This cell-biology, fluorescence-imaging, biochemical, and computational-docking study investigates glucocortic |
| [`10.3390/ijms262311404`](https://doi.org/10.3390/ijms262311404) | 0 | 0 | 0 | 0 | Pharmacology paper on synephrine-derivative ligands of the glucocorticoid receptor ligand-binding domain. It p |
| [`10.3390/md23060232`](https://doi.org/10.3390/md23060232) | 0 | 0 | 0 | 1 |  |

**Explicit figure-only, SI-only, or access gaps (55):**

- GR diffusion coefficients (DCs), multi-component diffusion times (tau_D,2, tau_D,3), and relative molar fractions (F1, F2, F3) for eGFP-GR and mStayGold-GR in cytoplasm and nucleus ([`10.1016/j.bbagen.2025.130809`](https://doi.org/10.1016/j.bbagen.2025.130809)): figure only / in supplement not available (plotted in Fig. 4B-C, Fig. 5D-F, and Figs. S10-S12, S15; not printed as numbers in the text)
- GR monomer and homodimer fractions (Fm, Fd) and relative molecular brightness (R) values for eGFP-GR and mStayGold-GR ([`10.1016/j.bbagen.2025.130809`](https://doi.org/10.1016/j.bbagen.2025.130809)): figure only / not printed (converted into Kd,homo plots in Fig. 4D-E and Fig. S14 without numeric Fm/Fd values printed in text)
- GR DNA-binding kinetic rate constants (kB,1, kB,2) from binding models (Eqs. 4-5) and concentration dependence of DNA-bound fraction ([`10.1016/j.bbagen.2025.130809`](https://doi.org/10.1016/j.bbagen.2025.130809)): in supplement not available / figure only (tested in Figs. S10 and S13; authors proceeded with Eq. 3 three-component free 3D diffusion model)
- Site-resolved and integrated two-foci cross-correlation amplitudes Gc,sub(tau) at nuclear envelope sites 1-15 (Fig. 5G-H, Figs. S16-S17) ([`10.1016/j.bbagen.2025.130809`](https://doi.org/10.1016/j.bbagen.2025.130809)): figure only / in supplement not available (only the peak lag time range 10-20 s and site indices showing import vs export are printed in text)
- Supplementary Material 1 (Figs. S1-S17 and binding-model derivation details) ([`10.1016/j.bbagen.2025.130809`](https://doi.org/10.1016/j.bbagen.2025.130809)): in supplement not available (only 'Supplementary material: 1' placeholder appears in 025.txt)
- CSP values, split-peak spectra, MD RMSF profiles ([`10.1038/ncomms12621`](https://doi.org/10.1038/ncomms12621)): figure only (Supplementary Figs 5, 6, 9, 10; Figs 5, 6)
- Ile484 ZZ-exchange conformational exchange rates (kex) and relaxation rates (plus Gly470 relaxation rates) plotted in Fig. 6b and Supplementary Fig. 5 ([`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595)): figure only / in supplement not available
- Supplementary Fig. 5 (Supplementary Fig. 5a–e: ZZ-exchange spectra, cross-peak fits, and DNA dissociation rate measurement) ([`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595)): in supplement not available
- Supplementary Figs. 1–4 and 6, and Main Figs. 2b–d, 3b–d, 6a, 6d (Gha NMR assignments >90%, unbound WT DBD HSQC comparison, per-residue CSPs, and chemical shift variances across 7 GBSs) ([`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595)): figure only / in supplement not available
- Supplementary Table 1 and Fig. 5a–c (full SPR K1/2, Hill coefficients nH, and dissociation half-lives t1/2 across seven GBSs at 35°C and 8°C) ([`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595)): in supplement not available / figure only
- Supplementary Table 2 (correlation analyses between transcriptional activity and DNA binding affinity/kinetics) ([`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595)): in supplement not available
- Supplementary Fig. 7 (FRET efficiency measurements for WT and A477T GR DBD across five GBSs) ([`10.1038/nsmb.2595`](https://doi.org/10.1038/nsmb.2595)): in supplement not available
- *... plus 43 additional gap entries in the `Gaps` tab.*

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
