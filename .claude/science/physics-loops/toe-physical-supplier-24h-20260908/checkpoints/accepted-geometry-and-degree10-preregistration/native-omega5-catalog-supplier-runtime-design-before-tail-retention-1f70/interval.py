from fractions import Fraction as F
from math import isqrt,comb
BITS=192;TERMS=160

def rnd(a,b):
 if a>b:raise ValueError('interval order')
 if any(max(abs(x.numerator).bit_length(),x.denominator.bit_length())>65536 for x in (a,b)):raise ValueError('rounding operand cap')
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
