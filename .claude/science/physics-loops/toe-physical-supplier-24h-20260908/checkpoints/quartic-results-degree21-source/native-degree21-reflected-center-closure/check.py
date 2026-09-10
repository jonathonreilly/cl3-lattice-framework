"""Exact rational 4-Majorana synthetic Fock comparison. No native inputs."""
import json
from functools import lru_cache
from fractions import Fraction as F
from math import factorial
class Q:
 def __init__(self,r=0,i=0):self.r=F(r);self.i=F(i)
 def __add__(x,y):
  y=asq(y);return Q(x.r+y.r,x.i+y.i)
 __radd__=__add__
 def __neg__(x):return Q(-x.r,-x.i)
 def __sub__(x,y):return x+-asq(y)
 def __rsub__(x,y):return asq(y)+-x
 def __mul__(x,y):
  y=asq(y);return Q(x.r*y.r-x.i*y.i,x.r*y.i+x.i*y.r)
 __rmul__=__mul__
 def __truediv__(x,y):
  y=F(y);return Q(x.r/y,x.i/y)
 def conj(x):return Q(x.r,-x.i)
 def __eq__(x,y):
  y=asq(y);return x.r==y.r and x.i==y.i
 def __repr__(x):return str((str(x.r),str(x.i)))
def asq(x):return x if isinstance(x,Q)else Q(x)
def zeros(n):return [[Q()for _ in range(n)]for _ in range(n)]
def eye(n):return [[Q(i==j)for j in range(n)]for i in range(n)]
def add(A,B):return [[x+y for x,y in zip(r,s)]for r,s in zip(A,B)]
def scale(A,q):return [[x*q for x in r]for r in A]
def mm(A,B):return [[sum((A[i][k]*B[k][j]for k in range(len(B))),Q())for j in range(len(B[0]))]for i in range(len(A))]
def power(A,n):
 R=eye(len(A))
 for _ in range(n):R=mm(R,A)
 return R
def kron(A,B):return [[A[i][j]*B[k][l]for j in range(len(A))for l in range(len(B))]for i in range(len(A))for k in range(len(B))]
I=Q(0,1);X=[[Q(),Q(1)],[Q(1),Q()]];Y=[[Q(),-I],[I,Q()]];Z=[[Q(1),Q()],[Q(),Q(-1)]]
gamma=[kron(X,eye(2)),kron(Y,eye(2)),kron(Z,X),kron(Z,Y)]
K=zeros(4);K[0][1]=Q(1);K[1][0]=Q(-1);K[2][3]=Q(2);K[3][2]=Q(-2)
h=scale(K,I);P=scale(add(eye(4),scale(h,-1)),F(1,2))
# Different free energies require sign(h) independently blockwise.
P[2][3]=-I/2;P[3][2]=I/2
H=zeros(4)
for i in range(4):
 for j in range(4):H=add(H,scale(mm(gamma[i],gamma[j]),I*K[i][j]/4))
H=add(H,scale(eye(4),F(3,2)))
a0=[Q(1),Q(),Q(),Q()];d=[Q(),Q(1),Q(1),Q()];e=[Q(),Q(1),Q(-1),Q()]
def cliff(v):
 R=zeros(4)
 for q,g in zip(v,gamma):R=add(R,scale(g,q))
 return R
def perturb(v):return scale(mm(cliff(a0),cliff(v)),I)
DA=add(H,perturb(d));DC=add(H,perturb(e));DP=scale(mm(mm(cliff(d),DA),cliff(d)),F(1,2))

checks=0
g=cliff(a0);BA=perturb(d);Ka=[sum((K[i][j]*a0[j]for j in range(4)),Q())for i in range(4)]
Dcenter=mm(mm(g,DA),g)
formula=add(add(H,scale(BA,-1)),scale(mm(g,cliff(Ka)),I))
assert Dcenter==formula;checks+=1
assert Dcenter!=add(add(H,BA),scale(mm(g,cliff(Ka)),I));checks+=1
J=scale(cliff(d),2*I);Jstar=scale(cliff(d),-2*I)
for n in range(5):
 assert mm(mm(Jstar,power(DA,n)),J)==scale(power(DP,n),8);checks+=1
ha=[sum((h[i][j]*a0[j]for j in range(4)),Q())for i in range(4)];Fsrc=[[a0[i],d[i],e[i],ha[i]]for i in range(4)];Fs=[[x.conj()for x in row]for row in zip(*Fsrc)]
Jc=zeros(4);Jc[0][1]=-2*I;Jc[1][0]=2*I;Jc[0][3]=Q(-2);Jc[3][0]=Q(-2)
Ja=zeros(4);Ja[0][1]=2*I;Ja[1][0]=-2*I
R=eye(4);R[0][0]=Q(-1)
assert mm(mm(Fsrc,Jc),Fs)==add(mm(mm(R,add(h,mm(mm(Fsrc,Ja),Fs))),R),scale(h,-1));checks+=1
p=[F(1,2),F(-1,8),F(1,32)];q0=F(2,3);q1=F(-1,7)
poly=zeros(4)
for j,x in enumerate(p):poly=add(poly,scale(power(DA,j),x))
bvec=mm(J,poly)
# Vacuum expectation of B* D^j B, independent full matrix product.
def adj(A):return[[x.conj()for x in row]for row in zip(*A)]
s=[mm(mm(adj(bvec),power(DA,j)),bvec)[0][0]for j in range(5)]
qpoly=add(scale(eye(4),q0),scale(DA,q1));res=mm(add(eye(4),scale(mm(DA,qpoly),-1)),bvec)
expected=s[0]-2*q0*s[1]+(q0*q0-2*q1)*s[2]+2*q0*q1*s[3]+q1*q1*s[4]
assert mm(adj(res),res)[0][0]==expected;checks+=1
trial=mm(qpoly,bvec)
assert mm(adj(trial),trial)[0][0]==q0*q0*s[0]+2*q0*q1*s[1]+q1*q1*s[2];checks+=1
for i in range(3):
 for j in range(3):
  left=mm(mm(mm(mm(power(DC,i),g),qpoly),J),power(DA,j))
  right=mm(mm(mm(power(DC,i),add(scale(eye(4),q0),scale(Dcenter,q1))),scale(BA,2)),power(DA,j))
  assert left==right;checks+=1
from itertools import combinations
from collections import Counter
labels=list(combinations(range(6),2));kind=lambda a:'O'if a[0]//2==a[1]//2 else'P'
census=Counter((kind(A),kind(C),sum((i^1)in C for i in A))for A in labels for C in labels if not set(A)&set(C))
assert sorted(census.values())==[6,12,12,12,48]and sum(census.values())==90;checks+=1
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':checks,'nominal_mask_coefficients':36,'inner_mask_coefficients':45,'native_values':0},indent=2))
