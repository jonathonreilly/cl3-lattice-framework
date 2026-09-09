from pathlib import Path
import types,sys,json
from fractions import Fraction as F
p=Path('/private/tmp/toe-24h-probes-20260908/native-sparse-pivot-action-design')
for n in ('interval','core'):
 m=types.ModuleType(n);sys.modules[n]=m;exec(compile((p/(n+'.py')).read_bytes(),str(p/(n+'.py')),'exec'),m.__dict__)
c=sys.modules['core'];iv=sys.modules['interval'];one=iv.ONE;zero=iv.ZERO;count=0
def req(x):
 global count
 if not x:raise ValueError(count)
 count+=1
# Dense independent coordinate-space calculation on ten formal orthonormal axes.
keys=[(r,g) for r in (396,397,399,400,401) for g in (0,1)];pos={k:i for i,k in enumerate(keys)}
cols=[{(396,0):one},{(396,1):one}];out=c.action(cols,tuple((396,g) for g in (0,1)),lambda a,b:one if a==b else zero,[one]*66,[one]*66,lambda e:None)
for result,q in zip(out['results'],(399,400)):
 images=[]
 for g in (0,1):
  v=[0]*10;v[pos[(401,g)]]=1
  # Delta K is rank-two on untransformed x0,q only, not its Gamma copy.
  if g==0:v[pos[(q,0)]]=-8
  images.append(v)
 expected=[[sum(a*b for a,b in zip(u,v)) for v in images] for u in images]
 for i in range(2):
  for j in range(2):req(result['L'][i][j]==iv.rational(expected[i][j]));req(result['T'][i][j]==zero)
 req(result['delta_squared_upper_numerator']==65*iv.S)
for i in range(12):
 s=c.seed(i);req(c.gamma(c.gamma(s))=={k:iv.neg(v) for k,v in s.items()})
try:c.free({(399,0):one},[one]*66,[one]*66)
except ValueError:req(True)
else:req(False)
try:c.native()
except ValueError:req(True)
else:req(False)
print(json.dumps({'status':'PASS','predicates':count,'native_history_or_gram':False,'scope':'tiny formal orthonormal coordinate model, independently dense rank-two action'}))
