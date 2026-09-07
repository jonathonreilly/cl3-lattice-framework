import time,signal,sys,resource,json,hashlib,itertools,os
from pathlib import Path
START=time.monotonic();signal.alarm(180)
os.environ['OPENBLAS_NUM_THREADS']='1'
import sympy as s
k=s.symbols('k',positive=True)
V=list(itertools.product((0,1),repeat=4));edges=[]
for v in V:
 for a in range(4):
  if not v[a]:
   w=list(v);w[a]=1;edges.append((v,tuple(w)))
def square(a,b,fixed):
 v=[0]*4
 for axis,val in fixed.items():v[axis]=val
 vs=[tuple(v)];v[a]=1;vs.append(tuple(v));v[b]=1;vs.append(tuple(v));v[a]=0;vs.append(tuple(v))
 return [(edges.index((u,w)),1) if (u,w) in edges else (edges.index((w,u)),-1) for u,w in zip(vs,vs[1:]+vs[:1])]
sources=[square(0,1,{2:0,3:t}) for t in (0,1)]
parent={v:v for v in V}
def root(v):
 while parent[v]!=v:v=parent[v]
 return v
tree=[]
for e in [e for src in sources for e,z in src[:3]]+list(range(32)):
 if e in tree:continue
 u,v=edges[e];ru,rv=root(u),root(v)
 if ru!=rv:parent[rv]=ru;tree.append(e)
chords=[e for e in range(32) if e not in tree];rows=[];weights=[]
for a,b in itertools.combinations(range(4),2):
 rest=[j for j in range(4) if j not in (a,b)]
 for vals in itertools.product((0,1),repeat=2):
  fixed=dict(zip(rest,vals))
  if (a,b)==(0,1) and fixed[2]==0:continue
  word=square(a,b,fixed);rows.append([sum(z for e,z in word if e==c) for c in chords]);weights.append(k if b==3 else s.Rational(1,2))
B=s.Matrix(rows);S=s.Matrix([[sum(z for e,z in word if e==c) for c in chords] for word in sources]);H=B.T*s.diag(*weights)*B
# DomainMatrix uses polynomial exact arithmetic rather than repeated symbolic pivots.
Hi=H.inv(method='DM');C=(S*Hi*S.T).applyfunc(s.factor);det=s.factor(H.det(method='domain-ge'))
checks=[]
def check(n,b):
 assert b,n;checks.append(n)
check('same independently constructed adapted tree',tree==[0,20,12,4,23,15,2,3,6,7,8,10,11,17,19])
check('22weighted faces',len(weights)==22 and weights.count(k)==12)
check('positive constant symmetric covariance mode',s.factor(C[0,0]+C[0,1]-10)==0)
check('rational antisymmetric covariance mode',s.factor(C[0,0]-C[0,1]-2*(4*k+5)/(4*k*k+6*k+1))==0)
check('source exchange symmetry',C[0,0]==C[1,1] and C[0,1]==C[1,0])
check('determinant exact',s.factor(det-k**7*(k+1)**2*(2*k+3)*(4*k*k+6*k+1)/8)==0)
check('isotropic covariance recovered',C.subs(k,1)==s.Matrix([[64,46],[46,64]])/11)
check('zero temporal rank loss',H.subs(k,0).rank()==10)
# Generator contractions in explicit trace-orthonormal coordinates.
I=s.I;r=s.sqrt(2)
T=[s.Matrix([[0,1,0],[1,0,0],[0,0,0]])/r,s.Matrix([[0,-I,0],[I,0,0],[0,0,0]])/r,s.diag(1,-1,0)/r,s.Matrix([[0,0,1],[0,0,0],[1,0,0]])/r,s.Matrix([[0,0,-I],[0,0,0],[I,0,0]])/r,s.Matrix([[0,0,0],[0,0,1],[0,1,0]])/r,s.Matrix([[0,0,0],[0,0,-I],[0,I,0]])/r,s.diag(1,1,-2)/s.sqrt(6)]
x,y=s.symbols('x y',real=True);W=s.diag(x,y,-x-y);q=s.trace(W**2);c=s.trace(W**3)
gc=[3*s.trace(W**2*A) for A in T];gq=[2*s.trace(W*A) for A in T]
check('q gradient squared4q',s.expand(sum(z*z for z in gq)-4*q)==0)
check('q c gradient contraction6c',s.expand(sum(a*b for a,b in zip(gq,gc))-6*c)==0)
check('c gradient squared3q2/2',s.expand(sum(z*z for z in gc)-s.Rational(3,2)*q*q)==0)
check('c harmonic',s.expand(sum(6*s.trace(W*A*A) for A in T))==0)
check('q Laplacian16',sum(2*s.trace(A*A) for A in T)==16)
check('discriminant domain polynomial',s.factor(q**3/6-c**2)==s.Rational(1,3)*(x-y)**2*(2*x+y)**2*(x+2*y)**2)
seconds=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
assert seconds<180 and rss<180
out=dict(status='PASS',TOTAL=len(checks),checks=checks,tree=tree,chords=chords,face_rows=rows,weights=list(map(str,weights)),source_rows=[list(S.row(i)) for i in range(2)],C=[[str(C[i,j]) for j in range(2)] for i in range(2)],determinant=str(det),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=seconds,rss_MiB=rss)
out['source_rows']=[[int(x) for x in row] for row in out['source_rows']]
print(json.dumps(out,indent=2))
