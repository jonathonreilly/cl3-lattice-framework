from itertools import product,combinations,permutations
from pathlib import Path
import json,time,signal,resource,sys
signal.alarm(180);start=time.monotonic();L=6;vs=list(product(range(L),repeat=3));idx={v:i for i,v in enumerate(vs)}
def shift(r,a,k=1):q=list(r);q[a]=(q[a]+k)%L;return tuple(q)
edges=[(idx[r],idx[shift(r,a)]) for r in vs for a in range(3)];E=len(edges)
lookup={frozenset(e):i for i,e in enumerate(edges)}
faces=[];fi={}
for a,b in combinations(range(3),2):
 for r in vs:
  verts=[r,shift(r,a),shift(shift(r,a),b),shift(r,b)];es=[lookup[frozenset((idx[verts[j]],idx[verts[(j+1)%4]]))] for j in range(4)];fi[a,b,r]=len(faces);faces.append(es)
masks=[sum(1<<e for e in es) for es in faces];seed=sum((r[a]%2)<<e for e,(r,a) in enumerate((r,a) for r in vs for a in range(3)))
inc=[[e for e,ends in enumerate(edges) if v in ends] for v in range(len(vs))]
def ice(z):return all(sum(z>>e&1 for e in row)==3 for row in inc)
def legal(z,p):b=[z>>e&1 for e in faces[p]];return all(b[j]!=b[(j+1)%4] for j in range(4))
cubes=[]
for root in vs:
 fs={}
 for axis in range(3):
  a,b=[q for q in range(3) if q!=axis]
  for side in (0,1):fs[axis,side]=fi[a,b,shift(root,axis,side)]
 union=set(e for p in fs.values() for e in faces[p]);cubes.append((root,fs,union))
checks=0;trials=0
def need(v,m):
 global checks
 checks+=1
 if not v:raise RuntimeError(m)
def scan(z,candidates):
 global trials
 for root,fs,_ in candidates:
  for corner in product((0,1),repeat=3):
   menu=[fs[a,corner[a]] for a in range(3)]
   for order in permutations(menu):
    trials+=1;x=z;states=[z]
    for p in order:
     if not legal(x,p):break
     x^=masks[p];states.append(x)
    else:
     if (x^z).bit_count()==6:return root,corner,order,states
 return None
initial=scan(seed,cubes);need(initial is None,'zero-preparation seed fails all cube orders')
found=None;attempted=0
for prep in range(len(faces)):
 if not legal(seed,prep):continue
 attempted+=1;z=seed^masks[prep];near=[c for c in cubes if c[2]&set(faces[prep])]
 result=scan(z,near)
 if result:found=(prep,result);break
one_failed=found is None
two_attempts=0
if found is None:
 for first in range(len(faces)):
  if not legal(seed,first):continue
  z1=seed^masks[first]
  for second in range(len(faces)):
   if second==first or not legal(z1,second):continue
   two_attempts+=1
   result=scan(z1^masks[second],[c for c in cubes if c[2]&set(faces[second])])
   if result:found=(first,result);second_prep=second;break
  if found:break
if found is None:raise RuntimeError('bounded two-flip search failed')
prep,(root,corner,order,states)=found
prep_tape=[prep]+([second_prep] if one_failed else [])
z=seed
for p in prep_tape:
 need(legal(z,p),'legal preparation tape');z^=masks[p]
need(z==states[0],'preparation reaches witness')
for z in [seed]+states:need(ice(z),'full ice state')
changed=[e for e in range(E) if (states[-1]^states[0])>>e&1];remaining=set(changed);here=min(v for e in changed for v in edges[e]);initialv=here;cycle=[]
while remaining:
 e=next(e for e in sorted(remaining) if here in edges[e]);remaining.remove(e);cycle.append(e);here=next(v for v in edges[e] if v!=here)
need(here==initialv and len(cycle)==6,'simple closing cycle')
phase_masks=[sum(1<<f for f in range(e) if set(edges[e])&set(edges[f])) for e in range(E)]
def act(z,es):
 amp=1
 for e in es:amp*=(-1)**((phase_masks[e]&z).bit_count());z^=1<<e
 return z,amp
amps=[]
for j,p in enumerate(order):
 z,s=act(states[j],faces[p]);need(z==states[j+1],'actual native face endpoint');amps.append(s)
z,s=act(states[-1],cycle);need(z==states[0],'actual native hexagon closure');amps.append(s)
sgn=-1
for a in amps:sgn*=a
need(sgn==-1,'negative closed effective product')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);need(rss<384 and time.monotonic()-start<180,'resources')
r=dict(L=L,checks=checks,zero_prep_complete=True,one_prep_attempts=attempted,cube_order_trials=trials,one_flip_failed=one_failed,two_prep_attempts=two_attempts,preparation_faces=prep_tape,preparation_edges=[faces[p] for p in prep_tape],cube_root=root,corner=corner,face_order=order,face_edges=[faces[p] for p in order],six_cycle=cycle,seed_bits=[seed>>e&1 for e in range(E)],loop_states=[[z>>e&1 for e in range(E)] for z in states],native_B_phases=amps,effective_sign_product=sgn,seconds=time.monotonic()-start,rss_mib=rss)
Path(__file__).with_name('RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k not in ['seed_bits','loop_states']},indent=2))
