from itertools import product,combinations
from fractions import Fraction
from pathlib import Path
import json,time,signal,resource
signal.alarm(180);start=time.monotonic();checks=0
def need(c,s):
 global checks
 checks+=1
 if not c:raise RuntimeError(s)
vs=list(product(range(4),repeat=3));ix={v:i for i,v in enumerate(vs)};N=len(vs)
def step(v,a,k=1):return tuple((v[b]+(k if b==a else 0))%4 for b in range(3))
edges=[(v,a,step(v,a)) for v in vs for a in range(3)]
base=[(-1)**sum(v[:a]) for v,a,w in edges]
def matrix(signs):
 K=[[0]*N for _ in vs]
 for (v,a,w),s in zip(edges,signs):
  i,j=sorted((ix[v],ix[w]));K[i][j]=-2*s;K[j][i]=2*s
 return [[-sum(K[i][k]*K[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def hol(signs,c):
 z=1
 for v,w in zip(c,c[1:]+c[:1]):
  e=next(e for e,(u,a,q) in enumerate(edges) if {u,q}=={v,w})
  # iK/2 phase = -i sign in canonical ordering.
  z*=(-1j if ix[v]<ix[w] else 1j)*signs[e]
 return z
cycles=[]
for v in vs:
 for a,b in combinations(range(3),2):cycles.append((v,step(v,a),step(step(v,a),b),step(v,b)))
for a in range(3):
 for v in vs:
  if v[a]==0:cycles.append(tuple(step(v,a,k) for k in range(4)))
A=matrix(base)
need(all(A[i][j]==24*(i==j) for i in range(N) for j in range(N)),'base square flat')
need(all(hol(base,c)==-1 for c in cycles),'base all basic hopping flux pi')
# Independent graph path multiplicities, including every seam.
adj=[set() for _ in vs]
for v,a,w in edges:adj[ix[v]].add(ix[w]);adj[ix[w]].add(ix[v])
for i in range(N):
 for j in range(N):
  q=len(adj[i]&adj[j]);need(q in (0,2,6),'two-step multiplicity')
  if i!=j and q:need(q==2,'exact two intermediates')
fixtures=[]
for label,flips in [('one-edge-'+str(e),[e]) for e in (0,3,47,191)]+[('axis-twist-'+str(a),[e for e,(v,b,w) in enumerate(edges) if a==b and v[a]==3]) for a in range(3)]:
 signs=base.copy()
 for e in flips:signs[e]*=-1
 B=matrix(signs);off=[B[i][j] for i in range(N) for j in range(N) if i!=j and B[i][j]]
 variance=sum((B[i][j]-24*(i==j))**2 for i in range(N) for j in range(N))
 need(all(B[i][i]==24 for i in range(N)),'trace fixed')
 need(bool(off) and set(off)<={-8,8},'wrong sector nonzero entries')
 need(variance>=128,'variance floor')
 wrong=[k for k,c in enumerate(cycles) if hol(signs,c)!=-1]
 need(bool(wrong),'noncanonical basic flux')
 if label.startswith('axis'):need(all(k>=192 for k in wrong),'winding-only adverse test')
 fixtures.append({'label':label,'flipped_edges':flips,'wrong_basic_cycles':wrong,'variance':variance,'nonzero_offdiagonal':len(off)})
need(Fraction(128,8*144*12)==Fraction(1,108),'concavity slack')
need(Fraction(1,108)/4==Fraction(1,432),'native energy factor')
print(json.dumps({'checks':checks,'status':'PASS','fixtures':fixtures,'seconds':time.monotonic()-start,'rss_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,'scope':'Exact integer square matrices and basic flux controls; no all-sector eigensolver'},indent=2))
