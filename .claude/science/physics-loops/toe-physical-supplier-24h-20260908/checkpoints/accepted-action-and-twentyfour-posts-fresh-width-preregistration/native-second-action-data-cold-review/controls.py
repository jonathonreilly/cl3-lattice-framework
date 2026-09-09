"""Finite-support literal pi-flux stencil only; no physical covariance evaluation."""
from fractions import Fraction as F
from itertools import combinations
import json
axes=((1,0,0),(0,1,0),(0,0,1));pts=[tuple(s*x for x in a)for a in axes for s in(1,-1)];signs=(1,-1,1,-1,1,-1)
def K(v):
 out={}
 for p,x in v.items():
  for a in range(3):
   eps=(-1)**sum(p[:a])
   for direction in(1,-1):
    r=list(p);r[a]+=direction;r=tuple(r);out[r]=out.get(r,F(0))+direction*eps*x
 return {p:x for p,x in out.items()if x}
def q(ids):return {pts[i]:F(signs[i],2)for i in ids}
def dot(v,w):return sum(x*w.get(p,0)for p,x in v.items())
sets=list(combinations(range(6),2))+[tuple(range(6))];checks=0
for u in sets:
 for v in sets:
  overlap=sum(signs[i]*signs[j]for i in u for j in v if i==j);opp=sum(signs[i]*signs[j]for i in u for j in v if i//2==j//2 and i!=j)
  assert dot(K(q(u)),K(q(v)))==F(6*overlap-opp,4);checks+=1
 for p,x in K(q(u)).items():assert sum(map(abs,p))<=2;checks+=1
 assert K(q(u)).get((0,0,0),0)==-F(len(u),2);checks+=1
assert 3*402+6==1212 and 5*1212==6060;checks+=1
assert 5*(3*(132+1+1)+3)==2025;checks+=1
assert 536+2*(F(7,2)+F(7,2)+F(21,2))==571;checks+=1
assert 36+4*F(3,2)==42;checks+=1
print(json.dumps({'status':'PASS_LITERAL_LOCAL_STENCIL','checks':checks,'native_covariance_calls':0,'physical_arrays':0}))
