from pathlib import Path
import json,hashlib,types,tempfile
base=Path('/private/tmp/toe-24h-probes-20260908');root=base/'native-common-cache-saved-root-review';m=types.ModuleType('schema');exec(compile((root/'schema.py').read_bytes(),str(root/'schema.py'),'exec'),m.__dict__)
n=0
def fixture(kind,key=None,value=None):
 global n
 with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as name:
  p=Path(name);v={'status':'PASS_SAVED_SCHEMA_AND_FIXED_SAMPLES','builder_calls':0,'oracle_calls':0,'samples':128};w={'status':'COMPLETE_SAVED_ONLY','runtime_sha256':'toy','seconds':.1,'rss_bytes':100}
  if key:(v if kind=='v' else w)[key]=value
  (p/'RESULT.json').write_text(json.dumps(v));w['result_sha256']=hashlib.sha256((p/'RESULT.json').read_bytes()).hexdigest();(p/'WORKER_COMPLETE.json').write_text(json.dumps(w))
  try:m.check(p,'toy',1);ok=True
  except (ValueError,TypeError):ok=False
  n+=1;return ok
if not fixture('v'):raise ValueError('valid')
for k,x in [('status','bad'),('samples',127),('samples',True),('samples',128.0),('builder_calls',1),('oracle_calls',1)]:
 if fixture('v',k,x):raise ValueError(k)
for k,x in [('seconds',True),('seconds',float('nan')),('seconds',31),('rss_bytes',True),('rss_bytes',385*1048576),('runtime_sha256','bad')]:
 if fixture('w',k,x):raise ValueError(k)
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();rf=json.loads((root/'ROOT_FREEZE.json').read_text())
for f,v in rf['files'].items():
 if h(root/f)!=v:raise ValueError('root pin')
p=base/'native-common-cache-saved-postcheck';wf=json.loads((p/'RUNTIME_FREEZE.json').read_text())
if h(p/'RUNTIME_FREEZE.json')!=rf['worker_freeze']:raise ValueError('workerfreeze')
for f,v in wf['inputs'].items():
 if h(f)!=v:raise ValueError('runtimepin '+f)
print(json.dumps({'status':'PASS','synthetic_cases':n,'runtime_pins':len(wf['inputs']),'native_calls':0,'saved_cache_replays':0},indent=2))
