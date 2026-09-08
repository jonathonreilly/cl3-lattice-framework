from itertools import product
from pathlib import Path
import json,time,signal
signal.alarm(180);start=time.monotonic();p=97;vs=list(product(range(6),repeat=3));idx={v:i for i,v in enumerate(vs)};N=len(vs)
K=[{} for _ in vs]
for i,v in enumerate(vs):
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%6;j=idx[tuple(w)];lo,hi=sorted((i,j));z=-2*(-1)**sum(v[:a]);K[lo][hi]=z;K[hi][lo]=-z
# Sparse left multiplication; no NumPy or author matrix routine.
def km(X):return [[sum(v*X[j][c] for j,v in K[i].items())%p for c in range(N)] for i in range(N)]
def am(X):return [[-v%p for v in row] for row in km(km(X))]
I=[[int(i==j) for j in range(N)] for i in range(N)];powers=[I]
for _ in range(3):powers.append(am(powers[-1]))
# Scalar Lagrange polynomials, independent coefficient interpolation.
co=[0]*4;xs=[12,24,36,48];rs=[20,86,6,40]
for x,r in zip(xs,rs):
 q=[1];den=1
 for y in xs:
  if y==x:continue
  z=[0]*(len(q)+1)
  for i,a in enumerate(q):z[i]-=y*a;z[i+1]+=a
  q=z;den=den*(x-y)%p
 for i,a in enumerate(q):co[i]=(co[i]+a*pow(den*r,-1,p))%p
F=[[sum(co[k]*powers[k][i][j] for k in range(4))%p for j in range(N)] for i in range(N)];S=km(F)
L=[i for i,v in enumerate(vs) if v[0]<3];R=[i for i,v in enumerate(vs) if v[0]>=3];B=[[S[i][j] for j in R] for i in L];det=1
for j in range(108):
 q=next(i for i in range(j,108) if B[i][j]);B[j],B[q]=B[q],B[j];det=det*(-1 if q!=j else 1)*B[j][j]%p
 inv=pow(B[j][j],-1,p)
 for i in range(j+1,108):
  f=B[i][j]*inv%p
  for k in range(j,108):B[i][k]=(B[i][k]-f*B[j][k])%p
if det!=88:raise ValueError(det)
Path(__file__).with_name('RESULT.json').write_text(json.dumps(dict(det_mod97=det,rank=108,seconds=time.monotonic()-start,scope='independent sparse integer polynomial and determinant; no eigensolver'),indent=2)+'\n');print(det)
