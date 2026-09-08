"""Finite L6 signed antisymmetric invariant-space census, exact integers."""
from itertools import product,combinations
from collections import deque,Counter
from pathlib import Path
import argparse,json,signal,time,resource,hashlib,sys
L=6;N=L**3
checks=0
def ck(x,s):
 global checks;checks+=1
 if not x:raise ValueError(s)
def run():
 vs=list(product(range(L),repeat=3));idx={v:i for i,v in enumerate(vs)};K=[[0]*N for _ in vs]
 for v in vs:
  for a in range(3):
   w=list(v);w[a]=(w[a]+1)%L;i,j=sorted((idx[v],idx[tuple(w)]));z=-2*(-1)**sum(v[:a]);ck(K[i][j]==0,'simple edge');K[i][j]=z;K[j][i]=-z
 fs=[]
 for a in range(3):
  for kind in ('shift','mirror'):
   f=[]
   for v in vs:
    w=list(v);w[a]=(w[a]+1)%L if kind=='shift' else (-w[a])%L;f.append(idx[tuple(w)])
   fs.append((kind+str(a),f))
 for a,b in ((0,1),(1,2)):
  f=[]
  for v in vs:w=list(v);w[a],w[b]=w[b],w[a];f.append(idx[tuple(w)])
  fs.append(('swap'+str(a)+str(b),f))
 lifts=[]
 for name,f in fs:
  ck(len(set(f))==N,'permutation');g=[None]*N;g[0]=1;todo=deque([0])
  while todo:
   i=todo.popleft()
   for j in range(N):
    if K[i][j]:
     ck(abs(K[f[i]][f[j]])==2,'edge image');z=g[i]*K[f[i]][f[j]]//K[i][j]
     if g[j] is None:g[j]=z;todo.append(j)
     else:ck(g[j]==z,'lift consistency')
  ck(all(x in (-1,1) for x in g),'gauge coverage')
  for i in range(N):
   for j in range(N):ck(K[f[i]][f[j]]==g[i]*g[j]*K[i][j],'whole matrix lift')
  lifts.append(dict(name=name,f=f,g=g))
 pairs={(i,j) for i,j in combinations(range(N),2) if (sum(vs[i])+sum(vs[j]))%2};unseen=set(pairs);orbits=[]
 while unseen:
  seed=min(unseen);labels={seed:1};todo=deque([seed]);conflict=None
  while todo:
   i,j=todo.popleft()
   for gen in lifts:
    a,b=gen['f'][i],gen['f'][j];pair=tuple(sorted((a,b)));sgn=gen['g'][i]*gen['g'][j]*(1 if a<b else -1);z=labels[i,j]*sgn
    ck(pair in pairs,'opposite-color image')
    if pair in labels:
     if labels[pair]!=z:conflict=dict(pair=pair,generator=gen['name'],existing=labels[pair],required=z)
    else:labels[pair]=z;todo.append(pair)
  unseen.difference_update(labels);types=Counter(tuple(sorted(min(abs(a-b),L-abs(a-b)) for a,b in zip(vs[i],vs[j]))) for i,j in labels)
  orbits.append(dict(representative=seed,size=len(labels),forced_zero=conflict is not None,conflict=conflict,displacements={str(k):v for k,v in types.items()},labels={str(k):v for k,v in sorted(labels.items())}))
 ck(sum(x['size'] for x in orbits)==N*N//4,'full pair coverage')
 return dict(L=L,vertices=N,pairs=len(pairs),orbits=orbits,invariant_dimension=sum(not x['forced_zero'] for x in orbits),generators=lifts,checks=checks)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');p.parse_args();signal.alarm(180);t=time.monotonic();result=run();rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);ck(time.monotonic()-t<180 and rss<384,'resources');result.update(checks=checks,seconds=time.monotonic()-t,rss_mib=rss);Path(__file__).with_name('RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ('orbits','generators')}));print([(x['size'],x['forced_zero'],x['displacements']) for x in result['orbits']])
