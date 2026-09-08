import itertools,json,time
from pathlib import Path
start=time.monotonic()
# Four degree-six active stars; exterior vertices merely supply boundary bits.
edges=[(0,1),(0,2),(0,3)];groups=[];nextv=4
for v,num in [(0,3),(1,5),(2,5),(3,5)]:
 ids=[]
 for _ in range(num):ids.append(len(edges));edges.append((v,nextv));nextv+=1
 groups.append(ids)
inc={v:[] for v in range(nextv)}
for e,(a,b) in enumerate(edges):inc[a].append((b,e));inc[b].append((a,e))
def nativeA(x,a,b):
 e=edges.index(tuple(sorted((a,b))));phase=1 if a<b else -1
 for v,w in [(a,b),(b,a)]:
  for nb,j in inc[v]:
   if nb<w and x>>j&1:phase=-phase
 return x^(1<<e),phase

def q(x,v):return (1 if v==0 else -1)*(sum(x>>e&1 for _,e in inc[v])-3)
def hop(x,a,b,s):
 if x is None or q(x,b)!=s or q(x,a)!=0:return None,0j
 y,phase=nativeA(x,a,b)
 if any(abs(q(y,v))>1 for v in range(4)):return None,0j
 return y,-1j*phase

def path(x,seq,s):
 amp=1+0j
 for a,b in seq:
  x,z=hop(x,a,b,s);amp*=z
  if x is None:return None,0j
 return x,amp
n=active=wrong=0
for core in range(8):
 for counts in itertools.product(range(4),range(6),range(6),range(6)):
  x=core
  for ids,c in zip(groups,counts):
   for e in ids[:c]:x|=1<<e
  if any(abs(q(x,v))>1 for v in range(4)):continue
  for s in [-1,1]:
   a,pa=path(x,[(0,1),(2,0),(0,3)],s);b,pb=path(x,[(0,3),(2,0),(0,1)],s)
   if a!=b or pa!=-pb:raise RuntimeError('three-hop identity')
   n+=1
   if pa:active+=1;wrong+=pa!=pb
assert active>0 and wrong==active
# A nonalternating cycle toggles a corner divergence; ungated ambient ring is adverse.
nonalternating=sum(any(2-2*(bits[j-1]+bits[j]) for j in range(4)) for bits in itertools.product([0,1],repeat=4))
assert nonalternating==14
out=dict(accepted_star_patterns=n,nonzero_exchange_domains=active,unsigned_identity_failures=wrong,nonalternating_face_patterns=nonalternating,seconds=time.monotonic()-start,scope='local phase representative boundary bits; global exchange proof additionally requires low-charge extendibility of boundary configuration')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
