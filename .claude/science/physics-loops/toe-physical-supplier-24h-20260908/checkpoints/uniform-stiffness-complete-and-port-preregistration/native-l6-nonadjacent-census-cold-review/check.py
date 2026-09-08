from pathlib import Path
from itertools import product,combinations
import json,hashlib,signal
signal.alarm(170);B=Path(__file__).parent.parent/'native-l6-nonadjacent-prefix-census';data=json.loads((B/'CENSUS.json').read_text());n=0

def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
V=list(product(range(6),repeat=3));idx={v:i for i,v in enumerate(V)};E=[]
for v in V:
 for a in range(3):
  w=tuple((v[d]+(d==a))%6 for d in range(3));E.append(tuple(sorted((idx[v],idx[w]))))
ck([list(x) for x in E]==data['edges']);stars=[{e for e,(a,b) in enumerate(E) if v in (a,b)} for v in range(216)];allm=set();starall=set()
for row in data['rows']:
 w=idx[tuple(map(int,row['name']))];s0=stars[0];s1=stars[w];ck(not s0&s1);ck(not any(set(E[a])&set(E[b]) for a in s0 for b in s1));ck(row['cut']==sorted(s0|s1))
 def even(star):return [frozenset(c) for k in (0,2,4,6) for c in combinations(sorted(star),k)]
 keys={tuple(sorted(a|b)) for a in even(s0) for b in even(s1) if 0<len(a|b)<12};ck(len(keys)==1022);actual={tuple(x['used']):int(x['mask']) for x in row['proper_keys']};ck(set(actual)==keys)
 for key in keys:ck(actual[key]==sum(1<<e for e in key))
 pairsets=set()
 for ps in row['pair_sets']:
  ps=tuple(sorted(tuple(sorted(p)) for p in ps));ck(len(ps)==6 and sorted(e for p in ps for e in p)==sorted(s0|s1));ck(all(set(E[a])&set(E[b]) for a,b in ps));pairsets.add(ps)
 ck(len(pairsets)==225);ck(row['ordered_words']==225*720)
 seen={next(v for v in range(216) if v not in (0,w))};todo=list(seen)
 while todo:
  v=todo.pop()
  for e in stars[v]:
   a,b=E[e];u=a^b^v
   if u not in (0,w) and u not in seen:seen.add(u);todo.append(u)
 ck(len(seen)==214);star={sum(1<<e for e in s0),sum(1<<e for e in s1)};ck(set(map(int,row['singleton_masks']))==star);starall|=star;allm.update(actual.values())
ck(len(allm)==4986);ck(allm==set(map(int,data['all_masks'])));ck(len(starall)==6)
# Full coboundary consistency independently verifies exactly the singleton exceptions.
gauge=set()
for mask in sorted(allm):
 color={0:0};todo=[0];okay=True
 while todo and okay:
  v=todo.pop()
  for e in stars[v]:
   a,b=E[e];u=a^b^v;want=color[v]^((mask>>e)&1)
   if u in color:
    if color[u]!=want:okay=False;break
   else:color[u]=want;todo.append(u)
 if okay:gauge.add(mask)
ck(gauge==starall)
print(json.dumps({'checks':n,'keys':5110,'masks':4986,'gauge_masks':len(gauge),'scope':'independent even-subset census and full cut consistency; no gap/eigenvalue calculation'}))
