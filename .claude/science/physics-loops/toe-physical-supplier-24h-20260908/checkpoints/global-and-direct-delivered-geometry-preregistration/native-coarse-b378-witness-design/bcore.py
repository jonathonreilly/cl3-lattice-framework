"""New fixed B-only contraction. No oracle; all calls prospective."""
from fractions import Fraction as F
from math import comb,factorial
from interval import add,mul,inv,neg,const

def sub(a,b):return add(a,neg(b))
def scale(a,q):return mul(a,const(q))
def moment(n):
 return sum((F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b) for a in range(n+1) for b in range(n-a+1)),F(0))
def one(s,a,nodes,moments,pi,emit):
 s=const(F(s));ss=mul(s,s);total=const(0)
 if len(nodes)!=1742 or len(moments)!=41:raise ValueError('fixed node/moment census')
 for i,row in enumerate(nodes):
  emit('before_node',{'id':i})
  t,weight,at=row['t'],row['weight'],row['A'];tt=mul(t,t);den=sub(tt,ss)
  if den[0]<=0<=den[1]:raise ValueError('separation failed')
  g=mul(sub(mul(tt,at),mul(ss,a)),inv(den));total=add(total,mul(weight,g))
  if (i+1)%26==0:emit('panel',{'completed':i+1,'sum':total})
 eps=F(1,2**64)
 # G(0)=A(s), |G(t)-A(s)|<=t² A0/s².
 low=add(scale(a,eps),(-eps**3*F(17,60)/(3*ss[0]),F(0)))
 high=const(0);c=sub(const(1),mul(ss,a))
 for n in range(40):
  emit('before_high',{'n':n})
  high=add(high,scale(c,F((-1)**n,(2*n+1)*8**(2*n+1))))
  c=sub(const(moments[n+1]),mul(ss,c))
 rem=F(12**40,81*8**81);high=add(high,(F(0),rem))
 quad=F(128,4**52)
 full=add(add(add(total,low),high),(-quad,quad))
 ans=mul(full,scale(inv(pi),2));emit('final_interval',{'B':ans,'low':low,'high':high,'quadrature_radius':str(quad)})
 return ans
def pi_bounds():
 def atan(q,n):
  x=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0));d=F((-1)**n,(2*n+1)*q**(2*n+1));return min(x,x+d),max(x,x+d)
 a=atan(5,40);b=atan(239,12)
 return 16*a[0]-4*b[1],16*a[1]-4*b[0]
