from pathlib import Path
from fractions import Fraction as F
import types,sys,json,hashlib
P=Path(__file__).resolve().parent;A=P.parent/'native-elliptic-b-transform-stretch'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1<<20),b''):h.update(z)
 return h.hexdigest()
f=json.loads((A/'FREEZE.json').read_text())
for p,h in f['inputs'].items():
 if sha(Path(p))!=h:raise ValueError('pin '+p)
for name in ('interval_base','elliptic','highorder','core'):
 p=A/(name+'.py');m=types.ModuleType(name);m.__file__=str(p);exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__);sys.modules[name]=m
c=sys.modules['core'];el=sys.modules['elliptic'];g=sys.modules['highorder'];checks=0
def require(b):
 global checks
 checks+=1
 if not b:raise ValueError('predicate '+str(checks))
xs=(F(0),F(3),F(12));ws=(F(1,4),F(1,2),F(1,4))
def avg(f):return sum(w*f(x) for w,x in zip(ws,xs))
# Substitute synthetic moment functional into an isolated in-memory module only.
c.moment=lambda n:avg(lambda x:x**n)
for s in (F(1),F(2)):
 a=avg(lambda x:1/(x+s*s));da=-2*s*avg(lambda x:1/(x+s*s)**2)
 for t in (F(1,3),F(3,2),F(5)):
  at=avg(lambda x:1/(x+t*t));u,v=c.integrands(s,el.const(t),el.const(a),el.const(da),el.const(at))
  ug=avg(lambda x:x/((x+s*s)*(x+t*t)));vh=2*s*avg(lambda x:x/((x+s*s)**2*(x+t*t)))
  require(u[0]<=ug<=u[1]);require(v[0]<=vh<=v[1])
 u,v=c.high_tail(s,el.const(a),el.const(da))
 G=H=F(0)
 for n in range(64):
  weight=F((-1)**n,(2*n+1)*8**(2*n+1))
  C=avg(lambda x:x**(n+1)/(x+s*s));E=2*s*avg(lambda x:x**(n+1)/(x+s*s)**2)
  G+=weight*C;H+=weight*E
 require(u[0]<=G<=u[1]);require(v[0]<=H<=v[1])
# Same Gauss implementation, nonphysical two-node polynomial exactness.
rule=g.gauss(2)
for n in range(4):
 lo=hi=F(0)
 for node,w in rule:
  v=(F(1),F(1))
  for _ in range(n):v=g.mul(v,node)
  z=g.mul(w,v);lo+=z[0];hi+=z[1]
 truth=F(0) if n%2 else F(2,n+1)
 require(lo<=truth<=hi)
# Analytic error allocation, not physical integral.
require(F(2)*1+F(16,9)*2==F(50,9))
require(F(20,3)*F(50,9)==F(1000,27))
require(F(2,3)*F(1000,27)==F(2000,81))
require(F(12,64)<1)
result={'status':'PASS','checks':checks,'verified_pins':len(f['inputs']),'freeze':sha(A/'FREEZE.json'),'physical_B_calls':0,'physical_A_calls':0,'scope':'synthetic three-atom measure with injected moments; generic Gauss2; exact arithmetic budgets'}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
