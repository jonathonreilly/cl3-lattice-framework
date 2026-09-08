import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import pathlib,json,hashlib,time,signal,resource,sys,itertools
import numpy as np
from fractions import Fraction as F
from scipy.sparse import csr_matrix,diags,eye
from scipy.sparse.linalg import eigsh
from core import Path,geometry,legal,flip,count,next_count,affected_faces
signal.alarm(180);start=time.monotonic();P=pathlib.Path(__file__).parent;checks=0
def req(c,m):
 global checks
 checks+=1
 if not c:raise RuntimeError(m)
faces,coeff,seed=geometry(2);bits=lambda x:sum(int(v)<<i for i,v in enumerate(x));states=[seed];index={bits(seed):0};moves=[];rows=[]
for x in states:
 row=[]
 for f in range(24):
  if legal(x,faces[f]):
   y=flip(x,f,faces);z=bits(y)
   if z not in index:index[z]=len(states);states.append(y)
   row.append(index[z]);moves.append((len(rows),index[z]))
  else:row.append(-1)
 rows.append(row)
req(len(states)==864 and len(moves)==6912,'fixed seed graph');T=np.array(rows);nf=(T>=0).sum(1);states=np.array(states);A=csr_matrix((np.ones(len(moves)),tuple(zip(*moves))),shape=(864,864));req((A-A.T).nnz==0,'symmetry');S=np.sum(abs((states-.5)@coeff.T)**2,axis=1);aff=affected_faces(faces)
for i,x in enumerate(states):
 for f,y in enumerate(T[i]):
  if y<0:continue
  req(T[y,f]==i,'reverse label');req(next_count(x,f,faces,aff,int(nf[i]))==nf[y],'allflip NF');req(np.max(abs(coeff@(states[y]-.5)-(coeff@(x-.5)+coeff[:,faces[f]]@(1.-2*x[faces[f]]))))<1e-12,'allflip complex O')
oracles=[]
for v in (F(0),F(19,20),F(1)):
 V=float(v);H=V*diags(nf.astype(float))-A;G=eye(864)-H/24;b=1+(1-V)*nf/24
 for i,d in enumerate(nf):
  d=int(d);br=1+(1-v)*d/24;selfweight=1-v*d/24
  req(selfweight>=0 and selfweight+F(d,24)==br,'rational G row')
  req(F(24-d,1)+(1-v)*d==24*selfweight,'aggregated self branch')
  req(selfweight/br+F(d,24)/br==1,'Q probability')
 req(np.max(abs(np.asarray(G.sum(1)).ravel()-b))<1e-13,'sparse row')
 h=(V-1)*nf
 for n in (2,48,192):
  m=n//2;psi=np.ones(864);raw=np.ones(864)
  for _ in range(m):psi=G@psi;psi/=np.linalg.norm(psi)
  # Independent labeled recurrence, including duplicate endpoints and aggregated self.
  for _ in range(m):
   new=(1-V*nf/24)*raw
   for f in range(24):
    good=T[:,f]>=0;new[good]+=raw[T[good,f]]/24
   raw=new/np.linalg.norm(new)
  req(np.max(abs(raw-psi))<2e-14,'labeled/sparse finite power')
  w=psi*psi;w/=sum(w);energy=float(psi@(H@psi)/(psi@psi));var=float(psi@(H@(H@psi))/(psi@psi)-energy**2)
  endpoint=G@(np.ones(864)) # actual endpoint h obtained independently from H1
  req(np.max(abs(H@np.ones(864)-h))<1e-13,'endpoint local energy')
  z=np.ones(864)
  for _ in range(n):z=G@z;z/=np.max(abs(z))
  ep=float(h@z/sum(z));req(abs(ep-energy)<2e-12,'endpoint midpoint energy identity')
  s=float(w@S);N=float(w@nf);D=4*(V*N-energy)/(8*s)
  xpsi=S*psi;R=float((coeff@(states[0]-.5)).real.sum()) # overwritten by sum six actual source quadratic forms
  O=(states-.5)@coeff.T;R=sum(float(np.vdot(O[:,j]*psi,H@(O[:,j]*psi)).real) for j in range(6))/(s*(psi@psi))-energy
  cov=float(xpsi@(H@psi)/(psi@psi)/s-energy)
  req(abs(R-D-cov)<2e-12,'Dirichlet residual identity')
  oracles.append(dict(V=V,n=n,E=energy,NF=N,S=s,D=D,R=R,correction=cov,VarH=var))
 vals,vec=eigsh(H,k=1,which='SA',tol=1e-12,v0=1+np.arange(864)/86400);res=float(np.linalg.norm(H@vec[:,0]-vals[0]*vec[:,0]));req(res<1e-9,'ground residual');req(vals[0]>=-float(nf.max())-1e-10 and vals[0]<=float((V-1)*nf.mean())+1e-10,'variational bounds')
 oracles.append(dict(V=V,ground_energy=float(vals[0]),ground_residual=res))
