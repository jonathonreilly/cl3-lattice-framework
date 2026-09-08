import itertools,json,time,resource
from fractions import Fraction as F
start=time.monotonic();n=0
def ck(c):
 global n;n+=1
 if not c:raise ValueError(n)
vs=list(itertools.product(range(4),repeat=3));ids={v:i for i,v in enumerate(vs)}
def mv(v,a):return tuple((x+(a==b))%4 for b,x in enumerate(v))
es=sorted({tuple(sorted((ids[v],ids[mv(v,a)]))) for v in vs for a in range(3)});ei={e:i for i,e in enumerate(es)}
def cycle(vs):
 out=0
 for a,b in zip(vs,vs[1:]+vs[:1]):out^=1<<ei[tuple(sorted((ids[a],ids[b])))]
 return out
def rank(rows):
 piv={}
 for x in rows:
  while x:
   k=x.bit_length()-1
   if k not in piv:piv[k]=x;break
   x^=piv[k]
 return len(piv)
plaquettes=[cycle([v,mv(v,a),mv(mv(v,a),b),mv(v,b)]) for v in vs for a,b in itertools.combinations(range(3),2)]
winds=[]
for a in range(3):
 v=(0,0,0);c=[]
 for _ in range(4):c.append(v);v=mv(v,a)
 winds.append(cycle(c))
ck(rank(plaquettes)==126);ck(rank(plaquettes+winds)==129);ck(len(es)-len(vs)+1==129)
# Every generated vector has even incidence and arbitrary sign assignment is
# determined modulo a vertex gauge once all129 independent cycles are fixed.
for c in plaquettes+winds:
 degrees=[0]*64
 for k,(a,b) in enumerate(es):
  if c>>k&1:degrees[a]^=1;degrees[b]^=1
 ck(not any(degrees))
ck(F(128,8*144*12)==F(1,108));ck(F(128,8*144*12*4)==F(1,432))
# Exact factorization for rational sqrt(x)=y, sqrt(mu)=a, sqrt(M)=b.
for b in (F(1),F(12)):
 for a in (b/4,b/2,b):
  for y in (F(0),b/7,b/2,b):
   tangent=a+(y*y-a*a)/(2*a)-y
   ck(tangent==(y-a)**2/(2*a))
   ck(tangent>=(y*y-a*a)**2/(8*b**3))
print(json.dumps(dict(checks=n,seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576,plaquette_rank=126,with_three_windings_rank=129),indent=2))
