from pathlib import Path
from fractions import Fraction as F
import types,sys,json,hashlib,time
B=Path('/private/tmp/toe-24h-probes-20260908');P=B/'native-highprecision-b-contraction-design';R=B/'native-highprecision-b-contraction-root-review';O=B/'native-highprecision-b-root-independent-review/SYNTHETIC_SHARD'
# Actual compute source, synthetic scalar callbacks ONLY. No actual integrands, moments or oracle.
v=types.ModuleType('interval');v.const=lambda x:(F(x),F(x));v.add=lambda a,b:(a[0]+b[0],a[1]+b[1]);v.mul=lambda a,b:(min(x*y for x in a for y in b),max(x*y for x in a for y in b));v.neg=lambda a:(-a[1],-a[0]);sys.modules['interval']=v
c=types.ModuleType('core');c.integrands=lambda *args:((F(0),F(0)),(F(0),F(0)));c.high_tail=lambda *args:((F(0),F(0)),(F(0),F(0)));c.moment=lambda n:F(0);sys.modules['core']=c
ib=types.ModuleType('interval_base');ib.pi_bounds=lambda:(F(3),F(4));sys.modules['interval_base']=ib
m=types.ModuleType('compute');m.__file__=str(P/'compute.py');exec(compile((P/'compute.py').read_bytes(),m.__file__,'exec'),m.__dict__)
poles=[{'s_midpoint':str(i+1)} for i in range(66)];a66=[{'oracle':{'s':str(i+1),'A':['1','1'],'Aprime':['-1','-1']}} for i in range(66)];cat=[{'id':26*(j+64)+i,'panel':j,'t_interval':(F(1),F(1)),'A_interval':(F(1),F(1)),'weight_interval':(F(1),F(1))} for j in range(-64,3) for i in range(26)]
t=time.monotonic();m.run(O,poles,a66,cat,list(range(6)));elapsed=time.monotonic()-t
s=types.ModuleType('schema');exec(compile((R/'schema.py').read_bytes(),str(R/'schema.py'),'exec'),s.__dict__)
w={'status':'COMPLETE','shard':0,'freeze_sha256':'synthetic','binding_sha256':'synthetic','result_sha256':s.sha(O/'RESULT.json'),'seconds':elapsed+1,'rss_bytes':1};(O/'WORKER_COMPLETE.json').write_text(json.dumps(w));s.shard(O,0,poles,'synthetic','synthetic',elapsed+2)
# Actual file adverse; retain intentionally corrupt fixture separately.
p=O/'PANELS/00.json';old=p.read_bytes();x=json.loads(old);x['cumulative']['0'][0]=['1','1'];p.write_text(json.dumps(x));failed=False
try:s.shard(O,0,poles,'synthetic','synthetic',elapsed+2)
except ValueError:failed=True
if not failed:raise ValueError('corrupt cumulative accepted')
p.write_bytes(old)
print(json.dumps({'status':'PASS_ACTUAL_COMPUTE_SCHEMA_SYNTHETIC','actual_compute_sha256':hashlib.sha256((P/'compute.py').read_bytes()).hexdigest(),'actual_schema_sha256':hashlib.sha256((R/'schema.py').read_bytes()).hexdigest(),'panels':67,'poles':6,'synthetic_callback_pairs':10452,'physical_calls':0,'adverse_rejected':True}))
