import json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
p=Path('/private/tmp/toe-24h-probes-20260908/native-stationary-pole-scalar-batch-design');b=Path('/private/tmp/toe-24h-probes-20260908/native-elliptic-b-run-76350');f=json.loads((p/'FREEZE.json').read_text());checks=0
def req(x):
 global checks
 if not x:raise ValueError('check '+str(checks))
 checks+=1
def sha(x):return hashlib.sha256(x.read_bytes()).hexdigest()
req(sha(p/'FREEZE.json')=='9845c5473716c7477c0833e9741b531dda4f80ff74ece0c0f16a8e515a7c043d')
for k,v in f['inputs'].items():req(sha(Path(k))==v)
d=json.loads((p/'POLES.json').read_text());req(len(d['rows'])==66);rule=json.loads((b/'GAUSS.json').read_text())['rule'];cs=[]
for j in range(-28,3):
 for x,w in rule:cs.append(tuple(F(2)**j*(3+F(z))/2 for z in x))
P6=lambda x:(231*x**6-315*x**4+105*x*x-5)/16
sep=None
for i,r in enumerate(d['rows']):
 req((r['id'],r['panel'],r['root'])==(i,i//6-7,i%6));lo,hi=map(F,r['s_interval']);a=F(2)**r['panel'];x,y=2*lo/a-3,2*hi/a-3
 req(-1<x<y<1 and y-x<=F(1,2**160) and P6(x)*P6(y)<0);req(F(r['s_midpoint'])==(lo+hi)/2)
 req(F(r['A_midpoint_inflation'])==(hi-lo)/6);req(F(r['Aprime_midpoint_inflation'])==3*(hi-lo)/lo**4)
 distances=[]
 for cl,ch in cs:
  z=max(lo-ch,cl-hi);req(z>0);distances.append(z)
 req(F(r['minimum_catalog_separation'])==min(distances));sep=min(distances+[sep]) if sep is not None else min(distances)
req(sep==F(d['minimum_separation']));req(d['separation_predicates']==66*372)
times=[json.loads(x.read_text())['seconds'] for x in (b/'ORACLES').glob('*.json')];req(len(times)==746 and all(math.isfinite(x) and x>0 for x in times));forecast=10+3*66*max(times);req(forecast<30)
print(json.dumps({'status':'PASS_EXACT_SAVED_GEOMETRY','checks':checks,'separations':24552,'minimum_separation':str(sep),'oracle_prior_max':max(times),'forecast_seconds':forecast,'oracle_calls':0,'source_freeze':sha(p/'FREEZE.json')},indent=2))
