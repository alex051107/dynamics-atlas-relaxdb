# DNA helicase II (UrvD domain) (`UVRDTD`)

**Atlas tier:** Tier 2 · Quantitative relaxation / HDX / DEER / FRET or exchange detected (no rate/pop)  
**UniProt:** `P03018` · **RelaxDB deposited card:** T = `298.5 (possible placeholder)`, field = `700/800` MHz, pH = `n/a`  
**Links:** [Back to 131-Protein Atlas Index](../ATLAS_131.md)

## 1. Experimental conformational exchange (rates, populations, Δω)

No experimental exchange rate (`kex`, `kAB/kBA`, `kopen/kclose`) or minor-state population (`pB`, `population`) was printed in the full-text papers read so far.

## 2. Other experimental dynamics (spin relaxation, HDX, EPR/DEER, FRET)

*21 rows total (9 spin-relaxation/model-free; 12 HDX/DEER/FRET/biophysics), summarized by paper and condition:*

| Paper | Method group | Species | Ligand / state | Quantities & row counts | Example printed value |
|---|---|---|---|---|---|
| [`10.1038/s42003-020-01332-2`](https://doi.org/10.1038/s42003-020-01332-2) | `NMR_spin_relaxation_and_MF` | `same_protein_other_construct` | apo | tau_m (2), NOE (2), R2 (2), S2 (2), R1 (1) | tau_m = 3.63 ns (whole construct) |
| [`10.1016/j.jmb.2011.06.019`](https://doi.org/10.1016/j.jmb.2011.06.019) | `FRET_and_fluorescence` | `same_protein_other_construct` | apo, varying NaCl | other (6) | other = 64 Å (Cys473 (2B) / Cys100 (1B) alpha-carb…) |
| [`10.1126/science.aaa0130`](https://doi.org/10.1126/science.aaa0130) | `FRET_and_fluorescence` | `same_protein_other_construct` | bound to DNA hairpin, ATP present | other (2) | other = 0.7±0.2 FRET efficiency (2B domain, closed (high FRET) state) |
| [`10.1016/j.jmb.2011.06.019`](https://doi.org/10.1016/j.jmb.2011.06.019) | `FRET_and_fluorescence` | `same_protein_other_construct` | apo, buffer T20 (20 mM NaCl) | other (1) | other = ~35 Å (2B sub-domain, DM-1B/2B, no DNA, buf…) |
| [`10.1016/j.jmb.2011.06.019`](https://doi.org/10.1016/j.jmb.2011.06.019) | `FRET_and_fluorescence` | `same_protein_other_construct` | bound to (dT)35 | other (1) | other = ~50 Å (2B sub-domain, DM-1B/2B, bound to (d…) |
| [`10.1016/j.jmb.2011.06.019`](https://doi.org/10.1016/j.jmb.2011.06.019) | `FRET_and_fluorescence` | `same_protein_other_construct` | translocation on ssDNA | other (1) | other = 182 nucleotides/s (ssDNA translocation, unlabeled DM-1B…) |
| [`10.1016/j.jmb.2011.06.019`](https://doi.org/10.1016/j.jmb.2011.06.019) | `FRET_and_fluorescence` | `same_protein_other_construct` | apo | other (1) | other = 158 nucleotides/s (ssDNA translocation, UvrDΔ73 monomer) |

## 3. Author-named dynamic regions and conformational PDB states

### Dynamic residue regions (`Residue_sets`)

- **salt bridges between 1B and 2B stabilizing the closed state** ([`10.1016/j.jmb.2011.06.019`](https://doi.org/10.1016/j.jmb.2011.06.019), sample `S1`): D115–K389 and D118–R396
- **elevated micro-to-millisecond exchange (Rex) in aromatic cage residues** ([`10.1038/s42003-020-01332-2`](https://doi.org/10.1038/s42003-020-01332-2), sample `S1`): F702, W709
- **natively disordered / unresolved C-terminal region in crystal structures (conserved ~50-aa core predicted to adopt a RapA/HepA-like beta-sheet Tudor fold and act as RNAP interaction hub)** ([`10.1371/journal.pone.0078141`](https://doi.org/10.1371/journal.pone.0078141), sample `S3`): ~90 amino acids at C-terminus, of which the final ~50 are well conserved
- **disordered C-terminal extension of GstPcrA (PcrA-Ct), necessary and sufficient for direct RNAP pull-down interaction** ([`10.1371/journal.pone.0078141`](https://doi.org/10.1371/journal.pone.0078141), sample `S14`): residues 653-724 (final 72 amino-acids)

### Conformational and complex PDB states (`States`)

- [`3LFU`](https://www.rcsb.org/structure/3LFU): apo UvrD, 2B sub-domain open ([`10.1016/j.jmb.2011.06.019`](https://doi.org/10.1016/j.jmb.2011.06.019))
- [`2IS1`](https://www.rcsb.org/structure/2IS1): UvrD bound to 3′-ssDNA-duplex junction, 2B closed ([`10.1016/j.jmb.2011.06.019`](https://doi.org/10.1016/j.jmb.2011.06.019))
- [`7EGS`](https://www.rcsb.org/structure/7EGS): E. coli UvrD-CTD/RNAP-β2i4 binary complex ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6))
- [`7EGT`](https://www.rcsb.org/structure/7EGT): T. thermophilus UvrD-CTD/UvrB-NTD complex (homolog) ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6))
- [`3LFU`](https://www.rcsb.org/structure/3LFU): apo form (UvrDapo) ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6))
- [`2IS1`](https://www.rcsb.org/structure/2IS1): closed form (UvrDclosed) ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6))
- [`6YI2`](https://www.rcsb.org/structure/6YI2): solution NMR structure of UvrD-CTD ([`10.1038/s42003-020-01332-2`](https://doi.org/10.1038/s42003-020-01332-2))
- [`2IS6`](https://www.rcsb.org/structure/2IS6): closed 2B subdomain, EcUvrD bound to DNA junction ([`10.1073/pnas.2422330122`](https://doi.org/10.1073/pnas.2422330122))
- [`3LFU`](https://www.rcsb.org/structure/3LFU): open ([`10.1126/science.aaa0130`](https://doi.org/10.1126/science.aaa0130))
- [`2IS2`](https://www.rcsb.org/structure/2IS2): closed ([`10.1126/science.aaa0130`](https://doi.org/10.1126/science.aaa0130))

## 4. Papers read and explicit gaps

**Checked `v3` / supplemental papers (9):**

| Paper (DOI) | Rows kept | States | Regions | Gaps | Summary |
|---|---:|---:|---:|---:|---|
| [`10.1016/j.jmb.2011.06.019`](https://doi.org/10.1016/j.jmb.2011.06.019) | 10 | 2 | 1 | 1 | Ensemble Cy3/Cy5 FRET on UvrD double-cysteine mutants gives conformational distances and salt midpoints for 2B |
| [`10.1038/s42003-020-01332-2`](https://doi.org/10.1038/s42003-020-01332-2) | 9 | 1 | 1 | 2 | Nine rows for the UvrD C-terminal domain (UvrD-CTD, 645-720): one TRACT correlation time and averaged 15N rela |
| [`10.1126/science.aaa0130`](https://doi.org/10.1126/science.aaa0130) | 2 | 2 | 0 | 1 |  |
| [`10.1038/nature12928`](https://doi.org/10.1038/nature12928) | 0 | 0 | 0 | 1 | This paper investigates how Escherichia coli UvrD promotes transcription-coupled nucleotide excision repair by |
| [`10.1038/ncomms2882`](https://doi.org/10.1038/ncomms2882) | 0 | 0 | 0 | 0 | Single-molecule TIRF and optical-tweezers study of E. coli UvrD translocation and unwinding on ssDNA. It print |
| [`10.1038/s41467-021-27304-6`](https://doi.org/10.1038/s41467-021-27304-6) | 0 | 0 | 0 | 0 | Single-molecule optical tweezers and MD paper on UvrD stepping; no NMR, HDX, FRET or EPR dynamics values are p |
| [`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6) | 0 | 4 | 0 | 4 | This paper investigates E. coli transcription-coupled DNA repair (TCR) via in vivo/in vitro crosslinking mass  |
| [`10.1073/pnas.2422330122`](https://doi.org/10.1073/pnas.2422330122) | 0 | 1 | 0 | 0 | Cryo-EM structural paper on Mycobacterium tuberculosis UvrD1 dimers plus one E. coli UvrD mutant; it prints no |
| [`10.1371/journal.pone.0078141`](https://doi.org/10.1371/journal.pone.0078141) | 0 | 0 | 2 | 4 | This paper investigates direct physical and functional interactions between SF1A UvrD/PcrA helicases and RNA p |

**Explicit figure-only, SI-only, or access gaps (13):**

- FRET titration curves and relative FRET changes for DNA and nucleotide states ([`10.1016/j.jmb.2011.06.019`](https://doi.org/10.1016/j.jmb.2011.06.019)): figure only
- Quantitative percentages and emPAI values shown only inside figure panels (Fig. 1b inactivated EC36-39 %; Fig. 2a UvrC cleavage %; Fig. 2b % repair; Fig. 3 and Fig. 5b survival bars; Fig. 5a % runoff; Extended Data Fig. 1a emPAI values; Extended Data Fig. 9 arrest efficiency % vs UvrD concentration) ([`10.1038/nature12928`](https://doi.org/10.1038/nature12928)): figure only
- Supplementary Table 1 (in vivo and in vitro XLMS inter-protein crosslink lists) ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6)): in supplement not available
- Supplementary Table 2 (crystallographic data collection and refinement statistics for PDB 7EGS and 7EGT; bacterial strains/plasmids) ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6)): in supplement not available
- Supplementary Table 3 (oligonucleotides and strains/plasmids) ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6)): in supplement not available
- Time-course curves and percentage values plotted only in figures (Fig. 1b UvrD-RNAP binding fold-change post-UV; Fig. 3b fraction of inactivated EC26 over time; Extended Data Fig. 7a runoff %; Extended Data Fig. 7b UvrD WT vs ΔCTD ATPase time course) ([`10.1038/s41586-022-04530-6`](https://doi.org/10.1038/s41586-022-04530-6)): figure only
- Per-residue hetNOE, R1, S2 and Rex of UvrD-CTD ([`10.1038/s42003-020-01332-2`](https://doi.org/10.1038/s42003-020-01332-2)): figure only (Fig. 2a-e), no printed numbers
- R2beta profile, R2 and tau_c profiles ([`10.1038/s42003-020-01332-2`](https://doi.org/10.1038/s42003-020-01332-2)): Supplementary Fig. 4, not in text
- Dwell times and rates of open/closed switching, fluorophore positions ([`10.1126/science.aaa0130`](https://doi.org/10.1126/science.aaa0130)): in supplement not available; main text prints no kinetic rate for conformational switching
- File S1 (Supplementary Materials and Methods; Figures S1, S2, S3, S4; Table S1) ([`10.1371/journal.pone.0078141`](https://doi.org/10.1371/journal.pone.0078141)): in supplement not available (text file contains main article only; no supplement appended)
- Figure 2 SPR sensorgrams and binding response curves (and quantitative Kd/kinetic parameters) ([`10.1371/journal.pone.0078141`](https://doi.org/10.1371/journal.pone.0078141)): figure only (Discussion states only qualitative 'dissociation constant in the mid to high nanomolar range' without printed numeric Kd, kon, or koff)
- Figure 6 helicase unwinding timecourses (% DNA unwound vs time for GstPcrA and GstPcrAΔCt +/- RNAP) ([`10.1371/journal.pone.0078141`](https://doi.org/10.1371/journal.pone.0078141)): figure only (enzymatic DNA unwinding plots with no printed numeric rates in text)
- *... plus 1 additional gap entries in the `Gaps` tab.*

---
*Draft status: automated protein-level synthesis combining verified full-text extraction rows with Release 0.1 expert-reviewed calls where available. All `v3` rows await NMR specialist sign-off before promotion to Release 0.2.*
