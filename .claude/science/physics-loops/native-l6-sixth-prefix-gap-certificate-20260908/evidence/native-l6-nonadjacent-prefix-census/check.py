import itertools,json,time,signal,resource,hashlib
from pathlib import Path
signal.alarm(30);t=time.monotonic();P=Path(__file__).parent
V=list(itertools.product(range(6),repeat=3));vi={v:i for i,v in enumerate(V)};edges=[]
for v in V:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%6;edges.append(tuple(sorted((vi[v],vi[tuple(w)]))))
stars=[{e for e,ab in enumerate(edges) if v in ab} for v in range(216)]
def matching(es):
 if not es:yield ();return
 a=min(es)
 for b in sorted(es-{a}):
  if set(edges[a])&set(edges[b]):
   for rest in matching(es-{a,b}):yield ((a,b),)+rest
rows=[];allmask=set();checks=0
for name in ['003','012','023','122','223']:
 w=vi[tuple(map(int,name))];cut=stars[0]^stars[w];sets=list(matching(cut))
 if len(cut)!=12 or len(sets)!=225:raise RuntimeError('matching census')
 keys={}
 for pairs in sets:
  if any(not(set(pair)<=stars[0] or set(pair)<=stars[w]) for pair in pairs):raise RuntimeError('cross star insertion')
  for bits in range(1,63):
   used=tuple(sorted(e for j,pair in enumerate(pairs) if bits>>j&1 for e in pair));mask=sum(1<<e for e in used)
   keys[used]=mask
 if len(keys)!=1022:raise RuntimeError('keys')
 # Literal graph minus centers connected: all cuts supported in the two stars are subsets of centers up to complement.
 seen={next(v for v in range(216) if v not in (0,w))};todo=list(seen)
 while todo:
  v=todo.pop()
  for e in stars[v]:
   u=next(x for x in edges[e] if x!=v)
   if u not in (0,w) and u not in seen:seen.add(u);todo.append(u)
 if len(seen)!=214:raise RuntimeError('deleted graph disconnected')
 singleton={sum(1<<e for e in stars[v]):v for v in (0,w)}
 if len(set(keys.values())&set(singleton))!=2:raise RuntimeError('singleton count')
 masks=sorted(keys.values());allmask.update(masks)
 rows.append(dict(name=name,centers=[0,w],cut=sorted(cut),pair_sets=sets,proper_keys=[dict(used=list(k),mask=str(v),order=len(k)//2) for k,v in sorted(keys.items())],singleton_masks={str(k):v for k,v in singleton.items()},ordered_words=len(sets)*720))
 checks+=len(sets)+len(keys)+len(seen)+3
 if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1024**2:raise RuntimeError('RSS cap')
out=dict(vertices=V,edges=edges,rows=rows,proper_keys=5110,distinct_masks=len(allmask),fixed_case_order=[r['name'] for r in rows],all_masks=[str(x) for x in sorted(allmask)])
(P/'CENSUS.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
r=dict(status='PASS',exact_checks=checks,proper_keys=5110,distinct_masks=len(allmask),ordered_words=sum(r['ordered_words'] for r in rows),seconds=time.monotonic()-t,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),census_sha256=hashlib.sha256((P/'CENSUS.json').read_bytes()).hexdigest())
(P/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
