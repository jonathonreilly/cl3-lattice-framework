from pathlib import Path
import sys,types,json,time,hashlib
from fractions import Fraction as F
b=Path('/private/tmp/toe-24h-probes-20260908');s=b/'native-cminus-catalog-design';r=b/'native-cminus-catalog-root-review';o=b/'native-cminus-catalog-cold-review/MONITOR_TOY';start=time.monotonic()
for name,path in [('interval',s/'interval.py'),('interval_base',s/'interval_base.py'),('compute',s/'compute.py'),('schema',r/'schema.py')]:
 m=types.ModuleType(name);m.__file__=str(path);sys.modules[name]=m;exec(compile(path.read_bytes(),str(path),'exec'),m.__dict__)
# Stub the ONLY moment callback: no native moment evaluation, loader or scalar data.
sys.modules['compute'].moment=lambda _:F(0)
sys.modules['compute'].pi_bounds=lambda:(F(3),F(4))
catalog=[{'panel':j,'A_interval':(F(0),F(0)),'weight_interval':(F(1),F(1))} for j in range(-64,3) for k in range(26)]
sys.modules['compute'].run(o,catalog)
freeze=hashlib.sha256((s/'RUNTIME_FREEZE.json').read_bytes()).hexdigest();h=hashlib.sha256((o/'RESULT.json').read_bytes()).hexdigest()
(o/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE_CATALOG_INTEGRAL','runtime_sha256':freeze,'result_sha256':h,'seconds':time.monotonic()-start,'rss_bytes':1048576}))
v=sys.modules['schema'].check(o,freeze,time.monotonic()-start)
p=json.loads((o/'PARTIAL.json').read_text());before=(o/'PARTIAL.json').read_bytes();p['seconds']=float('nan');(o/'PARTIAL.json').write_text(json.dumps(p))
try:sys.modules['schema'].check(o,freeze,time.monotonic()-start)
except ValueError:bad=True
else:bad=False
(o/'PARTIAL.json').write_bytes(before)
if not bad:raise ValueError('NaN partial accepted')
print(json.dumps({'status':'PASS_ACTUAL_COMPUTE_STUB_SCHEMA','schema':v,'nan_partial_rejected':bad,'native_calls':0,'moment_calls':0,'loader_calls':0,'synthetic_nodes':1742}))
