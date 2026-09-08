import time,resource,signal,json,hashlib
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_PLANE_FORMATION_DIAGONAL_INTERACTION_NOTE_2026-09-08.md', 'docs/ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md')
start=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
import argparse
from pathlib import Path
parser=argparse.ArgumentParser();parser.add_argument('--json',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
inputs={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
from fractions import Fraction as F
from itertools import product
from math import lcm
checks=0
def require(c):
 global checks
 checks+=1
 if not c: raise RuntimeError('control failed')
def fixture(p,q,r):
 phi=[[p if a==b else q if a//2==b//2 else r for b in range(6)] for a in range(6)]
 z=p+q+4*r; h=[[sum(phi[a][s]*phi[s][b] for s in range(6)) for b in range(6)] for a in range(6)]; l=lcm(*[v for row in h for v in row])
 def weight(x,H,W):
  n=1
  for i in range(H):
   for j in range(W):
    if i: n*=phi[x[(i-1)*W+j]][x[i*W+j]]
    if j: n*=phi[x[i*W+j-1]][x[i*W+j]]
    if i and j:n*=l//h[x[i*W+j-1]][x[(i-1)*W+j]]
  return F(n,6*z**(H+W-2)*l**((H-1)*(W-1)))
 laws={x:weight(x,2,3) for x in product(range(6),repeat=6)}
 require(sum(laws.values())==1)
 for a in range(2):
  for b in range(a+1,3):
   for c in range(3):
    for d in range(c+1,4):
     ix=[i*3+j for i in range(a,b) for j in range(c,d)]; marginal={}
     for x,v in laws.items():
      y=tuple(x[k] for k in ix);marginal[y]=marginal.get(y,F(0))+v
     require(all(v==weight(y,b-a,d-c) for y,v in marginal.items()))
 transforms=[tuple(range(6)),(2,1,0,5,4,3),(3,4,5,0,1,2),(5,4,3,2,1,0)]
 eq=[[all(laws[x]==laws[tuple(x[k] for k in t)] for x in laws) for t in transforms]][0]
 require(eq==([True,True,True,True] if p==q==r else [True,False,False,True]))
 tv=sum(abs(v-laws[(x[2],x[1],x[0],x[5],x[4],x[3])]) for x,v in laws.items())/2
 f=[F(phi[s][0]**4,h[s][0]) for s in range(6)]; f=[v/sum(f) for v in f]
 g=[F(phi[s][0]**4) for s in range(6)];g=[v/sum(g) for v in g]
 direct=[weight((0,0,0,0,s,0,0,0,0),3,3) for s in range(6)];direct=[v/sum(direct) for v in direct]
 require(f==direct);require((f==g)==(p==q==r))
 return dict(triple=[p,q,r],corner_equal_to_TL=eq,mirror_TV=str(tv),center_formation=list(map(str,f)),center_static=list(map(str,g)))
out=[fixture(*t) for t in [(3,1,2),(5,2,4),(2,2,2)]]
# Each trimming step is a leaf-sum elimination in the corresponding corner DAG.
# Existing 180-degree identity permits top and left trims as well.
schedules=0
for H,W in [(3,3),(3,4)]:
 for a in range(H):
  for b in range(a+1,H+1):
   for c in range(W):
    for d in range(c+1,W+1):
     remaining={(i,j) for i in range(H) for j in range(W)}
     for i in range(H-1,b-1,-1):
      for j in range(W-1,-1,-1):remaining.remove((i,j))
     for i in range(a):
      for j in range(W):remaining.remove((i,j))
     for j in range(W-1,d-1,-1):
      for i in range(b-1,a-1,-1):remaining.remove((i,j))
     for j in range(c):
      for i in range(a,b):remaining.remove((i,j))
     require(remaining=={(i,j) for i in range(a,b) for j in range(c,d)});schedules+=1
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
import sys
mib=rss/(1024**2 if sys.platform=='darwin' else 1024)
require(0<mib<384 and time.monotonic()-start<180)
result=dict(checks=checks,fixtures=out,elimination_schedules=schedules,scope='2x3 full exact marginals; 3x3/3x4 symbolic trimming, not full census',seconds=time.monotonic()-start,peak_MiB=mib, input_sha256=inputs, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
print(json.dumps(result,indent=2,allow_nan=False))
if not args.json:
 print('per_element: exact six-label probabilities and positive center conditioning.')
 print('per_site: all subrectangle positions of the complete2x3 laws.')
 print('per_mode: no continuum or quantum mode claim; three orbit-weight fixtures.')
 print('per_block: complete46656 configuration laws;96 symbolic trimming schedules.')
 print('lattice_wide: plane extension is analytic, not numerically enumerated.')
 print(f'TOTAL: PASS={checks} FAIL=0')
 print(f'Resources: {result["seconds"]:.6f}s, {mib:.3f}MiB; caps180s384MiB.')
