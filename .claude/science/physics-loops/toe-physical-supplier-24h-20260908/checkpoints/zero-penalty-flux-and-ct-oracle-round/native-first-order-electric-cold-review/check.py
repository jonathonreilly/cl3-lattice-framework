from itertools import combinations,product
from fractions import Fraction as F
import json,time
from pathlib import Path
st=time.monotonic();n=0
def check(c,m):
 global n
 if not c:raise RuntimeError(m)
 n+=1
rows=[]
for name,v,edges in [('square',4,[(0,1),(1,2),(2,3),(0,3)]),('K4',4,list(combinations(range(4),2)))]:
 stars=[sum(1<<e for e,(a,b) in enumerate(edges) if i in (a,b)) for i in range(v)]
 # Literal normalized Gauss orbit in X-link basis; unnormalized coefficients +/-1, norm2=v-1.
 vals=[]
 for occ in range(1<<v):
  if occ.bit_count()%2:continue
  state={}
  for S in range(1<<(v-1)):
   bits=0
   for i in range(v-1):
    if S>>i&1:bits^=stars[i]
   state[bits]=(-1)**((S&occ).bit_count())
  check(len(state)==1<<(v-1),'orbit injective')
  out={b:F(len(edges),2)*a for b,a in state.items()}
  for i in range(v):
   for e,f in combinations([e for e in range(len(edges)) if stars[i]>>e&1],2):
    for b,a in state.items():out[b^(1<<e)^(1<<f)]=out.get(b^(1<<e)^(1<<f),F(0))+F(a,2)
  val=sum(state.get(b,0)*a for b,a in out.items())/len(state);vals.append(str(val))
  check(val== (F(3) if name=='K4' else (F(4) if occ==0 else F(0) if occ==15 else F(2))),'literal Gauss D compression')
 rows.append({'graph':name,'values':vals})
# Four edge-disjoint detours on unequal even extents, each including seam cases.
L=(4,6,4);coords=list(product(*(range(l) for l in L)))
def shift(r,a,k):
 s=list(r);s[a]=(s[a]+k)%L[a];return tuple(s)
for r in coords:
 for a in range(3):
  end=shift(r,a,1);used=set();direct=frozenset((r,end))
  for b in range(3):
   if a==b:continue
   for sign in [-1,1]:
    p=[r,shift(r,b,sign),shift(end,b,sign),end]
    es={frozenset((p[k],p[k+1])) for k in range(3)}
    check(len(es)==3 and direct not in es and not used.intersection(es),'four disjoint detours');used|=es
Path(__file__).with_name('RESULT.json').write_text(json.dumps({'checks':n,'rows':rows,'seconds':time.monotonic()-st},indent=2)+'\n')
