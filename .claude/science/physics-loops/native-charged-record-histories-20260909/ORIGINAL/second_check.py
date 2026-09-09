"""Small exact CAR conjugation and refinement-boundary controls."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
P=Path(__file__).parent;checks=0

def ck(x,s):
 global checks
 checks+=1
 if not x:raise ValueError(s)
def gam(n,v,x):return x^(1<<v),(-1)**((x&((1<<v)-1)).bit_count())
def ann(v,x,create=False):
 if bool(x>>v&1)==create:return None,0
 return x^(1<<v),(-1)**((x&((1<<v)-1)).bit_count())
def C(i,j,x):
 x,a=gam(3,j,x);x,b=gam(3,i,x);return x,-1j*a*b
for i in range(3):
 for j in range(i+1,3):
  for v in range(3):
   for x in range(8):
    y,a=C(i,j,x);y,b=ann(v,y)
    lhs={}
    if b:
     y,c=C(i,j,y);lhs[y]=a*b*c
    y,b=ann(v,x,create=v in (i,j));rhs={} if not b else {y:(-b if v in (i,j) else b)}
    ck(lhs==rhs,'particle-hole conjugation')
    shifted=x^(1<<i)^(1<<j)
    old=x.bit_count();weighted=sum((1-((shifted>>k)&1)) if k in (i,j) else ((shifted>>k)&1) for k in range(3));ck(old==weighted,'transported number')
# Exact unchanged-carrier counterexample to forgetting-outcome identity.
rho=[[F(1,2)]*2 for _ in range(2)];deph=[[rho[i][j] if i==j else F(0) for j in range(2)] for i in range(2)]
ck(rho!=deph and sum(deph[i][i] for i in range(2))==1,'dephasing boundary')
# Raw deleting-factor contraction sum equals partial trace on a Bell input.
bell=[[F(0) for _ in range(4)] for _ in range(4)]
for i in [0,3]:
 for j in [0,3]:bell[i][j]=F(1,2)
tr=[[sum(bell[2*i+b][2*j+b] for b in range(2)) for j in range(2)] for i in range(2)]
ck(tr==[[F(1,2),F(0)],[F(0),F(1,2)]],'discard diagram')
r=dict(status='PASS',checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='three-mode exact CAR and two-qubit rational controls')
(P/'SECOND_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(r)
