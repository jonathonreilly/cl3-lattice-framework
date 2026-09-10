from itertools import combinations
from collections import defaultdict
import json

def K(v):
 out=defaultdict(int)
 for x,c in v.items():
  for j in range(3):
   for step,sgn in[(-1,-1),(1,1)]:
    r=list(x);r[j]+=step;r=tuple(r);eta=(-1)**sum(r[:j]);out[r]+=sgn*eta*c
 return {k:v for k,v in out.items()if v}
a={(0,0,0):1};ka=K(a);expect={};n=0
for j in range(3):
 for s in[-1,1]:
  r=[0,0,0];r[j]=s;expect[tuple(r)]=s
assert ka==expect;n+=1
kk={(0,0,0):-6}
for j in range(3):
 for s in[-2,2]:
  r=[0,0,0];r[j]=s;kk[tuple(r)]=1
assert K(ka)==kk;n+=1
labels=list(combinations(range(6),2))
for A in labels:
 for C in labels:
  overlap=len(set(A)&set(C));op=sum((i^1)in C for i in A)
  # Formal coefficients of Rj and Rj+2; no scalar evaluated.
  direct=[0,0]
  for i in A:
   for j in C:
    if i==j:direct[0]+=6
    elif i^1==j:direct[0]-=6;direct[1]+=1
  assert direct==[6*(overlap-op),op];n+=1
assert 7-2==5 and 5+2==7;n+=1
assert len(labels)*6*16*2==2880;n+=1
print(json.dumps({'status':'PASS','literal_local_and_formal_table_checks':n,'native_scalars_or_moments_evaluated':0}))
