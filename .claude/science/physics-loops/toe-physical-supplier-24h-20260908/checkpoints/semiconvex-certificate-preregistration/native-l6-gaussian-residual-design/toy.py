from fractions import Fraction as F
from itertools import product
import json
n=0
def ck(x,s):
 global n;n+=1
 if not x:raise RuntimeError(s)
def pf(a):
 m=len(a)
 if not m:return F(1)
 return sum((-1)**(j+1)*a[0][j]*pf([[a[x][y] for y in range(1,m) if y!=j] for x in range(1,m) if x!=j]) for j in range(1,m))
def ov(z,w):
 m=len(z);a=[[F(0) for j in range(2*m)] for i in range(2*m)]
 for i in range(m):
  for j in range(m):a[i][j]=-z[i][j];a[m+i][m+j]=w[i][j]
  a[i][m+i]=-1;a[m+i][i]=1
 return (-1)**(m*(m+1)//2)*pf(a)
def zmat(x,y):
 z=[[F(0) for _ in range(4)] for _ in range(4)];z[0][1]=x;z[1][0]=-x;z[2][3]=y;z[3][2]=-y;return z
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def solve(a,b):
 a=[list(row)+[v] for row,v in zip(a,b)];m=len(b)
 for j in range(m):
  k=next(k for k in range(j,m) if a[k][j]);a[j],a[k]=a[k],a[j];d=a[j][j];a[j]=[x/d for x in a[j]]
  for k in range(m):
   if k!=j:d=a[k][j];a[k]=[x-d*y for x,y in zip(a[k],a[j])]
 return [row[-1] for row in a]
# Pair occupations00,10,01,11, denominator1+2n_pair1+4n_pair2.
b=[F(1),F(3),F(5),F(7)];source=[F(1)]*4;target=[1/x for x in b]
ck(target[0]*target[3]!=target[1]*target[2],'inverse is non-Gaussian')
vectors=[[F(1),F(x),F(y),F(x*y)] for x,y in product((0,1),repeat=2)]
zs=[zmat(F(x),F(y)) for x,y in product((0,1),repeat=2)]
G=[[ov(z,w) for w in zs] for z in zs]
for i in range(4):
 for j in range(4):ck(G[i][j]==dot(vectors[i],vectors[j]),'Pfaffian overlap sign')
A=[[dot(u,[b[k]*v[k] for k in range(4)]) for v in vectors] for u in vectors];rhs=[dot(v,source) for v in vectors];c=solve(A,rhs)
y=[sum(c[j]*vectors[j][k] for j in range(4)) for k in range(4)]
ck(y==target,'Galerkin exact inverse');ck(sum((source[k]-b[k]*y[k])**2 for k in range(4))==0,'exact residual zero')
# A deliberately restricted one-vector dictionary gives a nonzero certified error.
c1=dot(vectors[0],source)/A[0][0];y1=[c1*x for x in vectors[0]];r2=sum((source[k]-b[k]*y1[k])**2 for k in range(4));error2=sum((target[k]-y1[k])**2 for k in range(4))
ck(r2>0,'rank-one failure preserved');ck(error2<=r2,'gap-one residual enclosure')
# Incorrect block-Pfaffian sign produces the wrong vacuum overlap.
ck(-ov(zs[0],zs[0])!=dot(vectors[0],vectors[0]),'overlap-sign adverse')
print(json.dumps({'status':'PASS','predicates':n,'rank_one_residual_squared':str(r2),'rank_one_error_squared':str(error2),'scope':'four-mode exact Gaussian dictionary/residual fixture, not a physical rank forecast'}))
