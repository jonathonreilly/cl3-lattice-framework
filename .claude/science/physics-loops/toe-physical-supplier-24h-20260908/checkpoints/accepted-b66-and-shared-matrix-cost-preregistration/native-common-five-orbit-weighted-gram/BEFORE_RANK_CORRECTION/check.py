"""Exact seven-source selector and orbit algebra only; no native scalar/matrix input."""
from fractions import Fraction as F
from itertools import combinations,permutations,product
import json,time,signal,resource
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('29s exact scope')));signal.alarm(29)
start=time.monotonic();n=0

def ck(x):
 global n
 if not x:raise ValueError('exact common-frame check')
 n+=1

def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def scale(a,c):return [[c*x for x in r] for r in a]
def add(*args):return [[sum(a[i][j] for a in args) for j in range(len(args[0][0]))] for i in range(len(args[0]))]
def rank(a):
 a=[r[:] for r in a];k=0
 for j in range(len(a[0])):
  candidates=[i for i in range(k,len(a)) if a[i][j]]
  if not candidates:continue
  i=candidates[0];a[i],a[k]=a[k],a[i];v=a[k][j];a[k]=[x/v for x in a[k]]
  for i in range(len(a)):
   if i!=k:
    v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
  k+=1
 return k
I=[[F(i==j) for j in range(7)] for i in range(7)];O=[[F(0)]*7 for _ in range(7)];T=[[F(0)]*7 for _ in range(7)]
for i in range(6):O[i+1][(i^1)+1]=1;T[0][i+1]=-(-1)**i;T[i+1][0]=(-1)**i
N=add(I,O)
def W(a,c):
 w=[[F(0)]*3 for _ in range(7)];w[0][0]=1
 for j,pair in [(1,a),(2,c)]:
  for i in pair:w[i+1][j]=(-1)**i
 return w

def params(a,c):return (int(a[0]^1==a[1]),int(c[0]^1==c[1]),sum((i^1) in c for i in a))
reps=[((0,1),(2,3)),((0,1),(2,4)),((0,2),(4,5)),((0,2),(1,3)),((0,2),(1,4))]
expected=[(1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1)];counts={q:0 for q in expected};neighborcols=[]
for a,c in reps:
 neighborcols.extend(tr(W(a,c))[1:])
ck(rank(tr(neighborcols))==6)
for a in combinations(range(6),2):
 for c in combinations([i for i in range(6) if i not in a],2):
  oa,oc,k=params(a,c);counts[oa,oc,k]+=1;w=W(a,c);wt=tr(w)
  ip=[[F(1),0,0],[0,2,0],[0,0,2]];op=[[0,0,0],[0,-2*oa,-k],[0,-k,-2*oc]];tp=[[0,-2,-2],[2,0,0],[2,0,0]]
  ck(mm(mm(wt,I),w)==ip);ck(mm(mm(wt,O),w)==op);ck(mm(mm(wt,T),w)==tp)
  for s in [F(1,2),F(2)]:
   A,Ap,B,Bp=F(2,7),F(-3,11),F(5,13),F(-7,17) # formal synthetic coefficients
   D=(1-s*s*A)/6;Dp=-(2*s*A+s*s*Ap)/6
   for sig in [-1,1]:
    full=[add(scale(N,sig*s*A),scale(O,-sig*s*D),scale(T,D)),add(scale(N,sig*(A+s*Ap)),scale(O,-sig*(D+s*Dp)),scale(T,Dp)),add(scale(N,-B),scale(O,-s*s*B/6),scale(T,sig*s*B/6)),add(scale(N,-Bp),scale(O,-(2*s*B+s*s*Bp)/6),scale(T,sig*(B+s*Bp)/6))]
    ga,gc=(D if oa else A),(D if oc else A);gpa,gpc=(Dp if oa else Ap),(Dp if oc else Ap)
    la,lc=(s*s*B/3 if oa else -2*B),(s*s*B/3 if oc else -2*B)
    lpa,lpc=((2*s*B+s*s*Bp)/3 if oa else -2*Bp),((2*s*B+s*s*Bp)/3 if oc else -2*Bp)
    reduced=[[[sig*s*A,-2*D,-2*D],[2*D,2*sig*s*ga,k*sig*s*(D-A)],[2*D,k*sig*s*(D-A),2*sig*s*gc]],[[sig*(A+s*Ap),-2*Dp,-2*Dp],[2*Dp,2*sig*(ga+s*gpa),k*sig*(D-A+s*(Dp-Ap))],[2*Dp,k*sig*(D-A+s*(Dp-Ap)),2*sig*(gc+s*gpc)]],[[-B,-sig*s*B/3,-sig*s*B/3],[sig*s*B/3,la,k*B*(1+s*s/6)],[sig*s*B/3,k*B*(1+s*s/6),lc]],[[-Bp,-sig*(B+s*Bp)/3,-sig*(B+s*Bp)/3],[sig*(B+s*Bp)/3,lpa,k*(Bp*(1+s*s/6)+s*B/3)],[sig*(B+s*Bp)/3,k*(Bp*(1+s*s/6)+s*B/3),lpc]]]
    for f,r in zip(full,reduced):ck(mm(mm(wt,f),w)==r)
ck([counts[q] for q in expected]==[6,12,12,12,48])
orbits=[set() for _ in reps]
for perm in permutations(range(3)):
 for signs in product([-1,1],repeat=3):
  image=[];R=[[F(0)]*7 for _ in range(7)];R[0][0]=1
  for i in range(6):
   j=2*perm[i//2]+int(signs[i//2]*(-1)**i<0);image.append(j);R[j+1][i+1]=signs[i//2]
  for m in [N,O,T]:ck(mm(mm(tr(R),m),R)==m)
  for q,(a,c) in enumerate(reps):orbits[q].add((tuple(sorted(image[i] for i in a)),tuple(sorted(image[i] for i in c))))
ck([len(x) for x in orbits]==[6,12,12,12,48]);ck(len(set.union(*orbits))==90)
eps=F(48166272,10**19)
ck(4*529*1584*eps<F(4099,10**6)**2);ck(1584*eps<F(1,10**6))
for ep,target in [(F(2**38,10**30),F(1,10**6)),(F(1,2**60),F(2,10**6))]:
 ck(4*529*1584*ep<(target-F(1,10**9))**2);ck(1584*ep<F(1,10**9))
ck(F(529,2**40)<F(1,10**9));ck(F(41,10000)+F(3,10**6)+F(2,10**9)<F(1,200))
seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;ck(seconds<30 and rss<384*1048576)
print(json.dumps({'status':'PASS','predicates':n,'ordered_pairs':90,'magnetic_star_lifts':48,'multiplicities':[len(x) for x in orbits],'common_raw_dimension':396,'common_closed_dimension':792,'universal_source_rank':7,'seconds':seconds,'rss_bytes':rss,'physical_calls':0},indent=2))
