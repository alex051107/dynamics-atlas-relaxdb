#!/usr/bin/env python3
"""Which deposited structures of one protein are apo, which are bound, and where each sits between an open and a
closed reference (Gina's 9-29 addition: judge from all same-sequence PDB entries which ones represent alternate states,
using the binding partner, or none, and the conditions).

Reads structures/<ENTRY>/metadata.json and cif/*.cif.gz (downloaded 2026-10-12). Cα only, numpy only.
For every chain mapped to the accession: superpose on the core residues, then RMSD of the mobile residues to the
open and to the closed reference chain. closure = d_open / (d_open + d_closed): 0 = like open, 1 = like closed.

  pdb_states.py CONFIG.json   -> outputs/pdb_states/<ENTRY>.json and .md
  config: {"entry", "accession", "core": [[a, b], ...], "mobile": [[a, b], ...], "open": "PDB:chain", "closed": "PDB:chain",
           "note"}
  optional (added 2026-10-20 for the CPMG-10 extension; absent keys leave the AQADK/ARGKIN behaviour unchanged):
    "renumber": {"PDB" or "PDB:chain": [[auth_lo, auth_hi, delta], ...]}  auth_seq_id in [lo, hi] -> auth + delta; residues
                outside every rule are dropped. Use it when a deposition is not in the accession's author numbering.
    "count_as_ligand": ["PO4", ...]  comp ids taken out of SOLVENT for the apo / ligand-bound call (e.g. the BlaC anion site).
    "verify_numbering": true  adds n_resname_mismatch per chain (residue names at core+mobile positions vs the open reference).
  optional (added 2026-10-20 evening for CypA / RNase A / K-Ras; all off unless the key is present):
    "altlocs": true  every altloc letter seen at a mobile-residue CA or at a chi1 side chain becomes its own row "PDB:chain:X"
               (mobile CA and chi1 atoms taken from altloc X where it exists, otherwise from the base conformer). The base row
               "PDB:chain" is unchanged (altloc '.'/A). Altloc letters are assigned per residue by the depositor, so a
               composite row X is not a coupled conformer unless the authors say so. altloc_occ = mean occupancy of the
               mobile CA atoms taken from X.
    "sidechain_chi1": [55, 61, ...]  chi1 (N-CA-CB-CG / OG / OG1 / SG / CG1) per listed residue, with the rotamer
               g+ (0..120), t (120..240), g- (240..360), per conformer; the base row lists every altloc with its occupancy.
    "cofactor": ["GDP", "GNP", ...]  comp ids reported in their own column and excluded from the ligand list, so the apo /
               ligand-bound call ignores them (K-Ras: GDP vs GTP analogue is a state, not a ligand).
    "detect_fused_covalent": true  adds fused/covalent columns from local CIF mappings and covale links; off by default.
    "metadata_table": true  also writes <ENTRY>_metadata_all.md/.json, one row per mapped entry from metadata.json (including
               entries above the download cap): method, resolution, cofactor, ligands, partners, mutation (deposited field, and
               parsed from the title when the field is empty), class.
"""
import gzip
import json
import re
import sys
from pathlib import Path

import numpy as np

WORK = Path.home() / "dynamics_atlas_work"
SOLVENT = {"HOH", "DOD", "SO4", "PO4", "NO3", "CL", "NA", "K", "BR", "IOD", "GOL", "EDO", "PEG", "PG4", "PGE", "1PE", "ACT",
           "FMT", "MPD", "TRS", "EPE", "MES", "DMS", "BME", "DTT", "IPA", "EOH", "MOH", "CIT", "ACE", "NH2", "SCN", "AZI",
           "BU3", "P6G", "TLA", "MLI", "IMD", "CAC", "NI", "UNX"}
