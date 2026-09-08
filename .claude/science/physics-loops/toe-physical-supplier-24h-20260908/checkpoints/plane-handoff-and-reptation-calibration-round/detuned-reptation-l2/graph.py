import os,sys,signal,time,resource,json,hashlib
from pathlib import Path
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
sys.dont_write_bytecode=True;start=time.monotonic()
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
