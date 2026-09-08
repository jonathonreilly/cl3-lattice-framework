"""Exact modular Schmidt-rank certificate; characteristic-zero spectrum imported."""
from itertools import product
import time,json
start=time.monotonic();checks=0
def ck(c,label):
 global checks
 checks+=1
 if not c:raise RuntimeError(label)
p=97;sqrt2=13;sqrt3=10
ck(p>1 and all(p%d for d in range(2,10)),'prime')
ck(sqrt2*sqrt2%p==2,'sqrt2 image')
ck(sqrt3*sqrt3%p==3,'sqrt3 image')
vs=list(product(range(6),repeat=3));idx={v:i for i,v in enumerate(vs)};N=len(vs)
ck(N==216,'site coverage')
K=[{} for _ in vs]
for i,v in enumerate(vs):
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%6;j=idx[tuple(w)];lo,hi=sorted((i,j));z=-2*(-1)**sum(v[:a]);K[lo][hi]=z;K[hi][lo]=-z
for i,row in enumerate(K):
 ck(len(row)==6,'six neighbors')
 for j,z in row.items():ck(abs(z)==2 and K[j].get(i)==-z,'canonical skew edge')
def km(X):return [[sum(v*X[j][c] for j,v in K[i].items())%p for c in range(N)] for i in range(N)]
def am(X):return [[-v%p for v in row] for row in km(km(X))]
I=[[int(i==j) for j in range(N)] for i in range(N)];powers=[I]
for _ in range(4):powers.append(am(powers[-1]))
xs=[12,24,36,48];rs=[2*sqrt3%p,2*sqrt2*sqrt3%p,6,4*sqrt3%p];co=[0]*4
for x,r in zip(xs,rs):
 ck(r!=0 and r*r%p==x%p,'inverse root domain')
 q=[1];den=1
 for y in xs:
  if y==x:continue
  z=[0]*(len(q)+1)
  for i,a in enumerate(q):z[i]-=y*a;z[i+1]+=a
  q=z;den=den*(x-y)%p
 ck(den!=0,'interpolation denominator')
 for i,a in enumerate(q):co[i]=(co[i]+a*pow(den*r,-1,p))%p
for x,r in zip(xs,rs):ck(sum(a*pow(x,i,p) for i,a in enumerate(co))%p==pow(r,-1,p),'interpolation value')
# Modular consistency only: the exact characteristic-zero spectrum is an
# explicit upstream premise, not deduced from this finite-field identity.
poly=[1]
for x in xs:
 q=[0]*(len(poly)+1)
 for i,a in enumerate(poly):q[i]-=x*a;q[i+1]+=a
 poly=q
for i in range(N):
 for j in range(N):ck(sum(poly[k]*powers[k][i][j] for k in range(5))%p==0,'modular annihilating polynomial')
F=[[sum(co[k]*powers[k][i][j] for k in range(4))%p for j in range(N)] for i in range(N)];S=km(F)
left=[i for i,v in enumerate(vs) if v[0]<3];right=[i for i,v in enumerate(vs) if v[0]>=3]
ck(len(left)==len(right)==108,'balanced coordinate cut')
B=[[S[i][j] for j in right] for i in left];det=1;pivots=[]
for j in range(108):
 pivot=next((i for i in range(j,108) if B[i][j]),None)
 ck(pivot is not None,'full Schmidt cross rank')
 B[j],B[pivot]=B[pivot],B[j];value=B[j][j];pivots.append(value);det=det*(-1 if pivot!=j else 1)*value%p
 inv=pow(value,-1,p)
 for i in range(j+1,108):
  f=B[i][j]*inv%p
  for k in range(j,108):B[i][k]=(B[i][k]-f*B[j][k])%p
ck(len(pivots)==108,'rank count')
ck(det==88 and det!=0,'nonzero algebraic determinant witness')
out={'checks':checks,'prime':p,'sqrt2_image':sqrt2,'sqrt3_image':sqrt3,'site_count':N,'half_size':108,'rank':len(pivots),'det_mod_prime':det,'pivot_values':pivots,'interpolation_coefficients_mod_prime':co,'seconds':time.monotonic()-start,'scope':'Exact finite-field nonzero determinant certificate, assuming linked characteristic-zero canonical spectrum; no numerical flux-gap value.'}
if __name__=='__main__':print(json.dumps(out,indent=2))
