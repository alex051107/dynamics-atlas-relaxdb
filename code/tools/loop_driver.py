#!/usr/bin/env python3
"""Restartable Stage-1 scheduler; bounded jobs, explicit receipts, no goal loop."""
import argparse
import difflib
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import time

WORK = Path(__file__).resolve().parents[1]
LEDGER = WORK / 'ledger'
EVAL = Path.home() / 'dynamics_atlas_eval'
TASK = Path('<workspace>/autoresearch/tasks/dynamics_atlas_stage1_loop_20261002')
sys.path.insert(0, str(EVAL / 'runner'))
import run_worker as runner


def read(p, default=None):
    try: return json.loads(Path(p).read_text())
    except (OSError, ValueError): return default


def rows(p):
    if not Path(p).exists(): return []
    return [json.loads(x) for x in Path(p).read_text().splitlines() if x.strip()]


def write(p, value):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2))
    tmp.replace(p)


def log(event, **fields):
    runner.append_jsonl(LEDGER / 'events.jsonl', {'ts': time.time(), 'event': event, **fields})


def state(**changes):
    s = read(LEDGER / 'state.json', {}) or {}
    s.update(changes, updated_at=time.time())
    write(LEDGER / 'state.json', s)
    return s


def pause(reason):
    state(status='paused', pause_reason=reason)
    log('WAIT_FOR_ALEX', reason=reason)
    raise RuntimeError(reason)


def command(args, timeout=None):
    p = subprocess.run(args, cwd=WORK, capture_output=True, text=True, timeout=timeout)
    log('command', program=Path(args[1] if len(args) > 1 else args[0]).name, rc=p.returncode)
    return p


def check_launch(worker=True):
    if runner.stopped(): pause('STOP exists')
    guard = runner.leak_guard()
    if not guard['allowed']: pause(guard['reason'] + f" ({guard['count']} helpers)")
    if worker and runner.runs_used() >= int(runner.auth()['run_cap']): pause('run cap reached')
    setup = read(LEDGER / 'setup_status.json', {}) or {}
    if not setup.get('trusted_worker_hook_verified'): pause('Trust Atlas hooks and verify real worker hook smoke first')
    if not setup.get('runner_smoke_verified'): pause('Runner real smoke must pass before campaign launch')


def run_batch(iteration, kind, version=None, **kwargs):
    development_draft = iteration == 0 and kind == 'dev' and bool(kwargs.get('entries')) and set(kwargs['entries']) <= {'AQADK_CPMG', 'CHEY_CPMG'}
    if iteration == 0 and kind == 'dev' and not development_draft:
        raise RuntimeError('Initial development batch is restricted to the two review proteins')
    milestone = f'batch_i{iteration:02}_{kind}'
    s = read(LEDGER / 'state.json', {}) or {}
    completed = s.get('completed_steps', {})
    if milestone in completed:
        spec = read(LEDGER / 'batches' / (completed[milestone] + '.json'))
        if spec.get('summary',{}).get('rule',{}).get('decision') == 'needs_judge':
            command([sys.executable, str(EVAL / 'runner/run_worker.py'), 'rejudge', spec['batch_id']])
            spec = read(LEDGER / 'batches' / (completed[milestone] + '.json'))
        return spec
    check_launch()
    references=read(LEDGER/'reference_judge_status.json',{}) or {}
    if not development_draft and (references.get('scope')!='all' or references.get('completed') is not True):
        pause('Reference pool judging must finish and be frozen before evaluated worker batches')
    bid = s.get('batch') if s.get('batch_step') == milestone else None
    if not bid:
        args = [sys.executable, str(EVAL / 'runner/run_worker.py'), 'batch', 'start', '--iter', str(iteration), '--kind', kind]
        if version: args += ['--version', version]
        for key, value in kwargs.items():
            if value is not None:
                args += ['--' + key.replace('_', '-')]
                args += list(value) if isinstance(value, list) else [str(value)]
        p = command(args)
        if p.returncode: pause('batch launch refused: ' + p.stdout[-500:])
        info = json.loads(p.stdout.strip().splitlines()[-1])
        bid = info['batch_id']
        state(batch=bid, batch_step=milestone)
    while True:
        if runner.stopped():
            command([sys.executable, str(EVAL / 'runner/run_worker.py'), 'abort-all'])
            pause('STOP exists')
        spec = read(LEDGER / 'batches' / (bid + '.json')) or {}
        if spec.get('status') != 'running': break
        if not runner.batch_status(bid).get('process_alive'): pause('batch process exited without completion')
        time.sleep(15)
    if spec.get('status') != 'complete' or any(j.get('result', {}).get('status') != 'done' for j in spec['jobs']):
        pause('batch has incomplete/failed jobs: ' + bid)
    completed = (read(LEDGER / 'state.json', {}) or {}).get('completed_steps', {})
    completed[milestone] = bid
    state(completed_steps=completed, batch=None)
    return spec


