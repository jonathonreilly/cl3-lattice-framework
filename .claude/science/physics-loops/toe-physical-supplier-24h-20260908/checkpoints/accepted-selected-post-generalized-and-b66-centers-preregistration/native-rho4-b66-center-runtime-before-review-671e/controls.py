from fractions import Fraction as F
import core as c
n=0
def check(x):
 global n
 if not x:raise ValueError(n)
 n+=1
for x in(F(1,3),F(2),F(9)):
 for s,t in[(F(1),F(2)),(F(2),F(1)),(F(1,2),F(3))]:
  A=1/(x+s*s);Ap=-2*s/(x+s*s)**2;At=1/(x+t*t);g,h=c.center(s,(t,t),(At,At),(A,A),(Ap,Ap),(F(1),F(1)))
  exactg=x/((x+s*s)*(x+t*t));exacth=2*s*x/((x+s*s)**2*(x+t*t))
  check(g<=exactg<g+F(1,c.S));check(h<=exacth<h+F(1,c.S))
try:c.center(F(1),(F(1),F(1)),(F(1),F(1)),(F(1),F(1)),(F(-1),F(-1)),(F(1),F(1)))
except ValueError:check(True)
else:check(False)
check(F(1744,c.S)<F(1,10**35))
print(__import__('json').dumps({'status':'PASS_SINGLE_ATOM_CENTER_IDENTITIES','checks':n,'native_nodes':0,'moment40_calls':0,'tail40_calls':0}))
