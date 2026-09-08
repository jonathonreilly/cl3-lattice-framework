import os,sys,time,signal,json,hashlib
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
signal.alarm(180);start=time.monotonic();sys.dont_write_bytecode=True
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from scipy import sparse
from itertools import product,combinations
p=Path(__file__).resolve().parent
# Independent bit-graph construction; retain geometric duplicate moves.
roots=list(product(range(2),repeat=3));links=[(r,a) for r in roots for a in range(3)];lookup={z:i for i,z in enumerate(links)};faces=[]
for a,b in combinations(range(3),2):
 for r in roots:
  ra=list(r);ra[a]^=1;rb=list(r);rb[b]^=1
  faces.append([lookup[r,a],lookup[tuple(ra),b],lookup[tuple(rb),a],lookup[r,b]])
x0=sum(1<<i for i,(r,a) in enumerate(links) if r[a]);states=[x0];index={x0:0};rows=[];cols=[]
for x in states:
 for f in faces:
  z=[(x>>i)&1 for i in f]
  if z[0]==z[2] and z[1]==z[3] and z[0]!=z[1]:
   y=x^sum(1<<i for i in f)
   if y not in index:index[y]=len(states);states.append(y)
   rows.append(index[x]);cols.append(index[y])
A=sparse.coo_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(states),len(states))).tocsr();counts=np.asarray(A.sum(1)).ravel();assert len(states)==864 and len(rows)==6912 and (A-A.T).nnz==0
O=np.array([sum((-1)**sum(r)*(((x>>i)&1)-.5)*(-1)**r[0]/np.sqrt(8) for i,(r,a) in enumerate(links) if a==1) for x in states]);Q=sparse.eye(864)-sparse.diags(counts)/24+A/24
rinit=np.zeros(864);rinit[0]=1
for _ in range(480):rinit=Q@rinit
results=[]
for V in [.95,1.]:
 H=(sparse.diags(V*counts)-A).toarray();ev,U=eigh(H);psi=U[:,0];psi*=np.sign(psi.sum());G=sparse.eye(864)-sparse.csr_matrix(H)/24;g=1-ev[0]/24;R=G/g
 left=np.ones(864)
 for _ in range(144):left=R@left
 den=(left*O*O)@psi/psi.sum();w=O*psi;curve=[]
 for t in range(17):
  curve.append(float((left*O)@w/(den*psi.sum())))
  for _ in range(24):w=R@w
 amp=U.T@(O*psi);pure=np.array([sum(amp*amp*((1-ev/24)/g)**(24*t))/sum(amp*amp) for t in range(17)])
 burntargets={}
 for burn in [20,40]:
  r=rinit.copy()
  for _ in range(24*burn):r=G@r;r/=r.sum()
  # Endpoint population normalization is time-dependent away from stationarity.
  leftG=left*g**144;D=(leftG*O*O)@r/(leftG@r);v=O*r;right=r.copy();c=[]
  for t in range(17):
   c.append(float((leftG*O)@v/(leftG@right)/D))
   for _ in range(24):v=G@v;right=G@right
  burntargets[str(burn)]={'curve':c,'max_stationary_difference':float(max(abs(np.array(c)-curve))),'right_l1_error':float(sum(abs(r-psi/psi.sum())))}
 results.append({'V':V,'E0':float(ev[0]),'denominator':float(den),'finite_F_curve':curve,'pure_curve':pure.tolist(),'max_F6_bias':float(max(abs(np.array(curve)-pure))),'burn_targets':burntargets})
np.savez(p/'exact_data.npz',states=np.array(states),O=O,counts=counts,faces=np.array(faces))
(p/'exact_result.json').write_text(json.dumps({'states':864,'arcs':6912,'rows':results,'seconds':time.monotonic()-start},indent=2,allow_nan=False)+'\n')
