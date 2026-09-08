from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib,time
start=time.monotonic();out=[];checks=0
for p,q,r in [(3,1,2),(5,2,4),(7,3,5),(2,2,2)]:
 def w(s,a):return p if s==a else q if s==(a^1) else r
 beta={}
 for a,b in product(range(6),repeat=2):
  values=[w(s,a)*w(s,b) for s in range(6)];beta[a,b]=[F(x,sum(values)) for x in values]
 tv=lambda u,v:sum(abs(x-y) for x,y in zip(u,v))/2
 c=max(tv(beta[a,b],beta[d,b]) for a,b,d in product(range(6),repeat=3))
 for a,b,d,e in product(range(6),repeat=4):
  if tv(beta[a,b],beta[d,e])>c*((a!=d)+(b!=e)):raise RuntimeError('two-parent coefficient')
  checks+=1
 alpha=2*c;depth={(i,0):F(1) for i in range(25)}|{(0,j):F(1) for j in range(25)}
 for i in range(1,25):
  for j in range(1,25):
   depth[i,j]=c*(depth[i-1,j]+depth[i,j-1])
   if depth[i,j]>alpha**min(i,j):raise RuntimeError('depth bound')
   checks+=1
 out.append({'weights':[p,q,r],'one_parent_TV':str(c),'branch_sum':str(alpha),'upper_TV_depth10':str(alpha**10),'recursion_depth10':str(depth[10,10])})
if [x['one_parent_TV'] for x in out]!=['30/143','65/434','910/5609','0']:raise RuntimeError('coefficient')
p=Path(__file__).resolve();result={'status':'PASS','checks':checks,'results':out,'seconds':time.monotonic()-start,'source_sha':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Exact local coefficient and deterministic recursion only, no stochastic production or global Gibbs uniqueness.'};(p.parent/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
