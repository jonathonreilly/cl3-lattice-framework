import time
START=time.monotonic()
import sys,json,hashlib,types,argparse,signal,resource
from pathlib import Path
P=Path(__file__).resolve().parent
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','verify']);ap.add_argument('output');ap.add_argument('--authorization');a=ap.parse_args()
if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('-I-B-S')
f=json.loads((P/'RUNTIME_FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(x.name for x in P.iterdir() if x.is_dir() or x.suffix in('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for x,h in f['inputs'].items():
 if sha(x)!=h:raise ValueError('source/runtime pin '+x)
p=P/'check.py';raw=p.read_bytes()
if hashlib.sha256(raw).hexdigest()!=f['inputs'][str(p)]:raise ValueError('verified byte source')
m=types.ModuleType('saved_checker');m.__file__=str(p);sys.modules[m.__name__]=m;exec(compile(raw,str(p),'exec'),m.__dict__)
def guard():
 for mod in list(sys.modules.values()):
  x=getattr(mod,'__file__',None)
  if x:
   x=str(Path(x).resolve())
   if x not in f['inputs'] or sha(x)!=f['inputs'][x]:raise ValueError('loaded origin '+x)
guard()
if a.mode=='readiness':print(json.dumps({'status':'PASS_SOURCE_READINESS_ONLY','saved_verification_calls':0}));raise SystemExit
out=Path(a.output).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
binding=json.loads((P/'BINDING.json').read_text())
if binding['status']!='ACCEPTED_RESULT_BOUND' or not a.authorization:raise ValueError('accepted binding and authorization required')
auth=json.loads(Path(a.authorization).read_text())
if auth!={'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':sha(P/'BINDING.json'),'output':str(out),'seconds':30,'rss_bytes':384*1048576,'no_retry':True}:raise ValueError('authorization')
with P.with_name(P.name+'.ATTEMPT.json').open('x') as z:json.dump(auth,z)
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('29s saved verification')));signal.setitimer(signal.ITIMER_REAL,max(.001,29-(time.monotonic()-START)))
try:
 sys.argv=[str(P/'check.py'),'verify','--output',str(out)];m.main();guard();elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if elapsed>=29 or rss>384*1048576:raise ValueError('resources')
 (out/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE_SAVED_ONLY','seconds':elapsed,'rss_bytes':rss,'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':sha(P/'BINDING.json'),'result_sha256':sha(out/'RESULT.json')})+'\n')
except BaseException as e:
 out.mkdir(exist_ok=True);(out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-START})+'\n');raise
