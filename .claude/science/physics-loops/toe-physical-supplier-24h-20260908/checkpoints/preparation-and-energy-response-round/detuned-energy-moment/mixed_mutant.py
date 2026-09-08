import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
from itertools import product,combinations
from pathlib import Path
import json,hashlib,time,resource
start=time.monotonic();checks={}
def ck(k,p):
 if not bool(p):raise AssertionError(k)
 checks[k]=True
L=2;vol=8;sites=list(product(range(2),repeat=3));links=[(r,a) for r in sites for a in range(3)];idx={x:j for j,x in enumerate(links)}
faces=[];planes=[]
for a,b in combinations(range(3),2):
 for r in sites:
  ra=list(r);ra[a]^=1;rb=list(r);rb[b]^=1
  faces.append([idx[r,a],idx[tuple(ra),b],idx[tuple(rb),a],idx[r,b]]);planes.append((a,b))
x0=sum(1<<j for j,(r,a) in enumerate(links) if r[a]);states=[x0];lookup={x0:0};rr=[];cc=[];ff=[]
for x in states:
 for k,f in enumerate(faces):
  z=[(x>>j)&1 for j in f]
  if z[0]==z[2] and z[1]==z[3] and z[0]!=z[1]:
   y=x^sum(1<<j for j in f)
   if y not in lookup:lookup[y]=len(states);states.append(y)
   rr.append(lookup[x]);cc.append(lookup[y]);ff.append(k)
A=sparse.coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(len(states),)*2).tocsr();nf=np.asarray(A.sum(1)).ravel();N=sparse.diags(nf)
ck('graph864_6912',len(states)==864 and len(rr)==6912);ck('symmetric',(A-A.T).nnz==0)
modes=[(a,b) for a in range(3) for b in range(3) if a!=b]
O=np.array([[sum((-1)**(sum(r)+r[a])*(((x>>j)&1)-.5)/np.sqrt(vol) for j,(r,d) in enumerate(links) if d==b) for x in states] for a,b in modes])
values={};psis={}
Vs=sorted({round(.95+k*h,6) for h in [.02,.01,.005] for k in [-2,-1,0,1,2]})
for V in Vs:
 H=V*N-A;e,u=eigsh(H,k=1,which='SA',tol=1e-13,v0=np.ones(864));psi=u[:,0];psi*=np.sign(psi.sum());values[V]=float(e[0]);psis[V]=psi
 ck('eigenres_'+str(V),np.linalg.norm(H@psi-e[0]*psi)<1e-10)
V=.95;E=values[V];psi=psis[V];H=V*N-A
pureN=float(psi@nf/psi.sum());mixedN=float(psi@nf/psi.sum());kin=float(psi@(A@psi));S=O**2@(psi*psi);means=O@(psi*psi)
ck('zero_means',max(abs(means))<1e-10)
ck('mixed_energy_identity',abs((V-1)*mixedN-E)<1e-10)
ck('pure_FH_algebra',abs(V*pureN-E-kin)<1e-10)
num=np.array([(o*psi)@((H-E*sparse.eye(864))@(o*psi)) for o in O]);pooled=float(sum(num)/sum(S))
ck('sixmode_sumrule',abs(sum(num)-4*kin/vol)<1e-10)
ck('wrong_orientation_factor_detected',abs(pooled-4*kin/(2*vol*sum(S)))>.1)
ck('mixed_shortcut_detected',abs((V*mixedN-E)-kin)>1e-4)
R=(sparse.eye(864)-H/24)/(1-E/24);left=np.ones(864)
for _ in range(144):left=R@left
SF=(O**2@(left*psi))/(left@psi)
rows=[]
for h in [.02,.01,.005]:
 f=lambda k:values[round(V+k*h,6)]
 d2=(f(1)-f(-1))/(2*h);d4=(f(-2)-8*f(-1)+8*f(1)-f(2))/(12*h)
 lo=(f(1)-f(0))/h;hi=(f(0)-f(-1))/h
 ck('concavity_bracket_'+str(h),lo-1e-9<=pureN<=hi+1e-9)
 rows.append({'h':h,'derivative2':d2,'derivative4':d4,'derivative2_error':d2-pureN,'derivative4_error':d4-pureN,'kinetic2':V*d2-E,'moment2':4*(V*d2-E)/(vol*sum(S)),'moment4':4*(V*d4-E)/(vol*sum(S)),'moment_bracket':[4*(V*lo-E)/(vol*sum(S)),4*(V*hi-E)/(vol*sum(S))]})
r={'checks':checks,'count':len(checks),'E0':E,'pure_Nf':pureN,'mixed_Nf':mixedN,'pure_A':kin,'S_six':S.tolist(),'S_F6_six':SF.tolist(),'F6_Smax_bias':float(max(abs(SF-S))),'pooled_moment':pooled,'energies':values,'stencils':rows,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_sec':time.monotonic()-start,'rss_native':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
print(json.dumps(r,indent=2,allow_nan=False))
