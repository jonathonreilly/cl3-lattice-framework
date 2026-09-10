"""Fixed-grid outward input adapter and bounded exact integer residual."""
from fractions import Fraction as F
from math import isqrt
Q=1<<256;CAP=32768
class Limit(ValueError):pass
def ck(x):
 if type(x)is not int or x.bit_length()>CAP:raise Limit('integer bit cap')
 return x
def prod(a,b):return ck(a*b)
def plus(a,b):return ck(a+b)
def frac(x):
 if type(x)is not F:raise Limit('Fraction required')
 ck(x.numerator);ck(x.denominator);return x

def floorq(x):frac(x);return ck(prod(x.numerator,Q)//x.denominator)
def ceilq(x):return ck(-floorq(-x))
def exactq(x):
 a=floorq(x)
 if F(a,Q)!=x:raise Limit('candidate/embedding not exact grid dyadic')
 return a

def mat(A,B):
 out=[]
 for row in A:
  rr=[]
  for col in zip(*B):
   z=0
   for a,b in zip(row,col):z=plus(z,prod(a,b))
   rr.append(z)
  out.append(rr)
 return out

def norm(A,den):
 z=0
 for row in A:
  for x in row:z=plus(z,prod(x,x))
 z=prod(z,prod(Q,Q));dd=prod(den,den);r=isqrt(z//dd)
 if prod(prod(r,r),dd)<z:r=plus(r,1)
 return F(ck(r),Q)

def verify(G0,radii,T,E,persist=lambda stage,data:None):
 p=len(T)
 if not 0<p<=48 or len(G0)!=p or len(radii)!=p or any(len(r)!=p for A in (G0,radii,T,E)for r in A) or not 0<len(E)<=96:raise Limit('shape')
 for A in(G0,radii,T,E):
  for row in A:
   for x in row:frac(x)
 if any(G0[i][j]!=G0[j][i] or radii[i][j]!=radii[j][i] or radii[i][j]<0 for i in range(p)for j in range(p)):raise Limit('symmetric intervals')
 if any(T[i][i]<=0 or any(T[i][j]for j in range(i))for i in range(p)):raise Limit('positive upper')
 C=[];R=[]
 for i in range(p):
  cr=[];rr=[]
  for j in range(p):
   lo=floorq(G0[i][j]-radii[i][j]);hi=ceilq(G0[i][j]+radii[i][j]);c=ck(plus(lo,hi)//2);cr.append(c);rr.append(max(hi-c,c-lo))
  C.append(cr);R.append(rr)
 Ti=[[exactq(x)for x in row]for row in T];Ei=[[exactq(x)for x in row]for row in E]
 persist('dyadic_inputs',{'Gcenter':C,'radius':R,'T':Ti,'E':Ei,'scale':Q})
 H=mat(list(map(list,zip(*Ti))),mat(C,Ti));den=Q**3;persist('H_integer',{'H':H,'denominator':den})
 D=[[ck(H[i][j]-(den if i==j else 0))for j in range(p)]for i in range(p)]
 eta=norm(R,Q);tn=norm(Ti,Q);e=norm(D,den)+tn*tn*eta
 for x in (eta,tn,e):frac(x)
 persist('error',{'e':e,'eta':eta,'Tnorm_upper':tn})
 if e>=1:return {'status':'INDETERMINATE_RESIDUAL','e':e}
 ET=mat(Ei,Ti);B=e/(1-e)**2;bc=norm(ET,Q*Q)*B
 for x in (B,bc):frac(x)
 center=[[F(x,Q*Q)for x in row]for row in ET];persist('coefficient_box',{'center':center,'radius':bc})
 l1=max(sum((abs(center[i][j])+bc for i in range(len(E))),F(0))for j in range(p));frac(l1)
 return {'status':'CERTIFIED_ENCLOSURE','center':center,'radius':bc,'width_pass':2*bc<=F(1,2**39),'l1_pass':l1<=2**40,'e':e}
