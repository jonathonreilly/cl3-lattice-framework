import os,sys,signal,time,resource,json,hashlib
from pathlib import Path
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
sys.dont_write_bytecode=True;signal.alarm(180);start=time.monotonic()
import numpy as np
from itertools import product,combinations
p=Path(__file__).resolve().parent;rs=list(product(range(2),repeat=3));links=[(r,a) for r in rs for a in range(3)];ix={x:i for i,x in enumerate(links)};faces=[]
for a,b in combinations(range(3),2):
 for r in rs:
  ra=list(r);rb=list(r);ra[a]^=1;rb[b]^=1;faces.append([ix[r,a],ix[tuple(ra),b],ix[tuple(rb),a],ix[r,b]])
x0=sum(1<<i for i,(r,a) in enumerate(links) if r[a]);states=[x0];index={x0:0};moves=[]
for x in states:
 for f in faces:
  z=[(x>>i)&1 for i in f]
  if z[0]==z[2] and z[1]==z[3] and z[0]!=z[1]:
   y=x^sum(1<<i for i in f)
   if y not in index:index[y]=len(states);states.append(y)
   moves.append((index[x],index[y]))
n=len(states);M=24;A=np.zeros((n,n))
for i,j in moves:A[i,j]+=1
nf=A.sum(1);H=np.diag(nf)-A;P=np.eye(n)-H/M
O=np.array([[sum((-1)**(sum(r)+r[a])*(((x>>i)&1)-.5)/np.sqrt(8) for i,(r,b) in enumerate(links) if b==pol) for a in range(3) for pol in range(3) if pol!=a] for x in states]);S=np.sum(O*O)/n
checks={}
def ck(k,b):
 if not bool(b):raise AssertionError(k)
 checks[k]=True
ck('actual_graph',n==864 and len(moves)==6912);ck('stochastic',np.min(P)>=0 and np.max(abs(P.sum(1)-1))<1e-14);ck('seed_self_loop',P[0,0]==.5);ck('centered_sources',np.max(abs(O.mean(0)))<1e-14)
e,U=np.linalg.eigh(H);amp=np.sum(abs(U.T@O)**2,axis=1)/n;ck('unique_zero',abs(e[0])<1e-12 and e[1]>0);ck('weight',abs(sum(amp)-S)<1e-12 and amp[0]<1e-24)
w=amp[1:]/S;om=e[1:];z=1-om/M;inv=float(sum(w/om));m1=float(sum(w*om));ck('inverse_exposed_comparison',abs(1/inv-1.38398932012680)<1e-11)
# Direct pseudoinverse contraction independently against spectral sum.
f=O/np.sqrt(n);projector=np.ones((n,n))/n;solution=np.linalg.solve(H+projector,f);direct=float(np.sum(f*solution)/S);ck('Poisson_pseudoinverse',abs(direct-inv)<1e-12)
lagrows=[]
for K in [0,1,4,16,64,256]:
 elementary=float(sum(w*(1-z**(K+1))/(1-z))/M)
 sweep=float(sum(w*(1-z**(M*(K+1)))/(1-z**M)))
 # Direct repeated matrix application at elementary grid (all six sources).
 v=O.copy();raw=0.
 for j in range(K+1):raw+=float(np.sum(O*v)/(n*S*M));v=P@v
 ck('direct_elementary_'+str(K),abs(raw-elementary)<1e-12)
 lagrows.append({'max_lag':K,'elementary_sum_divM':elementary,'elementary_error':elementary-inv,'sweep_sum':sweep,'sweep_minus_inverse':sweep-inv})
sweepinf=float(sum(w/(1-z**M)));continuoushalf=float(sum(w*(.5+1/(np.exp(om)-1))))
ck('sweep_naive_wrong',abs(sweepinf-inv)>.1)
# Different elementary eigenvalues with identical sweep samples for even M.
ck('sweep_alias',abs((.5)**M-(-.5)**M)==0 and abs(1/(M*(1-.5))-1/(M*(1+.5)))>.05)
# Positive-p correction bound derived separately in text; verify all actual p when applicable.
positive=bool(np.min(z)>=0)
if positive:ck('positive_sweep_correction',0<=sweepinf-inv<=(M-1)/M+1e-12)
rows=[]
for alpha in [.25,.5,1.]:
 q=M/(M+alpha);K=int(np.ceil(np.log(alpha*.001)/np.log(q)))-1
 true=float(sum(w/(om+alpha)));geom=float(sum(w/(M+alpha)/(1-q*z)))
 trunc=float(sum(w/(M+alpha)*(1-(q*z)**(K+1))/(1-q*z)));bound=q**(K+1)/alpha
 ck('resolvent_'+str(alpha),abs(true-geom)<1e-12 and abs(true-trunc)<=bound+1e-12 and bound<=.001+1e-12)
 rows.append({'alpha':alpha,'inverse_regularized':true,'bias_from_unregularized':true-inv,'expected_elementary_steps':M/alpha,'Kmax':K,'truncated_value':trunc,'actual_truncation_error':trunc-true,'absolute_tail_bound':bound})
ck('resource',time.monotonic()-start<180 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)<384)
out={'checks':checks,'count':len(checks),'S_sum':S,'m1':m1,'inverse_moment':inv,'inverse_reciprocal':1/inv,'spectral_max':float(e[-1]),'P_min_eigenvalue':float(1-e[-1]/M),'sweep_integral':sweepinf,'sweep_error':sweepinf-inv,'continuous_unit_trapezoid':continuoushalf,'lag_rows':lagrows,'resolvents':rows,'seconds':time.monotonic()-start,'rss_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};(p/'RESULT.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');np.savez_compressed(p/'spectral_raw.npz',energy=e,weight=amp,S=S);print(json.dumps(out,indent=2,allow_nan=False))