# Literal path replay with fixed test variates, not a stationary statistical estimate.
class Tape:
 def __init__(self,u):self.u=iter(u)
 def random(self):return next(self.u)
replays=[]
for L in (2,4):
 for V in (0.,.95,1.):
  a=Path(L,8,V);path=[a.states[0].copy() for _ in range(9)];d=1;rejected=0
  for t in range(512):
   u=((37*t+11)%509+.5)/509;v=((173*t+3)%503+.5)/503;old=path[-1] if d==1 else path[0];near=path[1] if d==1 else path[-2];M=len(a.faces);N=count(old,a.faces);adj=count(near,a.faces)
   r=u*(M+(1-V)*N);f=int(r) if r<M else -1;label=f if f>=0 and legal(old,a.faces[f]) else -1;ok=v<min(1,(M+(1-V)*N)/(M+(1-V)*adj));got=a.step(Tape([u,v]));req(got==(label,ok),'literal decision')
   if ok:path=path[1:]+[flip(old,label,a.faces)] if d==1 else [flip(old,label,a.faces)]+path[:-1]
   else:d=-d;rejected+=1
   req(a.direction==d,'direction')
   for k,j in enumerate((0,4,8)):
    req(np.array_equal(a.states[k],path[j]),'literal state');req(a.nf[k]==count(path[j],a.faces),'literal cached NF');req(np.max(abs(a.O[k]-a.coeff@(path[j].astype(float)-.5)))<1e-12,'literal cached O')
  replays.append(dict(L=L,V=V,attempts=512,rejections=rejected))
req(any(x['rejections'] for x in replays if x['V']==0),'V0 rejection coverage')
# Four-cycle census on simple tori, independent adjacency walks.
loops=[]
for L in (4,6):
 rs=list(itertools.product(range(L),repeat=3));ids={r:i for i,r in enumerate(rs)};es={};nb=[[] for _ in rs]
 for r in rs:
  for a in range(3):
   s=list(r);s[a]=(s[a]+1)%L;i,j=ids[r],ids[tuple(s)];es[tuple(sorted((i,j)))]=(r,a);nb[i].append(j);nb[j].append(i)
 C=set()
 for i in range(len(rs)):
  for j in nb[i]:
   for k in nb[j]:
    if k==i:continue
    for l in nb[k]:
     if l!=j and l!=i and i in nb[l]:C.add(tuple(sorted((tuple(sorted(e)) for e in [(i,j),(j,k),(k,l),(l,i)]))))
 winding=plaquette=0
 for c in C:
  axes={es[e][1] for e in c};sig=1
  for e in c:
   r,a=es[e];sig*=(-1)**(r[1]+r[2]) if a==0 else (-1)**r[2] if a==1 else 1
  if len(axes)==1:winding+=1;req(L==4 and sig==1,'winding sign')
  else:plaquette+=1;req(len(axes)==2 and sig==-1,'plaquette pi sign')
 req(plaquette==3*L**3 and winding==(48 if L==4 else 0),'cycle census');loops.append(dict(L=L,plaquettes=plaquette,winding=winding))
# Explicit L4 straight loop on the standard ice seed.
L=4;rs=list(itertools.product(range(L),repeat=3));links=[(r,a) for r in rs for a in range(3)];ix={z:i for i,z in enumerate(links)};x=np.array([r[a]%2 for r,a in links]);z=x.copy()
for t in range(4):z[ix[((t,0,0),0)]]^=1
def charge(x,r):
 s=0
 for a in range(3):
  v=list(r);v[a]=(v[a]-1)%4;s+=x[ix[r,a]]+x[ix[tuple(v),a]]
 return (-1)**sum(r)*(s-3)
def flux(x,a):return sum((-1)**sum(r)*(x[ix[r,a]]-.5) for r in rs if r[a]==0)
req(all(charge(x,r)==charge(z,r)==0 for r in rs),'winding Gauss');fluxdelta=[flux(z,a)-flux(x,a) for a in range(3)];req(abs(fluxdelta[0])==1 and fluxdelta[1:]==[0,0],'winding changes flux')
for bad in (-.1,1.1,float('nan')):
 try:Path(2,2,bad)
 except ValueError:pass
 else:raise RuntimeError('invalid V accepted')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(rss<384 and time.monotonic()-start<180,'resources')
out=dict(predicates=checks,oracles=oracles,literal_replays=replays,cycles=loops,winding_flux_delta=fluxdelta,seconds=time.monotonic()-start,rss_mib=rss,scope='deterministic implementation controls; no sampling or phase claim')
(P/'RESULT.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,indent=2,allow_nan=False))
