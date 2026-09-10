from fractions import Fraction as F
from itertools import combinations
import json
n=0
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def mv(A,v):return [dot(r,v)for r in A]
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def scale(q,v):return [q*x for x in v]
def transpose(A):return list(map(list,zip(*A)))
def mm(A,B):return [[dot(r,c)for c in transpose(B)]for r in A]
labels=list(combinations(range(6),2));T=[[int(not(set(a)&set(b)))for b in labels]for a in labels];T2=mm(T,T)
for i in range(15):
 for j in range(15):assert T2[i][j]==3*int(i==j)-2*T[i][j]+3;n+=1
# Exact noncommuting H/T, skew J; no model arrays.
T=[[F(6,25),F(108,25)],[F(108,25),F(69,25)]];H=[[F(2),0],[0,F(3)]];J=[[0,F(2)],[-F(2),0]];C=[scale(-1,r)for r in J];CT=transpose(C);B=T
omega=[F(1),F(2)];x=[-omega[0]/2,-omega[1]/3];v=mv(C,x);v=[v[0]/2,v[1]/3]
W=lambda a,b:dot(a,mv(T,a))-dot(a,mv(B,b))
for k in range(-3,4):
 x0=[F(k,7),F(2,5)];v0=[F(1,3),F(k,11)];y=[F(2,9),F(k,13)];z=[F(k,5),F(1,2)]
 e=sub(x,x0);f=sub(v,v0);r=sub(scale(-1,omega),mv(H,x0));s=sub(mv(C,x0),mv(H,v0))
 a=add(sub(sub(scale(2,mv(T,x0)),mv(B,v0)),mv(H,y)),mv(CT,z));b=sub(scale(-1,mv(transpose(B),x0)),mv(H,z));corr=dot(r,y)+dot(s,z);R=dot(e,mv(T,e))-dot(e,mv(B,f))
 assert W(x,v)-W(x0,v0)-corr==dot(e,a)+dot(f,b)+R;n+=1
 G0=dot(x0,mv(mm(T,T),x0));G1=dot(v0,mv(mm(T,T),v0));G2=dot(x0,mv(mm(T,T),v0));w=sub(scale(2,mv(T,x0)),mv(B,v0))
 assert dot(w,w)==4*G0+G1-4*G2;n+=1
# Sharp endpoint and interior examples in eigenbasis diag(-3,6).
T=[[-3,0],[0,6]]
def lower(E,Fv):
 if Fv<=2*E:return -3*E*E-3*E*Fv
 if Fv<=4*E:return -6*E*E-F(3,4)*Fv*Fv
 return 6*E*E-6*E*Fv
units=[(F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5)),(F(5,13),F(12,13))]
for e in units:
 for direction in units:
  for Fv in map(F,[0,1,2,3,4,7]):
   h=scale(Fv,direction);value=dot(e,mv(T,e))-dot(e,mv(T,h));assert value>=lower(F(1),Fv);n+=1
 te=mv(T,e);h=scale(F(2,3),te);f2=dot(h,h);assert 4<=f2<=16
 assert dot(e,te)-dot(e,mv(T,h))==-6-F(3,4)*f2;n+=1
for f in map(F,[0,1,2]):
 assert dot([1,0],mv(T,[1,0]))-dot([1,0],mv(T,[-f,0]))==lower(F(1),f);n+=1
for f in map(F,[4,5,9]):assert 6-6*f==lower(F(1),f);n+=1
assert 120+210+135==465 and 465*16*15==111600;n+=1
print(json.dumps({'status':'PASS','predicates':n,'native_values':0,'scope':'exact finite graph, noncommuting dual identity, gradient identity, sharp endpoint/interior remainder'}))
