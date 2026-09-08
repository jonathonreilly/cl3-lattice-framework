from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,permutations
import json,signal,time
signal.alarm(180);start=time.monotonic();p=Path(__file__).resolve().parent;r=json.loads((p/'PREFIXES.json').read_text());edges=r['edge_order'];cut=r['boundary_edges'];checks=0
def need(c,s):
 global checks
 checks+=1
 if not c:raise RuntimeError(s)
def R(mask,x):
 a=F(3+mask%3);b=F(5+mask.bit_count()%3);det=a*b-1
 return ((b*x[0]-x[1])/det,(-x[0]+a*x[1])/det)
def plus(x,y):return (x[0]+y[0],x[1]+y[1])
counts=[];mock=None
for row in r['rows']:
 bridge=row['bridge_edge'];allowed=sorted(cut+[bridge]);terms=[(a,b) for a,b in combinations(allowed,2) if set(edges[a])&set(edges[b])]
 keys={(int(x['boundary_used_mask']),x['bridge_count']):x for x in row['prefixes']};zero=(0,0);target=(sum(1<<e for e in cut),2)
 cnt={zero:1};val={zero:(F(1),F(2))}
 for k in range(6):
  nc={};nv={}
  for key,n in cnt.items():
   used,c=key
   for a,b in terms:
    bd=[e for e in (a,b) if e!=bridge]
    if any(used>>e&1 for e in bd):continue
    q=(used|sum(1<<e for e in bd),c+((a==bridge)+(b==bridge)))
    if q not in keys:continue
    nc[q]=nc.get(q,0)+n
    if bridge==r['rows'][1]['bridge_edge']:nv[q]=plus(nv.get(q,(0,0)),tuple(x/2 for x in val[key]))
  cnt=nc
  if bridge==r['rows'][1]['bridge_edge']:
   val={q:(x if k==5 else R(int(keys[q]['full_toggle_mask']),x)) for q,x in nv.items()}
 need(cnt[target]==row['unordered_pair_sets']*720,'DP full word count');counts.append(cnt[target])
 if bridge==r['rows'][1]['bridge_edge']:
  # Independently enumerate distinct occurrence matchings and all permutations.
  def pairings(es):
   if not es:return {()}
   a=es[0];out=set()
   for j,b in enumerate(es[1:],1):
    if a==b or not(set(edges[a])&set(edges[b])):continue
    for q in pairings(es[1:j]+es[j+1:]):out.add(tuple(sorted(q+(tuple(sorted((a,b))),))))
   return out
  total=(0,0);wrong=(0,0)
  for pairset in pairings(sorted(cut+[bridge,bridge])):
   for order in permutations(pairset):
    x=(F(1),F(2));y=x;mask=0
    for j,(a,b) in enumerate(order):
     prev=mask;mask^=(1<<a)^(1<<b);x=tuple(v/2 for v in x);y=tuple(v/2 for v in y)
     if j<5:x=R(mask,x);y=R(prev,y)
    total=plus(total,x);wrong=plus(wrong,y)
  need(val[target]==total,'complete noncommuting resolvent mock');need(wrong!=total,'wrong prefix-resolvent adverse')
  mock={'bridge':bridge,'result':list(map(str,total)),'wrong_prefix_differs':True}
print(json.dumps({'checks':checks,'PASS':True,'word_counts':counts,'mock':mock,'seconds':time.monotonic()-start,'scope':'Exact two-dimensional mock and full incidence-DP count; no physical coefficient'},indent=2))
