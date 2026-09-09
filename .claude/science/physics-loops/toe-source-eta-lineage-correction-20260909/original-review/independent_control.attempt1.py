import os,signal,resource,time,json,itertools,collections
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('30 second bound')));signal.alarm(30)
resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
start=time.monotonic()
from fractions import Fraction as F
A=set([5,6,9,10,17,18,20,23,24,27,29,30,33,34,36,39,40,43,45,46,53,54,57,58])
c=collections.Counter()
for d in range(6):
 for x in range(64):
  if x&(1<<d):continue
  for y in range(64):
   if y&(1<<(d^1)):continue
   c[int(x in A)+int((y|(1<<(d^1))) in A)-int(y in A)-int((x|(1<<d)) in A)]+=1
assert c=={0:2112,1:1152,-1:1152,2:864,-2:864}
# Independent exact norm bound, directly telescope three products.
x=F(1,10**9); a=22*13*x;b=16*13*x
Y=F(22)/(1-a);R=F(20)/(1-b);dY=x*22**2*13/(1-a);dR=x*16*13*20/(1-b)
bound=2*(dR*Y*R+20*dY*R+20*22*dR)
assert bound==F(2193749493000038667200,177556693536960624997803) and bound<F(1,71)
# All undirected four-vertex graphs: adjacency-independent readiness proof control.
checks=0
for edges in range(64):
 adj=[set() for _ in range(4)]
 for k,(i,j) in enumerate(itertools.combinations(range(4),2)):
  if edges>>k&1:adj[i].add(j);adj[j].add(i)
 for m in range(16):
  O={i for i in range(4) if m>>i&1}; ready={i for i in range(4) if i not in O and adj[i]<=O}
  for i in ready:
   OO=O|{i};rr={j for j in range(4) if j not in OO and adj[j]<=OO};assert rr==ready-{i};checks+=1
# Exact Pauli control: claimed sufficient algebra, cylinders, covariance counterexample.
import sympy as s
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);Ds=[s.diag(X,X),s.diag(Y,-Y),s.diag(Z,Z)];I=s.eye(4)
chi=s.I*Ds[0]*Ds[1]*Ds[2]; assert sorted(chi.diagonal())==[-1,-1,1,1]
weights={}
for u in [s.Integer(1),s.Rational(1,2)]:
 def root(D,b):return s.sqrt((1+u)/2)*(I+(-1)**b*D)/2+s.sqrt((1-u)/2)*(I-(-1)**b*D)/2
 weights[str(u)]=[]
 for b,c0 in itertools.product(range(2),repeat=2):
  k=root(Ds[1],b);q=root(Ds[1] if b==0 else Ds[0],c0);weights[str(u)].append(str(s.simplify(s.trace(q*k*(I/4)*k*q))))
assert weights=={'1':['1/2','0','1/4','1/4'],'1/2':['5/16','3/16','1/4','1/4']}
Rmat=s.Matrix([[0,0,1],[0,-1,0],[1,0,0]]);shell=[(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
mask=sum(1<<shell.index(tuple(Rmat*s.Matrix(shell[k]))) for k in [0,4]);assert Rmat.det()==1 and mask==17
assert Rmat*s.Matrix([0,1,0])==s.Matrix([0,-1,0]); effect_residual=Ds[1];assert effect_residual.rank()==4
print(json.dumps({'curl_census':dict(c),'ready_appends':checks,'gram_bound':str(bound),'cylinders':weights,'covariance_counterexample':{'rotation':Rmat.tolist(),'fixed_mask':mask,'orientation_before':[0,1,0],'required_after':[0,-1,0],'effect_difference_rank':4},'elapsed_sec':time.monotonic()-start,'maxrss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},default=str,indent=2))
