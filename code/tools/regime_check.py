#!/usr/bin/env python3
"""Check reported exchange rates against angular shift differences without modifying source files.

  python3 tools/regime_check.py [--work PATH] [--output PATH]

Accept explicit units, ranges, +/- uncertainties and residue-labelled lists. Unpaired ranges give a conservative
outer envelope; matching residue lists are paired. Unsupported or ambiguous text is printed, never inferred.
MHz defaults to proton frequency; shift nucleus defaults to 15N. s-1 shift differences are already angular.
"""
import argparse
import csv
import json
import math
from pathlib import Path
import re

WORK = Path(__file__).resolve().parents[1]
RATIOS = {'1H': 1.0, '15N': 0.10136, '13C': 0.25145}
PROTON_MHZ_T = 42.57747892
NUMBER = r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
UNIT = r'rad\s*/\s*s|s\s*\^?\s*-\s*1|1\s*/\s*s|Hz|ppm|MHz|T'
QUANTITY = re.compile(rf'({NUMBER})(?:\s*(\+/-|±|to|-)\s*({NUMBER}))?\s*({UNIT})?(?![\w])', re.I)
NUCLEUS = re.compile(r'\b(15\s*N|13\s*C|1\s*H)\b', re.I)
COLUMNS = ['entry', 'judgment_id', 'kex_text', 'delta_omega_text', 'field_used', 'ratio_range', 'regime', 'literal_two_peak']


def normalized(text):
    return str(text).translate(str.maketrans({'−': '-', '–': '-', '—': '-', '⁻': '-', '¹': '1', 'Δ': 'delta'}))


def isotope(text, default):
    found = {re.sub(r'\s', '', m[0]).upper() for m in NUCLEUS.finditer(text)}
    if len(found) > 1:
        raise ValueError('multiple nuclei; cannot assign quantities to one nucleus')
    return next(iter(found), default)


def quantities(text, allowed):
    """Parse only explicit numeric expressions; reject leftover numbers and unexplained qualifiers."""
    text = normalized(text).strip()
    if not text or re.search(r'[<>≤≥~≈]|\b(?:about|approximately)\b', text, re.I):
        raise ValueError('missing value or approximate/open bound')
    text = NUCLEUS.sub('', text)
    text = re.sub(r'\b(?:kex|k_ex|delta_omega|delta|field|B0|nu_H|nu_N|nu_C)\b', '', text, flags=re.I)
    text = re.sub(r'\b(?:and|or)\b', ',', text, flags=re.I)
    text = re.sub(r'\(\s*\)', '', text)
    chunks = re.split(r';|\n|,(?=\s*(?:[A-Z]\d+|[A-Z][a-z]{2}\d+))', text)
    result = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        label = ''
        match = re.match(r'^([A-Z]\d+|[A-Z][a-z]{2}\d+)\s*[:=]?\s*', chunk)
        if match:
            label, chunk = match[1], chunk[match.end():]
        values, end = [], 0
        for match in QUANTITY.finditer(chunk):
            gap = chunk[end:match.start()]
            if values and not re.search(r'[,/]', gap):
                raise ValueError('adjacent numbers without a list separator')
            if gap.strip(' ,:/=()[]'):
                raise ValueError(f'unsupported quantity text: {gap.strip()}')
            a, operator, b, unit = match.groups()
            a = float(a)
            if b is None:
                lo = hi = a
            elif operator in ('±', '+/-'):
                lo, hi = a - abs(float(b)), a + abs(float(b))
            else:
                lo, hi = sorted((a, float(b)))
            values.append([label, lo, hi, unit])
            end = match.end()
        if not values or chunk[end:].strip(' ,:/=()[]'):
            raise ValueError(f'unsupported quantity text: {chunk[end:].strip() or chunk}')
        result.extend(values)
    units = {re.sub(r'\s|\^', '', v[3]).lower() for v in result if v[3]}
    if not units:
        raise ValueError('number without units')
    for value in result:
        if value[3] is None:
            if len(units) != 1:
                raise ValueError('ambiguous shared units')
            value[3] = next(iter(units))
        else:
            value[3] = re.sub(r'\s|\^', '', value[3]).lower()
        if value[3] not in allowed:
            raise ValueError(f'unsupported units: {value[3]}')
        if not all(math.isfinite(n) for n in value[1:3]):
            raise ValueError('non-finite value')
    if not result:
        raise ValueError('no quantities')
    return result


def regime(lo, hi):
    names = []
    if lo < 0.3:
        names.append('slow')
    if hi >= 0.3 and lo <= 3:
        names.append('intermediate')
    if hi > 3:
        names.append('fast')
    return '/'.join(names)


