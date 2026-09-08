import os
import sys,json,hashlib,time,signal,resource,importlib.util,math
from pathlib import Path
P=Path(__file__).resolve().parent
if not sys.flags.isolated or not sys.dont_write_bytecode or len(sys.argv)!=2:raise ValueError('-I -B run.py FRESH_OUTPUT')
start=time.monotonic();signal.alarm(29)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
f=json.loads((P/'FREEZE.json').read_text())
if sorted(x.name for x in P.iterdir() if x.suffix in ('.py','.pyc','.so','.dylib') or x.is_dir())!=f['membership']:raise ValueError('shadow membership')
for p,h in f['inputs'].items():
 if sha(p)!=h:raise ValueError('input '+p)
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if any(os.environ.get(x)!='1' for x in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')):raise ValueError('thread1 environment')
out=Path(sys.argv[1]).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh output')
out.mkdir(parents=True);rows=[]
try:
 spec=importlib.util.spec_from_file_location('action_kernel',P/'kernel.py');k=importlib.util.module_from_spec(spec);spec.loader.exec_module(k)
 if str(Path(k.np.__file__).resolve())!=f['numpy_origin'] or k.np.__version__!=f['numpy_version']:raise ValueError('numpy origin/version')
 for module in list(sys.modules.values()):
  path=getattr(module,'__file__',None)
  if path and 'numpy' in path and str(Path(path).resolve()) not in f['inputs']:raise ValueError('unbound numpy module')
 raw=json.loads(Path(f['basis']).read_text())['one_star'];result=json.loads(Path(f['basis_result']).read_text());lambdas=[r['lambda'] for r in result['cases'][0]['sectors'] for _ in range(r['blocks'])]
 if len(raw)!=42 or len(lambdas)!=21:raise ValueError('frame')
 coeff={v:[(raw[2*j]['vector'][v]/math.sqrt(raw[2*j]['norm_squared']),raw[2*j+1]['vector'][v]/math.sqrt(raw[2*j+1]['norm_squared'])) for j in range(21)] for v in range(216)}
 from itertools import product
 vs=list(product(range(6),repeat=3));vi={v:i for i,v in enumerate(vs)};edges=[]
 for v in vs:
  for a in range(3):
   w=list(v);w[a]=(w[a]+1)%6;i,j=sorted((vi[v],vi[tuple(w)]));edges.append((i,j,-2*(-1)**sum(v[:a])))
 def edge(v):return next(e for e,(i,j,z) in enumerate(edges) if {i,j}=={0,vi[v]})
 pairs=[(edge((1,0,0)),edge((0,1,0))),(edge((1,0,0)),edge((5,0,0)))];np=k.np
 ids=np.arange(k.SIZE,dtype=np.int64);x=((ids%17)-8).astype(np.complex128)/16;del ids
 rows=[]
 for name,pair in zip(('perpendicular','opposite'),pairs):
  t=time.monotonic();y=k.action(x,coeff,edges,pair,lambdas);action=time.monotonic()-t
  if not np.isfinite(y).all():raise ValueError('nonfinite candidate')
  t=time.monotonic();path=out/(name+'.npy');np.save(path,y,allow_pickle=False);loaded=np.load(path,allow_pickle=False)
  if not np.array_equal(y,loaded):raise ValueError('serialization')
  io=time.monotonic()-t;rows.append(dict(name=name,pair=pair,action_seconds=action,serialization_seconds=io,sha256=sha(path),bytes=path.stat().st_size));del y,loaded
  (out/'PARTIAL.json').write_text(json.dumps(dict(rows=rows,seconds=time.monotonic()-start,freeze=sha(P/'FREEZE.json')),indent=2)+'\n')
  if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise MemoryError('RSS')
 payload=dict(status='COMPLETE',rows=rows,seconds=time.monotonic()-start,rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,freeze=sha(P/'FREEZE.json'),scope='two candidate operator actions cost only; no residual/CG/spectrum certificate')
 (out/'RESULT.json').write_text(json.dumps(payload,indent=2)+'\n')
except BaseException as e:
 (out/'FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-start,'rows':rows})+'\n');raise
