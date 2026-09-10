"""Exact rational synthetic model of proposed coefficient algebra; no file IO."""
from fractions import Fraction as F
I=[[int(i==j)for j in range(7)]for i in range(7)]
O=[[int(i>0 and j>0 and (i-1)//2==(j-1)//2 and i!=j)for j in range(7)]for i in range(7)]
T=[[0]*7 for _ in range(7)]
for j in range(1,7):T[0][j]=-(-1)**(j+1);T[j][0]=-T[0][j]
def source_triple(x,y):return tuple(sum(x[i]*M[i][j]*y[j]for i in range(7)for j in range(7))for M in [I,O,T])
def coefficients(s,sign,A,B):
 d=(1-s*s*A)/6
 return (sign*s*A,sign*s*(A-d),d),(-B,-(1+s*s/6)*B,sign*s*B/6)
def contract(c,d):return sum(x*y for x,y in zip(c,d))
def cross(s,sign,t,tau,As,Bs,At,Bt,gamma,d):
 C,L=coefficients(t,tau,At,Bt);N,J=coefficients(s,-sign,As,Bs);den=sign*s+tau*t
 if not den:raise ValueError('fixed denominator zero')
 return contract(tuple(((-1 if gamma else 1)*(x-y)/den)for x,y in zip(L if gamma else C,J if gamma else N)),d)
def local_gamma(s,sign,A,B,mu,d):
 _,L=coefficients(s,sign,A,B);return contract((-L[0],-L[1]-mu/6,-L[2]),d)
