"""Independent small integer geometry/action and rational budget controls only."""
from fractions import Fraction as Q
from itertools import combinations
import json
count=0
def req(x):
 global count
 if not x:raise ValueError('predicate '+str(count))
 count+=1
N=8
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def apply(m,x):return [dot(r,x) for r in m]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def scale(t,x):return [t*y for y in x]
def basis(i):return [int(j==i) for j in range(N)]
e=basis(0)
def ds(indices):return [0]+[(1 if i%2 else -1) if i in indices else 0 for i in range(1,7)]+[0]
T=[[0]*N for _ in range(N)]
for j in range(1,7):T[0][j]=-(1 if j%2 else -1);T[j][0]=-T[0][j]
O=[[int(1<=i<=6 and 1<=j<=6 and i!=j and (i-1)//2==(j-1)//2) for j in range(N)] for i in range(N)]
Gamma=[[0]*N for _ in range(N)]
for j in range(0,N,2):Gamma[j][j+1]=-1;Gamma[j+1][j]=1
D=ds(range(1,7));noncommuting=False
for aa in combinations(range(1,7),2):
 for cc in combinations([j for j in range(1,7) if j not in aa],2):
  A,C=ds(aa),ds(cc);vectors=(A,C,D)
  gram=[[Q(dot(u,v),4) for v in vectors] for u in vectors]
  req(gram==[[Q(1,2),0,Q(1,2)],[0,Q(1,2),Q(1,2)],[Q(1,2),Q(1,2),Q(3,2)]])
  req(gram[0][0]*(gram[1][1]*gram[2][2]-gram[1][2]**2)-gram[0][2]*gram[1][1]*gram[2][0]==Q(1,8))
  for u in vectors:
   req(Q(-dot(u,apply(T,e)),24)==(-Q(1,4) if u==D else -Q(1,12)))
   for v in (A,C):
    req(abs(dot(u,v)+dot(u,apply(O,v)))<=2 and abs(dot(u,apply(O,v)))<=2)
  x=scale(Q(1,2),e);q=scale(Q(1,2),A)
  def delta(v):return scale(2,sub(scale(dot(A,v),e),scale(dot(e,v),A)))
  for j in range(N):
   v=basis(j)
   req(delta(v)==scale(8,sub(scale(dot(q,v),x),scale(dot(x,v),q))))
   # Same identity on Gamma columns; never replace by commuting Gamma.
   gv=apply(Gamma,v)
   req(delta(gv)==scale(8,sub(scale(dot(q,gv),x),scale(dot(x,gv),q))))
   if delta(gv)!=apply(Gamma,delta(v)):noncommuting=True
req(noncommuting)
# Endpoint envelopes monotone in positive s <=16; alpha^(1/2) /2 <=2.
s=Q(16)
req(2*s*(2+s*s/3)<2800);req(2*s*s<=2800)
req(2*(2+s*s/3)<176);req(2*s<=176)
req(Q(2*2,6)<=1)
eps=Q(48985020+804*178,10**19);req(eps<Q(5,10**12))
def bound(e,t):return t-1608*e>0 and 4*536*1608*e<(t-1608*e)**2
req(bound(Q(5,10**12),Q(416,100000)))
req(bound(Q(2**40+804*2800,10**30),Q(2,10**6)))
req(bound(Q(1,2**60),Q(2,10**6)))
req(Q(536,2**40)<Q(1,10**9))
req(Q(416,100000)+Q(4,10**6)+Q(1,10**9)+Q(1,10**6)<Q(42,10000))
print(json.dumps({'status':'PASS_TINY_INDEPENDENT','checks':count,'native_calls':0,'interpretation':'literal geometry, finite action identities and rational budget; not native Gram values'}))
