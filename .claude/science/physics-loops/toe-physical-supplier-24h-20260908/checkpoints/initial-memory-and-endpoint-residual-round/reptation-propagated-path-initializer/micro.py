import os,time,signal,resource,json,sys,hashlib
for v in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[v]='1'
start=time.monotonic();signal.alarm(30)
import numpy as np
from initialize import initialize
from core import count
from pathlib import Path
p=Path(__file__).resolve().parent;rng=np.random.default_rng(812913);t=time.monotonic();a,info=initialize(4,13824,rng,128);init=time.monotonic()-t
initial_NF=a.nf.copy();initial_X=[float(np.vdot(o,o).real) for o in a.O];v=np.zeros(4);accepted=0;t=time.monotonic()
for j in range(4096):
 _,ok=a.step(rng);accepted+=int(ok);o=a.O[1];v+=[a.nf[1],np.vdot(o[:6],o[:6]).real,np.vdot(o[6:],o[6:]).real,-.05*(a.nf[0]+a.nf[2])/2]
hot=time.monotonic()-t
for i,x in enumerate(a.states):
 if a.nf[i]!=count(x,a.faces) or np.max(abs(a.O[i]-a.coeff@(x.astype(float)-.5)))>1e-9:raise RuntimeError('cache')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<384 or time.monotonic()-start>=30:raise RuntimeError('micro resource')
print(json.dumps(dict(seed=812913,L=4,n=13824,info=info,initialization_seconds=init,updates=4096,update_measurement_seconds=hot,accepted=accepted,initial_NF=initial_NF,initial_X12=initial_X,diagnostic_means=(v/4096).tolist(),seconds=time.monotonic()-start,peak_MiB=rss,scope='one throughput/cache micro, not scientific estimate or equilibration evidence',sha256={n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ('core.py','initialize.py','micro.py','PREREGISTRATION.md')}),indent=2,allow_nan=False))
