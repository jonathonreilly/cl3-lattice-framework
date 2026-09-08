import time,signal,resource,json,sys,hashlib
start=time.monotonic();signal.alarm(180)
from pathlib import Path
from itertools import product
L=4;verts=list(product(range(L),repeat=3));vid={r:i for i,r in enumerate(verts)};edges=[]
for i,r in enumerate(verts):
 for a in range(3):
  z=list(r);z[a]=(z[a]+1)%L;j=vid[tuple(z)];edges.append(tuple(sorted((i,j))))
edges=sorted(set(edges));E=len(edges);V=len(verts);eid={e:k for k,e in enumerate(edges)};nbr=[sorted(j if i==v else i for i,j in edges if v in (i,j)) for v in range(V)];inc=[sum(1<<k for k,e in enumerate(edges) if v in e) for v in range(V)];eps=[(-1)**sum(r) for r in verts]
w=[];M=[]
for k,(i,j) in enumerate(edges):
 mask=sum(1<<eid[tuple(sorted((i,l)))] for l in nbr[i] if l<j)^sum(1<<eid[tuple(sorted((j,l)))] for l in nbr[j] if l<i);w.append(mask)
 ell=0
 for v in range(i,j):ell^=inc[v]
 M.append(mask^ell)
checks=0
def req(c):
 global checks
 checks+=1
 if not c:raise RuntimeError('native ordered-hole phase check')
req(V==64 and E==192)
req(all(((M[i]>>j)&1)==((M[j]>>i)&1) for i in range(E) for j in range(E)))
upper=[M[i]&~((1<<(i+1))-1) for i in range(E)]
def Q(z):return [eps[i]*((z&inc[i]).bit_count()-3) for i in range(V)]
def dphase(z):
 q=0;b=z
 while b:
  bit=b&-b;i=bit.bit_length()-1;q^=(upper[i]&z).bit_count()%2;b-=bit
 return (-z.bit_count()+2*q)%4
def frame(z,charge):
 x=charge.index(1);y=charge.index(-1);s=(x+y-int(y<x))%2
 return (2*s-dphase(z))%4
seed=0
for k,(i,j) in enumerate(edges):
 ri,rj=verts[i],verts[j];a=next(a for a in range(3) if ri[a]!=rj[a]);root=i if (ri[a]+1)%L==rj[a] else j
 if verts[root][a]%2:seed|=1<<k
req(Q(seed)==[0]*V)
# Directed electric BFS support witness from0 to vertex2 along x-coordinate.
target=vid[(2,0,0)];paths={0:[]};queue=[0]
for i in queue:
 if i==target:break
 for j in nbr[i]:
  k=eid[tuple(sorted((i,j)))];bit=(seed>>k)&1
  if eps[i]*(2*bit-1)==1 and j not in paths:paths[j]=paths[i]+[k];queue.append(j)
z=seed
for k in paths[target]:z^=1<<k
req(sorted(Q(z))==[-1]+[0]*62+[1])
seen={z};front={z};rows=[];wrong_unordered=0
for depth in range(3):
 nxt=set();counts=[]
 for z in front:
  q=Q(z);amp=frame(z,q);degree=0
  for k,(i,j) in enumerate(edges):
   Bi=1 if (z&inc[i]).bit_count()%2==0 else -1;Bj=1 if (z&inc[j]).bit_count()%2==0 else -1
   if Bi==Bj:continue
   zz=z^(1<<k);qq=Q(zz)
   if any(abs(a)>1 for a in qq):continue
   req(sorted(qq)==[-1]+[0]*62+[1]);degree+=1
   tphase=(1+2*((w[k]&z).bit_count()%2)+ (2 if Bi-Bj<0 else 0))%4
   req((amp+tphase-frame(zz,qq))%4==2)
   pos=q.index(1);neg=q.index(-1);pos2=qq.index(1);neg2=qq.index(-1)
   req(eps[pos]*eps[neg]==-eps[pos2]*eps[neg2])
   # Ordinary occupation order omits charge-sign ordering and does not have uniform negative hopping.
   if ((-dphase(z))+tphase+dphase(zz))%4!=2:wrong_unordered+=1
   if zz not in seen:nxt.add(zz)
  req(degree in (6,8));counts.append(degree)
 rows.append(dict(depth=depth,states=len(front),degree6=counts.count(6),degree8=counts.count(8)));seen|=nxt;front=nxt
req(wrong_unordered>0)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);req(0<rss<384)
p=Path(__file__).resolve().parent
print(json.dumps(dict(status='PASS',checks=checks,graph=dict(vertices=V,edges=E),layers=rows,seen_including_next=len(seen),unordered_frame_nonnegative_hop_cases=wrong_unordered,seconds=time.monotonic()-start,peak_MiB=rss,source_sha256={n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ('check.py','DERIVATION.md','PREREGISTRATION.md')},scope='bounded native phase neighborhood, not allD2 configuration census'),indent=2))
