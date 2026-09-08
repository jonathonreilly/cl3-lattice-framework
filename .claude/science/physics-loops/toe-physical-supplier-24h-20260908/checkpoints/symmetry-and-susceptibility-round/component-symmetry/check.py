import itertools,json,time,resource,sys
from pathlib import Path
start=time.monotonic()
def geometry(L):
 rs=list(itertools.product(range(L),repeat=3));links=[(r,a) for r in rs for a in range(3)];ix={x:i for i,x in enumerate(links)};faces=[];labels=[]
 for a,b in itertools.combinations(range(3),2):
  for r in rs:
   ra=list(r);rb=list(r);ra[a]=(ra[a]+1)%L;rb[b]=(rb[b]+1)%L
   faces.append([ix[r,a],ix[tuple(ra),b],ix[tuple(rb),a],ix[r,b]]);labels.append((a,b,r))
 return rs,links,ix,faces,labels
def flipok(x,f):
 z=[(x>>i)&1 for i in f];return z in ([0,1,0,1],[1,0,1,0])
rs,links,ix,faces,labels=geometry(2);seed=sum((r[a]%2)<<i for i,(r,a) in enumerate(links));prev={seed:None};queue=[seed]
for x in queue:
 for k,f in enumerate(faces):
  if flipok(x,f):
   y=x^sum(1<<i for i in f)
   if y not in prev:prev[y]=(x,k);queue.append(y)
paths=[]
for a in range(3):
 y=seed^sum(1<<i for i,(r,d) in enumerate(links) if d==a);path=[]
 while y!=seed:
  y,k=prev[y];path.append(labels[k])
 paths.append(list(reversed(path)))
rows=[]
for L in (2,4,6):
 rs,links,ix,faces,labels=geometry(L);seed=sum((r[a]%2)<<i for i,(r,a) in enumerate(links))
 for a,path in enumerate(paths):
  x=seed;moves=0
  for aa,bb,parity in path:
   layer=[f for f,(c,d,r) in zip(faces,labels) if (c,d)==(aa,bb) and tuple(v%2 for v in r)==tuple(parity)]
   flat=sum(layer,[]);assert len(flat)==len(set(flat))
   for f in layer:assert flipok(x,f);x^=sum(1<<i for i in f);moves+=1
  target=seed^sum(1<<i for i,(r,d) in enumerate(links) if d==a);assert x==target
  for r in rs:
   degree=0
   for d in range(3):
    q=list(r);q[d]=(q[d]-1)%L;degree+=((x>>ix[r,d])&1)+((x>>ix[tuple(q),d])&1)
   assert degree==3
  flux=[sum((-1)**sum(r)*(2*((x>>ix[r,d])&1)-1) for r in rs) for d in range(3)];assert flux==[0]*3
  plane_flux=[sum((-1)**sum(r)*(2*((x>>ix[r,d])&1)-1) for r in rs if r[d]==0) for d in range(3)];assert plane_flux==[0]*3
  rows.append({'L':L,'translation_axis':a,'layers':len(path),'moves':moves,'pass':True})
out={'paths':paths,'L2_component_size':len(prev),'rows':rows,'seconds':time.monotonic()-start,'rss_mib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
