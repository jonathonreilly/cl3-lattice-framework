"""Inactive runtime: source-readiness only. Native execution is unconditionally refused."""
import sys,json,hashlib,types,argparse,time,signal,resource
from pathlib import Path
P=Path(__file__).resolve().parent
START=time.monotonic()
# 65536-bit bounded scalar numerator/denominator needs at most19729 decimal digits.
sys.set_int_max_str_digits(20000)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def main():
 parser=argparse.ArgumentParser();parser.add_argument('mode',choices=('source-readiness','native'));parser.add_argument('output',nargs='?');parser.add_argument('--authorization');a=parser.parse_args()
 if not(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):raise ValueError('require -I -B -S')
 freeze=json.loads((P/'RUNTIME_FREEZE.json').read_text());pins=freeze['readiness_inputs']
 if str(Path(sys.executable).resolve())!=freeze['interpreter']:raise ValueError('interpreter')
 if sorted(x.name for x in P.iterdir())!=freeze['membership']:raise ValueError('membership')
 for p,h in pins.items():
  if sha(p)!=h:raise ValueError('source/runtime pin '+p)
 def guard():
  for m in list(sys.modules.values()):
   p=getattr(m,'__file__',None)
   if p:
    p=str(Path(p).resolve())
    if p not in pins or sha(p)!=pins[p]:raise ValueError('loaded origin '+p)
 guard()
 for name in ('interval','old_reader','data_adapter','leakage','adapter','cache_binder','append_binder','pilot_binder','action_binder','data_binder','selected_binder','binder','worker'):
  p=P/(name+'.py');data=p.read_bytes()
  if hashlib.sha256(data).hexdigest()!=pins[str(p)]:raise ValueError('verified source bytes')
  m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(data,str(p),'exec'),m.__dict__)
 guard()
 if a.mode=='native':
  if not a.output or not a.authorization:raise ValueError('native explicit output/authorization')
  auth=json.loads(Path(a.authorization).read_text());plan=json.loads((P/'BINDING.json').read_text())
  if plan.get('status')!='ROOT_REVIEWED_GENERALIZED_LEAKAGE' or auth.get('status')!='AUTHORIZED_ONCE_GENERALIZED_LEAKAGE' or auth.get('worker_freeze')!=sha(P/'RUNTIME_FREEZE.json') or auth.get('output')!=str(Path(a.output).resolve()):raise ValueError('NOTREADY authorization')
  signal.signal(signal.SIGALRM,lambda *_:(_ for _ in()).throw(TimeoutError('179s worker')));signal.setitimer(signal.ITIMER_REAL,max(.001,179-(time.monotonic()-START)))
  output=Path(a.output);prepared=None
  try:
   if output.exists():raise ValueError('fresh output')
   prepared=sys.modules['binder'].load(plan)
   result=sys.modules['worker'].compute(prepared,output);prepared=None
   for path,h in plan['inputs'].items():
    if sha(path)!=h:raise ValueError('final input closure')
   guard();elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
   if not 0<elapsed<179 or not 0<rss<=384*1048576:raise ValueError('worker resource')
   (output/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE_GENERALIZED_LEAKAGE_ATTEMPT','seconds':elapsed,'rss_bytes':rss,'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'result_sha256':sha(output/'RESULT.json')})+'\n')
  except BaseException as exc:
   if output.is_dir():(output/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(exc)})+'\n')
   raise
  finally:
   signal.setitimer(signal.ITIMER_REAL,0)
   for path,h in plan['inputs'].items():
    if sha(path)!=h:
     if output.is_dir():(output/'FINAL_PIN_FAILURE.json').write_text(json.dumps({'path':path})+'\n')
     raise ValueError('final input pin failure')
  return
 print(json.dumps({'status':'PASS_SOURCE_READINESS_NATIVE_DISABLED','runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'accepted_loads':0,'index_calls':0,'entry_calls':0,'matrix_calls':0,'seconds':time.monotonic()-START}))
if __name__=='__main__':main()
