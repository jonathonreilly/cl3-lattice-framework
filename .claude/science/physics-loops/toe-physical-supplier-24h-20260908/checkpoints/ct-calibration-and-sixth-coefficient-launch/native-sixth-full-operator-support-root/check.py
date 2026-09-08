from itertools import product,combinations
from functools import lru_cache
from pathlib import Path
import json,time,signal,resource
signal.alarm(180);start=time.monotonic();checks=0

def ck(c,s):
 global checks
 checks+=1
 if not c:raise RuntimeError(s)
vs=list(product(range(4),repeat=3));ix={v:i for i,v in enumerate(vs)};edges=[];K=[[0]*64 for _ in vs]
for r in vs:
 for a in range(3):
  q=list(r);q[a]=(q[a]+1)%4;u,v=sorted((ix[r],ix[tuple(q)]));e=len(edges);edges.append((u,v));xi=(-1)**sum(r[:a]);K[u][v]=-2*xi;K[v][u]=2*xi
stars=[{e for e,(u,v) in enumerate(edges) if i in (u,v)} for i in range(64)]
ck(all(len(s)==6 for s in stars),'degree6')
rows={}
for v,w in combinations(range(64),2):
 cut=stars[v]^stars[w];d=sum(min(abs(a-b),4-abs(a-b)) for a,b in zip(vs[v],vs[w]));ck(len(cut)==(10 if d==1 else 12),'paircut')
 if d==1:continue
 boundary=sorted(cut);adj=[sum(1<<j for j,f in enumerate(boundary) if i!=j and set(edges[e])&set(edges[f])) for i,e in enumerate(boundary)]
 @lru_cache(None)
 def count(mask):
  if not mask:return 1
  low=mask&-mask;i=low.bit_length()-1;rest=mask^low;jobs=adj[i]&rest;s=0
  while jobs:
   bit=jobs&-jobs;jobs^=bit;s+=count(rest^bit)
  return s
 matches=count((1<<12)-1);ck(matches>=225,'center pairings included');key=(d,(sum(vs[v])+sum(vs[w]))%2,matches);rows[key]=rows.get(key,0)+1
 if d>3:
  Sv={v}|{j for j in range(64) if K[v][j]};Sw={w}|{j for j in range(64) if K[w][j]}
  ck(not Sv&Sw and all(K[a][b]==0 for a in Sv for b in Sw),'orthogonal Wstar')
# Finite exact Clifford representation; Gaussian integer entries only.
def gamma(j,x):
 mode=j//2;sgn=(-1)**((x&((1<<mode)-1)).bit_count());return x^(1<<mode),sgn*(1 if j%2==0 else 1j*(-1)**((x>>mode)&1))
for i,j in combinations(range(8),2):
 for x in range(16):
  y,a=gamma(j,x);z,b=gamma(i,y);value=a*b
  ck(value.imag==0 if i%2==j%2 else value.real==0,'color reality')
  y,c=gamma(i,x);zz,d=gamma(j,y);ck(zz==z and value==-c*d,'antihermitian Clifford')
# On even spectator parity, distinct bilinears orthogonal for eight Majoranas.
even=[x for x in range(16) if x.bit_count()%2==0];pairs=list(combinations(range(8),2));cols={}
for i,j in pairs:
 z=[]
 for x in even:
  y,a=gamma(j,x);y,b=gamma(i,y);z.append((y,a*b))
 cols[i,j]=z
for a,b in combinations(pairs,2):
 tr=sum(x[1].conjugate()*y[1] for x,y in zip(cols[a],cols[b]) if x[0]==y[0]);ck(tr==0,'spectator independence')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576;ck(rss<384,'rss')
out=dict(checks=checks,seconds=time.monotonic()-start,rss_mib=rss,nonadjacent_pair_classes=[dict(distance=k[0],opposite_color=bool(k[1]),matchings=k[2],pairs=v) for k,v in sorted(rows.items())],scope='support geometry and exact Clifford controls; no coefficient or linked-cluster cancellation proof')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
