import itertools,json,time,resource,sys
from pathlib import Path
start=time.monotonic()
def rank(xs):
 basis={}
 for x in xs:
  while x:
   k=x.bit_length()-1
   if k in basis:x^=basis[k]
   else:basis[k]=x;break
 return len(basis)
rows=[]
for L in (4,6,8):
 vs=list(itertools.product(range(L),repeat=3));edges=[];labels=[]
 for v in vs:
  for a in range(3):
   w=list(v);w[a]=(w[a]+1)%L;edges.append((v,tuple(w)));labels.append((v,a))
 ix={x:i for i,x in enumerate(labels)};faces=[]
 for v in vs:
  for a,b in itertools.combinations(range(3),2):
   va=list(v);vb=list(v);va[a]=(va[a]+1)%L;vb[b]=(vb[b]+1)%L
   faces.append(sum(1<<ix[e] for e in [(v,a),(tuple(va),b),(tuple(vb),a),(v,b)]))
 rankp=rank(faces);E=len(edges);V=len(vs)
 if rankp!=E-V-2:raise AssertionError('plaquette span codim3')
 S={v for v in vs if all(x%2==0 for x in v)};keep=[i for i,e in enumerate(edges) if not(set(e)&S)];adj={v:set() for v in vs if v not in S}
 for i in keep:
  a,b=edges[i];adj[a].add(b);adj[b].add(a)
 seen={next(iter(adj))};todo=list(seen)
 while todo:
  for b in adj[todo.pop()]-seen:seen.add(b);todo.append(b)
 if len(seen)!=V-len(S):raise AssertionError('residual connected')
 cuts=[sum(1<<i for i,(v,a) in enumerate(labels) if a==j and v[j]==L-1) for j in range(3)]
 loops=[]
 for a in range(3):
  b=(a+1)%3;vertices=[]
  for t in range(L):
   v=[0,0,0];v[b]=1;v[a]=t;vertices.append(tuple(v))
  loop=sum(1<<ix[v,a] for v in vertices)
  if any(i not in keep for i in range(E) if (loop>>i)&1):raise AssertionError('loop touches removed star')
  w=[(loop&cut).bit_count()%2 for cut in cuts]
  if w!=[int(j==a) for j in range(3)]:raise AssertionError('winding basis')
  loops.append(loop)
 if rank(faces+loops)!=E-V+1:raise AssertionError('full cycle span')
 if any((face&cut).bit_count()%2 for face in faces for cut in cuts):raise AssertionError('local preserves winding')
 rows.append(dict(L=L,V=V,E=E,local_rank=rankp,full_cycle_rank=E-V+1,star_count=len(S),residual_winding_rank=3,completion_per_star_assignment_per_sector_exponent=E-V-5*len(S)-2))
result=dict(rows=rows,seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024));Path(__file__).with_name('RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
