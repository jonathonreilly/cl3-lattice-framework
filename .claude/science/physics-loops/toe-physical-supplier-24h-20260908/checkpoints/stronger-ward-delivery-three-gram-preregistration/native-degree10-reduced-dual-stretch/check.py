from fractions import Fraction as F
from itertools import combinations
import json
nchecks=0
zero=(F(0),F(0));one=(F(1),F(0));ii=(F(0),F(1))
def ca(x,y):return x[0]+y[0],x[1]+y[1]
def cm(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def clean(p):return {m:c for m,c in p.items()if c!=zero}
def add(*ps):
 out={}
 for p in ps:
  for m,c in p.items():out[m]=ca(out.get(m,zero),c)
 return clean(out)
def scale(c,p):
 if not isinstance(c,tuple):c=(F(c),F(0))
 return clean({m:cm(c,v)for m,v in p.items()})
def mul(*ps):
 out={0:one}
 for p in ps:
  z={}
  for a,x in out.items():
   for b,y in p.items():
    sign=(-1)**sum(1 for i in range(4)for j in range(4)if a>>i&1 and b>>j&1 and i>j);v=cm((F(sign),0),cm(x,y));z[a^b]=ca(z.get(a^b,zero),v)
  out=clean(z)
 return out
I={0:one}
def ga(v):return clean({1<<i:(F(x),F(0))for i,x in enumerate(v)})
def vecadd(x,y):return[a+b for a,b in zip(x,y)]
def vs(c,x):return[c*a for a in x]
def mv(K,x):return[sum(a*b for a,b in zip(row,x))for row in K]
a=[1,0,0,0];d=[0,1,1,0];g=ga(a);dd=ga(d);B=scale(ii,mul(g,dd));J=scale((0,F(2)),dd)
for z in range(1,5):
 K=[[0,-1,-1,-z],[1,0,z,0],[1,-z,0,0],[z,0,0,0]];k=mv(K,a);v=mv(K,d)
 def deriv(p):
  ans={}
  for mask,c in p.items():
   ids=[i for i in range(4)if mask>>i&1]
   for pos,i in enumerate(ids):
    factors=[{1<<j:one}for j in ids];factors[pos]=scale(ii,ga([K[j][i]for j in range(4)]));ans=add(ans,scale(c,mul(*factors)))
  return ans
 def H(p):return add(deriv(p),mul(B,p))
 W=[0,2,-1,z];beta=[0,-2,z,1];U=z+1;alpha=-3
 up=add(scale(-U,g),scale((0,F(-1)),ga(W)));wp=add(scale(alpha,I),scale(ii,mul(g,ga(beta))))
 ju=add(scale((0,F(2*U)),mul(g,dd)),scale(2,mul(dd,ga(W))))
 hu=add(ga(mv(K,W)),scale((0,F(U)),ga(vecadd(d,vs(-1,k)))),mul(g,dd,ga(W)))
 hw=add(scale(-1,mul(ga(k),ga(beta))),scale(-1,mul(g,ga(mv(K,beta)))),scale((0,F(alpha)),mul(g,dd)),mul(dd,ga(beta)))
 hju=add(scale(-2*U,mul(ga(k),dd)),scale(-2*U,mul(g,ga(v))),scale((0,F(2)),mul(ga(v),ga(W))),scale((0,F(2)),mul(dd,ga(mv(K,W)))),scale(4*U,I),scale((0,F(4)),mul(g,ga(W))))
 for lhs,rhs in [(mul(J,up),ju),(H(up),hu),(H(wp),hw),(H(ju),hju)]:assert lhs==rhs;nchecks+=1
 u0=3;w0=z;q=2;p=add(scale(u0,I),scale(w0,B))
 r=add(scale(-1,I),H(p));sr=add(mul(J,p),scale(-q,H(mul(J,p))))
 rr=add(scale(-1+2*w0,I),scale((0,F(u0)),mul(g,dd)),scale(-w0,mul(ga(k),dd)),scale(-w0,mul(g,ga(v))))
 ss=add(scale((0,F(2*u0)),dd),scale(4*w0+4*q*u0,g),scale(2*q*u0,ga(v)),scale((0,F(-4*q*w0)),ga(vecadd(k,vs(-1,d)))))
 assert r==rr and sr==ss;nchecks+=2
labels=list(combinations(range(6),2));wP=2;wO=5;uP=3;uO=7
for A in labels:
 Cs=[C for C in labels if not(set(C)&set(A))];W=[sum((wO if C[0]//2==C[1]//2 else wP)*int(j in C)for C in Cs)for j in range(6)];U=sum(uO if C[0]//2==C[1]//2 else uP for C in Cs)
 if A[0]//2==A[1]//2:expected=[(2*wP+wO)*int(j not in A)for j in range(6)];eu=4*uP+2*uO
 else:
  axis=next(k for k in range(3)if k not in [A[0]//2,A[1]//2]);expected=[3*wP*int(j not in A)+(wO-wP)*int(j//2==axis)for j in range(6)];eu=5*uP+uO
 assert W==expected and U==eu;nchecks+=1
assert (128+19+24)*15*2==5130;nchecks+=1
print(json.dumps({'status':'PASS','predicates':nchecks,'native_values':0,'scope':'exact integer/Fraction Clifford derivation and all15 complement identities'}))
