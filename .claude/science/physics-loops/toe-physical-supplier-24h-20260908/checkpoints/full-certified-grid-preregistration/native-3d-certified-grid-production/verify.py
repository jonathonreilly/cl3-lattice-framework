import sys
if not sys.flags.isolated:raise RuntimeError('isolated Python required')
from pathlib import Path
import json,hashlib,os
B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def verify():
 f=json.loads((B/'FREEZE.json').read_text());r=json.loads((B/'RUNTIME.json').read_text());allowed={n for n in f['files'] if not Path(n).is_absolute()}
 for p in B.rglob('*'):
  rel=p.relative_to(B)
  if rel.parts[0]=='__pycache__':continue
  if p.is_dir():raise ValueError('unlisted local package')
  if p.suffix in ('.py','.so','.dylib','.pyc','.pyo') and str(rel) not in allowed:raise ValueError('unlisted local module')
 for p,h in {**f['files'],**r['files']}.items():
  q=Path(p);q=q if q.is_absolute() else B/q
  if sha(q)!=h:raise ValueError('source/runtime pin '+p)
 if str(Path(sys.executable).resolve())!=r['interpreter']:raise ValueError('interpreter')
 for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
  if os.environ.get(n)!='1':raise ValueError('thread setting')
 return sha(B/'FREEZE.json')
def verify_numpy(np):
 r=json.loads((B/'RUNTIME.json').read_text())
 if np.__version__!=r['numpy_version'] or str(Path(np.__file__).resolve()) not in r['files']:raise ValueError('numpy identity')
 for n,m in list(sys.modules.items()):
  p=getattr(m,'__file__',None)
  if p and (n=='numpy' or n.startswith('numpy.')) and str(Path(p).resolve()) not in r['files']:raise ValueError('numpy module pin')
