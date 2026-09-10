"""Portable packet checks and synthetic algebra; no native numerical replay."""
from pathlib import Path
import runpy,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/native-stronger-ward-20260910'
def main():
 for row in json.loads((PACK/'IMPORT_PROVENANCE.json').read_text()):
  assert hashlib.sha256((ROOT/row['local']).read_bytes()).hexdigest()==row['sha256'],row['local']
 result=runpy.run_path(str(PACK/'source_draft/check.py'))['main']()
 assert result['native_replay']is False
 print(f"TOTAL: PASS={result['checks']} FAIL=0")
 print('SUPPORT_ONLY: all tested alpha intervals remain indeterminate; no native replay; full integration and formal audit UNRUN')
if __name__=='__main__':main()
