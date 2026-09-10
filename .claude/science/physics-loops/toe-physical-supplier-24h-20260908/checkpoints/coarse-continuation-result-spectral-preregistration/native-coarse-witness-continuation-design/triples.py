from fractions import Fraction as F
from functools import lru_cache
from interval import const,add,mul,neg
from dictionary import I,O,T

def scale(a,q):return mul(a,const(q))
def sub(a,b):return add(a,neg(b))
@lru_cache(maxsize=256)
def dots(x,y):return tuple(sum(x[i]*M[i][j]*y[j]for i in range(7)for j in range(7))for M in [I,O,T])
def contract(coef,d):
 z=const(0)
 for a,k in zip(coef,d):
  if k:z=add(z,scale(a,k))
 return z
@lru_cache(maxsize=900)
def coefficients(s,sigma,A,B):
 d=scale(sub(const(1),scale(A,s*s)),F(1,6));C=(scale(A,sigma*s),scale(sub(A,d),sigma*s),d);L=(neg(B),neg(mul(add(const(1),const(s*s/6)),B)),scale(B,sigma*s/6));return C,L
@lru_cache(maxsize=528)
def divided(s,sigma,t,tau,As,Bs,At,Bt,gamma):
 den=sigma*s+tau*t
 if not den:raise ValueError('fixed denominator zero')
 C,L=coefficients(t,tau,At,Bt);N,J=coefficients(s,-sigma,As,Bs);return tuple(scale(sub(a,b),F(-1 if gamma else 1)/den)for a,b in zip(L if gamma else C,J if gamma else N))
def local(s,sigma,A,B,mu,gamma,d):
 C,L=coefficients(s,sigma,A,B)
 if gamma:C=(neg(L[0]),sub(neg(L[1]),scale(mu,F(1,6))),neg(L[2]))
 return contract(C,d)
