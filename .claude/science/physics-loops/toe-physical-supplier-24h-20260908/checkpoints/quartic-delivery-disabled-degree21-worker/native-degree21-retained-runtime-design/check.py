"""Exact rational 4-Majorana synthetic Fock comparison. No native inputs."""
import json
from functools import lru_cache
from fractions import Fraction as F
from math import factorial
import core as c
import assembly as A
import time,resource
START=time.monotonic()
import arithmetic as a
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
def box(q):return a.ri(q.r.numerator,q.r.denominator),a.ri(q.i.numerator,q.i.denominator)
def enclosed(z,q):return all(F(lo,a.S)<=v<=F(hi,a.S)for(lo,hi),v in zip(z,(q.r,q.i)))
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
def gram(sources,projected):
 @lru_cache(None)
 def query(n,i,j):
  op=mm(power(h,n),P)if projected else power(h,n)
  val=sum((sources[i][u].conj()*op[u][v]*sources[j][v]for u in range(4)for v in range(4)),Q())
  return box(val)
 return query

def adj(M):return [[x.conj()for x in r]for r in zip(*M)]
def poly(D,p):
 R=zeros(4)
 for i,v in enumerate(p):R=add(R,scale(power(D,i),v))
 return R
p=[F(1,2),F(-1,8),F(1,32)];oldq=F(1,4);checks=0;profiles=[];events=[];trial0=None
for index,dd in enumerate((d,e)):
 D=add(H,perturb(dd));DD=scale(mm(mm(cliff(dd),D),cliff(dd)),F(1,2));sources=[a0,dd,[sum((h[i][j]*dd[j]for j in range(4)),Q())for i in range(4)]]
 before=time.monotonic();jet,count=c.jet('inner21',A.defects('inner21'),gram(sources,False),gram(sources,True),lambda st,data:events.append((st,data)))
 for(i,j,k),z in jet.items():
  direct=mm(mm(power(D,i),power(DD,k)),power(D,j))[0][0]*F((-1)**(i+j+k),factorial(i)*factorial(j)*factorial(k));assert enclosed(z,direct);checks+=1
 JJ=scale(cliff(dd),2*I);bp=mm(JJ,poly(D,p));ss=[mm(mm(adj(bp),power(D,k)),bp)[0][0]for k in range(5)]
 new=A.new_inner(jet,p,[box(x)for x in ss[:3]],lambda st,data:events.append((st,data)))
 assert all(enclosed(z,q)for z,q in zip(new,ss));checks+=1
 trial=A.choose(new,oldq,lambda st,data:events.append((st,data)));q0,q1=trial['q'];qp=add(scale(eye(4),q0),scale(D,q1));res=mm(add(eye(4),scale(mm(D,qp),-1)),bp);vb=mm(qp,bp)
 assert enclosed(trial['eta'],mm(adj(res),res)[0][0]);assert enclosed(trial['trial_norm'],mm(adj(vb),vb)[0][0]);checks+=2
 if index==0:trial0=trial
 profiles.append({'profile':'inner21','index':index,'seconds':time.monotonic()-before,**count})
ha=[sum((h[i][j]*a0[j]for j in range(4)),Q())for i in range(4)];g=cliff(a0);Dcenter=mm(mm(g,DA),g)
cs=[d,e,[Q(),Q(1),Q(),Q(1)],[Q(),Q(),Q(1),Q(1)],[Q(),Q(),Q(1),Q(-1)]]
for index,dc in enumerate(cs):
 DC=add(H,perturb(dc));sources=[a0,d,dc,ha];before=time.monotonic();jet,count=c.jet('nominal21',A.defects('nominal21'),gram(sources,False),gram(sources,True),lambda st,data:events.append((st,data)))
 for(i,j,k,w),z in jet.items():
  op=mm(mm(mm(power(DC,i),power(Dcenter,k)),power(perturb(d),w)),power(DA,j));direct=op[0][0]*F((-1)**(i+j+k)*2**w,factorial(i)*factorial(j)*factorial(k)*factorial(w));assert enclosed(z,direct);checks+=1
 val=A.nominal(jet,p,p,trial0['q'],lambda st,data:events.append((st,data)));q0,q1=trial0['q'];Pc=poly(DC,p);Pa=poly(DA,p);qp=add(scale(eye(4),q0),scale(DA,q1));direct=add(mm(Pc,Pa),mm(mm(mm(mm(Pc,g),qp),scale(cliff(d),2*I)),Pa))[0][0]
 assert enclosed(val,direct);checks+=1
 profiles.append({'profile':'nominal21','index':index,'seconds':time.monotonic()-before,**count})
assert A.proposal([a.ZERO]*5,oldq)[0]==(oldq,F(0));checks+=1
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':checks,'exact_fock_coefficients':270,'profiles':profiles,'seconds':time.monotonic()-START,'process_ru_maxrss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'events':len(events),'native_values':0,'actual_q_fits':0},indent=2))
