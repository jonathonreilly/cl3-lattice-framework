import itertools,collections,random,time,resource,pathlib,json,hashlib
start=time.monotonic();count=0
def need(p,s):
 global count
 count+=1
 if not p:raise RuntimeError(s)
def mul(a,b):
 p,x,z=a;q,y,w=b
 return ((p+q+2*((z&y).bit_count()%2))%4,x^y,z^w)
def action(s,n):
 p,x,z=s
 return (p+2*((z&n).bit_count()%2))%4,n^x
L=4;coords=list(itertools.product(range(L),repeat=3));ids={r:i for i,r in enumerate(coords)}
edges=[];directions={}
for r in coords:
 for a in range(3):
  t=list(r);t[a]=(t[a]+1)%L
  directions[r,a]=len(edges);edges.append((ids[r],ids[tuple(t)]))
adj=[[] for _ in coords];lookup={};inc=[0]*len(coords)
for e,(u,v) in enumerate(edges):
 adj[u].append((v,e));adj[v].append((u,e));lookup[min(u,v),max(u,v)]=e
 inc[u]|=1<<e;inc[v]|=1<<e
As={}
for e,(u,v) in enumerate(edges):
 z=0
 for i,j in ((u,v),(v,u)):
  for w,f in adj[i]:
   if w<j:z^=1<<f
 As[u,v]=(0 if u<v else 2,1<<e,z);As[v,u]=(2 if u<v else 0,1<<e,z)
def cycle(path):
 s=((len(path)-1)%4,0,0)
 for u,v in zip(path,path[1:]):s=mul(s,As[u,v])
 return s
parent={0:None};tree=set();q=collections.deque([0])
while q:
 u=q.popleft()
 for v,e in adj[u]:
  if v not in parent:parent[v]=u;tree.add(e);q.append(v)
fund=[]
for e,(u,v) in enumerate(edges):
 if e in tree:continue
 pu=[u];pv=[v]
 while parent[pu[-1]] is not None:pu.append(parent[pu[-1]])
 while parent[pv[-1]] is not None:pv.append(parent[pv[-1]])
 common=next(w for w in pu if w in pv)
 path=pu[:pu.index(common)+1]+list(reversed(pv[:pv.index(common)]))+[u]
 fund.append((e,cycle(path)))
seed=sum(1<<e for (r,a),e in directions.items() if r[a]%2)
def phase(n):
 delta=n^seed;state=seed;p=0
 for e,s in fund:
  if delta&(1<<e):
   pp,state=action(s,state);p=(p+pp)%4
 need(state==n,'fundamental-coordinate phase reaches requested state')
 return p
plaquettes=[]
for r in coords:
 for a,b in ((0,1),(0,2),(1,2)):
  ra=list(r);ra[a]=(ra[a]+1)%L;ra=tuple(ra)
  rb=list(r);rb[b]=(rb[b]+1)%L;rb=tuple(rb)
  rab=list(ra);rab[b]=(rab[b]+1)%L;rab=tuple(rab)
  es=[directions[r,a],directions[ra,b],directions[rb,a],directions[r,b]]
  s=cycle([ids[r],ids[ra],ids[rab],ids[rb],ids[r]])
  need(s[1]==sum(1<<e for e in es),'plaquette X support')
  prod=(0,0,0)
  for e,f in fund:
   if s[1]&(1<<e):prod=mul(prod,f)
  need(prod==s,'full Pauli phase agrees with fundamental-cycle product')
  plaquettes.append((ids[r],es,s))
rng=random.Random(20260908);n=seed;observed=set();negative_phases=0;nonflips=0
for sample in range(128):
 need(all((n&m).bit_count()==3 for m in inc),'ice configuration')
 observed.add(n);eta=phase(n);moves=[];root_counts=[0]*len(coords)
 for root,es,s in plaquettes:
  bits=[(n>>e)&1 for e in es]
  allowed=bits[0]==bits[2] and bits[1]==bits[3] and bits[0]!=bits[1]
  pp,target=action(s,n)
  inside=all((target&m).bit_count()==3 for m in inc)
  need(allowed==inside,'compression is exactly alternating flippability')
  if allowed:
   moves.append(target);root_counts[root]+=1
   need((eta+pp-phase(target))%4==0,'diagonal phase removes native ring sign')
   negative_phases+=int(pp==2)
  else:nonflips+=1
 need(max(root_counts)<=2 and sum(root_counts)<=2*len(coords),'extensive flippability bound')
 need(bool(moves),'selected component has a next legal move')
 n=rng.choice(moves)
# Local gated ring is Hermitian and conserves each corner degree for all16patterns,
# including backgrounds outside the ice constraint.
for bits in itertools.product((0,1),repeat=4):
 allowed=bits[0]==bits[2] and bits[1]==bits[3] and bits[0]!=bits[1]
 target=tuple(1-b for b in bits)
 reverse=target[0]==target[2] and target[1]==target[3] and target[0]!=target[1]
 need(allowed==reverse,'gate commutes with cycle toggle')
 if allowed:need(all(bits[i]+bits[(i+1)%4]==target[i]+target[(i+1)%4] for i in range(4)),'all corner degrees preserved')
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024**2
need(seconds<180 and rss<384,'resource limit')
result=dict(status='PASS',checks=count,seconds=seconds,peak_MiB=rss,unique_ice_configurations=len(observed),sampled_native_negative_ring_phases=negative_phases,nonflippable_compressions_zero=nonflips,script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),scope='Finite operator controls; no ergodic or equilibrium sample claim.')
pathlib.Path(__file__).with_name('RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