def close(iteration, decision, change_type, evidence, **kwargs):
    runner.append_jsonl(LEDGER / 'iterations.jsonl', {'iteration': iteration, 'decision': decision,
        'change_type': change_type, 'evidence': evidence, 'evaluated': True, 'ts': time.time(), **kwargs})
    log('iteration_closed', iteration=iteration, decision=decision)


def release_batch(batch_id, decision='keep'):
    # Frozen release needs a decision first; this is not a closed evaluated round.
    if not any(r.get('decision') == decision and
               (r.get('batch_id') == batch_id or r.get('evidence') == batch_id)
               for r in rows(LEDGER / 'iterations.jsonl')):
        runner.append_jsonl(LEDGER / 'iterations.jsonl', {'event': 'decision_pending_release',
            'batch_id': batch_id, 'decision': decision, 'evidence': batch_id,
            'evaluated': False, 'ts': time.time()})
    p = command([sys.executable, str(EVAL / 'runner/run_worker.py'), 'release', batch_id])
    if p.returncode: pause('release failed')


def release(spec, iteration, change_type, decision='keep', **kwargs):
    release_batch(spec['batch_id'], decision)
    close(iteration, decision, change_type, spec['batch_id'], **kwargs)


def finish_iteration():
    pending = (read(LEDGER / 'state.json', {}) or {}).get('pending_iteration')
    if not pending: return
    i, decision = pending['iteration'], pending['decision']
    if any(r.get('iteration') == i and r.get('decision') in ('keep', 'revert') and r.get('evaluated') is True
           for r in rows(LEDGER / 'iterations.jsonl')):
        state(pending_iteration=None)
        return
    proposal, error = pending['proposal'], pending['error']
    if pending.get('batch_id'):
        release_batch(pending['batch_id'], decision)
        collect_errors(read(LEDGER / 'batches' / (pending['batch_id'] + '.json')))
    if decision == 'keep':
        (WORK / 'config/active_prompt.txt').write_text(proposal['candidate'] + '\n')
        errors = rows(LEDGER / 'errors.jsonl')
        for e in errors:
            if e['id'] == error['id']: e.update(closed=True, closed_iteration=i)
        path = LEDGER / 'errors.jsonl'
        tmp = path.with_suffix('.jsonl.tmp')
        tmp.write_text(''.join(json.dumps(e) + '\n' for e in errors))
        tmp.replace(path)
    else:
        rollback(proposal)
        failures = (read(LEDGER / 'state.json', {}) or {}).get('target_failures', {})
        failures[error['id']] = pending['target_failures']
        state(target_failures=failures)
    close(i, decision, proposal['change_type'], pending['evidence'], **pending['close_fields'])
    state(pending_iteration=None)


