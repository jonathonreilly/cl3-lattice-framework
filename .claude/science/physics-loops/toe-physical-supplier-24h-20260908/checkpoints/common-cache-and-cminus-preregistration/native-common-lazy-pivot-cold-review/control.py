from pathlib import Path
from fractions import Fraction as F
import types,sys,json
P=Path('/private/tmp/toe-24h-probes-20260908/native-common-lazy-pivot-candidate')
for name in ('interval','pivot'):
 m=types.ModuleType(name);sys.modules[name]=m;exec(compile((P/(name+'.py')).read_bytes(),str(P/(name+'.py')),'exec'),m.__dict__)
iv=sys.modules['interval'];p=sys.modules['pivot'];V=[[F(x) for x in a] for a in [[1,0,0,0],[1,0,1,0],[0,1,0,2],[0,0,0,1]]];chi=[1,1,-1,-1]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F())
def J(v):return [-v[1],v[0],-v[3],v[2]]
def fetch(i,j):return iv.rational(dot(V[i],V[j])),iv.rational(dot(V[i],J(V[j])))
rows=[];result=p.compress(fetch,chi,rows.append);count=0;res=[v[:] for v in V]
for h in result['history']:
 i=h['index'];x=res[i][:];jx=J(x);r=dot(x,x)
 def contains(a,v):
  global count
  if not F(a[0],iv.S)<=v<=F(a[1],iv.S):raise ValueError((a,v))
  count+=1
 contains(h['r'],r)
 for j,y in enumerate(res):contains(h['g'][j],dot(x,y));contains(h['j'][j],dot(x,J(y)))
 res=[[z-dot(x,y)/r*u-dot(jx,y)/r*v for z,u,v in zip(y,x,jx)] for y in res]
if result['status']!='CERTIFIED_COMPRESSION' or any(dot(y,y) for y in res):raise ValueError('final projection')
# An uncertain positive semidefinite diagonal must not be inverted.
r=p.compress(lambda i,j:((0,iv.S),iv.ZERO),[1],lambda _:None)
if r['status']!='PRECISION_STALL':raise ValueError('uncertain pivot')
count+=1
try:p.compress(fetch,chi,lambda _:None,epsilon=F(1,100))
except ValueError:count+=1
else:raise ValueError('changed target accepted')
print(json.dumps({'status':'PASS','predicates':count,'direct_projection_pairs':len(result['history']),'native_calls':0}))
