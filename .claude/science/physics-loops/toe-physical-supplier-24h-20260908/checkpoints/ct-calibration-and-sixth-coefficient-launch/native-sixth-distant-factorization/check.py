from itertools import product,combinations
from pathlib import Path
import json,time,signal,resource
signal.alarm(180);t=time.monotonic();n=0
def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
V=list(product(range(4),repeat=3));adj={v:set() for v in V}
for v in V:
 for a in range(3):
  for s in (-1,1):
   w=list(v);w[a]=(w[a]+s)%4;adj[v].add(tuple(w))
for v,w in combinations(V,2):
 d=sum(min(abs(x-y),4-abs(x-y)) for x,y in zip(v,w))
 if d<=3:continue
 rest=set(V)-{v,w};seen={next(iter(rest))};todo=list(seen)
 while todo:
  x=todo.pop()
  for y in (adj[x]&rest)-seen:seen.add(y);todo.append(y)
 ck(seen==rest)
# Clifford monomial commutation: sign=(-1)^(|A||B|-|A intersect B|).
def commute(a,b):return ((len(a)*len(b)-len(a&b))%2)==0
W=set(range(12));beta=12;remote=13;other=14
sym=W|{beta,remote}
for a,b in combinations(range(12),2):ck(commute(sym,{a,b}))
for a in range(12):ck(commute(sym,{a,beta}))
ck(not commute({beta,remote},{beta,other}))
ck(commute(sym,set(range(16))))
Path(__file__).with_name('RESULT.json').write_text(json.dumps(dict(checks=n,seconds=time.monotonic()-t,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,scope='finite graph closure and abstract Clifford symmetry; no coefficient solve'),indent=2)+'\n')
