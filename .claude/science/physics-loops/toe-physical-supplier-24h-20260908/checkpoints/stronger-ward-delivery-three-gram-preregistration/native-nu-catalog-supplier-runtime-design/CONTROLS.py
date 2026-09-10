"""Tiny synthetic identities; no catalog load, panel or integral call."""
from fractions import Fraction as F
import compute
assert compute.moment(0)==1 and compute.moment(1)==6 and compute.moment(2)==42
checks=3
for x in (F(0),F(2),F(7)):
 for t in (F(1,2),F(2),F(8)):
  assert x*x/(x+t*t)==x-t*t+t**4/(x+t*t);checks+=1
  n=4;partial=sum(((-1)**k*x**(k+2)/t**(2*k+2)for k in range(n)),F(0));rem=x**(n+2)/(t**(2*n)*(x+t*t));assert partial+rem==x*x/(x+t*t) and rem>=0;checks+=1
print({'status':'PASS_SYNTHETIC_NU_IDENTITIES','checks':checks,'catalog_calls':0,'integral_calls':0})
