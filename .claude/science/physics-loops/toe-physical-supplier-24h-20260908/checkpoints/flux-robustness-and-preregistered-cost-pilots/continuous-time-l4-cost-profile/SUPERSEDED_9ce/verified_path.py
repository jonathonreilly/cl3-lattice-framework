"""Immutable verified paths; full validation at external boundaries."""
from dataclasses import dataclass
import math
from geometry import FrozenGeometry
@dataclass(frozen=True,slots=True)
class Witness:
 parent:object
 label:int
 length:int

def labels(node):
 out=[]
 while node is not None:out.append(node.label);node=node.parent
 return list(reversed(out))

def event_check(g,initial,events,T,full=False):
 if not math.isfinite(T) or T<=0:raise ValueError('total time')
 x=initial;last=0.
 for t,p in events:
  if type(t) is not float or not math.isfinite(t) or not last<t<T or type(p) is not int or not 0<=p<g.M or not g.legal(x,p):raise ValueError('ordered legal event')
  x^=g.masks[p];last=t
  if full:g.validate(x)
 return x

class Trajectory:
 __slots__=('g','initial','events','T','_witness','_final','_sealed')
 def __delattr__(self,k):raise AttributeError('immutable object deletion')
 def __setattr__(self,k,v):
  if getattr(self,'_sealed',False):raise AttributeError('immutable verified path')
  object.__setattr__(self,k,v)
 def __init__(self,g,initial,events,T,witness):
  if type(g) is not FrozenGeometry:raise ValueError('immutable geometry required')
  if type(initial) is not int:raise ValueError('initial integer')
  x=g.seed;node=None
  for p in witness:
   if type(p) is not int or not 0<=p<g.M or not g.legal(x,p):raise ValueError('seed witness')
   x^=g.masks[p];node=Witness(node,p,1 if node is None else node.length+1)
  if x!=initial:raise ValueError('initial witness')
  g.validate(x);events=tuple((t,p) for t,p in events);final=event_check(g,x,events,T,True)
  self._set(g,initial,events,T,node,final)
 def _set(self,g,initial,events,T,node,final):
  self.g=g;self.initial=initial;self.events=events;self.T=T;self._witness=node;self._final=final;self._sealed=True
 @property
 def witness(self):return labels(self._witness)
 def check(self):return self._final
 def full_check(self):
  x=self.g.seed
  for p in self.witness:
   if not self.g.legal(x,p):raise ValueError('seed witness')
   x^=self.g.masks[p]
  if x!=self.initial:raise ValueError('initial witness')
  self.g.validate(x);end=event_check(self.g,x,self.events,self.T,True)
  if end!=self._final:raise ValueError('cached endpoint')
  return end
 @classmethod
 def from_conditional(cls,old,initial,events,p):
  if type(old) is not cls or type(p) is not int or not 0<=p<old.g.M:raise ValueError('verified predecessor')
  g=old.g;node=old._witness
  if initial!=old.initial:
   if initial!=old.initial^g.masks[p] or not g.legal(old.initial,p):raise ValueError('conditional initial orbit')
   node=Witness(node,p,1 if node is None else node.length+1)
  events=tuple((t,p) for t,p in events)
  if tuple(e for e in events if e[1]!=p)!=tuple(e for e in old.events if e[1]!=p):raise ValueError('retained physical skeleton')
  # All legal plaquette flips preserve ice. Full component provenance follows
  # from the verified predecessor and optional legal initial p flip.
  final=event_check(g,initial,events,old.T)
  out=object.__new__(cls);out._set(g,initial,events,old.T,node,final);return out