IONS = {"MG", "ZN", "CA", "MN", "CO", "CU", "CU1", "FE", "FE2", "CD", "HG", "SR", "NI"}
CHI1_GAMMA = {"SER": "OG", "THR": "OG1", "CYS": "SG", "ILE": "CG1", "VAL": "CG1"}  # every other residue with a CB uses CG
CHI1_ATOMS = {"N", "CA", "CB", "CG", "OG", "OG1", "SG", "CG1"}
AA1 = {"ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q", "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I",
       "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V",
       "MSE": "M"}


def ca_coords(cif_gz, chains, names=None, altlocs=False, side=None):
    """auth_asym_id -> {auth_seq_id: xyz} for CA atoms, first model, first altloc. names (optional dict) gets
    auth_asym_id -> {auth_seq_id: label_comp_id}.
    altlocs=True (opt-in) returns (out, alt) with alt: auth_asym_id -> {auth_seq_id: {altloc: (xyz, occ)}} for CA atoms that
    carry a letter altloc. side (opt-in dict) gets auth_asym_id -> {auth_seq_id: {altloc_or_'.': {atom: (xyz, occ)}}} for the
    chi1 atoms of every residue."""
    out, cols, rows = {c: {} for c in chains}, [], False
    alt = {c: {} for c in chains}
    if names is not None:
        names.update({c: {} for c in chains})
    if side is not None:
        side.update({c: {} for c in chains})
    with gzip.open(cif_gz, "rt", errors="replace") as fh:
        for line in fh:
            if line.startswith("_atom_site."):
                cols.append(line.strip().split(".", 1)[1]); rows = True; continue
            if rows and cols and not line.startswith(("ATOM", "HETATM")):
                if out and any(out.values()):
                    break
                continue
            if rows and line.startswith(("ATOM", "HETATM")):
                f = line.split()
                if len(f) < len(cols):
                    continue
                d = dict(zip(cols, f))
                atom = d.get("label_atom_id")
                if d.get("pdbx_PDB_model_num", "1") != "1":
                    continue
                ch = d.get("auth_asym_id")
                if ch not in out:
                    continue
                al = d.get("label_alt_id", ".")
                if side is not None and atom in CHI1_ATOMS:
                    try:
                        side[ch].setdefault(int(d["auth_seq_id"]), {}).setdefault(al, {}).setdefault(
                            atom, ([float(d["Cartn_x"]), float(d["Cartn_y"]), float(d["Cartn_z"])], float(d.get("occupancy") or 1)))
                    except ValueError:
                        pass
                if atom != "CA":
                    continue
                if al not in (".", "A", "?"):
                    if altlocs:
                        try:
                            alt[ch].setdefault(int(d["auth_seq_id"]), {})[al] = (
                                [float(d["Cartn_x"]), float(d["Cartn_y"]), float(d["Cartn_z"])], float(d.get("occupancy") or 1))
                        except ValueError:
                            pass
                    continue
                try:
                    out[ch].setdefault(int(d["auth_seq_id"]), [float(d["Cartn_x"]), float(d["Cartn_y"]), float(d["Cartn_z"])])
                    if names is not None:
                        names[ch].setdefault(int(d["auth_seq_id"]), d.get("label_comp_id"))
                    if altlocs and al == "A":
                        alt[ch].setdefault(int(d["auth_seq_id"]), {})["A"] = (out[ch][int(d["auth_seq_id"])], float(d.get("occupancy") or 1))
                except ValueError:
                    pass
    if altlocs:
        return out, alt
    return out



