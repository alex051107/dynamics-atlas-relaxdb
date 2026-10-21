#!/usr/bin/env python3
"""Source-number to UniProt/entry mapping with an explicit sequence alignment."""
import argparse
import json


def align(a, b):
    """Global alignment; ambiguity must be reviewed before biological use."""
    n, m = len(a), len(b)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): d[i][0] = -2 * i
    for j in range(m + 1): d[0][j] = -2 * j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = max(d[i-1][j-1] + (2 if a[i-1] == b[j-1] else -1),
                          d[i-1][j] - 2, d[i][j-1] - 2)
    mapping, mismatches, ambiguous = {}, [], False
    i, j = n, m
    while i or j:
        options = []
        if i and j and d[i][j] == d[i-1][j-1] + (2 if a[i-1] == b[j-1] else -1): options.append('diag')
        if i and d[i][j] == d[i-1][j] - 2: options.append('up')
        if j and d[i][j] == d[i][j-1] - 2: options.append('left')
        ambiguous |= len(options) > 1
        if options[0] == 'diag':
            mapping[i] = j
            if a[i-1] != b[j-1]: mismatches.append({'from': i, 'to': j, 'author_type': a[i-1], 'target_type': b[j-1]})
            i -= 1; j -= 1
        elif options[0] == 'up':
            mapping[i] = None; i -= 1
        else:
            j -= 1
    return {'positions': mapping, 'mismatches': mismatches, 'ambiguous_alignment': ambiguous}


def mapping(author, uniprot, entry, author_start=1, uniprot_start=1):
    au, ue = align(author, uniprot), align(uniprot, entry)
    rows = []
    for i in range(1, len(author) + 1):
        u = au['positions'].get(i)
        e = ue['positions'].get(u) if u else None
        rows.append({'author_number': author_start + i - 1, 'author_type': author[i-1],
                     'uniprot_number': uniprot_start + u - 1 if u else None,
                     'entry_position': e, 'entry_type': entry[e-1] if e else None,
                     'type_matches': bool(e and author[i-1] == entry[e-1])})
    return {'rows': rows, 'needs_review': au['ambiguous_alignment'] or ue['ambiguous_alignment']
            or bool(au['mismatches'] or ue['mismatches']),
            'author_to_uniprot': au, 'uniprot_to_entry': ue}


def self_test():
    r = mapping('ACDE', 'MACDE', 'ACDE', author_start=5)
    assert [(x['author_number'], x['uniprot_number'], x['entry_position']) for x in r['rows']] == [(5,2,1),(6,3,2),(7,4,3),(8,5,4)]
    assert all(x['type_matches'] for x in r['rows'])
    assert mapping('ACDE', 'ACNE', 'ACNE')['needs_review']
    assert align('AAA', 'AA')['ambiguous_alignment']
    assert align('', 'AC')['positions'] == {}
    print('residue alignment self-test PASS')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--self-test', action='store_true')
    ap.add_argument('--author'); ap.add_argument('--uniprot'); ap.add_argument('--entry')
    ap.add_argument('--author-start', type=int, default=1)
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not all((a.author, a.uniprot, a.entry)): ap.error('three explicitly sourced sequences required')
    print(json.dumps(mapping(a.author, a.uniprot, a.entry, a.author_start), indent=2))


if __name__ == '__main__': main()
