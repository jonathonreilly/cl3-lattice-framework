"""Inductively certified construction; reference full validation is retained."""
from array import array
import math
from guarded import Geometry,PackedPath

def valid_parameters(L,n,V,rk_sweeps):
 if type(L) is not int or L<2 or L%2 or type(n) is not int or n<1:raise ValueError('dimensions')
 if isinstance(V,bool) or not math.isfinite(float(V)) or not 0<=V<1:raise ValueError('V<1')
 if type(rk_sweeps) is not int or rk_sweeps<0:raise ValueError('RK sweeps')

def initialize(g,n,V,rng,rk_sweeps):
 valid_parameters(g.L,n,V,rk_sweeps)
 x=g.seed;witness=array('H')
 if g.M>65535:raise ValueError('witness uint16 capacity')
 for _ in range(rk_sweeps*g.M):
  p=rng.randrange(g.M)
  if g.legal(x,p):x^=g.masks[p];witness.append(p)
 nf=g.nf(x);states=[x];counts=[nf];nonself=0
 for _ in range(n):
  u=rng.random()*(g.M+(1-float(V))*nf);p=int(u) if u<g.M else -1
  if p>=0 and g.legal(x,p):nf=g.changed_nf(x,p,nf);x^=g.masks[p];nonself+=1
  states.append(x);counts.append(nf)
 obj=PackedPath.__new__(PackedPath);obj.g=g;obj.V=V;obj.states=states;obj.nf=counts;obj.witness=witness
 return obj,dict(rk_proposals=rk_sweeps*g.M,accepted_RK=len(witness),Q_steps=n,nonself_Q=nonself,law='RK then product-Q, nonstationary initializer')

def draw(obj,p,uniforms):
 before=obj.states[0];obj.draw(p,uniforms)
 if obj.states[0]!=before:obj.witness.append(p)


def reconstruct(g,states,counts,V,witness,total_nf):
 valid_parameters(g.L,len(states)-1,V,0)
 if len(counts)!=len(states) or type(total_nf) is not int:raise ValueError('counts shape')
 x=g.seed
 for p in witness:
  if type(p) is not int or not 0<=p<g.M or not g.legal(x,p):raise ValueError('witness')
  x^=g.masks[p]
 if type(states[0]) is not int or states[0]!=x:raise ValueError('witness endpoint')
 nf=g.nf(x);reconstructed=[nf]
 for y in states[1:]:
  if type(y) is not int or y<0 or y>>g.E:raise ValueError('packed state')
  if y!=x:
   choices=[p for p in g.by_mask.get(x^y,()) if g.legal(x,p)]
   if not choices:raise ValueError('path bond')
   nf=g.changed_nf(x,choices[0],nf)
  reconstructed.append(nf);x=y
 if any(type(k) is not int or k!=r for k,r in zip(counts,reconstructed)) or sum(reconstructed)!=total_nf:raise ValueError('all-time Nf')
 obj=PackedPath.__new__(PackedPath);obj.g=g;obj.V=V;obj.states=list(states);obj.nf=reconstructed;obj.witness=array('H',witness)
 return obj
