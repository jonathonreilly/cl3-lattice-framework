"""Hash-only preflight, safe to execute without any spectral call."""
import sys
if not sys.flags.isolated:raise RuntimeError('isolated Python -I required')
from pathlib import Path
import hashlib,json,os,sys

def verify():
 root=Path(__file__).resolve().parent
 f=json.loads((root/'FREEZE.json').read_text());r=json.loads((root/'RUNTIME.json').read_text())
 allowed={name for name in f['files'] if not Path(name).is_absolute()}
 for item in root.rglob('*'):
  rel=item.relative_to(root)
  if rel.parts[0]=='__pycache__':continue # -I prevents imports from this directory
  if item.is_dir():raise RuntimeError('unlisted local package directory '+str(rel))
  if item.suffix in ('.py','.so','.dylib','.pyc','.pyo') and str(rel) not in allowed:raise RuntimeError('unlisted local module '+str(rel))
 if str(Path(sys.executable).resolve())!=r['interpreter']:raise RuntimeError('wrong interpreter')
 for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
  if os.environ.get(name)!='1':raise RuntimeError('single-thread setting '+name)
 if (root/'COST_RESULT.json').exists():raise RuntimeError('existing pilot result; no rerun')
 for name,expected in {**f['files'],**r['files']}.items():
  p=Path(name);p=p if p.is_absolute() else root/p
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:raise RuntimeError('changed input '+name)
 return hashlib.sha256((root/'FREEZE.json').read_bytes()).hexdigest()
if __name__=='__main__':print(json.dumps(verify()))

def verify_numpy(np):
 root=Path(__file__).resolve().parent;r=json.loads((root/'RUNTIME.json').read_text())
 origin=str(Path(np.__file__).resolve())
 if origin not in r['files'] or not origin.endswith('/numpy/__init__.py') or np.__version__!=r['numpy_version']:raise RuntimeError('unexpected NumPy origin/version')
 for name,module in list(sys.modules.items()):
  if name=='numpy' or name.startswith('numpy.'):
   path=getattr(module,'__file__',None)
   if path and str(Path(path).resolve()) not in r['files']:raise RuntimeError('unbound loaded NumPy module '+name)
 return origin
