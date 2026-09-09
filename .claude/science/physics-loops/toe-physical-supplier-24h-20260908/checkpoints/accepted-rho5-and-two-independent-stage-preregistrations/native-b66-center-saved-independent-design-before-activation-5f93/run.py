import time
START=time.monotonic()
import sys,json,hashlib,types,argparse,signal,resource,os
from pathlib import Path
sys.set_int_max_str_digits(20000)
P=Path(__file__).resolve().parent

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def save(p,x):
 q=p.with_suffix(p.suffix+'.tmp');q.write_text(json.dumps(x,default=str)+'\n');os.replace(q,p)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','verify']);ap.add_argument('output');ap.add_argument('--authorization');args=ap.parse_args()
 if not(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):raise ValueError('flags')
 f=json.loads((P/'RUNTIME_FREEZE.json').read_text());plan=json.loads((P/'BINDING.json').read_text());out=Path(args.output);current={'stage':'startup'}
 def pins():
  if sorted(x.name for x in P.iterdir())!=f['membership']:raise ValueError('membership')
  for p,h in f['readiness_inputs'].items():
   if sha(p)!=h:raise ValueError('runtime pin')
 def guard():
  for m in list(sys.modules.values()):
   p=getattr(m,'__file__',None)
   if p:
    p=str(Path(p).resolve())
    if f['readiness_inputs'].get(p)!=sha(p):raise ValueError('loaded source')
 pins();guard()
 for name in ('arithmetic','binder','check'):
  path=P/(name+'.py');data=path.read_bytes();m=types.ModuleType(name);m.__file__=str(path);sys.modules[name]=m;exec(compile(data,str(path),'exec'),m.__dict__)
 guard()
 if args.mode=='readiness':print(json.dumps({'status':'PASS_SOURCE_ONLY','scientific_loads':0}));return
 if not args.authorization or plan['status']!='ROOT_REVIEWED_SAVED_CENTER_REPLAY':raise ValueError('NOTREADY')
 auth=json.loads(Path(args.authorization).read_text())
 if auth!={'worker_freeze':sha(P/'RUNTIME_FREEZE.json'),'output':str(out),'no_retry':True}:raise ValueError('authorization')
 with P.with_name(P.name+'.ATTEMPT.json').open('x')as fmark:json.dump(auth,fmark)
 out.mkdir();signal.signal(signal.SIGALRM,lambda *_:(_ for _ in()).throw(TimeoutError('119s')));signal.setitimer(signal.ITIMER_REAL,max(.001,119-(time.monotonic()-START)))
 def emit(x):
  nonlocal current
  current=x;save(out/'PARTIAL.json',x)
 try:
  source=sys.modules['binder'].load(plan);ans=sys.modules['check'].check(source,out,emit);save(out/'RESULT.json',ans);emit({'stage':'complete','node_pairs':114972});elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  if not 0<elapsed<119 or not 0<rss<=384*1048576:raise ValueError('resources')
  save(out/'WORKER_COMPLETE.json',{'status':'COMPLETE_SAVED_CENTER_REPLAY','seconds':elapsed,'rss_bytes':rss,'worker_freeze':sha(P/'RUNTIME_FREEZE.json'),'result_sha256':sha(out/'RESULT.json')})
 except BaseException as exc:
  try:save(out/'FAILURE.json',{'current':current,'error':repr(exc)})
  except BaseException as retention:exc.add_note('retention '+repr(retention))
  raise
 finally:
  errors=[];original=sys.exception()
  try:pins();guard()
  except BaseException as e:errors.append('runtime/source '+repr(e))
  for path,digest in plan['inputs'].items():
   try:
    if sha(path)!=digest:raise ValueError(path)
   except BaseException as e:errors.append(repr(e))
  if errors:
   try:save(out/'CLOSURE_FAILURE.json',errors)
   except BaseException as e:errors.append('closure retention '+repr(e))
   if original:original.add_note(repr(errors))
   else:raise ValueError('closure')
if __name__=='__main__':main()
