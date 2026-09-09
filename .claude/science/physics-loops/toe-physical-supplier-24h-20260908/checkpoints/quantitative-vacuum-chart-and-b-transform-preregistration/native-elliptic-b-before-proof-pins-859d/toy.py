from fractions import Fraction as F
from core import integrands,moment
from elliptic import const
import json
n=0
for s in (F(1),F(2)):
 for t in (F(1,2),F(3),F(4)):
  xs=[F(1),F(4),F(9)];a=sum(1/(x+s*s) for x in xs)/3;da=-2*s*sum(1/(x+s*s)**2 for x in xs)/3;at=sum(1/(x+t*t) for x in xs)/3
  g,h=integrands(s,const(t),const(a),const(da),const(at));eg=sum(x/((x+s*s)*(x+t*t)) for x in xs)/3;eh=2*s*sum(x/((x+s*s)**2*(x+t*t)) for x in xs)/3
  if not g[0]<=eg<=g[1] or not h[0]<=eh<=h[1]:raise ValueError('synthetic transform')
  n+=2
try:integrands(F(1),(F(1),F(1)),const(1),const(-1),const(1))
except ValueError:n+=1
else:raise ValueError('pole guard')
if [moment(j) for j in range(3)]!=[1,6,42]:raise ValueError('moments')
n+=3
print(json.dumps({'status':'PASS','checks':n,'physical_calls':0}))