def collect_errors(spec):
    known = {(e.get('case_dir'), e.get('class'), e.get('kind'), e.get('row'), e.get('field')) for e in rows(LEDGER / 'errors.jsonl')}
    counter = len(rows(LEDGER / 'errors.jsonl'))
    for j in spec['jobs']:
        name = j.get('result', {}).get('case')
        if not name: continue
        sc = read(WORK / 'cases' / name / 'scorecard.json', {}) or {}
        if sc.get('visibility') != 'full': continue
        error_list = [dict(e, **{'class': 'integrity'}) for e in sc.get('integrity', {}).get('errors', [])]
        error_list += [{'class': k, 'detail': 'released class count: ' + str(v)} for k, v in sc.get('error_classes', {}).items()
                       if v and k != 'integrity']
        if (WORK / 'cases' / name / 'native_judge.json').is_file():
            import subagent_judge
            error_list += subagent_judge.error_records(WORK / 'cases' / name)
        for e in error_list:
            key = (name, e['class'], e.get('kind'), e.get('row'), e.get('field'))
            if key in known: continue
            counter += 1
            runner.append_jsonl(LEDGER / 'errors.jsonl', dict(e, id=f'E-{counter:03}', case_dir=name,
                               entry=j['entry'], closed=False))
            known.add(key)


def helper(tag, prompt, cwd, add_dirs=()):
    check_launch(worker=False)
    cwd.mkdir(parents=True, exist_ok=True)
    args = [runner.CODEX, 'exec', '--skip-git-repo-check', '--json', '-s', 'workspace-write']
    for p in add_dirs: args += ['--add-dir', str(p)]
    args += runner.codex_overrides('high') + ['-']
    event_tag = tag + '_' + str(time.time_ns())
    rc, status_, wall = runner.spawn(args, cwd, prompt, 3600, cwd / (event_tag + '.events.jsonl'), event_tag)
    log('helper', role=tag, rc=rc, status=status_, wall_s=wall)
    if rc or status_ != 'exited': pause(tag + ' failed')


def summary_pairs(cases):
    pairs = []
    for entry in ('AQADK_CPMG', 'CHEY_CPMG'):
        old = next((c for c in package_cases('C1') if read(c / 'input.json')['entry_id'] == entry), None)
        new = next((c for c in cases if read(c / 'input.json')['entry_id'] == entry), None)
        if old is None or new is None or old.resolve() == new.resolve():
            raise ValueError('Checkpoint requires distinct C1 and current cases for ' + entry)
        pairs.append((entry, old, new))
    return pairs


