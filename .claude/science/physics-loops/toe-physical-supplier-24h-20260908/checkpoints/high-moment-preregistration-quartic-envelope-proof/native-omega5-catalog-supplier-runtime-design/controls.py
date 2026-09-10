from fractions import Fraction as F
import json
from compute import moment,node_value
from pi import pi_bounds
checks=0
def ok(x):
 global checks
 if not x:raise AssertionError(checks)
 checks+=1
for n,x in enumerate([1,6,42,324]):ok(moment(n)==x)
e=F(1,2**64);R=F(1904,4**52);rem=F(12**43,81*8**81)
pi=pi_bounds();ok(pi[0]>3)
ok(F(2,3)*(F(1,10**24)+2*R+F(17,60)*e**7/7+rem)+F(1,10**35)<F(1,10**24))
ok(F(8**7,7)<299594)
ok(9*6*8**5*F(1,2**140)+1742*8**6*(F(1,10**38)+F(2,2**192))<1)
ok(300000*F(3,10**30)+9*2**17*F(1,2**140)+1742*43*(F(1,10**38)+F(2,2**192))+F(1,10**43)<F(1,10**24))
ok(25000*2**24*F(2,2**192)<F(1,10**43))
# Literal single-atom polynomial-division identity, independent of catalog.
for X in [F(1),F(2),F(7)]:
 for t in [F(1,3),F(2)]:
  exact=X*X-t*t*X+t**4-t**6/(X+t*t)
  ok(exact==X**3/(X+t*t))
# Small synthetic node verifies implementation's fixed42/6 polynomial only.
node={'t_interval':(F(1),F(1)),'A_interval':(F(1,7),F(1,7)),'weight_interval':(F(1,2),F(1,2))}
q,weighted,power=node_value(node);truth=42-6+1-F(1,7)
ok(q[0]<=truth<=q[1]);ok(weighted[0]<=truth/2<=weighted[1]);ok(power==(F(1,2),F(1,2)))
# Reversed low correction and missing factorX falsifiers.
ok(42*e-2*e**3+e**5/5-F(17,60)*e**7/7 <42*e-2*e**3+e**5/5)
ok(F(2)**3/(2+F(1,3)**2)!=F(2)**2/(2+F(1,3)**2))
print(json.dumps({'status':'PASS_SYNTHETIC_AND_ANALYTIC_BUDGET_ONLY','checks':checks,'max_moment_degree_evaluated':3,'catalog_calls':0,'omega5_evaluations':0},indent=2))
