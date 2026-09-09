from fractions import Fraction as F
from math import isqrt,isfinite
EXP=2148
D=1<<100
def roots(n):
 a=isqrt(n*D*D);return F(a,D),F(a+1,D)
def sqrt_up(x):
 x=F(x)
 if x<0:raise ValueError('negative square')
 a=isqrt(x.numerator*D*D//x.denominator)
 if F(a*a,D*D)<x:a+=1
 return F(a,D)
def square(x):
 if not isfinite(x):raise ValueError('nonfinite')
 a,b=x.as_integer_ratio();k=b.bit_length()-1
 if b!=1<<k or k>1074:raise ValueError('dyadic')
 return a*a<<(EXP-2*k)
def counts(index):
 if type(index)is not int or not 0<=index<1<<20:raise ValueError('index')
 top=1^(index.bit_count()&1);bits=index|(top<<20)
 return tuple(((bits>>lo)&((1<<size)-1)).bit_count() for lo,size in [(0,6),(6,6),(12,6),(18,3)])
def energy(c):
 a,b,e,d=c;l3,u3=roots(3);l6,u6=roots(6)
 return (2*a+4*d)*l3+2*b*l6+6*e,(2*a+4*d)*u3+2*b*u6+6*e
def down(x):
 x=F(x);return F((x.numerator*D)//x.denominator,D)
def up(x):
 return -down(-F(x))
def interval(lo,hi):return [str(down(lo)),str(up(hi))]
def summarize(bins,error):
 error=F(error)
 if not 0<=error<=F(1,10**6):raise ValueError('certified Echi domain')
 output={}
 for label,test in [('one',lambda n:n==1),('higher',lambda n:n>=3),('total',lambda n:True)]+[(str(k),lambda n,k=k:n==k) for k in range(1,22,2)]:
  qlo=F(0);qhi=F(0);w=F(0)
  for c,num in bins.items():
   if not test(sum(c)):continue
   w0=F(num,1<<EXP);lo,hi=energy(c)
   if lo<=0:raise ValueError('positive odd excitation')
   w+=w0;qlo+=w0/hi;qhi+=w0/lo
  norm=sqrt_up(w);wlo=max(F(0),norm-F(1,D)-error)**2;whi=(norm+error)**2
  minenergy=(6 if label=='higher' else 2)*roots(3)[0]
  err=error*(2*norm+error)/minenergy
  output[label]={'stored_weight':str(w),'true_weight_interval':interval(wlo,whi),'stored_susceptibility_interval':interval(qlo,qhi),'quadratic_error':str(up(err)),'true_susceptibility_interval':interval(max(F(0),qlo-err),qhi+err)}
 return output
