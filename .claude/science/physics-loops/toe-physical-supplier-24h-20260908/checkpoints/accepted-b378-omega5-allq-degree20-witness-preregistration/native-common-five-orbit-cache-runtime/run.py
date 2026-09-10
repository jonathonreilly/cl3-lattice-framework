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
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['source-readiness','accepted-input-readiness','native']);ap.add_argument('output');ap.add_argument('--authorization');a=ap.parse_args()
if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('-I-B-S')
f=json.loads((P/'RUNTIME_FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(x.name for x in P.iterdir() if x.is_dir() or x.suffix in('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for p,h in f['inputs'].items():
 if sha(p)!=h:raise ValueError('pin '+p)
for name in ('interval','core','cache','binder','worker'):
 path=P/(name+'.py');data=path.read_bytes()
 if hashlib.sha256(data).hexdigest()!=f['inputs'][str(path)]:raise ValueError('verified bytes')
 m=types.ModuleType(name);m.__file__=str(path);sys.modules[name]=m;exec(compile(data,str(path),'exec'),m.__dict__)
def guard():
 for m in list(sys.modules.values()):
  path=getattr(m,'__file__',None)
  if path:
   path=str(Path(path).resolve())
   if path not in f['inputs'] or sha(path)!=f['inputs'][path]:raise ValueError('loaded origin '+path)
guard();plan=json.loads((P/'BINDING.json').read_text());out=Path(a.output).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
if a.mode!='native':
 if a.mode=='accepted-input-readiness':sys.modules['binder'].load(plan)
 guard();print(json.dumps({'status':'PASS_READINESS_ONLY','mode':a.mode,'native_matrix_calls':0}));raise SystemExit
# Cost contract is source-bound; root authorization/preregistration is still mandatory.
contract=json.loads((P/'CONTRACT.json').read_text())
if contract['status']!='ROOT_COST_ACCEPTED_AUTHORIZATION_REQUIRED' or not a.authorization:raise ValueError('cost/preregistration absent')
auth=json.loads(Path(a.authorization).read_text())
if auth!={'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'contract_sha256':sha(P/'CONTRACT.json'),'binding_sha256':sha(P/'BINDING.json'),'output':str(out),'no_retry':True}:raise ValueError('authorization')
cap=contract['worker_seconds'];limit=contract['tree_rss_bytes']
if not 0<cap<contract['external_seconds']<=180 or limit!=384*1048576:raise ValueError('contract limits')
marker=P.with_name(P.name+'.ATTEMPT.json')
with marker.open('x') as fp:fp.write(json.dumps(auth)+'\n')
out.mkdir();(out/'STARTED.json').write_text(json.dumps(auth)+'\n')
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('worker inclusive cap')));signal.setitimer(signal.ITIMER_REAL,max(.001,cap-(time.monotonic()-START)))
try:
 sys.modules['worker'].run(plan,out);guard()
 elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if elapsed>cap or rss>limit:raise ValueError('worker resources')
 for p,h in f['inputs'].items():
  if sha(p)!=h:raise ValueError('post pin')
 (out/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE_MIDPOINT_CACHE_ONLY','seconds':time.monotonic()-START,'rss_bytes':rss,'freeze_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':sha(P/'BINDING.json'),'result_sha256':sha(out/'RESULT.json')},indent=2)+'\n')
except BaseException as e:
 (out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-START})+'\n');raise
