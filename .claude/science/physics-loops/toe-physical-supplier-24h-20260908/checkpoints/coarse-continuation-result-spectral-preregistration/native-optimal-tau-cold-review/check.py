from pathlib import Path
from fractions import Fraction as F
import types,json
p=Path('/private/tmp/toe-24h-probes-20260908/native-residual-optimal-tau-stretch/proposal.py');m=types.ModuleType('proposal');exec(compile(p.read_text(),str(p),'exec'),m.__dict__)
n=0;d=F(1,4)
for atoms in [[(d,F(2))],[(F(1,2),F(1))],[(F(2),F(3))],[(F(1,2),F(1,3)),(F(3),F(2,3))]]:
 r=[sum(w*x**k for x,w in atoms)for k in range(3)];B,C,D=m.coefficients(r);t=m.propose(r)
 assert d<t<=2**22;n+=1
 assert B+2*C/d+3*D/d**2==8/d**3*sum(w*(x-d)**2 for x,w in atoms);n+=1
 actual=sum(w/x**2 for x,w in atoms);u=m.upper([(x,x)for x in r],t);assert u>=actual;n+=1
 if len(atoms)==1 and atoms[0][0]>d:assert t==atoms[0][0]and u==actual;n+=1
assert m.propose([0,0,0])==1;n+=1
assert m.propose([10,0,-1])==1;n+=1
# Negative rho1 coefficient must use its LOWER endpoint.
ranges=[(F(1),F(2)),(F(1),F(3)),(F(10),F(11))];t=F(2);A=(t+2*d)/(d*d*t**3);B=-2/t**3-2*t*A;C=3/t**2+t*t*A
assert B<0 and m.upper(ranges,t)==A*11+B*1+C*2;n+=1
for t in [F(0),F(-1)]:
 try:m.upper(ranges,t)
 except ValueError:n+=1
 else:raise AssertionError('nonpositive parameter')
print(json.dumps({'status':'PASS','independent_synthetic_predicates':n,'native_calls':0}))
