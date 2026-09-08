import itertools,json,pathlib,time,signal
signal.alarm(180);start=time.monotonic();p=pathlib.Path(__file__).parent
edges=[(i,6+j) for i in range(6) for j in range(6)];ind={e:k for k,e in enumerate(edges)};inc=[[k for k,e in enumerate(edges) if v in e] for v in range(12)]
def q(x):return [(1 if v<6 else -1)*(sum(x>>e&1 for e in inc[v])-3) for v in range(12)]
def arcs(x):return [(u,v,k) if x>>k&1 else (v,u,k) for k,(u,v) in enumerate(edges)]
def move(x,k):
 y=x^(1<<k)
 if max(map(abs,q(y)))>1:raise RuntimeError('illegal intermediate')
 return y
ice=sum(1<<ind[i,6+j] for i in range(6) for j in range(6) if (j-i)%6<3)
def reduce(x):
 tape=[]
 while any(q(x)):
  Q=q(x);source=Q.index(1);front=[source];paths={source:[]};target=None
  while front:
   u=front.pop()
   if Q[u]==-1:target=u;break
   for a,b,k in arcs(x):
    if a==u and b not in paths:paths[b]=paths[u]+[(a,b,k)];front.append(b)
  if target is None:raise RuntimeError('sink counterexample')
  path=paths[target];last=max(i for i,(a,b,k) in enumerate(path) if Q[a]==1);path=path[last:]
  if any(Q[a]!=0 for a,b,k in path[1:]):raise RuntimeError('interior')
  old=sum(t*t for t in Q)
  for a,b,k in path:x=move(x,k);tape.append(k)
  if sum(t*t for t in q(x))!=old-2:raise RuntimeError('D drop')
 return x,tape

def join(x,y):
 tape=[]
 while x!=y:
  changed=x^y;ar=[(a,b,k) for a,b,k in arcs(x) if changed>>k&1];v=ar[0][0];seen={};walk=[]
  while v not in seen:
   seen[v]=len(walk);edge=next(t for t in ar if t[0]==v);walk.append(edge);v=edge[1]
  cycle=walk[seen[v]:]
  for a,b,k in cycle:x=move(x,k);tape.append(k)
  if any(q(x)):raise RuntimeError('ice cycle endpoint')
 if len(tape)>36:raise RuntimeError('join bound')
 return tape
fixtures=[ice,sum(1<<ind[i,6+j] for i in range(6) for j in range(6) if (j-i)%6<2)]
fixtures.append(fixtures[1]^((1<<36)-1));x=ice
for t in range(512):
 k=(t*t+17*t+7)%36;y=x^(1<<k)
 if max(map(abs,q(y)))<=1:x=y
 if t in [7,15,31,63,127,255,511]:fixtures.append(x)
reductions=[reduce(x) for x in fixtures];pairs=[]
for i,j in itertools.product(range(len(fixtures)),repeat=2):
 a,ta=reductions[i];b,tb=reductions[j];mid=join(a,b);tape=ta+mid+list(reversed(tb));x=fixtures[i]
 for k in tape:x=move(x,k)
 bound=(sum(t*t for t in q(fixtures[i]))+sum(t*t for t in q(fixtures[j])))*11//2+36
 if x!=fixtures[j] or len(tape)>bound:raise RuntimeError('full pair route')
 pairs.append(dict(i=i,j=j,tape=tape,bound=bound))
# Exact native A phase with ascending neighbor order, no external witness.
def amp(x,k):
 i,j=edges[k];before=[f for v,w in [(i,j),(j,i)] for f in inc[v] if (edges[f][1] if edges[f][0]==v else edges[f][0])<w]
 return (-1)**sum(x>>f&1 for f in before)
a,b,c=ind[0,6],ind[0,9],ind[0,7];word=[a,b,c,a,b,c];x=ice;phase=1;states=[x]
for k in word:phase*=amp(x,k);x=move(x,k);states.append(x)
if x!=ice or phase!=-1:raise RuntimeError('closed A phase')
(p/'RESULT.json').write_text(json.dumps(dict(graph='K6,6',fixture_bits=fixtures,D=[sum(t*t for t in q(x)) for x in fixtures],all_ordered_pair_routes=pairs,phase_word=word,phase_states=states,phase=phase,seconds=time.monotonic()-start,scope='different graph exact constructive controls,not exhaustive orientations'),indent=2)+'\n')
print(len(pairs),phase,time.monotonic()-start)
