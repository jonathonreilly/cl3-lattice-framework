"""Unlaunched dimensionless t=1 coefficient solver with outward error ledger."""
from fractions import Fraction as F
from math import isqrt,nextafter,inf,sqrt,isfinite
from itertools import combinations
import numpy as np
EPS=2.0**-53
TINY=float.fromhex('0x0.0000000000001p-1022')
def up(x):
 if not isfinite(x) or x<0:raise ArithmeticError('nonfinite/negative upper bound')
 return nextafter(x,inf)
def plus(a,b):return up(a+b)
def times(a,b):return up(a*b)
def divide(a,b):
 if b<=0:raise ArithmeticError('nonpositive denominator')
 return up(a/b)
def sumup(xs):
 z=0.0
 for x in xs:z=plus(z,float(x))
 return z
def normup(x):return up(sqrt(sumup(times(abs(float(z)),abs(float(z))) for z in x)))
def gamma(n):return up(float(F(n,2**53-n)))
def fraction_up(x):return up(float(x))
def fraction_down(x):
 y=nextafter(float(x),-inf)
 if not y>0:raise ArithmeticError('nonpositive lower')
 return y
def algebraic(num,den):
 """Enclose rational num/sqrt(den) by exact integer square-root brackets."""
 num=F(num);den=F(den)
 if not num:return 0.0,0.0
 if den<=0:raise ArithmeticError('sqrt domain')
 scale=10**80;k=isqrt(den.numerator*scale**2//den.denominator)
 if not k:raise ArithmeticError('sqrt bracket underflow')
 lo=num/F(k+1,scale);hi=num/F(k,scale)
 if lo>hi:lo,hi=hi,lo
 z=float((lo+hi)/2);fz=F.from_float(z)
 return z,fraction_up(max(abs(fz-lo),abs(fz-hi)))
class Model:
 def __init__(self,raw):
  self.raw=raw;self.edges=[tuple(x) for x in raw['edge_order']];self.vs=[tuple(x) for x in raw['coordinates']];self.N=64
  ix={v:i for i,v in enumerate(self.vs)};K=[[0]*64 for _ in range(64)];generated=[]
  for v in self.vs:
   for a in range(3):
    w=list(v);w[a]=(w[a]+1)%4;i,j=sorted((ix[v],ix[tuple(w)]));generated.append((i,j));K[i][j]=-2*(-1)**sum(v[:a]);K[j][i]=-K[i][j]
  if generated!=self.edges:raise ValueError('edge dictionary')
  if any(sum(K[i][k]*K[k][j] for k in range(64))!=-24*(i==j) for i in range(64) for j in range(64)):raise ValueError('flat base')
  self.K=K;self.inc=[sum(1<<e for e,ab in enumerate(self.edges) if v in ab) for v in range(64)]
  S=sorted({v for e in raw['boundary_edges'] for v in self.edges[e]});black=[i for i,v in enumerate(self.vs) if sum(v)%2==0];self.black=black;self.white=[i for i in range(64) if i not in black]
  basis=[];norms=[]
  for s in S:
   b=[F(i==s) if s in black else F(K[i][s]) for i in range(64)]
   if s not in black:b=[x if i in black else F(0) for i,x in enumerate(b)]
   for c,d in zip(basis,norms):
    q=sum(x*y for x,y in zip(b,c))/d;b=[x-q*y for x,y in zip(b,c)]
   d=sum(x*x for x in b)
   if d:basis.append(b);norms.append(d)
  if len(basis)!=10:raise ValueError('rank10')
  self.basis=basis;self.norms=norms;KB=[[sum(K[i][j]*b[j] for j in range(64)) for i in range(64)] for b in basis]
  self.omega,self.omega_error=algebraic(24,24)
  self.base=np.eye(10)*self.omega;self.base_error=times(5,self.omega_error)
  support=set(raw['boundary_edges'])|{r['bridge_edge'] for r in raw['rows']};self.delta={}
  for e in sorted(support):
   v,w=self.edges[e];M=np.zeros((10,10));err=[]
   for i in range(10):
    for j in range(10):
     num=2*K[v][w]*(basis[i][v]*KB[j][w]-basis[i][w]*KB[j][v]);z,d=algebraic(num,24*norms[i]*norms[j]);M[i,j]=z;err.append(d)
   self.delta[e]=(M,times(.5,sumup(err)),sumup(abs(float(x)) for x in M.flat))
  self.states=np.array([b for b in range(1024) if b.bit_count()%2==0],dtype=np.int64);index={int(b):i for i,b in enumerate(self.states)}
  self.z=np.array([[1-2*((int(b)>>i)&1) for i in range(10)] for b in self.states]);self.pairs=[]
  for i,j in combinations(range(10),2):
   targets=np.array([index[int(b)^(1<<i)^(1<<j)] for b in self.states]);sg=np.array([(-1)**((int(b)&((1<<i)-1)).bit_count()+(int(b)&((1<<j)-1)).bit_count()) for b in self.states]);self.pairs.append((i,j,targets,sg))
  v,w=raw['centers']
  if v not in black or w in black or v>=w:raise ValueError('closing convention')
  M=np.zeros((10,10));errs=[]
  for i in range(10):
   for j in range(10):
    z,d=algebraic(-2*basis[i][v]*KB[j][w],24*norms[i]*norms[j]);M[i,j]=z;errs.append(d)
  H,rounding=self.fock(M);self.close=H[0].copy();self.close_error=plus(times(.5,sumup(errs)),rounding)
  self.gaps={};self.gap_records={}
 def fock(self,M):
  H=np.zeros((512,512));diag=np.sum(-.5*self.z*np.diag(M)[None,:],axis=1);np.fill_diagonal(H,diag)
  rows=np.arange(512)
  for i,j,targets,sg in self.pairs:H[targets,rows]=.5*sg*(M[j,i]*self.z[:,i]-M[i,j]*self.z[:,j])
  diagonal_abs=times(.5,sumup(abs(float(M[i,i])) for i in range(10)));off_abs=times(.5,sumup(abs(float(M[i,j])) for i in range(10) for j in range(10) if i!=j))
  error=plus(times(gamma(20),diagonal_abs),times(gamma(3),off_abs));error=plus(error,1e-300)
  return H,error
 def matrix(self,mask):
  M=self.base.copy();err=self.base_error;ab=sumup(abs(float(x)) for x in M.flat);n=0
  for e,(D,de,da) in self.delta.items():
   if mask>>e&1:M=M+D;err=plus(err,de);ab=plus(ab,da);n+=1
  err=plus(err,times(.5*gamma(n+1),ab));H,assembly=self.fock(M);offset=5*self.omega;diagmax=max(abs(float(H[i,i])) for i in range(512));H[np.diag_indices(512)]+=offset
  shift_error=plus(times(5,self.omega_error),times(gamma(3),plus(diagmax,abs(offset))))
  return H,plus(plus(err,assembly),shift_error)
 def gap(self,mask):
  if mask in self.gaps:return self.gaps[mask]
  ell=F(2449489742783178,10**15)
  if mask in self.inc:g=2*ell;record={'kind':'odd singleton parity','gap':str(g)}
  else:
   if not mask:raise ValueError('zero proper prefix')
   bi={v:i for i,v in enumerate(self.black)};wi={v:i for i,v in enumerate(self.white)};B=np.zeros((32,32),dtype=np.int64)
   for e,(v,w) in enumerate(self.edges):
    k=self.K[v][w]//2*(-1 if mask>>e&1 else 1)
    if v in bi:B[bi[v],wi[w]]=k
    else:B[bi[w],wi[v]]=-k
   E=B@B.T-6*np.eye(32,dtype=np.int64)
   if int(np.max(abs(E)))>6 or 192*30**9>=2**63:raise ValueError('integer bound')
   P=np.eye(32,dtype=np.int64);tr=[]
   for _ in range(10):P=P@E;tr.append(int(np.trace(P)))
   c=[1]
   for k in range(1,11):
    num=sum((-1)**(j-1)*c[k-j]*tr[j-1] for j in range(1,k+1))
    if num%k:raise ValueError('Newton integrality')
    c.append(num//k)
   s=F(49,4);q=sum(F(c[k])*s**(10-k) for k in range(11));qp=sum(F(c[k])*(10-k)*s**(9-k) for k in range(10))
   if q<=0:raise ValueError('positive determinant')
   ti=22/s+qp/q;upper=F(196,5)+F(5,2)*(32-F(25,4)*ti)
   g=32*ell-upper;kind='rational Newton trace'
   if g<=0:g=F(1,432);kind='prospective global fallback'
   record={'kind':kind,'gap':str(g),'polynomial':c}
  self.gaps[mask]=fraction_down(g);self.gap_records[str(mask)]=record;return self.gaps[mask]
def residual_certificate(A,matrix_error,x,b,incoming_error,gap):
 xn=normup(x);res=A@x+b;absolute=np.abs(A)@np.abs(x)
 dotbound=plus(divide(normup(absolute),nextafter(1-gamma(512),-inf)),normup(b))
 residual=plus(normup(res),times(gamma(514),dotbound));residual=plus(residual,times(matrix_error,xn));residual=plus(residual,1e-300)
 return divide(plus(incoming_error,residual),gap),residual
def solve_bridge(model,row):
 bridge=row['bridge_edge'];boundary=model.raw['boundary_edges'];terms=[(a,b) for a,b in combinations(sorted(boundary+[bridge]),2) if set(model.edges[a])&set(model.edges[b])]
 keys={(int(x['boundary_used_mask']),x['bridge_count']):x for x in row['prefixes']};target=(sum(1<<e for e in boundary),2);vac=np.zeros(512);vac[0]=1
 layer={(0,0):(vac,0.0,1.0,1)};ledger=[]
 for k in range(1,7):
  incoming={}
  for key,data in layer.items():
   used,c=key
   for a,b in terms:
    bd=[e for e in (a,b) if e!=bridge]
    if any(used>>e&1 for e in bd):continue
    q=(used|sum(1<<e for e in bd),c+int(a==bridge)+int(b==bridge))
    if q in keys:incoming.setdefault(q,[]).append(data)
  nxt={}
  for q,parts in incoming.items():
   b=np.zeros(512);en=0.0;normsum=0.0;count=0
   for x,e,n,c in parts:b=b+.5*x;en=plus(en,times(.5,e));normsum=plus(normsum,times(.5,n));count+=c
   en=plus(en,times(gamma(2*len(parts)+2),normsum));en=plus(en,1e-300)
   if k==6:x=b;error=en
   else:
    mask=int(keys[q]['full_toggle_mask']);A,ae=model.matrix(mask);gap=model.gap(mask);x=-np.linalg.solve(A,b)
    if not np.isfinite(x).all():raise ArithmeticError('nonfinite solve')
    error,residual=residual_certificate(A,ae,x,b,en,gap)
    ledger.append({'k':k,'boundary_used_mask':str(q[0]),'bridge_count':q[1],'toggle_mask':str(mask),'gap_lower':gap,'matrix_operator_error':ae,'residual_bound':residual,'incoming_error':en,'solution_error':error,'word_count':count})
   nxt[q]=(x,error,normup(x),count)
  layer=nxt
 x,error,xn,count=layer[target]
 if count!=row['unordered_pair_sets']*720:raise ValueError('word count')
 center=-float(model.close@x);dotabs=float(np.abs(model.close)@np.abs(x));rounding=times(gamma(512),divide(up(dotabs),nextafter(1-gamma(512),-inf)));radius=plus(error,plus(times(model.close_error,xn),rounding))
 if not isfinite(center):raise ArithmeticError('nonfinite result')
 return {'bridge':bridge,'coefficient':center,'absolute_error_bound':radius,'interval':[nextafter(center-radius,-inf),nextafter(center+radius,inf)],'word_count':count,'proper_keys':len(ledger),'ledger':ledger,'gap_records':model.gap_records,'scope':'dimensionless t=1 coefficient of ordered i bar_gamma_0 bar_gamma_16; IEEE754/error-model assumptions explicit'}
