"""Independent rational interval operations; no producer imports."""
from fractions import Fraction as F
CAP=65536
def scalar(x):
 x=F(x)
 if max(abs(x.numerator).bit_length(),x.denominator.bit_length())>CAP:raise ValueError('bit limit')
 return x
def interval(lo,hi):
 lo,hi=scalar(lo),scalar(hi)
 if lo>hi:raise ValueError('empty interval')
 return lo,hi
def plus(a,b):return interval(a[0]+b[0],a[1]+b[1])
def minus(a):return -a[1],-a[0]
def times(a,b):
 z=[x*y for x in a for y in b];return interval(min(z),max(z))
def transpose(a):return [list(r)for r in zip(*a)]
def multiply(a,b):
 out=[[(F(),F())for _ in b[0]]for _ in a]
 for k,row in enumerate(b):
  for j,v in enumerate(row):
   for i in range(len(a)):out[i][j]=plus(out[i][j],times(a[i][k],v))
 return out

def gram_action(m,c,b):
 # Alternative association to the producer C^T(M C), C^T(M B), B^T(M B).
 return multiply(multiply(transpose(c),m),c),multiply(multiply(transpose(c),m),b),multiply(multiply(transpose(b),m),b)
def point(a):return [[interval(x,x)for x in row]for row in a]
