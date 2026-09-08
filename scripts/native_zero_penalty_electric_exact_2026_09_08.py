from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import json,time,signal
if __name__=='__main__':signal.alarm(180)
start=time.monotonic();n=0
def need(c,m):
 global n
 if not c:raise RuntimeError(m)
 n+=1
L=4;vs=list(product(range(L),repeat=3));ix={v:i for i,v in enumerate(vs)};edges=[]
for v in vs:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%L;edges.append((ix[v],ix[tuple(w)]))
adj=[[] for _ in vs]
for e,(a,b) in enumerate(edges):adj[a].append((b,e));adj[b].append((a,e))
for at in adj:
 for (_,e),(_,f) in combinations(at,2):
  seen={0};todo=[0]
  for v in todo:
   for u,k in adj[v]:
    if k not in (e,f) and u not in seen:seen.add(u);todo.append(u)
  need(len(seen)==64,'every incident pair noncut')
# Exact compressed D in X-link gauge quotient. No CAR or author code needed.
rows=[]
for name,v,ed in [('square',4,[(0,1),(1,2),(2,3),(0,3)]),('K4',4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])]:
 cuts={}
 for S in range(1<<(v-1)):
  mask=sum(1<<e for e,(a,b) in enumerate(ed) if ((S>>a)&1)!=((S>>b)&1));cuts[mask]=S
 pairterms=[(1<<e)|(1<<f) for a in range(v) for e,f in combinations([e for e,ab in enumerate(ed) if a in ab],2)]
 vals=[]
 for occ in range(1<<v):
  if occ.bit_count()%2:continue
  vals.append(F(len(ed),2)+sum((F((-1)**((cuts[m]&occ).bit_count()),2) for m in pairterms if m in cuts),F(0)))
 need((len(set(vals))>1)==(name=='square'),'cut exceptions nonscalar')
 if name=='K4':need(set(vals)=={F(3)},'K4 scalar E/2')
 rows.append({'graph':name,'diagonal_fixed_flux_values':list(map(str,vals)),'off_flux_pair_terms':sum(m not in cuts for m in pairterms)})
need(rows[1]['off_flux_pair_terms']>0,'not all D scalar')
out={'checks':n,'rows':rows,'seconds':time.monotonic()-start,'scope':'actual L4 all960 incident-pair deletions and exact small-graph gauge-parity compressions; no sampling'}
if __name__=='__main__':print(json.dumps(out,indent=2))
