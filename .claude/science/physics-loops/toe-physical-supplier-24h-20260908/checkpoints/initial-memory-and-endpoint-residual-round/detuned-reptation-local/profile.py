import os,sys,time,signal,resource,json,pathlib,hashlib
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
start=time.monotonic();signal.alarm(30)
import numpy as np
from core import Path,geometry,legal
p=pathlib.Path(__file__).resolve().parent
faces,coeff,seed=geometry(4,(1,2));checks=0;x=seed.copy()
for sample in range(8):
 # Explicit independent coordinate loop verifies both complex coefficients.
 direct=[]
 for h in [1,2]:
  for a in range(3):
   for b in range(3):
    if a==b:continue
    z=0j
    for i in range(192):
     r=np.unravel_index(i//3,(4,4,4));pol=i%3
     if pol==b:z+=(-1)**sum(r)*np.exp(2j*np.pi*h*r[a]/4)*(float(x[i])-.5)/8
    direct.append(z)
 if np.max(abs(coeff@(x.astype(float)-.5)-direct))>1e-12:raise RuntimeError('harmonic dictionary')
 for f in faces:
  if legal(x,f):
   y=x.copy();y[f]^=1
   if np.max(abs(coeff@(y.astype(float)-.5)-coeff@(x.astype(float)-.5)-coeff[:,f]@(1.-2*x[f])))>1e-12:raise RuntimeError('allflip complex')
   checks+=12
 available=[f for f in faces if legal(x,f)];x[available[sample%len(available)]]^=1
init=time.monotonic();a=Path(4,384,(1,2));initialization=time.monotonic()-init;rng=np.random.default_rng(202609150401);t=time.monotonic();reject=selfmoves=0
for _ in range(8192):
 f,ok=a.step(rng);reject+=not ok;selfmoves+=f<0
hot=time.monotonic()-t
for j,x in enumerate(a.states):
 if np.max(abs(a.O[j]-a.coeff@(x.astype(float)-.5)))>1e-11:raise RuntimeError('cache drift')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if rss>=384 or time.monotonic()-start>=30:raise RuntimeError('resource')
print(json.dumps(dict(scope='throughput diagnostic only',updates=8192,n=384,harmonics=[1,2],seed=202609150401,allflip_mode_checks=checks,initialization_seconds=initialization,hot_seconds=hot,seconds=time.monotonic()-start,rss_mib=rss,rejections=reject,self_proposals=selfmoves,core_sha=hashlib.sha256((p/'core.py').read_bytes()).hexdigest()),indent=2))
