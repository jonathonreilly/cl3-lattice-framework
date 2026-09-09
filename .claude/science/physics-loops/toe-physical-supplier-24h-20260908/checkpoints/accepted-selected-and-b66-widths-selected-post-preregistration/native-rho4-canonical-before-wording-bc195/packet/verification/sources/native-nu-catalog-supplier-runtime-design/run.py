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
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','integral']);ap.add_argument('output');ap.add_argument('--authorization');a=ap.parse_args()
if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('strict flags')
f=json.loads((P/'RUNTIME_FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(x.name for x in P.iterdir() if x.is_dir() or x.suffix in('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for n,h in f['inputs'].items():
 if sha(n)!=h:raise ValueError('pin '+n)
for name in ('interval','interval_base','loader','compute'):
 p=P/(name+'.py');data=p.read_bytes()
 if hashlib.sha256(data).hexdigest()!=f['inputs'][str(p)]:raise ValueError('source bytes')
 m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(data,str(p),'exec'),m.__dict__)
def guard():
 for m in list(sys.modules.values()):
  x=getattr(m,'__file__',None)
  if x:
   x=str(Path(x).resolve())
   if x not in f['inputs'] or sha(x)!=f['inputs'][x]:raise ValueError('origin '+x)
guard();b=json.loads((P/'BINDING.json').read_text());out=Path(a.output).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
if a.mode=='readiness':
 print(json.dumps({'status':'PASS_SOURCE_READINESS','integral_calls':0,'oracle_calls':0}));raise SystemExit
if not a.authorization:raise ValueError('root authorization absent')
auth=json.loads(Path(a.authorization).read_text())
if auth!={'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'output':str(out),'no_retry':True,'seconds':30,'rss_bytes':384*1048576}:raise ValueError('authorization')
with P.with_name(P.name+'.ATTEMPT.json').open('x') as mark:json.dump(auth,mark)
out.mkdir();(out/'STARTED.json').write_text(json.dumps(auth)+'\n')
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('29s inclusive worker')));signal.setitimer(signal.ITIMER_REAL,max(.001,29-(time.monotonic()-START)))
try:
 catalog=sys.modules['loader'].load(b);sys.modules['compute'].run(out,catalog);guard()
 elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if elapsed>29 or rss>384*1048576:raise ValueError('resources')
 (out/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE_CATALOG_INTEGRAL','seconds':elapsed,'rss_bytes':rss,'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'result_sha256':sha(out/'RESULT.json')})+'\n')
except BaseException as e:
 (out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-START})+'\n');raise