def export(kind, specs, checkpoint=False):
    folder = 'gina_review_20261005' if kind == 'C1' else 'atlas_10_20261008'
    dest = WORK / 'outputs' / folder
    cases = [WORK / 'cases' / j['result']['case'] for spec in specs for j in spec['jobs'] if j.get('result', {}).get('case')]
    pairs = summary_pairs(cases) if checkpoint else []
    tool = WORK / 'tools/export_package.py'
    if not tool.exists():
        prompt = '''Implement tools/export_package.py using stdlib or already installed openpyxl, no installs.
CLI: --output DIR --cases CASEDIR... . For each supplied dev case only, read rows.jsonl, coverage.json,
summary.md, input.json, scorecard.json and not_read_in_full.json. Refuse non-dev cases and failed integrity.
Write atlas_rows.csv, atlas.xlsx (evidence_rows, method_coverage, relaxdb_issues, not_read_in_full), one
printable HTML per protein, review_papers.json (at most8 priority studies per protein; rest appendix),
manifest.json with entries, integrity_pass, built_at as ISO8601 UTC, and source cases/version. HTML-escape content and make summary row ids inspectable.
For C1 write REPLY_GINA_EN.md at most5 sentences asking for missing key papers, incorrect quantities or
conditions and whether reported dataset issues are real. Include in relaxdb_issues these USER-REPORTED,
UNVERIFIED issues from the adopted execution order:7/10 residue annotations differ between dataset
versions; phosphate-buffer column contradicts; MesoAdK vs Aquifex, BLAC labelled TEM-1, RNase species,
ArgKin3 residue/UniProt differences, KRAS missing UniProt, HtrA2 construct. Do not access dataset websites
or hidden reference data to verify these claims. Preserve exact uncertainty labels. CheY Table2 residues
must have been newly source-extracted and typed; refuse C1 if no Table2 row locator/type check exists.
Add --self-test using synthetic data outside cases and no network. Do not create method documents.'''
        helper('write_export', prompt, LEDGER / 'export_builder', [WORK / 'tools'])
    p = command([sys.executable, str(tool), '--self-test'])
    if p.returncode: pause('export self-test failed')
    p = command([sys.executable, str(tool), '--output', str(dest), '--cases'] + [str(c) for c in cases])
    if p.returncode: pause('export failed: ' + p.stderr[-400:])
    manifest = read(dest / 'manifest.json', {}) or {}
    if checkpoint:
        checks = []
        # Public labels via scorer only; CheY is explicitly excluded from this diagnostic.
        for c in cases:
            card = read(c / 'input.json')
            if card['entry_id'] != 'CHEY_CPMG':
                checks.append({'entry': card['entry_id'], 'rc': command([sys.executable, str(EVAL / 'eval/score.py'), str(c), '--checkpoint']).returncode})
        for entry, old, new in pairs:
            p = command([sys.executable, str(runner.JUDGE), 'synthesis', '--iter', '6', '--a', str(old), '--b', str(new)])
            checks.append({'summary_pair': entry, 'a_case': old.name, 'b_case': new.name,
                           'a_version': read(old/'run.json')['prompt_version'],
                           'b_version': read(new/'run.json')['prompt_version'],
                           'rc': p.returncode, 'aggregate': p.stdout[-800:]})
        write(LEDGER / 'checkpoint.json', checks)
        manifest['checkpoint_complete'] = bool(checks) and all(c['rc'] == 0 for c in checks)
        write(dest / 'manifest.json', manifest)
        if not manifest['checkpoint_complete']:
            pause('C2 checkpoint incomplete; retain cases and resume judging before advancing')
    shutil.copytree(dest, TASK / 'outputs' / folder, dirs_exist_ok=True)
    state(**{kind: {'ready': True, 'folder': folder, 'cases': [c.name for c in cases]}})
    if kind == 'C1': log('WAIT_FOR_ALEX', reason='C1 ready; sending is outside scheduler scope')


def ensure_c2():
    s = read(LEDGER / 'state.json', {}) or {}
    if s.get('C2', {}).get('ready'): return
    version = s.get('c2_version') or (WORK / 'config/active_prompt.txt').read_text().strip()
    state(c2_version=version)
    entries = (WORK / 'config/dev_ids.txt').read_text().split()
    spec = run_batch(6, 'dev', version, entries=entries)
    if {j.get('version') for j in spec['jobs']} != {version}:
        pause('C2 cached batch version differs from its pinned version')
    export('C2', [spec], checkpoint=True)


def package_cases(kind):
    s = read(LEDGER / 'state.json', {}) or {}
    return [WORK / 'cases' / c for c in s.get(kind, {}).get('cases', [])]


def inventory():
    return {str(p.relative_to(WORK)): p.read_bytes() for folder in ('tools', 'prompts', 'config')
            for p in (WORK / folder).rglob('*') if p.is_file() and '__pycache__' not in str(p)}


def sentence_changes(old, new):
    a, b = [re.split(r'(?<=[.!?。！？])\s+', x) for x in (old, new)]
    count = 0
    for tag, i, j, k, l in difflib.SequenceMatcher(a=a, b=b).get_opcodes():
        if tag != 'equal': count += max(j-i, l-k)
    return count


