from itertools import product,combinations
from pathlib import Path
import json,hashlib,signal,time,resource
signal.alarm(180);t=time.monotonic();n=0
def ck(x):
 global n;n+=1
 if not x:raise ValueError(n)
v=list(product(range(4),repeat=3));E=set()
for x in v:
 for a in range(3):
  y=list(x);y[a]=(y[a]+1)%4;E.add(tuple(sorted((x,tuple(y)))))
def boundary(S):return {e for e in E if (e[0] in S)!=(e[1] in S)}
for k in (1,2,3):
 for S in combinations(v,k):
  b=len(boundary(set(S)));ck(b==6 if k==1 else b in (10,12) if k==2 else b>=14)
def match(es):
 if not es:return 1
 e=es[0];return sum(match(es[1:j]+es[j+1:]) for j in range(1,len(es)) if set(e)&set(es[j]))
classes={}
for w in v[1:]:
 d=sum(min(x,4-x) for x in w)
 if d==1:continue
 m=match(sorted(boundary({v[0],w})));ck(m==(234 if d==2 else 225));classes[str((d,m))]=classes.get(str((d,m)),0)+1
# General parity-trace independence: a product of two distinct bilinears
# has Clifford grade 2 or 4, and complement has grade N-2 or N-4.
for N in (8,64):
 for p,q in combinations(list(combinations(range(N),2)),2):
  grade=len(set(p)^set(q));ck(grade in (2,4) and grade not in (0,N))
r=Path(__file__).parent;r.joinpath('RESULT.json').write_text(json.dumps(dict(checks=n,classes_from_origin=classes,seconds=time.monotonic()-t,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576),indent=2)+'\n')
