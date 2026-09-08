"""Packed-state exact-target prototype; no RNG or simulation launcher."""
from itertools import product, combinations
from fractions import Fraction
import math


def guarded_product(t,h):
 f=float(t)
 if not math.isfinite(f) or f<0 or not math.isfinite(h) or h<0:raise ValueError('message entry')
 if t>0 and f==0:raise ValueError('transition underflow')
 z=f*h
 if f>0 and h>0 and z==0:raise ValueError('message product underflow')
 if not math.isfinite(z):raise ValueError('message overflow')
 return z

class Geometry:
 def __init__(self,L):
  if type(L) is not int or L<2 or L%2: raise ValueError('even L>=2')
  self.L=L; self.vertices=list(product(range(L),repeat=3))
  self.links=[(r,a) for r in self.vertices for a in range(3)]
  ix={e:i for i,e in enumerate(self.links)}; self.E=len(self.links)
  def shift(r,a):
   z=list(r);z[a]=(z[a]+1)%L;return tuple(z)
  self.faces=[(ix[r,a],ix[shift(r,a),b],ix[shift(r,b),a],ix[r,b]) for a,b in combinations(range(3),2) for r in self.vertices]
  self.M=len(self.faces); self.masks=[sum(1<<e for e in f) for f in self.faces]
  self.patterns=[((1<<f[0])|(1<<f[2]),(1<<f[1])|(1<<f[3])) for f in self.faces]
  self.by_mask={}
  for p,m in enumerate(self.masks):self.by_mask.setdefault(m,[]).append(p)
  self.affected=[tuple(q for q,g in enumerate(self.faces) if set(f)&set(g)) for f in self.faces]
  self.incident=[tuple(e for e,(s,a) in enumerate(self.links) if s==r or shift(s,a)==r) for r in self.vertices]
  self.seed=sum((r[a]%2)<<e for e,(r,a) in enumerate(self.links))
 def legal(self,x,p): return (x&self.masks[p]) in self.patterns[p]
 def nf(self,x): return sum(self.legal(x,p) for p in range(self.M))
 def validate(self,x):
  if type(x) is not int or x<0 or x>>self.E:raise ValueError('packed binary state')
  if any(sum((x>>e)&1 for e in edges)!=3 for edges in self.incident):raise ValueError('ice constraint')
 def changed_nf(self,x,p,nf):
  y=x^self.masks[p]
  return nf+sum(int(self.legal(y,q))-int(self.legal(x,q)) for q in self.affected[p])
 def weight(self,x,y,nf,V):
  if x==y:return 1-V*nf/self.M
  return sum(self.legal(x,p) for p in self.by_mask.get(x^y,()))/self.M if not isinstance(V,Fraction) else Fraction(sum(self.legal(x,p) for p in self.by_mask.get(x^y,())),self.M)
 def flux(self,x):
  return tuple(sum((-1)**sum(r)*(2*((x>>e)&1)-1) for e,(r,b) in enumerate(self.links) if b==a and r[a]==0) for a in range(3))

class PackedPath:
 def __init__(self,g,states,V,witness=()):
  if isinstance(V,bool) or not math.isfinite(float(V)) or not 0<=V<1:raise ValueError('0<=V<1')
  if len(states)<2:raise ValueError('at least one bond')
  self.g=g;self.V=V;self.states=list(states)
  for x in states:g.validate(x)
  x=g.seed
  for p in witness:
   if type(p) is not int or not 0<=p<g.M or not g.legal(x,p):raise ValueError('seed witness')
   x^=g.masks[p]
  if x!=states[0]:raise ValueError('witness endpoint')
  self.nf=[g.nf(x) for x in states]
  self.check()
 def check(self):
  g=self.g
  if len(self.nf)!=len(self.states) or any(type(k) is not int or k!=g.nf(x) for x,k in zip(self.states,self.nf)):raise ValueError('Nf cache')
  for x in self.states:g.validate(x)
  if any(g.weight(x,y,k,self.V)<=0 for x,y,k in zip(self.states,self.states[1:],self.nf)):raise ValueError('path transition')
 def fiber(self,p):
  if type(p) is not int or not 0<=p<self.g.M:raise ValueError('face')
  g=self.g;orbits=[];counts=[]
  for x,k in zip(self.states,self.nf):
   pair=sorted((x,x^g.masks[p])) if g.legal(x,p) else [x]
   orbits.append(pair);counts.append([k if y==x else g.changed_nf(x,p,k) for y in pair])
  matrices=[[[g.weight(x,y,counts[i][s],self.V) for y in orbits[i+1]] for s,x in enumerate(orbits[i])] for i in range(len(orbits)-1)]
  return orbits,counts,matrices
 def draw(self,p,uniforms):
  if len(uniforms)!=len(self.states) or any(not math.isfinite(u) or not 0<=u<1 for u in uniforms):raise ValueError('variates')
  O,N,T=self.fiber(p);h=[[1.]*len(z) for z in O]
  for i in range(len(T)-1,-1,-1):
   h[i]=[sum(guarded_product(t,h[i+1][j]) for j,t in enumerate(row)) for row in T[i]]
   scale=max(h[i])
   if not math.isfinite(scale) or scale<=0:raise ValueError('message normalizer')
   scaled=[z/scale for z in h[i]]
   if any(z>0 and q==0 for z,q in zip(h[i],scaled)):raise ValueError('message scaling underflow')
   h[i]=scaled
  selected=[]
  for i,u in enumerate(uniforms):
   weights=h[i] if i==0 else [guarded_product(T[i-1][selected[-1]][j],h[i][j]) for j in range(len(O[i]))]
   total=sum(weights)
   if not math.isfinite(total) or total<=0:raise ValueError('conditional normalizer')
   target=u*total;cum=0.;pick=None
   for j,w in enumerate(weights):
    cum+=w
    if target<cum:pick=j;break
   if pick is None:raise ValueError('CDF rounding')
   selected.append(pick)
  self.states=[O[i][j] for i,j in enumerate(selected)];self.nf=[N[i][j] for i,j in enumerate(selected)]
  return selected
