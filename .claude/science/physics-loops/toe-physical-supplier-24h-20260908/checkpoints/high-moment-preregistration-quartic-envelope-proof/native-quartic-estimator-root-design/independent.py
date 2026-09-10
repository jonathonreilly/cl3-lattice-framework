"""Independent exact quartic arithmetic; no producer imports or input loader."""
from fractions import Fraction as F
from math import isqrt
from itertools import combinations_with_replacement
PAIRS=tuple(combinations_with_replacement(map(F,[1,2,4,8,16]),2));DELTA=F(1,4)
def guard(x):
 if type(x)is not F or max(abs(x.numerator).bit_length(),x.denominator.bit_length())>32768:raise ValueError('rational cap')
 return x
def plus(x,y):return guard(x+y)
def times(x,y):return guard(x*y)
def nonnegative(a):
 if a[1]<0:raise ValueError('contradictory norm')
 return max(F(0),a[0]),a[1]
def scaled(a,c):
 return (times(a[0],c),times(a[1],c))if c>=0 else(times(a[1],c),times(a[0],c))
def summed(a,b):return plus(a[0],b[0]),plus(a[1],b[1])
def root(a):
 a=nonnegative(a);q=1<<128;out=[]
 for j,v in enumerate(a):
  n=isqrt(v.numerator*q*q//v.denominator)
  if j and n*n*v.denominator<v.numerator*q*q:n+=1
  out.append(guard(F(n,q)))
 return tuple(out)
def coefficients(t,u):
 d=DELTA;B=guard(1/(d*t*t*u*u));A=guard(B*(1/d+2/t+2/u));e1=d+2*t+2*u;e2=t*t+u*u+4*t*u+2*d*(t+u);e3=2*t*u*(t+u)+d*(t*t+u*u+4*t*u);e4=t*t*u*u+2*d*t*u*(t+u)
 return [guard(x)for x in[A*e4-B*e3,B*e2-A*e3,A*e2-B*e1,B-A*e1,A]]
def rho(m,p,old_r2):
 v=[F(1)]+[-x for x in p];d=[guard(sum(v[i]*v[j]for i in range(4)for j in range(4)if i+j==k))for k in range(7)];out=[nonnegative(old_r2)]
 for n in range(1,5):
  acc=(F(0),F(0))
  for k in range(7):acc=summed(acc,scaled(m[n+k],d[k]))
  out.append(nonnegative(acc))
 return d,out

def class_candidates(m,p,old_r2,old_first_squared):
 d,r=rho(m,p,old_r2);best=min(old_first_squared,guard(r[0][1]/DELTA**2));records=[]
 if best<0:raise ValueError('negative inherited bound')
 for t,u in PAIRS:
  c=coefficients(t,u);v=(F(0),F(0))
  for a,b in zip(r,c):v=summed(v,scaled(a,b))
  records.append({'tau1':t,'tau2':u,'coefficients':c,'interval':v})
  if v[1]<0:raise ValueError('negative envelope upper')
  best=min(best,v[1])
 return {'convolution':d,'rho':r,'candidates':records,'best_squared_upper':best}
def posterior(E,FF,a2,b2,nominal,old):
 a=root(a2)[1];b=root(b2)[1];X=guard(4*root((F(15),F(15)))[1]);V=guard(32*root((F(30),F(30)))[1]);chi=min(X,plus(a,E));psi=min(V,plus(b,FF));error=guard(6*(E*(a+chi)+min(E*b+chi*FF,E*psi+a*FF)));new=(guard((nominal[0]-error)/8),guard((nominal[1]+error)/8));final=(max(new[0],old[0]),min(new[1],old[1]))
 if final[0]>final[1]:raise ValueError('empty valid intersection')
 return {'E_upper':E,'F_upper':FF,'trial_a_upper':a,'trial_b_upper':b,'error_upper':error,'new_alpha':new,'old_alpha':old,'intersection':final}
