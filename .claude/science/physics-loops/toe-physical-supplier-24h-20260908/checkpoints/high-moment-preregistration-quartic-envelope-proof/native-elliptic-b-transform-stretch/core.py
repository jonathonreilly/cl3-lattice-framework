from fractions import Fraction as F
from math import comb,factorial
from elliptic import add,mul,inv,neg,const

def sub(a,b):return add(a,neg(b))
def scale(a,x):return mul(a,const(x))
def moment(n):
 return sum((F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b) for a in range(n+1) for b in range(n-a+1)),F(0))
def integrands(s,t,a,da,at):
 ss=s*s;tt=mul(t,t);den=sub(tt,const(ss))
 if den[0]<=0<=den[1]:raise ValueError('coincident interval pole')
 num=sub(mul(tt,at),scale(a,ss));g=mul(num,inv(den))
 hn=sub(mul(add(scale(a,2*s),scale(da,ss)),den),scale(num,2*s))
 h=mul(hn,inv(mul(den,den)))
 return g,h
def high_tail(s,a,da):
 c=sub(const(1),scale(a,s*s));e=add(scale(a,2*s),scale(da,s*s));g=h=const(0)
 for n in range(16):
  weight=F((-1)**n,(2*n+1)*8**(2*n+1));g=add(g,scale(c,weight));h=add(h,scale(e,weight))
  c,e=sub(const(moment(n+1)),scale(c,s*s)),sub(scale(c,2*s),scale(e,s*s))
 rem=F(12**16,33*8**33)
 return add(g,(F(0),rem)),add(h,(F(0),rem/(2*s)))
