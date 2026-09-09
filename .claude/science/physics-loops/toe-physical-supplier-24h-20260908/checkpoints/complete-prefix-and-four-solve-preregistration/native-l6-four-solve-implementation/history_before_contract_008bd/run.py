"""Prospective strict wrapper. Full run requires external reviewed CONTRACT.json."""
import sys,os,json,hashlib,time,signal,resource,importlib.util
from pathlib import Path
P=Path(__file__).resolve().parent;start=time.monotonic()
if not sys.flags.isolated or not sys.dont_write_bytecode or len(sys.argv)!=3 or sys.argv[1] not in ('readiness','run'):raise ValueError('-I -B run.py readiness|run OUTPUT')
f=json.loads((P/'RUNTIME_FREEZE.json').read_text())
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(x.name for x in P.iterdir() if x.is_dir() or x.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for path,h in f['inputs'].items():
 if sha(path)!=h:raise ValueError('pin '+path)
if any(os.environ.get(k)!='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')):raise ValueError('threads')
# Import reviewed local modules explicitly, never extend ambient sys.path.
for name in ('exact_square','envelope','real_kernel','transport','fp_guard','norms','cg_candidate','formats','validate_coefficients','worker'):
 spec=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m)
def loaded():
 for m in list(sys.modules.values()):
  path=getattr(m,'__file__',None)
  if path:
   path=str(Path(path).resolve())
   if path not in f['inputs'] or sha(path)!=f['inputs'][path]:raise ValueError('loaded origin '+path)
loaded()
if sys.argv[1]=='readiness':print(json.dumps({'status':'PASS','imports_only':True,'physical_calls':0}));raise SystemExit
contract=P/'CONTRACT.json'
if not contract.exists():raise RuntimeError('No reviewed full-CG execution contract; unlaunched')
c=json.loads(contract.read_text())
if c.get('authorized') is not True or c.get('source_freeze')!=sha(P/'RUNTIME_FREEZE.json'):raise ValueError('contract')
out=Path(sys.argv[2]).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
signal.alarm(int(c['internal_seconds']))
try:
 import numpy as np
 result=sys.modules['worker'].planned_worker(np,out);loaded()
 if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise MemoryError('RSS')
except BaseException as e:
 out.mkdir(exist_ok=True);(out/'FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-start})+'\n');raise
