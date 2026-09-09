import time
START=time.monotonic()
import sys,json,hashlib,types,argparse,signal,resource
from pathlib import Path
P=Path(__file__).resolve().parent

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['source-readiness','check']);ap.add_argument('output');a=ap.parse_args()
if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('-I-B-S')
f=json.loads((P/'RUNTIME_FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(x.name for x in P.iterdir() if x.is_dir() or x.suffix in('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for name,h in f['inputs'].items():
 if sha(name)!=h:raise ValueError('pin '+name)
def guard():
 for m in list(sys.modules.values()):
  path=getattr(m,'__file__',None)
  if path:
   path=str(Path(path).resolve())
   if path not in f['inputs'] or sha(path)!=f['inputs'][path]:raise ValueError('loaded origin '+path)
p=P/'check.py';data=p.read_bytes()
if hashlib.sha256(data).hexdigest()!=f['inputs'][str(p)]:raise ValueError('verified checker bytes')
m=types.ModuleType('postchecker');m.__file__=str(p);sys.modules['postchecker']=m;exec(compile(data,str(p),'exec'),m.__dict__);guard();out=Path(a.output).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
if a.mode=='source-readiness':print(json.dumps({'status':'PASS_SOURCE_READINESS','saved_replay_executed':False,'physical_calls':0}));raise SystemExit
out.mkdir();(out/'STARTED.json').write_text(json.dumps({'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'post_binding_sha256':sha(P/'POST_BINDING.json'),'seconds':30,'rss_bytes':384*1048576,'no_retry':True})+'\n')
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('25s postcheck deadline')));signal.setitimer(signal.ITIMER_REAL,max(.001,25-(time.monotonic()-START)))
try:
 sys.argv=[str(p),str(P/'POST_BINDING.json'),str(out/'RESULT.json')];m.main();guard();seconds=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if seconds>30 or rss>384*1048576:raise ValueError('postcheck resources')
 (out/'COMPLETE.json').write_text(json.dumps({'status':'COMPLETE_SAVED_ONLY','seconds':seconds,'rss_bytes':rss,'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'result_sha256':sha(out/'RESULT.json'),'external_receipt_pending':True},indent=2)+'\n')
except BaseException as e:
 (out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-START})+'\n');raise
