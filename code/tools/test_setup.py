#!/usr/bin/env python3
"""Offline checks only; these are not worker runs or scientific evaluations."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

WORK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORK / 'tools'))
sys.path.insert(0, str(Path.home() / 'dynamics_atlas_eval/runner'))
import run_worker as runner
import prefetch
import loop_driver
import map_residues
import subagent_judge


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def main():
    (WORK / 'ledger/tests').mkdir(parents=True, exist_ok=True)
    guard = module(Path.home() / '.codex/hooks/atlas_guard.py', 'atlas_guard')
    with tempfile.TemporaryDirectory(dir=WORK / 'ledger/tests') as temp:
        temp = Path(temp); (temp / '.atlas_worker').write_text(json.dumps({'entry':'CHEY_CPMG'}))
        for event in ('SessionStart','UserPromptSubmit','PreToolUse','Stop','SessionEnd'):
            data = {'cwd':str(temp),'session_id':'offline-test','hook_event_name':event,
                    'tool_input':{'cmd':'cat summary.md'},'stop_hook_active':True}
            with patch.object(guard.subprocess,'run', return_value=subprocess.CompletedProcess([],0)):
                value = guard.check(data)
            json.dumps(value)
            cli = subprocess.run([sys.executable, str(Path.home() / '.codex/hooks/atlas_guard.py')],
                                 input=json.dumps({'cwd':'/tmp/unrelated','hook_event_name':event}),
                                 capture_output=True,text=True,timeout=2)
            assert cli.returncode==0 and json.loads(cli.stdout)=={}, (event,cli.stderr)
        for command in ('cat ~/dynamics_atlas_eval/gold/x.json','pip install example',
                        'codex exec hello','git push','cat ../other/rows.jsonl',
                        'echo bad > ~/dynamics_atlas_work/outputs/out'):
            value = guard.check({'cwd':str(temp),'hook_event_name':'PreToolUse','tool_name':'exec_command',
                                 'tool_input':{'cmd':command}})
            assert value['hookSpecificOutput']['permissionDecision']=='deny',command
        assert guard.check({'cwd':'/tmp/unrelated','hook_event_name':'PreToolUse',
                            'tool_input':{'cmd':'pip install example'}})=={}
        assert guard.check({'cwd':str(temp),'hook_event_name':'PreToolUse',
                            'tool_input':{'cmd':'cat summary.md'}})=={}
        native=temp/'native'; jid='a'*24; folder=native/'judge_queue'/jid
        folder.mkdir(parents=True); (folder/'request.json').write_text('{}')
        (folder/'status.json').write_text(json.dumps({'status':'pending'}))
        (native/'state.json').write_text(json.dumps({'status':'running'}))
        message=str(folder/'request.json')+' '+str(folder/'response.json')
        data={'cwd':str(WORK),'hook_event_name':'PreToolUse','tool_name':'spawn_agent',
              'tool_input':{'task_name':'atlas_judge_'+jid,'fork_turns':'none','message':message}}
        with patch.object(guard,'LEDGER',native):
            assert guard.check(data)=={}, 'registered isolated judge denied'
            data['tool_input']['fork_turns']='all'
            assert guard.check(data)['hookSpecificOutput']['permissionDecision']=='deny'
        assert runner.JUDGE==WORK/'tools/subagent_judge.py'
        (temp/'rows.jsonl').write_text('{"row_id":"r1"}\n')
        for declared, expected in [('partial','partial'),('blocked','blocked'),('done','done')]:
            (temp/'result.json').write_text(json.dumps({'entry_id':'CHEY_CPMG','status':declared,'n_rows':1}))
            assert runner.final_result_status(temp,'CHEY_CPMG')==expected
        assert runner.final_result_status(temp,'OTHER')=='invalid_worker_result'
        (temp/'result.json').write_text(json.dumps({'entry_id':'CHEY_CPMG','status':'done','n_rows':2}))
        assert runner.final_result_status(temp,'CHEY_CPMG')=='invalid_worker_result'
        spec={'jobs':[{'arm':'old','result':{'case':'synthetic'}}],'iter':0}
        with patch.object(runner.subprocess,'run',return_value=subprocess.CompletedProcess([],4,'{"rows_with_contradiction":0}')):
            assert runner.judge_arm(spec,'old')['judge']=='unavailable'
        subagent_judge.self_test()
        native_case=temp/'case'; native_case.mkdir()
        row={'row_id':'r1','doi':'10/example','method_class':'fret','locator':'Table 1'}
        (native_case/'rows.jsonl').write_text(json.dumps(row)+'\n')
        audit={'results':[{'row_id':'r1','fields':{'temperature':'supported'},'relevance':'target'}],
               'row_keys':{'r1':subagent_judge.row_key(row)}}
        (native_case/'native_judge.json').write_text(json.dumps(audit))
        (temp/'errors.jsonl').write_text(json.dumps({'id':'E-fixture','class':'faithfulness','field':'temperature',
                        'row_key':subagent_judge.row_key(row),'case_dir':'baseline'})+'\n')
        pair={'origin':{'error_id':'E-fixture'},'jobs':[{'arm':'origin','result':{'case':'case','status':'done'}}]}
        arms={arm:{'classes':{'faithfulness':n},'runs':3,'median_wall_s':10,'judge':{}}
              for arm,n in [('old',1),('new',0)]}
        with patch.object(runner,'LEDGER',temp), patch.object(runner,'CASES',temp), patch.object(
                runner,'full_scorecard',return_value={'integrity':{'pass':True},'error_classes':{}}):
            assert runner.keep_rule(pair,arms)['decision']=='keep'
            pair['jobs'][0]['result']['status']='partial'
            assert runner.keep_rule(pair,arms)['decision']=='revert'
            pair['jobs'][0]['result']['status']='done'
            audit['results'][0]['fields']['temperature']='not_supported'
            (native_case/'native_judge.json').write_text(json.dumps(audit))
            assert runner.keep_rule(pair,arms)['decision']=='revert', 'aggregate drop concealed unrepaired field'
        identity={'names':['CheY'], 'genes':['cheY'], 'organism':'Escherichia coli (strain K12)'}
        source='<pmc-articleset><article><front><article-meta><article-id pub-id-type="pmcid">PMC123</article-id>'
        source+='</article-meta></front><body><p>'+('Synthetic source fixture. '*20)+'</p></body></article></pmc-articleset>'
        with patch.object(prefetch,'WORK',temp), patch.object(prefetch,'get',side_effect=[RuntimeError('HTTP Error 500'),source]):
            assert prefetch.fetch_source('PMC123')['pmcid']=='PMC123'
            assert 'eutils.ncbi.nlm.nih.gov' in json.loads((temp/'sources_cache/PMC123.source.json').read_text())['url']
        with patch.object(prefetch,'WORK',temp), patch.object(prefetch,'get',side_effect=RuntimeError('HTTP Error 403')) as fetch:
            try: prefetch.fetch_source('PMC124')
            except RuntimeError: pass
            else: raise AssertionError('Access restriction must not trigger fallback')
            assert fetch.call_count==1
        recipe=json.loads((WORK/'config/recipe.json').read_text())
        plans=prefetch.query_plan({'entry_id':'CHEY_CPMG'},identity,recipe)
        assert len(plans)==11 and all('CheY' in x for x in plans.values())
        assert all('Escherichia coli' in x for x in plans.values())
        assert all('strain K12' not in x and 'E. coli' in x for x in plans.values())
        assert loop_driver.sentence_changes('A. B.','A. C.')==1
        old, new = [], []
        for entry in ('AQADK_CPMG', 'CHEY_CPMG'):
            for label, group in [('old', old), ('new', new)]:
                c=temp/(label+'_'+entry); c.mkdir()
                (c/'input.json').write_text(json.dumps({'entry_id':entry})); group.append(c)
        with patch.object(loop_driver,'package_cases',return_value=old):
            assert len(loop_driver.summary_pairs(new))==2
            for bad in (old, new[:1]):
                try: loop_driver.summary_pairs(bad)
                except ValueError: pass
                else: raise AssertionError('Self-comparison or missing pair accepted')
        (temp/'batches').mkdir()
        (temp/'batches/fixture.json').write_text(json.dumps({'batch_id':'fixture','status':'complete',
                                                          'jobs':[{'result':{'status':'done'}}]}))
        with patch.object(loop_driver,'LEDGER',temp), patch.object(loop_driver,'check_launch'), patch.object(
                loop_driver,'command',return_value=subprocess.CompletedProcess([],0,'{"batch_id":"fixture"}')):
            assert loop_driver.run_batch(0,'dev','fixture',entries=['AQADK_CPMG','CHEY_CPMG'])['status']=='complete'
            for kind, iteration, entries in [('aa',0,[]),('paired',2,[]),('dev',6,['AQADK_CPMG']),('dev',0,['OTHER'])]:
                try: loop_driver.run_batch(iteration,kind,'fixture',entries=entries)
                except RuntimeError: pass
                else: raise AssertionError('Reference gate incorrectly bypassed')
        assert runner.is_helper({'command':'node /example/mcp-slack'})
        assert not runner.is_helper({'command':'python3 test_setup.py mcp-slack'})
        assert runner.is_helper({'command':'/Users/example/.codex/computer-use/Codex Computer Use.app/Contents/MacOS/SkyComputerUseClient event-stream mcp'})
        with patch.object(runner,'leak_processes',return_value=[{}]*31):
            assert not runner.leak_guard()['allowed']
        with patch.object(runner,'leak_processes',return_value=[{}]*30):
            assert runner.leak_guard()['allowed']
        # Missing origin/judge/comparison data must never produce a keep decision.
        assert runner.keep_rule({}, {})['decision']!='keep'
        cfg=runner.codex_overrides('high')
        assert 'notify=[]' in cfg and 'features.memories=false' in cfg
        map_residues.self_test()
        score = module(Path.home() / 'dynamics_atlas_eval/eval/score.py', 'atlas_score_test')
        coverage = {'classes':{}}
        for method in recipe['methods']:
            p = temp / 'prefetch' / (method + '.json'); p.parent.mkdir(exist_ok=True)
            reference={'status':'ok','search_id':'test-'+method,'query':'test','hits':0}
            p.write_text(json.dumps(reference))
            coverage['classes'][method]={'status':'searched_not_found','queries':[reference]}
        errs, *_ = score.integrity(temp, {'entry_id':'CHEY_CPMG','sequence':'ACD'}, [], coverage, 'No conclusion.', '', {'CHEY_CPMG'})
        assert not errs,errs
        coverage['classes']['fret']['queries'][0]['search_id']='wrong-id'
        errs, *_ = score.integrity(temp, {'entry_id':'CHEY_CPMG','sequence':'ACD'}, [], coverage, 'No conclusion.', '', {'CHEY_CPMG'})
        assert any(e['kind']=='coverage_prefetch_reference_missing' for e in errs)
    for p in [Path.home()/'.codex/hooks/atlas_guard.py',
              Path.home()/'dynamics_atlas_eval/runner/run_worker.py'] + list((WORK/'tools').glob('*.py')):
        compile(p.read_text(),str(p),'exec')
    print('Offline hook/runner/prefetch/mapping/proposal checks PASS; no scientific or live-worker claim.')


if __name__=='__main__': main()
