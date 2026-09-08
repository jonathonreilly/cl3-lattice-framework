from fractions import Fraction as F
from pathlib import Path
import json
# Gaussian rational complex numbers represented with Python complex integers here;
# all coefficients integral, so every computed value is exact in binary64.
def pf(A):
 if not A:return 1
 return sum((-1)**(j+1)*A[0][j]*pf([[A[a][b] for b in range(1,len(A)) if b!=j] for a in range(1,len(A)) if a!=j]) for j in range(1,len(A)))
def gamma(j,x):return x^(1<<(j//2)),(-1)**((x&((1<<(j//2))-1)).bit_count())*(1 if j%2==0 else 1j*(-1)**((x>>(j//2))&1))
def pair(a,b,v):
 out=[0j]*4
 for x,z in enumerate(v):
  y,s=gamma(b,x);y,t=gamma(a,y);out[y]+=z*s*t
 return out
checks=0
for pairs in [[(0,1),(1,2),(2,3)],[(0,2),(0,3),(1,3)],[(0,1),(0,1),(0,1)]]:
 for insertion in (False,True):
  ops=([(0,3)]+pairs) if insertion else pairs;weights=([1]+[2,-1,3]) if insertion else [2,-1,3]
  v=[1,0,0,0]
  for k in reversed(range(len(ops))):
   a,b=ops[k];z=pair(a,b,v);v=[weights[k]*z[i]+(0 if insertion and k==0 else v[i]) for i in range(4)]
  ids=[j for ab in ops for j in ab];D=[w if i%2==0 else 1 for w in weights for i in (0,1)];A=[[0j]*len(ids) for _ in ids]
  for i in range(len(ids)):
   for j in range(i+1,len(ids)):
    z=pair(ids[i],ids[j],[1,0,0,0])[0];A[i][j]=D[i]*D[j]*z
    if j==i+1 and i%2==0 and not(insertion and i==0):A[i][j]+=1
    A[j][i]=-A[i][j]
  if pf(A)!=v[0]:raise ValueError('Pfaffian sign')
  checks+=1
Path(__file__).with_name('PFAFFIAN_RESULT.json').write_text(json.dumps({'checks':checks,'scope':'exact integer Gaussian rational CAR/Wick fixture, not physical time integration'},indent=2)+'\n')
