"""Hash and import closure guards; no gap or baseline arithmetic."""
from pathlib import Path
import sys,json,hashlib,math,os
P=Path(__file__).resolve().parent
def require(c,m):
 if not c:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def verify():
 require(sys.flags.isolated and sys.dont_write_bytecode,'requires -I -B')
 f=json.loads((P/'FREEZE.json').read_text())
 actual=sorted(str(x.relative_to(P)) for x in P.rglob('*') if x.is_file() and x.suffix in ('.py','.pyc','.so','.dylib'))
 require(actual==f['membership'],'executable membership')
 require(str(Path(sys.executable).resolve())==f['interpreter'],'interpreter origin')
 for name,h in f['files'].items():require(sha(P/name)==h,'source '+name)
 for name,h in f['runtime'].items():require(sha(name)==h,'runtime '+name)
 for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):require(os.environ.get(name)=='1','threads')
 verify_loaded(f)
 return f
def verify_loaded(f):
 for module in tuple(sys.modules.values()):
  name=getattr(module,'__file__',None)
  if not name:continue
  path=str(Path(name).resolve())
  if path.startswith(str(P)+'/'):
   rel=str(Path(path).relative_to(P));require(rel in f['files'] and sha(path)==f['files'][rel],'loaded local origin')
  else:require(path in f['runtime'] and sha(path)==f['runtime'][path],'loaded runtime origin '+path)