def propose(i, error, old_version):
    candidate = f'worker_i{i:02d}'
    folder = LEDGER / 'improvers' / f'i{i:02d}'
    proposal_path = LEDGER / 'proposals' / f'i{i:02d}.json'
    saved=read(proposal_path,{}) or {}
    if saved.get('old_version')==old_version and saved.get('error_id')==error['id'] and saved.get('after_hash'):
        if all((WORK/name).is_file() and hashlib.sha256((WORK/name).read_bytes()).hexdigest()==digest
               for name,digest in saved['after_hash'].items()):
            return saved
        pause('Saved pending proposal changed; inspect before resuming, do not launch another improver')
    before = inventory()
    context = {'error': error, 'active_prompt': (WORK / 'prompts' / (old_version + '.md')).read_text(),
               'released_cases': [p.parent.name for p in (WORK / 'cases').glob('*/.released')],
               'prior_iterations': rows(LEDGER / 'iterations.jsonl')}
    prompt = ('You are the improver, not a protein researcher. Fix exactly one located open error using one file '
              'in prompts, config/recipe.json, or tools. Do not inspect other inputs/cases or reference data. '
              f'For prompt changes create prompts/{candidate}.md from the active prompt, change at most5 sentences '
              'and keep length<=6000. For recipe changes edit only config/recipe.json. For tool changes choose a '
              'standalone tool with --self-test and --case CLI; do not edit the driver or check_done.py. '
              f'Write {proposal_path} with error_id,change_type(prompt|recipe|tool),summary,files(relative paths). '
              'No new method documents. You may read only the released error case and relevant released details.\n' + json.dumps(context))
    helper(f'improver_i{i:02d}', prompt, folder, [WORK / 'prompts', WORK / 'config', WORK / 'tools', LEDGER])
    proposal = read(proposal_path, {}) or {}
    after = inventory()
    changed = {k for k in set(before)|set(after) if before.get(k) != after.get(k)}
    allowed = set(proposal.get('files', []))
    valid = bool(changed) and changed == allowed and len(changed) == 1 and proposal.get('error_id') == error['id']
    kind = proposal.get('change_type')
    for name in changed:
        p = WORK / name
        if kind == 'prompt':
            valid &= name == f'prompts/{candidate}.md' and len(p.read_text()) <= 6000
            valid &= sentence_changes(context['active_prompt'], p.read_text()) <= 5
        elif kind == 'recipe': valid &= name == 'config/recipe.json'
        elif kind == 'tool': valid &= name.startswith('tools/') and name not in ('tools/loop_driver.py','tools/check_done.py')
        else: valid = False
    backup = LEDGER / 'proposal_backups' / f'i{i:02d}'
    backup.mkdir(parents=True, exist_ok=True)
    for name in changed:
        if name in before:
            p = backup / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(before[name])
    if not valid:
        restore(before, changed)
        rejected = LEDGER / 'proposals' / ('rejected_i' + str(i) + '_' + str(time.time_ns()) + '.json')
        write(rejected, proposal)
        log('invalid_proposal', iteration=i, actual_files=sorted(changed), proposal=proposal)
        return None
    if kind == 'recipe':
        mapping = read(WORK / 'config/version_recipes.json', {}) or {}
        if old_version not in mapping:
            old_recipe = WORK / 'config/recipes' / (old_version + '.json')
            old_recipe.parent.mkdir(exist_ok=True)
            old_recipe.write_bytes(before['config/recipe.json'])
            mapping[old_version] = str(old_recipe.relative_to(WORK))
        new_recipe = WORK / 'config/recipes' / (candidate + '.json')
        new_recipe.write_bytes((WORK / 'config/recipe.json').read_bytes())
        mapping[candidate] = str(new_recipe.relative_to(WORK))
        write(WORK / 'config/version_recipes.json', mapping)
        (WORK / 'prompts' / (candidate + '.md')).write_text(context['active_prompt'])
    elif kind == 'prompt':
        mapping = read(WORK / 'config/version_recipes.json', {}) or {}
        if old_version in mapping:
            mapping[candidate] = mapping[old_version]
            write(WORK / 'config/version_recipes.json', mapping)
    proposal.update(candidate=candidate if kind in ('prompt', 'recipe') else old_version, changed=sorted(changed),
                    backup=str(backup), old_version=old_version,
                    before_hash={k:hashlib.sha256(v).hexdigest() for k,v in before.items() if k in changed},
                    after_hash={k:hashlib.sha256((WORK/k).read_bytes()).hexdigest() for k in changed})
    write(proposal_path, proposal)
    return proposal


