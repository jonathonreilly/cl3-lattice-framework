"""Exact dyadic residual and Gram; no NumPy dependency or top-level execution."""
from fractions import Fraction as F
from math import isqrt,isfinite

def sqrt_bounds(x,bits=80):
 x=F(x)
 if x<0:raise ValueError('negative square root')
 scaled=x.numerator<<(2*bits);q=isqrt(scaled//x.denominator)
 lower=F(q,1<<bits)
 upper=lower if q*q*x.denominator==scaled else F(q+1,1<<bits)
 return lower,upper

def dyadic(values):
 ratios=[];power=0
 for x in values:
  x=float(x)
  if not isfinite(x):raise ValueError('finite candidate')
  a,b=x.as_integer_ratio();p=b.bit_length()-1
  if b!=1<<p:raise ValueError('dyadic representation')
  ratios.append((a,p));power=max(power,p)
 return [a<<(power-p) for a,p in ratios],power

def certificate(D,Q,eigenvalues,input_radius):
 n=len(D)
 if n!=16 or len(Q)!=n or len(eigenvalues)!=n or any(len(x)!=n for x in D+Q):raise ValueError('matrix dimensions')
 input_radius=F(input_radius)
 if input_radius<0:raise ValueError('input radius')
 dn,d=dyadic([v for row in D for z in row for v in (complex(z).real,complex(z).imag)])
 qn,b=dyadic([v for row in Q for z in row for v in (complex(z).real,complex(z).imag)])
 en,e=dyadic(eigenvalues)
 Dn=[[(dn[2*(i*n+j)],dn[2*(i*n+j)+1]) for j in range(n)] for i in range(n)]
 Qn=[[(qn[2*(i*n+j)],qn[2*(i*n+j)+1]) for j in range(n)] for i in range(n)]
 for i in range(n):
  for j in range(n):
   if Dn[i][j]!=(Dn[j][i][0],-Dn[j][i][1]):raise ValueError('exact Hermitian candidate matrix')
 residual_squared=0;gram_squared=0
 for i in range(n):
  for j in range(n):
   ar=ai=gr=gi=0
   for k in range(n):
    x,y=Dn[i][k];u,v=Qn[k][j];ar+=x*u-y*v;ai+=x*v+y*u
    x,y=Qn[k][i];u,v=Qn[k][j];gr+=x*u+y*v;gi+=x*v-y*u
   u,v=Qn[i][j];ar=(ar<<e)-((u*en[j])<<d);ai=(ai<<e)-((v*en[j])<<d)
   residual_squared+=ar*ar+ai*ai
   if i==j:gr-=1<<(2*b)
   gram_squared+=gr*gr+gi*gi
 r=sqrt_bounds(F(residual_squared,1<<(2*(d+b+e))))[1]
 eta=sqrt_bounds(F(gram_squared,1<<(4*b)))[1]
 if eta>F(1,2):raise ValueError('Gram tolerance')
 L=max(abs(F(x,1<<e)) for x in en)
 radius=2*r+4*L*eta
 root_lo=root_hi=F(0);intervals=[]
 for x in en:
  center=F(x,1<<e);lo=center-radius;hi=center+radius
  if hi<0:raise ValueError('negative PSD upper endpoint')
  a=sqrt_bounds(max(F(0),lo))[0];z=sqrt_bounds(hi)[1];root_lo+=a;root_hi+=z;intervals.append([str(a),str(z)])
 return dict(eta=str(eta),residual=str(r),input_radius=str(input_radius),eigenvalue_radius=str(radius),density_lower=str(-root_hi/32),density_upper=str(-root_lo/32),root_intervals=intervals,arithmetic='exact dyadic integers; rational outward sqrt',dimension=n)
