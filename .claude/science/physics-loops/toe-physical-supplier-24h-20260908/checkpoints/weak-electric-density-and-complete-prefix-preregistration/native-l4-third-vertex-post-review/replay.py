from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import json,hashlib,signal,resource,time
signal.alarm(29);start=time.monotonic();P=Path(__file__).parent;D=P.parent/'native-l4-third-vertex-run-1085';pins=json.loads((P/'INPUTS.json').read_text())
for name,h in pins.items():
 if hashlib.sha256((D/name).read_bytes()).hexdigest()!=h:raise ValueError('input')
vs=list(product(range(4),repeat=3));ix={v:i for i,v in enumerate(vs)};K=[[F(0)]*64 for _ in vs];edges=[]
for v in vs:
 for axis in range(3):
  w=list(v);w[axis]=(w[axis]+1)%4;i,j=sorted((ix[v],ix[tuple(w)]));edges.append((i,j));K[i][j]=F(-2*(-1)**sum(v[:axis]));K[j][i]=-K[i][j]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mv(A,x):return [dot(row,x) for row in A]
star=[e for e,(i,j) in enumerate(edges) if i==0 or j==0];neighbors=sorted({v for e in star for v in edges[e]}-{0});r=[]
for v in [0]+neighbors:
 x=[F(i==0) for i in range(64)] if v==0 else [K[i][v] for i in range(64)]
 for b in r:
  c=dot(x,b)/dot(b,b);x=[u-c*w for u,w in zip(x,b)]
 if any(x):r.append(x)
d=[dot(x,x) for x in r];kr=[mv(K,x) for x in r];bits={p:[b for b in range(64) if b.bit_count()%2==p] for p in (0,1)}
def mat(pair,p):
 k=[row[:] for row in K]
 for e in pair:
  i,j=edges[e];k[i][j]=-k[i][j];k[j][i]=-k[j][i]
 q=[[-dot(x,mv(k,y))/12 for y in kr] for x in r];bs=bits[p];index={b:i for i,b in enumerate(bs)};A=[[F(6*int(i==j)) for j in range(32)] for i in range(32)]
 # Direct ordered CAR action i*a_i*b_j/2; b_j acts first.
 for col,b in enumerate(bs):
  for i in range(6):
   for j in range(6):
    mid=b^(1<<j);a=mid^(1<<i)
    sign=(-1)**((b&((1<<j)-1)).bit_count()+(mid&((1<<i)-1)).bit_count())
    factor=1/d[i] if i==j else d[i]**(((b>>i)&1)-1)*d[j]**(((b>>j)&1)-1)
    A[index[a]][col]+=-q[i][j]*F(sign,2)*(1-2*((b>>j)&1))*factor
 return A
def gamma(x):
 z=[F(0)]*32;idx={b:i for i,b in enumerate(bits[1])}
 for col,b in enumerate(bits[0]):
  for i in range(6):z[idx[b^(1<<i)]]+=x[col]*(-1)**((b&((1<<i)-1)).bit_count())*r[i][0]*(1 if b>>i&1 else 1/d[i])
 return z
raw=json.loads((D/'SOLVE_VECTORS.json').read_text());res=json.loads((D/'RESULT.json').read_text());pairs=list(combinations(star,2));xs={tuple(map(int,k.split(','))):list(map(F,v)) for k,v in raw['first'].items()};ys=[list(map(F,v)) for v in raw['second']]
if set(xs)!=set(pairs) or len(ys)!=15:raise ValueError('membership')
for pair in pairs:
 if mv(mat(pair,0),xs[pair])!=[F(i==0) for i in range(32)]:raise ValueError('even residual')
for pair,y in zip(pairs,ys):
 rhs=gamma([sum(xs[a][i] for a in pairs if set(a).isdisjoint(pair)) for i in range(32)])
 if mv(mat(pair,1),y)!=rhs:raise ValueError('odd residual')
z=[sum(y[i] for y in ys)/48 for i in range(32)];W=[__import__('functools').reduce(lambda a,i:a*d[i],(i for i in range(6) if b>>i&1),F(1)) for b in bits[1]];weights={str(k):sum(W[i]*z[i]**2 for i,b in enumerate(bits[1]) if b.bit_count()==k) for k in (1,3,5)}
if z!=list(map(F,res['coordinates'])) or W!=list(map(F,res['metric'])) or weights!={k:F(v) for k,v in res['particle_weights'].items()}:raise ValueError('decomposition')
if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise ValueError('RSS')
print(json.dumps({'status':'PASS','independent_direct_CAR_residuals':30,'particle_weights':{k:str(v) for k,v in weights.items()},'seconds':time.monotonic()-start,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'author_import':False}))
