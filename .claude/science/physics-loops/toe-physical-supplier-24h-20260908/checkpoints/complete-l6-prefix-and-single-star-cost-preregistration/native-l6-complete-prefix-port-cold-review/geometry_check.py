from pathlib import Path
from fractions import Fraction as F
import json
p=Path('/private/tmp/toe-24h-probes-20260908/native-l6-complete-prefix-gap-port');o=Path(__file__).parent;read=lambda n:json.loads((p/n).read_text());a=read('ADJACENT_CENSUS.json');b=read('NONADJACENT_PLAN.json');targets=read('TARGETS.json')['cases'];cost=read('COST_PLAN.json')['cases'];by={x['mask']:x for x in targets};checks=0
am={x['mask'] for r in a['rows'] for x in r['prefixes']};bm={x['mask'] for x in b['cases']}
def ck(x):
 global checks
 if not x:raise ValueError('geometry')
 checks+=1
ck(len(am)==1534 and len(bm)==4986 and len(am&bm)==31 and len(am|bm)==6489);ck(set(by)==am|bm and len(targets)==6489)
for c in targets:
 es=[a['edges'][e] for e in range(648) if int(c['mask'])>>e&1];res=[e for e in es if 0 not in e and c['center'] not in e];ck(len(res)<=1);ck(F(c['gap_lower'])>F(1,3))
sizes={}
for r in a['rows']:
 cases=[c for c in cost if c['bridge']==r['bridge']];ck(len(cases)==5);eligible=sorted({x['mask'] for x in r['prefixes'] if (r['bridge']==0 or x['bridge_count']%2==1) and by[x['mask']]['singleton'] is None},key=int);ck([c['mask'] for c in cases]==eligible[:5])
 for c in cases:
  res=[a['edges'][e] for e in range(648) if int(c['mask'])>>e&1 and 0 not in a['edges'][e] and 36 not in a['edges'][e]];ck(len(res)==(0 if r['bridge']==0 else 1))
 sizes[str(r['bridge'])]=len(cases)
print(json.dumps({'status':'PASS','predicates':checks,'union':6489,'overlap':31,'cost_bridge_counts':sizes,'scope':'literal residual-support and exact saved-bound comparisons, no baseline/gap call'},indent=2))
