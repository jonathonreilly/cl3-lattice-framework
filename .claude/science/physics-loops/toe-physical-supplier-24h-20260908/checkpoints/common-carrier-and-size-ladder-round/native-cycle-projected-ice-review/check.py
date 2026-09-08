from itertools import product,combinations
import json,hashlib,time
from pathlib import Path
start=time.monotonic();L=4;verts=list(product(range(L),repeat=3));idx={v:i for i,v in enumerate(verts)};edges=[]
for v in verts:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%L;edges.append((idx[v],idx[tuple(w)]))
edgeidx={frozenset(e):i for i,e in enumerate(edges)};inc={i:[] for i in range(64)}
for k,(u,v) in enumerate(edges):inc[u].append((v,k));inc[v].append((u,k))
def mul(a,b):return(a[0]^b[0],a[1]^b[1],(a[2]+b[2]+2*((a[1]&b[0]).bit_count()%2))%4)
def A(u,v):
 k=edgeidx[frozenset((u,v))];z=0
 for s,t in [(u,v),(v,u)]:
  for w,j in inc[s]:
   if w<t:z^=1<<j
 return(1<<k,z,0 if u<v else 2)
def cycle(path):
 out=(0,0,len(path)-1)
 for u,v in zip(path,path[1:]):out=mul(out,A(u,v))
 return(out[0],out[1],out[2]%4)
parent={0:None};pe={};queue=[0]
for u in queue:
 for v,k in inc[u]:
  if v not in parent:parent[v]=u;pe[v]=k;queue.append(v)
tree=set(pe.values());fund=[];chords=[]
for k,(u,v) in enumerate(edges):
 if k in tree:continue
 pu=[];x=u
 while x is not None:pu.append(x);x=parent[x]
 pv=[];x=v
 while x not in pu:pv.append(x);x=parent[x]
 path=pu[:pu.index(x)+1]+pv[::-1]+[u];fund.append(cycle(path));chords.append(k)
checks={};count=0;ss=[]
for v in verts:
 for a,b in combinations(range(3),2):
  w=list(v);w[a]=(w[a]+1)%L;t=list(w);t[b]=(t[b]+1)%L;r=list(v);r[b]=(r[b]+1)%L;path=[idx[v],idx[tuple(w)],idx[tuple(t)],idx[tuple(r)],idx[v]];s=cycle(path);g=(0,0,0)
  for k,f in zip(chords,fund):
   if (s[0]>>k)&1:g=mul(g,f)
  if s!=g:raise AssertionError(('holonomy',path,s,g))
  if mul(s,s)!=(0,0,0):raise AssertionError('square')
  ss.append(s);count+=1
checks['all192fundamental_products']=count==192
checks['commuting']=all(mul(s,t)==mul(t,s) for s,t in combinations(ss,2))
checks['local_square_alternation']=all((all(bits[j]!=bits[(j+1)%4] for j in range(4)))==(bits in [(0,1,0,1),(1,0,1,0)]) for bits in product([0,1],repeat=4))
checks['rooted_pair_bound']=max(sum(x!=y for x,y in combinations(bits,2)) for bits in product([0,1],repeat=3))==2
if not all(checks.values()):raise AssertionError(checks)
print(json.dumps(dict(checks=checks,vertices=64,edges=192,fundamental_cycles=len(fund),squares=count,seconds=time.monotonic()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))
