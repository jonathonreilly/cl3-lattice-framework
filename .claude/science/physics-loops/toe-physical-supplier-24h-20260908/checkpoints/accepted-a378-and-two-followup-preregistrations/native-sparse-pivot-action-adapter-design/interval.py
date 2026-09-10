"""Outward fixed192-bit integer intervals. No floating arithmetic."""
from fractions import Fraction
from math import isqrt
BITS=192;S=1<<BITS
ZERO=(0,0);ONE=(S,S)
def rational(x):
 x=Fraction(x);a=x.numerator*S;b=x.denominator
 return (a//b,-((-a)//b))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 z=[x*y for x in a for y in b];return(min(z)//S,-((-max(z))//S))
def div(a,b):
 if b[0]<=0<=b[1]:raise ValueError('interval divisor contains zero')
 q=[(x*S,y) for x in a for y in b]
 lows=[x//y for x,y in q];highs=[-((-x)//y) for x,y in q]
 return(min(lows),max(highs))
def scale(a,x):return mul(a,rational(x))
def sqrt(a):
 if a[0]<0:raise ValueError('negative sqrt input')
 lo=isqrt(a[0]*S);hi=isqrt(a[1]*S)
 if hi*hi<a[1]*S:hi+=1
 return(lo,hi)
def width(a):return a[1]-a[0]
def midpoint(a):return Fraction(a[0]+a[1],2*S)
def bounds(a):return [str(Fraction(x,S)) for x in a]
def contains_zero(a):return a[0]<=0<=a[1]
def matmul(a,b):
 return [[sum_iv(mul(a[i][k],b[k][j]) for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def sum_iv(a):
 z=ZERO
 for x in a:z=add(z,x)
 return z
