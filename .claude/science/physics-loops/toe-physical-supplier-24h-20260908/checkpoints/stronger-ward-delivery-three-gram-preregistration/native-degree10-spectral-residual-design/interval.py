from fractions import Fraction as F
from math import isqrt
import re
BITS=32768

def check(v):
 if max(abs(v.numerator).bit_length(),v.denominator.bit_length())>BITS:raise ValueError('stored rational cap')
 return v
def parse(x):
 if type(x)is not str or len(x)>20000 or re.fullmatch(r'-?\d+(?:/\d+)?',x)is None:raise ValueError('rational syntax')
 v=check(F(x))
 if str(v)!=x:raise ValueError('canonical rational')
 return v
def point(v):v=check(F(v));return(v,v)
def box(x):
 if type(x)is not list or len(x)!=2:raise ValueError('interval shape')
 a,b=map(parse,x)
 if a>b:raise ValueError('interval order')
 return(a,b)
def add(a,b):return(check(a[0]+b[0]),check(a[1]+b[1]))
def neg(a):return(-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 v=[check(x*y)for x in a for y in b];return(min(v),max(v))
def scale(a,v):return mul(a,point(v))
def div(a,b):
 if b[0]<=0<=b[1]:raise ValueError('zero denominator interval')
 return mul(a,(check(1/b[1]),check(1/b[0])))
def square(a):
 if a[0]>=0:return(check(a[0]*a[0]),check(a[1]*a[1]))
 if a[1]<=0:return square(neg(a))
 return(F(0),max(check(a[0]*a[0]),check(a[1]*a[1])))
def root(a):
 if a[0]<0:raise ValueError('negative root input')
 s=1<<128
 def floor(v):
  k=isqrt(v.numerator*s*s//v.denominator)
  if not k*k*v.denominator<=v.numerator*s*s<(k+1)**2*v.denominator:raise ValueError('root proof')
  return k
 lo=floor(a[0]);hi=floor(a[1]);exact=hi*hi*a[1].denominator==a[1].numerator*s*s
 return(check(F(lo,s)),check(F(hi if exact else hi+1,s)))
def nonnegative(a):
 if a[1]<0:raise ValueError('negative certified norm upper')
 return(max(F(0),a[0]),a[1])
def mid(a):return check((a[0]+a[1])/2)
def encode(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,(tuple,list)):return[encode(x)for x in v]
 if isinstance(v,dict):return{k:encode(x)for k,x in v.items()}
 return v
