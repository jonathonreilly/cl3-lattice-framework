"""Outward rational local-bath enclosures. Import performs no integration."""
from fractions import Fraction as F
from math import isqrt
from functools import lru_cache
from itertools import product
import heapq
BITS=40;ROOTBITS=80;MAX_DEPTH=12

def down(x,b=BITS):return F((x.numerator*(1<<b))//x.denominator,1<<b)
def up(x,b=BITS):return -down(-x,b)
def roots(x,b=ROOTBITS):
 if x<0:raise ValueError('negative radicand')
 n=isqrt((x.numerator<<(2*b))//x.denominator);lo=F(n,1<<b)
 return lo,lo if lo*lo==x else F(n+1,1<<b)

def atan_bounds(x,n):
 total=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n)),F(0));rem=x**(2*n+1)/F(2*n+1)
 return (total,total+rem) if n%2==0 else (total-rem,total)

@lru_cache(None)
def pi_bounds():
 a,b=atan_bounds(F(1,5),32),atan_bounds(F(1,239),10)
 return 16*a[0]-4*b[1],16*a[1]-4*b[0]

@lru_cache(None)
def sin_bounds(u):
 if u==0:return F(0),F(0)
 if u==1:return F(1),F(1)
 if not 0<u<1:raise ValueError('sine coordinate')
 lo,hi=pi_bounds();x=u*(lo+hi)/4;rad=u*(hi-lo)/4
 term=x;total=term
 for k in range(1,24):term=-term*x*x/F((2*k)*(2*k+1));total+=term
 remainder=abs(term*x*x/F(48*49))
 return max(F(0),down(total-rad,64)),min(F(1),up(total+remainder+rad,64))

def endpoint_x(depth,indices):
 scale=1<<depth;lo=hi=F(0)
 for i in indices:
  a=sin_bounds(F(i,scale))[0];b=sin_bounds(F(i+1,scale))[1];lo+=4*a*a;hi+=4*b*b
 return lo,hi

def a_values(s,x):
 a=s*s+x;rlo,rhi=roots(a*(a+4))
 return (1/rhi,1/rlo),(2*s*(a+2)/rhi**3,2*s*(a+2)/rlo**3)

def ranges_a(s,xlo,xhi):
 lo=a_values(s,xhi);hi=a_values(s,xlo)
 return [(down(lo[0][0]),up(hi[0][1])),(down(-hi[1][1]),up(-lo[1][0]))]

def ranges_b(s,xlo,xhi):
 wlo=roots(xlo)[0];whi=roots(xhi)[1]
 def g(w):return w/(w*w+s*s)
 def mag(w):return 2*s*w/(w*w+s*s)**2
 bmin=min(g(wlo),g(whi));bmax=max(g(wlo),g(whi))
 if wlo<=s<=whi:bmax=max(bmax,1/(2*s))
 dmin=min(mag(wlo),mag(whi));dmax=max(mag(wlo),mag(whi));rlo,rhi=roots(F(3))
 if wlo<=s/rlo and whi>=s/rhi:dmax=max(dmax,F(9)/(8*rlo*s*s))
 return [(down(bmin),up(bmax)),(down(-dmax),up(-dmin))]

def integrate(s,kind,cap,target=F(1,32),progress=None):
 dim=2 if kind=='A' else 3
 def cell(depth,index):
  xl,xh=endpoint_x(depth,index);bounds=ranges_a(s,xl,xh) if kind=='A' else ranges_b(s,xl,xh)
  volume=F(1,1<<(dim*depth));weighted=[(a*volume,b*volume) for a,b in bounds]
  priority=-max(b-a for a,b in weighted)
  return (priority,depth,index,weighted)
 root=cell(0,(0,)*dim);heap=[root];lower=[a for a,b in root[3]];upper=[b for a,b in root[3]];leaves=1;splits=0;blocked=[]
 while max(b-a for a,b in zip(lower,upper))>target and leaves+(1<<dim)-1<=cap:
  while heap and heap[0][1]>=MAX_DEPTH:blocked.append(heapq.heappop(heap))
  if not heap:break
  _,depth,index,old=heapq.heappop(heap)
  for j,(a,b) in enumerate(old):lower[j]-=a;upper[j]-=b
  for bits in product(range(2),repeat=dim):
   child=cell(depth+1,tuple(2*i+b for i,b in zip(index,bits)));heapq.heappush(heap,child)
   for j,(a,b) in enumerate(child[3]):lower[j]+=a;upper[j]+=b
  leaves+=(1<<dim)-1;splits+=1
  if progress and splits%32==0:progress({'leaves':leaves,'splits':splits,'bounds':[(str(a),str(b)) for a,b in zip(lower,upper)]})
 status='CERTIFIED_TARGET' if max(b-a for a,b in zip(lower,upper))<=target else 'INDETERMINATE_AT_CAP'
 return {'s':str(s),'kind':kind,'status':status,'leaves':leaves,'splits':splits,'bounds':[(str(a),str(b)) for a,b in zip(lower,upper)],'widths':[str(b-a) for a,b in zip(lower,upper)],'target':str(target),'cap':cap}
