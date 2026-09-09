import time
START=time.monotonic()
import sys,json,hashlib,types,argparse,signal,resource,math
from pathlib import Path
P=Path(__file__).resolve().parent
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','verify']);ap.add_argument('output');ap.add_argument('--authorization');a=ap.parse_args()
 if not(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site):raise ValueError('require-I-B-S')
 f=json.loads((P/'RUNTIME_FREEZE.json').read_text())
 if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
 if sorted(x.name for x in P.iterdir() if x.is_dir() or x.suffix in('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
 for x,h in f['inputs'].items():
  if sha(x)!=h:raise ValueError('source/runtime '+x)
 out=Path(a.output).resolve()
 if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
 for name in ('arithmetic','schema','check'):
  path=P/(name+'.py');raw=path.read_bytes()
  if hashlib.sha256(raw).hexdigest()!=f['inputs'][str(path)]:raise ValueError('verified source bytes')
  m=types.ModuleType(name);m.__file__=str(path);sys.modules[name]=m;exec(compile(raw,str(path),'exec'),m.__dict__)
 def guard():
  for mod in list(sys.modules.values()):
   x=getattr(mod,'__file__',None)
   if x:
    x=str(Path(x).resolve())
    if x not in f['inputs'] or sha(x)!=f['inputs'][x]:raise ValueError('loaded origin '+x)
 guard()
 if a.mode=='readiness':print(json.dumps({'status':'PASS_SOURCE_READINESS_ONLY','saved_verification_calls':0,'native_input_loads':0}));return
 b=json.loads((P/'BINDING.json').read_text())
 if b['status']!='ACCEPTED_RESULT_BOUND' or not a.authorization:raise ValueError('actual binding/root authorization')
 auth=json.loads(Path(a.authorization).read_text())
 if auth!={'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':sha(P/'BINDING.json'),'output':str(out),'seconds':120,'rss_bytes':384*1048576,'no_retry':True}:raise ValueError('authorization')
 with P.with_name(P.name+'.ATTEMPT.json').open('x') as z:json.dump(auth,z)
 out.mkdir();(out/'STARTED.json').write_text(json.dumps(auth)+'\n')
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('119s saved action verification')));signal.setitimer(signal.ITIMER_REAL,max(.001,119-(time.monotonic()-START)))
 try:
  sys.modules['check'].run(b,out);guard();elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  if not math.isfinite(elapsed) or not 0<elapsed<119 or type(rss)is not int or not 0<rss<=384*1048576:raise ValueError('resources')
  (out/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE_SAVED_ONLY','seconds':elapsed,'rss_bytes':rss,'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':sha(P/'BINDING.json'),'result_sha256':sha(out/'RESULT.json')})+'\n')
 except BaseException as e:
  (out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-START})+'\n');raise
if __name__=='__main__':main()
