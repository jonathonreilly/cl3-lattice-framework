"""Native two-seed midpoint formulae. Imported intervals are arithmetic-only."""
from fractions import Fraction as F
import interval as iv

def coefficients(s,sigma,values,kind):
 if kind not in ('P','O') or sigma not in(-1,1):raise ValueError('kind/sign')
 A,Ap,B,Bp=map(iv.rational,values);s=iv.rational(s);s2=iv.mul(s,s)
 D=iv.scale(iv.sub(iv.ONE,iv.mul(s2,A)),F(1,6))
 Dp=iv.scale(iv.neg(iv.add(iv.scale(iv.mul(s,A),2),iv.mul(s2,Ap))),F(1,6))
 geo,geop=(A,Ap) if kind=='P' else (D,Dp)
 C=[[iv.scale(iv.mul(s,A),sigma),iv.scale(D,-2)],[iv.scale(D,2),iv.scale(iv.mul(s,geo),2*sigma)]]
 Cp=[[iv.scale(iv.add(A,iv.mul(s,Ap)),sigma),iv.scale(Dp,-2)],[iv.scale(Dp,2),iv.scale(iv.add(geo,iv.mul(s,geop)),2*sigma)]]
 off=iv.scale(iv.mul(s,B),F(sigma,3));offp=iv.scale(iv.add(B,iv.mul(s,Bp)),F(sigma,3))
 last=iv.scale(B,-2) if kind=='P' else iv.scale(iv.mul(s2,B),F(1,3))
 lastp=iv.scale(Bp,-2) if kind=='P' else iv.scale(iv.add(iv.scale(iv.mul(s,B),2),iv.mul(s2,Bp)),F(1,3))
 L=[[iv.neg(B),iv.neg(off)],[off,last]];Lp=[[iv.neg(Bp),iv.neg(offp)],[offp,lastp]]
 return C,Cp,L,Lp

def woodbury(s,values,kind):
 A=iv.rational(values[0]);s=iv.rational(s);D=iv.scale(iv.sub(iv.ONE,iv.mul(iv.mul(s,s),A)),F(1,6));geo=A if kind=='P' else D
 a=iv.sub(iv.ONE,iv.scale(D,4));det=iv.add(iv.mul(a,a),iv.scale(iv.mul(iv.mul(iv.mul(s,s),A),geo),8))
 if det[0]<=0:raise ValueError('Woodbury determinant gate')
 # T=i*t, Jnode off-diagonal blocks T/35,T*/35.
 t=[[iv.div(iv.scale(iv.mul(s,geo),-8),det),iv.div(iv.scale(a,2),det)],[iv.div(iv.scale(a,-2),det),iv.div(iv.scale(iv.mul(s,A),-4),det)]]
 signed=[[iv.scale(x,F(1,35)) for x in row] for row in t]
 # V^-1+G = i*q; (i*q)(i*t)=-q*t=I.
 # V=2iJ has inverse=iJ/2 (J²=-I).
 q=[[iv.mul(s,A),iv.add(iv.scale(D,-2),iv.rational(F(1,2)))],[iv.sub(iv.scale(D,2),iv.rational(F(1,2))),iv.scale(iv.mul(s,geo),2)]]
 qt=iv.matmul(q,t);res=[[iv.add(qt[i][j],iv.ONE if i==j else iv.ZERO) for j in range(2)] for i in range(2)]
 if not all(iv.contains_zero(x) for row in res for x in row):raise ValueError('coefficient inverse identity')
 return signed,det,res

def entry(i,j,labels,cache):
 ni,s,sig,a=labels[i];nj,t,tau,b=labels[j];den=sig*s+tau*t
 if den:
  g=iv.div(iv.sub(cache[nj,tau][0][a][b],cache[ni,-sig][0][a][b]),iv.rational(den))
  z=iv.neg(iv.div(iv.sub(cache[nj,tau][2][a][b],cache[ni,-sig][2][a][b]),iv.rational(den)))
 else:
  g=iv.scale(cache[nj,tau][1][a][b],tau);z=iv.scale(cache[nj,tau][3][a][b],-tau)
 return g,iv.ZERO if i==j else z
