import itertools,json,time,resource,hashlib
from fractions import Fraction
from pathlib import Path
start=time.monotonic(); count=0
def require(p,s):
 global count
 count+=1
 if not p: raise RuntimeError(s)
def add(A,B):
 C=dict(A)
 for ij,v in B.items(): C[ij]=C.get(ij,0)+v
 return {ij:v for ij,v in C.items() if v}
def scale(A,c):return {ij:c*v for ij,v in A.items() if c*v}
def mul(A,B):
 rows={}
 for (j,k),v in B.items():rows.setdefault(j,[]).append((k,v))
 C={}
 for (i,j),u in A.items():
  for k,v in rows.get(j,[]):C[i,k]=C.get((i,k),0)+u*v
 return {ij:v for ij,v in C.items() if v}
def rank(A,n):
 rows=[{j:Fraction(v) for (i,j),v in A.items() if i==r} for r in range(n)]; piv={}
 for row in rows:
  while row:
   j=min(row)
   if j not in piv:
    v=row[j];piv[j]={k:w/v for k,w in row.items()};break
   v=row[j]
   for k,w in piv[j].items():
    row[k]=row.get(k,0)-v*w
    if not row[k]:del row[k]
 return len(piv)
results=[]
for L in [(4,4,4),(4,4,6)]:
 coords=list(itertools.product(*(range(l) for l in L)));idx={r:i for i,r in enumerate(coords)};n=len(coords)
 for tau in itertools.product([-1,1],repeat=3):
  K={};Ds=[];expected={}
  for a in range(3):
   T={};D={}
   for r in coords:
    s=list(r);s[a]=(s[a]+1)%L[a];s=tuple(s);i,j=idx[r],idx[s]
    eta=(-1)**sum(r[:a]);xi=eta*(tau[a] if r[a]==L[a]-1 else 1)
    lo,hi=sorted((i,j));K[lo,hi]=-2*xi;K[hi,lo]=2*xi
    b=-tau[a] if r[a]==L[a]-1 else 1
    T[i,j]=b
    D[i,j]=eta*b;D[j,i]=-eta*b
   Ds.append(D)
   Td={(j,i):v for (i,j),v in T.items()}
   expected=add(expected,scale(add(add(mul(T,T),mul(Td,Td)),{(i,i):-2 for i in range(n)}),-4))
  require(K==scale(add(add(Ds[0],Ds[1]),Ds[2]),-2),'literal canonical K')
  for a in range(3):
   for b in range(a):require(not add(mul(Ds[a],Ds[b]),mul(Ds[b],Ds[a])),'anticommutation')
  require(scale(mul(K,K),-1)==expected,'exact squared dispersion')
  rk=rank(K,n);require(rk==n-(8 if tau==(-1,-1,-1) else 0),'exact zero mode rank')
  results.append({'L':L,'tau':tau,'rank':rk,'active_zero_modes':n-rk})
require(results[0]['rank']!=results[7]['rank'],'seam omission adverse distinguishes ranks')
print(json.dumps({'predicates':count,'rows':results,'seconds':time.monotonic()-start,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