def restore(before, changed):
    for name in changed:
        p = WORK / name
        if name in before: p.write_bytes(before[name])
        elif p.exists():
            # Keep failed new files as an audit object, outside active prompts/tools.
            dest = LEDGER / 'reverted_files' / (str(time.time_ns()) + '_' + p.name)
            dest.parent.mkdir(exist_ok=True); p.replace(dest)


def rollback(proposal):
    before = {name: (Path(proposal['backup']) / name).read_bytes() for name in proposal['changed']
              if (Path(proposal['backup']) / name).exists()}
    restore(before, proposal['changed'])


def tool_iteration(i, proposal, error):
    tool = WORK / proposal['files'][0]
    p = command([sys.executable, str(tool), '--self-test'])
    if p.returncode:
        write(LEDGER / 'tests' / f'i{i:02d}_tool.json', {'self_test_rc':p.returncode,'cases':[]})
        return 'revert'
    results = []
    case_backup = LEDGER / 'tool_case_backups' / f'i{i:02d}'
    case_backup.mkdir(parents=True, exist_ok=True)
    for c in [p.parent for p in (WORK / 'cases').glob('*/.released')]:
        before = read(c / 'scorecard.json', {}) or {}
        backup = case_backup / c.name
        backup.mkdir(exist_ok=True)
        for name in ('rows.jsonl','coverage.json','summary.md','scorecard.json'):
            if (c / name).exists(): shutil.copy2(c / name, backup / name)
        q = command([sys.executable, str(tool), '--case', str(c)])
        after_score = command([sys.executable, str(EVAL / 'eval/score.py'), str(c)])
        after = read(c / 'scorecard.json', {}) or {}
        results.append({'case':c.name, 'apply_rc':q.returncode, 'score_rc':after_score.returncode,
                        'before':before.get('error_classes', {}), 'after':after.get('error_classes', {})})
    target = next((r for r in results if r['case'] == error['case_dir']), {})
    exported = command([sys.executable, str(WORK/'tools/export_package.py'), '--verify-export', '--cases'] +
                       [str(WORK/'cases'/r['case']) for r in results]) if results else None
    keep = p.returncode == 0 and bool(target) and all(r['apply_rc']==0 and r['score_rc']==0 and
                all(v <= r['before'].get(k,0) for k,v in r['after'].items()) for r in results)
    keep &= target.get('after', {}).get(error['class'],0) < target.get('before',{}).get(error['class'],0)
    keep &= bool(exported and exported.returncode == 0)
    if keep and error['class']=='integrity' and error.get('kind'):
        current=read(WORK/'cases'/error['case_dir']/'scorecard.json',{}) or {}
        keep &= not any(e.get('kind')==error['kind'] and (not error.get('row') or e.get('row')==error['row'])
                        for e in current.get('integrity',{}).get('errors',[]))
    write(LEDGER / 'tests' / f'i{i:02d}_tool.json', {'self_test_rc':p.returncode,'cases':results,
                                                'reexport_rc':exported.returncode if exported else None})
    if not keep:
        for c in case_backup.iterdir():
            for p in c.iterdir(): shutil.copy2(p, WORK / 'cases' / c.name / p.name)
            command([sys.executable, str(EVAL / 'eval/score.py'), str(WORK / 'cases' / c.name)])
    return 'keep' if keep else 'revert'


