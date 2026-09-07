import itertools,json,hashlib,time,signal,resource,sys
from fractions import Fraction as F
from pathlib import Path
start=time.monotonic();signal.alarm(180)
V=list(itertools.product((0,1),repeat=4));edges=[]
for v in V:
 for a in range(4):
  if v[a]==0:
   w=list(v);w[a]=1;edges.append((v,tuple(w)))
def square(a,b,fixed):
 v=[0]*4
 for axis,val in fixed.items():v[axis]=val
 vs=[tuple(v)];v[a]=1;vs.append(tuple(v));v[b]=1;vs.append(tuple(v));v[a]=0;vs.append(tuple(v))
 return [(edges.index((u,w)),1) if (u,w) in edges else (edges.index((w,u)),-1) for u,w in zip(vs,vs[1:]+vs[:1])]
sources=[square(0,1,{2:0,3:t}) for t in (0,1)]
parent={v:v for v in V}
def root(v):
 while parent[v]!=v:v=parent[v]
 return v
tree=[]
for e in [e for src in sources for e,s in src[:3]]+list(range(32)):
 if e in tree:continue
 u,v=edges[e];ru,rv=root(u),root(v)
 if ru!=rv:parent[rv]=ru;tree.append(e)
chords=[e for e in range(32) if e not in tree];assert len(tree)==15 and len(chords)==17
B=[];weights=[]
for a,b in itertools.combinations(range(4),2):
 rest=[j for j in range(4) if j not in (a,b)]
 for vals in itertools.product((0,1),repeat=2):
  fixed=dict(zip(rest,vals))
  if (a,b)==(0,1) and fixed[2]==0:continue
  word=square(a,b,fixed);B.append([sum(s for e,s in word if e==c) for c in chords]);weights.append(F(1) if b==3 else F(1,2))
S=[[sum(s for e,s in word if e==c) for c in chords] for word in sources]
assert all(sum(v!=0 for v in row)==1 for row in S)
assert next(i for i,v in enumerate(S[0]) if v)!=next(i for i,v in enumerate(S[1]) if v)
H=[[sum(weights[f]*B[f][i]*B[f][j] for f in range(22)) for j in range(17)] for i in range(17)]
M=[r[:] for r in H];pivots=[]
for k in range(17):
 pivot=M[k][k];assert pivot>0;pivots.append(pivot)
 for i in range(k+1,17):
  for j in range(k+1,17):M[i][j]-=M[i][k]*M[k][j]/pivot
from functools import reduce
print(json.dumps(dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),vertices=V,edges=edges,tree=tree,chords=chords,source_rows=S,face_rows=B,weights=list(map(str,weights)),positive_LDL_pivots=list(map(str,pivots)),determinant=str(reduce(lambda a,b:a*b,pivots,F(1))),seconds=time.monotonic()-start,rss_MiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024),scope='Independent adaptedsource-tree geometry and exact positive Hessian only; nonlinearHSproof is analytical.'),indent=2))
