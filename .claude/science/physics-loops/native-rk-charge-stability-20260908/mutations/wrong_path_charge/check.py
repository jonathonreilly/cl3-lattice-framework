AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ()
import itertools,collections,json,time,hashlib,resource,os
from pathlib import Path
start=time.monotonic();checks=0
def require(ok,msg):
 global checks
 if not ok:raise RuntimeError(msg)
 checks+=1

def run(extents,opposite_only=False):
 vertices=list(itertools.product(*(range(L) for L in extents)));ids={r:i for i,r in enumerate(vertices)}
 edges=[];lookup={}
 for r in vertices:
  for a in range(3):
   q=list(r);q[a]=(q[a]+1)%extents[a];lookup[r,a]=len(edges);edges.append((ids[r],ids[tuple(q)]))
 eps=[(-1)**sum(r) for r in vertices]
 bits=[r[a]%2 for r in vertices for a in range(3)]
 faces=[]
 for r in vertices:
  for a,b in itertools.combinations(range(3),2):
   ra=list(r);ra[a]=(ra[a]+1)%extents[a]
   rb=list(r);rb[b]=(rb[b]+1)%extents[b]
   faces.append([lookup[r,a],lookup[tuple(ra),b],lookup[tuple(rb),a],lookup[r,b]])
 states=[bits.copy()];rings=0
 for face in faces:
  b=[bits[e] for e in face]
  if all(b[k]!=b[(k+1)%4] for k in range(4)):
   for e in face:bits[e]^=1
   rings+=1
 states.append(bits.copy());summaries=[]
 for state in states:
  degree=[0]*len(vertices);out=[[] for _ in vertices]
  for e,(i,j) in enumerate(edges):
   degree[i]+=state[e];degree[j]+=state[e]
   tail,head=(i,j) if eps[i]*(2*state[e]-1)==1 else (j,i)
   out[tail].append((head,e))
  require(all(d==3 for d in degree),'actual-ice-degree')
  require(all(len(row)==3 for row in out),'three-outgoing-arrows')
  pairs=0;maxlen=0
  for u,r in enumerate(vertices):
   parent={u:None};queue=collections.deque([u])
   while queue:
    i=queue.popleft()
    for j,e in out[i]:
     if j not in parent:parent[j]=(i,e);queue.append(j)
   require(len(parent)==len(vertices),'directed-strong-connectivity')
   targets=[ids[tuple((r[a]+extents[a]//2)%extents[a] for a in range(3))]] if opposite_only else range(len(vertices))
   for v in targets:
    if v==u:continue
    path=[];j=v
    while j!=u:
     i,e=parent[j];path.append((i,j,e));j=i
    path.reverse();q=[0]*len(vertices);seen={u}
    for i,j,e in path:
     require(j not in seen,'simple-path');seen.add(j)
     a,b=edges[e];delta=1-2*state[e]
     require(eps[a]*delta==(-1 if a==i else 1),'oriented-electric-flip')
     q[a]-=eps[a]*delta;q[b]+=eps[b]*delta
     require(all(abs(x)<=1 for x in q),'prefix-low-charge')
    require(q[u]==-1 and q[v]==1 and all(q[k]==0 for k in range(len(q)) if k not in (u,v)),'signed-pair-only')
    # Recompute actual degree after simultaneous path flip, independent of prefix update.
    new=state.copy()
    for i,j,e in path:new[e]^=1
    deg=[0]*len(vertices)
    for e,(i,j) in enumerate(edges):deg[i]+=new[e];deg[j]+=new[e]
    require([eps[k]*(deg[k]-3) for k in range(len(vertices))]==q,'literal-final-Gauss')
    pairs+=1;maxlen=max(maxlen,len(path))
  summaries.append({'pairs':pairs,'maximum_constructed_path_length':maxlen})
 return {'extents':extents,'vertices':len(vertices),'edges':len(edges),'deterministic_legal_ring_flips':rings,'two_orientations':summaries}
results=[run((4,4,4)),run((4,4,6)),run((8,8,8),True)]
# Actual16bit face operator, F(I-Xall), including both alternating states.
F=[int(all(((x>>k)&1)!=((x>>((k+1)%4))&1) for k in range(4))) for x in range(16)]
R=[[F[x]*(int(y==x)-int(y==(x^15))) for x in range(16)] for y in range(16)]
require(all(sum(row)==0 for row in R),'RK-uniform-zero')
require(all(R[i][j]==R[j][i] for i in range(16) for j in range(16)),'RK-Hermitian')
require(all(sum(R[i][k]*R[k][j] for k in range(16))==2*R[i][j] for i in range(16) for j in range(16)),'RK-spectrum-zero-two')
v=[0]*16;v[5]=1;v[10]=-1
require(sum(v[i]*R[i][j]*v[j] for i in range(16) for j in range(16))==4,'negative-J-adverse-numerator')
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if os.uname().sysname=='Darwin' else 1024)
require(seconds<180 and 0<rss<384,'resource-bound')
print(json.dumps({'checks':checks,'graphs':results,'seconds':seconds,'rss_mib':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
