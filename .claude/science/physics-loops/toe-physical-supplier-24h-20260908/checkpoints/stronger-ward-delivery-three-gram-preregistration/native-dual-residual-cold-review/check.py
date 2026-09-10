from fractions import Fraction as F
from itertools import combinations
import json
labels=list(combinations(range(6),2));T=[[int(not(set(a)&set(b)))for b in labels]for a in labels];n=0
for i,a in enumerate(labels):
 for j,b in enumerate(labels):
  t2=sum(T[i][k]*T[k][j]for k in range(15));assert t2==3*int(i==j)-2*T[i][j]+3;n+=1
  assert T[i][j]==1+int(i==j)-len(set(a)&set(b));n+=1
# Noncommuting finite synthetic matrices; no native state constraints asserted.
def mv(A,x):return[sum(a*y for a,y in zip(r,x))for r in A]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def plus(x,y):return[a+b for a,b in zip(x,y)]
def minus(x,y):return[a-b for a,b in zip(x,y)]
def sc(t,x):return[t*v for v in x]
H=[[F(2),0],[0,F(3)]];C=[[0,F(-1)],[F(1),0]];CT=[[0,F(1)],[F(-1),0]];T0=[[F(1),F(2)],[F(2),F(-1)]];B=T0
x=[F(-1,2),F(-2,3)];v=[mv(C,x)[0]/2,mv(C,x)[1]/3];x0=[F(1,7),F(-1,5)];v0=[F(2,9),F(1,11)];y=[F(3,8),F(1,4)];z=[F(-1,9),F(2,7)]
e=minus(x,x0);f=minus(v,v0);r=mv(H,e);s=minus(mv(H,f),mv(C,e));a=plus(minus(minus(sc(2,mv(T0,x0)),mv(B,v0)),mv(H,y)),mv(CT,z));bb=minus(sc(-1,mv(B,x0)),mv(H,z))
W=lambda x,v:dot(x,mv(T0,x))-dot(x,mv(B,v))
R=dot(e,mv(T0,e))-dot(e,mv(B,f));assert W(x,v)-W(x0,v0)-dot(r,y)-dot(s,z)==dot(e,a)+dot(f,bb)+R;n+=1
# Exact minimizing values at endpoint and interior branches; E=1.
for ff in [F(0),F(1),F(2),F(3),F(4),F(7)]:
 L=-3-3*ff if ff<=2 else -6-3*ff*ff/4 if ff<=4 else 6-6*ff
 if ff<=2:m,root=F(-3),F(3)
 elif ff<=4:root=3*ff/2;m=(root*root-18)/3
 else:m,root=F(6),F(6)
 assert m-ff*root==L;n+=1
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','predicates':n,'native_calls':0}))
