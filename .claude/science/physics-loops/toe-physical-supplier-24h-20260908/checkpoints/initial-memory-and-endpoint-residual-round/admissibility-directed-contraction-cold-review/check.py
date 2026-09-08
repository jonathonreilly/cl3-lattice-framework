from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import json,hashlib
out=[]
for triple in [(3,1,2),(5,2,4),(7,3,5),(2,2,2)]:
 p,q,r=triple;phi=[[p if a==b else q if a//2==b//2 else r for b in range(6)] for a in range(6)]
 dist={}
 for a,b in product(range(6),repeat=2):
  w=[phi[s][a]*phi[s][b] for s in range(6)];dist[a,b]=[F(z,sum(w)) for z in w]
 c=F(0);arg=None
 for a,d in combinations(range(6),2):
  for b in range(6):
   delta=[x-y for x,y in zip(dist[a,b],dist[d,b])]
   # Supremum over all events, independently of author's L1 computation.
   tv=max(abs(sum(delta[s] for s in range(6) if mask>>s&1)) for mask in range(64))
   if tv>c:c=tv;arg=[a,d,b]
 out.append({'triple':triple,'one_parent_coefficient':str(c),'witness':arg,'branch_sum':str(2*c)})
assert [z['one_parent_coefficient'] for z in out]==['30/143','65/434','910/5609','0']
print(json.dumps({'results':out,'source_sha':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
