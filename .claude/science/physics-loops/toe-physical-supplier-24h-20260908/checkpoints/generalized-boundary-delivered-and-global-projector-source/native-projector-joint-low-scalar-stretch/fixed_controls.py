from fractions import Fraction as F
import json
quad=F(640,3)*2**64*F(1,25)**32
high=F(2,3)*F(12**19,41*16**41)
low=F(1,2**80)
node=F(32,3)*F(1,10**24)
extra=F(1,10**23)
assert low+quad+high+node+extra<F(1,10**21)
assert 7*F(1,2**96)<F(1,10**27)
# Finite atomic measure: exact divided difference and confluence, no native data.
for x in [F(1,3),F(2),F(7)]:
 for s,t in [(F(1,2),F(3,4)),(F(2),F(2))]:
  k=1/((x+s*s)*(x+t*t))
  if s!=t: assert k==(1/(x+t*t)-1/(x+s*s))/(s*s-t*t)
  else: assert k==(2*s/(x+s*s)**2)/(2*s)
print(json.dumps({'scope':'rational budgets and synthetic atomic identities only','radius_bound':str(low+quad+high+node+extra),'display':float(low+quad+high+node+extra),'nodes_per_pole':84*32,'unshared_nodes':378*84*32},indent=2))
