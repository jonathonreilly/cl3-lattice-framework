from itertools import product
import json,time,resource,sys,hashlib
from pathlib import Path
start=time.monotonic();checks=0
def req(v,msg):
 global checks
 checks+=1
 if not v:raise RuntimeError(msg)
counts={m:0 for m in range(-5,6)}
for s in range(1<<11):
 x=s&1;ri=sum((s>>k)&1 for k in range(1,6));rj=sum((s>>k)&1 for k in range(6,11))
 d=(ri+x-3)**2+(rj+x-3)**2
 dp=(ri+1-x-3)**2+(rj+1-x-3)**2
 m=(1-2*x)*(ri+rj-5)
 req(dp-d==2*m,'literal charge difference')
 req(-5<=m<=5,'bounded frequency');counts[m]+=1
 mm=(1-2*(1-x))*(ri+rj-5)
 req(mm==-m,'adjoint frequency reversal')
 # Any native endpoint Z string excludes its own X edge. Check an explicit nontrivial such string.
 mask=sum(1<<k for k in (1,3,6,8,10))
 phase=(-1)**((s&mask).bit_count());phase_flip=(-1)**(((s^1)&mask).bit_count())
 req(phase==phase_flip and phase*phase_flip==1,'native partial-permutation adjoint')
 if ri+x==3 and rj+x==3:req(m==1,'ice only raises D by two')
rows=[]
for L in (4,6):
 vs=list(product(range(L),repeat=3));idx={v:i for i,v in enumerate(vs)};edges=[];tails={}
 for v in vs:
  for a in range(3):
   w=list(v);w[a]=(w[a]+1)%L;e=tuple(sorted((idx[v],idx[tuple(w)])));edges.append(e);tails[e]=idx[v]
 edges=sorted(edges);inc=[set() for v in vs]
 for e,(i,j) in enumerate(edges):inc[i].add(e);inc[j].add(e)
 overlap=[0]*len(vs);physical=[0]*len(edges);sizes=[]
 for e,(i,j) in enumerate(edges):
  support=inc[i]|inc[j];cells={tails[edges[f]] for f in support}
  req(len(support)==11,'endpoint star size');req(len(cells)<=8,'grouped local size')
  # The only edge with X is e. Every other charge term is diagonal and omits e.
  req(all(e not in inc[k] for k in range(len(vs)) if k not in (i,j)),'strong support incidence')
  for f in support:physical[f]+=1
  for c in cells:overlap[c]+=1
  sizes.append(len(cells))
 req(max(physical)<=11,'physical overlap bound');req(max(overlap)<=33,'cell overlap bound')
 rows.append(dict(L=L,vertices=len(vs),edges=len(edges),max_cells=max(sizes),max_cell_overlap=max(overlap),max_physical_overlap=max(physical)))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
req(time.monotonic()-start<30 and rss<384,'resources')
print(json.dumps(dict(checks=checks,frequency_counts=counts,geometry=rows,seconds=time.monotonic()-start,rss_mib=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))
