import hashlib,json,resource,signal,sys,time
from collections import deque
from itertools import product
from pathlib import Path
signal.alarm(180);start=time.monotonic();checks=0

def req(c,label):
 global checks
 checks+=1
 if not c:raise RuntimeError(label)
vs=list(product(range(4),repeat=3));vi={v:i for i,v in enumerate(vs)};es=set();axis={};forward={}
for a,v in enumerate(vs):
 for d in range(3):
  w=list(v);w[d]=(w[d]+1)%4;b=vi[tuple(w)];e=tuple(sorted((a,b)));es.add(e);axis[e]=d;forward[e]=(a,b)
es=sorted(es);ei={e:k for k,e in enumerate(es)};eps=[(-1)**sum(v) for v in vs];inc=[sum(1<<k for k,e in enumerate(es) if v in e) for v in range(64)];nb=[sorted(b if a==v else a for a,b in es if v in (a,b)) for v in range(64)]
def edge(a,b):return ei[tuple(sorted((a,b)))]
def Q(x):return [eps[v]*((x&inc[v]).bit_count()-3) for v in range(64)]
def out(x,a,b):return eps[a]*(2*((x>>edge(a,b))&1)-1)==1
def native(x,k):
 a,b=es[k];s=0
 for v,w in ((a,b),(b,a)):
  for u in nb[v]:
   if u<w:s^=(x>>edge(v,u))&1
 return (-1)**s

def flip(x,a,b,tape):
 q=Q(x);req(out(x,a,b),'directed move');k=edge(a,b);phase=native(x,k);y=x^(1<<k);r=Q(y)
 req(all(abs(v)<=1 for v in r),'low support');want=q.copy();want[a]-=1;want[b]+=1;req(r==want,'charge increment');req(native(y,k)*phase==1,'native involution')
 tape.append([a,b,phase,sum(v*v for v in r)]);return y

def reduce(x):
 initial=x;tape=[];pairs=[]
 while any(Q(x)):
  q=Q(x);D=sum(v*v for v in q);p=q.index(1);prev={p:None};queue=deque([p]);m=None
  while queue:
   a=queue.popleft()
   if q[a]==-1:m=a;break
   for b in nb[a]:
    if b not in prev and out(x,a,b):prev[b]=a;queue.append(b)
  req(m is not None,'positive reaches negative');path=[m]
  while prev[path[-1]] is not None:path.append(prev[path[-1]])
  path.reverse();path=path[max(k for k,v in enumerate(path) if q[v]==1):];req(all(q[v]==0 for v in path[1:-1]),'neutral interior')
  begin=len(tape)
  for a,b in zip(path,path[1:]):x=flip(x,a,b,tape)
  req(sum(v*v for v in Q(x))==D-2,'pair reduction');pairs.append(dict(path=path,begin=begin,stop=len(tape)))
 req(len(tape)<=sum(v*v for v in Q(initial))*63//2,'reduction length')
 return x,tape,pairs

def join(x,y):
 req(not any(Q(x)) and not any(Q(y)),'ice endpoints');mask=x^y;tape=[];cycles=[]
 while mask:
  k=(mask&-mask).bit_length()-1;a,b=es[k]
  if not out(x,a,b):a,b=b,a
  walk=[a];pos={a:0}
  while True:
   a=walk[-1];b=next(v for v in nb[a] if (mask>>edge(a,v))&1 and out(x,a,v))
   if b in pos:C=walk[pos[b]:]+[b];break
   pos[b]=len(walk);walk.append(b)
  for a,b in zip(C,C[1:]):x=flip(x,a,b,tape);mask^=1<<edge(a,b)
  req(not any(Q(x)),'cycle returns ice');cycles.append(C)
 req(x==y and len(tape)<=192,'ice join endpoint/bound');return tape,cycles
ice=sum(((1+eps[forward[e][0]])//2)<<k for k,e in enumerate(es));req(not any(Q(ice)),'initial ice')
fixtures=[ice,sum((axis[e]==0)<<k for k,e in enumerate(es)),sum((axis[e]!=2)<<k for k,e in enumerate(es))]
x=ice;r=19
for step in range(1200):
 r=(1103515245*r+12345)%(1<<31);k=r%192;y=x^(1<<k)
 if all(abs(v)<=1 for v in Q(y)):x=y
 if step in [0,1,3,9,31,95,287,599,1199]:fixtures.append(x)
rows=[]
for x in fixtures:
 y,t,p=reduce(x);u,c=join(y,ice);req(len(t)+len(u)<=sum(v*v for v in Q(x))*63//2+192,'full route bound')
 rows.append(dict(initial_bits=format(x,'0192b'),D=sum(v*v for v in Q(x)),ice_bits=format(y,'0192b'),reduction=t,pairs=p,ice_join=u,cycles=c))
# Literal globally supported native-A exchange replay using the separately delivered finite witness.
source=Path(__file__).parents[1]/'native-global-charge-exchange/RESULT.json';w=json.loads(source.read_text());x=int(w['witnesses'][0]['initial_bits'],2);star=w['star'];a,b,c=[edge(star['i'],star[v]) for v in ['j','k','l']];z=x;phase=1
for k in [a,b,c,a,b,c]:
 phase*=native(z,k);z^=1<<k;req(all(abs(v)<=1 for v in Q(z)),'A exchange low support')
req(z==x and phase==-1,'A exchange closed minus')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);req(0<rss<384,'memory');req(set([0,64])<=set(r['D'] for r in rows),'domain endpoints')
print(json.dumps(dict(PASS=True,checks=checks,rows=rows,A_exchange_phase=phase,seconds=time.monotonic()-start,peak_MiB=rss,source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),exchange_fixture_sha=hashlib.sha256(source.read_bytes()).hexdigest()),indent=2))
