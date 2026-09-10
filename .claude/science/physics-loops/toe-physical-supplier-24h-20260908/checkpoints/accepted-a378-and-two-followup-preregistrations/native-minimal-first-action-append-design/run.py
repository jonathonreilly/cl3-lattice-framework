"""Guarded once-only first-action DATA append. No accepted-input readiness mode."""
import time
START=time.monotonic()
import sys,json,hashlib,types,argparse,signal,resource,math
from pathlib import Path
P=Path(__file__).resolve().parent

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as fp:
  for data in iter(lambda:fp.read(1048576),b''):h.update(data)
 return h.hexdigest()

def write(path,obj):
 path.write_text(json.dumps(obj,sort_keys=True,indent=2)+'\n')

def parser():
 p=argparse.ArgumentParser();p.add_argument('mode',choices=('source-readiness','native'));p.add_argument('output');p.add_argument('--authorization');return p

def main():
 a=parser().parse_args()
 if not(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):raise ValueError('require -I -B -S')
 freeze=json.loads((P/'RUNTIME_FREEZE.json').read_text());contract=json.loads((P/'CONTRACT.json').read_text())
 if str(Path(sys.executable).resolve())!=freeze['interpreter']:raise ValueError('interpreter')
 if contract['worker_seconds']!=29 or contract['external_seconds']!=30 or contract['root_kill_seconds']!=29.5 or contract['tree_rss_bytes']!=384*1048576:raise ValueError('fixed contract')
 out=Path(a.output).resolve()
 if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
 native=a.mode=='native';stage='preflight'
 if native:
  if not a.authorization:raise ValueError('root authorization absent')
  auth=json.loads(Path(a.authorization).read_text())
  expected={'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'contract_sha256':sha(P/'CONTRACT.json'),'binding_sha256':sha(P/'BINDING.json'),'output':str(out),'no_retry':True}
  if auth!=expected:raise ValueError('root authorization binding')
  marker=P.with_name(P.name+'.ATTEMPT.json')
  with marker.open('x') as fp:fp.write(json.dumps(auth)+'\n')
  out.mkdir();write(out/'STARTED.json',auth)
  signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('29s inclusive worker cap')))
  remaining=29-(time.monotonic()-START)
  if remaining<=0:write(out/'DISPATCH_FAILURE.json',{'stage':stage,'error':'startup deadline'});raise TimeoutError('startup deadline')
  signal.setitimer(signal.ITIMER_REAL,remaining)
 try:
  if sorted(x.name for x in P.iterdir())!=freeze['membership']:raise ValueError('exact directory membership')
  def pins(which):
   for path,digest in which.items():
    if sha(path)!=digest:raise ValueError('pin '+path)
  # Source-readiness excludes accepted scientific data bytes: it checks only
  # local source/metadata and the external installed interpreter runtime.
  pins(freeze['readiness_inputs'])
  if native:stage='accepted_input_hashes';pins(freeze['inputs'])
  def guard():
   for m in list(sys.modules.values()):
    path=getattr(m,'__file__',None)
    if path:
     path=str(Path(path).resolve())
     if path not in freeze['readiness_inputs'] or sha(path)!=freeze['readiness_inputs'][path]:raise ValueError('loaded origin '+path)
  guard();stage='verified_source_imports'
  for name in ('interval','cache_binder','append_binder','binder','core','worker'):
   path=P/(name+'.py');data=path.read_bytes()
   if hashlib.sha256(data).hexdigest()!=freeze['readiness_inputs'][str(path)]:raise ValueError('source bytes')
   m=types.ModuleType(name);m.__file__=str(path);sys.modules[name]=m;exec(compile(data,str(path),'exec'),m.__dict__)
  guard()
  if not native:
   print(json.dumps({'status':'PASS_SOURCE_RUNTIME_READINESS_ONLY','accepted_input_loads':0,'entry_calls':0,'full_stream_calls':0,'runtime_sha256':sha(P/'RUNTIME_FREEZE.json')}));return
  stage='fixed_first_action_append';plan=json.loads((P/'BINDING.json').read_text())
  # This in-memory transition exists only after the exact root authorization.
  plan['status']='ROOT_REVIEWED_FIRST_ACTION_APPEND'
  sys.modules['worker'].run(plan,out)
  result=json.loads((out/'RESULT.json').read_text())
  stage='post_source_runtime';guard();pins(freeze['inputs'])
  elapsed=time.monotonic()-START;peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  if not math.isfinite(elapsed) or not 0<elapsed<29 or not 0<peak<=384*1048576:raise ValueError('worker resources')
  if result['status']!='COMPLETE_FIRST_ACTION_DATA_APPEND_MIDPOINT_ONLY' or len(result['orbits'])!=5 or result['entries']!=6015 or result['rows']!=2010:raise ValueError('append census')
  write(out/'WORKER_COMPLETE.json',{'status':'COMPLETE_FIRST_ACTION_DATA_APPEND_ONLY','seconds':elapsed,'rss_bytes':peak,'freeze_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':sha(P/'BINDING.json'),'result_sha256':sha(out/'RESULT.json'),'generator_assembled':False,'leakage_computed':False})
 except BaseException as exc:
  if native and out.is_dir():write(out/'DISPATCH_FAILURE.json',{'status':'FAILED','stage':stage,'error':repr(exc),'seconds':time.monotonic()-START})
  raise
if __name__=='__main__':main()
