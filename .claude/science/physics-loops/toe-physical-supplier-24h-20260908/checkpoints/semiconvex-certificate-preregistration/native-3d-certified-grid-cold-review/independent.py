"""Exact Fraction-pair certificate replay, no producer or NumPy imports."""
from fractions import Fraction as F
from itertools import product
import math
ZERO=(F(0),F(0))
def ck(x,msg):
 if not x:raise ValueError(msg)
def z(x):
 if isinstance(x,tuple):return x
 if isinstance(x,complex):return F(x.real),F(x.imag)
 return F(x),F(0)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def neg(a):return -a[0],-a[1]
def conj(a):return a[0],-a[1]
def sub(a,b):return add(a,neg(b))
def sq(a):return a[0]*a[0]+a[1]*a[1]
def summ(xs):
 s=ZERO
 for a in xs:s=add(s,a)
 return s
def matrix(cube,grid):
 vs=list(product((0,1),repeat=3));es=[(v,a) for v in vs for a in range(3) if v[a]==0];sign=dict(zip(es,cube['cube_signs']));C=[[0]*8 for _ in vs]
 for i,v in enumerate(vs):
  for a in range(3):
   w=list(v);w[a]^=1;base=list(v);base[a]=0;C[i][vs.index(tuple(w))]=sign[tuple(base),a]
 A=[[ZERO for _ in range(16)] for _ in range(16)]
 for i in range(8):
  for j in range(8):
   b=sum(C[i][k]*C[k][j] for k in range(8))+3*(i==j)
   for s in (0,1):A[2*i+s][2*j+s]=z(b)
 radius=F(0)
 for a,g in enumerate(grid):
  q=F(float.fromhex(g['q_hex']));lo=F(g['lower_numerator'],g['denominator']);hi=F(g['upper_numerator'],g['denominator']);ck(0<=lo<=hi<=2,'q interval');radius+=max(abs(q-lo),abs(q-hi))
  for i,v in enumerate(vs):
   w=list(v);w[a]^=1;j=vs.index(tuple(w));base=list(v);base[a]=0;sg=sign[tuple(base),a];ay=(F(0),F(sg*(1 if v[a] else -1)))
   for s in (0,1):
    if a==0:t=1-s;pa=z(1)
    elif a==1:t=1-s;pa=(F(0),F(1 if s else -1))
    else:t=s;pa=z(1 if s==0 else -1)
    A[2*i+s][2*j+t]=add(A[2*i+s][2*j+t],mul(z(q),mul(ay,pa)))
 return A,radius

def verify(A,Q,lam,radius,cert):
 n=len(A);ck(n==16 and len(Q)==n and len(lam)==n and all(len(row)==n for row in A+Q),'shape')
 A=[[z(x) for x in row] for row in A];Q=[[z(x) for x in row] for row in Q];lam=list(map(F,lam));rs=gs=F(0)
 for i in range(n):
  for j in range(n):
   ck(A[i][j]==conj(A[j][i]),'Hermitian')
   R=sub(summ(mul(A[i][k],Q[k][j]) for k in range(n)),mul(Q[i][j],z(lam[j])))
   G=sub(summ(mul(conj(Q[k][i]),Q[k][j]) for k in range(n)),z(int(i==j)))
   rs+=sq(R);gs+=sq(G)
 r=F(cert['residual']);eta=F(cert['eta']);step=F(1,1<<80)
 ck(r>=0 and r*r>=rs and (r==0 or (r-step)**2<rs or r<step),'residual upper')
 ck(0<=eta<=F(1,2) and eta*eta>=gs and (eta==0 or (eta-step)**2<gs or eta<step),'Gram upper')
 ck(F(cert['input_radius'])==radius,'input radius')
 delta=radius+2*r+4*max(map(abs,lam))*eta;ck(F(cert['eigenvalue_radius'])==delta,'Weyl radius');ck(len(cert['root_intervals'])==16,'roots')
 lows=[];highs=[]
 for l,pair in zip(lam,cert['root_intervals']):
  a,b=map(F,pair);lo=max(F(0),l-delta);hi=l+delta;ck(hi>=0,'PSD upper');ck(0<=a<=b and a*a<=lo and b*b>=hi,'root containment');ck((a+step)**2>lo and (b==0 or (b-step)**2<hi),'root grid tightness');lows.append(a);highs.append(b)
 ck(F(cert['density_lower'])==-sum(highs)/32 and F(cert['density_upper'])==-sum(lows)/32,'density');return {'residual_squared':str(rs),'gram_squared':str(gs),'density_width':str((sum(highs)-sum(lows))/32)}
