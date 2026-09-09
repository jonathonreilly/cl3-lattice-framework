from pathlib import Path
import json,hashlib,math
from fractions import Fraction as F
from math import factorial
s=Path('/private/tmp/toe-24h-probes-20260908');p=s/'native-highprecision-b-catalog-design';checks=0
def req(x):
 global checks
 if not x:raise ValueError(checks)
 checks+=1
def sha(x):return hashlib.sha256(x.read_bytes()).hexdigest()
f=json.loads((p/'FREEZE.json').read_text());req(sha(p/'FREEZE.json')=='c643064136e292c84c06ffdcb72160bb2fbf86db7e863416cf94f43c4a1dd1c6')
for k,v in f['inputs'].items():req(Path(k).is_file() and sha(Path(k))==v)
for name in ('elliptic.py','interval_base.py'):req((p/name).read_bytes()==(s/'native-elliptic-b-transform-stretch'/name).read_bytes())
req((p/'highorder.py').read_bytes()==(s/'native-stationary-pole-scalar-batch-design/highorder.py').read_bytes())
g=json.loads((p/'CATALOG_GEOMETRY.json').read_text());ps=json.loads((s/'native-stationary-pole-scalar-batch-design/POLES.json').read_text())['rows'];req(len(g['nodes'])==1742 and len(g['endpoints'])==3484);req(len({x['s'] for x in g['endpoints']})==3484)
coef=[F((-1)**k*factorial(52-2*k),2**26*factorial(k)*factorial(26-k)*factorial(26-2*k)) for k in range(14)]
def poly(x):return sum(c*x**(26-2*k) for k,c in enumerate(coef))
roots=[];prev=F(-1)
for n in g['nodes'][:26]:
 a=F(2)**n['panel'];lo,hi=map(F,n['t_interval']);x,y=2*lo/a-3,2*hi/a-3;req(prev<x<y<1 and y-x<=F(1,2**160) and poly(x)*poly(y)<0);prev=y;roots.append((x,y))
sep=None
for i,n in enumerate(g['nodes']):
 req((n['id'],n['panel'],n['root'])==(i,i//26-64,i%26));a=F(2)**n['panel'];lo,hi=map(F,n['t_interval']);x,y=roots[i%26];req((lo,hi)==(a*(x+3)/2,a*(y+3)/2));req(n['endpoint_ids']==[2*i,2*i+1]);dist=[]
 for r in ps:
  l,h=map(F,r['s_interval']);d=max(lo-h,l-hi);req(d>0);dist.append(d)
 req(min(dist)==F(n['minimum_stationary_separation']));sep=min(dist+[sep]) if sep is not None else min(dist)
 for z,side,t in [(2*i,'lower',lo),(2*i+1,'upper',hi)]:req(g['endpoints'][z]=={'id':z,'node_id':i,'side':side,'s':str(t)})
req(sep==F(g['minimum_separation']) and g['separation_predicates']==114972)
times=[json.loads(x.read_text())['seconds'] for x in (s/'native-elliptic-b-run-76350/ORACLES').glob('*.json')];req(len(times)==746 and all(math.isfinite(t) and t>0 for t in times));forecast=10+3*3484*max(times);req(forecast<180)
print(json.dumps({'status':'PASS_SAVED_GEOMETRY_SOURCE','checks':checks,'separations':114972,'forecast':forecast,'physical_calls':0,'source_freeze':sha(p/'FREEZE.json')},indent=2))
