from fractions import Fraction as F
import json,time
start=time.monotonic();n=0

def ck(x):
 global n
 if not x:raise ValueError('independent exact control')
 n+=1

def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(2)),F(0)) for j in range(2)] for i in range(2)]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def nb(a):return max([sum(map(abs,r)) for r in a]+[sum(abs(a[i][j]) for i in range(2)) for j in range(2)])
def inverse(a):
 d=det(a);return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def log_interval(x):
 k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 def series(z):
  lo=2*sum((z**(2*j+1)/(2*j+1) for j in range(40)),F(0));return lo,lo+2*z**81/(81*(1-z*z))
 a,b=series((x-1)/(x+1));l,u=series(F(1,3))
 return (a+k*l,b+k*u) if k>=0 else (a+k*u,b+k*l)
I=[[F(1),F(0)],[F(0),F(1)]]
M=[[F(3,4),F(-1,8)],[F(1,16),F(7,8)]];E=sub(I,M);g=F(1,2)
ck(nb(E)<=1-g)
P=I;S=[[F(0)]*2 for _ in range(2)]
for _ in range(7):S=add(S,P);P=mm(P,E)
R=sub(I,mm(M,S));error=sub(inverse(M),S)
ck(error==mm(inverse(M),R))
ck(sum(x*x for row in error for x in row)<= (nb(R)/g)**2)
ck(nb(R)>0) # falsely declaring the candidate residual zero is discriminated
B=add(M,[[F(1,128),F(0)],[F(0),F(0)]])
# Deliberately force an odd row permutation in exact LU.
PB=[B[1][:],B[0][:]];L=[[F(1),F(0)],[PB[1][0]/PB[0][0],F(1)]];U=[PB[0][:],[F(0),PB[1][1]-L[1][0]*PB[0][1]]]
ck(mm(L,U)==PB);ck(-U[0][0]*U[1][1]==det(B)>0);ck(U[0][0]*U[1][1]<0)
eta=nb(sub(B,M));ck(eta<g/2)
lb,ub=log_interval(det(B));lm,um=log_interval(det(M));bound=4*eta/g
ck(max(abs(lb-um),abs(ub-lm))<bound)
for x in [F(1,128),F(5,64),F(3,2),F(8),F(65,32)]:
 l,u=log_interval(x);a,b=log_interval(1/x)
 ck(l<=u and a<=b and l+a<=0<=u+b)
print(json.dumps({'status':'PASS','predicates':n,'seconds':time.monotonic()-start,'scope':'independent exact nonnormal inverse residual, forced odd-permutation LU and signed-exponent scalar logs; no native computation'},indent=2))
