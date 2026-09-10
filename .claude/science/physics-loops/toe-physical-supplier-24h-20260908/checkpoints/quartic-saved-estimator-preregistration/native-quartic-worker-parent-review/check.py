from pathlib import Path
from fractions import Fraction as F
import sys,types,json
P=Path('/private/tmp/toe-24h-probes-20260908/native-quartic-spectral-estimator-design')
for n in ['interval','core']:
 m=types.ModuleType(n);m.__file__=str(P/(n+'.py'));sys.modules[n]=m;exec(compile(Path(m.__file__).read_bytes(),m.__file__,'exec'),m.__dict__)
C=sys.modules['core'];I=sys.modules['interval'];ev=[];row=dict(moments=[(F(2)**n,F(2)**n)for n in range(11)],p=[F(0)]*3,r2=(F(1),F(1)),t2=(F(0),F(0)),old_first_squared_upper=F(16));z=C.evaluate({'P':row,'O':row},(F(0),F(0)),(F(-1000),F(1000)),(F(0),F(0)),(F(0),F(0)),lambda s,d:ev.append((s,d)));n=0
assert len(ev)==45 and z['status']=='INDETERMINATE_SIGN';n+=1
E=z['E_upper'];G=z['F_upper'];assert(E-F(1,2**120))**2<F(15,4)<=E**2;n+=1;assert(G-F(1,2**120))**2<480<=G**2;n+=1
assert z['new_alpha']==(-z['error_upper']/8,z['error_upper']/8)and z['intersection']==z['new_alpha'];n+=1
for stage,x in ev:
 if stage=='quartic_candidate_raw':
  value=sum(a*F(2)**j for j,a in enumerate(x['coefficients']));assert x['interval']==(value,value)and value>=F(1,4);n+=1
 if stage=='class_residual_bound':assert x['first_squared_upper']==F(1,4);n+=1
try:I.nonnegative((F(-2),F(-1)))
except ValueError:n+=1
else:raise AssertionError('negative upper clipped')
print(json.dumps({'status':'PASS','checks':n,'fixture':'fabricated spectral atomD=2,p=q=0,15abstractchannels','native_loads':0}))
