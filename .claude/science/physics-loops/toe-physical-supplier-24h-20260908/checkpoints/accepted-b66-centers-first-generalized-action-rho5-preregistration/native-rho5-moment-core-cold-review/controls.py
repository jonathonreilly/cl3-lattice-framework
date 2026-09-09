from pathlib import Path
from fractions import Fraction as F
import json
p=Path('/private/tmp/toe-24h-probes-20260908/native-rho5-moment-recertification-design');d={};exec(compile((p/'core.py').read_bytes(),str(p/'core.py'),'exec'),d);n=0
for k in ('cminus','mu','nu'):
 assert 0<d['RAD5'][k]<d['RAD4'][k];n+=1
 for x in (F(-3),F(2)):
  old=d['finish']((x,x+F(1,7)),(F(1,11),F(1,10)),(F(1,13),F(1,17)),(F(31415,10000),F(31416,10000)),d['RAD4'][k])
  new=d['finish']((x,x+F(1,7)),(F(1,11),F(1,10)),(F(1,13),F(1,17)),(F(31415,10000),F(31416,10000)),d['RAD5'][k])
  assert old[0]<=new[0]<=new[1]<=old[1];n+=1
# Exact nesting can degenerate to equality under outward rounding; no strict gain claim.
assert d['rounded']((F(0),F(0)))==(0,0);n+=1
print(json.dumps({'synthetic_predicates':n,'moment_calls':0,'native_calls':0}))
