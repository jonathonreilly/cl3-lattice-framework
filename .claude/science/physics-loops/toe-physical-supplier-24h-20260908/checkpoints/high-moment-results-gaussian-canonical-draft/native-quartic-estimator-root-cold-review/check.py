# Independent exact factor identity; no input loader or producer arithmetic.
import importlib.util,json
from fractions import Fraction as F
from pathlib import Path
p=Path('/private/tmp/toe-24h-probes-20260908/native-quartic-estimator-root-review/independent.py');s=importlib.util.spec_from_file_location('qroot',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);n=0
for a,b in m.PAIRS:
 c=m.coefficients(a,b);d=F(1,4);B=1/(d*a*a*b*b);A=B*(1/d+2/a+2/b)
 for x in [d,F(1,2),F(3),F(33)]:
  poly=sum(v*x**i for i,v in enumerate(c));rhs=(x-d)*(x-a)**2*(x-b)**2*(A*x+B)/x**2
  assert poly-1/x**2==rhs and rhs>=0;n+=1
for v in [F(0),F(1,7),F(2),F(121,49)]:
 lo,hi=m.root((v,v));assert lo*lo<=v<=hi*hi;n+=1
try:m.root((F(-2),F(-1)))
except ValueError:n+=1
else:raise AssertionError('negative norm accepted')
print(json.dumps({'checks':n,'native_calls':0,'status':'PASS'}))
