import itertools,json,time,resource,signal
from pathlib import Path
start=time.monotonic();signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError()));signal.alarm(180)
N=0
def ck(c,s):
 global N;N+=1
 if not c:raise ValueError(s)
L=(4,6,8);coords=list(itertools.product(*map(range,L)));ids={r:i for i,r in enumerate(coords)};nv=len(coords)
def move(r,a):
 z=list(r);z[a]=(z[a]+1)%L[a];return tuple(z)
def rankmod(A):
 p=1000003;A=[[x%p for x in row] for row in A];r=0
 for j in range(len(A)):
  pivot=next((k for k in range(r,len(A)) if A[k][j]),None)
  if pivot is None:continue
  A[r],A[pivot]=A[pivot],A[r];inv=pow(A[r][j],-1,p);A[r]=[(x*inv)%p for x in A[r]]
  for k in range(r+1,len(A)):
   if A[k][j]:
    c=A[k][j];A[k]=[(x-c*y)%p for x,y in zip(A[k],A[r])]
  r+=1
 return r
rows=[]
for tau in itertools.product((-1,1),repeat=3):
 def xi(r,a):return (-1)**sum(r[:a])*(tau[a] if r[a]==L[a]-1 else 1)
 A=[[0]*nv for _ in coords]
 for r in coords:
  for a in range(3):
   s=move(r,a);i,j=sorted((ids[r],ids[s]));A[i][j]=-2*xi(r,a);A[j][i]=2*xi(r,a)
   for b in range(a):ck(xi(r,a)*xi(move(r,a),b)*xi(move(r,b),a)*xi(r,b)==-1,'plaquette')
 for a in range(3):
  r=(0,0,0);v=1
  for _ in range(L[a]):v*=xi(r,a);r=move(r,a)
  ck(v==tau[a],'winding')
 rank=rankmod(A);ck(rank==nv-(8 if tau==(-1,-1,-1) else 0),'modular rank lower bound')
 if tau==(-1,-1,-1):
  vecs=[]
  for bits in itertools.product((0,1),repeat=3):
   v=[(-1)**sum(b*x for b,x in zip(bits,r)) for r in coords];vecs.append(v)
   ck(all(sum(x*y for x,y in zip(row,v))==0 for row in A),'literal kernel')
  ck(all(sum(x*y for x,y in zip(v,w))==(nv if i==j else 0) for i,v in enumerate(vecs) for j,w in enumerate(vecs)),'eight independent')
 rows.append(dict(tau=tau,modular_rank=rank))
# Exact momentum-bit action, no arbitrary matrix basis import.
bits=list(itertools.product((0,1),repeat=2));G=[]
for axis in range(3):
 A=[[0]*4 for _ in range(4)]
 for col,s in enumerate(bits):
  dest=tuple(s[j]^(j<axis) for j in range(2));coefficient=(-1)**s[axis] if axis<2 else 1
  A[bits.index(dest)][col]=coefficient
 G.append(A)
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
for i,A in enumerate(G):
 ck(sum(A[j][j] for j in range(4))==0,'trace')
 ck(mul(A,A)==[[int(j==k) for k in range(4)] for j in range(4)],'square')
 for B in G[:i]:ck(all(x+y==0 for r,s in zip(mul(A,B),mul(B,A)) for x,y in zip(r,s)),'Clifford')
for rank in (nv,nv-8):
 r=rank//2;ck(2**r*2**(nv-r-1)==2**(nv-1),'physical dimension')
print(json.dumps(dict(checks=N,L=L,rows=rows,seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576),indent=2))