def calculate(detection):
    ktext, dtext, ftext = (detection.get(key, '') for key in ('kex', 'delta_omega', 'field'))
    if not all(isinstance(s, str) for s in (ktext, dtext, ftext)):
        raise ValueError('quantities must be reported text with units')
    context = ' '.join(str(detection.get(k, '')) for k in ('nucleus', 'method', 'observable'))
    delta_nucleus = isotope(normalized(dtext), None) or isotope(context, '15N')
    field_nucleus = isotope(normalized(ftext), '1H')
    parsed = []
    for key, text, units in (('kex', ktext, {'s-1', '1/s', 'hz'}),
                             ('delta_omega', dtext, {'ppm', 'hz', 's-1', '1/s', 'rad/s'}),
                             ('field', ftext, {'mhz', 't'})):
        try:
            parsed.append(quantities(text, units))
        except ValueError as exc:
            raise ValueError(f'{key}: {exc}') from exc
    rates, shifts, fields = parsed
    frequency = []
    for label, lo, hi, unit in fields:
        if label or lo <= 0:
            raise ValueError('invalid field or residue-labelled field')
        factor = PROTON_MHZ_T if unit == 't' else 1 / RATIOS[field_nucleus]
        frequency.extend((lo * factor, hi * factor))
    fmin, fmax = min(frequency), max(frequency)
    angular = []
    for label, lo, hi, unit in shifts:
        if lo <= 0 <= hi:
            raise ValueError('shift interval includes zero')
        lo, hi = sorted((abs(lo), abs(hi)))
        if unit == 'ppm':
            lo *= 2 * math.pi * RATIOS[delta_nucleus] * fmin
            hi *= 2 * math.pi * RATIOS[delta_nucleus] * fmax
        elif unit == 'hz':
            lo *= 2 * math.pi
            hi *= 2 * math.pi
        angular.append((label, lo, hi))
    klabels, dlabels = {r[0] for r in rates}, {r[0] for r in angular}
    if '' not in klabels and len(klabels) != len(rates) or '' not in dlabels and len(dlabels) != len(angular):
        raise ValueError('repeated residue label; condition pairing ambiguous')
    if klabels != {''} and dlabels != {''} and klabels != dlabels:
        raise ValueError('residue lists do not match')
    if '' in klabels and len(klabels) > 1 or '' in dlabels and len(dlabels) > 1:
        raise ValueError('mixed labelled and unlabelled values')
    ratios = []
    for kl, klo, khi, _ in rates:
        if klo <= 0:
            raise ValueError('non-positive exchange rate')
        for dl, dlo, dhi in angular:
            if kl and dl and kl != dl:
                continue
            ratios.extend((klo / dhi, khi / dlo))
    lo, hi = min(ratios), max(ratios)
    field = f'{ftext}; {fmin:g}-{fmax:g} MHz 1H; shift nucleus {delta_nucleus}'
    return lo, hi, regime(lo, hi), field


def literal_word(text):
    if not isinstance(text, str) or not text.strip():
        return ''
    return text.strip().split()[0].rstrip(':;,').lower()


def is_conflict(literal, computed):
    return (literal == 'qualifies' and computed == 'fast') or (literal == 'does' and computed == 'slow')


def scan(work, output):
    """Read source judgments and alternate-state text, write only the requested CSV."""
    literal, ambiguous = {}, set()
    for path in sorted((work / 'outputs').glob('alt_apo_states_*.json')):
        data = json.loads(path.read_text())
        if not isinstance(data, list):
            print(f'UNPARSEABLE {path.name}: expected a list of alternate-state rows')
            continue
        for row in data:
            entry = row.get('entry', '')
            text = row.get('literal_two_peak', '')
            word = literal_word(text)
            if word == 'does' and not re.match(r'^does\s+not\b', str(text).strip(), re.I):
                word = ''
            if entry in literal and literal[entry] != word:
                ambiguous.add(entry)
            literal[entry] = word
    rows, conflicts, skipped = [], [], []
    for path in sorted((work / 'outputs/judgment_v0').glob('*.json')):
        if path.name.endswith('.check.json'):
            continue
        data = json.loads(path.read_text())
        if not isinstance(data, dict) or not isinstance(data.get('judgments'), list):
            print(f'UNPARSEABLE {path.name}: expected judgments list')
            continue
        for judgment in data['judgments']:
            entry = judgment.get('entry_id') or path.stem
            jid = judgment.get('judgment_id', '')
            detection = judgment.get('detection') or {}
            try:
                lo, hi, state, field = calculate(detection)
            except (ValueError, TypeError) as exc:
                reason = f'{entry} {jid}: {exc}'
                skipped.append(reason)
                print('UNPARSEABLE ' + reason)
                continue
            word = literal.get(entry, '') if entry not in ambiguous else ''
            if not word:
                print(f'UNPARSEABLE {entry} {jid}: missing/ambiguous literal_two_peak; conflict not evaluated')
            row = dict(zip(COLUMNS, (entry, jid, detection['kex'], detection['delta_omega'], field,
                                     f'{lo:.8g}-{hi:.8g}', state, word)))
            rows.append(row)
            if is_conflict(word, state):
                conflicts.append(row)
                print(f'CONFLICT {entry} {jid}: {word}, computed {state}, ratio {row["ratio_range"]}')
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({'rows': len(rows), 'conflicts': len(conflicts), 'unparseable': len(skipped), 'output': str(output)}))
    return rows, conflicts, skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work', type=Path, default=WORK)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    scan(args.work, args.output or args.work / 'outputs/regime_check.csv')


if __name__ == '__main__':
    main()
