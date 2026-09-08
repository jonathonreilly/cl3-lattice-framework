from fractions import Fraction as F
from itertools import product
from pathlib import Path
import time,json,signal
signal.alarm(180);start=time.monotonic();vs=list(product(range(4),repeat=3));ix={v:i for i,v in enumerate(vs)};K=[[0]*64 for _ in vs]
for r in vs:
 for a in range(3):
  q=list(r);q[a]=(q[a]+1)%4;i,j=sorted((ix[r],ix[tuple(q)]));K[i][j]=-2*(-1)**sum(r[:a]);K[j][i]=-K[i][j]
def span(S):
 cols=[]
 for v in sorted(S):cols.extend([[F(i==v) for i in range(64)],[F(K[i][v]) for i in range(64)]])
 basis={}
 for col in cols:
  for i,b in basis.items():
   z=col[i]
   if z:col=[x-z*y for x,y in zip(col,b)]
  i=next((i for i,x in enumerate(col) if x),None)
  if i is not None:
   z=col[i];basis[i]=[x/z for x in col]
 return list(basis.values())
rows=[]
for coord in [(1,0,0),(1,1,1),(2,1,0),(2,2,1)]:
 v,w=0,ix[coord];Sv={v}|{i for i in range(64) if K[i][v]};Sw={w}|{i for i in range(64) if K[i][w]};a,b=span(Sv),span(Sw);dim=len(span(Sv|Sw));cross=sum(bool(sum(x*y for x,y in zip(c,d))) for c in a for d in b)
 rows.append(dict(displacement=coord,vertex=w,star_ranks=[len(a),len(b)],union_rank=dim,parity_fock_dimension=2**(dim//2-1),nonzero_cross_gram=cross))
out=dict(rows=rows,seconds=time.monotonic()-start,scope='exact rank only; no linkedcluster or coefficient inference');Path(__file__).with_name('RANK_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
