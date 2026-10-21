"""Synthetic second reader; run as second_read.py CASE --backend NAME inside the fixture workspace."""
import json
from pathlib import Path
import sys

root = Path.cwd()
plan = json.loads((root / 'reader_plan.json').read_text())[sys.argv[-1]]
with (root / 'reader_calls.txt').open('a') as fh:
    fh.write(sys.argv[-1] + '\n')
if 'rows' in plan:
    (root / 'cases' / sys.argv[1] / 'second_read.jsonl').write_text(
        ''.join(json.dumps(row) + '\n' for row in plan['rows']))
if 'raw' in plan:
    (root / 'cases' / sys.argv[1] / 'second_read.jsonl').write_text(plan['raw'])
sys.exit(plan['returncode'])
