from pathlib import Path
import hashlib,json,sys,os
P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def verify():
 if not sys.flags.isolated:raise ValueError('requires isolated -I interpreter')
 f=json.loads((P/'FREEZE.json').read_text())
 actual=sorted(str(p.relative_to(P)) for p in P.rglob('*') if p.is_file() and p.suffix in ('.py','.so','.dylib','.pyc'))
 if actual!=f['executable_membership']:raise ValueError('local executable membership')
 if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter origin')
 for name,h in f['files'].items():
  if sha(P/name)!=h:raise ValueError('source pin '+name)
 for name,h in f['dependencies'].items():
  if sha(name)!=h:raise ValueError('dependency pin '+name)
 for name,h in f['runtime'].items():
  if sha(name)!=h:raise ValueError('runtime pin '+name)
 for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
  if os.environ.get(key)!='1':raise ValueError('thread pin '+key)
 return sha(P/'FREEZE.json'),f
