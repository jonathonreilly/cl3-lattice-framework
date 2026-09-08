from itertools import product,permutations
from pathlib import Path
import json,time
start=time.monotonic();L=4;verts=list(product(range(L),repeat=3));idx={v:i for i,v in enumerate(verts)};edges=[];bits=[]
for v in verts:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%L;edges.append((idx[v],idx[tuple(w)]));bits.append(v[a]%2)
lookup={frozenset(e):i for i,e in enumerate(edges)}
def edge(v,w):return lookup[frozenset((idx[tuple(v)],idx[tuple(w)]))]
def face(a,b,fix):
 vs=[]
 for x,y in [(0,0),(1,0),(1,1),(0,1)]:
  v=list(fix);v[a]=x;v[b]=y;vs.append(v)
 return [edge(vs[i],vs[(i+1)%4]) for i in range(4)]
faces={}
for axis in range(3):
 for side in (0,1):
  axes=[a for a in range(3) if a!=axis];v=[0]*3;v[axis]=side;faces[axis,side]=face(*axes,v)
masks=[sum(1<<f for f in range(e) if set(edges[e])&set(edges[f])) for e in range(len(edges))]
seed=sum(x<<e for e,x in enumerate(bits));inc=[[e for e,ends in enumerate(edges) if v in ends] for v in range(64)]
def legal(z):return all(sum(z>>e&1 for e in row)==3 for row in inc)
def act(z,es):
 phase=1
 for e in es:phase*=(-1)**((masks[e]&z).bit_count());z^=1<<e
 return z,phase
found=None
for corner in product((0,1),repeat=3):
 fs=[faces[a,corner[a]] for a in range(3)]
 for order in permutations(range(3)):
  z=seed;states=[z];amps=[]
  for j in order:
   zz,s=act(z,fs[j])
   if not legal(zz):break
   z=zz;states.append(z);amps.append(s)
  else:
   changed=[e for e in range(192) if (z^seed)>>e&1]
   # Order actual six boundary edges by connected traversal.
   if len(changed)!=6:continue
   here=min(v for e in changed for v in edges[e]);initial=here;remaining=set(changed);cy=[]
   while remaining:
    e=next(e for e in sorted(remaining) if here in edges[e]);cy.append(e);remaining.remove(e);here=next(v for v in edges[e] if v!=here)
   if here!=initial:raise RuntimeError('not cycle')
   back,s=act(z,cy)
   if back!=seed:raise RuntimeError('not closed')
   product_sign=-s
   for a in amps:product_sign*=a
   found=dict(corner=corner,face_order=order,faces=[fs[j] for j in order],states=[[state>>e&1 for e in range(192)] for state in states],six_cycle=cy,native_B_phases=amps+[s],effective_edge_signs=amps+[-s],closed_product=product_sign)
   break
 if found:break
if found is None:raise RuntimeError('seed no witness')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(dict(witness=found,seconds=time.monotonic()-start),indent=2)+'\n');print({k:v for k,v in found.items() if k!='states'})
