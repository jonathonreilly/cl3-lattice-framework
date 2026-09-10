from pathlib import Path
import types,hashlib,json
from fractions import Fraction as F
p=Path('/private/tmp/toe-24h-probes-20260908/native-degree10-posterior-certificate-design/posterior.py');raw=p.read_bytes();m=types.ModuleType('testposterior');exec(compile(raw,str(p),'exec'),m.__dict__)
n=0
for t in [F(0),F(1,3),F(2),F(17,19)]:
 u=m.upper_root(t);assert u*u>=t and (u-F(1,2**256))**2<t if u else t==0;n+=1
r=m.evaluate({'P':['8','8'],'O':['8','8']},{'P':'0','O':'0'},{'E':['0','0'],'F':['0','0'],'nominal':['1','1']});assert r['error_upper']==0 and r['alpha_interval']==(F(1,8),F(1,8));n+=1
for bad in [True,'01','1/0','2/2']:
 try:m.rat(bad)
 except (ValueError,ZeroDivisionError):n+=1
 else:raise AssertionError('bad rational')
for bad in [['2','1'],[False,'1']]:
 try:m.box(bad)
 except ValueError:n+=1
 else:raise AssertionError('bad box')
try:m.evaluate({'P':['-1','-1'],'O':['8','8']},{'P':'0','O':'0'},{'E':['0','0'],'F':['0','0'],'nominal':['1','1']})
except ValueError:n+=1
else:raise AssertionError('negative norm')
print(json.dumps({'checks':n,'status':'PASS_SYNTHETIC_ONLY','source':hashlib.sha256(raw).hexdigest(),'accepted_inputs_read':0}))
