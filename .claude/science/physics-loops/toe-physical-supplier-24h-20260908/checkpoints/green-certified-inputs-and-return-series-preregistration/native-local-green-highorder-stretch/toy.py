from fractions import Fraction as F
from highorder import gauss,mul,poly
import json
checks=0
for n in (2,4):
 rule=gauss(n)
 for k in range(2*n):
  lo=hi=F(0)
  for x,w in rule:
   z=(F(1),F(1))
   for _ in range(k):z=mul(z,x)
   a,b=mul(w,z);lo+=a;hi+=b
  exact=F(0) if k%2 else F(2,k+1)
  if not lo<=exact<=hi:raise ValueError('Gauss exact polynomial enclosure')
  checks+=1
print(json.dumps({'status':'PASS','checks':checks,'physical_integrals':0}))
