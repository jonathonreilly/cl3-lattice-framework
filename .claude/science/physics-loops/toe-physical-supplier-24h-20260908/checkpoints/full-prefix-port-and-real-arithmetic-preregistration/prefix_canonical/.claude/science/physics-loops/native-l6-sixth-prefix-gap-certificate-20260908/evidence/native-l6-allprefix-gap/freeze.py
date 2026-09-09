from pathlib import Path
import sys,json,hashlib
import core, subprocess, signal, resource, verify
B=Path(__file__).parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
paths={Path(sys.executable).resolve()}
for m in list(sys.modules.values()):
 p=getattr(m,'__file__',None)
 if p and Path(p).is_file():paths.add(Path(p).resolve())
f=dict(status='UNLAUNCHED',files={p.name:sha(p) for p in B.iterdir() if p.is_file() and p.name!='FREEZE.json'},runtime={str(p):sha(p) for p in paths})
(B/'FREEZE.json').write_text(json.dumps(f,indent=2)+'\n');print(sha(B/'FREEZE.json'))
