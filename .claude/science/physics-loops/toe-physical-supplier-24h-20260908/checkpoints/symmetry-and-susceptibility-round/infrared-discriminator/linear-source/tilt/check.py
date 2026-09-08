import os,time,signal,sys
start=time.monotonic();signal.alarm(180)
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import numpy as np,runpy,contextlib,io,json,hashlib,resource
from pathlib import Path
from scipy import sparse
from scipy.sparse.linalg import eigsh
import kernel
p=Path(__file__).resolve().parent;inp=Path('/private/tmp/toe-24h-probes-20260908/detuned-energy-moment/check.py')
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(inp))
A,N,nf,states,faces=d['A'],d['N'],d['nf'],d['states'],d['faces'];n=len(states);lookup=d['lookup'];O=d['O'];F=O[0];I=sparse.eye(n)
coeff=np.array([(-1)**(sum(r)+r[0])/np.sqrt(8) if a==1 else 0 for r,a in d['links']]);checks={};rows=[]
def ck(k,b):
 if not bool(b):raise AssertionError(k)
 checks[k]=True
for V in [.95,1.]:
 for xi in [0.,-.01,.01,-.005,.005,-.0025,.0025]:
  b=kernel.branch(nf,F,V,xi,8);rs=[];cs=[];vs=[];cacheerr=0
  for i,x in enumerate(states):
   for f in range(24):
    y,g,w=kernel.step(x,F[i],f,0.,faces,coeff,nf[i],V,xi,8)
    cacheerr=max(cacheerr,abs(g-F[lookup[y]]));prob=1/(24*b[i]) if y!=x else 1/24
    rs.append(lookup[y]);cs.append(i);vs.append(prob)
    if y!=x:rs.append(i);cs.append(i);vs.append((1-1/b[i])/24)
  P=sparse.coo_matrix((vs,(rs,cs)),shape=(n,n)).tocsr();shift=abs(xi)*np.sqrt(8)/2;H=V*N-A+sparse.diags(xi*F);G=I-(H-shift*I)/24
  delta=P@sparse.diags(b)-G;res=max(abs(delta.data),default=0)
  ck(f'complete_{V}_{xi}',res<1e-12 and max(abs(np.asarray(P.sum(0)).ravel()-1))<1e-12 and min(P.data)>=-1e-14)
  ck(f'cache_{V}_{xi}',cacheerr<1e-12)
  E,u=eigsh(H,k=1,which='SA',tol=1e-13,v0=1+np.arange(n)/n);psi=u[:,0];Es=24*(1-sum(G@psi)/sum(psi));mixed=psi@((V-1)*nf+xi*F)/sum(psi)
  ck(f'restore_{V}_{xi}',abs(kernel.restore(Es,xi,8)-E[0])<1e-10 and abs(mixed-E[0])<1e-10)
  rows.append(dict(V=V,xi=xi,E=float(E[0]),residual=float(res),cache_error=float(cacheerr)))
# Actual finite symmetry checks: no forced sign equality in solves.
for V in [.95,1.]:
 for h in [.01,.005,.0025]:
  es=[r['E'] for r in rows if r['V']==V and abs(r['xi'])==h];ck(f'sign_symmetry_{V}_{h}',abs(es[0]-es[1])<1e-10)
# Fixed path micro is timing only, not a population/energy estimate.
rng=np.random.default_rng(81209);x=states[0];fval=F[0];t=time.monotonic()
for _ in range(10000):
 i=lookup[x];x,fval,b=kernel.step(x,fval,int(rng.integers(24)),rng.random(),faces,coeff,nf[i],.95,.01,8)
ck('micro_cache',abs(fval-F[lookup[x]])<1e-10)
micro=time.monotonic()-t;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
ck('resources',time.monotonic()-start<180 and rss<384 and micro<30)
r=dict(checks=checks,count=len(checks),rows=rows,micro_steps=10000,micro_seconds=micro,elapsed_sec=time.monotonic()-start,rss_mib=rss,hashes={str(q):hashlib.sha256(q.read_bytes()).hexdigest() for q in [inp,p/'kernel.py',Path(__file__)]})
print(json.dumps(r,indent=2,allow_nan=False))
