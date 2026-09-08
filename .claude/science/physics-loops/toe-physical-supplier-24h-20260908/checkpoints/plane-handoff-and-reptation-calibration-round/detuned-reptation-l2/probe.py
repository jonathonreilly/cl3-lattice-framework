import os,sys,signal,time,resource,json,hashlib
from pathlib import Path
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
sys.dont_write_bytecode=True;signal.alarm(60);start=time.monotonic()
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

T=np.full((n,24),-1,dtype=int)
for row,x in enumerate(states):
 for j,f in enumerate(faces):
  z=[(x>>i)&1 for i in f]
  if z[0]==z[2] and z[1]==z[3] and z[0]!=z[1]:T[row,j]=index[x^sum(1<<i for i in f)]
from scipy.sparse import csr_matrix,eye,diags
require=lambda c,s: None if c else (_ for _ in ()).throw(RuntimeError(s))
require(n==864 and len(moves)==6912,'component')
H=.95*diags(nf)-csr_matrix(A);G=eye(n)-H/24;b=1+.05*nf/24;S=np.sum(O*O,axis=1)
require(np.max(abs(np.asarray(G.sum(1)).ravel()-b))<1e-14,'rows')
for x in range(n):
 for f in range(24):
  if T[x,f]>=0:require(T[T[x,f],f]==x,'same-label reverse')
def power(k):
 psi=np.ones(n)
 for _ in range(k):psi=G@psi;psi/=np.linalg.norm(psi)
 return psi
oracle=[]
for bonds in [48,192,768]:
 psi=power(bonds//2);mid=psi**2;end=power(bonds);end/=end.sum();en=-.05*(end@nf);ray=psi@(H@psi)
 require(abs(en-ray)<1e-12,'endpoint Rayleigh');nn=mid@nf;ss=mid@S
 oracle.append(dict(n=bonds,tau=bonds/48,midNf=float(nn),midS=float(ss),endpointE=float(en),rayleigh=float(ray),finite_dirichlet=float(.5*(.95*nn-en)/ss)))
bonds=192;buf=np.zeros(bonds+1,int);head=0;direction=1;direct=[0]*(bonds+1);rng=np.random.default_rng(202609090701);series=[];events=[];runs=[];run=0;t=time.monotonic()
for step in range(4096):
 old=buf[(head+bonds)%(bonds+1)] if direction==1 else buf[head];second=buf[(head+1)%(bonds+1)] if direction==1 else buf[(head+bonds-1)%(bonds+1)]
 u=rng.random()*(24+.05*nf[old]);f=int(u) if u<24 else -1;y=T[old,f] if f>=0 else -1;label=f if y>=0 else -1;y=y if y>=0 else old
 accept=rng.random()<min(1,b[old]/b[second]);before=direction
 if accept:
  if direction==1:buf[head]=y;head=(head+1)%(bonds+1);direct=direct[1:]+[int(y)]
  else:head=(head-1)%(bonds+1);buf[head]=y;direct=[int(y)]+direct[:-1]
  run+=1
 else:direction=-direction;runs.append(run);run=0
 require(np.array_equal(np.roll(buf,-head),direct),'buffer')
 mid=buf[(head+bonds//2)%(bonds+1)];series.append([nf[mid],S[mid],-.05*(nf[buf[head]]+nf[buf[(head+bonds)%(bonds+1)]])/2]);events.append([before,label,int(accept)])
hot=time.monotonic()-t;series=np.array(series);events=np.array(events);np.savez_compressed(p/'MICRO_RAW.npz',series=series,events=events,final_path=np.roll(buf,-head),states=states,targets=T,Nf=nf,S=S)
z=series-series.mean(0);variance=(z*z).mean(0);lags=[]
for lag in [1,4,16,64,256]:lags.append(dict(lag=lag,normalized=((z[:-lag]*z[lag:]).mean(0)/variance).tolist()))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);require(rss<384 and time.monotonic()-start<60,'resources')
print(json.dumps(dict(mode='nonequilibrated resource micro only',oracle=oracle,updates=4096,seed=202609090701,mean=series.mean(0).tolist(),covariance=np.cov(series,rowvar=False).tolist(),self_proposals=int(sum(events[:,1]<0)),accepted_self=int(sum((events[:,1]<0)&(events[:,2]==1))),rejections=int(sum(events[:,2]==0)),completed_direction_runs=runs,unfinished_run=run,lag_diagnostics=lags,hot_seconds=hot,seconds=time.monotonic()-start,rss_mib=rss,source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2,allow_nan=False))
