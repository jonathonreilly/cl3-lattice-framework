"""Finite exact controls of the separate analytical proof; standard library only."""
from fractions import Fraction as F
from itertools import product,combinations
MAX_FLIPPED=8
FACE_TERMS=32

def cutoff(a):return max(0,-(-a.numerator//a.denominator)-1)
def exponent(m,m0):return max(0,(m-m0+7)//8)
def check():
 counts={}
 def require(ok,group):
  if not ok:raise ValueError('mathematical predicate: '+group)
  counts[group]=counts.get(group,0)+1
 for L in (4,6):
  verts=list(product(range(L),repeat=3));edges=[(v,a) for v in verts for a in range(3)];ei={e:i for i,e in enumerate(edges)}
  def step(v,a):return tuple((v[k]+(k==a))%L for k in range(3))
  incidence={v:[] for v in verts};ef=[set() for _ in edges];faces=[]
  for i,(v,a) in enumerate(edges):incidence[v].append(i);incidence[step(v,a)].append(i)
  for v in verts:
   for a,b in combinations(range(3),2):
    face={ei[v,a],ei[step(v,a),b],ei[step(v,b),a],ei[v,b]};idx=len(faces);faces.append(face)
    require(len(face)==4,'geometry')
    for e in face:ef[e].add(idx)
  affected=[0]*len(faces)
  for v in verts:
   require(len(incidence[v])==6,'geometry')
   for a,b in combinations(incidence[v],2):
    changed=ef[a]^ef[b];expected=8 if edges[a][1]==edges[b][1] else 6
    require(len(changed)==expected and len(changed)<=MAX_FLIPPED,'flip_support')
    for f in changed:affected[f]+=1
  for n in affected:require(n==FACE_TERMS,'face_incidence')
  # Both relative flux patterns exist: uniform signs vs staggered pi signs.
  for face in faces:
   pi=1
   for e in face:
    v,a=edges[e];pi*=(-1)**sum(v[:a])
   require(pi==-1,'flux_counterexample')
 # Literal commuting-projector selection, all small bitstrings and masks.
 for bits in range(64):
  for C in range(1,64):
   for flip in (1,3,15,42,63):
    if not C&flip:continue
    rhs=(bits&(C&~flip))==(C&~flip)
    lhs=((bits^flip)&C)==C and (bits&C)!=C
    require(not lhs or rhs,'projector_selection')
 for a in (F(0),F(1,10),F(1),F(9,8),F(8),F(81,10),F(32)):
  z=cutoff(a);require(z>=0 and F(z+1)>=a,'integer_cutoff')
  if z>0:require(F(z)<a,'integer_cutoff')
 for m0 in range(33):
  for m in range(m0+1,m0+65):
   for d in range(1,min(MAX_FLIPPED,m)+1):require(exponent(m,m0)<=1+exponent(m-d,m0),'recursion')
   require(exponent(m,m0)==-(-(m-m0)//8),'recursion')
 for N in (64,216,128**3):
  for x in (F(1,10000),F(1,1000),F(1,100)):
   a=300*N*x*x;m=max(1,cutoff(a)+1)
   require(F(m)>=a and 75*N*x*x<=F(m,4),'macro_square')
   require(F(3,4)*m-75*N*x*x>=F(m,2),'young')
  x=F(1,3*N);require(F(3,2)*N*x<=F(1,2),'finite_volume')
 # Mean-density and arbitrary joint event can differ by an extensive exponent.
 p=F(1,100)
 law={0:1-p,63:p}
 for C in range(1,64):require(sum(w for b,w in law.items() if b&C==C)==p,'mixture_boundary')
 return {'status':'PASS','groups':counts,'total_checks':sum(counts.values()),'max_flipped':MAX_FLIPPED,'face_terms':FACE_TERMS,'scope':'Finite lemma controls; no physical ground-state computation.'}
