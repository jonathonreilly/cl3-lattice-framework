from pathlib import Path
from fractions import Fraction as F
import types,json
P=Path('/private/tmp/toe-24h-probes-20260908/native-spectral-residual-root-review/schema.py');m=types.ModuleType('schema');exec(compile(P.read_bytes(),str(P),'exec'),m.__dict__);n=0
for x in [F(1,2),F(1),F(2),F(8)]:
 t,status=m.proposed_tau([(F(1),F(1)),(x,x),(x*x,x*x)]);assert t==x and status=='PROPOSED';n+=1
v=F(1)+F(1,2**4200);assert m.proposed_tau([(v,v)]*3)==(F(1),'FALLBACK_FIXED_ONE');n+=1
assert m.proposed_tau([(F(0),F(0))]*3)==(F(1),'PROPOSED');n+=1
assert not m.legal_prefix(['bad']);n+=1
print(json.dumps({'checks':n,'scope':'synthetic proposal and grammar only','actual_values':0}))
