import adapter,interval as iv
from fractions import Fraction as F
import json
n=0
def req(x):
 global n
 if not x:raise ValueError(n)
 n+=1
class Old:
 oi=0
 def pole(self,*a):self.call=a;return(10,12),(3,5)
 def append_pole(self,*a):self.call=a;return(20,22),(7,9)
 def self_append(self,*a):self.call=a;return(30,32),iv.ZERO
class New:
 def get(self,k,j):
  self.call=(k,j)
  return ((0,0),(11,13)) if 396<=j<399 else ((40,42),((0,0) if j>=399 else(17,19)))
o=Old();q=New();e=adapter.Entries(o,q,0,etaA=F(0),etaB=F(0),etac=F(0),etamu=F(0))
for a,b in [(0,3),(7,11),(395,0)]:
 e.raw(a,b);na,ta=divmod(a,6);nb,tb=divmod(b,6);req(o.call==(2*na+ta//3,2*nb+tb//3,ta%3,tb%3))
req(e.raw(400,9)==((40,42),(17,19)));req(q.call==((0,400,9),9));req(e.raw(9,400)==((40,42),(-19,-17)))
for ga,gb,z in [(0,0,(40,42)),(1,1,(40,42)),(0,1,(17,19)),(1,0,(-19,-17))]:req(e((400,ga),(9,gb))==z)
req(e.raw(399,397)==((0,0),(11,13)));req(e.raw(397,399)==((0,0),(-13,-11)))
req(adapter.embed_original_flat(399)==(0,1));req(adapter.embed_original_flat(797)==(398,1))
for key in ((0,True),(True,0),(402,0)):
 try:adapter.key(key)
 except ValueError:n+=1
 else:raise ValueError('bad key')
s,a=adapter.exact_midpoint_family(['1/3']*66,['2/7']*66)
req(F(s[0][0],iv.S)<=F(1,3)<=F(s[0][1],iv.S));req(F(a[0][0],iv.S)<=F(2,7)<=F(a[0][1],iv.S))
print(json.dumps({'status':'PASS_TINY_SYNTHETIC_ADAPTER','predicates':n,'native_index_calls':0,'native_entries':0,'core_action_calls':0}))
