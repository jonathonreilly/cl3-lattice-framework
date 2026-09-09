from pathlib import Path
import types,json
from fractions import Fraction as F
p=Path('/private/tmp/toe-24h-probes-20260908/native-sparse-action-saved-postcheck/arithmetic.py');a=types.ModuleType('a');exec(compile(p.read_bytes(),str(p),'exec'),a.__dict__);n=0
for x in (F(-5,7),F(0),F(3,11)):
 for y in (F(2,9),F(7,3)):
  xx=a.q(x);yy=a.q(y)
  for name,target in [('add',x+y),('mul',x*y),('div',x/y)]:
   lo,hi=a.op(xx,yy,name)
   if not F(lo,a.S)<=target<=F(hi,a.S):raise ValueError('exact endpoint')
   n+=1
for v in (F(2),F(1,7)):
 lo,hi=a.root(a.q(v))
 if not F(lo*lo,a.S*a.S)<=v<=F(hi*hi,a.S*a.S):raise ValueError('root')
 n+=1
v={(396,0):a.q(F(3,7)),(397,1):a.q(F(-5,11))}
if a.gamma(a.gamma(v))!={k:a.minus(x) for k,x in v.items()}:raise ValueError('Gamma')
n+=1
try:a.intersect((0,1),(2,3))
except ValueError:n+=1
else:raise ValueError('empty')
print(json.dumps({'status':'PASS','checks':n,'actual_saved_arithmetic':False}))
