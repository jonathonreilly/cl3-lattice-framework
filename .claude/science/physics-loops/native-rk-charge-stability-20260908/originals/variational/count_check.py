from pathlib import Path
import runpy,contextlib,io,json,time
start=time.monotonic();p=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):a=runpy.run_path(str(p/'check.py'))
edges=a['edges'];inc=a['inc'];Q=a['Q'];nbr=a['nbr'];eid=a['eid'];checks=0

def req(c):
 global checks
 checks+=1
 if not c:raise RuntimeError('counting extension')
def bad(z,q=None):
 q=Q(z) if q is None else q;i=q.index(1);j=q.index(-1)
 if j not in nbr[i]:return False
 bit=(z>>eid[tuple(sorted((i,j)))])&1;G=(z&inc[i]).bit_count()-3
 return 1-2*bit==-G

def hops(z):
 q=Q(z);out=[]
 for k,(i,j) in enumerate(edges):
  if (q[i]!=0)==(q[j]!=0):continue
  zz=z^(1<<k);qq=Q(zz)
  if all(abs(v)<=1 for v in qq):out.append(zz)
 return out
for i in range(64):
 for j in range(i+1,64):req(len(set(nbr[i])&set(nbr[j]))<=2)
created=[]
for k,(i,j) in enumerate(edges):
 z=a['seed']^(1<<k);req(bad(z));req(len(hops(z))==6);req(all(not bad(y) for y in hops(z)));created.append(z)
req(len(set(created))==192)
for z in a['seen']:
 hh=hops(z);b=bad(z);req(len(hh)==(6 if b else 8))
 req(sum(bad(y) for y in hh)==0 if b else sum(bad(y) for y in hh)<=4)
print(json.dumps(dict(checks=checks,common_neighbor_pairs=2016,seed_edge_bijection_cases=192,charged_states=len(a['seen']),seconds=time.monotonic()-start,scope='native phase helper imported explicitly; independent combinatorial predicates, not fullD2census'),indent=2))
