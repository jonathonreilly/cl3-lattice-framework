# Independent single-atom identities, never a native moment/catalog call.
import pathlib,importlib.util,json
from fractions import Fraction as F
p=pathlib.Path('/private/tmp/toe-24h-probes-20260908/native-omega79-root-review/schema.py');sp=importlib.util.spec_from_file_location('schema',p);s=importlib.util.module_from_spec(sp);sp.loader.exec_module(s);n=0
for x in [F(2),F(5)]:
 for t in [F(1,2),F(3,4)]:
  for r in [3,4]:
   m={j:x**j for j in range(46)};a=F(1)/(x+t*t);q,v,p=s.node((t,t),(a,a),(F(1,8),F(1,8)),r,m);truth=x**(r+1)/(x+t*t);assert q[0]<=truth<=q[1];assert v[0]<=truth/8<=v[1];n+=2
# Exact signed rounding including negative rationals.
for x in [F(-1,3),F(1,7),F(-2),F(0)]:
 lo,hi=s.rounding((x,x));assert lo<=x<=hi and hi-lo<=F(1,s.S);n+=1
print(json.dumps({'status':'PASS','checks':n,'native_calls':0,'new_moment_calls':0}))
