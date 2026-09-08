from pathlib import Path
from fractions import Fraction as F
import itertools,json,hashlib
P=Path('/private/tmp/toe-24h-probes-20260908/native-full-eighth-diagonal');rows=json.loads((P/'RESULT.json').read_text())['rows'];checks=0
shapes={'cycle4':[(0,1),(1,2),(2,3),(3,0)],'path4':[(0,1),(1,2),(2,3),(3,4)],'fork4':[(0,1),(0,2),(0,3),(3,4)]}
def energy(edges,bits,z):
 return sum(sum((1-2*bits[e]) for e,ends in enumerate(edges) if v in ends and z>>e&1)**2 for v in set(sum(([a,b] for a,b in edges),[])))
def hop(edges,z,e):
 # Reverse local edge ordering relative to author.
 return z^(1<<e),(-1)**sum(bool(z>>f&1) for f in range(e+1,len(edges)) if set(edges[e])&set(edges[f]))
def recurrence(en,V):
 size=len(en);psi=[[F(int(i==0)) for i in range(size)]];E=[F(0)]
 for n in range(1,9):
  v=[sum(V[i][j]*psi[-1][j] for j in range(size)) for i in range(size)];E.append(v[0]);psi.append([F(0)]+[(sum(E[k]*psi[n-k][i] for k in range(1,n))-v[i])/en[i] for i in range(1,size)])
 return E[8]
def coeff(edges,bits):
 N=1<<len(edges);en=[energy(edges,bits,z) for z in range(N)]
 if en.count(0)==1:
  V=[[0]*N for _ in range(N)]
  for z in range(N):
   for e in range(len(edges)):
    y,s=hop(edges,z,e);V[y][z]+=s
  return recurrence(en,V)
 # Independent rank-two extraction: split exact commuting full-toggle symmetry.
 if not (en.count(0)==2 and len(edges)==4):raise RuntimeError('rank')
 def full(z):
  sign=1
  for e in range(4):z,s=hop(edges,z,e);sign*=s
  return z,sign
 total=F(0)
 for sector in (-1,1):
  V=[[0]*8 for _ in range(8)]
  for z in range(8):
   for e in range(4):
    y,s=hop(edges,z,e)
    if y>=8:y^=15;s*=sector*full(y)[1]
    V[y][z]+=s
  if not all(V[i][j]==V[j][i] for i in range(8) for j in range(8)):raise RuntimeError('Hermitian')
  total+=recurrence(en[:8],V)
 return total/2
out=[]
for shape,bits in [('cycle4',(0,0,0,0)),('cycle4',(0,0,0,1)),('cycle4',(0,0,1,1)),('cycle4',(0,1,0,1)),('path4',(0,1,0,1)),('path4',(0,0,0,0)),('fork4',(1,0,1,0))]:
 edges=shapes[shape];c=F(0)
 for mask in range(1,16):
  ids=[i for i in range(4) if mask>>i&1];c+=(-1)**(4-len(ids))*coeff([edges[i] for i in ids],[bits[i] for i in ids])
 row=next(r for r in rows if r['shape']==shape and tuple(r['bits'])==bits);
 if c!=F(row['connected8']):raise RuntimeError('coefficient')
 checks+=1;out.append(dict(shape=shape,bits=bits,connected8=str(c)))
Path(__file__).with_name('RESULT.json').write_text(json.dumps(dict(checks=checks,rows=out,scope='Independent reversed-edge-phase recurrence; rank-two cycle split by exact symmetry, no contour implementation reused'),indent=2)+'\n');print(out)
