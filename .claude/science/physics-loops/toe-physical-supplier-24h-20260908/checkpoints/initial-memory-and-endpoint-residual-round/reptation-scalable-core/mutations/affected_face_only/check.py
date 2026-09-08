import os,time,signal,resource,json,hashlib
for v in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[v]='1'
start=time.monotonic();signal.alarm(180)
from pathlib import Path
import numpy as np
import core
p=Path(__file__).resolve().parent
slow={};s=(p/'slow_original.py').read_text().replace('L not in (2,4)','(L<2 or L%2)');exec(compile(s,'slow_domain_only','exec'),slow)
checks=0;maxerr=0

def req(c):
 global checks
 checks+=1
 if not c:raise RuntimeError('independent comparison failed')
rng=np.random.default_rng(812908);rows=[]
for L in (4,8,12):
 faces,coef,seed=core.geometry(L);affected=core.affected_faces(faces);x=seed.copy()
 for j in range(64):
  candidates=[i for i,f in enumerate(faces) if core.legal(x,f)]
  f=candidates[int(rng.integers(len(candidates)))];x[faces[f]]^=1
 legalchecks=0
 for state in (seed,x):
  nf=core.count(state,faces);O=coef@(state.astype(float)-.5)
  for j,f in enumerate(faces):
   y=state.copy();y[f]^=1
   req(core.next_count(state,j,faces,affected,nf)==core.count(y,faces))
   if core.legal(state,f):
    err=float(np.max(np.abs(O+coef[:,f]@(1.-2*state[f])-coef@(y.astype(float)-.5))))
    maxerr=max(maxerr,err);req(err<1e-11);legalchecks+=1
  req(core.next_count(state,-1,faces,affected,nf)==nf)
 rows.append(dict(L=L,faces=len(faces),legal_Fourier_checks=legalchecks,max_affected=max(map(len,affected))))
class Uniforms:
 def __init__(self,v):self.v=iter(v)
 def random(self):return next(self.v)
replay=[]
for L,N in ((4,1000),(8,200)):
 a=core.Path(L,20);b=slow['Path'](L,20);accepts=0
 for j in range(N):
  u=rng.random(2);ra=a.step(Uniforms(u));rb=b.step(Uniforms(u));req(ra==rb);accepts+=int(ra[1])
  req(a.head==b.head and a.direction==b.direction and a.nf==b.nf and np.array_equal(a.labels,b.labels))
  req(all(np.array_equal(x,y) for x,y in zip(a.states,b.states)))
  req(all(np.max(np.abs(x-y))<1e-11 for x,y in zip(a.O,b.O)))
 replay.append(dict(L=L,events=N,accepted=accepts))
a=core.Path(8,20);t=time.monotonic()
for j in range(1000):a.step(rng)
micro=time.monotonic()-t;req(micro<30)
import sys
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);req(0<rss<384)
print(json.dumps(dict(status='PASS',checks=checks,local=rows,replay=replay,max_Fourier_error=maxerr,micro_events=1000,micro_seconds=micro,seconds=time.monotonic()-start,peak_MiB=rss,sha256={n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ('core.py','slow_original.py','check.py','PREREGISTRATION.md')}),indent=2,allow_nan=False))
