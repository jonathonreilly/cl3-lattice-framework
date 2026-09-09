from fractions import Fraction as F
from math import comb, factorial
import json, time, signal
from pathlib import Path
signal.alarm(50)
t=time.monotonic(); checks=0
def require(v):
 global checks
 if not v: raise ValueError('independent check failed')
 checks+=1
root=Path('/private/tmp/toe-24h-probes-20260908/native-infinite-star-node-stretch')
ref=json.loads((root/'IMPURITY_GAP_CONTROL.json').read_text())
# Multinomial-square identity summed by one coordinate, unlike author's three factorial loops.
s=F(0)
for n in range(101):
 s+=F(comb(2*n,n)*sum(comb(n,a)**2*comb(2*(n-a),n-a) for a in range(n+1)),6**(2*n))
require(s==F(ref['return_partial_exact']));require(s<F(3,2))
a=F(17,60); c=[F(8,9),-(4*a/9+8*a*a),-4*a*a/9]
# Direct trinomial integration, no iterative polynomial convolution.
integ=F(0)
for n in range(1,13):
 for j in range(n+1):
  for k in range(n-j+1):
   i=n-j-k
   integ+=F(comb(n,j)*comb(n-j,k),n*(2*j+4*k+1))*c[0]**i*c[1]**j*c[2]**k
lower=F(7,44)*integ
require(lower==F(ref['gap_lower_exact']));require(lower>F(1,6));require(sum(c)>0)
require(F(27)*F(22,7)**3<F(1024));require(F(400)>F(343)) # opposite >1/5 by squaring
for u in [F(1,3),F(1),F(7),F(100)]:
 z=(u+1)/(u+7)
 require((1+2*z)**2/9+8*z*z/u==1-(24-8/u)/(u+7)**2)
# Rank-two determinant, using c=-sqrt(2)D and beta=2sqrt(2), with sqrt(2) represented by a 2D exact field.
# Algebraic product beta*c=-4D and beta²=8; expand determinant independently.
for D in [F(0),F(1,12),F(1,6)]:
 for aa,bb in [(F(2,3),F(1,4)),(F(1,9),F(7,8))]:
  det=(1-4*D)*(1-4*D)-(-8*aa*bb)
  require(det==(1-4*D)**2+8*aa*bb)
delta=F(1,6); T=160; beta=3
exp_lower=sum((delta*T)**n/F(factorial(n)) for n in range(161))
tail=F(90,8)*(2/delta**2+beta*T/delta**2+2*beta/delta**3)/exp_lower
require(tail<F(1,10**6));require(tail==F(json.loads((root/'IMPROVED_TAIL_CONTROL.json').read_text())['tail_exact_upper']))
print(json.dumps({'checks':checks,'partial':str(s),'gap_lower':str(lower),'tail_upper':str(tail),'seconds':time.monotonic()-t,'physical_runs':0},indent=2))
