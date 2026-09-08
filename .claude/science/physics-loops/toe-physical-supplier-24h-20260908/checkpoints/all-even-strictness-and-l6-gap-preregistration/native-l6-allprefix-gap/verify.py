from pathlib import Path
import hashlib,json
B=Path(__file__).parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def verify():
 f=json.loads((B/'FREEZE.json').read_text())
 for p,h in f['files'].items():
  if sha(B/p)!=h:raise ValueError('local pin '+p)
 for p,h in f['runtime'].items():
  if sha(p)!=h:raise ValueError('runtime pin '+p)
 return sha(B/'FREEZE.json')
