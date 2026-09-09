import os,sys,json,time,hashlib,signal,resource,importlib.util
from pathlib import Path
P=Path(__file__).resolve().parent;start=time.monotonic();signal.alarm(29)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if not sys.flags.isolated or not sys.dont_write_bytecode or len(sys.argv)!=2:raise ValueError('-I -B fresh output')
f=json.loads((P/'FREEZE.json').read_text())
if sorted(x.name for x in P.iterdir() if x.suffix in ('.py','.pyc','.so','.dylib') or x.is_dir())!=f['membership']:raise ValueError('membership')
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if any(os.environ.get(x)!='1' for x in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')):raise ValueError('threads')
for path,h in f['inputs'].items():
 if sha(path)!=h:raise ValueError('pin '+path)
out=Path(sys.argv[1]).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external')
out.mkdir(parents=True);rows=[]
try:
 import numpy as np
 if str(Path(np.__file__).resolve())!=f['numpy_origin'] or np.__version__!=f['numpy_version']:raise ValueError('numpy')
 for m in list(sys.modules.values()):
  path=getattr(m,'__file__',None)
  if path and 'numpy' in path and str(Path(path).resolve()) not in f['inputs']:raise ValueError('numpy module')
 spec=importlib.util.spec_from_file_location('transport',P/'transport.py');t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t);cases=json.loads((P/'CASES.json').read_text())
 ids=np.arange(1<<20,dtype=np.int64);x=((ids%17)-8)/16+1j*((ids%13)-6)/32;del ids
 for parity in cases['parities']:
  begun=time.monotonic();y=t.apply(x,cases['symmetry_index'],parity);action=time.monotonic()-begun
  if not np.isfinite(y).all():raise ValueError('finite')
  begun=time.monotonic();path=out/f'parity{parity}.npy';np.save(path,y,allow_pickle=False);z=np.load(path,allow_pickle=False)
  if not np.array_equal(z,y):raise ValueError('io roundtrip')
  io=time.monotonic()-begun;rows.append(dict(parity=parity,action_seconds=action,io_seconds=io,sha256=sha(path),bytes=path.stat().st_size))
  (out/'PARTIAL.json').write_text(json.dumps(dict(rows=rows,seconds=time.monotonic()-start,freeze=sha(P/'FREEZE.json')),indent=2)+'\n')
  del y,z
  if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise MemoryError('RSS')
 (out/'RESULT.json').write_text(json.dumps(dict(status='COMPLETE',rows=rows,seconds=time.monotonic()-start,rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,freeze=sha(P/'FREEZE.json'),scope='candidate transport cost only; no certified FP or physical solve'),indent=2)+'\n')
except BaseException as e:
 (out/'FAILURE.json').write_text(json.dumps(dict(error=repr(e),seconds=time.monotonic()-start,rows=rows))+'\n');raise