def cif_categories(cif_gz):
    """Read the sequence mapping and connection categories, including quoted/multiline CIF values."""
    wanted = {"_struct_ref", "_struct_ref_seq", "_struct_ref_seq_dif", "_entity_poly", "_entity_poly_seq",
              "_struct_asym", "_struct_conn", "_pdbx_poly_seq_scheme"}
    result, singles = {}, {}
    with gzip.open(cif_gz, "rt") as fh:
        text = fh.read()
    # RCSB separates categories with #; retain only relevant blocks before tokenizing the large atom table.
    for block in re.split(r"^#\s*$", text, flags=re.M):
        if not any(re.search(r"^" + category + r"\.", block, re.M) for category in wanted):
            continue
        tokens, multiline = [], None
        for line in block.splitlines():
            if line.startswith(";"):
                if multiline is None:
                    multiline = [line[1:]]
                else:
                    tokens.append(("\n".join(multiline), True)); multiline = None
                continue
            if multiline is not None:
                multiline.append(line); continue
            for match in re.finditer(r"'(.*?)'(?=\s|$)|\"(.*?)\"(?=\s|$)|(\S+)", line):
                if match.group(3) and match.group(3).startswith("#"):
                    break
                tokens.append((next(v for v in match.groups() if v is not None), match.group(3) is None))
        i = 0
        def control(token):
            return not token[1] and (token[0].startswith(("_", "data_")) or token[0] in ("loop_", "stop_"))
        while i < len(tokens):
            token, quoted = tokens[i]
            if token == "loop_" and not quoted:
                i += 1; fields = []
                while i < len(tokens) and tokens[i][0].startswith("_") and not tokens[i][1]:
                    fields.append(tokens[i][0]); i += 1
                if not fields:
                    raise ValueError("CIF loop has no fields")
                while i < len(tokens) and not control(tokens[i]):
                    values = tokens[i:i + len(fields)]
                    if len(values) != len(fields) or any(control(v) for v in values):
                        raise ValueError("Incomplete CIF loop row")
                    category = fields[0].split(".")[0]
                    if category in wanted:
                        result.setdefault(category, []).append({f.split(".", 1)[1]: v[0] for f, v in zip(fields, values)})
                    i += len(fields)
            elif token.startswith("_") and not quoted:
                category, field = token.split(".", 1)
                if i + 1 >= len(tokens) or control(tokens[i + 1]):
                    raise ValueError("Missing CIF item value")
                if category in wanted:
                    singles.setdefault(category, {})[field] = tokens[i + 1][0]
                i += 2
            else:
                i += 1
    for category, row in singles.items():
        result.setdefault(category, []).append(row)
    return result


def tag_linker(seq):
    """Recognize common short cloning scars, His/epitope tags and flexible tag linkers."""
    tags = ("WSHPQFEK", "DYKDDDDK", "YPYDVPDYA", "EQKLISEEDL", "ENLYFQG", "LEVLFQGP", "LVPRGS")
    for tag in tags:
        seq = seq.replace(tag, "")
    seq = re.sub(r"H{4,}", "", seq)
    return not seq or bool(re.fullmatch(r"[GSAHM]*", seq))


