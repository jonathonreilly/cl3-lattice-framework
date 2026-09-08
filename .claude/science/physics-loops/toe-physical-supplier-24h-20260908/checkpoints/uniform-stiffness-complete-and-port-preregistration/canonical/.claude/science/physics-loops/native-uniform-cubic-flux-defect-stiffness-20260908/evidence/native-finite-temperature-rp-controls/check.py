import itertools,json,time,signal,resource,hashlib
from pathlib import Path
signal.alarm(30)

t0=time.monotonic(); Z=(0,0); O=(1,0); I=(0,1)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def conj(a):return a[0],-a[1]
def eye(n):return [[O if i==j else Z for j in range(n)] for i in range(n)]
def scale(a,M):return [[mul(a,x) for x in r] for r in M]
def bar(M):return [[conj(x) for x in r] for r in M]
def mm(A,B):
 n=len(A); C=[[Z for _ in range(n)] for _ in range(n)]
 for i in range(n):
  for k in range(n):
   if A[i][k]!=Z:
    for j in range(n):
     if B[k][j]!=Z:C[i][j]=add(C[i][j],mul(A[i][k],B[k][j]))
 return C
def kron(A,B):return [[mul(a,b) for a in ar for b in br] for ar in A for br in B]
def tr(A):
 s=Z
 for i in range(len(A)):s=add(s,A[i][i])
 return s
X=[[Z,O],[O,Z]];Y=[[Z,(0,-1)],[I,Z]];ZZ=[[O,Z],[Z,(-1,0)]]
def car(n):
 out=[]
 for j in range(n):
  for pa in (X,Y):
   A=[[O]]
   for k in range(n):A=kron(A,ZZ if k<j else pa if k==j else eye(2))
   out.append(A)
 P=[[O]]
 for j in range(n):P=kron(P,ZZ)
 return out,P
count=0; killed={'wrong_cross_i':0,'missing_parity':0}; odd=even=0

def test(n,indices,L,R):
 global count,odd,even
 if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 384*1024**2:raise RuntimeError("RSS cap")
 a,P=car(n);d=2**n;m=len(indices)
 wl=L[0];wr=R[0];full=kron(L[0],bar(R[0]));bad=full;badp=full
 for k,j in enumerate(indices):
  wl=mm(mm(wl,a[j]),L[k+1]);wr=mm(mm(wr,a[j]),R[k+1])
  cross=kron(mm(a[j],P),bar(a[j]));tail=kron(L[k+1],bar(R[k+1]))
  full=mm(mm(full,scale(I,cross)),tail)
  bad=mm(mm(bad,cross),tail)
  badp=mm(mm(badp,scale(I,kron(a[j],bar(a[j])))),tail)
 expected=Z if m%2 else mul(tr(wl),conj(tr(wr)))
 if tr(full)!=expected:raise RuntimeError(('coefficient',n,indices,tr(full),expected))
 count+=1
 if m%2:odd+=1
 else:even+=1
 for key,v in [('wrong_cross_i',bad),('missing_parity',badp)]:
  if tr(v)!=expected:killed[key]+=1
 return tr(wl)
for m in range(4):
 for ix in itertools.product(range(2),repeat=m):
  for choices in itertools.product(range(2),repeat=2*(m+1)):
   basis=[eye(2),ZZ];test(1,ix,[basis[x] for x in choices[:m+1]],[basis[x] for x in choices[m+1:]])
a,P=car(2);basis=[eye(4)]+[scale(I,mm(a[i],a[j])) for i in range(4) for j in range(i+1,4)]+[P]
if mm(basis[1],basis[2])==mm(basis[2],basis[1]):raise RuntimeError('noncommuting fixture absent')
for m in range(7):
 for seed in range(16):
  ix=tuple((seed+3*k)%4 for k in range(m))
  L=[basis[(seed+k)%8] for k in range(m+1)];R=[basis[(3*seed+2*k+1)%8] for k in range(m+1)]
  test(2,ix,L,R)
# Exact Gram PSD minors for explicit unequal complex features.
f=[(1,2),(3,-1),(-2,1)];g=[(2,-1),(0,3),(1,1)]
aa=bb=ab=Z
for x,y in zip(f,g):aa=add(aa,mul(x,conj(x)));bb=add(bb,mul(y,conj(y)));ab=add(ab,mul(x,conj(y)))
det=add(mul(aa,bb),tuple(-x for x in mul(ab,conj(ab))))
if aa[1] or bb[1] or det[1] or det[0]<0:raise RuntimeError('Gram')
if not all(killed.values()):raise RuntimeError(('surviving mutant',killed))
r={'status':'PASS','coefficient_cases':count,'odd':odd,'even':even,'gram_determinant':det[0],'actual_mutation_mismatches':killed,'seconds':time.monotonic()-t0,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact finite coefficient controls; no all-size or thermal scan claim.'}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
