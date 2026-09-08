from fractions import Fraction as F
from itertools import product,combinations
V=list(product(range(4),repeat=3));vi={x:i for i,x in enumerate(V)};K=[[0]*64 for _ in V];edges=[]
for r in V:
 for a in range(3):
  s=list(r);s[a]=(s[a]+1)%4;i,j=sorted((vi[r],vi[tuple(s)]));val=-2*(-1)**sum(r[:a]);K[i][j]=val;K[j][i]=-val;edges.append((i,j))
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def mv(A,x):return [dot(r,x) for r in A]
star=[e for e,ab in enumerate(edges) if 0 in ab];neighbors=sorted({v for e in star for v in edges[e]}-{0})
r=[]
for v in [0]+neighbors:
 x=[F(int(i==0)) for i in range(64)] if v==0 else [F(K[i][v]) for i in range(64)]
 for b in r:
  c=dot(x,b)/dot(b,b);x=[a-c*z for a,z in zip(x,b)]
 if any(x):r.append(x)
d=[dot(x,x) for x in r];n=len(r);kr=[mv(K,x) for x in r]
bits={p:[b for b in range(1<<n) if b.bit_count()%2==p] for p in (0,1)}
W={p:[__import__('functools').reduce(lambda x,i:x*d[i],[i for i in range(n) if b>>i&1],F(1)) for b in bits[p]] for p in (0,1)}
def changed(mask):
 A=[row[:] for row in K]
 for e,(i,j) in enumerate(edges):
  if mask>>e&1:A[i][j]*=-1;A[j][i]*=-1
 return A
def matrix(mask,p):
 KF=changed(mask);kfr=[mv(KF,y) for y in kr];q=[[-dot(x,y)/12 for y in kfr] for x in r];bs=bits[p];ix={b:i for i,b in enumerate(bs)};A=[[F(0) for _ in bs] for _ in bs]
 for col,b in enumerate(bs):
  A[col][col]=sum(q[i][i]/d[i]*(F((b>>i)&1)-F(1,2)) for i in range(n))+n
  for i,j in combinations(range(n),2):
   target=b^(1<<i)^(1<<j);sgn=(-1)**((b&((1<<i)-1)).bit_count()+(b&((1<<j)-1)).bit_count())
   A[ix[target]][col]=F(sgn,2)*(q[j][i]*(1-2*((b>>i)&1))-q[i][j]*(1-2*((b>>j)&1)))*d[i]**(((b>>i)&1)-1)*d[j]**(((b>>j)&1)-1)
 return A
def gamma(p):
 G=[[F(0) for _ in bits[p]] for _ in bits[1-p]];ix={b:i for i,b in enumerate(bits[1-p])}
 for j,b in enumerate(bits[p]):
  for i in range(n):G[ix[b^(1<<i)]][j]=(-1)**((b&((1<<i)-1)).bit_count())*r[i][0]*(F(1) if b>>i&1 else 1/d[i])
 return G
def solve(A,b):
 M=[row[:]+[x] for row,x in zip(A,b)];N=len(b)
 for j in range(N):
  pivot=next(i for i in range(j,N) if M[i][j]);M[j],M[pivot]=M[pivot],M[j];v=M[j][j];M[j]=[x/v for x in M[j]]
  for i in range(N):
   if i!=j:
    v=M[i][j]
    if v:M[i]=[x-v*y for x,y in zip(M[i],M[j])]
 x=[row[-1] for row in M]
 if mv(A,x)!=b:raise ValueError('exact solve residual')
 return x
pairs=list(combinations(star,2))
def mask(pair):return sum(1<<e for e in pair)
def controls():
 if n!=6 or len(star)!=6 or len(pairs)!=15:raise ValueError('dimension')
 for i,x in enumerate(r):
  if mv(K,mv(K,x))!=[-24*a for a in x]:raise ValueError('canonical flat restriction')
  for j,y in enumerate(r):
   if dot(x,y)!=(d[i] if i==j else 0):raise ValueError('orthogonal frame')
 for v in [0]+neighbors:
  norm=sum(x[v]**2/dd for x,dd in zip(r,d))+sum(x[v]**2/(24*dd) for x,dd in zip(kr,d))
  if norm!=1:raise ValueError('endpoint containment')
 for p in (0,1):
  A=matrix(0,p)
  for i,b in enumerate(bits[p]):
   if A[i]!=[F(2*b.bit_count() if i==j else 0) for j in range(32)]:raise ValueError("base particle energies")
 G=gamma(0);H=gamma(1)
 a=matrix(mask(star),1);b=matrix(0,0)
 for j in range(32):
  e=[F(int(i==j)) for i in range(32)]
  if mv(H,mv(G,e))!=e:raise ValueError('gamma square')
  if mv(a,mv(G,e))!=mv(G,mv(b,e)):raise ValueError('Gauss intertwiner')
 for pair in pairs:
  for p in (0,1):
   A=matrix(mask(pair),p)
   for i in range(32):
    for j in range(32):
     if W[p][i]*A[i][j]!=W[p][j]*A[j][i]:raise ValueError('metric Hermiticity')
 if sum(not(set(a)&set(c)) for a in pairs for c in pairs)!=90:raise ValueError('90 words')
 return dict(frame_rank=6,real_active_dimension=12,parity_dimension=32,pairs=15,grouped_words=90)
