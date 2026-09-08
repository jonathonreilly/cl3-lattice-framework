from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,time,hashlib,resource,sys
start=time.monotonic();checks=0
def req(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
V=F(19,20);M=2;degree=(1,2,1)
G=[[F(0) for j in range(3)] for i in range(3)]
for i in range(3):
 G[i][i]=1-V*degree[i]/M
 for j in range(3):
  if abs(i-j)==1:G[i][j]=F(1,M)
def weight(x,g):
 w=F(1)
 for a,b in zip(x,x[1:]):w*=g[a][b]
 return w
paths={x:weight(x,G) for x in product(range(3),repeat=4) if weight(x,G)>0}
rows=[];biased=0;aliasclasses=0
for inv in ((1,0,2),(0,2,1)):
 classes={}
 for x,w in paths.items():
  key=tuple(min(z,inv[z]) for z in x);classes.setdefault(key,{})[x]=w
 for key,group in classes.items():
  orbit=[sorted({z,inv[z]}) for z in key];Z=sum(group.values());back=[[F(1) for z in orbit[-1]]]
  for k in range(2,-1,-1):back.append([sum(G[a][b]*back[-1][j] for j,b in enumerate(orbit[k+1])) for a in orbit[k]])
  back.reverse();req(sum(back[0])==Z,'exact orbit partition')
  forward=[[F(1) for z in orbit[0]]]
  for k in range(3):forward.append([sum(forward[k][i]*G[a][b] for i,a in enumerate(orbit[k])) for b in orbit[k+1]])
  for k,states in enumerate(orbit):
   for i,a in enumerate(states):req(forward[k][i]*back[k][i]/Z==sum(w for x,w in group.items() if x[k]==a)/Z,'exact slice marginal')
  # Duplicate representations at fixed slices only. Every physical path has common2^fixed multiplicity.
  dup=[[z,inv[z]] for z in key];agg={}
  for indices in product((0,1),repeat=4):
   path=tuple(dup[k][j] for k,j in enumerate(indices));w=weight(path,G)
   if w:agg[path]=agg.get(path,F(0))+w
  factor=2**sum(len(o)==1 for o in orbit);req(agg=={x:factor*w for x,w in group.items()},'singleton aliases common factor')
  req(all(agg[x]/sum(agg.values())==w/Z for x,w in group.items()),'singleton pushforward law unchanged');aliasclasses+=int(factor>1)
  wrong=[[G[a][b] if a!=b else F(1) for b in range(3)] for a in range(3)];bad={x:weight(x,wrong) for x in group};badZ=sum(bad.values())
  biased+=int(any(w/Z!=bad[x]/badZ for x,w in group.items()))
 rows.append(dict(involution=inv,classes=len(classes)))
req(biased>0,'missing diagonal is actual biased mutant')
req(aliasclasses>0,'nonempty singleton controls')
# Parallel geometric labels must aggregate in the physical offdiagonal G.
req(F(2,M)==1 and F(1,M)!=1,'offdiagonal label multiplicity')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
req(time.monotonic()-start<30 and rss<384,'resources')
print(json.dumps(dict(checks=checks,positive_paths=len(paths),rows=rows,biased_diagonal_classes=biased,harmless_singleton_alias_classes=aliasclasses,seconds=time.monotonic()-start,rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))
