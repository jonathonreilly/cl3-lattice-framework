from fractions import Fraction as F
from itertools import product,combinations
from math import lcm,isqrt,sqrt,isfinite
import json
from pathlib import Path
class ExactModel:
 def __init__(self,frame,prefix):
  self.d=list(map(F,frame['norms']));vs=list(product(range(4),repeat=3));ids={v:i for i,v in enumerate(vs)};black=[i for i,v in enumerate(vs) if sum(v)%2==0]
  self.K=[[0]*64 for _ in vs];self.edges=[]
  for v in vs:
   for a in range(3):
    w=list(v);w[a]=(w[a]+1)%4;i,j=sorted((ids[v],ids[tuple(w)]));self.edges.append((i,j));self.K[i][j]=-2*(-1)**sum(v[:a]);self.K[j][i]=-self.K[i][j]
  if prefix['coordinates']!=[list(v) for v in vs] or prefix['edge_order']!=[list(e) for e in self.edges]:raise ValueError('geometry')
  self.r=[[F(0)]*64 for _ in range(10)]
  for i,row in enumerate(frame['raw_black_basis']):
   for k,x in zip(black,row):self.r[i][k]=F(x)
  for i in range(10):
   for j in range(10):
    if sum(a*b for a,b in zip(self.r[i],self.r[j]))!=(self.d[i] if i==j else 0):raise ValueError('Gram')
  self.kr=[[sum(self.K[i][j]*row[j] for j in range(64)) for i in range(64)] for row in self.r]
  self.states=[b for b in range(1024) if b.bit_count()%2==0];self.ix={b:i for i,b in enumerate(self.states)}
  self.W=[]
  for b in self.states:
   z=F(1)
   for i,d in enumerate(self.d):
    if b>>i&1:z*=d
   self.W.append(z)
  self.Wden=lcm(*(x.denominator for x in self.W));self.Wint=[int(x*self.Wden) for x in self.W]
  self.support=sorted(set(prefix['boundary_edges'])|{x['bridge_edge'] for x in prefix['rows']});delta={}
  for e in self.support:
   v,w=self.edges[e];Q=[[F(self.K[v][w],6)*(self.r[i][v]*self.kr[j][w]-self.r[i][w]*self.kr[j][v]) for j in range(10)] for i in range(10)]
   delta[e]=self.fock(Q)
  self.den=lcm(*(x.denominator for D in delta.values() for x in D.values()))
  self.delta={e:{ij:int(x*self.den) for ij,x in D.items()} for e,D in delta.items()}
  self.base={(i,i):2*b.bit_count()*self.den for i,b in enumerate(self.states)}
  v,w=prefix['centers'];self.ell=[F(0)]*512
  for col,b in enumerate(self.states):
   for i in range(10):
    for j in range(10):
     q=b^(1<<j);a=q^(1<<i)
     if a:continue
     sign=(-1)**((b&((1<<j)-1)).bit_count()+(q&((1<<i)-1)).bit_count())*(1-2*((b>>j)&1))
     factor=1/self.d[i] if i==j else self.d[i]**(((b>>i)&1)-1)*self.d[j]**(((b>>j)&1)-1)
     self.ell[col]+=self.r[i][v]*(-self.kr[j][w]/2)*sign*factor
  if sum(x*x/w for x,w in zip(self.ell,self.W))!=6:raise ValueError('closing dual norm')
 def fock(self,Q):
  J={}
  for col,b in enumerate(self.states):
   z=sum(Q[i][i]/self.d[i]*(F((b>>i)&1)-F(1,2)) for i in range(10))
   if z:J[col,col]=z
   for i,j in combinations(range(10),2):
    bi=(b>>i)&1;bj=(b>>j)&1;sgn=(-1)**((b&((1<<i)-1)).bit_count()+(b&((1<<j)-1)).bit_count())
    z=F(sgn,2)*(Q[j][i]*(1-2*bi)-Q[i][j]*(1-2*bj))*self.d[i]**(bi-1)*self.d[j]**(bj-1)
    if z:J[self.ix[b^(1<<i)^(1<<j)],col]=z
  return J
 def matrix(self,mask):
  if mask & ~sum(1<<e for e in self.support):raise ValueError('outside support')
  out=dict(self.base)
  for e,D in self.delta.items():
   if mask>>e&1:
    for ij,v in D.items():out[ij]=out.get(ij,0)+v
  return {ij:v for ij,v in out.items() if v}

def candidate(vector,k,W):
 # This conversion may round: the resulting dyadics are arbitrary candidates.
 values=[]
 for x,w in zip(vector,W):
  z=float(x)*sqrt(6.)**k/sqrt(float(w))
  if not isfinite(z):raise ValueError('nonfinite converted candidate')
  values.append(F.from_float(z))
 den=max(x.denominator for x in values)
 return [int(x*den) for x in values],den

def upper_sqrt(x,D=10**50):
 if x<0:raise ValueError('negative squared norm')
 p=x.numerator*D*D;q=x.denominator;n=isqrt(p//q)
 if n*n*q<p:n+=1
 return F(n,D)

def incoming(parts):
 den=2*max(d for v,d in parts);v=[0]*512
 for x,d in parts:
  factor=den//(2*d)
  for i,z in enumerate(x):v[i]+=z*factor
 return v,den

def residual(model,A,cand,parts):
 x,dx=cand;b,db=incoming(parts);common=max(dx,db)
 r=[-z*(common//db)*model.den for z in b]
 factor=common//dx
 for (i,j),a in A.items():r[i]-=a*x[j]*factor
 sq=F(sum(w*z*z for w,z in zip(model.Wint,r)),model.Wden*(model.den*common)**2)
 return upper_sqrt(sq)

def gap(model,mask):
 ell=F(2449489742783178,10**15)
 if mask in [sum(1<<e for e,ab in enumerate(model.edges) if v in ab) for v in range(64)]:return 2*ell
 if not mask:raise ValueError('zero proper prefix')
 black=[i for i in range(64) if any(row[i] for row in model.r)];white=[i for i in range(64) if i not in black]
 # r-span does not contain every black coordinate! Use geometric bipartition.
 vs=list(product(range(4),repeat=3));black=[i for i,v in enumerate(vs) if sum(v)%2==0];white=[i for i in range(64) if i not in black]
 K=[row[:] for row in model.K]
 for e,(i,j) in enumerate(model.edges):
  if mask>>e&1:K[i][j]*=-1;K[j][i]*=-1
 A=[[F(sum(K[i][k]*K[j][k] for k in white),4)+F(25,4)*(i==j) for j in black] for i in black]
 L=[[F(i==j) for j in range(32)] for i in range(32)];D=[]
 for j in range(32):
  d=A[j][j]-sum(L[j][k]**2*D[k] for k in range(j))
  if d<=0:raise ValueError('positive LDL pivot')
  D.append(d)
  for i in range(j+1,32):L[i][j]=(A[i][j]-sum(L[i][k]*L[j][k]*D[k] for k in range(j)))/d
 V=[[F(i==j) for j in range(32)] for i in range(32)]
 for i in range(32):
  for j in range(i):V[i][j]=-sum(L[i][k]*V[k][j] for k in range(j,i))
 tr=sum(sum(v*v for v in row)/d for row,d in zip(V,D));bound=32*ell-(F(196,5)+F(5,2)*(32-F(25,4)*tr))
 return max(F(1,432),bound)
