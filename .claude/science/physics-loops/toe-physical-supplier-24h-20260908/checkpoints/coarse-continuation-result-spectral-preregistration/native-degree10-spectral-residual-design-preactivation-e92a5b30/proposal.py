"""Inert exact dyadic proposal; no physical input acquisition or runtime."""
from fractions import Fraction as F
from math import isqrt
DELTA=F(1,4);GRID=1<<32;SQGRID=1<<256

def checked(x,cap=65536):
 x=F(x)
 if max(abs(x.numerator).bit_length(),x.denominator.bit_length())>cap:raise ValueError('rational cap')
 return x

def coefficients(r):
 a,b,c=map(lambda x:checked(x,4096),r)
 B=checked(8*a-32*b);C=checked(3*a-16*b+16*c);D=checked(8*c-2*b)
 return B,C,D

def propose(r):
 B,C,D=coefficients(r)
 if B>=0 or D<=0:return F(1)
 S=checked(checked(C*C)-checked(checked(3*D)*B))
 if S<=0:raise ValueError('radicand')
 integer=(S.numerator*SQGRID*SQGRID)//S.denominator
 k=isqrt(integer)
 if F(k*k,SQGRID*SQGRID)<S:k+=1
 root=checked(F(k,SQGRID))
 if C>=0:tau=checked(checked(root+C)/(-B))
 else:tau=checked(checked(3*D)/checked(root-C))
 ratio=checked(tau/DELTA);ratio=max(F(GRID+1,GRID),min(F(1<<24),ratio))
 n=-((-ratio.numerator*GRID)//ratio.denominator)
 return checked(DELTA*F(n,GRID))

def upper(ranges,tau):
 tau=checked(tau,4096)
 if tau<=0:raise ValueError('positive tau')
 A=checked((tau+2*DELTA)/(DELTA**2*tau**3))
 B=checked(-2/tau**3-2*tau*A);C=checked(3/tau**2+tau*tau*A)
 boxes=[tuple(map(lambda x:checked(x,4096),p))for p in ranges]
 if len(boxes)!=3 or any(len(p)!=2 or p[0]>p[1]for p in boxes):raise ValueError('moment boxes')
 u=checked(checked(A*boxes[2][1])+checked(B*boxes[1][0])+checked(C*boxes[0][1]))
 if u<0:raise ValueError('contradictory negative upper bound')
 return u
