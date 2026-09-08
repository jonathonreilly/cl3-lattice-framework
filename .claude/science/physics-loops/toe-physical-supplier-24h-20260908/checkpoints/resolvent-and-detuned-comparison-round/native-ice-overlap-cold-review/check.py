import itertools,json
from pathlib import Path
rows=[]
for L in (4,6,8):
 vs=list(itertools.product(range(L),repeat=3));edges=[]
 for r in vs:
  for a in range(3):
   t=list(r);t[a]=(t[a]+1)%L;edges.append((r,tuple(t)))
 S={r for r in vs if all(v%2==0 for v in r)};stars=[{i for i,e in enumerate(edges) if s in e} for s in S]
 if not all(len(x)==6 for x in stars) or len(set.union(*stars))!=6*len(S):raise AssertionError('disjoint stars')
 rem=set(vs)-S;seen={next(iter(rem))};stack=list(seen)
 while stack:
  v=stack.pop()
  for e in edges:
   if v in e:
    w=e[1] if e[0]==v else e[0]
    if w in rem and w not in seen:seen.add(w);stack.append(w)
 if seen!=rem:raise AssertionError('complement connected')
 seed=[u[a]%2 for u in vs for a in range(3)];degree={r:sum(seed[i] for i,e in enumerate(edges) if r in e) for r in vs}
 if set(degree.values())!={3}:raise AssertionError('seed ice')
 root=(0,0,0);facevs=[(0,0,0),(1,0,0),(1,1,0),(0,1,0)];face=[next(i for i,e in enumerate(edges) if set(e)==set((facevs[j],facevs[(j+1)%4]))) for j in range(4)]
 if any(seed[i] for i in face):raise AssertionError('empty face')
 changed=seed.copy()
 for i in face:changed[i]^=1
 ds=[sum(changed[i] for i,e in enumerate(edges) if r in e) for r in vs]
 if not all(d%2==1 for d in ds) or 5 not in ds:raise AssertionError('outside ice odd fiber')
 rows.append(dict(L=L,V=len(vs),E=len(edges),stars=len(S),complement_connected=True,star_edges_disjoint=True,cycle_rank=len(edges)-len(vs)+1,conditional_completion_exponent=len(edges)-6*len(S)-(len(vs)-len(S))+1))
odd=[x for x in itertools.product((0,1),repeat=6) if sum(x)%2];good=[x for x in odd if sum(x)==3]
if (len(odd),len(good))!=(32,20):raise AssertionError('star marginal')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(dict(rows=rows,odd_patterns=32,ice_patterns=20),indent=2)+'\n');print(rows)
