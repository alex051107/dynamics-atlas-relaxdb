#!/usr/bin/env python3
"""Deterministic identity/method searches and open-access source caching."""
import argparse
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import xml.etree.ElementTree as ET

WORK = Path(__file__).resolve().parents[1]
API = 'https://www.ebi.ac.uk/europepmc/webservices/rest/'


def get(url):
    last = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'DynamicsAtlas/1.0'}), timeout=35) as r:
                return r.read().decode('utf-8', 'replace')
        except Exception as e:
            last = e
            time.sleep(attempt + 1)
    raise RuntimeError(str(last))


def aliases(card):
    result = {'names': [card['name']], 'genes': [], 'organism': ''}
    acc = card.get('uniprot')
    if acc and re.fullmatch(r'[A-Z0-9]{6,10}', acc):
        try:
            d = json.loads(get('https://rest.uniprot.org/uniprotkb/' + acc + '.json'))
            desc = d.get('proteinDescription', {})
            for item in [desc.get('recommendedName', {})] + desc.get('alternativeNames', [])[:3]:
                name = item.get('fullName', {}).get('value')
                if name:
                    result['names'].append(name)
            result['genes'] = [g['geneName']['value'] for g in d.get('genes', []) if g.get('geneName')]
            result['organism'] = d.get('organism', {}).get('scientificName', '')
        except RuntimeError as e:
            result['identity_lookup_error'] = str(e)
        result['same_sequence'] = same_sequence(acc, result['organism'])
    result['names'] = list(dict.fromkeys(result['names']))
    return result


def same_sequence(acc, own):
    """E-031: Swiss-Prot entries with exactly this sequence (UniParc). Papers on them study the same protein, not a homolog
    (TRX: card P0AA29 Salmonella typhi is identical to E. coli TrxA P0AA25, which the literature uses)."""
    out = []
    try:
        upi = json.loads(get(f'https://rest.uniprot.org/uniparc/search?query=uniprotkb:{acc}&format=json&size=1'))['results'][0]['uniParcId']
        for c in json.loads(get(f'https://rest.uniprot.org/uniparc/{upi}/databases?format=json&size=200')).get('results', []):
            o = re.sub(r'\s*\(.*\)$', '', (c.get('organism') or {}).get('scientificName', ''))
            if c.get('database') == 'UniProtKB/Swiss-Prot' and c.get('active') and c.get('id') != acc and o and o != own:
                out.append({'accession': c.get('id'), 'organism': o,
                            'note': 'identical sequence to the entry: same protein (target or same_protein_other_construct), not a homolog'})
    except (RuntimeError, KeyError, IndexError, ValueError):
        pass
    return out[:6]


def fetch_source(pmcid):
    """Fetch only the archive's open-access XML endpoint; never a paywall."""
    if not re.fullmatch(r'PMC\d+', pmcid):
        raise ValueError('invalid PMCID')
    cache = WORK / 'sources_cache'
    cache.mkdir(exist_ok=True)
    xml = cache / (pmcid + '.xml')
    txt = cache / (pmcid + '.txt')
    if xml.exists() and txt.exists():
        return {'pmcid': pmcid, 'xml': xml.name, 'text': txt.name, 'cached': True}
    source_url = API + pmcid + '/fullTextXML'
    endpoint_failure = None
    try:
        raw = get(source_url)
    except RuntimeError as error:
        if not re.search(r'HTTP Error (404|50[0234])', str(error)): raise
        endpoint_failure = str(error)
        source_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=' + pmcid[3:]
        raw = get(source_url)
    tree = ET.fromstring(raw)
    article = tree if tree.tag == 'article' else tree.find('.//article')
    if article is None: raise ValueError('source endpoint has no article object')
    identifiers = {e.get('pub-id-type'): ''.join(e.itertext()).strip()
                   for e in article.findall('./front/article-meta/article-id')}
    if endpoint_failure and not any(identifiers.get(k, '').removeprefix('PMC') == pmcid[3:]
                                   for k in ('pmcid', 'pmc', 'pmcaid')):
        raise ValueError('fallback primary article identity mismatch')
    text = '\n'.join(' '.join(e.itertext()).strip() for e in tree.iter()
                     if e.tag in ('article-title', 'title', 'p', 'table', 'caption', 'label'))
    if len(text) < 200:
        raise ValueError('unreadable article XML')
    xml.write_text(raw)
    txt.write_text(text)
    (cache / (pmcid + '.source.json')).write_text(json.dumps({
        'url': source_url, 'retrieved_at': time.time(), 'article_identifiers': identifiers,
        'primary_endpoint_failure': endpoint_failure,
        'converter': 'stdlib ElementTree block text',
        'limitation': 'Inline formula/table layout must be verified in XML or original figure; SI separate.'}, indent=2))
    return {'pmcid': pmcid, 'xml': xml.name, 'text': txt.name, 'cached': False}


