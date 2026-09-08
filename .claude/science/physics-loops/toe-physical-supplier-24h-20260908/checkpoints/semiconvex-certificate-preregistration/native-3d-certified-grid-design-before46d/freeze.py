from pathlib import Path
import sys,json,hashlib,runpy,argparse,resource,signal,time,itertools
import exact_certificate,matrix,forecast
B=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r=json.loads((B/'RUNTIME.json').read_text())
for m in list(sys.modules.values()):
 name=getattr(m,'__file__',None)
 if name:
  p=Path(name).resolve()
  if p.is_file() and p.suffix not in ('.pyc','.pyo') and p.parent!=B:r['files'][str(p)]=sha(p)
(B/'RUNTIME.json').write_text(json.dumps(r,indent=2)+'\n')
refs=[B.parent/'native-3d-bloch-clifford/DERIVATION.md',B.parent/'native-spectral-arithmetic-certificate/DERIVATION.md',B.parent/'native-spectral-semiconvex-quadrature/DERIVATION.md',B.parent/'native-spectral-rational-trig/INPUTS.json',B.parent/'native-spectral-rational-trig/FREEZE.json']
(B/'SOURCE_BINDINGS.json').write_text(json.dumps({str(p):sha(p) for p in refs},indent=2)+'\n')
files={p.name:sha(p) for p in B.iterdir() if p.is_file() and p.name!='FREEZE.json'};files.update({str(p):sha(p) for p in refs})
(B/'FREEZE.json').write_text(json.dumps(dict(status='UNLAUNCHED, review and root external watchdog/checkpoint required',files=files),indent=2)+'\n');print(sha(B/'FREEZE.json'))
