"""Portable receipt and synthetic checks; no estimator or native replay."""
from pathlib import Path
import runpy,hashlib,json,io,contextlib
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/native-quartic-ward-20260910'
def main():
 for row in json.loads((PACK/'IMPORT_PROVENANCE.json').read_text()):
  assert hashlib.sha256((ROOT/row['local']).read_bytes()).hexdigest()==row['sha256'],row['local']
 out=io.StringIO()
 with contextlib.redirect_stdout(out):runpy.run_path(str(PACK/'source_draft/check.py'))['main']()
 result=json.loads(out.getvalue())
 assert result['status']=='PASS_COMPACT_ONLY' and result['native_or_event_arithmetic_replays']==0
 print(f"TOTAL: PASS={result['checks']} FAIL=0")
 print('SUPPORT_ONLY: both unchanged-trial intervals contain zero; integration and formal audit UNRUN')
if __name__=='__main__':main()
