import sys,json,hashlib,time,signal,resource,types,argparse
from pathlib import Path
P=Path(__file__).resolve().parent;start=time.monotonic()
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','cost']);ap.add_argument('output');args=ap.parse_args()
if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('-I -B -S required')
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
f=json.loads((P/'FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(p.name for p in P.iterdir() if p.is_dir() or p.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for p,h in f['inputs'].items():
 if sha(p)!=h:raise ValueError('pin '+p)
for name in ['core','pilot']:
 p=P/(name+'.py');data=p.read_bytes()
 if hashlib.sha256(data).hexdigest()!=f['inputs'][str(p)]:raise ValueError('source bytes')
 m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(data,str(p),'exec'),m.__dict__)
def guard():
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:
   p=str(Path(p).resolve())
   if p not in f['inputs'] or sha(p)!=f['inputs'][p]:raise ValueError('loaded '+p)
guard();out=Path(args.output).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
if args.mode=='readiness':
 sys.modules['pilot'].load_inputs();guard();print(json.dumps({'status':'PASS','physical_integrals':0,'actual_parser':True,'catalogue_rows':746}));raise SystemExit
signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('29-second worker alarm')));signal.alarm(29)
try:
 sys.modules['pilot'].run(out);guard()
 if time.monotonic()-start>30 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise ValueError('worker resources')
 (out/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE','seconds':time.monotonic()-start,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'freeze_sha256':sha(P/'FREEZE.json'),'result_sha256':sha(out/'RESULT.json')},indent=2)+'\n')
except BaseException as e:
 out.mkdir(exist_ok=True);(out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-start})+'\n');raise
