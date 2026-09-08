"""Period-four integer Laurent matrices. Import performs no spectral calculation."""
from itertools import product,permutations
V=list(product(range(4),repeat=3));INDEX={v:i for i,v in enumerate(V)}
C=list(product(range(2),repeat=3));EDGES=[(v,a) for v in C for a in range(3) if v[a]==0]
TREE=[];known={(0,0,0)}
while len(known)<8:
 for v,a in EDGES:
  w=list(v);w[a]=1;w=tuple(w)
  if (v in known)!=(w in known):TREE.append((v,a));known.update((v,w))
FREE=[e for e in EDGES if e not in TREE]
def base(bits):return {e:(-1 if e in FREE and bits>>FREE.index(e)&1 else 1) for e in EDGES}
def signature(bits):
 b=base(bits);out=[]
 for normal in range(3):
  a,c=[x for x in range(3) if x!=normal]
  for side in range(2):
   v=[0,0,0];v[normal]=side;va=v.copy();va[a]=1;vc=v.copy();vc[c]=1
   out.append(b[tuple(v),a]*b[tuple(va),c]*b[tuple(vc),a]*b[tuple(v),c])
 return tuple(out)
def sign(bits,r,a):
 b=[x//2 for x in r]
 if r[a]%2==0:
  v=[(0,1,1,0)[x%4] for x in r];v[a]=0
  return (-1)**sum(b)*base(bits)[tuple(v),a]
 return (-1)**sum(b[a+1:])
def terms(bits):
 out=[]
 for r in V:
  for a in range(3):
   w=list(r);w[a]=(w[a]+1)%4;d=[0,0,0];d[a]=int(r[a]==3)
   i,j=INDEX[r],INDEX[tuple(w)];s=sign(bits,r,a)
   out.append((i,j,tuple(d),s));out.append((j,i,tuple(-x for x in d),s))
 return out
def orbit(q):
 return {tuple(q[2*p[a]+(s^f[a])] for a in range(3) for s in range(2)) for p in permutations(range(3)) for f in product(range(2),repeat=3)}
def inputs():
 sig={b:signature(b) for b in range(32)};rows=[]
 for b,q in sig.items():
  rep=min(c for c in range(32) if sig[c] in orbit(q))
  rows.append({'id':b,'cube_signs':[base(b)[e] for e in EDGES],'face_signs':q,'defects':q.count(1),'symmetry_representative':rep,'terms':terms(b)})
 return {'cell_extents':[4,4,4],'site_order':V,'cube_edge_order':EDGES,'free_edge_order':FREE,'hopping_magnitude':1,'rows':rows}
