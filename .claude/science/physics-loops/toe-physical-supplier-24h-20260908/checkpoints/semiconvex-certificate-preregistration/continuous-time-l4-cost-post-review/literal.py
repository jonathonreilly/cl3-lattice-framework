"""Independent coordinate/path readouts; no producer imports or random draws."""
from itertools import product,combinations
import math
V=list(product(range(4),repeat=3)); E=[(v,a) for v in V for a in range(3)]; IDX={e:i for i,e in enumerate(E)}
def step(v,a):
 w=list(v);w[a]=(w[a]+1)%4;return tuple(w)
F=[(IDX[v,a],IDX[step(v,a),b],IDX[step(v,b),a],IDX[v,b]) for a,b in combinations(range(3),2) for v in V]
MASK=[sum(1<<e for e in f) for f in F]
SEED=sum((v[a]%2)<<i for i,(v,a) in enumerate(E))
NAMES=('mid_NF','mid_X1','mid_X2','mid_X1_square','mid_X2_square','endpoint_h','hL_hR','mid_X1_endpoint_h','mid_X2_endpoint_h','time_average_NF','endpoint_overlap','physical_event_count','hamming_activity_per_time','electric_corner_intensity','plane_anisotropy')
def require(ok,msg):
 if not ok:raise ValueError(msg)
def legal(x,p):return tuple((x>>e)&1 for e in F[p]) in ((0,1,0,1),(1,0,1,0))
def nf(x):return sum(legal(x,p) for p in range(192))
def flip(x,p):
 require(type(p) is int and 0<=p<192,'label');require(legal(x,p),'illegal flip');return x^MASK[p]
def ice(x):
 require(type(x) is int and 0<=x<1<<192,'bits')
 for v in V:require(sum((x>>i)&1 for i,(w,a) in enumerate(E) if w==v or step(w,a)==v)==3,'degree')
def measure(z):
 require(set(z)=={'L','V','T','initial','events','witness'},'path schema');require(z['L']==4 and z['V']=='19/20','domain')
 T=float.fromhex(z['T']);require(math.isfinite(T) and T>0,'T');x=SEED
 for p in z['witness']:x=flip(x,p)
 require(x==int(z['initial'],16),'witness');ice(x);initial=x;mid=x;last=0;integral=0
 for th,p in z['events']:
  t=float.fromhex(th);require(math.isfinite(t) and last<t<T,'time');integral+=(t-last)*nf(x);x=flip(x,p);ice(x)
  if t<=T/2:mid=x
  last=t
 integral+=(T-last)*nf(x);xs=[]
 for h in (1,2):
  total=0
  for a in range(3):
   for b in range(3):
    if a==b:continue
    q=sum((1j)**(h*v[a])*(-1)**sum(v)*(2*((mid>>i)&1)-1) for i,(v,c) in enumerate(E) if c==b)
    total+=q.real*q.real+q.imag*q.imag
  xs.append(total/256)
 N=nf(mid);hl=-nf(initial)/20;hr=-nf(x)/20;en=(hl+hr)/2;planes=[sum(legal(mid,p) for p in range(a*64,(a+1)*64)) for a in range(3)]
 vals=[N,*xs,xs[0]**2,xs[1]**2,en,hl*hr,xs[0]*en,xs[1]*en,integral/T,sum((2*((initial>>i)&1)-1)*(2*((x>>i)&1)-1) for i in range(192))/192,len(z['events']),len(z['events'])/(48*T),sum(sum(2*((mid>>i)&1)-1 for i,(v,c) in enumerate(E) if c==a)**2 for a in range(3))/(4*64**2),(3*sum(v*v for v in planes)-N*N)/(3*64**2)]
 return dict(zip(NAMES,vals))
