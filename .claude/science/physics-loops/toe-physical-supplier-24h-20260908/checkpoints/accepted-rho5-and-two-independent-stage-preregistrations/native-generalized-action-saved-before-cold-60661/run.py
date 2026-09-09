import time
START=time.monotonic()
import sys,json,hashlib,types,argparse,signal,resource
from pathlib import Path
P=Path(__file__).resolve().parent
sys.set_int_max_str_digits(20000)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
a=argparse.ArgumentParser();a.add_argument('mode',choices=['readiness','saved']);a.add_argument('output');a.add_argument('--authorization');a=a.parse_args()
if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('strict flags')
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('119s inclusive worker')));signal.setitimer(signal.ITIMER_REAL,max(.001,119-(time.monotonic()-START)))
f=json.loads((P/'RUNTIME_FREEZE.json').read_text())
def guard():
 if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
 if sorted(x.name for x in P.iterdir()if x.is_dir()or x.suffix in('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
 for n,h in f['inputs'].items():
  if sha(n)!=h:raise ValueError('pin '+n)
 for m in list(sys.modules.values()):
  q=getattr(m,'__file__',None)
  if q:
   q=str(Path(q).resolve())
   if q not in f['inputs']or sha(q)!=f['inputs'][q]:raise ValueError('loaded origin '+q)
# Pin source before executing imports; guard requires this script to be pinned.
guard()
for name in ('stages','action','replay','stream','worker'):
 path=P/(name+'.py');raw=path.read_bytes()
 if hashlib.sha256(raw).hexdigest()!=f['inputs'][str(path)]:raise ValueError('source bytes')
 m=types.ModuleType(name);m.__file__=str(path);sys.modules[name]=m;exec(compile(raw,str(path),'exec'),m.__dict__)
guard();out=Path(a.output).resolve()
if out.exists()or out==P or P in out.parents:raise ValueError('fresh external output')
if a.mode=='readiness':print(json.dumps({'status':'PASS_SOURCE_ONLY','native_calls':0}));raise SystemExit
b=json.loads((P/'BINDING.json').read_text())
if b['status']!='ROOT_REVIEWED_GENERALIZED_SAVED':raise ValueError('NOT_READY')
if not a.authorization:raise ValueError('authorization required')
auth=json.loads(Path(a.authorization).read_text())
if auth!={'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':sha(P/'BINDING.json'),'output':str(out),'seconds':120,'rss_bytes':384*1048576,'no_retry':True}:raise ValueError('authorization')
with P.with_name(P.name+'.ATTEMPT.json').open('x')as z:json.dump(auth,z)
out.mkdir();(out/'STARTED.json').write_text(json.dumps(auth)+'\n')
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('119s worker')));signal.setitimer(signal.ITIMER_REAL,max(.001,119-(time.monotonic()-START)))
try:
 sys.modules['worker'].compute(b,out);guard();elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if not 0<elapsed<119 or type(rss)is not int or not 0<rss<=384*1048576:raise ValueError('resources')
 (out/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE_GENERALIZED_SAVED','seconds':elapsed,'rss_bytes':rss,'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':sha(P/'BINDING.json'),'result_sha256':sha(out/'RESULT.json')})+'\n')
except BaseException as exc:(out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(exc)})+'\n');raise