def fused_covalent(cif_gz, chains, accession):
    """Return deposited unmapped segments and covalent connections for author chain IDs."""
    data = cif_categories(cif_gz)
    out = {c: {"fused": [], "covalent": []} for c in chains}
    refs = {r["id"]: r for r in data.get("_struct_ref", [])}
    poly = {r["entity_id"]: r for r in data.get("_entity_poly", [])}
    asym = {r["id"]: r["entity_id"] for r in data.get("_struct_asym", [])}
    seqs = {}
    for r in data.get("_entity_poly_seq", []):
        seqs.setdefault(r["entity_id"], {})[int(r["num"])] = AA1.get(r["mon_id"], "X")
    for entity, r in poly.items():
        if entity not in seqs:
            seq = re.sub(r"\s+", "", r.get("pdbx_seq_one_letter_code_can", r.get("pdbx_seq_one_letter_code", "")))
            seq = re.sub(r"\(([^)]+)\)", lambda m: AA1.get(m[1], "X"), seq)
            seqs[entity] = dict(enumerate(seq, 1))
    for chain in chains:
        entity = next((e for e, r in poly.items() if chain in r.get("pdbx_strand_id", "").split(",")), None)
        seq = seqs.get(entity, {})
        mapped, tags = set(), set()
        for r in data.get("_struct_ref_seq", []):
            ref = refs.get(r.get("ref_id"), {})
            acc = r.get("pdbx_db_accession", ref.get("pdbx_db_accession"))
            if acc == accession and chain in r.get("pdbx_strand_id", "").split(","):
                try:
                    mapped.update(range(int(r["seq_align_beg"]), int(r["seq_align_end"]) + 1))
                except (ValueError, KeyError):
                    pass
        if not mapped:
            for ref in refs.values():
                if ref.get("entity_id") != entity or ref.get("pdbx_db_accession") != accession:
                    continue
                segment = re.sub(r"\s+", "", ref.get("pdbx_seq_one_letter_code", ""))
                full = "".join(seq[i] for i in sorted(seq))
                if segment not in ("", "?", ".") and full.count(segment) == 1:
                    start = full.index(segment) + 1
                    mapped.update(range(start, start + len(segment)))
        for r in data.get("_struct_ref_seq_dif", []):
            if r.get("pdbx_pdb_strand_id") == chain and re.search(r"expression tag|cloning artifact|linker|purification tag", r.get("details", ""), re.I):
                try:
                    tags.add(int(r["seq_num"]))
                except (KeyError, ValueError):
                    pass
        if mapped:
            runs = []
            for i in sorted(set(seq) - mapped - tags):
                if not runs or i != runs[-1][-1] + 1:
                    runs.append([])
                runs[-1].append(i)
            for run in runs:
                segment = "".join(seq[i] for i in run)
                if len(run) >= 4 and not tag_linker(segment):
                    out[chain]["fused"].append(f"{segment} (label_seq_id {run[0]}-{run[-1]})")
    label_auth = {}
    for r in data.get("_pdbx_poly_seq_scheme", []):
        label_auth[r["asym_id"]] = r.get("pdb_strand_id", "")
    for label, entity in asym.items():
        auths = poly.get(entity, {}).get("pdbx_strand_id", "").split(",")
        if label not in label_auth and len(auths) == 1 and auths[0]:
            label_auth[label] = auths[0]
    standard = set(AA1) - {"MSE"}
    for r in data.get("_struct_conn", []):
        if r.get("conn_type_id") != "covale":
            continue
        ends = []
        for n in (1, 2):
            prefix = f"ptnr{n}_"
            label = r.get(prefix + "label_asym_id", "")
            auth = r.get(prefix + "auth_asym_id")
            if auth in (None, "?", "."):
                auth = label_auth.get(label) or label
            comp = r.get(prefix + "label_comp_id", r.get(prefix + "auth_comp_id", "?"))
            nonpoly = asym.get(label) not in poly and r.get(prefix + "label_seq_id", ".") in (".", "?")
            residue = r.get(prefix + "auth_seq_id", r.get(prefix + "label_seq_id", "?"))
            ends.append((auth, asym.get(label) in poly or not nonpoly, nonpoly or comp not in standard,
                         f"{auth}:{comp}{residue}"))
        for a, b in ((ends[0], ends[1]), (ends[1], ends[0])):
            if a[0] in out and a[1] and b[2]:
                value = f"{a[3]}--{b[3]} ({r.get('id', 'covale')})"
                if value not in out[a[0]]["covalent"]:
                    out[a[0]]["covalent"].append(value)
    return out

def renumber(d, rules):
    """apply [[lo, hi, delta], ...] to a {auth_seq_id: value} dict; residues outside every rule are dropped."""
    if not rules:
        return d
    out = {}
    for k, v in d.items():
        for lo, hi, delta in rules:
            if lo <= k <= hi:
                out[k + delta] = v
                break
    return out


def kabsch(P, Q):
    """rotation + translation that superposes P onto Q."""
    pc, qc = P.mean(0), Q.mean(0)
    U, _, Vt = np.linalg.svd((P - pc).T @ (Q - qc))
    d = np.sign(np.linalg.det(U @ Vt))
    R = U @ np.diag([1, 1, d]) @ Vt
    return R, pc, qc


