"""Portable receipt and synthetic checks; no native replay."""
from pathlib import Path
import runpy,hashlib,json,io,contextlib
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/native-gaussian-moment-jet-20260910'
def main():
 for row in json.loads((PACK/'IMPORT_PROVENANCE.json').read_text()):
  assert hashlib.sha256((ROOT/row['local']).read_bytes()).hexdigest()==row['sha256'],row['local']
 output=io.StringIO()
 with contextlib.redirect_stdout(output):
  runpy.run_path(str(PACK/'source_draft/check.py'))['main']()
 result=json.loads(output.getvalue())
 assert result['status']=='PASS_COMPACT_ONLY'
 assert result['native_replays']==0 and result['event_arithmetic_replays']==0
 print(f"TOTAL: PASS={result['checks']} FAIL=0")
 print('SUPPORT_ONLY: moment precision certified; Ward sign remains open; integration and formal audit UNRUN')
if __name__=='__main__':main()
