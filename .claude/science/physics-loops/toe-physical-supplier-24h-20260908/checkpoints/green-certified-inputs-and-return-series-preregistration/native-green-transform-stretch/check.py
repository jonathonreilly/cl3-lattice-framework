from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json
xs=[F(1),F(4),F(9)];weights=[F(1,6),F(1,3),F(1,2)]
def avg(fun):return sum((w*fun(x) for x,w in zip(xs,weights)),F(0))
n=0
for s in [F(1,2),F(1),F(2),F(3)]:
 A=lambda t:avg(lambda x:1/(x+t*t))
 for t in [F(1,2),F(1),F(2),F(3),F(4)]:
  direct=avg(lambda x:x/((x+s*s)*(x+t*t)))
  other=(t*t*A(t)-s*s*A(s))/(t*t-s*s) if t!=s else A(s)-s*s*avg(lambda x:1/(x+s*s)**2)
  if direct!=other:raise ValueError('divided difference')
  n+=1
 c=1-s*s*A(s)
 for j in range(10):
  if c!=avg(lambda x:x**(j+1)/(x+s*s)):raise ValueError('moment recurrence')
  c=avg(lambda x:x**(j+1))-s*s*c;n+=1
# Independent exact native moment normalization, no momentum evaluation.
def moment(n):
 return sum((F(factorial(n),factorial(a)*factorial(b)*factorial(n-a-b))*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b) for a in range(n+1) for b in range(n-a+1)),F(0))
if [moment(j) for j in range(3)]!=[1,6,42]:raise ValueError('native moments')
n+=3
out={'status':'PASS','checks':n,'physical_runs':0,'scope':'synthetic finite spectral measure identities and exact combinatorial moments'}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
