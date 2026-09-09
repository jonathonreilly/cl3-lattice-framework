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
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['source-readiness','fixture']);ap.add_argument('output');ap.add_argument('--authorization');a=ap.parse_args()
if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('-I-B-S')
f=json.loads((P/'RUNTIME_FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(x.name for x in P.iterdir() if x.is_dir() or x.suffix in('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for name,h in f['inputs'].items():
 if sha(name)!=h:raise ValueError('pin '+name)
for name in ('interval','core','assemble','fixture'):
 p=P/(name+'.py');source=p.read_bytes()
 if hashlib.sha256(source).hexdigest()!=f['inputs'][str(p)]:raise ValueError('source bytes')
 m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(source,str(p),'exec'),m.__dict__)
def guard():
 for m in list(sys.modules.values()):
  path=getattr(m,'__file__',None)
  if path:
   path=str(Path(path).resolve())
   if path not in f['inputs'] or sha(path)!=f['inputs'][path]:raise ValueError('loaded origin '+path)
guard();out=Path(a.output).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
if a.mode=='source-readiness':
 print(json.dumps({'status':'PASS_SOURCE_READINESS_ONLY','fixture_executed':False,'native_calls':0}));raise SystemExit
if not a.authorization:raise ValueError('source-bound root authorization required')
auth=json.loads(Path(a.authorization).read_text())
if auth!={'mode':'SYNTHETIC_COST_ONLY','runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'fixture_sha256':sha(P/'FIXTURE.json'),'output':str(out),'external_seconds':180,'tree_rss_bytes':384*1048576,'no_retry':True}:raise ValueError('authorization binding')
# Once marker is deliberately outside the source package; an existing output cannot retry.
out.mkdir();(out/'STARTED.json').write_text(json.dumps(auth)+'\n')
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('179s secondary worker deadline')));signal.setitimer(signal.ITIMER_REAL,max(.001,179-(time.monotonic()-START)))
try:
 sys.modules['fixture'].run(out);guard()
 elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if elapsed>180 or rss>384*1048576:raise ValueError('worker resources')
 (out/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE_SYNTHETIC_ONLY','seconds':elapsed,'rss_bytes':rss,'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'result_sha256':sha(out/'RESULT.json')},indent=2)+'\n')
except BaseException as e:
 (out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-START,'synthetic_only':True})+'\n');raise