def rng(spans):
    return [i for a, b in spans for i in range(a, b + 1)]


def dihedral(p0, p1, p2, p3):
    """dihedral angle in degrees, 0..360."""
    p0, p1, p2, p3 = (np.array(p) for p in (p0, p1, p2, p3))
    b0, b1, b2 = p0 - p1, p2 - p1, p3 - p2
    b1 = b1 / np.linalg.norm(b1)
    v = b0 - np.dot(b0, b1) * b1
    w = b2 - np.dot(b2, b1) * b1
    return float(np.degrees(np.arctan2(np.dot(np.cross(b1, v), w), np.dot(v, w))) % 360.0)


def rotamer(chi):
    return "g+" if chi < 120 else "t" if chi < 240 else "g-"


def chi1_of(resatoms, resname, al):
    """chi1 (deg) and lowest occupancy for one residue; atoms of altloc al, falling back to '.' (shared backbone atoms)."""
    gamma = CHI1_GAMMA.get(resname, "CG")
    pts = []
    for atom in ("N", "CA", "CB", gamma):
        src = resatoms.get(al, {}).get(atom) or resatoms.get(".", {}).get(atom)
        if src is None:
            return None, None
        pts.append(src)
    return dihedral(*(p[0] for p in pts)), min(p[1] for p in pts)


def state_class(entry_md, chain):
    ligs, ions, cof = [], [], []
    cofactor = set(CFG.get("cofactor") or [])
    for ne in entry_md.get("nonpolymer_entities") or []:
        cc = ne["nonpolymer_comp"]["chem_comp"]["id"]
        if chain in (ne["rcsb_nonpolymer_entity_container_identifiers"].get("auth_asym_ids") or []):
            if cc in cofactor:
                cof.append(cc); continue
            (ions if cc in IONS else ligs if cc not in SOLVENT or cc in CFG.get("count_as_ligand", []) else []).append(cc)
    partners = [pe["rcsb_polymer_entity"]["pdbx_description"] for pe in entry_md.get("polymer_entities") or []
                if not any(r.get("database_accession") == CFG["accession"] for r in (pe["rcsb_polymer_entity_container_identifiers"].get("reference_sequence_identifiers") or []))]
    cls = "complex" if partners else ("ligand-bound" if ligs else "apo")
    if cofactor:
        return cls, sorted(set(ligs)), sorted(set(ions)), partners, sorted(set(cof))
    return cls, sorted(set(ligs)), sorted(set(ions)), partners


MUT_RE = re.compile(r"\b([ACDEFGHIKLMNPQRSTVWY])(\d{1,3})([ACDEFGHIKLMNPQRSTVWY])\b")