def reference_pool(background=False):
    p = LEDGER / 'references.pid'
    if background and p.exists():
        try:
            os.kill(int(p.read_text()),0)
            return {'status':'running','pid':int(p.read_text())}
        except OSError: pass
    if background:
        with (LEDGER / 'reference_build.log').open('a') as f:
            child = subprocess.Popen([sys.executable, __file__, 'references'], stdout=f, stderr=f, start_new_session=True)
        p.write_text(str(child.pid))
        return {'status':'running','pid':child.pid}
    args = [sys.executable, str(EVAL / 'eval/build_reference.py'), '--all', '--no-judge']
    with (LEDGER / 'reference_counts.jsonl').open('a') as f:
        child = subprocess.Popen(args, stdout=f, stderr=subprocess.STDOUT, start_new_session=True)
        write(LEDGER / 'reference_child.json', {'pid':child.pid, 'started':time.time()})
        while child.poll() is None:
            if runner.stopped():
                os.killpg(child.pid, signal.SIGTERM); break
            time.sleep(15)
    log('reference_pool_exit', rc=child.returncode)
    write(LEDGER / 'reference_status.json', {'completed':child.returncode == 0,'judge_pending':True})
    return {'rc':child.returncode}


def run():
    check_launch()
    finish_iteration()
    state(status='running', phase='S6', frozen=True)
    os.environ['ATLAS_SESSION_ID'] = 'atlas-loop-' + str(os.getpid())
    version = (WORK / 'config/active_prompt.txt').read_text().strip()
    s = read(LEDGER / 'state.json', {}) or {}
    dev = run_batch(0,'dev',version,entries=['AQADK_CPMG','CHEY_CPMG'])
    collect_errors(dev)
    if not s.get('C1',{}).get('ready'): export('C1',[dev])
    aa = run_batch(0,'aa',version,block='H0')
    if not any(x.get('evidence')==aa['batch_id'] and x.get('evaluated') is True for x in rows(LEDGER / 'iterations.jsonl')):
        release(aa,0,'aa_baseline')
    collect_errors(aa)
    if not any(x.get('iteration')==1 and x.get('evaluated') is True for x in rows(LEDGER / 'iterations.jsonl')):
        p = command([sys.executable,str(WORK/'tools/map_residues.py'),'--self-test'])
        if p.returncode: pause('number mapping unit test failed')
        close(1,'keep','tool','tools/map_residues.py --self-test',note='Explicit sequence numbering mapping; no worker run')
    failures = (read(LEDGER / 'state.json', {}) or {}).get('target_failures', {}); invalid = 0
    for i in range(2,13):
        if i > 6: ensure_c2()
        if any(x.get('iteration')==i and x.get('decision') in ('keep','revert') and x.get('evaluated') is True for x in rows(LEDGER/'iterations.jsonl')): continue
        state(round=i)
        errors = [e for e in rows(LEDGER/'errors.jsonl') if not e.get('closed') and failures.get(e['id'],0)<2]
        if not errors: pause('No verified open error available; do not invent improvement rounds')
        error = errors[0]
        version = (WORK/'config/active_prompt.txt').read_text().strip()
        proposal = propose(i,error,version)
        if proposal is None:
            invalid += 1
            if invalid>=2: pause('Two consecutive noncompliant proposals')
            proposal = propose(i,error,version)
            if proposal is None: pause('Two consecutive noncompliant proposals')
        invalid=0
        if proposal['change_type']=='tool':
            decision = tool_iteration(i,proposal,error)
            evidence = str(LEDGER/'tests'/f'i{i:02d}_tool.json')
            close_fields = {'error_id': error['id']}
            batch_id = None
        else:
            reserve_final = 8 + (0 if (read(LEDGER/'state.json',{}).get('C2') or {}).get('ready') else 10)
            if runner.runs_used()+7+reserve_final>runner.auth()['run_cap']:
                rollback(proposal);pause('Insufficient run budget for paired batch plus required final/development runs')
            used = len([r for r in rows(LEDGER/'iterations.jsonl') if r.get('batch_id') and r.get('evaluated') is True])
            block = f'H{used+1}'
            spec = run_batch(i,'paired',old=version,new=proposal['candidate'],block=block,
                             origin_entry=error['entry'],origin_error=error['id'])
            rule = spec['summary']['rule']
            if rule['decision']=='needs_judge': pause('Paired decision waiting for registered Codex judge requests')
            decision=rule['decision']
            batch_id = evidence = spec['batch_id']
            close_fields = {'batch_id': batch_id, 'error_id': error['id'], 'rule': rule,
                            'note': '在3个蛋白上没有变差，并修好了'+error['id'] if decision=='keep' else '回退，依据见rule'}
        state(pending_iteration={'iteration': i, 'decision': decision, 'proposal': proposal, 'error': error,
                                 'batch_id': batch_id, 'evidence': evidence, 'close_fields': close_fields,
                                 'target_failures': failures.get(error['id'], 0) + 1})
        finish_iteration()
        failures = (read(LEDGER/'state.json', {}) or {}).get('target_failures', {})
        if i == 6: ensure_c2()
    version=(WORK/'config/active_prompt.txt').read_text().strip()
    sealed=run_batch(13,'sealed',version)
    aggregate=sealed['summary']['by_arm']['sealed']
    write(LEDGER/'sealed_final.json',{'version':version,'runs':aggregate['runs'],
        'all_completed':aggregate['not_ok']==0,'judge_complete':aggregate['judge']!='unavailable',
        'aggregate':aggregate,'batch_id':sealed['batch_id']})
    prompt=('Write FINAL_REPORT_ZH.md for Alex and one-page plain scientific English FINAL_SUMMARY_EN.md in this outputs '
            'directory. Read only released ledger counts, proposals, iterations, C1/C2 packages and ledger/sealed_final.json '
            'aggregate; never sealed case contents or hidden reference data. Report actual errors, kept/reverted changes, '
            'limitations, budget and source-access gaps; no generic improvement claim. Copy these final files nowhere else. '
            'Do not claim completion unless tools/check_done.py passes; sending is Alex\'s responsibility.')
    helper('write_final',prompt,WORK/'outputs',[WORK/'outputs'])
    for name in ('FINAL_REPORT_ZH.md','FINAL_SUMMARY_EN.md'):
        shutil.copy2(WORK/'outputs'/name,TASK/'outputs'/name)
    p=command([sys.executable,str(WORK/'tools/check_done.py')])
    state(status='complete' if p.returncode==0 else 'pending_checks', completion_output=p.stdout)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['run','start','status','references'])
    ap.add_argument('--background',action='store_true');a=ap.parse_args()
    if a.command=='status': print(json.dumps(read(LEDGER/'state.json',{}),ensure_ascii=False));return 0
    if a.command=='references': print(json.dumps(reference_pool(a.background)));return 0
    if a.command=='start':
        check_launch()
        with (LEDGER/'loop.log').open('a') as f:
            p=subprocess.Popen([sys.executable,__file__,'run'],stdout=f,stderr=f,start_new_session=True)
        write(LEDGER/'loop_process.json',{'pid':p.pid,'started':time.time()});print(json.dumps({'pid':p.pid}));return 0
    with (LEDGER/'driver.lock').open('a') as lock:
        try: fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError: print('another scheduler owns the campaign');return 2
        try: run()
        except Exception as e:
            state(status='paused',pause_reason=str(e));log('scheduler_paused',reason=str(e));print(str(e));return 2
    return 0


if __name__=='__main__':
    try: raise SystemExit(main())
    except RuntimeError as e: print(str(e));raise SystemExit(2)
