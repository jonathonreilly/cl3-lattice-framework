from fractions import Fraction as F
from pathlib import Path
import types
p=Path('/private/tmp/toe-24h-probes-20260908/native-rho4-b66-feasibility-design/ledger.py');m=types.ModuleType('ledger');exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__)
n=0
for s in(F(1),F(3)):
 for t in(F(1,2),F(2)):
  X=F(5);As=1/(X+s*s);At=1/(X+t*t);Ap=-2*s/(X+s*s)**2;d=t*t-s*s
  assert t*t/d*At-s*s/d*As==X/((X+s*s)*(X+t*t));n+=1
  assert 2*s*t*t*(As-At)/d**2+s*s*Ap/d==2*s*X/((X+s*s)**2*(X+t*t));n+=1
  rad,_=m.node(s,(t,t),(At,At),(As,As),(Ap,Ap),(F(1),F(1)));assert rad==(0,0);n+=1
print({'status':'PASS_SINGLE_ATOM','checks':n,'actual_catalog_calls':0})
