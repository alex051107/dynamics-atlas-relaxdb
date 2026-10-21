# KRAS_CPMG: deposited structures between open 9OEL:A and closed 36OL:A

K-Ras4B 1-169 numbering (KRAS-J1 numbering_note; the N-terminal tag residue is 0 and is outside core and mobile). Mobile = Switch I 25-40 (Y32, T35, I36, E37, D38) and Switch II 57-76 (G60, Q61, E62, Y64, Y71); the P-loop 10-17 carries CPMG residues but its Calpha does not move between the two states and stays in the core; 36OL helix/strand records: helices 15-26, 61-66, 67-75, 86-105, 126-138, 151-168, strands 3-10, 37-46, 49-58, 77-83, 111-116, 141-143. The literature contrast is state 1 (open Switch I, T35 off the Mg2+/gamma-phosphate; GDP-like shifts, KRAS-r1) versus state 2 (T35 on the gamma-phosphate); the state-1 crystals the rows cite (6MBQ Mg-free GMPPNP, KRAS-r36; 6ASA/6ASE D33E/A59G, KRAS-r74/r75; 6BP1, KRAS-r76) and the WT references 4OBE (GDP) and 6GOD (GMPPNP) are all outside the 150 downloaded files, which are the newest 150 of 556 by release date (2025-07 onward). Within the downloaded set: 'open' = 9OEL chain A, wild type GDP.Mg at 298 K with no inhibitor or partner (the GDP state that state 1 resembles by chemical shift), 'closed' = 36OL chain A, wild type GMPPNP.Mg with no inhibitor or partner (state 2 expected; its paper was not read). The only downloaded structure deposited as state 1 is the NMR ensemble 9Q30 (T35S/C118S GppNHp, model 1 used), with 9Q2X/9Q2Z the G12D/G12C versions; T35S itself shows extra processes (KRAS-J20). The nucleotide (GDP, GNP = GppNHp, GCP = GppCH2p, GSP = GTPgammaS, GTP, AF3 transition-state mimic) is reported in its own column and is not a ligand: apo = nucleotide only, ligand-bound = plus a small-molecule inhibitor or fragment, complex = plus a protein partner (RAF RBD, CypA tri-complexes, SOS, PI3K, antibodies, VHL ternary complexes). The 556-entry metadata table (<ENTRY>_metadata_all.md) classifies every mapped entry by nucleotide, partner and mutation; the deposited mutation field is empty for many G12C/G12D/G13C entries, so a second column parses the title (regex X123Y) and is marked as such. T35 chi1 (N-CA-CB-OG1), Y32, Q61, Y64 and Y71 chi1 are listed per altloc.

