from itertools import product,combinations
from collections import deque
from pathlib import Path
import json,time,signal,resource,sys
if __name__=='__main__':signal.alarm(180)
start=time.monotonic();vs=list(product(range(4),repeat=3));idx={v:i for i,v in enumerate(vs)};K=[[0]*64 for _ in vs];checks=0
def ck(c,s):
 global checks
 checks+=1
 if not c:raise RuntimeError(s)
for r in vs:
 for a in range(3):
  q=list(r);q[a]=(q[a]+1)%4;i,j=sorted((idx[r],idx[tuple(q)]));K[i][j]=-2*(-1)**sum(r[:a]);K[j][i]=-K[i][j]
gens=[]
for a in range(3):
 for kind in ('translate','reflect'):
  f=[]
  for r in vs:
   q=list(r);q[a]=((q[a]+1) if kind=='translate' else -q[a])%4;f.append(idx[tuple(q)])
  gens.append((f'{kind}{a}',f))
for a,b in ((0,1),(1,2)):
 f=[]
 for r in vs:q=list(r);q[a],q[b]=q[b],q[a];f.append(idx[tuple(q)])
 gens.append((f'swap{a}{b}',f))
lifts=[]
for name,f in gens:
 g={0:1};todo=deque([0])
 while todo:
  i=todo.popleft()
  for j in range(64):
   if not K[i][j]:continue
   ck(abs(K[f[i]][f[j]])==2,'graph lift');s=g[i]*(K[f[i]][f[j]]//K[i][j])
   if j in g:ck(g[j]==s,'gauge consistency')
   else:g[j]=s;todo.append(j)
 ck(len(g)==64,'connected gauge')
 ck(all(K[f[i]][f[j]]==g[i]*g[j]*K[i][j] for i in range(64) for j in range(64)),'exact matrix covariance')
 lifts.append((name,f,[g[i] for i in range(64)]))
pairs=[(i,j) for i,j in combinations(range(64),2) if (sum(vs[i])+sum(vs[j]))%2];index={p:k for k,p in enumerate(pairs)};seen=set();orbits=[]
for root in range(len(pairs)):
 if root in seen:continue
 values={root:1};todo=deque([root]);bad=False
 while todo:
  k=todo.popleft();i,j=pairs[k]
  for name,f,g in lifts:
   a,b=f[i],f[j];sg=g[i]*g[j]*(1 if a<b else -1);q=index[tuple(sorted((a,b)))];v=values[k]*sg
   if q in values:
    if values[q]!=v:bad=True
   else:values[q]=v;todo.append(q)
 seen.update(values);ds=sorted(set(sum(min(abs(a-b),4-abs(a-b)) for a,b in zip(vs[pairs[k][0]],vs[pairs[k][1]])) for k in values));orbits.append(dict(size=len(values),forced_zero=bad,distances=ds,representative=pairs[root],values={str(pairs[k]):v for k,v in values.items()}))
ck(len(seen)==1024,'all oppositecolor pairs')
ck(sum(not o['forced_zero'] for o in orbits)==1,'one dimensional invariant bilinear space')
ck(sorted((o['size'],o['forced_zero'],tuple(o['distances'])) for o in orbits)==[(192,False,(1,)),(192,True,(5,)),(256,True,(3,)),(384,True,(3,))],'complete nearest and forbidden distant orbits')
out=dict(checks=checks,seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024),generators=[dict(name=n,permutation=f,gauge=g) for n,f,g in lifts],orbits=orbits,invariant_dimension=sum(not x['forced_zero'] for x in orbits),scope='exact signed graph-symmetry constraint space; physical lift still separate proof')
if __name__=='__main__':print(json.dumps(out))
