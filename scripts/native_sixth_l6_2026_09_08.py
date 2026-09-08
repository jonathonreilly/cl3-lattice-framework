"""Portable exact sixth-order control; original source preserved in packet."""
AUDIT_TIMEOUT_SEC=180
import argparse,signal
if __name__=='__main__':
 signal.alarm(AUDIT_TIMEOUT_SEC)
 p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');p.parse_args()
from itertools import product,permutations
from pathlib import Path
import json,time
start=time.monotonic();L=6;verts=list(product(range(L),repeat=3));idx={v:i for i,v in enumerate(verts)};edges=[];bits=[]
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
seed=sum(x<<e for e,x in enumerate(bits));inc=[[e for e,ends in enumerate(edges) if v in ends] for v in range(len(verts))]
def legal(z):return all(sum(z>>e&1 for e in row)==3 for row in inc)
def act(z,es):
 phase=1
 for e in es:phase*=(-1)**((masks[e]&z).bit_count());z^=1<<e
 return z,phase

# Find a degree-three global completion of fixed cube-edge bits by integral flow.
def complete(fixed):
 demand=[3]*len(verts)
 for e,b in fixed.items():
  for v in edges[e]:demand[v]-=b
 if any(d<0 for d in demand):return None
 src,sink=len(verts),len(verts)+1;adj=[[] for _ in range(len(verts)+2)]
 def add(a,b,c):
  adj[a].append([b,c,len(adj[b])]);adj[b].append([a,0,len(adj[a])-1]);return len(adj[a])-1
 for v in range(len(verts)):
  if sum(verts[v])%2==0:add(src,v,demand[v])
  else:add(v,sink,demand[v])
 refs={}
 for e,(a,b) in enumerate(edges):
  if e in fixed:continue
  if sum(verts[a])%2:a,b=b,a
  refs[e]=(a,add(a,b,1))
 flow=0
 while True:
  parent={src:None};queue=[src]
  for a in queue:
   for j,(b,c,_) in enumerate(adj[a]):
    if c and b not in parent:parent[b]=(a,j);queue.append(b)
   if sink in parent:break
  if sink not in parent:break
  z=sink
  while z!=src:
   a,j=parent[z];entry=adj[a][j];entry[1]-=1;adj[z][entry[2]][1]+=1;z=a
  flow+=1
 if flow!=sum(demand[v] for v in range(len(verts)) if sum(verts[v])%2==0):return None
 values=dict(fixed)
 for e,(a,j) in refs.items():values[e]=1-adj[a][j][1]
 z=sum(b<<e for e,b in values.items())
 return z if legal(z) else None
cube=sorted(set(e for fs in faces.values() for e in fs))
chosen=None
for word in product((0,1),repeat=12):
 fixed=dict(zip(cube,word))
 # Test local degree preservation at each face transition before max flow.
 for corner in product((0,1),repeat=3):
  fs=[faces[a,corner[a]] for a in range(3)]
  for order in permutations(range(3)):
   trial=fixed.copy();ok=True
   for j in order:
    if not all(trial[fs[j][k]]!=trial[fs[j][(k+1)%4]] for k in range(4)):ok=False;break
    for e in fs[j]:trial[e]^=1
   if ok:
    z=complete(fixed)
    if z is not None:chosen=z;break
  if chosen is not None:break
 if chosen is not None:break
if chosen is None:raise RuntimeError('no exact completion')
seed=chosen

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
   changed=[e for e in range(len(edges)) if (z^seed)>>e&1]
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
   found=dict(corner=corner,face_order=order,faces=[fs[j] for j in order],states=[[state>>e&1 for e in range(len(edges))] for state in states],six_cycle=cy,native_B_phases=amps+[s],effective_edge_signs=amps+[-s],closed_product=product_sign)
   break
 if found:break
if found is None:raise RuntimeError('seed no witness')

# New prospective explicit delivered-witness predicates; original search guards remain uncounted.
checks=0
def need(v,label):
 global checks
 checks+=1
 if not v:raise RuntimeError(label)
for bs in found['states']:need(legal(sum(bit<<e for e,bit in enumerate(bs))),'delivered full ice state')
for es in found['faces']:
 need(len(es)==4 and len(set(es))==4,'four distinct face edges')
need(len(found['six_cycle'])==6 and len(set(found['six_cycle']))==6,'six distinct closing edges')
need(found['closed_product']==-1,'negative closed effective sign')

(Path(__file__).resolve().parents[1]/'outputs/native_sixth_l6_2026_09_08.json').write_text(json.dumps(dict(checks=checks,witness=found,seconds=time.monotonic()-start),indent=2)+'\n');print({k:v for k,v in found.items() if k!='states'})
