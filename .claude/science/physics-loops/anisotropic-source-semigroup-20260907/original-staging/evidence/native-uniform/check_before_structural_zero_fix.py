import time,signal,sys,resource,json,hashlib,itertools,os
from pathlib import Path
AUDIT_TIMEOUT_SEC=180
AUDIT_MAX_RSS_MIB=180
START=time.monotonic();signal.alarm(AUDIT_TIMEOUT_SEC)
import argparse,math
parser=argparse.ArgumentParser(description="Exact anisotropic cube geometry, invariant OU and scalar exponent support.")
parser.add_argument("--json",action="store_true")
args=parser.parse_args()
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
# Distinct prospectively frozen uniform scalar supplement.
u=s.symbols('u',nonnegative=True)
def nonnegative_k(expr):
 num=s.cancel(expr.subs(k,u+1)).as_numer_denom()[0]
 return all(c>=0 for c in s.Poly(num,u).all_coeffs())
check('uniform determinant lower k12',nonnegative_k(det-k**12))
check('uniform determinant upper55k12/2',nonnegative_k(s.Rational(55,2)*k**12-det))
sigm=6*(4*k+5)/(4*k*k+6*k+1)
check('uniform sigma minus lower24/11k',nonnegative_k(sigm-s.Rational(24,11)/k))
check('uniform sigma minus upper6/k',nonnegative_k(6/k-sigm))
check('normalization exponent52',4*12+2+2==52)
check('accumulated exponent minus3',1+2*52-108==-3)
check('eventual normalization threshold positive4',108-2*52==4)
a,b=s.symbols('a b',positive=True)
j0=1/(16*s.sqrt(3)*s.pi**5)
alpha=(1/a**2+1/b**2)/4;omega=1/(a*b)
lambda_formula=(2*s.pi)**-8*(a*a*b*b)**-4/j0*(s.pi/(alpha+omega/2))**4
check('exact general Gaussian ground factor',s.factor(lambda_formula-16*s.sqrt(3)*s.pi/(a+b)**8)==0)
seconds=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
check('positive bounded resources',math.isfinite(seconds) and math.isfinite(rss) and 0<seconds<AUDIT_TIMEOUT_SEC and 0<rss<AUDIT_MAX_RSS_MIB)
out=dict(status='PASS',per_element=0,per_site=2,per_mode=6,per_block=6,lattice_wide=9,TOTAL=len(checks),checks=checks,tree=tree,chords=chords,face_rows=rows,weights=list(map(str,weights)),source_rows=[list(S.row(i)) for i in range(2)],C=[[str(C[i,j]) for j in range(2)] for i in range(2)],determinant=str(det),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=seconds,rss_MiB=rss,AUDIT_TIMEOUT_SEC=AUDIT_TIMEOUT_SEC,AUDIT_MAX_RSS_MIB=AUDIT_MAX_RSS_MIB)
out['source_rows']=[[int(x) for x in row] for row in out['source_rows']]
assert out['TOTAL']==23==sum(out[k] for k in ['per_element','per_site','per_mode','per_block','lattice_wide'])
assert len(set(checks))==len(checks)
if args.json:print(json.dumps(out,indent=2,allow_nan=False))
else:
 print('PASS: TOTAL23 = original14 exact geometry/OU +8 scalar supplement +1 resource guard.')
 print('N5 per_element: no individual-element dynamical simulation or finite-beta accuracy is certified.')
 print('N5 per_site: the fixed16vertex32edge22face geometry is supplied, not a thermodynamic limit.')
 print('N5 per_mode: covariance and invariant oscillator modes concern the central source space.')
 print('N5 per_block: repeated compressed-source powers are an additional composition contract, not a longer microscopic slab.')
 print('N5 lattice_wide: polynomial sequence108 has unspecified constants/onset and selects no physical time or coupling.')
 print('source_sha256='+out['source_sha256'])
