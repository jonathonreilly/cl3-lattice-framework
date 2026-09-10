import sys,json,hashlib,time,signal,resource,types,argparse
from pathlib import Path
P=Path(__file__).resolve().parent;start=time.monotonic()
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['source-readiness','readiness','shard']);ap.add_argument('output');ap.add_argument('--shard',type=int);args=ap.parse_args()
if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('-I -B -S required')
if args.mode=='shard' and args.shard not in range(11):raise ValueError('fixed shard id')
if args.mode!='shard' and args.shard is not None:raise ValueError('unexpected shard')
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
f=json.loads((P/'RUNTIME_FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(p.name for p in P.iterdir() if p.is_dir() or p.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for p,h in f['inputs'].items():
 if sha(p)!=h:raise ValueError('pin '+p)
for name in ['interval','interval_base','core','input_loader','compute']:
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
if args.mode=='source-readiness':print(json.dumps({'status':'PASS_SOURCE_ONLY','physical_contractions':0,'binding_ready':f['binding_sha256'] is not None}));raise SystemExit
if f['binding_sha256'] is None or sha(P/'BINDING.json')!=f['binding_sha256']:raise ValueError('accepted input binding not finalized')
b=json.loads((P/'BINDING.json').read_text())
if b['shards']!=[list(range(6*i,6*i+6)) for i in range(11)]:raise ValueError('fixed shard schedule')
# Input loading is saved-data verification only; no contraction occurs in readiness.
if args.mode=='readiness':
 data=sys.modules['input_loader'].load(b);guard();print(json.dumps({'status':'PASS_ACCEPTED_INPUT_READINESS','physical_contractions':0,'poles':len(data[0]),'catalog_nodes':len(data[2])}));raise SystemExit
signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('179-second worker alarm')));signal.alarm(179)
stage='load'
try:
 data=sys.modules['input_loader'].load(b);stage='contract';sys.modules['compute'].run(out,*data,b['shards'][args.shard]);guard()
 if time.monotonic()-start>180 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise ValueError('worker resources')
 (out/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE','shard':args.shard,'seconds':time.monotonic()-start,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'freeze_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':f['binding_sha256'],'result_sha256':sha(out/'RESULT.json')},indent=2)+'\n')
except BaseException as e:
 out.mkdir(exist_ok=True);(out/'DISPATCH_FAILURE.json').write_text(json.dumps({'stage':stage,'shard':args.shard,'error':repr(e),'seconds':time.monotonic()-start})+'\n');raise
