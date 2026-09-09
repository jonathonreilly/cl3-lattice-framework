"""Exact reconstruction of declared insertion families; no spectral arithmetic."""
from itertools import product,combinations
from functools import lru_cache
import json

def require(c,m):
 if not c:raise ValueError(m)
def canonical(x):return json.loads(json.dumps(x))
def check(adj,non,targets,adj_result,non_rows):
 V=list(product(range(6),repeat=3));vi={v:i for i,v in enumerate(V)};E=[]
 for v in V:
  for a in range(3):
   w=list(v);w[a]=(w[a]+1)%6;E.append(tuple(sorted((vi[v],vi[tuple(w)]))))
 require(canonical(E)==adj['edges']==non['edges'],'literal edge order')
 stars=[{e for e,ab in enumerate(E) if v in ab} for v in range(216)]
 @lru_cache(None)
 def match(es):
  if not es:return frozenset({()})
  a=es[0];out=set()
  for b in set(es[1:]):
   if a==b or not set(E[a])&set(E[b]):continue
   rem=list(es[1:]);rem.remove(b)
   for tail in match(tuple(rem)):out.add(tuple(sorted(((min(a,b),max(a,b)),)+tail)))
  return frozenset(out)
 bd=sorted(stars[0]^stars[36]);ar=[];members={};keys=0
 for e in range(648):
  if e in bd:continue
  sets=match(tuple(sorted(bd+[e,e])))
  if not sets:continue
  prefixes=set()
  for pairs in sets:
   for k in range(1,6):
    for sub in combinations(pairs,k):
     used=bc=mask=0
     for a,b in sub:
      for x in (a,b):
       mask^=1<<x
       if x==e:bc+=1
       else:used|=1<<x
     prefixes.add((k,used,bc,mask));members.setdefault(str(mask),set()).add(36)
  ar.append(dict(bridge=e,endpoints=E[e],matchings=len(sets),prefixes=[dict(k=k,used=str(u),bridge_count=c,mask=str(m)) for k,u,c,m in sorted(prefixes)]));keys+=len(prefixes)
 require(canonical(ar)==adj['rows'] and keys==2038,'complete adjacent families')
 for row,name in zip(non['rows'],['003','012','023','122','223']):
  w=vi[tuple(map(int,name))];cut=stars[0]^stars[w];sets=match(tuple(sorted(cut)))
  require(row['name']==name and row['centers']==[0,w] and len(sets)==225 and set(tuple(tuple(p) for p in ps) for ps in row['pair_sets'])==set(sets),'nonadjacent actual pairings')
  subsets=[]
  for star in (stars[0],stars[w]):
   subsets.append([set(c) for k in (0,2,4,6) for c in combinations(sorted(star),k)])
  pairs={}
  for a in subsets[0]:
   for b in subsets[1]:
    used=tuple(sorted(a|b))
    if not used or len(used)==12:continue
    mask=sum(1<<e for e in used);pairs[used]=mask;members.setdefault(str(mask),set()).add(w)
  expected=[dict(used=list(k),mask=str(v),order=len(k)//2) for k,v in sorted(pairs.items())]
  require(expected==row['proper_keys'] and len(expected)==1022,'all even-subset proper keys');keys+=len(expected)
 require(keys==7148 and len(members)==6489,'union key/mask counts')
 a={r['mask']:r['gap_lower'] for r in adj_result['rows']};n={r['case']['mask']:r['gap_lower'] for r in non_rows}
 require(len(a)==1534 and len(n)==4986 and len(a.keys()&n.keys())==31,'source union')
 require(all(a[k]==n[k] for k in a.keys()&n.keys()),'overlap equality')
 require(set(members)==a.keys()|n.keys() and len(targets)==6489 and len({r['mask'] for r in targets})==6489,'target coverage')
 # Literal spanning-tree gauge test for every mask, not merely flux labels.
 neighbors=[[] for _ in V]
 for e,(i,j) in enumerate(E):neighbors[i].append((j,e));neighbors[j].append((i,e))
 order=[0];seen={0};tree=[]
 for i in order:
  for j,e in neighbors[i]:
   if j not in seen:seen.add(j);order.append(j);tree.append((i,j,e))
 star_masks={sum(1<<e for e in s):v for v,s in enumerate(stars)};singletons=0
 for row in targets:
  mask=int(row['mask']);potential=[0]*216
  for i,j,e in tree:potential[j]=potential[i]^((mask>>e)&1)
  iscut=all((potential[i]^potential[j])==((mask>>e)&1) for e,(i,j) in enumerate(E))
  singleton=star_masks.get(mask)
  require(iscut==(singleton is not None) and row['singleton']==singleton,'proper cut/parity class')
  singletons+=iscut
  require(row['center'] in members[row['mask']] and row['gap_lower']==(a.get(row['mask']) or n[row['mask']]),'target source binding')
 require(singletons==7,'seven singleton stars')
 return dict(status='PASS',masks=6489,keys=7148,overlap=31,singletons=7,scope='complete declared-support geometry and source ledger')
