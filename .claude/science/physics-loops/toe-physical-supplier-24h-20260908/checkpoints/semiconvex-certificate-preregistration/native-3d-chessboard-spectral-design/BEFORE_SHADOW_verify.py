"""Hash-only preflight, safe to execute without any spectral call."""
from pathlib import Path
import hashlib,json,os,sys

def verify():
 root=Path(__file__).resolve().parent
 f=json.loads((root/'FREEZE.json').read_text());r=json.loads((root/'RUNTIME.json').read_text())
 if str(Path(sys.executable).resolve())!=r['interpreter']:raise RuntimeError('wrong interpreter')
 for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
  if os.environ.get(name)!='1':raise RuntimeError('single-thread setting '+name)
 if (root/'COST_RESULT.json').exists():raise RuntimeError('existing pilot result; no rerun')
 for name,expected in {**f['files'],**r['files']}.items():
  p=Path(name);p=p if p.is_absolute() else root/p
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:raise RuntimeError('changed input '+name)
 return {'status':'source/runtime binding PASS; no spectral execution','source_files':len(f['files']),'runtime_files':len(r['files'])}
if __name__=='__main__':print(json.dumps(verify()))
