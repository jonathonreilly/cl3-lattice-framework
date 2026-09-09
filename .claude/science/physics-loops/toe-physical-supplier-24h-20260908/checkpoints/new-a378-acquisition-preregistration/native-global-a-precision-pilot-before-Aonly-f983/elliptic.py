from fractions import Fraction as F
from math import isqrt,comb
BITS=384;TERMS=512

def rnd(a,b):
 q=1<<BITS
 return F((a.numerator*q)//a.denominator,q),F(-((-b.numerator*q)//b.denominator),q)
def const(x):x=F(x);return (x,x)
def add(a,b):return rnd(a[0]+b[0],a[1]+b[1])
def neg(a):return -a[1],-a[0]
def mul(a,b):
 z=[x*y for x in a for y in b];return rnd(min(z),max(z))
def inv(a):
 if a[0]<=0<=a[1]:raise ValueError('reciprocal zero')
 return rnd(1/a[1],1/a[0])
def sqrt(a):
 if a[0]<0:raise ValueError('negative root')
 q=1<<BITS;l=isqrt((a[0].numerator*q*q)//a[0].denominator);h=isqrt((a[1].numerator*q*q)//a[1].denominator)
 if F(h*h,q*q)<a[1]:h+=1
 return F(l,q),F(h,q)
class D:
 def __init__(self,v,d=0):self.v=v if isinstance(v,tuple) else const(v);self.d=d if isinstance(d,tuple) else const(d)
 def __add__(a,b):
  b=b if isinstance(b,D) else D(b);return D(add(a.v,b.v),add(a.d,b.d))
 __radd__=__add__
 def __neg__(a):return D(neg(a.v),neg(a.d))
 def __sub__(a,b):return a+-asD(b)
 def __rsub__(a,b):return asD(b)+-a
 def __mul__(a,b):
  b=asD(b);return D(mul(a.v,b.v),add(mul(a.d,b.v),mul(a.v,b.d)))
 __rmul__=__mul__
 def reciprocal(a):
  v=inv(a.v);return D(v,neg(mul(a.d,mul(v,v))))
 def __truediv__(a,b):return a*asD(b).reciprocal()
 def __rtruediv__(a,b):return asD(b)*a.reciprocal()
 def root(a):
  v=sqrt(a.v);return D(v,mul(a.d,inv(mul(const(2),v))))
 def __pow__(a,n):
  z=D(1)
  for _ in range(n):z=z*a
  return z
def asD(a):return a if isinstance(a,D) else D(a)

def oracle(s):
 s=F(s)
 if s<0:raise ValueError('nonnegative s')
 x=D(s,1);q=x*x+6
 xi=(4/((q+(q*q-4).root())*(q+x*(x*x+12).root()))).root()
 den=(1-xi)**3*(1+3*xi);m=16*xi**3/den
 if not 0<=m.v[0]<=m.v[1]<F(16,27):raise ValueError('elliptic parameter bound')
 C=D(0);power=D(1)
 for n in range(TERMS):
  C=C+F(comb(2*n,n)**2,16**n)*power;power=power*m
 # Positive scalar series tail; derivative w.r.t m is positive.
 z=m.v[1];r=z**TERMS/(1-z);dr=TERMS*z**(TERMS-1)/(1-z)+z**TERMS/(1-z)**2
 C=D(add(C.v,(F(0),r)),add(C.d,mul((F(0),dr),m.d)))
 A=(1-9*xi**4)/den*C*C/q
 return {'audit':{name:{'value':[str(y) for y in obj.v],'derivative':[str(y) for y in obj.d]} for name,obj in [('xi',xi),('den',den),('m',m),('series_with_tail',C)]},'bits':BITS,'s':str(s),'A':[str(t) for t in A.v],'Aprime':[str(t) for t in A.d],'widths':[str(A.v[1]-A.v[0]),str(A.d[1]-A.d[0])],'terms':TERMS,'derivative_side':'right' if s==0 else 'ordinary','target':'1/1000000000000','status':'CERTIFIED_TARGET' if max(A.v[1]-A.v[0],A.d[1]-A.d[0])<=F(1,10**12) else 'INDETERMINATE'}
