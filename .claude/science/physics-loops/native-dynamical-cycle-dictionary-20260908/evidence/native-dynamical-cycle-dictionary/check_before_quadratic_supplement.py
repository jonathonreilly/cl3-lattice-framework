import itertools,json,hashlib,time
from pathlib import Path
start=time.monotonic()
checks=[]
def require(ok,name):
 if not ok: raise RuntimeError(name)
 checks.append(name)
def build(v,edges,cycles,reverse=False):
 edges=sorted(tuple(sorted(e)) for e in edges); ne=len(edges); dim=1<<ne
 lookup={e:k for k,e in enumerate(edges)}
 neigh={i:sorted([b if a==i else a for a,b in edges if i in (a,b)],reverse=reverse) for i in range(v)}
 def occ(x):
  return sum(((sum((x>>k)&1 for k,e in enumerate(edges) if i in e)%2)<<i) for i in range(v))
 def native(i,j,x):
  e=lookup[tuple(sorted((i,j)))]; sign=1 if i<j else -1
  for vertex,other in ((i,j),(j,i)):
   for k in neigh[vertex][:neigh[vertex].index(other)]:
    sign*=1-2*((x>>lookup[tuple(sorted((vertex,k)))])&1)
  return x^(1<<e),complex(sign)
 def gamma(i,n):return n^(1<<i),(-1)**((n&((1<<i)-1)).bit_count())
 def gauge(i,j,x):
  n=occ(x); n1,a=gamma(j,n); n2,b=gamma(i,n1)
  y=x^(1<<lookup[tuple(sorted((i,j)))])
  require(n2==occ(y),'gauge-preservation')
  return y,-1j*a*b
 phase=[0j]*dim;phase[0]=1
 for x in range(1,dim):
  e=x.bit_length()-1;y=x^(1<<e);i,j=edges[e]
  _,a=native(i,j,y);_,b=gauge(i,j,y);phase[x]=phase[y]*b/a
 residual=0
 for x in range(dim):
  require(abs(phase[x])==1,'unitary-basis-phase')
  require(occ(x).bit_count()%2==0,'even-total-matter-parity')
  for i in range(v):
   b=(-1)**sum((x>>k)&1 for k,e in enumerate(edges) if i in e)
   require(b==1-2*((occ(x)>>i)&1),'B-parity-and-Gauss')
  for i,j in edges:
   y,a=native(i,j,x);z,b=gauge(i,j,x)
   require(y==z and a*phase[y]==phase[x]*b,'full-A-intertwining')
   residual=max(residual,abs(a-b))
   # Independent CAR hopping (annihilation and creation separately).
   n=occ(x);car=0
   for src,dst in ((i,j),(j,i)):
    if (n>>src)&1 and not ((n>>dst)&1):
     n1=n^(1<<src);sgn=(-1)**((n&((1<<src)-1)).bit_count())
     sgn*=(-1)**((n1&((1<<dst)-1)).bit_count());n2=n1^(1<<dst)
     require(n2==occ(y),'hopping-Gauss-image');car+=sgn
   bi=1-2*((n>>i)&1);bj=1-2*((n>>j)&1)
   require(1j*a*(bi-bj)/2*phase[y]==phase[x]*car,'full-T-CAR-X-intertwining')
   # Bare Majorana bilinear changes matter but not links, hence violates Gauss.
   require(occ(y)!=occ(x),'omitted-link-X-adverse')
 for cycle in cycles:
  pairs=list(zip(cycle,cycle[1:]+cycle[:1])); mask=sum(1<<lookup[tuple(sorted(e))] for e in pairs)
  for x in range(dim):
   y=x;z=x;na=1+0j;ga=1+0j
   for i,j in reversed(pairs):
    y,a=native(i,j,y);na*=a;z,b=gauge(i,j,z);ga*=b
   na*=1j**len(cycle);ga*=1j**len(cycle)
   require(z==x^mask and ga==1,'exact-Wilson-cycle-phase')
   require(y==z and na*phase[y]==phase[x],'native-cycle-Wilson-intertwining')
  if len(cycle)%4:
   require((1j**len(cycle))!=1,'omitted-cycle-phase-adverse')
 require(residual>0,'omitted-basis-phase-adverse')
 return {'vertices':v,'edges':ne,'physical_dimension':dim,'enlarged_dimension':1<<(v+ne),'cycles':cycles,'reversed_neighbor_orders':reverse,'basis_phase_exponents':[int(round(__import__('cmath').phase(z)/(3.141592653589793/2)))%4 for z in phase]}
fixtures=[]
fixtures.append(build(3,[(0,1),(1,2),(2,0)],[[0,1,2]]))
fixtures.append(build(4,[(0,1),(1,2),(2,3),(3,0)],[[0,1,2,3]]))
for rev in (False,True):fixtures.append(build(4,[(0,1),(1,2),(2,3),(3,0),(0,2)],[[0,1,2],[0,2,3],[0,1,2,3]],rev))
fixtures.append(build(6,[(i,(i+1)%6) for i in range(6)],[[0,1,2,3,4,5]]))
print(json.dumps({'checks':len(checks),'groups':{k:checks.count(k) for k in sorted(set(checks))},'fixtures':fixtures,'seconds':time.monotonic()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2,allow_nan=False))
