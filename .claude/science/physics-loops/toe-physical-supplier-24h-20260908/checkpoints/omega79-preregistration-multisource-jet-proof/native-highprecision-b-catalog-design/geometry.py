"""Fixed p26 catalog geometry. Exact Legendre arithmetic, no physical oracle."""
import json,hashlib,types,sys
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
for name in ('interval_base','highorder'):
 p=P/(name+'.py');m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(p.read_bytes(),str(p),'exec'),m.__dict__)
rule=sys.modules['highorder'].gauss(26)
pp=Path('/private/tmp/toe-24h-probes-20260908/native-stationary-pole-scalar-batch-design/POLES.json')
poles=json.loads(pp.read_text())['rows'];nodes=[];endpoints=[];checks=0;sep=None
for j in range(-64,3):
 for i,(x,w) in enumerate(rule):
  a=F(2)**j;lo=a*(x[0]+3)/2;hi=a*(x[1]+3)/2;weight=[str(a*z/2) for z in w]
  local=None
  for p in poles:
   pl,ph=map(F,p['s_interval']);d=max(lo-ph,pl-hi)
   if d<=0:raise ValueError(('collision',j,i,p['id']))
   local=d if local is None else min(local,d);checks+=1
  sep=local if sep is None else min(sep,local)
  node={'id':len(nodes),'panel':j,'root':i,'t_interval':[str(lo),str(hi)],'weight':weight,'minimum_stationary_separation':str(local),'endpoint_ids':[len(endpoints),len(endpoints)+1]}
  nodes.append(node)
  for side,t in [('lower',lo),('upper',hi)]:endpoints.append({'id':len(endpoints),'node_id':node['id'],'side':side,'s':str(t)})
if len(endpoints)!=3484 or len({p['s'] for p in endpoints})!=3484:raise ValueError('endpoint census')
result={'scope':'exact root geometry only; no A/B oracle','p':26,'root_bracket_bits':160,'panels':[-64,2],'nodes':nodes,'endpoints':endpoints,'separation_predicates':checks,'minimum_separation':str(sep),'minimum_separation_decimal':float(sep),'stationary_poles_sha256':hashlib.sha256(pp.read_bytes()).hexdigest()}
(P/'CATALOG_GEOMETRY.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('nodes','endpoints')},indent=2))
