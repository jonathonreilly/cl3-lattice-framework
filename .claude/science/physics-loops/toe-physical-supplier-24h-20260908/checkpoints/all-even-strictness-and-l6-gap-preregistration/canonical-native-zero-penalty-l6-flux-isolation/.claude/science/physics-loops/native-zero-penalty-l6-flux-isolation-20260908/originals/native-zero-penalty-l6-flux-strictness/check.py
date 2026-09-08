from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import json
# AP positive canonical winding: sin² values1/4 (4),1 (2).
# P negative winding:0 (2),3/4 (4).
def root(x):
 D=10**30;n=isqrt(x.numerator*D*D//x.denominator)
 return F(n,D),F(n+1,D)
rows=[]
for twists in product((1,-1),repeat=3):
 values=[[(F(1,4),4),(F(1),2)] if t==1 else [(F(0),2),(F(3,4),4)] for t in twists]
 lo=hi=F(0)
 for terms in product(*values):
  x=sum(t[0] for t in terms);m=1
  for z in terms:m*=z[1]
  a,b=root(x);lo+=m*a;hi+=m*b
 rows.append(dict(twists=twists,minus_energy_interval=[str(lo),str(hi)]))
a=F(rows[0]['minus_energy_interval'][0])
for r in rows[1:]:
 gap=a-F(r['minus_energy_interval'][1])
 if gap<=0:raise ValueError('twist degeneracy candidate not excluded')
 r['energy_gap_lower']=str(gap)
Path(__file__).with_name('RESULT.json').write_text(json.dumps({'scope':'all eight pi-plaquette flat winding sectors only, g lambda=1','rows':rows},indent=2)+'\n')