def query_plan(card, identity, recipe):
    names = identity['names'] + identity.get('genes', [])
    names = [n.replace('"', '') for n in names if n]
    identity_q = '(' + ' OR '.join(f'TITLE_ABS:"{n}"' for n in names) + ')'
    species = identity.get('organism', '').split('(')[0].strip().replace('"', '')
    # ponytail: canonical binomial and genus abbreviation; strain identity remains a worker judgment.
    words = species.split()
    variants = [species]
    if len(words) == 2:
        variants.append(words[0][0] + '. ' + words[1])
    for o in identity.get('same_sequence', []):  # E-031: organisms whose entry has the identical sequence
        w = o['organism'].split()
        variants += [o['organism']] + ([w[0][0] + '. ' + w[1]] if len(w) >= 2 else [])
    variants = list(dict.fromkeys(variants))
    species_q = ' AND (' + ' OR '.join('"' + s + '"' for s in variants) + ')' if species else ''
    return {method: identity_q + species_q + ' AND (' + ' OR '.join(f'"{word}"' for word in words) + ')'
            for method, words in recipe['methods'].items()}


def run(case, recipe_path=None):
    card = json.loads((case / 'input.json').read_text())
    recipe = json.loads((recipe_path or WORK / 'config/recipe.json').read_text())
    identity = aliases(card)
    (case / 'identity_aliases.json').write_text(json.dumps(identity, indent=2))
    target = case / 'prefetch'
    target.mkdir(exist_ok=True)
    plans = query_plan(card, identity, recipe)
    def search(pair):
        method, query = pair
        p = target / (method + '.json')
        search_id = 'epmc-' + hashlib.sha256((card['entry_id'] + method + query).encode()).hexdigest()[:16]
        if p.exists():
            old = json.loads(p.read_text())
            if old.get('query') == query and old.get('status') == 'ok':
                return old
        data = {'search_id': search_id, 'method_class': method, 'query': query,
                'channel': 'Europe PMC', 'date': time.strftime('%Y-%m-%d'), 'status': 'ok'}
        try:
            reply = json.loads(get(API + 'search?' + urllib.parse.urlencode({
                'query': query, 'format': 'json', 'resultType': 'core', 'pageSize': 100})))
            data.update(hits=reply.get('hitCount', 0), results=reply.get('resultList', {}).get('result', []))
        except Exception as e:
            data.update(status='error', hits=None, results=[], error=str(e))
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        return data
    with ThreadPoolExecutor(max_workers=2) as pool:
        result = list(pool.map(search, plans.items()))
    candidates = {}
    for r in result:
        for paper in r['results']:
            if paper.get('isOpenAccess') == 'Y' and paper.get('pmcid'):
                candidates.setdefault(paper['pmcid'], paper)
    cached = []
    # ponytail: cache up to eight OA candidates per case; worker fetches additional relevant originals.
    for pmcid in list(candidates)[:8]:
        try:
            cached.append(fetch_source(pmcid))
        except Exception as e:
            cached.append({'pmcid': pmcid, 'error': str(e)})
    (case / 'prefetch/cache_receipt.json').write_text(json.dumps(cached, indent=2))
    failures = sum(r['status'] != 'ok' for r in result)
    print(json.dumps({'entry': card['entry_id'], 'methods': len(result), 'failed_queries': failures,
                      'cached': sum('text' in r for r in cached)}))
    return 1 if failures else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', type=Path)
    ap.add_argument('--pmcid')
    ap.add_argument('--recipe', type=Path)
    a = ap.parse_args()
    if a.pmcid:
        print(json.dumps(fetch_source(a.pmcid)))
        return 0
    if not a.case:
        ap.error('--case or --pmcid required')
    return run(a.case.resolve(), a.recipe)


if __name__ == '__main__':
    raise SystemExit(main())
