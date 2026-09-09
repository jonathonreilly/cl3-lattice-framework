import sys,importlib.util,json
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
for name in ('envelope','transport','fp_guard','validate_coefficients','review'):
 s=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m)
import review as r
import numpy as np
checks=0
for p in (0,1):
 x=np.array([F(i-3,8) for i in range(8)],dtype=float)
 for j in range(4):
  for kind in ('A','B'):
   want=np.zeros(8)
   for i,v in enumerate(x):
    bits=i|(((i.bit_count()&1)^p)<<3);sg=(-1)**((bits&((1<<j)-1)).bit_count())
    if kind=='B':sg*=2*((bits>>j)&1)-1
    target=(bits^(1<<j))&7;want[target]+=v*sg
   r.same(r.linear(x,p,[(j,1.)],kind),want);checks+=1
 _,b=r.norm(x,p);expected=[F(0)]*22
 for i,v in enumerate(x):expected[i.bit_count()+((i.bit_count()&1)^p)]+=F(float(v))**2
 if [F(z,1<<2148) for z in b]!=expected:raise ValueError('norm')
 checks+=1
for value in (float.fromhex('0x0.0000000000001p-1022'),-0.,float.fromhex('0x1.fffffffffffffp+1023')):
 _,b=r.norm(np.array([value]),0)
 if F(sum(b),1<<2148)!=F(value)**2:raise ValueError('dyadic extreme')
 checks+=1
try:r.same(np.array([0.]),np.array([-0.]));raise RuntimeError('survived signedzero')
except ValueError:checks+=1
print(json.dumps({'status':'PASS','predicates':checks,'physical_calls':0}))