def metadata_table(md, out_dir, e):
    """one row per mapped entry (all of metadata.json, not only the downloaded files)."""
    cofactor = set(CFG.get("cofactor") or [])
    rows = []
    for pid, m in sorted(md.items()):
        mine = [pe for pe in m.get("polymer_entities") or []
                if any(r.get("database_accession") == CFG["accession"] for r in (pe["rcsb_polymer_entity_container_identifiers"].get("reference_sequence_identifiers") or []))]
        partners = sorted({pe["rcsb_polymer_entity"]["pdbx_description"] for pe in m.get("polymer_entities") or [] if pe not in mine})
        ligs, cof = set(), set()
        for ne in m.get("nonpolymer_entities") or []:
            cc = ne["nonpolymer_comp"]["chem_comp"]["id"]
            if cc in cofactor:
                cof.add(cc)
            elif (cc not in SOLVENT and cc not in IONS) or cc in CFG.get("count_as_ligand", []):
                ligs.add(cc)
        mut_field = "; ".join((pe["rcsb_polymer_entity"].get("pdbx_mutation") or "") for pe in mine).strip("; ")
        title = m["struct"]["title"]
        mut_title = sorted({f"{a}{n}{b}" for a, n, b in MUT_RE.findall(title)}) if not mut_field else []
        cls = "complex" if partners else ("ligand-bound" if ligs else "apo")
        rows.append({"pdb": pid, "downloaded": (WORK / "structures" / e / "cif" / f"{pid}.cif.gz").exists(),
                     "method": m["rcsb_entry_info"].get("experimental_method"),
                     "resolution": (m["rcsb_entry_info"].get("resolution_combined") or [None])[0],
                     "cofactor": sorted(cof), "ligands": sorted(ligs), "partners": partners, "mutation": mut_field,
                     "mutation_from_title": mut_title, "class": cls, "title": title})
    (out_dir / f"{e}_metadata_all.json").write_text(json.dumps(rows, indent=1))
    lines = [f"# {e}: all {len(rows)} mapped entries from metadata.json ({sum(r['downloaded'] for r in rows)} downloaded)", "",
             "| PDB | file | method | Å | cofactor | class | ligands | partners | mutation (field) | mutation (title) | title |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['pdb']} | {'yes' if r['downloaded'] else '-'} | {r['method']} | {r['resolution'] or '-'} | {'+'.join(r['cofactor']) or 'none'} | {r['class']} | "
                     f"{', '.join(r['ligands']) or '-'} | {'; '.join(p[:40] for p in r['partners']) or '-'} | {r['mutation'] or '-'} | {', '.join(r['mutation_from_title']) or '-'} | {r['title'][:80]} |")
    (out_dir / f"{e}_metadata_all.md").write_text("\n".join(lines) + "\n")
    return rows


