"""Deterministic graph identities, independent of physical H8 tables."""
from itertools import product,combinations
from collections import Counter
from math import comb
from pathlib import Path
import json,time,resource,sys,hashlib,signal
signal.alarm(180);started=time.monotonic();checks=0

def need(ok,label):
 global checks
 checks+=1
 if not ok:raise RuntimeError(label)
def pathclass(b):
 b=tuple(b);return min(b,b[::-1],tuple(1-x for x in b),tuple(1-x for x in b[::-1]))
def cycleclass(b):
 b=tuple(b);return min(pathclass(b[j:]+b[:j]) for j in range(4))
def choose(n,k):return comb(n,k) if 0<=k<=n else 0
def graph(L):
 vs=list(product(range(L),repeat=3));idx={v:i for i,v in enumerate(vs)};edges=[];bits=[];adj=[[] for v in vs]
 for v in vs:
  i=idx[v]
  for a in range(3):
   w=list(v);w[a]=(w[a]+1)%L;j=idx[tuple(w)];edges.append((i,j));bits.append(v[a]%2)
 lookup={frozenset(e):k for k,e in enumerate(edges)}
 for k,(i,j) in enumerate(edges):adj[i].append((j,k));adj[j].append((i,k))
 paths=set();cycles={}
 for initial in range(len(vs)):
  def step(vertices,es):
   if len(es)==4:
    if vertices[-1]==initial:
     cycles.setdefault(frozenset(es),tuple(es))
    else:
     need(len(set(vertices))==5,'only nonbacktracking collision is four-cycle')
     paths.add(min(tuple(es),tuple(es[::-1])))
    return
   for j,e in adj[vertices[-1]]:
    if len(vertices)>1 and j==vertices[-2]:continue
    step(vertices+[j],es+[e])
  step([initial],[])
 return vs,edges,bits,adj,paths,list(cycles.values())
results=[]
for L in (4,6):
 vs,edges,bits,adj,paths,cycles=graph(L);N=len(vs)
 need(2*len(paths)+8*len(cycles)==750*N,'walk multiplicities')
 need(len(cycles)==(240 if L==4 else 3*N),'full fourcycles including winding')
 expected_path=Counter()
 for b in product((0,1),repeat=4):
  weight=3*N
  for x,y in zip(b,b[1:]):weight*=2 if x==y else 3
  expected_path[pathclass(b)]+=weight
 expected_star=Counter({k:N*choose(3,k)*choose(3,4-k) for k in range(5) if choose(3,k)*choose(3,4-k)})
 expected_fork=Counter()
 for b,k,d in product(range(2),range(3),range(2)):
  expected_fork[b,k,d]=3*N*choose(3-b,k)*choose(2+b,2-k)*(2 if b==d else 3)
 seen={tuple(bits)};snapshots=[]
 for snap in range(4):
  need(all(sum(bits[e] for _,e in a)==3 for a in adj),'literal ice background')
  pc=Counter(pathclass([bits[e] for e in es]) for es in paths);cc=Counter(cycleclass([bits[e] for e in es]) for es in cycles)
  removed=Counter()
  for es in cycles:
   b=tuple(bits[e] for e in es)
   for j in range(4):removed[pathclass(b[j:]+b[:j])]+=2
  need(Counter({k:2*pc[k]+removed[k] for k in expected_path})==expected_path,'every independent path-pattern coefficient identity')
  sc=Counter();fc=Counter()
  for a in adj:
   for es in combinations(a,4):sc[sum(bits[e] for _,e in es)]+=1
  for center,a in enumerate(adj):
   for other,e in a:
    for leaves in combinations([(v,h) for v,h in a if h!=e],2):
     for end,h in adj[other]:
      if h==e:continue
      need(len({center,other,end,leaves[0][0],leaves[1][0]})==5,'fork no collision')
      fc[bits[e],sum(bits[q] for _,q in leaves),bits[h]]+=1
  need(sc==expected_star,'star degree count');need(fc==expected_fork,'fork degree count')
  wall=sum(sum(bits[es[j]]!=bits[es[(j+1)%4]] for j in range(4)) for es in cycles)
  if L==4:need(wall==9*N,'all L4 corner opposite-bit pairs')
  else:
   # Sum omitted collinear pairs, one per vertex and axis.
   collinear=0
   for i,v in enumerate(vs):
    for axis in range(3):
     ids=[]
     for j,e in adj[i]:
      if vs[j][axis]!=v[axis]:ids.append(e)
     need(len(ids)==2,'opposite-axis pair');collinear+=bits[ids[0]]!=bits[ids[1]]
   need(wall==9*N-collinear,'plaquette corners omit collinear pairs')
  snapshots.append({'cycle_classes':{str(k):v for k,v in sorted(cc.items())},'domainwalls':wall,'seed_sha256':hashlib.sha256(bytes(bits)).hexdigest()})
  if snap<3:
   # Deterministically perform a novel legal cycle flip; all witnesses retained.
   for es in cycles:
    b=[bits[e] for e in es]
    if all(b[j]!=b[(j+1)%4] for j in range(4)):
     new=bits.copy()
     for e in es:new[e]^=1
     if tuple(new) not in seen:bits=new;seen.add(tuple(bits));break
   else:raise RuntimeError('no new legal successor')
 results.append({'L':L,'vertices':N,'paths':len(paths),'cycles':len(cycles),'snapshots':snapshots})
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
need(time.monotonic()-started<180 and rss<384,'resource cap')
out={'checks':checks,'seconds':time.monotonic()-started,'rss_mib':rss,'results':results,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Independent symbolic motif multiplicities on eight deterministic ice backgrounds; no physical H8 coefficients or stochastic evidence.'}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'}))
