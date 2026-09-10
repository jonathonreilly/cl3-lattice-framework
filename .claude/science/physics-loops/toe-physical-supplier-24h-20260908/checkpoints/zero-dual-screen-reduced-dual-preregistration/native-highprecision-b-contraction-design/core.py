from fractions import Fraction as F
from math import comb,factorial
from interval import add,mul,inv,neg,const

def sub(a,b):return add(a,neg(b))
def scale(a,x):return mul(a,const(x))
def moment(n):
 return sum((F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b) for a in range(n+1) for b in range(n-a+1)),F(0))
def integrands(s,t,a,da,at):
 ss=mul(s,s);tt=mul(t,t);den=sub(tt,ss)
 if den[0]<=0<=den[1]:raise ValueError('coincident interval pole')
 num=sub(mul(tt,at),mul(ss,a));g=mul(num,inv(den))
 hn=sub(mul(add(scale(mul(s,a),2),mul(ss,da)),den),scale(mul(s,num),2))
 return g,mul(hn,inv(mul(den,den)))
def high_tail(s,a,da,moments):
 ss=mul(s,s);c=sub(const(1),mul(ss,a));e=add(scale(mul(s,a),2),mul(ss,da));g=h=const(0)
 for n in range(26):
  weight=F((-1)**n,(2*n+1)*8**(2*n+1));g=add(g,scale(c,weight));h=add(h,scale(e,weight))
  c,e=sub(const(moments[n+1]),mul(ss,c)),sub(scale(mul(s,c),2),mul(ss,e))
 rem=F(12**26,53*8**53)
 return add(g,(F(0),rem)),add(h,(F(0),rem/3))
