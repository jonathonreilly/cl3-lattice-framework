"""Exact rational a-priori envelopes; no array operations or physical calls."""
from fractions import Fraction as F
from math import isqrt
u=F(1,1<<53);zeta=F(1,1<<1075);s=1024

def root_upper(x):
 x=F(x)
 if x<0:raise ValueError('negative square')
 D=1<<100;n=isqrt(x.numerator*D*D//x.denominator)
 if F(n*n,D*D)<x:n+=1
 return F(n,D)
def gamma(k):return k*u/(1-k*u)
def endpoint(rows):
 m=len(rows);eta=root_upper(sum(F(r['candidate_radius'])**2 for r in rows));L=sum(abs(F(float.fromhex(r['candidate_hex']))) for r in rows)
 return eta+gamma(m+1)*L,s*2*m*zeta/(1-u)**(m+1)
def enderror(rows,X):
 e,a=endpoint(rows);return e*X+a

def action(coeff,pair,X):
 center=coeff['center'];chains=[]
 for v,k in pair:
  if abs(k)!=2:raise ValueError('power2 native scale')
  e=enderror(coeff['neighbors'][str(v)],X);e+=enderror(center,X+e);chains.append(e)
 T=sum(abs(F(float.fromhex(r['candidate_hex']))) for r in coeff['frequencies']);delta=sum(F(r['candidate_radius']) for r in coeff['frequencies']);lam=sum(F(r['upper']) for r in coeff['frequencies']);rounding=gamma(21)*T+21*zeta/(1-u)**21;dmax=T+rounding;ED=(delta+rounding+u*dmax)*X+s*zeta;Q=lam*X+ED;errors=[]
 for e in chains:
  V=2*(X+e);a=u*(Q+V)+s*zeta;errors.append(a);Q+=V+a
 EH=ED+2*sum(chains)+sum(errors)
 return EH,(lam+4)*X+EH

def residual(coeff,pair,X,R,Bhat,Berr=F(0)):
 EH,Y=action(coeff,pair,X);rho=R+EH+u*(Bhat+Y)+s*zeta
 return {'rho':rho,'solution_error':3*(rho+Berr),'action_error':EH}
def sum_error(norms):
 n=len(norms)
 if n<1:raise ValueError('empty sum')
 return gamma(n-1)*sum(norms)+(n-1)*s*zeta/(1-u)**(n-1)
def eg_error(eta,L,X):return (eta+gamma(3)*L)*X+3*s*zeta/(1-u)**3

def transport_error(eta,L,X):
 err=F(0)
 for _ in range(4):err+=eg_error(eta,L,X+err)
 return err

def final_error(second_errors,transport_errors,norms):
 if not(len(second_errors)==len(transport_errors)==len(norms)==15):raise ValueError('full fifteen')
 return (sum(second_errors)+sum(transport_errors)+sum_error(norms))/8+s*zeta
