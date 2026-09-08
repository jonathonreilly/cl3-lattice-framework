from fractions import Fraction as F
from itertools import product
import json,time,signal,resource
from pathlib import Path
signal.alarm(180);start=time.monotonic();checks=0
def ck(c):
 global checks;checks+=1
 if not c:raise ValueError(checks)
vs=list(product(range(4),repeat=3));ids={v:i for i,v in enumerate(vs)};edges=[]
for v in vs:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%4;edges.append((ids[v],ids[tuple(w)],(-1)**sum(v[:a])))
black=[i for i,v in enumerate(vs) if sum(v)%2==0]
def gram(mask):
 K=[[0]*64 for _ in vs]
 for e,(a,b,s) in enumerate(edges):
  i,j=sorted((a,b));K[i][j]=-2*s*(-1 if mask>>e&1 else 1);K[j][i]=-K[i][j]
 return [[F(-sum(K[i][k]*K[k][j] for k in range(64)),4) for j in black] for i in black]
def trinv(M):
 n=len(M);L=[[F(i==j) for j in range(n)] for i in range(n)];D=[]
 for j in range(n):
  D.append(M[j][j]-sum(L[j][k]**2*D[k] for k in range(j)));ck(D[j]>0)
  for i in range(j+1,n):L[i][j]=(M[i][j]-sum(L[i][k]*L[j][k]*D[k] for k in range(j)))/D[j]
 V=[[F(i==j) for j in range(n)] for i in range(n)]
 for i in range(n):
  for j in range(i):V[i][j]=-sum(L[i][k]*V[k][j] for k in range(j,i))
 ck(all(sum(L[i][k]*V[k][j] for k in range(n))==int(i==j) for i in range(n) for j in range(n)))
 return sum(sum(x*x for x in row)/d for row,d in zip(V,D))
def cert(mask):
 A=gram(mask);c=F(5,2);ell=F(2449489742783178,10**15);ck(ell**2<6)
 ck(sum(A[i][i] for i in range(32))==192)
 tr=trinv([[x+c*c*(i==j) for j,x in enumerate(row)] for i,row in enumerate(A)])
 return 32*ell-((192+32*c*c)/(4*c)+c*(32-c*c*tr))
raw=json.loads((Path(__file__).parents[1]/'native-sixth-spectator-gap-certificates/RESULT.json').read_text());first=raw['rows'][0];mask=int(first['mask_hex'],16)
ck(cert(mask)==F(first['gap_lower']))
other=cert((1<<0)|(1<<2));ck(other>0)
star=sum(1<<e for e,(i,j,s) in enumerate(edges) if i==0 or j==0);ck(cert(star)<0)
A=gram(0);ck(A==[[F(6*(i==j)) for j in range(32)] for i in range(32)])
for c in (F(1,3),F(5,2),F(7)):
 for z in (F(0),F(1,7),F(2),F(11)):
  x=z*z;y1=(c+x/c)/2;y2=(y1+x/y1)/2;formula=(x+c*c)/(4*c)+c*(1-c*c/(x+c*c))
  ck(y2==formula);ck(y2-z==(y1-z)**2/(2*y1));ck(y2>=z)
print(json.dumps(dict(checks=checks,distinct_mask_lower=str(other),seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576),indent=2))
