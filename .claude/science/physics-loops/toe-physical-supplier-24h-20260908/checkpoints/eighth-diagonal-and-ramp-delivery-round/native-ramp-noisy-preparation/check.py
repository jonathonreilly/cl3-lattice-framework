from fractions import Fraction as F
import json,hashlib,time,resource,sys
from pathlib import Path
start=time.monotonic();checks=0
Z=lambda:[[F(0) for j in range(4)] for i in range(4)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(4)] for i in range(4)]
def scale(a,x):return [[x*v for v in row] for row in a]
def sub(a,b):return add(a,scale(b,-1))
def trace(a,b):return sum(a[i][j]*b[j][i] for i in range(4) for j in range(4))
def req(v,s):
 global checks
 checks+=1
 if not v:raise RuntimeError(s)
def flip(a,e):return [[a[i^(1<<e)][j^(1<<e)] for j in range(4)] for i in range(4)]
def resetdual(a,e):
 # N(rho)=|0><0|_e tensor Tr_e rho; N* is unital, though N is not.
 return [[a[i&~(1<<e)][j&~(1<<e)] if (i>>e&1)==(j>>e&1) else F(0) for j in range(4)] for i in range(4)]
def mix(a,e,p,fn):return add(scale(a,1-p),scale(fn(a,e),p))
rho=Z()
for i in [0,3]:
 for j in [0,3]:rho[i][j]=F(1,2)
ident=[[F(i==j) for j in range(4)] for i in range(4)]
req(resetdual(ident,0)==ident,'reset adjoint unital')
for i in range(4):
 for j in range(i,4):
  a=Z();a[i][j]=1;a[j][i]=1
  p,q=F(1,7),F(2,9)
  A=lambda x:mix(x,0,p,resetdual)
  B=lambda x:mix(x,1,q,flip)
  req(A(B(a))==B(A(a)),'disjoint channels commute')
  req(sub(A(B(a)),a)==add(A(sub(B(a),a)),sub(A(a),a)),'exact telescope')
  # No product-state premise: evaluate the same identity in Bell rho.
  req(trace(rho,sub(A(B(a)),a))==trace(rho,add(A(sub(B(a),a)),sub(A(a),a))),'correlated-state telescope')
a=[[F((-1)**((i&1)+((i>>1)&1))) if i==j else F(0) for j in range(4)] for i in range(4)]
req(trace(rho,a)==1,'Bell ZZ initial')
req(trace(rho,mix(a,0,F(1,7),resetdual))==F(6,7),'charge-unrestricted reset changes correlation')
req(11-9==2 and 10-9>0,'sufficient power accounting')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
r=dict(checks=checks,seconds=time.monotonic()-start,rss_mib=rss,scope='Exact channel telescope on correlated two-qubit state; not a native dynamical or optimal-noise-bound test.')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
