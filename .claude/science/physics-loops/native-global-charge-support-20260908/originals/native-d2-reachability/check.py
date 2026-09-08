import time,signal,resource,json,sys,hashlib
start=time.monotonic();signal.alarm(180)
from itertools import product
from collections import deque
from pathlib import Path
checks=0
def req(c):
 global checks
 checks+=1
 if not c:raise RuntimeError('D2 reachability')
def graph(shape):
 vs=list(product(*map(range,shape)));ids={r:i for i,r in enumerate(vs)};es=set()
 for i,r in enumerate(vs):
  for a in range(len(shape)):
   y=list(r);y[a]=(y[a]+1)%shape[a];es.add(tuple(sorted((i,ids[tuple(y)]))))
 es=sorted(es);ix={e:k for k,e in enumerate(es)};inc=[sum(1<<k for k,e in enumerate(es) if v in e) for v in range(len(vs))];nb=[[] for _ in vs]
 for k,(a,b) in enumerate(es):nb[a].append((b,k));nb[b].append((a,k))
 return vs,ids,es,inc,nb
# Exhaustive dimension-two analogue is supporting control, not the 3D proof.
vs,ids,es,inc,nb=graph((4,4));mn=100
for z in range(1,(1<<16)-1):
 cut=sum(((z>>a)^(z>>b))&1 for a,b in es);mn=min(mn,cut)
req(mn==4)
rows=[]
for shape in ((4,4,4),(4,4,6),(6,6,6)):
 vs,ids,es,inc,nb=graph(shape);V=len(vs);eps=[(-1)**sum(r) for r in vs]
 def Q(z):return [eps[v]*((z&inc[v]).bit_count()-3) for v in range(V)]
 def bfs(z,root,blocked,s):
  prev={root:None};queue=deque([root])
  while queue:
   v=queue.popleft()
   for w,e in nb[v]:
    if w==blocked or w in prev:continue
    if s*eps[v]*(2*((z>>e)&1)-1)==1:prev[w]=(v,e);queue.append(w)
  return prev
 seed=0
 for e,(i,j) in enumerate(es):
  a=next(a for a in range(3) if vs[i][a]!=vs[j][a]);r=i if (vs[i][a]+1)%shape[a]==vs[j][a] else j
  seed|=(vs[r][a]%2)<<e
 req(Q(seed)==[0]*V)
 prev=bfs(seed,0,None,1);v=ids[(2,0,0)];path=[]
 while v:vv,e=prev[v];path.append(e);v=vv
 x=seed
 for e in path:x^=1<<e
 seen={x};front={x}
 for dep in range(2):
  nxt=set()
  for z in front:
   q=Q(z)
   for e,(a,b) in enumerate(es):
    if (q[a]!=0)==(q[b]!=0):continue
    zz=z^(1<<e)
    if all(abs(c)<=1 for c in Q(zz)):nxt.add(zz)
  front=nxt-seen;seen|=nxt
 paths=0;maxlen=0
 for z in sorted(seen):
  q=Q(z);req(q.count(1)==q.count(-1)==1)
  for s in (-1,1):
   root=q.index(s);blocked=q.index(-s);prev=bfs(z,root,blocked,s);req(len(prev)==V-1)
   for target in prev:
    path=[];v=target
    while v!=root:vv,e=prev[v];path.append((vv,v,e));v=vv
    path.reverse();zz=z;pos=root
    for a,b,e in path:
     before=Q(zz);req(before[a]==s and before[b]==0);zz^=1<<e;expected=[0]*V;expected[b]=s;expected[blocked]=-s;req(Q(zz)==expected);pos=b
    req(pos==target);paths+=1;maxlen=max(maxlen,len(path))
 # Coordinate-box cuts and singleton6 under actual periodic edge geometry.
 for a in range(1,shape[0]+1):
  for b in range(1,shape[1]+1):
   for c in range(1,shape[2]+1):
    subset={i for i,r in enumerate(vs) if r[0]<a and r[1]<b and r[2]<c}
    if len(subset)<V:req(sum((i in subset)!=(j in subset) for i,j in es)>=6)
 req(len(nb[0])==6)
 rows.append(dict(shape=shape,states=len(seen),directed_paths=paths,max_path_length=maxlen))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);req(0<rss<384)
p=Path(__file__).resolve().parent
print(json.dumps(dict(checks=checks,rows=rows,two_dimensional_min_cut=mn,seconds=time.monotonic()-start,peak_MiB=rss,source_sha256={n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ('check.py','DERIVATION.md','PREREGISTRATION.md')}),indent=2))
