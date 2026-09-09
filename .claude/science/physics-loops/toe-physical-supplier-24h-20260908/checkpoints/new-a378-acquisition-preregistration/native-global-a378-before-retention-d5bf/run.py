import sys,json,hashlib,time,signal,resource,types,argparse
from pathlib import Path
start=time.monotonic();P=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','acquire']);ap.add_argument('output');args=ap.parse_args()
def req(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
f=json.loads((P/'FREEZE.json').read_text())
def guard():
 req(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode,'strict flags')
 req(str(Path(sys.executable).resolve())==f['interpreter'],'interpreter')
 req(sorted(p.name for p in P.iterdir() if p.is_dir() or p.suffix in ('.py','.pyc','.so','.dylib'))==f['membership'],'membership')
 for p,h in f['inputs'].items():req(sha(p)==h,'pin '+p)
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:
   p=str(Path(p).resolve());req(p in f['inputs'] and sha(p)==f['inputs'][p],'origin '+p)
guard()
for name in ['elliptic','geometry','worker']:
 p=P/(name+'.py');data=p.read_bytes();req(hashlib.sha256(data).hexdigest()==f['inputs'][str(p)],'verified bytes');m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(data,str(p),'exec'),m.__dict__)
guard()
if args.mode=='readiness':
 print(json.dumps({'status':'PASS','actual_parser':True,'oracle_calls':0,'gauss_nodes':0}));raise SystemExit
req(f['status']=='ROOT_REVIEWED_A378_ACQUISITION','not activated')
auth=json.loads((P/'AUTHORIZATION.json').read_text());req(auth=={'freeze_sha256':sha(P/'FREEZE.json'),'output':str(Path(args.output).resolve()),'once':True},'authorization')
marker=P.with_name(P.name+'-ATTEMPT');marker.mkdir();out=Path(args.output).resolve();req(not out.exists() and P not in out.parents,'fresh output')
def alarm(*_):raise TimeoutError('inclusive179seconds')
signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,max(.001,179-(time.monotonic()-start)))
error=None
try:
 sys.modules['worker'].run(out,sys.modules['elliptic'].oracle,sys.modules['geometry'].generate)
 req(time.monotonic()-start<179,'worker time');req(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=384*1048576,'worker RSS')
except BaseException as e:error=e
finally:
 try:guard()
 except BaseException as e:
  if error is None:error=e
  else:error.add_note('final guard: '+repr(e))
if error is not None:
 try:
  out.mkdir(exist_ok=True);(out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(error),'seconds':time.monotonic()-start})+'\n')
 except BaseException as e:error.add_note('retention: '+repr(e))
 raise error
(out/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE','seconds':time.monotonic()-start,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'freeze_sha256':sha(P/'FREEZE.json'),'result_sha256':sha(out/'RESULT.json')},indent=2)+'\n')
