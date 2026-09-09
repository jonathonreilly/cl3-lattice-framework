from pathlib import Path
import types,sys,json
from fractions import Fraction as F
p=Path('/private/tmp/toe-24h-probes-20260908/native-sparse-pivot-action-adapter-design')
for n in ('interval','adapter'):
 m=types.ModuleType(n);sys.modules[n]=m;exec(compile((p/(n+'.py')).read_bytes(),str(p/(n+'.py')),'exec'),m.__dict__)
a=sys.modules['adapter'];iv=sys.modules['interval'];count=0
class Old:
 oi=0
 def pole(self,*x):return (2,2),(3,3)
 def append_pole(self,*x):return (5,5),(7,7)
 def self_append(self,*x):return (11,11),(0,0)
class New:
 def get(self,k,j):return ((13,13),(17,17)) if j<396 else ((0,0),(19,19)) if j<399 else ((23,23),(0,0))
def req(x):
 global count
 if not x:raise ValueError(count)
 count+=1
e=a.Entries(Old(),New(),0,etaA=F(1,10**31),etaB=F(1,10**20),etac=F(1,10**20),etamu=F(1,10**20))
for x,y in ((399,2),(400,398),(399,401),(396,2)):
 g,j=e.raw(x,y);gr,jr=e.raw(y,x);req(g==gr and jr==(-j[1],-j[0]))
 for ga in (0,1):
  for gb in (0,1):req(e((x,ga),(y,gb))==e((y,gb),(x,ga)))
g,j=e.raw(399,2);d=iv.rational(F(2800,10**31))[1];q=iv.rational(F(177,10**20))[1];req(g==(13-d,13+d) and j==(17-q,17+q))
for z in ((0,False),(0,1.0),(False,0),(402,0)):
 try:a.key(z)
 except ValueError:count+=1
 else:raise ValueError('bad key')
req(a.embed_original_flat(399)==(0,1) and a.embed_original_flat(797)==(398,1))
req(2*5*(64*16*24+64*24*24)==614400)
print(json.dumps({'status':'PASS','predicates':count,'native_index_entry_action_calls':0,'scope':'tiny fake callbacks, transpose/radius/int mapping'}))
