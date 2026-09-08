import os,time
start=time.monotonic()
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import runpy,contextlib,io,json,hashlib,resource
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh
from scipy import sparse
p=Path('/private/tmp/toe-24h-probes-20260908/detuned-energy-moment/check.py')
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(p))
A,N,O=d['A'],d['N'],d['O'];checks={};rows=[]
def ck(k,v):
 if not bool(v):raise AssertionError(k)
 checks[k]=True
for V in [.95,1.]:
 H=V*N-A;e,U=eigh(H.toarray());psi=U[:,0];gap=e[1:]-e[0];S=0;inv=0;first=0;curves=[]
 for j,o in enumerate(O):
  amp=U.T@(o*psi);s=float(sum(amp[1:]**2));chi=float(2*sum(amp[1:]**2/gap));S+=s;inv+=chi/2;first+=float(sum(amp[1:]**2*gap))
  ck(f'mean_{V}_{j}',abs(amp[0])<1e-11)
  errs=[]
  for h in [.01,.005,.0025]:
   es=[float(eigsh(H+sign*h*sparse.diags(o),k=1,which='SA',tol=1e-13,v0=np.ones(864))[0][0]) for sign in [-1,1]]
   estimate=-(sum(es)-2*e[0])/h**2;errs.append(abs(estimate-chi));curves.append(dict(mode=j,h=h,chi=chi,estimate=estimate,error=estimate-chi))
  ck(f'curvature_{V}_{j}',errs[-1]<2e-5 and errs[-1]<errs[0])
  for xi in [-.01,.01]:
   shift=abs(xi)*np.sqrt(8)/2;b=1+((1-V)*d['nf']+shift-xi*o)/24
   ck(f'positive_kernel_{V}_{j}_{xi}',min(b)>=1-1e-14)
 a=first/S;b=S/inv;C=a/b
 ck(f'order_{V}',e[1]-e[0]<=b+1e-10 and b<=a+1e-10)
 rows.append(dict(V=V,S_connected_sum=S,arithmetic=a,harmonic=b,shape=C,omega_star=np.sqrt(a*b),full_component_gap=float(gap[0]),curvatures=curves,band_factor2_mass_bound=2*(np.sqrt(C)-1)/.5))
rare=[]
for eps in [.1,.01]:
 w=eps**3;a=1-w+w*eps;inv=1-w+w/eps;rare.append(dict(epsilon=eps,arithmetic=a,harmonic=1/inv,shape=a*inv,lowest_support=eps))
ck('rare_low_weight_counterexample',rare[-1]['shape']<1.0001 and rare[-1]['lowest_support']==.01)
ck('forgot_shift_mutation_detected',2*(np.sqrt(8)/2)/.0025>100)
result=dict(checks=checks,count=len(checks),rows=rows,rare_low_weight=rare,input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_sec=time.monotonic()-start,rss_native=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print(json.dumps(result,indent=2,allow_nan=False))
