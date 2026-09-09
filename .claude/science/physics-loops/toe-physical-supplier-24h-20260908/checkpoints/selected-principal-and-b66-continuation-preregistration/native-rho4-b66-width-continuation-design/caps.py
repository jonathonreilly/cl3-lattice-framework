"""Stored Fraction cap32768; explicit fixed256 rounding temporary cap33024."""
from fractions import Fraction as F
CAP=32768;GRID=256;TRANSIENT=CAP+GRID

def guard(x):
 if type(x)is not F or max(abs(x.numerator).bit_length(),x.denominator.bit_length())>CAP:raise ValueError('stored Fraction cap32768')
 return x

def upward(x):
 guard(x)
 if x<0:raise ValueError('nonnegative radius')
 # Multiplication by a power of two has exactly bounded bit growth.
 n=x.numerator<<GRID
 if n.bit_length()>TRANSIENT:raise ValueError('rounding transient cap33024')
 q,r=divmod(n,x.denominator)
 if q.bit_length()>TRANSIENT:raise ValueError('rounding quotient cap33024')
 q+=bool(r)
 if q.bit_length()>TRANSIENT+1:raise ValueError('rounding increment cap33025')
 return guard(F(q,1<<GRID))

def tree(x):
 if type(x)is F:return guard(x)
 if isinstance(x,dict):
  for v in x.values():tree(v)
 elif isinstance(x,(tuple,list)):
  for v in x:tree(v)
 return x
def operand(x):
 guard(x)
 if max(abs(x.numerator).bit_length(),x.denominator.bit_length())>512:raise ValueError('input operand cap512')
 return x
def pole(x):
 guard(x)
 if max(abs(x.numerator).bit_length(),x.denominator.bit_length())>256:raise ValueError('pole operand cap256')
 return x
