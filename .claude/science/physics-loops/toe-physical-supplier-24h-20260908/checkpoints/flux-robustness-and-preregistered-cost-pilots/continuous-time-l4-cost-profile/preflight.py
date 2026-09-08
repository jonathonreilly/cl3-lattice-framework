import json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def verify():
 f=json.loads((B/'FREEZE.json').read_text())
 if sorted(p.name for p in B.glob('*.py'))!=f['python_membership']:raise ValueError('source membership')
 for p,h in f['files'].items():
  if sha(B/p)!=h:raise ValueError('source pin '+p)
 for p,h in json.loads((B/'RUNTIME.json').read_text())['files'].items():
  if sha(p)!=h:raise ValueError('runtime pin '+p)
 return sha(B/'FREEZE.json')
