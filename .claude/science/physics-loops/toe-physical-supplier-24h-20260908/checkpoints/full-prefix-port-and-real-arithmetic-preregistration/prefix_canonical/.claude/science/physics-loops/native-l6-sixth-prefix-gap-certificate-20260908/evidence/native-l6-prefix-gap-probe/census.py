from itertools import product,combinations
from functools import lru_cache
from pathlib import Path
import json,signal,time
signal.alarm(180);t=time.monotonic();V=list(product(range(6),repeat=3));ix={v:i for i,v in enumerate(V)};E=[]
for v in V:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%6;E.append(tuple(sorted((ix[v],ix[tuple(w)]))))
v,w=0,36;stars=[set(i for i,e in enumerate(E) if x in e) for x in (v,w)];bd=sorted(stars[0]^stars[1]);rows=[]
@lru_cache(None)
def match(es):
 if not es:return frozenset({()})
 a=es[0];out=set()
 for b in set(es[1:]):
  if a==b or not set(E[a])&set(E[b]):continue
  r=list(es[1:]);r.remove(b)
  for z in match(tuple(r)):out.add(tuple(sorted(((min(a,b),max(a,b)),)+z)))
 return frozenset(out)
for e in range(len(E)):
 if e in bd:continue
 sets=match(tuple(sorted(bd+[e,e])))
 if not sets:continue
 prefixes=set()
 for pairs in sets:
  for k in range(1,6):
   for sub in combinations(pairs,k):
    used=0;bc=0;mask=0
    for a,b in sub:
     for x in (a,b):
      mask^=1<<x
      if x==e:bc+=1
      else:used|=1<<x
    prefixes.add((k,used,bc,mask))
 rows.append(dict(bridge=e,endpoints=E[e],matchings=len(sets),prefixes=[dict(k=k,used=str(u),bridge_count=c,mask=str(m)) for k,u,c,m in sorted(prefixes)]))
Path(__file__).with_name('CENSUS.json').write_text(json.dumps(dict(L=6,centers=[v,w],edges=E,boundary=bd,rows=rows,seconds=time.monotonic()-t),indent=2)+'\n')
print([(r['bridge'],r['matchings'],len(r['prefixes'])) for r in rows])
