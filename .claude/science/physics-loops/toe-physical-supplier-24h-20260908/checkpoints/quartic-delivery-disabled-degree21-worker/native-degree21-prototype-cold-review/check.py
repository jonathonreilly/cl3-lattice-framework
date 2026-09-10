from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
sys.dont_write_bytecode=True
p=Path('/private/tmp/toe-24h-probes-20260908/native-degree21-masked-jet-prototype');sys.path.insert(0,str(p))
import assembly as A, arithmetic as a, tables,core
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert h(p/'SOURCE_FREEZE.json')=='efc0533462690b58fedd46391378677e95824e05a9b37a1d3c54c31aef6a8cdc'
f=json.loads((p/'SOURCE_FREEZE.json').read_text())
for n,v in f.items():assert h(p/n)==v,n
checks=0
def enclosed(b,x):
 global checks
 assert F(b[0][0],a.S)<=x<=F(b[0][1],a.S) and b[1][0]<=0<=b[1][1];checks+=1
# Independent finite positive spectral measure, not native inputs.
xs=[F(1,4),F(3,2),F(7)];weights=[F(2,7),F(3,7),F(2,7)]
s=[sum(w*x**k for x,w in zip(xs,weights)) for k in range(5)]
boxes=[a.point(x.numerator,x.denominator) for x in s]
for q in [(F(0),F(0)),(F(2,3),F(-1,5)),(F(-2),F(3,7)),(F(1),F(1))]:
 e,b=A.forms(boxes,q)
 enclosed(e,sum(w*(1-x*(q[0]+q[1]*x))**2 for x,w in zip(xs,weights)))
 enclosed(b,sum(w*(q[0]+q[1]*x)**2 for x,w in zip(xs,weights)))
# Constant and linear marker coefficients must retain opposite z signs.
jet={(i,j,k,w):a.point(1+3*i+7*j+11*k+13*w)for i in range(3)for j in range(3)for k in range(2)for w in range(2)}
from math import factorial
pc=[F(1,2),F(-2,3),F(3,5)];pa=[F(-1,3),F(2,5),F(4,7)];q=(F(2,3),F(-5,7))
x=sum(pc[i]*pa[j]*(-1)**(i+j)*factorial(i)*factorial(j)*((1+3*i+7*j)+q[0]*(14+3*i+7*j)-q[1]*(25+3*i+7*j))for i in range(3)for j in range(3))
enclosed(A.nominal(jet,pc,pa,q),x)
# Every shifted table query stays within proven radial degree; no radial values acquired.
for kind in ['P','O']:
 seen=[]
 def R(n):seen.append(n);return a.point(1)
 for T in tables.inner(R,kind):
  for n in range(7):
   for i in range(3):
    for j in range(3):T(n,i,j)
 assert max(seen)<=10 and max(n for n in seen if n%2)<=9;checks+=1
for l,r,o,_ in A.SIGNATURES:
 seen=[]
 def R(n):seen.append(n);return a.point(1)
 for T in tables.nominal(R,l,r,o):
  for n in range(5):
   for i in range(4):
    for j in range(4):T(n,i,j)
 assert max(seen)==6 and max(n for n in seen if n%2)==5;checks+=1
assert sum(x[3]for x in A.SIGNATURES)==90;checks+=1
print(json.dumps({'status':'PASS_SOURCE_SYNTHETIC_ONLY','checks':checks,'source_pins':len(f),'native_calls':0,'full_jet_runs':0}))
