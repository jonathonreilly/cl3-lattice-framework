from types import MappingProxyType
from geometry_reference import Geometry
class FrozenGeometry(Geometry):
 def __getattribute__(self,k):
  value=object.__getattribute__(self,k)
  return MappingProxyType(value) if k=='__dict__' else value
 def __delattr__(self,k):raise AttributeError('immutable object deletion')
 def __setattr__(self,k,v):
  if getattr(self,'_sealed',False):raise AttributeError('immutable geometry')
  object.__setattr__(self,k,v)
 def __init__(self,L):
  super().__init__(L)
  for name in ('vertices','links','faces','patterns','affected','incident'):
   setattr(self,name,tuple(tuple(x) for x in getattr(self,name)))
  self.masks=tuple(self.masks);self.by_mask=MappingProxyType({k:tuple(v) for k,v in self.by_mask.items()});self._sealed=True