| chain | class | ligands / partners | mutation | pH | T (K) | Å | RMSD open | RMSD closed | closure | cofactor | altloc (occ) | chi1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9OEL:A | apo | - (MG) | - | - | 298.0 | 1.5 | 0.0 | 3.21 | 0.0 | GDP | base | Y32:t(+180); T35:g+(+70); Q61:g-(-67); Y64:g-(-55); Y71:g+(+75) |
| 9OEX:A | apo | - (MG) | G12V | - | 298.0 | 1.5 | 0.09 | 3.23 | 0.03 | GDP | base | Y32:t(-178); T35:g+(+68); Q61:g-(-63); Y64:g-(-54); Y71:g+(+75) |
| 9OEL:B | apo | - (MG) | - | - | 298.0 | 1.5 | 0.14 | 3.2 | 0.04 | GDP | base | Y32:t(-178); T35:g+(+69); Q61:g-(-67); Y64:g-(-55); Y71:g+(+75) |
| 9OEX:B | apo | - (MG) | G12V | - | 298.0 | 1.5 | 0.18 | 3.21 | 0.05 | GDP | base | Y32:t(-178); T35:g+(+68); Q61:g-(-65); Y64:g-(-56); Y71:g+(+79) |
| 11FT:A | apo | - (MG) | G12C,Q99L,C118S | - | 100.0 | 1.16 | 0.52 | 3.28 | 0.14 | GDP | base | Y32:t(-171); T35:g+(+67); Q61:g-(-61); Y64:g-(-62); Y71:g+(+76) |
| 11FT:A:B | apo | - (MG) | G12C,Q99L,C118S | - | 100.0 | 1.16 | 0.53 | 3.28 | 0.14 | GDP | B (0.44) | Y32:t(-171); T35:g+(+67); Q61:g-(-61); Y64:g-(-62); Y71:g+(+76) |
| 11FU:A | apo | - (MG) | G12C, R68S, C118S | - | 100.0 | 1.65 | 0.77 | 1.99 | 0.28 | GDP | base | Y32:t(-168); T35:g+(+68); Y71:g+(+66) |
| 11FU:A:B | apo | - (MG) | G12C, R68S, C118S | - | 100.0 | 1.65 | 0.77 | 1.99 | 0.28 | GDP | B (0.44) | Y32:t(-168); T35:g+(+68); Y71:g+(+66) |
| 9TBM:A | apo | - (MG) | G12D | 9.0 | 100.0 | 1.6 | 0.62 | 1.57 | 0.28 | GDP | base | Y32:t(-172); T35:g+(+64) |
| 9TBM:A:B | apo | - (MG) | G12D | 9.0 | 100.0 | 1.6 | 0.62 | 1.57 | 0.28 | GDP | B (0.5) | Y32:t(-172); T35:g+(+64) |
| 9C3Z:B | apo | - (MG) | G12D, G60R | - | 100.0 | 1.8 | 0.79 | 1.68 | 0.32 | GDP | base | Y32:t(-171); T35:g+(+68) |
| 9C41:B | apo | - (MG) | G12D, E62Q | - | 100.0 | 1.94 | 1.05 | 2.22 | 0.32 | GDP | base | Y32:t(-172); T35:g+(+76) |
| 9TBM:C | apo | - (MG) | G12D | 9.0 | 100.0 | 1.6 | 0.69 | 1.43 | 0.33 | GDP | base | T35:g+(+73) |
| 11FU:B | apo | - (MG) | G12C, R68S, C118S | - | 100.0 | 1.65 | 0.97 | 1.71 | 0.36 | GDP | base | Y32:t(-161); T35:g+(+70); Y71:g+(+74) |
| 9C3K:A | apo | - (MG) | G12D, M67R | - | 100.0 | 1.7 | 1.14 | 1.87 | 0.38 | GDP | base | Y32:t(-166); T35:g+(+65); Y71:t(-158) |
| 9C3R:B | apo | - | G12D, V45E | - | 100.0 | 2.2 | 1.57 | 2.56 | 0.38 | GDP | base | Y32:t(-169); T35:g+(+65); Y71:g-(-90) |
| 9I7Y:A | ligand-bound | A1I08 (MG) | - | - | 100.0 | 1.85 | 1.27 | 2.04 | 0.38 | none | base | Y32:t(-170); T35:g+(+87); Y71:g-(-110) |
| 9N44:A | ligand-bound | A1BV7 (MG) | G12C | - | 100.0 | 1.11 | 2.26 | 3.65 | 0.38 | GDP | base | Y32:t(-162); T35:g+(+71); Q61:g-(-69); Y64:g-(-69); Y71:t(-171) |
| 9N44:A:B | ligand-bound | A1BV7 (MG) | G12C | - | 100.0 | 1.11 | 2.26 | 3.65 | 0.38 | GDP | B (0.5) | Y32:t(-162); T35:g+(+71); Q61:g-(-69); Y64:g-(-69); Y71:t(-171) |
| 9OU0:B | ligand-bound | 6IC (MG) | G12D, C51S, C80L, C118S | - | 100.0 | 1.81 | 2.19 | 3.58 | 0.38 | GDP | base | Y32:t(-175); T35:g+(+75); Q61:g-(-60); Y64:g-(-60); Y71:t(-163) |
| 9OUI:B | ligand-bound | 6IC (MG) | G12D, C51S, C80L, C118S | - | 313.0 | 1.86 | 2.19 | 3.55 | 0.38 | GDP | base | Y32:t(-176); T35:g+(+71); Q61:t(-148); Y64:g-(-61); Y71:t(-162) |
| 9OUJ:B | ligand-bound | 6IC (MG) | G12D, C51S, C80L, C118S | - | 310.0 | 1.89 | 2.18 | 3.56 | 0.38 | GDP | base | Y32:t(-178); T35:g+(+73); Q61:g-(-66); Y64:g-(-60); Y71:t(-160) |
| 9PIZ:A | complex | A1CII, anti-KRAS light chain, anti-KRAS heavy chain (MG) | G12C | - | 93.0 | 1.94 | 2.27 | 3.69 | 0.38 | GDP | base | Y32:t(-172); T35:g+(+77); Q61:g+(+58); Y64:g-(-56); Y71:t(-152) |
| 9PZF:A | ligand-bound | A1CQ2 (MG) | G12C variant, C51S, C80L, C118S | - | 93.0 | 1.84 | 2.25 | 3.64 | 0.38 | GDP | base | Y32:t(-157); T35:g+(+70); Q61:g-(-72); Y64:g-(-58); Y71:t(-151) |
| 9RK8:H | complex | von Hippel-Lindau disease tumor suppressor, Elongin-C, Elongin-B (MG) | - | - | 100.0 | 2.63 | 2.18 | 3.58 | 0.38 | GDP | base | Y32:t(-165); T35:g+(+41); Y64:g-(-59); Y71:t(-167) |
| 9U41:A | ligand-bound | A1EN1 (MG) | - | 6.0 | 100.0 | 1.22 | 2.43 | 3.98 | 0.38 | GDP | base | Y32:t(-162); T35:g+(+71); Q61:g-(-78); Y64:g-(-60); Y71:t(-177) |
| 9U45:A | ligand-bound | A1EN2 (MG) | G12D | 6.0 | 100.0 | 1.36 | 2.43 | 3.98 | 0.38 | GDP | base | Y32:t(-173); T35:g+(+70); Q61:g-(-86); Y64:g-(-61); Y71:t(-178) |
| 9U8J:A | ligand-bound | 6IC (MG) | G12D,Y96D | - | 100.0 | 1.34 | 2.18 | 3.5 | 0.38 | GDP | base | Y32:t(-172); T35:g+(+70); Q61:g-(-63); Y64:g-(-61); Y71:t(-161) |
| 9U8J:A:B | ligand-bound | 6IC (MG) | G12D,Y96D | - | 100.0 | 1.34 | 2.18 | 3.49 | 0.38 | GDP | B (0.41) | Y32:t(-172); T35:g+(+70); Q61:g-(-63); Y64:g-(-61); Y71:t(-161) |
| 10NU:B | ligand-bound | A1C6Y (CA) | G12C; C51S; C80L; C118S | 8.5 | 100.0 | 1.5 | 2.34 | 3.64 | 0.39 | GDP | base | Y32:t(-164); T35:g+(+70); Q61:g-(-58); Y64:g-(-63); Y71:t(-171) |
| 10NU:B:B | ligand-bound | A1C6Y (CA) | G12C; C51S; C80L; C118S | 8.5 | 100.0 | 1.5 | 2.34 | 3.64 | 0.39 | GDP | B (0.54) | Y32:t(-164); T35:g+(+70); Q61:g-(-58); Y64:g-(-63); Y71:t(-171) |
| 10NV:B | ligand-bound | A1C60 (CA) | G12C; C51S; C80L; C118S | 8.5 | 100.0 | 1.52 | 2.35 | 3.65 | 0.39 | GDP | base | Y32:t(-163); T35:g+(+72); Q61:g-(-63); Y64:g-(-65); Y71:t(-172) |
| 12UW:B | ligand-bound | A1DEM (MG) | Q61K | 7.5 | 100.0 | 2.05 | 2.34 | 3.66 | 0.39 | GDP | base | Y32:t(-163); T35:g+(+61); Y64:g-(-64); Y71:t(-163) |
| 9C40:A | apo | - (MG) | G12D, V103Y | - | 100.0 | 1.8 | 2.59 | 4.03 | 0.39 | GDP | base | Y32:t(-162); T35:g+(+78); Y71:g-(-88) |
| 9IAP:A | ligand-bound | A1I1P (MG) | - | - | 100.0 | 1.182 | 2.39 | 3.67 | 0.39 | GDP | base | Y32:t(-161); T35:g+(+72); Q61:g-(-105); Y64:g-(-57); Y71:t(-172) |
| 9IAP:A:B | ligand-bound | A1I1P (MG) | - | - | 100.0 | 1.182 | 2.39 | 3.67 | 0.39 | GDP | B (0.68) | Y32:t(-161); T35:g+(+72); Q61:g-(-105); Y64:g-(-57); Y71:t(-172) |
| 9IAW:A | ligand-bound | A1I1R (MG) | - | - | 100.0 | 0.997 | 2.36 | 3.64 | 0.39 | GDP | base | Y32:t(-162); T35:g+(+72); Q61:g-(-66); Y64:g-(-58); Y71:t(-175) |
| 9IAW:A:B | ligand-bound | A1I1R (MG) | - | - | 100.0 | 0.997 | 2.36 | 3.64 | 0.39 | GDP | B (0.49) | Y32:t(-162); T35:g+(+72); Q61:g-(-66); Y64:g-(-58); Y71:t(-175) |
| 9IB4:A | ligand-bound | A1I1Z (MG) | - | - | 100.0 | 1.062 | 2.36 | 3.66 | 0.39 | GDP | base | Y32:t(-164); T35:g+(+75); Q61:g-(-74); Y64:g-(-62); Y71:t(-169) |
| 9IB5:A | ligand-bound | VU6 (MG) | - | - | 100.0 | 1.011 | 2.38 | 3.74 | 0.39 | GDP | base | Y32:t(-160); T35:g+(+73); Q61:g-(-52); Y64:g-(-60); Y71:t(-178) |
| 9IB5:A:B | ligand-bound | VU6 (MG) | - | - | 100.0 | 1.011 | 2.38 | 3.74 | 0.39 | GDP | B (0.48) | Y32:t(-160); T35:g+(+73); Q61:g-(-52); Y64:g-(-60); Y71:t(-178) |
| 9KFL:A | complex | TIG3 peptide (MG) | G12V | - | 100.0 | 3.45 | 2.67 | 4.17 | 0.39 | GDP | base | Y32:t(+173); T35:g+(+67); Q61:g-(-61); Y64:t(+140); Y71:g-(-98) |
| 9NF2:A | ligand-bound | 6IC (MG) | G12D, C51S, C80L, C118S | - | 298.0 | 1.7 | 2.24 | 3.45 | 0.39 | none | base | Y32:t(-178); T35:g+(+63); Q61:t(-150); Y64:g-(-64); Y71:t(-160) |
| 9NF2:A:B | ligand-bound | 6IC (MG) | G12D, C51S, C80L, C118S | - | 298.0 | 1.7 | 2.24 | 3.45 | 0.39 | none | B (0.38) | Y32:t(-178); T35:g+(+63); Q61:t(-150); Y64:g-(-64); Y71:t(-160) |
| 9O0N:A | ligand-bound | 6IC (MG) | - | 4.5 | 100.0 | 1.4 | 2.19 | 3.44 | 0.39 | GDP | base | Y32:t(-170); T35:g+(+68); Q61:g-(-78); Y64:g-(-64); Y71:t(-158) |
| 9OUI:A | ligand-bound | 6IC (MG) | G12D, C51S, C80L, C118S | - | 313.0 | 1.86 | 2.25 | 3.45 | 0.39 | GDP | base | Y32:t(-174); T35:g+(+71); Q61:t(-145); Y64:g-(-61); Y71:t(-162) |
| 9P44:A | ligand-bound | A1CG4 (MG) | G12D, C118S | - | 100.0 | 1.7 | 2.37 | 3.66 | 0.39 | GDP | base | Y32:t(-169); T35:g+(+71); Q61:g-(-64); Y64:g-(-61); Y71:t(-166) |
| 9P44:B | ligand-bound | A1CG4 (MG) | G12D, C118S | - | 100.0 | 1.7 | 2.39 | 3.68 | 0.39 | GDP | base | Y32:t(-160); T35:g+(+80); Q61:g-(-71); Y64:g-(-60); Y71:t(-171) |
| 9PZF:B | ligand-bound | A1CQ2 (MG) | G12C variant, C51S, C80L, C118S | - | 93.0 | 1.84 | 2.28 | 3.64 | 0.39 | GDP | base | Y32:t(-166); T35:g+(+67); Q61:g-(-72); Y64:g-(-59); Y71:g-(-87) |
| 9PZY:B | ligand-bound | A1AWR (MG) | G12C variant | - | 93.0 | 2.17 | 2.33 | 3.65 | 0.39 | GDP | base | Y32:t(-158); T35:g+(+73); Y64:g-(-60); Y71:t(-173) |
| 9PZY:B:B | ligand-bound | A1AWR (MG) | G12C variant | - | 93.0 | 2.17 | 2.33 | 3.65 | 0.39 | GDP | B (0.76) | Y32:t(-158); T35:g+(+73); Y64:g-(-60); Y71:t(-173) |
| 9RKC:D | complex | A1JHI, von Hippel-Lindau disease tumor suppressor, Elongin-C, Elongin-B (MG) | - | - | 100.0 | 2.19 | 2.25 | 3.49 | 0.39 | GDP | base | Y32:t(-164); T35:g-(-72); Q61:t(-160); Y64:g-(-58); Y71:t(-163) |
| 9RKC:H | complex | A1JHI, von Hippel-Lindau disease tumor suppressor, Elongin-C, Elongin-B (MG) | - | - | 100.0 | 2.19 | 2.24 | 3.54 | 0.39 | GDP | base | Y32:t(-170); T35:g+(+63); Q61:t(-164); Y64:g-(-59); Y71:t(-166) |
| 9TC6:A | ligand-bound | A1JU2 (MG) | G12D | 9.0 | 100.0 | 1.63 | 2.31 | 3.64 | 0.39 | GDP | base | Y32:t(-171); T35:g+(+56); Q61:t(-179); Y64:g-(-57); Y71:t(-172) |
| 9TC6:A:B | ligand-bound | A1JU2 (MG) | G12D | 9.0 | 100.0 | 1.63 | 2.31 | 3.64 | 0.39 | GDP | B (0.5) | Y32:t(-171); T35:g+(+56); Q61:t(-179); Y64:g-(-57); Y71:t(-172) |
| 9U3Z:A | ligand-bound | A1ENW (MG) | G12D | 6.0 | 100.0 | 2.60033089206 | 2.37 | 3.77 | 0.39 | GDP | base | Y32:t(-172); T35:g-(-85); Q61:g+(+82); Y64:g-(-57); Y71:t(+180) |
| 9U5T:A | ligand-bound | A1EN3 (MG) | - | 8.5 | 100.0 | 1.8 | 2.28 | 3.55 | 0.39 | GDP | base | Y32:t(-170); T35:g+(+74); Q61:g-(-51); Y64:g-(-57); Y71:t(-168) |
| 9U5T:A:B | ligand-bound | A1EN3 (MG) | - | 8.5 | 100.0 | 1.8 | 2.28 | 3.55 | 0.39 | GDP | B (0.5) | Y32:t(-170); T35:g+(+74); Q61:g-(-51); Y64:g-(-57); Y71:t(-168) |
| 9U8L:A | ligand-bound | 6IC (MG) | G12D,Y96S | - | 100.0 | 1.23 | 2.21 | 3.44 | 0.39 | GDP | base | Y32:t(-175); T35:g+(+72); Q61:g-(-51); Y64:g-(-64); Y71:t(-168) |
| 9U8T:A | ligand-bound | 6IC (MG) | G12D,R68M | - | 100.0 | 1.4 | 2.14 | 3.42 | 0.39 | GDP | base | Y32:t(-174); T35:g+(+74); Q61:g-(-66); Y64:g-(-61); Y71:t(-169) |
| 9U8U:A | ligand-bound | 6IC (MG) | G12D,Q61H | - | 100.0 | 1.32 | 2.24 | 3.55 | 0.39 | GDP | base | Y32:t(-172); T35:g+(+72); H61:g-(-67); Y64:g-(-61); Y71:t(-164) |
| 9U90:A | apo | - (MG) | G12D,E62K | - | 100.0 | 1.2 | 2.36 | 3.68 | 0.39 | GDP | base | Y32:t(-161); T35:g+(+75); Q61:g-(-76); Y64:g-(-57); Y71:g-(-83) |
| 9U95:A | ligand-bound | 6IC (MG) | G12D,Q99L | - | 100.0 | 1.75 | 2.25 | 3.48 | 0.39 | GDP | base | Y32:t(-168); T35:g+(+71); Q61:g-(-69); Y64:g-(-60); Y71:t(-166) |
| 9XZ1:B | complex | A1CRY, Heat shock protein HSP 90-alpha (MG) | - | 6.5 | 100.0 | 1.96 | 2.28 | 3.59 | 0.39 | GDP | base | Y32:t(-175); T35:g+(+62); Q61:g+(+63); Y64:g-(-53); Y71:t(-173) |
| 12UW:A | ligand-bound | A1DEM (MG) | Q61K | 7.5 | 100.0 | 2.05 | 2.34 | 3.47 | 0.4 | GDP | base | Y32:t(-161); T35:g+(+72); K61:g+(+62); Y64:g-(-62); Y71:t(-165) |
| 12UW:A:B | ligand-bound | A1DEM (MG) | Q61K | 7.5 | 100.0 | 2.05 | 2.34 | 3.47 | 0.4 | GDP | B (0.48) | Y32:t(-161); T35:g+(+72); K61:g+(+62); Y64:g-(-62); Y71:t(-165) |
| 12XE:A | ligand-bound | A1DEM (MG) | Q61K | - | 100.0 | 1.01 | 2.23 | 3.36 | 0.4 | GNP | base | Y32:t(-172); T35:g+(+70); K61:g-(-62); Y64:g-(-61); Y71:t(-165) |
| 9C3N:B | apo | - (MG) | G12D, P34R | - | 100.0 | 1.5 | 1.32 | 1.98 | 0.4 | GDP | base | Y32:t(-175); T35:g+(+71) |
| 9C3R:A | apo | - (MG) | G12D, V45E | - | 100.0 | 2.2 | 1.78 | 2.68 | 0.4 | GDP | base | Y32:t(-165); T35:g+(+65); Y71:g-(-86) |
| 9C3V:B | apo | - (MG) | G12D, D54R | - | 100.0 | 2.51 | 1.34 | 2.01 | 0.4 | GDP | base | Y32:t(-154); T35:g+(+61) |
| 9C41:A | apo | - (MG) | G12D, E62Q | - | 100.0 | 1.94 | 2.96 | 4.47 | 0.4 | GDP | base | Y32:t(-172); T35:g+(+76); Q61:g-(-62); Y64:t(+167); Y71:g-(-84) |
| 9C43:A | apo | - (MG) | G12D, E3K | - | 100.0 | 1.87 | 2.9 | 4.33 | 0.4 | GDP | base | Y32:t(-177); T35:g+(+77); Q61:g-(-59); Y64:t(+166); Y71:g-(-85) |
| 9C43:B | apo | - | G12D, E3K | - | 100.0 | 1.87 | 1.81 | 2.68 | 0.4 | GDP | base | Y32:t(-165); T35:g+(+64); Q61:g-(-52) |
| 9NZM:A | ligand-bound | A1B7P (MG) | G12C, C51S, C80L, C121S | 6.5 | 100.0 | 1.586 | 2.47 | 3.7 | 0.4 | GNP | base | Q61:g-(-69); Y64:g-(-58); Y71:g-(-90) |
| 9NZM:A:B | ligand-bound | A1B7P (MG) | G12C, C51S, C80L, C121S | 6.5 | 100.0 | 1.586 | 2.47 | 3.69 | 0.4 | GNP | B (0.46) | Q61:g-(-69); Y64:g-(-58); Y71:g-(-90) |
| 9NZN:A | ligand-bound | A1B7Q (MG) | - | 4.6 | 100.0 | 1.504 | 2.21 | 3.36 | 0.4 | GDP | base | Y32:t(-173); T35:g+(+68); Q61:g-(-60); Y64:g-(-61); Y71:t(-172) |
| 9NZN:A:B | ligand-bound | A1B7Q (MG) | - | 4.6 | 100.0 | 1.504 | 2.21 | 3.36 | 0.4 | GDP | B (0.4) | Y32:t(-173); T35:g+(+68); Q61:g-(-60); Y64:g-(-61); Y71:t(-172) |
| 9O0O:A | ligand-bound | 6IC (MG) | - | 6.0 | 100.0 | 1.9 | 2.42 | 3.56 | 0.4 | GNP | base | Y32:g-(-62); T35:g-(-48); Q61:g-(-57); Y64:g-(-59); Y71:t(-167) |
| 9OU0:A | ligand-bound | 6IC (MG) | G12D, C51S, C80L, C118S | - | 100.0 | 1.81 | 2.28 | 3.49 | 0.4 | GDP | base | Y32:t(-174); T35:g+(+75); Q61:g-(-66); Y64:g-(-60); Y71:t(-166) |
| 9OU2:A | ligand-bound | OFU (MG) | - | 4.6 | 100.0 | 1.55 | 2.36 | 3.49 | 0.4 | GDP | base | Y32:t(-165); T35:g+(+69); Q61:g-(-59); Y64:g-(-56); Y71:t(-166) |
| 9OU3:A | ligand-bound | OFU (MG) | - | 4.6 | 293.0 | 1.5 | 2.37 | 3.51 | 0.4 | GDP | base | Y32:t(-164); T35:g+(+69); Q61:g-(-48); Y64:g-(-58); Y71:t(-166) |
| 9OU3:A:B | ligand-bound | OFU (MG) | - | 4.6 | 293.0 | 1.5 | 2.37 | 3.51 | 0.4 | GDP | B (0.35) | Y32:t(-164); T35:g+(+69); Q61:g-(-48); Y64:g-(-58); Y71:t(-166) |
| 9OU4:A | ligand-bound | OFU (MG) | - | - | 313.0 | 1.89 | 2.39 | 3.58 | 0.4 | GDP | base | Y32:t(-160); T35:g+(+74); Q61:g+(+60); Y64:g-(-56); Y71:t(-163) |
| 9OUJ:A | ligand-bound | 6IC (MG) | G12D, C51S, C80L, C118S | - | 310.0 | 1.89 | 2.28 | 3.48 | 0.4 | GDP | base | Y32:t(-176); T35:g+(+74); Q61:g-(-68); Y64:g-(-62); Y71:t(-159) |
| 9PZY:A | ligand-bound | A1AWR (MG) | G12C variant | - | 93.0 | 2.17 | 2.36 | 3.6 | 0.4 | GDP | base | Y32:t(-166); T35:g+(+71); Q61:g+(+75); Y64:g-(-61); Y71:t(-159) |
| 9PZY:A:B | ligand-bound | A1AWR (MG) | G12C variant | - | 93.0 | 2.17 | 2.36 | 3.6 | 0.4 | GDP | B (0.55) | Y32:t(-166); T35:g+(+71); Q61:g+(+75); Y64:g-(-61); Y71:t(-159) |
| 9RK8:D | complex | von Hippel-Lindau disease tumor suppressor, Elongin-C, Elongin-B (MG) | - | - | 100.0 | 2.63 | 2.3 | 3.46 | 0.4 | GDP | base | Y32:t(-159); T35:g-(-41); Q61:t(-152); Y64:g-(-58); Y71:t(-166) |
| 9TBR:A | ligand-bound | A1JU6 (MG) | - | 9.0 | 100.0 | 1.65 | 2.33 | 3.55 | 0.4 | GDP | base | Y32:t(-172); T35:g+(+53); Q61:g-(-59); Y64:g-(-58); Y71:t(-170) |
| 9TBR:A:B | ligand-bound | A1JU6 (MG) | - | 9.0 | 100.0 | 1.65 | 2.33 | 3.55 | 0.4 | GDP | B (0.5) | Y32:t(-172); T35:g+(+53); Q61:g-(-59); Y64:g-(-58); Y71:t(-170) |
| 9TBW:A | ligand-bound | A1JU7 (CA,MG) | G12D | 9.0 | 100.0 | 1.54 | 2.33 | 3.5 | 0.4 | GDP | base | Y32:t(+178); T35:g+(+76); Q61:g-(-65); Y64:g-(-54); Y71:t(-176) |
| 9TC2:A | ligand-bound | A1JU3 (CA,MG) | G12D | 5.5 | 100.0 | 1.3 | 2.36 | 3.49 | 0.4 | GDP | base | Y32:t(-177); T35:g+(+69); Q61:g-(-55); Y64:g-(-55); Y71:t(-174) |
| 9TC2:A:B | ligand-bound | A1JU3 (CA,MG) | G12D | 5.5 | 100.0 | 1.3 | 2.36 | 3.49 | 0.4 | GDP | B (0.5) | Y32:t(-177); T35:g+(+69); Q61:g-(-55); Y64:g-(-55); Y71:t(-174) |
| 9TC5:A | ligand-bound | A1JU9 (MG) | G12D | 5.5 | 100.0 | 1.35 | 2.37 | 3.52 | 0.4 | GDP | base | Y32:t(-178); T35:g+(+68); Q61:g-(-62); Y64:g-(-54); Y71:t(-172) |
| 9TC5:A:B | ligand-bound | A1JU9 (MG) | G12D | 5.5 | 100.0 | 1.35 | 2.37 | 3.52 | 0.4 | GDP | B (0.5) | Y32:t(-178); T35:g+(+68); Q61:g-(-62); Y64:g-(-54); Y71:t(-172) |
| 9U50:A | ligand-bound | A1EN3 (MG) | - | 8.5 | 100.0 | 1.87 | 2.27 | 3.36 | 0.4 | GDP | base | Y32:t(-163); T35:g+(+61); Q61:g-(-61); Y64:g-(-53); Y71:t(-164) |
| 9U50:B | ligand-bound | A1EN3 (MG) | - | 8.5 | 100.0 | 1.87 | 2.31 | 3.42 | 0.4 | GDP | base | Y32:t(-179); T35:g+(+63); Q61:g-(-72); Y64:g-(-58); Y71:t(-157) |
| 9U50:C | ligand-bound | A1EN3 (MG) | - | 8.5 | 100.0 | 1.87 | 2.44 | 3.62 | 0.4 | GDP | base | T35:g+(+43); Q61:g-(-54); Y64:g-(-58); Y71:t(-173) |
| 9U95:B | ligand-bound | 6IC (MG) | G12D,Q99L | - | 100.0 | 1.75 | 2.37 | 3.52 | 0.4 | GDP | base | Y32:t(-176); T35:g+(+65); Q61:g-(-65); Y64:g-(-58); Y71:t(-170) |
| 9U97:A | ligand-bound | 6IC (MG) | G12D,G13D | - | 100.0 | 1.79 | 2.38 | 3.5 | 0.4 | GDP | base | Y32:t(+165); T35:g+(+68); Q61:g-(-47); Y64:g-(-59); Y71:t(-174) |
| 9U97:A:B | ligand-bound | 6IC (MG) | G12D,G13D | - | 100.0 | 1.79 | 2.38 | 3.5 | 0.4 | GDP | B (0.49) | Y32:t(+165); T35:g+(+68); Q61:g-(-47); Y64:g-(-59); Y71:t(-174) |
| 9U99:C | ligand-bound | 6IC (MG) | G12D,E62K | - | 100.0 | 2.5 | 2.25 | 3.33 | 0.4 | GDP | base | Y32:t(-164); T35:g+(+74); Q61:g-(-42); Y64:t(+167); Y71:t(-166) |
| 9U99:D | ligand-bound | 6IC (MG) | G12D,E62K | - | 100.0 | 2.5 | 2.23 | 3.35 | 0.4 | GDP | base | Y32:t(-172); T35:g+(+53); Q61:g+(+45); Y64:t(+166); Y71:t(-166) |
| 9USB:A | ligand-bound | A1EN3 (MG) | - | 8.5 | 100.0 | 2.35 | 2.28 | 3.36 | 0.4 | GNP | base | Y32:t(-166); T35:g+(+66); Q61:g-(-60); Y64:g-(-51); Y71:t(-165) |
| 9XB7:A | ligand-bound | A1EZH (MG) | G12R | - | 100.0 | 1.36 | 2.31 | 3.44 | 0.4 | GDP | base | Y32:t(-177); T35:g+(+71); Q61:g-(-65); Y64:g-(-54); Y71:t(+178) |
| 9YMN:A | ligand-bound | A1CZE (MG) | G12D, C118A | - | 100.0 | 1.25 | 2.53 | 3.78 | 0.4 | GDP | base | Y32:t(-179); T35:g+(+64); Q61:g-(-62); Y64:g-(-56); Y71:t(-165) |
| 9ZPE:A | ligand-bound | A1C3O (MG) | G12V, C51S, C80L, C118S | 4.6 | 100.0 | 1.91 | 2.3 | 3.42 | 0.4 | GDP | base | Y32:t(-172); T35:g+(+65); Q61:g-(-52,A,0.46)/g-(-80,B,0.54); Y64:g-(-56); Y71:t(-161) |
| 9ZPE:A:B | ligand-bound | A1C3O (MG) | G12V, C51S, C80L, C118S | 4.6 | 100.0 | 1.91 | 2.3 | 3.42 | 0.4 | GDP | B (0.54) | Y32:t(-172); T35:g+(+65); Q61:g-(-80); Y64:g-(-56); Y71:t(-161) |
| 10JT:B | ligand-bound | A1C5K (CA) | - | 7.5 | 100.0 | 1.489 | 2.45 | 3.51 | 0.41 | GDP | base | Y32:t(-167); T35:g+(+77); Q61:g-(-73); Y64:g-(-55); Y71:t(-169) |
| 10JT:B:B | ligand-bound | A1C5K (CA) | - | 7.5 | 100.0 | 1.489 | 2.45 | 3.51 | 0.41 | GDP | B (0.5) | Y32:t(-167); T35:g+(+77); Q61:g-(-73); Y64:g-(-55); Y71:t(-169) |
| 10NV:A | ligand-bound | A1C60 (CA) | G12C; C51S; C80L; C118S | 8.5 | 100.0 | 1.52 | 2.54 | 3.71 | 0.41 | GDP | base | Y32:t(-163); T35:g+(+69); Q61:g-(-72); Y64:g-(-59); Y71:t(-177) |
| 11ES:A | apo | - (MG) | G12C, H95Q, C118S | - | 100.0 | 1.35 | 2.36 | 3.34 | 0.41 | GDP | base | Y32:t(-167); T35:g+(+73); Y71:g-(-86) |
| 11ES:A:B | apo | - (MG) | G12C, H95Q, C118S | - | 100.0 | 1.35 | 2.36 | 3.34 | 0.41 | GDP | B (0.44) | Y32:t(-167); T35:g+(+73); Y71:g-(-86) |
| 9C3K:B | apo | - (MG) | G12D, M67R | - | 100.0 | 1.7 | 2.04 | 2.89 | 0.41 | GDP | base | Y32:t(-165); T35:g+(+66) |
| 9C3N:A | apo | - (MG) | G12D, P34R | - | 100.0 | 1.5 | 2.97 | 4.33 | 0.41 | GDP | base | Y32:t(-174); T35:g+(+79); Q61:g-(-62); Y64:t(+167); Y71:g-(-84) |
| 9C40:B | apo | - (MG) | G12D, V103Y | - | 100.0 | 1.8 | 2.07 | 3.01 | 0.41 | GDP | base | Y32:t(-169); T35:g+(+66); Q61:t(+167); Y71:g-(-70) |
| 9I5E:A | complex | M1X, Nanobody 26 (MG) | - | - | - | 3.77 | 2.68 | 3.86 | 0.41 | GDP | base | Y32:t(-145); T35:g-(-33); Q61:g+(+78); Y64:t(-155); Y71:t(-166) |
| 9I5E:B | complex | M1X, Nanobody 26 (MG) | - | - | - | 3.77 | 2.71 | 3.86 | 0.41 | GDP | base | Y32:t(-145); T35:g-(-33); Q61:g+(+79); Y64:g-(-114); Y71:t(-166) |
| 9IAY:A | ligand-bound | WYU (MG) | - | - | 100.0 | 0.953 | 2.45 | 3.56 | 0.41 | GDP | base | Y32:t(-165); T35:g+(+73); Q61:g+(+73); Y64:g-(-54); Y71:t(-176) |
| 9IAY:A:B | ligand-bound | WYU (MG) | - | - | 100.0 | 0.953 | 2.45 | 3.56 | 0.41 | GDP | B (0.42) | Y32:t(-165); T35:g+(+73); Q61:g+(+73); Y64:g-(-54); Y71:t(-176) |
| 9KFL:H | complex | TIG3 peptide (MG) | G12V | - | 100.0 | 3.45 | 2.95 | 4.3 | 0.41 | GDP | base | Y32:t(-173); T35:g+(+63); Q61:g-(-52); Y64:t(+138); Y71:g-(-104) |
| 9KFL:K | complex | TIG3 peptide (MG) | G12V | - | 100.0 | 3.45 | 3.21 | 4.64 | 0.41 | GDP | base | Y32:t(-179); T35:g+(+59); Q61:g-(-59); Y64:t(+135); Y71:g-(-100) |
| 9RKN:H | complex | A1JHI, von Hippel-Lindau disease tumor suppressor, Elongin-C, Elongin-B (MG) | - | - | 100.0 | 2.85 | 2.56 | 3.74 | 0.41 | GCP | base | Y64:g-(-60); Y71:t(-167) |
| 9TBM:B | ligand-bound | A1JU5 (MG) | G12D | 9.0 | 100.0 | 1.6 | 2.33 | 3.42 | 0.41 | GDP | base | Y32:t(+175); T35:g+(+67); Q61:g-(-59); Y64:g-(-57); Y71:t(-165) |
| 9TBM:B:B | ligand-bound | A1JU5 (MG) | G12D | 9.0 | 100.0 | 1.6 | 2.33 | 3.42 | 0.41 | GDP | B (0.5) | Y32:t(+175); T35:g+(+67); Q61:g-(-59); Y64:g-(-57); Y71:t(-165) |
| 9U8Z:A | apo | - (MG) | G12D,Q61H | - | 100.0 | 1.2 | 2.35 | 3.4 | 0.41 | GDP | base | Y32:t(-173); T35:g+(+77); H61:g-(-52); Y71:g-(-84) |
| 9U99:A | ligand-bound | 6IC (MG) | G12D,E62K | - | 100.0 | 2.5 | 2.34 | 3.33 | 0.41 | GDP | base | Y32:t(+180); T35:g+(+57); Q61:t(+178); Y64:t(+157); Y71:g+(+57) |
| 9U99:B | ligand-bound | 6IC (MG) | G12D,E62K | - | 100.0 | 2.5 | 2.28 | 3.31 | 0.41 | GDP | base | Y32:t(-171); T35:g+(+69); Q61:g-(-50); Y64:t(+178); Y71:t(-165) |
| 9USB:C | ligand-bound | A1EN3 (MG) | - | 8.5 | 100.0 | 2.35 | 2.34 | 3.37 | 0.41 | GNP | base | Y32:t(-179); T35:g+(+71); Q61:g-(-37); Y64:g-(-54); Y71:t(-160) |
| 9XAM:A | ligand-bound | A1EZH (MG) | G12D | - | 100.0 | 1.23 | 2.44 | 3.44 | 0.41 | GDP | base | Y32:t(-167); T35:g+(+68); Q61:g-(-63); Y64:g-(-54); Y71:t(-175) |
| 9XB3:A | ligand-bound | A1EZK (MG) | G12D | - | 100.0 | 1.32 | 2.41 | 3.48 | 0.41 | GDP | base | Y32:t(-173); T35:g+(+68); Q61:g-(-57); Y64:g-(-54); Y71:t(-177) |
| 9XBZ:A | ligand-bound | A1EZK (MG) | G12R | - | 100.0 | 1.34 | 2.4 | 3.43 | 0.41 | GDP | base | Y32:t(-174); T35:g+(+67); Q61:g-(-60); Y64:g-(-51); Y71:t(-177) |
| 9XF7:A | ligand-bound | A1EZH (MG) | G12V | - | 100.0 | 1.34 | 2.41 | 3.46 | 0.41 | GDP | base | Y32:t(-168); T35:g+(+71); Q61:g-(-64); Y64:g-(-56); Y71:t(-176) |
| 9YMP:A | ligand-bound | A1AG3 (MG) | G12D, C118A | 4.6 | 100.0 | 1.12 | 2.31 | 3.29 | 0.41 | GCP | base | T35:g+(+68); Q61:g-(-49); Y64:g-(-62); Y71:t(-167) |
| 9YMR:A | ligand-bound | A1AG3 (MG) | G12V variant, C118A | 4.6 | 100.0 | 1.2 | 2.34 | 3.33 | 0.41 | GCP | base | Y32:g-(-52); T35:g+(+72); Q61:g-(-56); Y64:g-(-59); Y71:t(-166) |
| 9ZO9:A | ligand-bound | A1C3J (MG) | G13D, C51S, C80L, C118S | 7.5 | 100.0 | 1.7 | 2.39 | 3.42 | 0.41 | GDP | base | Y32:t(-161); T35:g+(+66); Q61:g-(-67); Y64:g-(-55); Y71:t(-163) |
| 9ZO9:A:B | ligand-bound | A1C3J (MG) | G13D, C51S, C80L, C118S | 7.5 | 100.0 | 1.7 | 2.39 | 3.42 | 0.41 | GDP | B (0.4) | Y32:t(-161); T35:g+(+66); Q61:g-(-67); Y64:g-(-55); Y71:t(-163) |
| 10JT:A | ligand-bound | A1C5K (CA) | - | 7.5 | 100.0 | 1.489 | 2.56 | 3.54 | 0.42 | GDP | base | Y32:t(-167); T35:g+(+76); Q61:g-(-74); Y64:g-(-52); Y71:t(-171) |
| 10NU:A | ligand-bound | A1C6Y (CA) | G12C; C51S; C80L; C118S | 8.5 | 100.0 | 1.5 | 2.55 | 3.54 | 0.42 | GDP | base | Y32:t(-166); T35:g+(+79); Q61:g-(-74); Y64:g-(-61); Y71:t(-167) |
| 10NU:A:B | ligand-bound | A1C6Y (CA) | G12C; C51S; C80L; C118S | 8.5 | 100.0 | 1.5 | 2.55 | 3.54 | 0.42 | GDP | B (0.48) | Y32:t(-166); T35:g+(+79); Q61:g-(-74); Y64:g-(-61); Y71:t(-167) |
| 12FF:C | ligand-bound | A1DB0 (CA,MG) | G12V | 8.5 | 100.0 | 2.1 | 2.56 | 3.49 | 0.42 | GDP | base | Y32:t(-161); T35:g+(+73); Q61:g-(-70); Y64:g-(-60); Y71:t(-169) |
| 12FG:A | ligand-bound | A1DBZ (MG) | G12V | 4.6 | 100.0 | 1.43 | 2.44 | 3.42 | 0.42 | GDP | base | Y32:t(-178); T35:g+(+70); Q61:g-(-56); Y64:g-(-57); Y71:t(-173) |
| 12FG:A:B | ligand-bound | A1DBZ (MG) | G12V | 4.6 | 100.0 | 1.43 | 2.44 | 3.42 | 0.42 | GDP | B (0.47) | Y32:t(-178); T35:g+(+70); Q61:g-(-56); Y64:g-(-57); Y71:t(-173) |
| 24HR:A | complex | AP6252 (MG) | G12D | - | 100.0 | 2.07 | 3.38 | 4.69 | 0.42 | GDP | base | Y32:t(-179); T35:g+(+67); Q61:g-(-66); Y64:t(-174); Y71:g-(-81) |
| 24HR:C | complex | AP6252 (MG) | G12D | - | 100.0 | 2.07 | 3.42 | 4.75 | 0.42 | GDP | base | Y32:t(+177); T35:g+(+86); Q61:g-(-71); Y64:t(-170); Y71:g-(-79) |
| 24HS:A | complex | AP4959 (MG) | G12D | 7.0 | 100.0 | 2.53 | 3.32 | 4.58 | 0.42 | GDP | base | Y32:t(-178); T35:g-(-48); Q61:g-(-59); Y64:t(-169); Y71:g-(-86) |
| 24HS:C | complex | AP4959 (MG) | G12D | 7.0 | 100.0 | 2.53 | 3.26 | 4.57 | 0.42 | GDP | base | Y32:t(-179); T35:g-(-76); Q61:g-(-58); Y64:t(-171); Y71:g-(-80) |
| 24HS:E | complex | AP4959 (MG) | G12D | 7.0 | 100.0 | 2.53 | 3.31 | 4.58 | 0.42 | GDP | base | Y32:t(-179); T35:g-(-46); Q61:g-(-58); Y64:t(+170); Y71:g-(-85) |
| 24HS:H | complex | AP4959 (MG) | G12D | 7.0 | 100.0 | 2.53 | 3.31 | 4.58 | 0.42 | GDP | base | Y32:t(-178); T35:g-(-54); Q61:g-(-73); Y64:t(-170); Y71:g-(-76) |
| 24HT:A | complex | ACY, AP2527 (MG) | G12D | 4.6 | 100.0 | 1.7 | 3.31 | 4.66 | 0.42 | GDP | base | Y32:t(-162); T35:g+(+74); Q61:g-(-74); Y64:t(+173); Y71:g-(-84) |
| 24HT:A:B | complex | ACY, AP2527 (MG) | G12D | 4.6 | 100.0 | 1.7 | 3.31 | 4.66 | 0.42 | GDP | B (0.44) | Y32:t(-162); T35:g+(+74); Q61:g-(-74); Y64:t(+173); Y71:g-(-84) |
| 24SP:A | complex | AP6296 (MG) | - | 8.5 | 100.0 | 1.45 | 3.25 | 4.52 | 0.42 | GDP | base | Y32:t(-163); T35:g+(+75); Q61:g-(-57); Y64:t(-166); Y71:g-(-84) |
| 24SP:B | complex | AP6296 (MG) | - | 8.5 | 100.0 | 1.45 | 3.29 | 4.54 | 0.42 | GDP | base | Y32:t(-162); T35:g+(+75); Y71:g-(-75) |
| 24SP:B:B | complex | AP6296 (MG) | - | 8.5 | 100.0 | 1.45 | 3.3 | 4.54 | 0.42 | GDP | B (0.48) | Y32:t(-162); T35:g+(+75); Y71:g-(-75) |
| 24SS:A | complex | AUBE00 (MG) | - | 6.5 | 100.0 | 1.56 | 3.35 | 4.72 | 0.42 | GDP | base | Y32:t(-179); T35:g+(+69); Q61:g-(-60); Y64:t(-177); Y71:g-(-82) |
| 24SS:A:B | complex | AUBE00 (MG) | - | 6.5 | 100.0 | 1.56 | 3.35 | 4.72 | 0.42 | GDP | B (0.55) | Y32:t(-179); T35:g+(+69); Q61:g-(-60); Y64:t(-177); Y71:g-(-82) |
| 24SS:B | complex | AUBE00 (MG) | - | 6.5 | 100.0 | 1.56 | 3.49 | 4.82 | 0.42 | GDP | base | Y32:t(-175); T35:g+(+72); Q61:g-(-53); Y64:t(-178); Y71:g-(-82) |
| 24SS:B:B | complex | AUBE00 (MG) | - | 6.5 | 100.0 | 1.56 | 3.49 | 4.82 | 0.42 | GDP | B (0.48) | Y32:t(-175); T35:g+(+72); Q61:g-(-53); Y64:t(-178); Y71:g-(-82) |
| 24SS:C | complex | AUBE00 (MG) | - | 6.5 | 100.0 | 1.56 | 3.45 | 4.75 | 0.42 | GDP | base | Y32:t(-177); T35:g+(+71); Q61:g-(-63); Y64:t(-175); Y71:g-(-82) |
| 9C3Z:A | apo | - (MG) | G12D, G60R | - | 100.0 | 1.8 | 3.08 | 4.29 | 0.42 | GDP | base | Y32:t(-175); T35:g+(+70); Y64:t(+170); Y71:g-(-79) |
| 9I7Y:B | ligand-bound | A1I08 (MG) | - | - | 100.0 | 1.85 | 2.01 | 2.8 | 0.42 | none | base | Y32:t(-167); T35:g+(+61); Y71:g-(-91) |
| 9KFL:D | complex | TIG3 peptide (MG) | G12V | - | 100.0 | 3.45 | 3.13 | 4.27 | 0.42 | GDP | base | Y32:t(+179); T35:g+(+68); Q61:g-(-57); Y64:t(+161); Y71:g-(-90) |
| 9MF0:A | complex | Leucine-zipper-like transcriptional regulator 1 (MG) | T35A, E62A | 5.0 | 100.0 | 3.3 | 2.76 | 3.81 | 0.42 | GDP | base | Y32:t(-173); Q61:g-(-74); Y64:g-(-71); Y71:g-(-93) |
| 9MF0:C | complex | Leucine-zipper-like transcriptional regulator 1 (MG) | T35A, E62A | 5.0 | 100.0 | 3.3 | 2.75 | 3.77 | 0.42 | GDP | base | Y32:t(-173); Q61:g-(-63); Y64:g-(-72); Y71:g-(-92) |
| 9MF0:E | complex | Leucine-zipper-like transcriptional regulator 1 (MG) | T35A, E62A | 5.0 | 100.0 | 3.3 | 2.73 | 3.74 | 0.42 | GDP | base | Y32:t(-172); Q61:g-(-75); Y64:g-(-70); Y71:g-(-95) |
| 9MF0:G | complex | Leucine-zipper-like transcriptional regulator 1 (MG) | T35A, E62A | 5.0 | 100.0 | 3.3 | 2.74 | 3.85 | 0.42 | GDP | base | Y32:t(-176); Q61:g-(-80); Y64:g-(-72); Y71:g-(-94) |
| 9MF0:I | complex | Leucine-zipper-like transcriptional regulator 1 (MG) | T35A, E62A | 5.0 | 100.0 | 3.3 | 2.71 | 3.77 | 0.42 | GDP | base | Y32:t(-176); Q61:g-(-69); Y64:g-(-71); Y71:g-(-94) |
| 9OUH:A | apo | - (MG) | G12D, C51S, C80L, C118S | - | 293.0 | 1.4 | 2.57 | 3.58 | 0.42 | GDP | base | Y32:t(-163); T35:g+(+75); Q61:g-(-94); Y64:g-(-64); Y71:g-(-82) |
| 9P45:A | ligand-bound | A1CG4 (MG) | G12D, C118S | - | 100.0 | 1.35 | 3.17 | 4.39 | 0.42 | GNP | base | Y32:g-(-58); T35:g+(+66); Q61:g-(-58); Y64:g-(-60); Y71:t(-176) |
| 9P45:A:B | ligand-bound | A1CG4 (MG) | G12D, C118S | - | 100.0 | 1.35 | 3.17 | 4.39 | 0.42 | GNP | B (0.5) | Y32:g-(-58); T35:g+(+66); Q61:g-(-58); Y64:g-(-60); Y71:t(-176) |
| 9RKN:D | complex | von Hippel-Lindau disease tumor suppressor, Elongin-C, Elongin-B (MG) | - | - | 100.0 | 2.85 | 2.66 | 3.64 | 0.42 | GCP | base | Y64:g-(-62); Y71:t(-167) |
| 9TC0:A | ligand-bound | A1JU8 (MG) | G12D | 5.5 | 100.0 | 1.6 | 2.33 | 3.29 | 0.42 | GDP | base | Y32:t(-177); T35:g+(+66); Q61:g-(-57); Y64:g-(-57); Y71:t(-166) |
| 9TC0:A:B | ligand-bound | A1JU8 (MG) | G12D | 5.5 | 100.0 | 1.6 | 2.33 | 3.29 | 0.42 | GDP | B (0.5) | Y32:t(-177); T35:g+(+66); Q61:g-(-57); Y64:g-(-57); Y71:t(-166) |
| 9U8V:A | apo | - (MG) | G12D,Y96S | - | 100.0 | 1.57 | 2.28 | 3.17 | 0.42 | GDP | base | Y32:t(-169); T35:g+(+60); Q61:g-(-100); Y71:g-(-89) |
| 9USB:B | ligand-bound | A1EN3 (MG) | - | 8.5 | 100.0 | 2.35 | 2.63 | 3.7 | 0.42 | GNP | base | Q61:g-(-62); Y64:g-(-63); Y71:t(-166) |
| 9XF8:A | ligand-bound | A1EZK (MG) | G12V | - | 100.0 | 1.26 | 2.45 | 3.43 | 0.42 | GDP | base | Y32:t(-169); T35:g+(+70); Q61:g-(-58); Y64:g-(-54); Y71:t(-177) |
| 9YMO:A | ligand-bound | A1AG3 (MG) | G12D, C118A | 4.6 | 100.0 | 1.25 | 2.47 | 3.38 | 0.42 | GDP | base | Y32:t(-170); T35:g+(+70); Q61:g-(-61); Y64:g-(-55); Y71:t(-177) |
| 9YMO:A:B | ligand-bound | A1AG3 (MG) | G12D, C118A | 4.6 | 100.0 | 1.25 | 2.47 | 3.38 | 0.42 | GDP | B (0.5) | Y32:t(-170); T35:g+(+70); Q61:g-(-61); Y64:g-(-55); Y71:t(-177) |
| 9YMQ:A | ligand-bound | A1AG3 (MG) | G12V, C118A | 4.6 | 100.0 | 1.2 | 2.45 | 3.41 | 0.42 | GDP | base | Y32:t(-170); T35:g+(+71); Q61:g-(-67); Y64:g-(-54); Y71:t(-177) |
| 9YMQ:A:B | ligand-bound | A1AG3 (MG) | G12V, C118A | 4.6 | 100.0 | 1.2 | 2.45 | 3.41 | 0.42 | GDP | B (0.5) | Y32:t(-170); T35:g+(+71); Q61:g-(-67); Y64:g-(-54); Y71:t(-177) |
| 9ZPA:A | ligand-bound | A1C3N (MG) | G12V, C51S, C80L, C118S | 7.5 | 100.0 | 1.68 | 2.47 | 3.35 | 0.42 | GDP | base | Y32:t(-171); T35:g+(+72); Q61:g-(-66); Y64:g-(-56); Y71:t(-172) |
| 9ZPA:A:B | ligand-bound | A1C3N (MG) | G12V, C51S, C80L, C118S | 7.5 | 100.0 | 1.68 | 2.47 | 3.35 | 0.42 | GDP | B (0.76) | Y32:t(-171); T35:g+(+72); Q61:g-(-66); Y64:g-(-56); Y71:t(-172) |
| 9ZPA:B | ligand-bound | A1C3N (MG) | G12V, C51S, C80L, C118S | 7.5 | 100.0 | 1.68 | 2.45 | 3.4 | 0.42 | GDP | base | Y32:t(-166); T35:g+(+70); Q61:g-(-66); Y64:g-(-55); Y71:t(-173) |
| 9ZPA:B:B | ligand-bound | A1C3N (MG) | G12V, C51S, C80L, C118S | 7.5 | 100.0 | 1.68 | 2.45 | 3.4 | 0.42 | GDP | B (0.54) | Y32:t(-166); T35:g+(+70); Q61:g-(-66); Y64:g-(-55); Y71:t(-173) |
| 9ZPE:B | ligand-bound | A1C3O (MG) | G12V, C51S, C80L, C118S | 4.6 | 100.0 | 1.91 | 2.39 | 3.35 | 0.42 | GDP | base | Y32:t(-166); T35:g+(+65); Q61:g-(-62); Y64:g-(-57); Y71:t(-169) |
| 11FB:A | apo | - (MG) | G12C,Y96C,C118S | - | 100.0 | 1.5 | 2.42 | 3.27 | 0.43 | GDP | base | Y32:t(-172); T35:g+(+72); Y71:g-(-87) |
| 12FF:A | ligand-bound | A1DB0 (CA,MG) | G12V | 8.5 | 100.0 | 2.1 | 2.44 | 3.23 | 0.43 | GDP | base | Y32:t(-162); T35:g+(+72); Q61:g-(-69); Y64:g-(-72,A,0.47)/t(+167,B,0.53); Y71:g-(-75) |
| 12FF:A:B | ligand-bound | A1DB0 (CA,MG) | G12V | 8.5 | 100.0 | 2.1 | 2.44 | 3.24 | 0.43 | GDP | B (0.53) | Y32:t(-162); T35:g+(+72); Q61:g-(-69); Y64:t(+167); Y71:g-(-75) |
| 12FF:B | ligand-bound | A1DB0 (CA,MG) | G12V | 8.5 | 100.0 | 2.1 | 2.43 | 3.25 | 0.43 | GDP | base | Y32:t(-161); T35:g+(+73); Q61:g-(-69); Y64:g-(-69,A,0.53)/t(+166,B,0.47); Y71:g-(-76) |
| 12FF:B:B | ligand-bound | A1DB0 (CA,MG) | G12V | 8.5 | 100.0 | 2.1 | 2.43 | 3.25 | 0.43 | GDP | B (0.52) | Y32:t(-161); T35:g+(+73); Q61:g-(-69); Y64:t(+166); Y71:g-(-76) |
| 12FF:D | ligand-bound | A1DB0 (CA,MG) | G12V | 8.5 | 100.0 | 2.1 | 2.56 | 3.47 | 0.43 | GDP | base | Y32:t(-162); T35:g+(+72); Q61:g-(-70); Y64:g-(-61); Y71:t(-169) |
| 9KFL:E | complex | TIG3 peptide (MG) | G12V | - | 100.0 | 3.45 | 3.29 | 4.37 | 0.43 | GDP | base | Y32:t(-178); T35:g+(+65); Q61:g-(-60); Y64:t(+149); Y71:g-(-93) |
| 9N9N:B | complex | cyclic peptide UNC10415730A (MG) | G12C | - | 100.0 | 1.24 | 2.56 | 3.41 | 0.43 | GDP | base | Y32:t(-176); T35:g+(+72); Q61:g-(-79); Y64:t(+162); Y71:g-(-90) |
| 9N9N:B:B | complex | cyclic peptide UNC10415730A (MG) | G12C | - | 100.0 | 1.24 | 2.56 | 3.41 | 0.43 | GDP | B (0.47) | Y32:t(-176); T35:g+(+72); Q61:g-(-79); Y64:t(+162); Y71:g-(-90) |
| 9PVF:E | complex | UM0152533 (MG) | - | 5.9 | 100.0 | 2.0 | 2.57 | 3.45 | 0.43 | GDP | base | Y32:t(-174); T35:g+(+68); Y64:g-(-44); Y71:g-(-92) |
| 9RKJ:H | complex | von Hippel-Lindau disease tumor suppressor, Elongin-C, Elongin-B (MG) | - | - | 100.0 | 2.89 | 2.76 | 3.69 | 0.43 | GCP | base | Q61:g+(+70); Y64:g-(-68); Y71:t(-169) |
| 9UOH:A | ligand-bound | A1L9E (MG) | - | 6.5 | 90.0 | 1.75 | 2.46 | 3.26 | 0.43 | GDP | base | Y32:t(-174); T35:g+(+61); Q61:g+(+62); Y64:t(+173) |
| 11FU:C | apo | - (MG) | G12C, R68S, C118S | - | 100.0 | 1.65 | 2.07 | 2.59 | 0.44 | GDP | base | Y71:g+(+68) |
| 11FU:C:B | apo | - (MG) | G12C, R68S, C118S | - | 100.0 | 1.65 | 2.07 | 2.59 | 0.44 | GDP | B (0.47) | Y71:g+(+68) |
| 24HR:B | complex | AP6252 (MG) | G12D | - | 100.0 | 2.07 | 3.43 | 4.42 | 0.44 | GDP | base | Y32:t(-177); T35:g+(+56); Q61:g-(-62); Y64:t(-163); Y71:g-(-83) |
| 24HR:D | complex | AP6252 (MG) | G12D | - | 100.0 | 2.07 | 3.4 | 4.38 | 0.44 | GDP | base | Y32:t(-174); T35:g+(+54); Q61:g-(-70); Y64:t(-161); Y71:g-(-86) |
| 24HS:B | complex | AP4959 (MG) | G12D | 7.0 | 100.0 | 2.53 | 3.42 | 4.43 | 0.44 | GDP | base | Y32:t(-167); T35:g-(-92); Q61:g-(-67); Y64:t(-167); Y71:g-(-91) |
| 24HS:D | complex | AP4959 (MG) | G12D | 7.0 | 100.0 | 2.53 | 3.45 | 4.47 | 0.44 | GDP | base | Y32:t(-171); T35:g-(-63); Q61:g-(-72); Y64:t(-174); Y71:g-(-91) |
| 24HS:F | complex | AP4959 (MG) | G12D | 7.0 | 100.0 | 2.53 | 3.52 | 4.39 | 0.44 | GDP | base | Y32:t(+171); T35:g+(+49); Q61:g-(-58); Y64:t(-170); Y71:g-(-86) |
| 24HS:G | complex | AP4959 (MG) | G12D | 7.0 | 100.0 | 2.53 | 3.47 | 4.42 | 0.44 | GDP | base | Y32:t(-177); T35:g-(-39); Q61:g-(-48); Y64:t(-164); Y71:g-(-90) |
| 9C3Q:A | apo | - (MG) | G12D, R41Q | - | 100.0 | 1.22 | 2.32 | 3.0 | 0.44 | GDP | base | Y32:t(-165); T35:g+(+68); Q61:g-(-77); Y64:t(+177); Y71:t(-162) |
| 9C3V:A | apo | - (MG) | G12D, D54R | - | 100.0 | 2.51 | 1.94 | 2.45 | 0.44 | GDP | base | Y32:t(-155); T35:g+(+59) |
| 9N9N:A | complex | cyclic peptide UNC10415730A (MG) | G12C | - | 100.0 | 1.24 | 2.75 | 3.49 | 0.44 | GDP | base | Y32:t(-162); T35:g+(+71); Q61:g-(-80); Y64:g-(-69); Y71:g-(-82) |
| 9PVF:A | complex | UM0152533 (MG) | - | 5.9 | 100.0 | 2.0 | 2.6 | 3.29 | 0.44 | GDP | base | Y32:t(-175); T35:g+(+67); Q61:t(+175); Y64:t(-166); Y71:g-(-90) |
| 9PVF:C | complex | UM0152533 (MG) | - | 5.9 | 100.0 | 2.0 | 2.64 | 3.34 | 0.44 | GDP | base | Y32:t(-173); T35:g+(+67); Y71:g-(-88) |
| 9PVF:C:B | complex | UM0152533 (MG) | - | 5.9 | 100.0 | 2.0 | 2.64 | 3.33 | 0.44 | GDP | B (0.59) | Y32:t(-173); T35:g+(+67); Y71:g-(-88) |
| 9RKE:D | complex | FLC, X53, von Hippel-Lindau disease tumor suppressor, Elongin-C, Elongin-B (MG) | - | - | 100.0 | 2.83 | 2.76 | 3.52 | 0.44 | GCP | base | Q61:g+(+70); Y64:g-(-59); Y71:t(-175) |
| 9RKE:H | complex | X53, von Hippel-Lindau disease tumor suppressor, Elongin-C, Elongin-B (MG) | - | - | 100.0 | 2.83 | 2.76 | 3.5 | 0.44 | GCP | base | Q61:g+(+69); Y64:g-(-60); Y71:t(-177) |
| 9RKJ:D | complex | von Hippel-Lindau disease tumor suppressor, Elongin-C, Elongin-B (MG) | - | - | 100.0 | 2.89 | 2.7 | 3.44 | 0.44 | GCP | base | Y64:g-(-68); Y71:t(-170) |
| 9U8W:B | apo | - (MG) | G12D,Q99L | - | 100.0 | 1.5 | 2.63 | 3.39 | 0.44 | GDP | base | Y32:t(-168); T35:g+(+71); Q61:g-(-54); Y64:t(+178); Y71:g-(-90) |
| 9U8W:B:B | apo | - (MG) | G12D,Q99L | - | 100.0 | 1.5 | 2.63 | 3.39 | 0.44 | GDP | B (0.43) | Y32:t(-168); T35:g+(+71); Q61:g-(-54); Y64:t(+178); Y71:g-(-90) |
| 12KZ:A | ligand-bound | A1DI3 (MG) | G12C, C118A | 8.5 | 100.0 | 1.45 | 2.44 | 2.99 | 0.45 | GDP | base | Y32:t(-172); T35:g+(+71); Q61:g-(-52); Y64:t(-170); Y71:g+(+74) |
| 12LA:A | ligand-bound | A1DI5 (MG) | G12C, C118A | 8.5 | 100.0 | 1.1 | 2.42 | 2.96 | 0.45 | GDP | base | Y32:t(-174); T35:g+(+71); Q61:g-(-59); Y64:t(-165); Y71:g+(+71) |
| 12LA:A:B | ligand-bound | A1DI5 (MG) | G12C, C118A | 8.5 | 100.0 | 1.1 | 2.42 | 2.96 | 0.45 | GDP | B (0.5) | Y32:t(-174); T35:g+(+71); Q61:g-(-59); Y64:t(-165); Y71:g+(+71) |
| 9NZM:B | ligand-bound | A1B7P (MG) | G12C, C51S, C80L, C121S | 6.5 | 100.0 | 1.586 | 4.85 | 5.92 | 0.45 | GNP | base | Q61:g-(-70); Y64:g-(-57); Y71:t(-177) |
| 9NZM:B:B | ligand-bound | A1B7P (MG) | G12C, C51S, C80L, C121S | 6.5 | 100.0 | 1.586 | 4.85 | 5.92 | 0.45 | GNP | B (0.44) | Q61:g-(-70); Y64:g-(-57); Y71:t(-177) |
| 9PVF:D | complex | UM0152533 (MG) | - | 5.9 | 100.0 | 2.0 | 2.92 | 3.57 | 0.45 | GDP | base | Y32:t(-176); T35:g+(+69); Y64:t(-143); Y71:g-(-87) |
| 12LB:A | ligand-bound | A1DI6 (MG) | G12C, C118A | 8.5 | 100.0 | 1.26 | 2.49 | 2.91 | 0.46 | GDP | base | Y32:t(-171); T35:g+(+74); Q61:g-(-55); Y64:t(-169); Y71:g+(+75) |
| 12LB:A:B | ligand-bound | A1DI6 (MG) | G12C, C118A | 8.5 | 100.0 | 1.26 | 2.49 | 2.91 | 0.46 | GDP | B (0.5) | Y32:t(-171); T35:g+(+74); Q61:g-(-55); Y64:t(-169); Y71:g+(+75) |
| 9GLU:A | complex | Peptide MPB1 (MG) | - | - | 100.0 | 1.9 | 2.84 | 3.36 | 0.46 | GDP | base | Y32:t(-166); T35:g+(+71); Q61:g+(+64); Y64:g-(-57); Y71:g-(-80) |
| 9GLU:B | complex | Peptide MPB1 (MG) | - | - | 100.0 | 1.9 | 2.81 | 3.28 | 0.46 | GDP | base | Y32:t(-165); T35:g+(+69); Q61:g+(+66); Y64:g-(-55); Y71:g-(-82) |
| 9L6F:H | complex | A1L66, Elongin-B, Elongin-C, von Hippel-Lindau disease tumor suppressor (MG) | G12D | - | 90.0 | 3.18 | 2.52 | 2.91 | 0.46 | GDP | base | Y32:t(-146); T35:g+(+43); Q61:t(-139); Y64:t(+163); Y71:g-(-85) |
| 9L6F:P | complex | A1L66, Elongin-B, Elongin-C, von Hippel-Lindau disease tumor suppressor (MG) | G12D | - | 90.0 | 3.18 | 2.51 | 2.96 | 0.46 | GDP | base | Y32:t(-156); T35:g+(+38); Q61:t(-146); Y64:t(+156); Y71:g-(-88) |
| 9PVF:B | complex | UM0152533 (MG) | - | 5.9 | 100.0 | 2.0 | 2.68 | 3.1 | 0.46 | GDP | base | Y32:t(-176); T35:g+(+64); Y64:t(-152); Y71:g-(-89) |
| 9PVF:B:B | complex | UM0152533 (MG) | - | 5.9 | 100.0 | 2.0 | 2.67 | 3.1 | 0.46 | GDP | B (0.47) | Y32:t(-176); T35:g+(+64); Y64:t(-152); Y71:g-(-89) |
| 12LC:A | ligand-bound | A1DI7 (MG) | G12C, C51S, C80L, C118S | 8.5 | 100.0 | 1.9 | 2.53 | 2.83 | 0.47 | GDP | base | Y32:t(-172); T35:g+(+73); Q61:g-(-58); Y64:t(-167); Y71:g+(+74) |
| 9L6A:A | ligand-bound | A1L65 (MG) | G12D | - | 90.0 | 1.36 | 2.68 | 3.06 | 0.47 | GDP | base | Y32:t(-168); T35:g+(+67); Q61:g-(-55); Y64:t(+171); Y71:g-(-63) |
| 9L6F:D | complex | Elongin-B, Elongin-C, von Hippel-Lindau disease tumor suppressor (MG) | G12D | - | 90.0 | 3.18 | 2.62 | 2.9 | 0.47 | GDP | base | Y32:t(-153); T35:g+(+44); Q61:t(-144); Y64:t(+164); Y71:g-(-91) |
| 9L6F:L | complex | A1L66, Elongin-B, Elongin-C, von Hippel-Lindau disease tumor suppressor (MG) | G12D | - | 90.0 | 3.18 | 2.51 | 2.87 | 0.47 | GDP | base | Y32:t(-155); T35:g+(+58); Q61:t(-132); Y64:t(+167); Y71:g-(-86) |
| 9PVF:F | complex | UM0152533 (MG) | - | 5.9 | 100.0 | 2.0 | 3.01 | 3.3 | 0.48 | GDP | base | Y32:t(-179); T35:g+(+65); Y64:g-(-6); Y71:g-(-88) |
| 11QE:A | apo | - (MG) | G12D, I55E | - | 100.0 | 1.23 | 16.93 | 17.32 | 0.49 | GDP | base | Y32:t(+178); T35:g+(+73); Q61:g+(+80); Y64:g-(-56); Y71:g-(-88) |
| 11QE:A:B | apo | - (MG) | G12D, I55E | - | 100.0 | 1.23 | 16.93 | 17.32 | 0.49 | GDP | B (0.44) | Y32:t(+178); T35:g+(+73); Q61:g+(+80); Y64:g-(-56); Y71:g-(-88) |
| 11FL:A | apo | - | G12C,Y96D,C118S | - | 100.0 | 1.5 | 17.33 | 17.57 | 0.5 | GDP | base | Y32:t(+176); T35:g+(+78); Q61:g+(+46); Y64:g-(-59); Y71:g-(-88) |
| 9C3M:A | apo | - (MG) | G12D, F28K | - | 100.0 | 1.74 | 8.02 | 8.15 | 0.5 | GDP | base | Y32:t(+179); T35:g-(-54); Q61:g-(-57); Y64:t(+175); Y71:g-(-73) |
| 9C3M:B | apo | - (MG) | G12D, F28K | - | 100.0 | 1.74 | 7.75 | 7.89 | 0.5 | GDP | base | Y32:t(+175); T35:g-(-63); Q61:g-(-75); Y64:t(+174); Y71:g-(-66) |
| 9Q2X:A | apo | - (MG) | G12D,T35S,C118S | 6.5 | 298 | - | 3.45 | 3.41 | 0.5 | GNP | base | Y32:g+(+71); S35:g-(-49); Q61:g-(-81); Y64:g+(+51); Y71:g+(+82) |
| 9U8X:A | apo | - (MG) | G12D,R68M | - | 100.0 | 1.65 | 3.2 | 2.82 | 0.53 | GDP | base | Y32:t(-173); T35:g+(+71); Q61:g-(-62); Y64:g-(-39); Y71:g-(-66) |
| 9Q30:A | apo | - (MG) | T35S, C118S | 6.5 | 298 | - | 3.65 | 3.1 | 0.54 | GNP | base | Y32:g+(+79); S35:t(-173); Q61:g+(+55); Y64:g-(-63); Y71:g-(-71) |
| 9Q2Z:A | apo | - (MG) | G12C, T35S, C118S | 6.5 | 298 | - | 3.78 | 3.07 | 0.55 | GNP | base | Y32:g+(+59); S35:g+(+36); Q61:g+(+75); Y64:g+(+39); Y71:g-(-59) |
| 9U8W:A | apo | - (MG) | G12D,Q99L | - | 100.0 | 1.5 | 3.53 | 2.89 | 0.55 | GDP | base | Y32:t(+177); T35:g-(-60); Q61:g+(+66); Y64:t(+176); Y71:g-(-100) |
| 9I7Y:C | ligand-bound | A1I08 (MG) | - | - | 100.0 | 1.85 | 1.41 | 1.12 | 0.56 | none | base | - |
| 9U8Y:A | apo | - (MG) | G12D,G13D | - | 100.0 | 1.73 | 4.37 | 3.47 | 0.56 | GDP | base | Y32:t(+169); T35:g+(+79); Q61:g-(-67); Y64:t(+178); Y71:g-(-66) |
| 36OJ:B | complex | A1DKX, Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.74 | 2.47 | 1.83 | 0.57 | GNP | base | Y32:t(+170); T35:g-(-64); Q61:g+(+65); Y64:g-(-56); Y71:g-(-70) |
| 36OJ:B:B | complex | A1DKX, Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.74 | 2.47 | 1.83 | 0.57 | GNP | B (0.5) | Y32:t(+170); T35:g-(-64); Q61:g+(+65); Y64:g-(-56); Y71:g-(-70) |
| 9YOW:C | complex | Peptidyl-prolyl cis-trans isomerase A (MG) | G12C | - | 100.0 | 1.57 | 2.62 | 1.97 | 0.57 | GNP | base | Y32:t(-177); T35:g-(-59); Q61:g+(+69); Y64:g-(-50); Y71:g-(-67) |
| 9YOW:A | complex | Peptidyl-prolyl cis-trans isomerase A (MG) | G12C | - | 100.0 | 1.57 | 2.71 | 1.93 | 0.58 | GNP | base | Y32:t(-176); T35:g-(-55); Q61:g+(+72); Y64:g-(-48); Y71:g-(-68) |
| 36OI:A | complex | Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.47 | 2.71 | 1.79 | 0.6 | GNP | base | Y32:t(+166); T35:g-(-62); Q61:g+(+60); Y64:g-(-59); Y71:g-(-66) |
| 36OK:B | complex | A1DKY, Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.21 | 2.72 | 1.84 | 0.6 | GNP | base | Y32:t(+175); T35:g-(-60); Q61:g+(+60); Y64:g-(-51); Y71:g-(-73) |
| 36OK:B:B | complex | A1DKY, Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.21 | 2.72 | 1.84 | 0.6 | GNP | B (0.56) | Y32:t(+175); T35:g-(-60); Q61:g+(+60); Y64:g-(-51); Y71:g-(-73) |
| 9CT7:A | complex | Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.42 | 2.69 | 1.82 | 0.6 | GNP | base | Y32:t(+180); T35:g-(-55); Q61:g+(+70); Y64:g-(-48); Y71:g-(-68) |
| 9CT7:A:B | complex | Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.42 | 2.69 | 1.82 | 0.6 | GNP | B (0.5) | Y32:t(+180); T35:g-(-55); Q61:g+(+70); Y64:g-(-48); Y71:g-(-68) |
| 9CT8:A | complex | A1AZX, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.28 | 2.74 | 1.82 | 0.6 | GNP | base | Y32:t(-167,A,0.51)/g-(-71,B,0.49); T35:g-(-58); Q61:g+(+64); Y64:g-(-46); Y71:g-(-68) |
| 9CT8:A:B | complex | A1AZX, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.28 | 2.74 | 1.82 | 0.6 | GNP | B (0.45) | Y32:g-(-71); T35:g-(-58); Q61:g+(+64); Y64:g-(-46); Y71:g-(-68) |
| 36OI:B | complex | Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.47 | 2.71 | 1.76 | 0.61 | GNP | base | Y32:t(+167); T35:g-(-62); Q61:g+(+62); Y64:g-(-43); Y71:g-(-67) |
| 36OI:B:B | complex | Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.47 | 2.71 | 1.76 | 0.61 | GNP | B (0.71) | Y32:t(+167); T35:g-(-62); Q61:g+(+62); Y64:g-(-43); Y71:g-(-67) |
| 36OJ:A | complex | A1DKX, Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.74 | 2.54 | 1.65 | 0.61 | GNP | base | Y32:t(+170); T35:g-(-61); Q61:g+(+62); Y64:g-(-66); Y71:g-(-69) |
| 36OK:A:B | complex | A1DKY, Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.21 | 3.01 | 1.89 | 0.61 | GNP | B (0.5) | Y32:t(+167); T35:g-(-61); Q61:g-(-66); Y64:g-(-56); Y71:g-(-63) |
| 36OK:A | complex | A1DKY, Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.21 | 3.01 | 1.89 | 0.62 | GNP | base | Y32:t(+167); T35:g-(-61); Q61:g-(-66); Y64:g-(-56); Y71:g-(-63) |
| 9CT7:B | complex | Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.42 | 2.85 | 1.71 | 0.62 | GNP | base | Y32:t(-179); T35:g-(-58); Q61:g+(+47); Y64:g-(-60); Y71:g-(-68) |
| 9CT7:B:B | complex | Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.42 | 2.84 | 1.71 | 0.62 | GNP | B (0.5) | Y32:t(-179); T35:g-(-58); Q61:g+(+47); Y64:g-(-60); Y71:g-(-68) |
| 9E3S:A | complex | A1BEA, Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.08 | 2.84 | 1.73 | 0.62 | GNP | base | Y32:t(+176); T35:g-(-60); Q61:t(-161); Y64:g-(-52); Y71:g-(-71,A,0.54)/g+(+72,B,0.46) |
| 9E3S:A:B | complex | A1BEA, Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.08 | 2.87 | 1.78 | 0.62 | GNP | B (0.49) | Y32:t(+176); T35:g-(-60); Q61:t(-161); Y64:g-(-52); Y71:g+(+72) |
| 9CT8:B | complex | A1AZX, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.28 | 2.95 | 1.71 | 0.63 | GNP | base | Y32:t(+178); T35:g-(-56); Q61:g+(+55); Y64:g-(-61); Y71:g-(-63) |
| 9CT8:B:B | complex | A1AZX, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.28 | 2.95 | 1.71 | 0.63 | GNP | B (0.53) | Y32:t(+178); T35:g-(-56); Q61:g+(+55); Y64:g-(-61); Y71:g-(-63) |
| 9CT9:A | complex | A1AZY, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.35 | 2.81 | 1.66 | 0.63 | GNP | base | Y32:t(-178); T35:g-(-58); Q61:g+(+59); Y64:g-(-59); Y71:g-(-69) |
| 9CTA:A | complex | A1AZW, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.29 | 2.97 | 1.76 | 0.63 | GNP | base | Y32:t(+178); T35:g-(-57); Q61:g+(+50,A,0.38)/t(-166,B,0.62); Y64:g-(-45); Y71:g-(-70,A,0.53)/g+(+65,B,0.47) |
| 9CTA:A:B | complex | A1AZW, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.29 | 2.97 | 1.76 | 0.63 | GNP | B (0.5) | Y32:t(+178); T35:g-(-57); Q61:t(-166); Y64:g-(-45); Y71:g+(+65) |
| 9CTA:A:C | complex | A1AZW, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.29 | 2.97 | 1.76 | 0.63 | GNP | C (0.14) | Y32:t(+178); T35:g-(-57); Q61:g+(+50); Y64:g-(-45); Y71:g-(-70) |
| 9HMR:A | ligand-bound | A1IWE | - | - | 193.0 | 1.5 | 7.0 | 4.09 | 0.63 | GDP | base | Y64:g+(+63); Y71:t(+158) |
| 9HMR:B | ligand-bound | A1IWE | - | - | 193.0 | 1.5 | 7.27 | 4.29 | 0.63 | GDP | base | Y64:g+(+62); Y71:t(+159) |
| 9HMR:C | ligand-bound | A1IWE | - | - | 193.0 | 1.5 | 6.46 | 3.87 | 0.63 | GDP | base | Y64:g+(+64); Y71:t(+158) |
| 9HMR:D | ligand-bound | A1IWE | - | - | 193.0 | 1.5 | 7.36 | 4.29 | 0.63 | GDP | base | Y64:g+(+65); Y71:t(+160) |
| 36OL:B | apo | - (MG) | - | - | 100.0 | 2.05 | 3.5 | 1.98 | 0.64 | GNP | base | Y32:t(-177); T35:g-(-51); Q61:g+(+66); Y64:t(-163); Y71:g+(+64) |
| 9CT9:B | complex | A1AZY, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.35 | 2.96 | 1.65 | 0.64 | GNP | base | Y32:t(+179); T35:g-(-54); Q61:g+(+54); Y64:g-(-58); Y71:g-(-63) |
| 9CT9:B:B | complex | A1AZY, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.35 | 2.96 | 1.65 | 0.64 | GNP | B (0.5) | Y32:t(+179); T35:g-(-54); Q61:g+(+54); Y64:g-(-58); Y71:g-(-63) |
| 9CTA:B | complex | A1AZW, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.29 | 3.01 | 1.68 | 0.64 | GNP | base | Y32:t(+178); T35:g-(-58); Q61:g-(-97); Y64:g-(-46); Y71:g-(-67,A,0.51)/g+(+63,B,0.49) |
| 9CTA:B:B | complex | A1AZW, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.29 | 3.0 | 1.68 | 0.64 | GNP | B (0.52) | Y32:t(+178); T35:g-(-58); Q61:g-(-97); Y64:g-(-46); Y71:g+(+63) |
| 9CTB:B | complex | A1AZZ, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.29 | 3.09 | 1.71 | 0.64 | GNP | base | Y32:t(+180); T35:g-(-55); Q61:t(+178); Y64:g-(-47); Y71:g-(-63,A,0.45)/g+(+62,B,0.55) |
| 9CTB:B:B | complex | A1AZZ, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.29 | 3.08 | 1.71 | 0.64 | GNP | B (0.55) | Y32:t(+180); T35:g-(-55); Q61:t(+178); Y64:g-(-47); Y71:g+(+62) |
| 9E3S:B | complex | A1BEA, Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.08 | 2.88 | 1.65 | 0.64 | GNP | base | Y32:t(+176); T35:g-(-58); Q61:g+(+61,A,0.44)/t(-156,B,0.56); Y64:g-(-47,A,0.49)/g-(-62,B,0.51); Y71:g-(-69,A,0.58)/g+(+67,B,0.42) |
| 9E3S:B:B | complex | A1BEA, Peptidyl-prolyl cis-trans isomerase A (MG) | - | - | 100.0 | 1.08 | 2.96 | 1.66 | 0.64 | GNP | B (0.52) | Y32:t(+176); T35:g-(-58); Q61:t(-156); Y64:g-(-62); Y71:g+(+67) |
| 35VB:A | complex | Serine/threonine-protein kinase B-raf (MG) | G13C | - | 100.0 | 2.85 | 2.91 | 1.51 | 0.66 | GNP | base | Y32:t(+175); T35:g-(-51); Q61:t(+160); Y64:g-(-62); Y71:g+(+73) |
| 9CTB:A | complex | A1AZZ, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.29 | 3.25 | 1.65 | 0.66 | GNP | base | Y32:t(+180); T35:g-(-58); Q61:g-(-85); Y64:g-(-55); Y71:g-(-72,A,0.5)/g+(+71,B,0.5) |
| 9CTB:A:B | complex | A1AZZ, Peptidyl-prolyl cis-trans isomerase A (MG) | G12D | - | 100.0 | 1.29 | 3.25 | 1.64 | 0.66 | GNP | B (0.47) | Y32:t(+180); T35:g-(-58); Q61:g-(-85); Y64:g-(-55); Y71:g+(+71) |
| 36OM:A | apo | - (CO,MG) | - | - | 100.0 | 1.25 | 3.64 | 1.57 | 0.7 | GNP | base | Y32:t(+165); T35:g+(+69); Q61:g-(-63); Y64:g-(-58); Y71:g-(-72) |
| 9YGS:A | complex | RAF proto-oncogene serine/threonine-protein kinase (MG) | Y71H | - | 100.0 | 1.68 | 3.31 | 1.21 | 0.73 | GNP | base | Y32:t(-173); T35:g-(-57); Q61:g-(-63); Y64:g-(-59); H71:g-(-66) |
| 9O65:B | complex | Serine/threonine-protein phosphatase PP1-alpha catalytic subunit, Leucine-rich repeat protein SHOC-2 (MG) | P50R; Q61R; M173I | - | - | 3.0 | 4.02 | 1.41 | 0.74 | GNP | base | Y32:t(+167); T35:g-(-41); R61:g-(-81); Y64:g-(-69); Y71:g-(-71) |
| 9NLC:C | complex | Phosphatidylinositol 3-kinase regulatory subunit alpha, Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | - | - | - | 10.0 | 3.72 | 1.07 | 0.78 | GNP | base | Y32:t(-176); T35:g-(-53); Q61:g+(+72); Y64:g-(-54); Y71:g+(+66) |
| 11GH:A | complex | RAF proto-oncogene serine/threonine-protein kinase (MG) | G12C,Y96D,C118S | - | 100.0 | 2.5 | 2.93 | 0.78 | 0.79 | GNP | base | Y32:t(-173); T35:g-(-61); Q61:g-(-102); Y64:g-(-56); Y71:g+(+61) |
| 9CMV:B | complex | Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | W1057A/I1058A/F1059A | 8.0 | 100.0 | 3.01 | 3.62 | 0.74 | 0.83 | GNP | base | Y32:t(-172); T35:g-(-48); Q61:g-(-56); Y64:g-(-45); Y71:g+(+64) |
| 9NI4:C | complex | Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | - | - | - | 2.61 | 3.58 | 0.67 | 0.84 | GNP | base | Y32:t(-175); T35:g-(-42); Q61:g-(-63); Y64:g-(-50); Y71:g+(+65) |
| 9NI7:C | complex | Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | - | - | - | 3.05 | 3.55 | 0.67 | 0.84 | GNP | base | Y32:t(-169); T35:g-(-46); Q61:g-(-64); Y64:g-(-53); Y71:g+(+70) |
| 9NID:C | complex | Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | - | - | - | 5.0 | 3.57 | 0.67 | 0.84 | GNP | base | Y32:t(-176); T35:g-(-56); Q61:g-(-60); Y64:g-(-50); Y71:g+(+63) |
| 9NI3:C | complex | Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | - | - | - | 2.82 | 3.49 | 0.6 | 0.85 | GNP | base | Y32:t(-173); T35:g-(-46); Q61:g-(-62); Y64:g-(-47); Y71:g+(+71) |
| 9NI4:D | complex | Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | - | - | - | 2.61 | 3.57 | 0.62 | 0.85 | GNP | base | Y32:t(-179); T35:g-(-40); Q61:g-(-69); Y64:g-(-50); Y71:g+(+64) |
| 9NI5:C | complex | Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | - | - | - | 2.89 | 3.52 | 0.62 | 0.85 | GNP | base | Y32:t(-173); T35:g-(-41); Q61:g-(-66); Y64:g-(-52); Y71:g+(+70) |
| 9NI6:C | complex | Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform, Phosphatidylinositol 3-kinase regulatory subunit alpha (MG) | - | - | - | 3.01 | 3.54 | 0.64 | 0.85 | GNP | base | Y32:t(-177); T35:g-(-53); Q61:g-(-67); Y64:g-(-48); Y71:g+(+73) |
| 9NI8:C | complex | Phosphatidylinositol 3-kinase regulatory subunit alpha, Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | - | - | - | 3.23 | 3.47 | 0.61 | 0.85 | GNP | base | Y32:t(+174); T35:g-(-50); Q61:g-(-56); Y64:g-(-47); Y71:g+(+68) |
| 9NID:D | complex | Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | - | - | - | 5.0 | 3.56 | 0.62 | 0.85 | GNP | base | Y32:t(-178); T35:g-(-51); Q61:g-(-70); Y64:g-(-50); Y71:g+(+64) |
| 9NIE:C | complex | Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | - | - | - | 5.0 | 3.53 | 0.63 | 0.85 | GNP | base | Y32:t(-174); T35:g-(-46); Q61:g-(-63); Y64:g-(-51); Y71:g+(+69) |
| 9NIF:C | complex | Phosphatidylinositol 4,5-bisphosphate 3-kinase catalytic subunit alpha isoform (MG) | - | - | - | 5.0 | 3.49 | 0.6 | 0.85 | GNP | base | Y32:t(-174); T35:g-(-49); Q61:g-(-63); Y64:g-(-47); Y71:g+(+69) |
| 36OL:A:B | apo | - (MG) | - | - | 100.0 | 2.05 | 3.21 | 0.06 | 0.98 | GNP | B (0.5) | Y32:t(+180); T35:g-(-55); Q61:g-(-82); Y64:g-(-61); Y71:g+(+71) |
| 36OL:A | apo | - (MG) | - | - | 100.0 | 2.05 | 3.21 | 0.0 | 1.0 | GNP | base | Y32:t(+180); T35:g-(-55); Q61:g-(-82); Y64:g-(-61); Y71:g+(+71) |
| 9NFB:C | complex | A1AWR, R302 Fab heavy chain, R302 Fab light chain, Beta-2-microglobulin, MHC class I antigen | G12C | - | - | 3.23 | None | None | None | none | base | - |
| 9NFC:C | complex | A1AWR, R302 Fab heavy chain, R302 Fab light chain, Beta-2-microglobulin, HLA class I histocompatibility antigen, A alpha chain | G12C | - | - | 2.58 | None | None | None | none | base | - |
| 9O55:C | complex | RM010 Fab light chain, RM010 Fab heavy chain, MHC class I antigen | - | - | - | 2.88 | None | None | None | none | base | - |
| 9WJ6:I | complex | Beta-2-microglobulin, C8K10D5-1 Fab heavy chain, HLA class I antigen, C8K10D5-1 Fab Light chain | G12D | - | 295.15 | 4.54 | None | None | None | none | base | - |
| 9WJ6:P | complex | Beta-2-microglobulin, C8K10D5-1 Fab heavy chain, HLA class I antigen, C8K10D5-1 Fab Light chain | G12D | - | 295.15 | 4.54 | None | None | None | none | base | - |
| 9Z50:E | complex | Q61H_Sahin-1 beta chain (TRBV9), Q61H_Sahin-1 alpha chain (TRAV14/DV4), Beta-2-microglobulin, MHC class I antigen | Q61H | - | 100.0 | 2.9 | None | None | None | none | base | - |
| 9Z50:P | complex | Q61H_Sahin-1 beta chain (TRBV9), Q61H_Sahin-1 alpha chain (TRAV14/DV4), Beta-2-microglobulin, MHC class I antigen | Q61H | - | 100.0 | 2.9 | None | None | None | none | base | - |
| 9ZCL:P | complex | N17.3.2 TCR beta, N17.3.2 TCR alpha, Beta-2-microglobulin, HLA class I histocompatibility antigen | - | 6.5 | 100.0 | 2.3 | None | None | None | none | base | - |
