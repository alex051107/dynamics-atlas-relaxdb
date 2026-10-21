"""Offline regression fixtures for tonight's tools; run python3 -m unittest tests.test_night_20261020 -v."""
import contextlib
import gzip
import io
import json
import math
import csv
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
try:
    import export_public_repo as export  # not shipped in the public copy
except ModuleNotFoundError:
    export = None
import identity_preflight as identity
import pdb_states as pdb
import regime_check as regime
import screen_candidates as screen

FIXTURES = ROOT / 'tests/fixtures_night'


class NightTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(dir=ROOT / 'tests')
        self.addCleanup(temp.cleanup)
        self.work = Path(temp.name)
        for folder in ('tools', 'ledger/sr_dual', 'cases/toy', 'config', 'outputs/screen', 'inputs', 'prompts'):
            (self.work / folder).mkdir(parents=True)
        for name in ('dual_read.py', 'reread_one.py'):
            shutil.copyfile(ROOT / 'tools' / name, self.work / 'tools' / name)
        shutil.copyfile(FIXTURES / 'second_read.py', self.work / 'tools/second_read.py')
        for name in ('rows.jsonl', 'screen_log.jsonl'):
            shutil.copyfile(FIXTURES / name, self.work / 'cases/toy' / name)
        self.sr = self.work / 'ledger/sr_dual'
        self.case = self.work / 'cases/toy'
        self.env = {**os.environ, 'DYNAMICS_ATLAS_WORK': str(self.work)}
        self.reads = [{'row_number': n, 'verdict': 'unverified', 'reason': 'fixture'} for n in (1, 2)]
        self.plan = {b: {'returncode': 0, 'rows': self.reads} for b in ('codex', 'claude')}

    def run_tool(self, name, *args):
        (self.work / 'reader_plan.json').write_text(json.dumps(self.plan))
        return subprocess.run([sys.executable, str(ROOT / 'tools' / name), *args], cwd=self.work,
                              env=self.env, capture_output=True, text=True, timeout=20)

    def flags(self):
        return json.loads((self.sr / 'toy_flags.json').read_text())

    def save_reads(self, backend, rows):
        (self.sr / f'toy_{backend}.jsonl').write_text(''.join(json.dumps(r) + '\n' for r in rows))

    def test_failed_reader_removes_stale_file_and_reports_failure(self):
        self.plan['claude'] = {'returncode': 1}
        self.save_reads('claude', self.reads)
        (self.case / 'second_read.jsonl').write_text('stale')
        result = self.run_tool('dual_read.py', 'toy')
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn('claude', self.flags()['failed_readers'])
        self.assertNotIn('claude', self.flags()['counts'])
        self.assertFalse((self.sr / 'toy_claude.jsonl').exists())
        self.assertFalse((self.case / 'second_read.jsonl').exists())
        self.assertEqual(self.flags()['flags'], [])

    def test_complete_exit_two_is_accepted(self):
        self.plan['codex'] = {'returncode': 2, 'rows': [dict(r, verdict='wrong') for r in self.reads]}
        result = self.run_tool('dual_read.py', 'toy')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.flags()['failed_readers'], {})
        self.assertEqual(self.flags()['counts']['codex']['wrong'], 2)
        self.assertEqual([r['why'] for r in self.flags()['flags']], ['wrong', 'wrong'])

    def test_unverified_full_text_flag_excludes_abstract(self):
        result = self.run_tool('dual_read.py', 'toy')
        self.assertEqual(result.returncode, 0, result.stderr)
        flags = self.flags()['flags']
        self.assertEqual([(r['row_number'], r['why']) for r in flags], [(1, 'all_unverified_full_text')])
        self.assertEqual(set(flags[0]['readers']), {'codex', 'claude'})

    def test_reuse_recomputes_flags_without_reader_calls(self):
        self.assertEqual(self.run_tool('dual_read.py', 'toy').returncode, 0)
        calls = (self.work / 'reader_calls.txt').read_text()
        for backend in self.plan:
            self.save_reads(backend, [dict(r, verdict='ok') for r in self.reads])
        result = self.run_tool('dual_read.py', 'toy', '--reuse')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.flags()['flags'], [])
        self.assertEqual((self.work / 'reader_calls.txt').read_text(), calls)

    def test_incomplete_duplicate_and_malformed_reads_are_rejected(self):
        for rows in (self.reads[:1], self.reads + self.reads[:1]):
            with self.subTest(rows=rows):
                self.plan['claude'] = {'returncode': 0, 'rows': rows}
                self.assertEqual(self.run_tool('dual_read.py', 'toy').returncode, 1)
                self.assertIn('claude', self.flags()['failed_readers'])
        self.plan['claude'] = {'returncode': 0, 'raw': '{bad json'}
        self.assertEqual(self.run_tool('dual_read.py', 'toy').returncode, 1)
        self.assertFalse((self.case / 'second_read.jsonl').exists())

    def test_reuse_missing_reader_reports_failure_without_using_one_reader_as_both(self):
        self.save_reads('codex', self.reads)
        result = self.run_tool('dual_read.py', 'toy', '--reuse')
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn('claude', self.flags()['failed_readers'])
        self.assertEqual(self.flags()['flags'], [])
        self.assertFalse((self.work / 'reader_calls.txt').exists())

    def test_reread_complete_exit_two_saves_and_recomputes(self):
        for backend in self.plan:
            self.save_reads(backend, self.reads)
        self.plan['codex'] = {'returncode': 2, 'rows': [dict(r, verdict='wrong') for r in self.reads]}
        result = self.run_tool('reread_one.py', 'toy', 'codex')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)['saved'])
        self.assertEqual(self.flags()['counts']['codex']['wrong'], 2)
        self.assertEqual((self.work / 'reader_calls.txt').read_text(), 'codex\n')

    def test_reread_failure_preserves_archived_read(self):
        self.save_reads('codex', self.reads)
        before = (self.sr / 'toy_codex.jsonl').read_bytes()
        for plan in ({'returncode': 1}, {'returncode': 1, 'rows': self.reads}, {'returncode': 0, 'rows': self.reads[:1]}):
            with self.subTest(plan=plan):
                self.plan['codex'] = plan
                result = self.run_tool('reread_one.py', 'toy', 'codex')
                self.assertFalse(json.loads(result.stdout)['saved'])
                self.assertEqual((self.sr / 'toy_codex.jsonl').read_bytes(), before)
                self.assertFalse((self.case / 'second_read.jsonl').exists())

    def test_promotion_script_keeps_schema_and_original_tier(self):
        row = json.loads((FIXTURES / 'screen.jsonl').read_text())
        target = self.work / 'outputs/screen/TOY.jsonl'
        target.write_text(json.dumps(row) + '\n')
        (self.work / 'config/relaxdb_source_dois.json').write_text(json.dumps({'TOY': [row['doi'].upper()]}))
        result = self.run_tool('promote_source_papers.py', '--write')
        self.assertEqual(result.returncode, 0, result.stderr)
        got = json.loads(target.read_text())
        self.assertEqual(set(got), screen.FIELDS)
        self.assertEqual(got['tier'], 'A')
        self.assertTrue(got['needs_full_text'])
        self.assertIn('promoted from C', got['reason'])
        self.assertIn(row['reason'], got['reason'])
        screen.validate_rows([got], [row], [])

    def test_screen_run_promotes_source_without_extra_field(self):
        row = json.loads((FIXTURES / 'screen.jsonl').read_text())
        (self.work / 'config/relaxdb_source_dois.json').write_text(json.dumps({'TOY': [row['doi']]}))
        (self.work / 'prompts/worker_v6_screen.md').write_text('Synthetic fixture prompt.')
        with contextlib.ExitStack() as stack:
            stack.enter_context(patch.object(screen, 'WORK', self.work))
            for name, value in {'check_entry': {}, 'candidates_for': [row], 'method_keys': [], 'run_records': [],
                                'append_run': None, 'enrich_abstracts': None, 'check_stop': None,
                                'screen_batches': [row]}.items():
                stack.enter_context(patch.object(screen, name, return_value=value))
            stack.enter_context(patch.object(screen, 'spawn_worker', side_effect=AssertionError('no models')))
            stack.enter_context(patch.object(screen.urllib.request, 'urlopen', side_effect=AssertionError('offline')))
            stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            screen.run_screen('TOY')
        got = json.loads((self.work / 'outputs/screen/TOY.jsonl').read_text())
        self.assertEqual(set(got), screen.FIELDS)
        self.assertEqual(got['tier'], 'A')
        self.assertIn('promoted from C', got['reason'])
        screen.validate_rows([got], [row], [])

    def test_superseded_case_does_not_count_as_read(self):
        rows = [{'doi': f'10.5555/{n}', 'tier': tier} for n, tier in ((1, 'A'), (2, 'B'), (3, 'C'))]
        (self.work / 'outputs/screen/TOY.jsonl').write_text(''.join(json.dumps(r) + '\n' for r in rows))
        for suffix, doi in (('old', '10.5555/1'), ('new', '10.5555/2')):
            case = self.work / f'cases/V6_r6_TOY_{suffix}'
            case.mkdir()
            (case / 'candidates.json').write_text(json.dumps([{'doi': doi}]))
        (self.work / 'ledger/superseded_cases.json').write_text(json.dumps(['V6_r6_TOY_old']))
        result = self.run_tool('unfilled_ab.py', 'TOY')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), '10.5555/1')

    @unittest.skipIf(export is None, 'export_public_repo.py is not in the public copy')
    def test_scrub_paths_and_prose_names_but_preserves_code_names(self):
        text = f'{Path.home()}/notes {export.WORK}/tools ~/dynamics_atlas_work/tools '
        text += f'{Path.home()}/Desktop/UNC/Soojung-Dynamic data/report <local scratch> Gina Alex Soojung'
        clean = export.scrub(text)
        self.assertIn('~/notes', clean)
        for forbidden in (str(Path.home()), 'Soojung-Dynamic data', '/private/tmp/claude-123', 'Gina', 'Alex', 'Soojung'):
            self.assertNotIn(forbidden, clean)
        self.assertIn('~/dynamics_atlas_work/tools', clean)  # the working-folder name is not personal and stays readable
        self.assertIn('<workspace>', clean)
        self.assertIn('<local scratch>', clean)
        code = export.scrub(text, names=False)
        self.assertIn('Gina Alex Soojung', code)
        self.assertNotIn(str(Path.home()), code)

    def test_identity_thresholds_match_partial_mismatch(self):
        seq = 'ACDEFGHIKLMNPQRSTVW'
        (self.work / 'inputs/TOY.json').write_text(json.dumps({'sequence': seq, 'uniprot': 'SYNTHETIC'}))
        for matched, expected in ((10, 'match'), (8, 'match'), (7, 'partial'), (3, 'partial'), (2, 'mismatch'), (0, 'mismatch')):
            ref = seq[:9 + matched] if matched else 'Z' * 19
            with self.subTest(matched=matched), patch.object(identity, 'WORK', self.work), patch.object(identity, 'uniprot_seq', return_value=ref) as fetch:
                got = identity.check('TOY')
                self.assertEqual(got['status'], expected)
                self.assertEqual(got['overlap'], matched / 10)
                fetch.assert_called_once_with('SYNTHETIC')

    def cif_result(self, text):
        path = self.work / 'synthetic.cif.gz'
        with gzip.open(path, 'wt') as fh:
            fh.write(text)
        return pdb.fused_covalent(path, ['A', 'B'], 'SYNTHETIC')

    def test_fused_segment_and_covalent_connections(self):
        got = self.cif_result((FIXTURES / 'fused.cif').read_text())
        for chain in ('A', 'B'):
            self.assertEqual(got[chain]['fused'], ['WTMFWV (label_seq_id 13-18)'])
            self.assertEqual(len(got[chain]['covalent']), 1)
        self.assertIn('L:LIG', got['A']['covalent'][0])
        self.assertIn('B:MLY8', got['B']['covalent'][0])

    def test_tags_and_short_segments_are_not_fused(self):
        text = (FIXTURES / 'fused.cif').read_text()
        for tail in ('HHHHHH', 'GSGSGS', 'WSHPQFEK', 'WTM'):
            with self.subTest(tail=tail):
                got = self.cif_result(text.replace('WTMFWV', tail))
                self.assertEqual(got['A']['fused'], [])
        self.assertFalse(pdb.tag_linker('HHHHHHWTMFWV'))

    def test_sequence_fallback_and_missing_mapping(self):
        text = (FIXTURES / 'fused.cif').read_text()
        text = text.replace('1 A 5 9 SYNTHETIC', '1 A ? ? SYNTHETIC').replace('1 B 5 9 SYNTHETIC', '1 B ? ? SYNTHETIC')
        self.assertEqual(len(self.cif_result(text)['A']['fused']), 1)
        self.assertEqual(self.cif_result(text.replace('SYNTHETIC', 'UNRELATED'))['A']['fused'], [])


