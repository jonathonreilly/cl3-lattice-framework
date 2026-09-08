import itertools,json,time,resource
start=time.monotonic();n=0
def ck(c):
 global n;n+=1
 if not c:raise ValueError(n)
for mask in range(1,65535):
 mixed=sum(len({(mask>>(4*x+y))&1 for x in range(4)})==2 for y in range(4))+sum(len({(mask>>(4*x+y))&1 for y in range(4)})==2 for x in range(4))
 ck(mixed>=4)
L=(4,6,8);vs=list(itertools.product(*map(range,L)));ix={v:i for i,v in enumerate(vs)};edges=[]
for v in vs:
 for a in range(3):
  w=list(v);w[a]=(w[a]+1)%L[a];edges.append((ix[v],ix[tuple(w)]))
inc=[set() for _ in vs]
for e,(i,j) in enumerate(edges):inc[i].add(e);inc[j].add(e)
# Tree paths define independent fundamental cycles.
seen={0};path={0:set()};todo=[0];tree=set()
while todo:
 i=todo.pop(0)
 for e in inc[i]:
  a,b=edges[e];j=b if a==i else a
  if j not in seen:seen.add(j);todo.append(j);tree.add(e);path[j]=path[i]^{e}
cycles=[path[i]^path[j]^{e} for e,(i,j) in enumerate(edges) if e not in tree]
ck(len(cycles)==len(edges)-len(vs)+1)
for axis in range(3):
 for width in range(1,L[axis]):
  S={i for i,v in enumerate(vs) if v[axis]<width};cut={e for e,(i,j) in enumerate(edges) if (i in S)!=(j in S)}
  ck(all(len(c&cut)%2==0 for c in cycles));ck(len(cut)==2*len(vs)//L[axis])
for e,(i,j) in enumerate(edges):
 a=inc[i]-{e};b=inc[j]-{e};ck(len(a)==len(b)==5)
 ck(all(not(set(edges[f])&set(edges[g])) for f in a for g in b))
 pairs=[]
 for star in (a,b):
  x=sorted(star);pairs.extend([(e,x[0]),(x[1],x[2]),(x[3],x[4])])
 cut=set()
 for f,g in pairs:cut^={f,g}
 ck(cut==a|b)
print(json.dumps(dict(checks=n,seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576),indent=2))
