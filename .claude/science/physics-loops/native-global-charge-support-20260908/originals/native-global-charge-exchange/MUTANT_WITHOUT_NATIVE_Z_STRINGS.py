import time,signal,resource,json,sys,hashlib
start=time.monotonic();signal.alarm(180)
from pathlib import Path
from itertools import product
from collections import deque
verts=list(product(range(4),repeat=3));vid={r:i for i,r in enumerate(verts)};edges=set()
for i,r in enumerate(verts):
 for a in range(3):
  z=list(r);z[a]=(z[a]+1)%4;edges.add(tuple(sorted((i,vid[tuple(z)]))))
edges=sorted(edges);eid={e:k for k,e in enumerate(edges)};eps=[(-1)**sum(r) for r in verts];nbr=[sorted(j if i==v else i for i,j in edges if v in (i,j)) for v in range(64)];inc=[sum(1<<k for k,e in enumerate(edges) if v in e) for v in range(64)]
i,j,k,l=map(vid.get,[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]);charge=[0]*64
for v in (j,l):charge[v]=1
for r in ((2,2,0),(2,0,2)):charge[vid[r]]=-1
fixed={eid[tuple(sorted((i,j)))]:0,eid[tuple(sorted((i,k)))]:1,eid[tuple(sorted((i,l)))]:0};demand=[3+eps[v]*charge[v] for v in range(64)]
for e,b in fixed.items():
 for v in edges[e]:demand[v]-=b
S,T=64,65;cap=[{} for _ in range(66)]
def add(a,b,c):cap[a][b]=c;cap[b][a]=0
for v in range(64):
 if eps[v]==1:add(S,v,demand[v])
 else:add(v,T,demand[v])
for e,(a,b) in enumerate(edges):
 if e in fixed:continue
 if eps[a]!=1:a,b=b,a
 add(a,b,1)
flow=0
while True:
 prev={S:None};q=deque([S])
 while q and T not in prev:
  a=q.popleft()
  for b,c in cap[a].items():
   if c and b not in prev:prev[b]=a;q.append(b)
 if T not in prev:break
 b=T;amount=10**9
 while b!=S:a=prev[b];amount=min(amount,cap[a][b]);b=a
 b=T
 while b!=S:a=prev[b];cap[a][b]-=amount;cap[b][a]+=amount;b=a
 flow+=amount
checks=0
def req(c):
 global checks
 checks+=1
 if not c:raise RuntimeError('global native exchange witness')
req(flow==sum(demand[v] for v in range(64) if eps[v]==1))
x=sum(b<<e for e,b in fixed.items())
for e,(a,b) in enumerate(edges):
 if e in fixed:continue
 if eps[a]!=1:a,b=b,a
 if cap[a][b]==0:x|=1<<e

def Q(z):return [eps[v]*((z&inc[v]).bit_count()-3) for v in range(64)]
def tape(z,seq,s):
 out=[dict(bits=format(z,'0192b'),charges=Q(z),phase_mod4=0)];phase=0
 for a,b in seq:
  q=Q(z);req(q[a]==0 and q[b]==s)
  e=eid[tuple(sorted((a,b)))];pa=2*int(a>b)
  for v,w in ((a,b),(b,a)):
   for nb in nbr[v]:
    if False:pa+=2*((z>>eid[tuple(sorted((v,nb)))])&1)
  Ba=(-1)**((z&inc[a]).bit_count());Bb=(-1)**((z&inc[b]).bit_count());req(Ba==-1 and Bb==1)
  phase=(phase+pa+3)%4;z^=1<<e;qq=Q(z)
  req(all(abs(q)<=1 for q in qq));req(qq.count(1)==qq.count(-1)==2);req(qq[a]==s and qq[b]==0)
  out.append(dict(bits=format(z,'0192b'),charges=qq,phase_mod4=phase))
 return z,phase,out
req(Q(x)==charge);req(all((x>>e)&1==b for e,b in fixed.items()))
seqA=[(i,j),(k,i),(i,l)];seqB=[(i,l),(k,i),(i,j)];witnesses=[]
for s,z in ((1,x),(-1,x^((1<<192)-1))):
 a,pa,ta=tape(z,seqA,s);b,pb,tb=tape(z,seqB,s);req(a==b);req((pa-pb)%4==2)
 # Reverse B at the common endpoint closes the six-hop loop.
 end,pc,tc=tape(a,[(v,u) for u,v in reversed(seqB)],s);req(end==z);req((pa+pc)%4==2)
 witnesses.append(dict(sign=s,initial_bits=format(z,'0192b'),routeA=ta,routeB=tb,reverseB=tc,routeA_phase=pa,routeB_phase=pb,closed_loop_phase=(pa+pc)%4))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);req(0<rss<384)
p=Path(__file__).resolve().parent
print(json.dumps(dict(status='PASS',checks=checks,vertices=verts,edges=edges,star=dict(i=i,j=j,k=k,l=l),fixed_star_bits=fixed,maxflow=flow,witnesses=witnesses,seconds=time.monotonic()-start,peak_MiB=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))
