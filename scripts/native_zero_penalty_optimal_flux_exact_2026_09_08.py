from itertools import product,combinations
from collections import Counter
from pathlib import Path
import json,time,resource,signal,sys
N=0;start=time.monotonic()
if __name__=='__main__':signal.alarm(180)
def need(c,m):
 global N;N+=1
 if not c:raise ValueError(m)

def convolve(a,b):
 c=Counter()
 for x,m in a.items():
  for y,n in b.items():c[x+y]+=m*n
 return c
# Formal partition Laurent coefficients: no decimal exponentials/frequency fits.
patterns=[]
for vertices,freqs in [(2,[]),(2,[1]),(4,[1]),(4,[1,2]),(6,[]),(6,[1,1,3])]:
 r=len(freqs);native=Counter({0:2**(vertices-r-1)})
 for w in freqs:native=convolve(native,Counter({-w:1,w:1}))
 aux=Counter({0:2**(vertices-2*r)})
 for w in freqs:aux=convolve(aux,Counter({-2*w:1,0:2,2*w:1}))
 squared=convolve(native,native)
 need(squared==Counter({k:2**(vertices-2)*v for k,v in aux.items()}),'physical versus auxiliary partition')
 need(sum(native.values())==2**(vertices-1) and sum(aux.values())==2**vertices,'dimensions inclzero')
 need(min(aux)==2*min(native),'groundfactor')
 patterns.append(dict(vertices=vertices,frequencies=freqs,native=dict(native),auxiliary=dict(aux)))
fixtures=[]
for dims in [(4,4,4),(6,6,6),(4,6,8)]:
 vs=list(product(*(range(L) for L in dims)));idx={v:i for i,v in enumerate(vs)}
 def shift(v,a):q=list(v);q[a]=(q[a]+1)%dims[a];return tuple(q)
 edges=[(v,shift(v,a),a) for v in vs for a in range(3)];edgekeys={frozenset((u,v)) for u,v,a in edges}
 xi={frozenset((u,v)):(-1)**sum(u[:a]) for u,v,a in edges}
 cycles=[]
 for v in vs:
  for a,b in combinations(range(3),2):cycles.append((v,shift(v,a),shift(shift(v,a),b),shift(v,b)))
 for a in range(3):
  for v in vs:
   if v[a]:continue
   cyc=[];u=v
   for _ in range(dims[a]):cyc.append(u);u=shift(u,a)
   cycles.append(tuple(cyc))
 wrong=0
 for c in cycles:
  eta=1;hol=1
  for u,v in zip(c,c[1:]+c[:1]):eta*=1 if idx[u]<idx[v] else -1;hol*=xi[frozenset((u,v))]
  hopping=(-1)**(len(c)//2)*eta*hol
  need(hopping==(-1)**(len(c)//2-1),'all canonical basic cycle phases')
  need(hol==(-1 if len(c)==4 and eta==1 else 1),'native magnetic sectors')
  if (-1)**(len(c)//2)*eta!=(-1)**(len(c)//2-1):wrong+=1
 need(wrong>0,'wrong trivial background actual noncanonical square')
 reflections=0;crossings=0
 for a,L in enumerate(dims):
  for s in range(L//2):
   def reflect(v):q=list(v);q[a]=(2*s+1-q[a])%L;return tuple(q)
   # Half contiguous vertices from s+1 through s+L/2; reflection exchanges it.
   half=lambda v:1<=((v[a]-s)%L)<=L//2
   need(all(reflect(v)!=v and reflect(reflect(v))==v and half(reflect(v))!=half(v) for v in vs),'fixedpointfree bipartition reflection')
   need(all(frozenset((reflect(u),reflect(v))) in edgekeys for u,v,_ in edges),'graph magnitude symmetry')
   for c in cycles:
    if len({half(v) for v in c})==2:
     ce={frozenset((u,v)) for u,v in zip(c,c[1:]+c[:1])}
     rc={frozenset((reflect(u),reflect(v))) for u,v in zip(c,c[1:]+c[:1])}
     need(ce==rc,'every crossing basic circuit invariant');crossings+=1
   reflections+=1
 fixtures.append(dict(extents=dims,vertices=len(vs),basic_cycles=len(cycles),reflections=reflections,crossing_invariances=crossings,wrong_trivial_background_cycles=wrong))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
need(rss<384,'RSS cap')
out=dict(checks=N,partition_controls=patterns,torus_controls=fixtures,seconds=time.monotonic()-start,rss_mib=rss,scope='exact objective identity and theorem assumption fixtures; no numerical optimization or phase claim')
if __name__=='__main__':print(json.dumps(out,indent=2))
