"""Fixed synthetic controls only; no 378-node assembly or physical acquisition."""
from fractions import Fraction as F
import json
import core as c
checks=0

def ok(x):
 global checks
 if not x: raise AssertionError('synthetic control')
 checks+=1

def refused(fn):
 try: fn()
 except ValueError: ok(True)
 else: ok(False)

for s in (F(1,8),F(1),F(3)):
 # Deliberately synthetic one-atom scalar law X=6, not the native measure.
 A=1/(6+s*s)
 for kind in ('P','O'):
  events=[]
  Q,err=c.coefficient(s,(A,A),kind,lambda k,v:events.append((k,v)))
  ok(err<=F(1,2**80));ok(len(events)==2)
  for pol in ('positive','negative'):
   C=c.block_imaginary(Q,F(2,7),F(7,22),pol)
   ok(all(C[i][j]==-C[j][i] for i in range(4) for j in range(4)))
  Cp=c.block_imaginary(Q,F(2,7),F(7,22),'positive')
  Cn=c.block_imaginary(Q,F(2,7),F(7,22),'negative')
  ok(all(Cp[i][j]==-Cn[i][j] for i in range(4) for j in range(4)))
  # Check explicit inverse through alternate2x2 determinant inversion.
  D=(1-s*s*A)/6;B=A if kind=='P' else D;a=1-4*D
  K=[[a,-4*s*B],[2*s*A,a]]
  det=K[0][0]*K[1][1]-K[0][1]*K[1][0]
  inv=[[K[1][1]/det,-K[0][1]/det],[-K[1][0]/det,K[0][0]/det]]
  exact=events[1][1]['Q']
  ok(c.mul(inv,[[F(0),F(2)],[F(-2),F(0)]])==exact)
for x in (F(-7,3),F(-1,2**85),F(0),F(1,2**85),F(9,7)):
 ok(abs(c.quantize(x)-x)<=F(1,2**85))
refused(lambda:c.interval((F(1),F(0))))
refused(lambda:c.interval((True,F(1))))
refused(lambda:c.coefficient(F(1),(F(0),F(1)),'P',lambda *args:None))
refused(lambda:c.assemble([], (F(1,4),F(1,4)),lambda *args:None))
refused(lambda:c.bounded(F(2**32769)))
q=[[F(1),F(2)],[F(3),F(4)]]
C=c.block_imaginary(q,F(1),F(1,4),'positive')
ok(C[0][2]==-F(1,8));ok(C[2][0]==F(1,8))
analytic=sum(c.analytic_budget().values(),F(0))
input_bound=2**27*F(1,10**30)+2**42*F(1,2**160)+2**13*F(1,2**160)+5*F(1,2**80)+2**12*F(1,2**180)
ok(analytic<F(2,10**13));ok(analytic+input_bound<F(1,10**12))
print(json.dumps(dict(status='PASS',checks=checks,scope='synthetic one-atom coefficient and rational budget controls only',native_calls=0,full_assembly_calls=0),indent=2))
