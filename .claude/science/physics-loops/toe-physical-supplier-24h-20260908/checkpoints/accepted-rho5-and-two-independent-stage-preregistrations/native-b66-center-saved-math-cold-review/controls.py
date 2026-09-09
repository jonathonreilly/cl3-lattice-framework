from pathlib import Path
from fractions import Fraction as F
import types,json
p=Path('/private/tmp/toe-24h-probes-20260908/native-b66-center-saved-independent-design/arithmetic.py');a=types.ModuleType('candidate');exec(compile(p.read_bytes(),str(p),'exec'),a.__dict__)
n=0
def ck(x):
 global n
 assert x;n+=1
for s in [F(1,2),F(1),F(2)]:
 for t in [F(1,4),F(3,2),F(3)]:
  for x in [F(1),F(3),F(7)]:
   A=1/(x+t*t);As=1/(x+s*s);Ap=-2*s/(x+s*s)**2;w=F(7,13)
   got=a.weighted(s,(t,t),(A,A),(As,As),(Ap,Ap),(w,w))
   ck(got==(a.fl(w*x/((x+s*s)*(x+t*t))),a.fl(w*2*s*x/((x+s*s)**2*(x+t*t)))))
 # Single-atom moments, not actual native M0..40.
 x=F(3);As=1/(x+s*s);Ap=-2*s/(x+s*s)**2;M=[x**j for j in range(41)];lo,hi=a.tails(s,(As,As),(Ap,Ap),M)
 g=sum((F((-1)**j,(2*j+1)*8**(2*j+1))*x**(j+1)/(x+s*s)for j in range(40)),F(0));h=2*s*g/(x+s*s);rem=F(12**40,81*8**81)
 ck(hi==(a.fl(g+rem/2),a.fl(h+rem/2)))
for x in [F(-7,13),F(-1,3),F(0),F(2,7)]:ck(a.fl(x)<=x<=a.ceil(x)and a.ceil(x)-a.fl(x)<=F(1,2**256))
try:a.weighted(F(1),(F(1,2),F(2)),(F(0),F(1)),(F(0),F(1)),(F(-1),F(0)),(F(1),F(1)))
except ValueError:ck(True)
else:raise AssertionError('singularity')
print(json.dumps({'status':'PASS','predicates':n,'scope':'single atom synthetic G/H and forty-term synthetic-tail identity; no native moments or accepted values'}))
