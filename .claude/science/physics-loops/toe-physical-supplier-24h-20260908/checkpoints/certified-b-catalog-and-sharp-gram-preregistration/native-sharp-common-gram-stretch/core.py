"""Exact outward arithmetic; import performs no physical work."""
from fractions import Fraction as F
BITS=48
S=1<<BITS
class Iv:
 def __init__(self,a,b=None):
  self.lo=F(a);self.hi=F(a if b is None else b)
  if self.lo>self.hi:raise ValueError('reversed interval')
 @staticmethod
 def rounded(a,b):return Iv(F((a*S).__floor__(),S),F((b*S).__ceil__(),S))
 def __add__(self,b):
  b=iv(b);return Iv.rounded(self.lo+b.lo,self.hi+b.hi)
 __radd__=__add__
 def __neg__(self):return Iv(-self.hi,-self.lo)
 def __sub__(self,b):return self+-iv(b)
 def __rsub__(self,b):return iv(b)+-self
 def __mul__(self,b):
  b=iv(b);v=[x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)];return Iv.rounded(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,b):
  b=iv(b)
  if b.lo<=0<=b.hi:raise ValueError('interval divisor contains zero')
  return self*Iv.rounded(1/b.hi,1/b.lo)
 def json(self):return [str(self.lo),str(self.hi)]
def iv(x):return x if isinstance(x,Iv) else Iv(x)
def operators():
 I=[[int(a==b) for b in range(7)] for a in range(7)];O=[[0]*7 for _ in range(7)];T=[[0]*7 for _ in range(7)]
 for a in range(3):
  u=1+2*a;v=u+1;O[u][v]=O[v][u]=1;T[0][u]=-1;T[0][v]=1;T[u][0]=1;T[v][0]=-1
 return [[I[a][b]+O[a][b] for b in range(7)] for a in range(7)],O,T

def coefficients(s,sigma,data):
 A,Ap,B,Bp=data;N,O,T=operators();D=(1-s*s*A)/6;Dp=-(2*s*A+s*s*Ap)/6
 C=[];Cp=[];L=[];Lp=[]
 for a in range(7):
  cr=[];cpr=[];lr=[];lpr=[]
  for b in range(7):
   n,o,t=N[a][b],O[a][b],T[a][b]
   E=A*n-D*o;Ep=Ap*n-Dp*o
   cr.append(sigma*s*E+D*t);cpr.append(sigma*(E+s*Ep)+Dp*t)
   lr.append(-B*n-s*s*B*o/6+sigma*s*B*t/6)
   lpr.append(-Bp*n-(2*s*B+s*s*Bp)*o/6+sigma*(B+s*Bp)*t/6)
  C.append(cr);Cp.append(cpr);L.append(lr);Lp.append(lpr)
 return C,Cp,L,Lp
LABELS=((1,1),(1,-1),(2,1),(2,-1))
def assemble(data):
 cache={(s,sig):coefficients(s,sig,data[s]) for s,sig in LABELS}
 size=28;G=[[Iv(0) for _ in range(size)] for _ in range(size)];J=[[Iv(0) for _ in range(size)] for _ in range(size)]
 for i in range(size):
  s,sig=LABELS[i//7];a=i%7
  for j in range(i,size):
   t,tau=LABELS[j//7];b=j%7;den=sig*s+tau*t
   if den:
    g=(cache[t,tau][0][a][b]-cache[s,-sig][0][a][b])/den
    z=-(cache[t,tau][2][a][b]-cache[s,-sig][2][a][b])/den
   else:
    g=cache[t,tau][1][a][b]/tau;z=-cache[t,tau][3][a][b]/tau
   G[i][j]=G[j][i]=g
   J[i][j]=z if i!=j else Iv(0);J[j][i]=-J[i][j]
 return G,J

def trace(G):return sum((G[i][i] for i in range(len(G))),Iv(0))
def pivot(G,J,i):
 n=len(G);r=G[i][i]
 if r.lo<=0:raise ValueError('uncertified positive pivot')
 g=G[i];j=J[i];A=[[Iv(0) for _ in range(n)] for _ in range(n)];B=[[Iv(0) for _ in range(n)] for _ in range(n)]
 for a in range(n):
  for b in range(a,n):
   A[a][b]=A[b][a]=G[a][b]-(g[a]*g[b]+j[a]*j[b])/r
   B[a][b]=J[a][b]-(g[a]*j[b]-j[a]*g[b])/r if a!=b else Iv(0);B[b][a]=-B[a][b]
 for a in range(n):A[i][a]=A[a][i]=B[i][a]=B[a][i]=Iv(0)
 return A,B

def compress(G,J,progress):
 initial=trace(G);rows=[]
 for step in range(29):
  residual=trace(G);upper=max(F(0),residual.hi)
  if residual.hi<0:raise ValueError('negative residual upper bound')
  square=4*max(F(0),initial.hi)*upper
  row={'pairs':step,'residual_trace':residual.json(),'error_squared_upper_for_coefficient_norm_le_one':str(square)};rows.append(row);progress(rows)
  if square<=F(1,4):return 'CERTIFIED_MODEST_CONDITIONAL_OPERATOR_ERROR',rows,initial
  if step==28:return 'INDETERMINATE_PAIR_CAP',rows,initial
  i=max(range(len(G)),key=lambda k:(G[k][k].lo,-k))
  row['next_index']=i;row['next_pivot']=G[i][i].json();progress(rows)
  if G[i][i].lo<=0:return 'INDETERMINATE_POSITIVE_PIVOT',rows,initial
  G,J=pivot(G,J,i)
 raise RuntimeError('unreachable')