def main():
    global CFG
    CFG = json.loads(Path(sys.argv[1]).read_text())
    e = CFG["entry"]
    md = {m["rcsb_id"]: m for m in json.loads((WORK / "structures" / e / "metadata.json").read_text())}
    core, mobile = rng(CFG["core"]), rng(CFG["mobile"])
    use_alt, chi_res, use_cof = bool(CFG.get("altlocs")), list(CFG.get("sidechain_chi1") or []), bool(CFG.get("cofactor"))
    chains, resnames, renum = {}, {}, CFG.get("renumber") or {}
    altca, sidec, conf_of = {}, {}, {}
    detect, attachments = bool(CFG.get("detect_fused_covalent")), {}
    for pid, m in md.items():
        cif = WORK / "structures" / e / "cif" / f"{pid}.cif.gz"
        if not cif.exists():
            continue
        mine = [c for pe in m.get("polymer_entities") or []
                if any(r.get("database_accession") == CFG["accession"] for r in (pe["rcsb_polymer_entity_container_identifiers"].get("reference_sequence_identifiers") or []))
                for c in pe["rcsb_polymer_entity_container_identifiers"].get("auth_asym_ids") or []]
        if detect:
            attachments[pid] = fused_covalent(cif, mine, CFG["accession"])
        nm, sd = {}, ({} if chi_res else None)
        got = ca_coords(cif, mine, nm, altlocs=use_alt, side=sd)
        cas, alts = got if use_alt else (got, {})
        for c, xyz in cas.items():
            rules = renum.get(f"{pid}:{c}", renum.get(pid))
            xyz, nmc = renumber(xyz, rules), renumber(nm.get(c, {}), rules)
            if xyz:
                chains[f"{pid}:{c}"] = xyz
                resnames[f"{pid}:{c}"] = nmc
                if use_alt:
                    altca[f"{pid}:{c}"] = renumber(alts.get(c, {}), rules)
                if chi_res:
                    sidec[f"{pid}:{c}"] = renumber(sd.get(c, {}), rules)
    # conformer rows (opt-in): one extra key "PDB:chain:X" per altloc letter other than A/'.' seen at a mobile CA or a chi1 residue
    if use_alt:
        for key in list(chains):
            letters = set()
            for i, d in altca[key].items():
                if i in mobile:
                    letters |= set(d)
            for i in chi_res:
                letters |= set(sidec.get(key, {}).get(i, {}))
            for al in sorted(letters - {".", "A", "?"}):
                x, occ = dict(chains[key]), []
                for i, d in altca[key].items():
                    if i in mobile and al in d:
                        x[i] = d[al][0]; occ.append(d[al][1])
                chains[f"{key}:{al}"] = x
                resnames[f"{key}:{al}"] = resnames[key]
                conf_of[f"{key}:{al}"] = (key, al, occ)
    ref_o, ref_c = chains[CFG["open"]], chains[CFG["closed"]]
    verify = bool(CFG.get("verify_numbering"))
    ref_names = resnames[CFG["open"]]

    def dist(x, ref):
        cr = [i for i in core if i in x and i in ref]
        mv = [i for i in mobile if i in x and i in ref]
        if len(cr) < 20 or len(mv) < 5:
            return None, len(cr), len(mv)
        P, Q = np.array([x[i] for i in cr]), np.array([ref[i] for i in cr])
        R, pc, qc = kabsch(P, Q)
        M = (np.array([x[i] for i in mv]) - pc) @ R + qc
        return float(np.sqrt(((M - np.array([ref[i] for i in mv])) ** 2).sum(1).mean())), len(cr), len(mv)

    def chi1_text(key):
        """per-residue chi1 string and values. Base row: every altloc with occupancy; conformer row: altloc X (fallback A/'.')."""
        base, al, _ = conf_of.get(key, (key, None, None))
        parts, data = [], {}
        for i in chi_res:
            ra, rn = sidec.get(base, {}).get(i), resnames[base].get(i)
            if not ra or not rn or rn in ("GLY", "ALA"):
                continue
            if al is None:
                vals = []
                for a in sorted(set(ra) - {"."}) or ["."]:
                    chi, occ = chi1_of(ra, rn, a)
                    if chi is not None:
                        vals.append((a, round(chi), round(occ, 2)))
                if vals:
                    data[i] = vals
                    if len(vals) == 1:
                        parts.append(f"{AA1.get(rn, rn)}{i}:{rotamer(vals[0][1])}({vals[0][1] % 360 - 360 if vals[0][1] > 180 else vals[0][1]:+d})")
                    else:
                        parts.append(f"{AA1.get(rn, rn)}{i}:" + "/".join(f"{rotamer(c)}({c - 360 if c > 180 else c:+d},{a},{o})" for a, c, o in vals))
            else:
                chi, occ = chi1_of(ra, rn, al)
                if chi is None:
                    chi, occ = chi1_of(ra, rn, "A")
                if chi is not None:
                    c = round(chi)
                    data[i] = [(al, c, round(occ, 2))]
                    parts.append(f"{AA1.get(rn, rn)}{i}:{rotamer(chi)}({c - 360 if c > 180 else c:+d})")
        return "; ".join(parts), data

    rows = []
    for key, x in sorted(chains.items()):
        pid, ch = key.split(":")[:2]
        m = md[pid]
        do, ncore, nmob = dist(x, ref_o)
        dc, _, _ = dist(x, ref_c)
        sc = state_class(m, ch)
        cls, ligs, ions, partners = sc[:4]
        grow = (m.get("exptl_crystal_grow") or [{}])[0] or {}
        nmr = (m.get("pdbx_nmr_exptl_sample_conditions") or [{}])[0] or {}
        row_extra = {}
        if detect:
            row_extra.update(attachments[pid][ch])
            if row_extra["covalent"]:
                cls = "ligand-bound (covalent)"
            elif row_extra["fused"]:
                cls = "ligand-bound (fused)"
        if verify:
            shared = [i for i in core + mobile if i in resnames[key] and i in ref_names]
            row_extra["n_resname_mismatch"] = sum(resnames[key][i] != ref_names[i] for i in shared)
            row_extra["n_resname_compared"] = len(shared)
        if use_cof:
            row_extra["cofactor"] = sc[4]
        if use_alt:
            base, al, occ = conf_of.get(key, (key, None, None))
            row_extra["altloc"] = al or "base"
            row_extra["altloc_occ"] = None if not occ else round(sum(occ) / len(occ), 2)
            row_extra["n_mobile_altloc"] = sum(1 for i, d in altca.get(base, {}).items() if i in mobile and len(d) > 1)
        if chi_res:
            txt, data = chi1_text(key)
            row_extra["chi1"] = txt
            row_extra["chi1_values"] = {str(i): v for i, v in data.items()}
        rows.append({"chain": key, "class": cls, "ligands": ligs, "ions": ions, "partners": partners, **row_extra,
                     "mutation": "; ".join(pe["rcsb_polymer_entity"].get("pdbx_mutation") or "" for pe in m.get("polymer_entities") or []).strip("; "),
                     "method": m["rcsb_entry_info"].get("experimental_method"),
                     "resolution": (m["rcsb_entry_info"].get("resolution_combined") or [None])[0],
                     "pH": grow.get("pH") or nmr.get("pH"), "temp_K": ((m.get("diffrn") or [{}])[0] or {}).get("ambient_temp") or nmr.get("temperature"),
                     "title": m["struct"]["title"],
                     "rmsd_open": None if do is None else round(do, 2), "rmsd_closed": None if dc is None else round(dc, 2),
                     "closure": None if do is None or dc is None else round(do / (do + dc), 2), "n_core": ncore, "n_mobile": nmob})
    out = WORK / "outputs/pdb_states"; out.mkdir(parents=True, exist_ok=True)
    (out / f"{e}.json").write_text(json.dumps({"config": CFG, "chains": rows}, indent=1))
    extra_cols = ("| cofactor " if use_cof else "") + ("| altloc (occ) " if use_alt else "") + ("| chi1 " if chi_res else "")
    extra_cols += "| fused | covalent " if detect else ""
    extra_sep = "|---" * (use_cof + use_alt + bool(chi_res) + 2 * detect)
    lines = [f"# {e}: deposited structures between open {CFG['open']} and closed {CFG['closed']}", "",
             CFG.get("note", ""), "", f"| chain | class | ligands / partners | mutation | pH | T (K) | Å | RMSD open | RMSD closed | closure {extra_cols}|",
             f"|---|---|---|---|---|---|---|---|---|---{extra_sep}|"]
    for r in sorted(rows, key=lambda r: (r["closure"] is None, r["closure"] or 0)):
        ex = ""
        if use_cof:
            ex += f"| {'+'.join(r['cofactor']) or 'none'} "
        if use_alt:
            ex += f"| {r['altloc']}{' (' + str(r['altloc_occ']) + ')' if r['altloc_occ'] is not None else ''} "
        if chi_res:
            ex += f"| {r['chi1'] or '-'} "
        if detect:
            ex += f"| {'; '.join(r['fused']) or '-'} | {'; '.join(r['covalent']) or '-'} "
        lines.append(f"| {r['chain']} | {r['class']} | {', '.join(r['ligands'] + r['partners']) or '-'}{' (' + ','.join(r['ions']) + ')' if r['ions'] else ''} | {r['mutation'] or '-'} | {r['pH'] or '-'} | {r['temp_K'] or '-'} | {r['resolution'] or '-'} | {r['rmsd_open']} | {r['rmsd_closed']} | {r['closure']} {ex}|")
    (out / f"{e}.md").write_text("\n".join(lines) + "\n")
    summary = {"entry": e, "chains": len(rows), "apo": sum(r["class"] == "apo" for r in rows)}
    if verify:
        summary["chains_with_resname_mismatch_gt2"] = [r["chain"] for r in rows if r.get("n_resname_mismatch", 0) > 2]
    if use_alt:
        summary["conformer_rows"] = len(conf_of)
    if CFG.get("metadata_table"):
        summary["metadata_rows"] = len(metadata_table(md, out, e))
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
