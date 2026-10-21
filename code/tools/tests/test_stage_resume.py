#!/usr/bin/env python3
"""Temporary offline failure-window checks, never scientific worker cases."""
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

WORK = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(WORK / 'tools'))
import loop_driver as d


def main():
    with tempfile.TemporaryDirectory(dir=WORK / 'ledger/tests') as folder:
        root = Path(folder); ledger = root / 'ledger'; ledger.mkdir()
        for name in ('config', 'tools', 'cases'):
            (root / name).mkdir()
        (root / 'tools/export_package.py').touch()
        (root / 'config/active_prompt.txt').write_text('old\n')
        (root / 'config/dev_ids.txt').write_text('AQADK_CPMG CHEY_CPMG\n')
        (ledger / 'batches').mkdir()
        old, new = [], []
        for entry in ('AQADK_CPMG', 'CHEY_CPMG'):
            for name, group, version in [('old', old, 'old'), ('new', new, 'new')]:
                case = root / 'cases' / (name + '_' + entry); case.mkdir()
                (case / 'input.json').write_text(json.dumps({'entry_id': entry}))
                (case / 'run.json').write_text(json.dumps({'prompt_version': version}))
                group.append(case)
        spec = {'batch_id': 'fixture', 'jobs': [{'version': 'old', 'result': {'case': p.name}} for p in new]}
        (ledger / 'batches/fixture.json').write_text(json.dumps({'batch_id': 'fixture', 'jobs': []}))
        with patch.object(d, 'WORK', root), patch.object(d, 'LEDGER', ledger), patch.object(d, 'TASK', root / 'task'), patch.object(d, 'log'):
            d.write(ledger / 'state.json', {'C1': {'cases': [p.name for p in old]}})
            def export_command(args, timeout=None):
                if '--output' in args:
                    dest = Path(args[args.index('--output') + 1]); dest.mkdir(parents=True, exist_ok=True)
                    d.write(dest / 'manifest.json', {'integrity_pass': True})
                return subprocess.CompletedProcess(args, 0, '', '')
            with patch.object(d, 'command', side_effect=export_command), patch.object(d, 'summary_pairs', return_value=[('AQADK_CPMG', old[0], new[0])]):
                def fail_check(args, timeout=None):
                    p = export_command(args, timeout)
                    if '--checkpoint' in args: p.returncode = 1
                    return p
                with patch.object(d, 'command', side_effect=fail_check):
                    try: d.export('C2', [spec], checkpoint=True)
                    except RuntimeError: pass
                    else: raise AssertionError('Failed checkpoint advanced')
                assert not d.read(ledger / 'state.json')['C1'].get('ready')
                assert not d.read(ledger / 'state.json').get('C2', {}).get('ready')
                d.export('C2', [spec], checkpoint=True)
                assert d.read(ledger / 'state.json')['C2']['ready']
            d.write(ledger / 'state.json', {})
            with patch.object(d, 'run_batch', return_value=spec) as batch, patch.object(d, 'export', side_effect=RuntimeError('pending')):
                for active in ('old', 'later'):
                    (root / 'config/active_prompt.txt').write_text(active)
                    try: d.ensure_c2()
                    except RuntimeError: pass
                assert [c.args[2] for c in batch.call_args_list] == ['old', 'old'], 'C2 version drifted on retry'
                spec['jobs'][0]['version'] = 'later'
                try: d.ensure_c2()
                except RuntimeError as e: assert 'version differs' in str(e)
                else: raise AssertionError('Cached C2 mixed versions accepted')
            for closed in (range(0, 7), range(0, 13)):
                d.write(ledger / 'state.json', {'C1': {'ready': True}})
                (ledger / 'iterations.jsonl').write_text(''.join(json.dumps({'iteration': i, 'decision': 'keep',
                    'evidence': 'fixture', 'evaluated': True}) + '\n' for i in closed))
                with patch.object(d, 'check_launch'), patch.object(d, 'finish_iteration'), patch.object(d, 'collect_errors'), patch.object(
                        d, 'run_batch', return_value={'batch_id': 'fixture'}) as batches, patch.object(
                        d, 'ensure_c2', side_effect=RuntimeError('checkpoint pending')), patch.object(d, 'propose') as propose:
                    try: d.run()
                    except RuntimeError as e: assert str(e) == 'checkpoint pending'
                    assert not propose.called, 'Iteration7 advanced before C2'
                    assert all(c.args[1] != 'sealed' for c in batches.call_args_list), 'Sealed advanced before C2'
            (ledger / 'iterations.jsonl').write_text('')
            error = {'id': 'E-fixture', 'closed': False}
            (ledger / 'errors.jsonl').write_text(json.dumps(error) + '\n')
            pending = {'iteration': 2, 'decision': 'keep', 'proposal': {'candidate': 'new', 'change_type': 'prompt'},
                       'error': error, 'batch_id': 'fixture', 'evidence': 'fixture', 'close_fields': {'batch_id': 'fixture'}, 'target_failures': 1}
            d.write(ledger / 'state.json', {'pending_iteration': pending})
            (root / 'config/active_prompt.txt').write_text('old')
            with patch.object(d, 'collect_errors'), patch.object(d, 'command', return_value=subprocess.CompletedProcess([], 6)):
                try: d.finish_iteration()
                except RuntimeError: pass
                else: raise AssertionError('Release failure ignored')
            decisions = d.rows(ledger / 'iterations.jsonl')
            assert len(decisions) == 1 and decisions[0]['evaluated'] is False and 'iteration' not in decisions[0]
            assert (root / 'config/active_prompt.txt').read_text() == 'old'
            assert d.read(ledger / 'state.json')['pending_iteration']
            # Use the frozen release function on a fully patched temporary ledger.
            with patch.object(d.runner, 'LEDGER', ledger), patch.object(d.runner, 'BATCHES', ledger / 'batches'), patch.object(d.runner, 'CASES', root / 'cases'), contextlib.redirect_stdout(io.StringIO()):
                assert d.runner.release('fixture') == 0, 'Pending decision violates frozen release contract'
            with patch.object(d, 'collect_errors'), patch.object(d, 'command', return_value=subprocess.CompletedProcess([], 0)):
                with patch.object(d, 'close', side_effect=RuntimeError('interruption before close')):
                    try: d.finish_iteration()
                    except RuntimeError: pass
                assert (root / 'config/active_prompt.txt').read_text() == 'new\n'
                assert not any(r.get('evaluated') is True for r in d.rows(ledger / 'iterations.jsonl'))
                d.finish_iteration(); d.finish_iteration()
            assert len([r for r in d.rows(ledger / 'iterations.jsonl') if r.get('evaluated') is True]) == 1
            assert d.rows(ledger / 'errors.jsonl')[0]['closed']
            assert not d.read(ledger / 'state.json')['pending_iteration']
            backup = ledger / 'backup/config'; backup.mkdir(parents=True)
            (backup / 'recipe.json').write_text('old recipe')
            (root / 'config/recipe.json').write_text('bad recipe')
            pending.update(iteration=3, decision='revert', batch_id=None, evidence='tool fixture',
                proposal={'candidate':'old', 'change_type':'tool', 'changed':['config/recipe.json'], 'backup':str(backup.parent)},
                close_fields={})
            d.write(ledger / 'state.json', {'pending_iteration': pending})
            with patch.object(d, 'close', side_effect=RuntimeError('interruption before close')):
                try: d.finish_iteration()
                except RuntimeError: pass
            assert (root / 'config/recipe.json').read_text() == 'old recipe'
            d.finish_iteration()
            assert d.read(ledger / 'state.json')['target_failures']['E-fixture'] == 1, 'Retry counted failure twice'
            assert len([r for r in d.rows(ledger / 'iterations.jsonl') if r.get('iteration') == 3]) == 1
    print('Offline C2 failure/retry/version/order and decision-release/finalize keep/revert recovery PASS; no campaign runs.')


if __name__ == '__main__':
    main()
