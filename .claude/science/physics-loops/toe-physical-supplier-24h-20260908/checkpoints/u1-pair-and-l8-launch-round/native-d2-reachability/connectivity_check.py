import json,time,signal,resource,sys,hashlib
from pathlib import Path
from itertools import product
from collections import deque
signal.alarm(180);start=time.monotonic();checks=0

def req(x):
 global checks
 checks+=1
 if not x:raise RuntimeError('connectivity certificate failed')
vs=list(product(range(4),repeat=3));vi={v:i for i,v in enumerate(vs)};es=set()
for i,v in enumerate(vs):
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%4;es.add(tuple(sorted((i,vi[tuple(w)]))))
es=sorted(es);ei={e:i for i,e in enumerate(es)};ep=[(-1)**sum(v) for v in vs];nb=[sorted(b if a==v else a for a,b in es if v in (a,b)) for v in range(64)];inc=[sum(1<<e for e,p in enumerate(es) if v in p) for v in range(64)]
def edge(a,b):return ei[tuple(sorted((a,b)))]
def Q(z):return [ep[v]*((z&inc[v]).bit_count()-3) for v in range(64)]
def arrow(z,a,b):return ep[a]*(2*((z>>edge(a,b))&1)-1)==1

def make(C,p,m):
 q=[0]*64;q[p]=1;q[m]=-1;fixed={edge(a,b):(1+ep[a])//2 for a,b in zip(C,C[1:]+C[:1])};d=[3+ep[v]*q[v] for v in range(64)]
 for e,b in fixed.items():
  for v in es[e]:d[v]-=b
 cap=[{} for _ in range(66)]
 def add(a,b,c):cap[a][b]=c;cap[b][a]=0
 for v in range(64):
  if ep[v]==1:add(64,v,d[v])
  else:add(v,65,d[v])
 for e,(a,b) in enumerate(es):
  if e not in fixed:
   if ep[a]<0:a,b=b,a
   add(a,b,1)
 flow=0
 while True:
  prev={64:None};queue=deque([64])
  while queue and 65 not in prev:
   a=queue.popleft()
   for b,c in cap[a].items():
    if c and b not in prev:prev[b]=a;queue.append(b)
  if 65 not in prev:break
  b=65
  while b!=64:a=prev[b];cap[a][b]-=1;cap[b][a]+=1;b=a
  flow+=1
 req(flow==sum(d[v] for v in range(64) if ep[v]>0))
 z=sum(b<<e for e,b in fixed.items())
 for e,(a,b) in enumerate(es):
  if e not in fixed:
   if ep[a]<0:a,b=b,a
   if cap[a][b]==0:z|=1<<e
 req(Q(z)==q);return z

results=[]
for coords,pcoord,mcoord in [([(0,0,0),(1,0,0),(1,1,0),(0,1,0)],(0,0,0),(1,1,0)), ([(0,0,0),(1,0,0),(2,0,0),(2,1,0),(1,1,0),(0,1,0)],(0,0,0),(2,1,0))]:
 C=[vi[v] for v in coords];z=make(C,vi[pcoord],vi[mcoord]);initial=z;tape=[];branches=[]
 def hop(a,b,s):
  global z
  q=Q(z);req(q[a]==s and q[b]==0);req(arrow(z,a,b)==(s==1))
  # Actual target-source native T phase: -i A_(b,a), ascending local orders.
  phase=3+2*int(b>a)
  for v,w in ((b,a),(a,b)):
   for u in nb[v]:
    if u<w:phase+=2*((z>>edge(v,u))&1)
  z^=1<<edge(a,b);qq=Q(z);req(qq[a]==0 and qq[b]==s);req(qq.count(1)==qq.count(-1)==1 and all(abs(x)<=1 for x in qq))
  tape.append(dict(source=a,target=b,sign=s,phase_mod4=phase%4,bits=format(z,'0192b'),charges=qq))
 def reverse(C):
  before=z;q0=Q(z);req(all(arrow(z,a,b) for a,b in zip(C,C[1:]+C[:1])))
  chord=next(((r,t) for r in range(len(C)) for t in range(r+2,len(C)) if not(r==0 and t==len(C)-1) and C[t] in nb[C[r]]),None)
  if chord:
   branches.append('chord');r,t=chord;P=C[r:t+1];R=C[t:]+C[:r+1]
   if arrow(z,C[r],C[t]):reverse([C[r]]+R[:-1]);reverse(P)
   else:reverse(P);reverse(R)
  else:
   p=q0.index(1);m=q0.index(-1);park=None
   if p in C and m in C:
    branches.append('both-charge-parking');park=next(b for b in nb[p] if b not in C and arrow(z,p,b));hop(p,park,1)
   q=Q(z);s=1 if q.index(-1) not in C else -1;origin=q.index(s);forbid=q.index(-s);prev={origin:None};queue=deque([origin]);hit=None
   while queue:
    a=queue.popleft()
    if a in C:hit=a;break
    for b in nb[a]:
     if b!=forbid and b not in prev and arrow(z,a,b)==(s==1):prev[b]=a;queue.append(b)
   req(hit is not None);path=[hit]
   while path[-1]!=origin:path.append(prev[path[-1]])
   path=path[::-1]
   for a,b in zip(path,path[1:]):hop(a,b,s)
   j=C.index(hit);route=[C[(j+s*k)%len(C)] for k in range(len(C)+1)]
   for a,b in zip(route,route[1:]):hop(a,b,s)
   for a,b in zip(path[::-1],path[-2::-1]):hop(a,b,s)
   if park is not None:hop(park,p,1)
  mask=sum(1<<edge(a,b) for a,b in zip(C,C[1:]+C[:1]));req(z==before^mask);req(Q(z)==q0)
 reverse(C);results.append(dict(cycle=C,initial_bits=format(initial,'0192b'),final_bits=format(z,'0192b'),branches=branches,hops=len(tape),tape=tape))
req('both-charge-parking' in results[0]['branches']);req('chord' in results[1]['branches'])
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);req(0<rss<384)
print(json.dumps(dict(status='PASS',checks=checks,vertices=vs,edges=es,fixtures=results,seconds=time.monotonic()-start,peak_MiB=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))
