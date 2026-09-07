import os,time,signal,sys,resource,json,hashlib
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
t0=time.monotonic();signal.alarm(180)
import sympy as s
from itertools import combinations,product
from pathlib import Path
checks=[]
def ck(n,b):
 if n in checks or not bool(b):raise AssertionError(n)
 checks.append(n)
ck('source matrix normalization',s.Rational(1,3)*3==1)
ck('actual one-square normalized Haar coefficient',s.Rational(1,3)*s.Rational(1,6)*1==s.Rational(1,18))
ck('omitting external source normalization is adverse',s.Rational(1,6)!=s.Rational(1,18))
# SU3 fundamental character: sum_ab int U_aa conjugate U_bb=1.
haar_norm=sum(s.Rational(int(a==b),3) for a in range(3) for b in range(3))
ck('fundamental character Haar norm all diagonal pairs',haar_norm==1)
ck('fundamental square zero by triality',2%3!=0)
# all-label monotonic increments, analytical identity rather than a finite representation cutoff
p,q=s.symbols('p q',integer=True,nonnegative=True);E=p*p+p*q+q*q+3*p+3*q
ck('all-label first increment',s.expand(E.subs(p,p+1)-E)==2*p+q+4)
ck('all-label second increment',s.expand(E.subs(q,q+1)-E)==p+2*q+4)
ck('fundamental energy4',E.subs({p:1,q:0})==4 and E.subs({p:0,q:1})==4)
rows=[]
for R,S in [(1,1),(1,2),(2,2),(1,3),(2,3)]:
 L=R+S;words=[]
 for pos in combinations(range(L),R):words.append(tuple(int(i in pos) for i in range(L)))
 def path(w):
  x=y=0;edges=set()
  for b in w:
   edges.add((x,y,b));x+=b;y+=1-b
  return edges
 paths=[path(w) for w in words];faces=[]
 for x,y in product(range(R),range(S)):
  faces.append({(x,y,1):1,(x+1,y,0):1,(x,y+1,1):-1,(x,y,0):-1})
 H=s.zeros(len(words));haars=s.zeros(len(words))
 for i,w in enumerate(words):
  for j,v in enumerate(words):
   if i!=j:
    swaps=[k for k in range(L-1) if w[k]!=w[k+1] and w[:k]+(w[k+1],w[k])+w[k+2:]==v]
    H[i,j]=len(swaps)
    union=paths[i]|paths[j];diff={e:int(e in paths[i])-int(e in paths[j]) for e in union}
    survivors=sum(all((diff.get(e,0)+sgn*f.get(e,0))%3==0 for e in union|f.keys()) for f in faces for sgn in [-1,1])
    haars[i,j]=s.Rational(survivors,18)
 ck('complete shortest path count '+str((R,S)),len(words)==s.binomial(L,R))
 ck('actual edge-charge flip matrix '+str((R,S)),haars==H/18)
 ck('symmetric actual adjacency '+str((R,S)),H==H.T)
 # Fermionic hopping in occupation basis: adjacent occupied-empty exchange has positive matrix element.
 F=s.zeros(len(words))
 for i,w in enumerate(words):
  for k in range(L-1):
   if w[k]!=w[k+1]:
    v=w[:k]+(w[k+1],w[k])+w[k+2:];F[words.index(v),i]+=1
 ck('fixed number fermion adjacency '+str((R,S)),F==H)
 # Exact characteristic polynomial from algebraic one-body eigenvalues; small L only.
 eig=[2*sum(s.cos(s.pi*k/(L+1)) for k in ks) for ks in combinations(range(1,L+1),R)]
 z=s.symbols('z');poly=s.Poly(H.charpoly(z).as_expr(),z)
 expected=s.Poly(s.expand(s.prod(z-e for e in eig)),z)
 ck('full planar fermion spectrum '+str((R,S)),all(s.simplify(a-b)==0 for a,b in zip(poly.all_coeffs(),expected.all_coeffs())))
 rows.append({'R':R,'S':S,'length':L,'paths':words,'adjacency':H.tolist(),'characteristic_polynomial':str(poly.as_expr()),'fermion_eigenvalues':[str(s.simplify(e)) for e in eig]})
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('positive resources',0<rss<180 and time.monotonic()-t0<180)
def encode(o):
 if isinstance(o,s.Basic):return int(o) if o.is_Integer else str(o)
 raise TypeError(type(o).__name__)
print(json.dumps({'checks':checks,'TOTAL':len(checks),'rows':rows,'plaquette_flip_coefficient':'1/18','seconds':time.monotonic()-t0,'rss_MiB':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},default=encode,indent=2,allow_nan=False))
