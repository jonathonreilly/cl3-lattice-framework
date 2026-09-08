from pathlib import Path
import hashlib,json
B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def verify():
 f=json.loads((B/'FINAL_FREEZE.json').read_text())
 if sorted(p.name for p in B.glob('*.py'))!=f['python_membership']:raise ValueError('source membership')
 for name,h in f['files'].items():
  if sha(B/name)!=h:raise ValueError('source pin '+name)
 for name,h in json.loads((B/'RUNTIME.json').read_text())['files'].items():
  if sha(name)!=h:raise ValueError('external runtime pin '+name)
 return sha(B/'FINAL_FREEZE.json')
