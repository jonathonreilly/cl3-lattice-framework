import sys,json
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path('/private/tmp/toe-24h-probes-20260908/native-omega79-catalog-supplier-design')))
import compute
n=0
for r,target,cap in[(3,F(1,10**22),15000000),(4,F(1,10**20),800000000)]:
 eps=F(1,2**64);R=F(136,3)*12**r/4**52;low=F(17,60)*eps**(2*r+3)/(2*r+3);hi=F(12**(r+41),81*8**81)
 assert F(2,3)*(target+2*R+low+hi)+F(1,10**32)<target;n+=1
 assert F(8**(2*r+3),2*r+3)+1<cap;n+=1
 # Synthetic point masses X=1,2,3 only; no native moment computation.
 for x in [F(1),F(2),F(3)]:
  m={j:x**j for j in range(46)}
  for t in [F(1,4),F(1),F(3)]:
   node={'t_interval':(t,t),'A_interval':(1/(x+t*t),1/(x+t*t)),'weight_interval':(F(1),F(1))}
   q,_,_=compute.node_value(node,r,m);truth=x**(r+1)/(x+t*t);assert q[0]<=truth<=q[1];n+=1
try:compute.moment(3);raise AssertionError('old moment recomputed')
except ValueError:n+=1
print(json.dumps({'status':'PASS','predicates':n,'native_moments_or_catalog_loaded':0,'new_M44_M45_evaluated':False}))
