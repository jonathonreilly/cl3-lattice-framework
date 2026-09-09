"""Exact small nonorthogonal-span identities; no native model data."""
from fractions import Fraction as F
import json
def tr(A):return list(map(list,zip(*A)))
def mm(A,B):return [[sum(x*y for x,y in zip(r,c))for c in zip(*B)]for r in A]
def add(A,B):return [[x+y for x,y in zip(r,s)]for r,s in zip(A,B)]
checks=0
for a,b,c in ((F(1),F(2),F(3)),(F(0),F(1,7),F(-2,5)),(F(4),F(0),F(0))):
 K=[[0,-a,-b],[a,0,-c],[b,c,0]];S=[[F(1),F(0)],[F(0),F(2)],[F(0),F(0)]];G=mm(tr(S),S);Gi=[[F(1),0],[0,F(1,4)]];KS=mm(K,S);J=mm(tr(S),KS);D=mm(tr(KS),KS);L=add(D,mm(mm(J,Gi),J));assert L==[[b*b,2*b*c],[2*b*c,4*c*c]];checks+=1
 T=[[F(1),0],[0,F(1,2)]];N=mm(mm(tr(T),L),T);assert N==[[b*b,b*c],[b*c,c*c]];checks+=1
 # Orthogonal residual in original Euclidean ambient coordinates has row(b,c).
 assert sum(N[i][i]for i in range(2))==b*b+c*c;checks+=1
for d in(F(1,10),F(-1,4),F(1,2)):
 H=[[1,d],[d,1]];Hi=[[1/(1-d*d),-d/(1-d*d)],[-d/(1-d*d),1/(1-d*d)]];err=[[Hi[i][j]-F(i==j)for j in range(2)]for i in range(2)];assert max(sum(abs(x)for x in r)for r in err)==abs(d)/(1-abs(d));checks+=1
assert 104*105//2==5460 and 4*24*24==2304;checks+=1
print(json.dumps({'status':'PASS_EXACT_COORDINATE_FREE_IDENTITIES','checks':checks,'native_calls':0}))
