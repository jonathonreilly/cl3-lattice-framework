from pathlib import Path
from itertools import product
import json,time,signal,resource
signal.alarm(180);start=time.monotonic();checks=0
p=Path('/private/tmp/toe-24h-probes-20260908/native-3d-chessboard-spectral-design');data=json.loads((p/'INPUTS.json').read_text());V=[tuple(x) for x in data['site_order']];C=list(product(range(2),repeat=3));ci={x:i for i,x in enumerate(C)}
def need(z,s):
 global checks
 checks+=1
 if not z:raise ValueError(s)
def add(A,B):
 D=A.copy()
 for k,v in B.items():D[k]=D.get(k,0)+v
 return {k:v for k,v in D.items() if v}
def scale(A,z):return {k:v*z for k,v in A.items() if v*z}
def mul(A,B):
 rows={}
 for (i,j),v in B.items():rows.setdefault(i,[]).append((j,v))
 D={}
 for (i,j),v in A.items():
  for k,w in rows.get(j,[]):D[i,k]=D.get((i,k),0)+v*w
 return {k:v for k,v in D.items() if v}
def kron(A,B,n):return {(i*n+k,j*n+l):v*w for (i,j),v in A.items() for (k,l),w in B.items()}
def I(n):return {(i,i):1 for i in range(n)}
def tr(A):return sum(v for (i,j),v in A.items() if i==j)
X={(0,1):1,(1,0):1};Y={(0,1):-1j,(1,0):1j};Z={(0,0):1,(1,1):-1};paulis=(X,Y,Z)
permutation=[]
for r in V:
 b=tuple(x//2 for x in r);y=tuple((0,1,1,0)[x] for x in r);permutation.append(ci[y]*8+ci[b])
mutants=0
for row in data['rows']:
 signs={ (tuple(v),a):s for (v,a),s in zip(data['cube_edge_order'],row['cube_signs'])};cube={};AA=[]
 for a in range(3):
  A={}
  for y in C:
   z=list(y);z[a]^=1;v=list(y);v[a]=0;s=signs[tuple(v),a];cube[ci[y],ci[tuple(z)]]=s
   A[ci[y],ci[tuple(z)]]=s*(-1j if y[a]==0 else 1j)
  AA.append(A)
 base=add(mul(cube,cube),scale(I(8),3))
 for ks in product((0,1),repeat=3):
  h={(permutation[i],permutation[j]):s*(-1)**sum(k*d for k,d in zip(ks,e)) for i,j,e,s in row['terms']};h2=mul(h,h)
  pred=kron(base,I(8),8);D=kron(base,I(2),2)
  for a,k in enumerate(ks):
   gamma={}
   for b in C:
    c=list(b);c[a]^=1;gamma[ci[b],ci[tuple(c)]]=(-1)**sum(b[:a])*(-2*k)*(-1j if b[a]==0 else 1j)
   pred=add(pred,kron(AA[a],gamma,8));D=add(D,scale(kron(AA[a],paulis[a],2),2*k))
  need(h2==pred,'literal square Clifford identity')
  need(all(v==D.get((j,i),0).conjugate() if isinstance(D.get((j,i),0),complex) else v==D.get((j,i),0) for (i,j),v in D.items()),'Hermitian reduced block')
  P=h2;Q=D
  for power in (1,2,3):
   need(tr(P)==4*tr(Q),'fourfold exact trace moment')
   P=mul(P,h2);Q=mul(Q,D)
  if any(ks):
   bad=kron(base,I(8),8)
   if h2!=bad:mutants+=1
need(mutants>0,'omitted cross term discriminated')
print(json.dumps(dict(checks=checks,backgrounds=32,momenta_per_background=8,omitted_cross_term_discriminations=mutants,seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,scope='exact Gaussian-integer matrix identities and trace moments; no eigensolver'),indent=2))
