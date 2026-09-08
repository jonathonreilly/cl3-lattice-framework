import json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def verify(root=B):
 root=Path(root);f=json.loads((root/'FINAL_FREEZE.json').read_text())
 actual={p.name for p in root.glob('*.py')}|{p.name for p in root.glob('*.sh')}
 if actual!=set(f['executable_membership']):raise ValueError('source membership')
 for name,h in f['files'].items():
  if sha(root/name)!=h:raise ValueError('source pin '+name)
 for name,h in json.loads((root/'RUNTIME.json').read_text())['files'].items():
  if sha(name)!=h:raise ValueError('runtime pin '+name)
 return sha(root/'FINAL_FREEZE.json')