class RegimeTests(unittest.TestCase):
    def detection(self, kex='100 s-1', delta='1 ppm', field='600 MHz', **extra):
        return {'kex': kex, 'delta_omega': delta, 'field': field, **extra}

    def test_default_nitrogen_and_hz_angular_conversion(self):
        lo, hi, state, field = regime.calculate(self.detection())
        self.assertAlmostEqual(lo, 100 / (2 * math.pi * 0.10136 * 600))
        self.assertEqual(lo, hi)
        self.assertEqual(state, 'slow')
        lo, _, _, _ = regime.calculate(self.detection(delta='100 Hz'))
        self.assertAlmostEqual(lo, 100 / (2 * math.pi * 100))
        lo, _, _, _ = regime.calculate(self.detection(delta='100 rad/s'))
        self.assertEqual(lo, 1)

    def test_carbon_proton_and_tesla_fields(self):
        for nucleus, factor in (('13C', 0.25145), ('1H', 1), ('15N', 0.10136)):
            with self.subTest(nucleus=nucleus):
                lo, _, _, _ = regime.calculate(self.detection(delta=f'1 ppm ({nucleus})', field='14.1 T'))
                self.assertAlmostEqual(lo, 100 / (2 * math.pi * factor * 14.1 * regime.PROTON_MHZ_T))
        lo, _, _, _ = regime.calculate(self.detection(field='60.816 MHz (15N)'))
        self.assertAlmostEqual(lo, 100 / (2 * math.pi * 60.816))

    def test_ranges_uncertainties_and_field_lists(self):
        lo, hi, state, _ = regime.calculate(self.detection('100-200 s^-1', '1-2 ppm', '600, 800 MHz'))
        self.assertAlmostEqual(lo, 100 / (2 * math.pi * 2 * 0.10136 * 800))
        self.assertAlmostEqual(hi, 200 / (2 * math.pi * 0.10136 * 600))
        self.assertEqual(state, 'slow/intermediate')
        lo, hi, _, _ = regime.calculate(self.detection('100 ± 20 s−1', '100 s-1'))
        self.assertAlmostEqual(lo, 0.8)
        self.assertAlmostEqual(hi, 1.2)

    def test_residue_lists_pair_by_label(self):
        lo, hi, _, _ = regime.calculate(self.detection('D64: 100; R19: 200 s-1', 'R19: 200; D64: 100 Hz'))
        self.assertAlmostEqual(lo, 1 / (2 * math.pi))
        self.assertEqual(lo, hi)
        lo, hi, _, _ = regime.calculate(self.detection('D64: 100, R19: 200 s-1', '100 Hz'))
        self.assertAlmostEqual(hi, 2 * lo)

    def test_boundaries_and_conflicts(self):
        for lo, hi, expected in ((0.1, 0.29, 'slow'), (0.3, 3, 'intermediate'), (3.01, 4, 'fast'),
                                  (0.1, 4, 'slow/intermediate/fast'), (3, 4, 'intermediate/fast')):
            self.assertEqual(regime.regime(lo, hi), expected)
        self.assertTrue(regime.is_conflict('qualifies', 'fast'))
        self.assertTrue(regime.is_conflict('does', 'slow'))
        self.assertFalse(regime.is_conflict('qualifies', 'slow/intermediate/fast'))

    def test_ambiguous_inputs_rejected(self):
        for detection in (self.detection(kex='100'), self.detection(delta='0-1 ppm'),
                          self.detection(kex='<100 s-1'), self.detection(kex='100 s-1 at 298 K'),
                          self.detection(delta='1 ppm (15N and 13C)'), self.detection(field=''),
                          self.detection(kex='D64:100 s-1', delta='R19:1 ppm'),
                          self.detection(kex='100 ppm'), self.detection(kex='1e999 s-1'),
                          self.detection(kex='100(10) s-1')):
            with self.subTest(detection=detection), self.assertRaises(ValueError):
                regime.calculate(detection)

    def test_synthetic_scan_writes_csv_conflicts_and_preserves_sources(self):
        with tempfile.TemporaryDirectory(dir=ROOT / 'tests') as temporary:
            work = Path(temporary)
            source = work / 'outputs/judgment_v0'
            source.mkdir(parents=True)
            fixture = json.loads((FIXTURES / 'regime.json').read_text())
            judgment = source / 'TOY.json'
            judgment.write_text(json.dumps({'judgments': fixture['judgments']}))
            alt = work / 'outputs/alt_apo_states_toy.json'
            alt.write_text(json.dumps(fixture['alt']))
            before = {p: p.read_bytes() for p in (judgment, alt)}
            output = work / 'outputs/regime_check.csv'
            with contextlib.redirect_stdout(io.StringIO()) as stdout:
                rows, conflicts, skipped = regime.scan(work, output)
            self.assertEqual(len(rows), 3)
            self.assertEqual({r['entry'] for r in conflicts}, {'TOY_FAST', 'TOY_SLOW'})
            self.assertEqual(len(skipped), 1)
            self.assertIn('UNPARSEABLE TOY_SKIP toy-J3: kex:', stdout.getvalue())
            with output.open() as fh:
                saved = list(csv.DictReader(fh))
            self.assertEqual(saved, rows)
            self.assertEqual({p: p.read_bytes() for p in before}, before)


if __name__ == '__main__':
    unittest.main()
