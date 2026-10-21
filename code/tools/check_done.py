#!/usr/bin/env python3
"""Only report completion from located campaign receipts and delivered artifacts."""
import json
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
TASK = Path('<workspace>/autoresearch/tasks/dynamics_atlas_stage1_loop_20261002')


def read(p, default):
    try:
        return json.loads(p.read_text())
    except (OSError, ValueError):
        return default


def check():
    missing = []
    for label, folder, n in [('C1', 'gina_review_20261005', 2), ('C2', 'atlas_10_20261008', 10)]:
        p = WORK / 'outputs' / folder
        manifest = read(p / 'manifest.json', {})
        try:
            completed = datetime.fromisoformat(manifest.get('built_at', '').replace('Z', '+00:00')).astimezone(ZoneInfo('America/New_York'))
            deadline = datetime(2026,10,5 if label=='C1' else 8,23,59,59,tzinfo=ZoneInfo('America/New_York'))
            if completed > deadline: missing.append(label + ': delivery deadline missed')
        except (ValueError, TypeError):
            missing.append(label + ': actual build timestamp missing')
        if len(set(manifest.get('entries', []))) != n:
            missing.append(label + ': complete entry manifest missing')
        expected = ['atlas.xlsx', 'atlas_rows.csv'] if label == 'C2' else ['atlas.xlsx', 'REPLY_GINA_EN.md']
        for filename in expected:
            if not (p / filename).is_file() or not (TASK / 'outputs' / folder / filename).is_file():
                missing.append(label + ': delivered ' + filename + ' missing')
        if len(list(p.glob('*.html'))) < n:
            missing.append(label + ': printable summaries missing')
        if manifest.get('integrity_pass') is not True:
            missing.append(label + ': source integrity not established')
        if not manifest.get('checkpoint_complete') and label == 'C2':
            missing.append('C2: checkpoint judge/residue comparison pending')
    iterations = []
    p = WORK / 'ledger/iterations.jsonl'
    if p.exists():
        for line in p.read_text().splitlines():
            try:
                iterations.append(json.loads(line))
            except ValueError:
                missing.append('C3: malformed iteration ledger')
    closed = {r.get('iteration') for r in iterations if r.get('iteration', 0) >= 1
              and r.get('decision') in ('keep', 'revert') and r.get('evidence') and r.get('evaluated') is True}
    if len(closed) < 12:
        missing.append(f'C3: {len(closed)}/12 evaluated iterations closed')
    sealed = read(WORK / 'ledger/sealed_final.json', {})
    if sealed.get('runs') != 8 or sealed.get('all_completed') is not True or sealed.get('judge_complete') is not True:
        missing.append('C3: eight sealed final runs/evaluation incomplete')
    final_prompt = (WORK / 'config/active_prompt.txt').read_text().strip() if (WORK / 'config/active_prompt.txt').exists() else ''
    if sealed.get('version') != final_prompt:
        missing.append('C3: sealed version differs from retained final version')
    for name in ('FINAL_REPORT_ZH.md', 'FINAL_SUMMARY_EN.md'):
        if not (WORK / 'outputs' / name).is_file() or not (TASK / 'outputs' / name).is_file():
            missing.append('C3: delivered ' + name + ' missing')
    if not read(WORK / 'ledger/setup_status.json', {}).get('trusted_worker_hook_verified'):
        missing.append('Setup: trusted worker hook receipt missing')
    for item in missing:
        print(item)
    if not missing:
        print('C1 package ready for Alex; C2 and C3 verified. Sending remains Alex\'s responsibility.')
    return 1 if missing else 0


if __name__ == '__main__':
    raise SystemExit(check())
