"""Independent exact four-Majorana Clifford/Wick derivative check; no physics."""
from fractions import Fraction as F
import json
n=4

def plus(a,b):
 z=dict(a)
 for k,x in b.items():z[k]=z.get(k,F(0))+x
 return {k:x for k,x in z.items() if x}
def scale(a,c):return {k:x*c for k,x in a.items() if x*c}
def mul(a,b):
 z={}
 for i,x in a.items():
  for j,y in b.items():
   sign=(-1)**sum((i>>(k+1)).bit_count() for k in range(n) if j>>k&1)
   z[i^j]=z.get(i^j,F(0))+sign*x*y
 return {k:x for k,x in z.items() if x}
g=[{1<<i:F(1)} for i in range(n)];I={0:F(1)}
def partial(i,a):
 z={}
 for mask,x in a.items():
  one={mask:x};z=plus(z,scale(plus(mul(g[i],one),scale(mul(one,g[i]),-(-1)**mask.bit_count())),F(1,2)))
 return z
U=plus(scale(I,F(3,5)),scale(mul(g[0],g[2]),F(4,5)));Ud=plus(scale(I,F(3,5)),scale(mul(g[0],g[2]),F(-4,5)))
count=0
def req(x):
 global count
 if not x:raise ValueError('control')
 count+=1
req(mul(U,Ud)==I)
R=[[mul(Ud,mul(g[i],U)).get(1<<j,F(0)) for j in range(n)] for i in range(n)]
D=[[R[i][j]-int(i==j) for j in range(n)] for i in range(n)]
DG=[{1<<j:D[i][j] for j in range(n) if D[i][j]} for i in range(n)]
for i in range(n):
 for j in range(n):req(partial(j,partial(i,U))==scale(mul(U,plus(mul(DG[j],DG[i]),scale(I,2*D[i][j]))),F(1,4)))
# Purely imaginary contractions C=iA, with real skew A. Endpoints are valid.
A0=[[F(0)]*n for _ in range(n)];A1=[[F(0)]*n for _ in range(n)]
A0[0][1]=F(1,2);A0[1][0]=F(-1,2);A0[2][3]=F(-1,3);A0[3][2]=F(1,3)
A1[0][1]=F(-1,4);A1[1][0]=F(1,4);A1[2][3]=F(1,5);A1[3][2]=F(-1,5)
A1=[[sum(R[i][a]*A1[a][b]*R[j][b] for a in range(n) for b in range(n)) for j in range(n)] for i in range(n)]
dA=[[A1[i][j]-A0[i][j] for j in range(n)] for i in range(n)];s=F(1,3);A=[[A0[i][j]+s*dA[i][j] for j in range(n)] for i in range(n)]
def pf(ids):
 if not ids:return F(1),F(0)
 v=d=F(0)
 for k in range(1,len(ids)):
  i,j=ids[0],ids[k];x,y=pf(ids[1:k]+ids[k+1:]);sgn=(-1)**(k+1)
  v+=sgn*A[i][j]*x;d+=sgn*(dA[i][j]*x+A[i][j]*y)
 return v,d
def expectation(op,derivative=False):
 out=[F(0),F(0)]
 for mask,c in op.items():
  ids=[i for i in range(n) if mask>>i&1]
  if len(ids)%2:continue
  x=pf(ids)[int(derivative)]*c;power=(len(ids)//2)%4
  out[power%2]+=x*(-1 if power>=2 else 1)
 return tuple(out)
ops=[{mask:F(1)} for mask in range(16)]+[U,mul(U,mul(g[1],g[3])),mul(U,mul(plus(g[0],scale(g[2],F(2))),plus(g[1],g[2])))]
for op in ops:
 rhs=[F(0),F(0)]
 for i in range(n):
  for j in range(i+1,n):
   re,im=expectation(partial(j,partial(i,op)));rhs[0]-=dA[i][j]*im;rhs[1]+=dA[i][j]*re
 req(tuple(rhs)==expectation(op,True))
print(json.dumps({'status':'PASS','exact_predicates':count,'physical_runs':0,'scope':'Clifford second derivative and Wick covariance interpolation'},indent=2))
