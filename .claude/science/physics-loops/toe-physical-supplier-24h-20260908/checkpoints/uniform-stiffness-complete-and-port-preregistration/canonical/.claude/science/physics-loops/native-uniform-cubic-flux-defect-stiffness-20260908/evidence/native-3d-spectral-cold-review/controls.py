"""Exact integer gauge/Bloch controls. No NumPy or eigensolver."""
from pathlib import Path
from itertools import product,permutations
from collections import deque,Counter
import json,time,signal,resource
signal.alarm(180);start=time.monotonic();checks=0
src=Path('/private/tmp/toe-24h-probes-20260908/native-3d-chessboard-spectral-design');data=json.loads((src/'INPUTS.json').read_text());V=list(product(range(4),repeat=3));idx={x:i for i,x in enumerate(V)}
def need(z,s):
 global checks
 checks+=1
 if not z:raise ValueError(s)
def edge(r,a):
 w=list(r);w[a]=(w[a]+1)%4;return idx[r],idx[tuple(w)]
def face(H,r,a,b):
 ra=list(r);ra[a]=(ra[a]+1)%4;rb=list(r);rb[b]=(rb[b]+1)%4
 return H[edge(r,a)]*H[edge(tuple(ra),b)]*H[edge(tuple(rb),a)]*H[edge(r,b)]
def sig(H):
 out=[]
 for n in range(3):
  a,b=[x for x in range(3) if x!=n]
  for side in range(2):r=[0,0,0];r[n]=side;out.append(face(H,tuple(r),a,b))
 return tuple(out)
Hs=[]
for row in data['rows']:
 H={(i,j):s for i,j,d,s in row['terms']};need(len(H)==384,'actual matrix entries')
 need(sig(H)==tuple(row['face_signs']),'internal signature')
 for r in V:
  for a in range(3):
   for b in range(a+1,3):
    if r[a]%2 or r[b]%2:need(face(H,r,a,b)==-1,'crossing canonical')
 Hs.append(H)
lookup={sig(H):i for i,H in enumerate(Hs)};observed=set();twists=Counter()
for rid,H in enumerate(Hs):
 for p in permutations(range(3)):
  for f in product(range(2),repeat=3):
   mapping=[idx[tuple((1-r[p[a]])%4 if f[a] else r[p[a]] for a in range(3))] for r in V]
   transformed={(mapping[i],mapping[j]):s for (i,j),s in H.items()};target=lookup[sig(transformed)];observed.add((rid,target));ratio={e:s*Hs[target][e] for e,s in transformed.items()}
   hol=[]
   for a in range(3):
    z=1
    for x in range(4):r=[0,0,0];r[a]=x;z*=ratio[edge(tuple(r),a)]
    hol.append(z)
   twists[tuple(hol)]+=1
   # Remove the3 seam holonomies, then construct literal periodic site gauge.
   rr={}
   for r in V:
    for a in range(3):
     i,j=edge(r,a);z=ratio[i,j]*(hol[a] if r[a]==3 else 1);rr[i,j]=rr[j,i]=z
   g={0:1};todo=deque([0])
   while todo:
    i=todo.popleft()
    for (k,j),z in rr.items():
     if k!=i:continue
     v=g[i]*z
     if j in g:need(g[j]==v,'flat gauge consistency')
     else:g[j]=v;todo.append(j)
   need(len(g)==64,'gauge coverage')
for row in data['rows']:
 members={j for i,j in observed if i==row['id']}
 declared={q['id'] for q in data['rows'] if q['symmetry_representative']==row['symmetry_representative']}
 need(members==declared,'all actual spatial symmetry classes')
# Finite8x4x4 periodic torus: exact character phases +1/-1 at cell momentum0/pi.
VV=list(product(range(8),range(4),range(4)));II={r:i for i,r in enumerate(VV)}
for rid,H in enumerate(Hs):
 for phase in (1,-1):
  # For each source sublattice column, compare direct finite H acting on Bloch lift.
  for col in range(64):
   for r in VV:
    cell=r[0]//4;s=tuple(x%4 for x in r);actual=0
    for a in range(3):
     for step in (-1,1):
      w=list(r);w[a]=(w[a]+step)%(8,4,4)[a];w=tuple(w);t=tuple(x%4 for x in w)
      if idx[t]==col:actual+=H[idx[s],idx[t]]*phase**(w[0]//4)
    expected=sum(z*phase**d[0] for i,j,d,z in data['rows'][rid]['terms'] if i==idx[s] and j==col)*phase**cell
    need(actual==expected,'finite Bloch intertwining')
print(json.dumps(dict(checks=checks,symmetry_maps=32*48,class_sizes=sorted(Counter(q['symmetry_representative'] for q in data['rows']).values()),gauge_holonomy_counts={str(k):v for k,v in twists.items()},seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,scope='exact geometry/gauge/finite Bloch only, no eigensolver'),indent=2))
