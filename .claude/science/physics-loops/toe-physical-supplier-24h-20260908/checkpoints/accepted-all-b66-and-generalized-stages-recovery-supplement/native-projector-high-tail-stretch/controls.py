from fractions import Fraction as F
import json
r=F(9,64)
def bound(n):return F(1,8)*r**n*(1+2*r/F(2*n+3))
assert bound(6)<F(1,10**6)
assert bound(1)<F(9,440)
assert all(bound(n+1)<bound(n)for n in range(1,12))
# Scalar division remainder identity; exact test, not lattice data.
for x in (F(-3),F(0),F(2)):
 for n in(1,2,3):
  t=F(16);poly=sum(((-1)**k*x**(2*k+1)/t**(2*k+2)for k in range(n)),F())
  rem=(-1)**n*x**(2*n+1)/(t**(2*n)*(x*x+t*t))
  assert x/(x*x+t*t)==poly+rem
print(json.dumps({'status':'PASS','scope':'scalar remainder and rational budget only','N6_bound':str(bound(6)),'rank_bound':22,'max_integer_moment':11}))
