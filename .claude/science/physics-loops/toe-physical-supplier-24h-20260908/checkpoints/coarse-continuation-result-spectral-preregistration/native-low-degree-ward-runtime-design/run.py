import time
START=time.monotonic()
import sys,json,hashlib,types,argparse,signal,resource
from pathlib import Path
sys.set_int_max_str_digits(20000)
P=Path(__file__).resolve().parent

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def need(x,m):
 if not x:raise ValueError(m)
INITIAL_FREEZE=sha(P/'RUNTIME_FREEZE.json')
def pins(scientific):
 raw=(P/'RUNTIME_FREEZE.json').read_bytes();need(hashlib.sha256(raw).hexdigest()==INITIAL_FREEZE,'immutable runtime freeze')
 f=json.loads(raw);need(sorted(x.name for x in P.iterdir())==f['membership'],'membership');need(str(Path(sys.executable).resolve())==f['interpreter'],'interpreter')
 for p,h in f['inputs'if scientific else'readiness_inputs'].items():need(sha(p)==h,'pin '+p)
 return f
def origins(f):
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:need(str(Path(p).resolve())in f['readiness_inputs']and sha(Path(p).resolve())==f['readiness_inputs'][str(Path(p).resolve())],'origin '+p)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','native']);ap.add_argument('output');ap.add_argument('--authorization');a=ap.parse_args();need(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site,'-I-B-S')
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in()).throw(TimeoutError('19s inclusive')));signal.setitimer(signal.ITIMER_REAL,max(.001,19-(time.monotonic()-START)));f=pins(False)
 for name in ['interval','compute','worker']:
  p=P/(name+'.py');raw=p.read_bytes();need(hashlib.sha256(raw).hexdigest()==f['readiness_inputs'][str(p)],'verified bytes');m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(raw,str(p),'exec'),m.__dict__)
 origins(f)
 if a.mode=='readiness':print(json.dumps({'status':'PASS_SOURCE_ONLY','accepted_loads':0,'certificate_calls':0}));return
 need(f['execution_enabled']is True and a.authorization,'NOT_READY');out=Path(a.output).resolve();need(not out.exists()and out!=P and P not in out.parents,'fresh output');auth=json.loads(Path(a.authorization).read_text());need(auth=={'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':sha(P/'BINDING.json'),'output':str(out),'no_retry':True},'authorization')
 with P.with_name(P.name+'.ATTEMPT.json').open('x')as z:json.dump(auth,z)
 failure=None
 def resources():
  elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  need(0<elapsed<19 and type(rss)is int and 0<rss<=384*1048576,'resources')
  return elapsed,rss
 try:
  out.mkdir();(out/'STARTED.json').write_text(json.dumps(auth)+'\n')
  pins(True);b=json.loads((P/'BINDING.json').read_text());b['_binding_file_sha256']=sha(P/'BINDING.json');sys.modules['worker'].run(b,out);origins(f)
  elapsed,rss=resources()
  sys.modules['worker'].atomic(out/'WORKER_COMPLETE.json',{'status':'COMPLETE_NEW_DEGREE10_ONLY','seconds':elapsed,'rss_bytes':rss,'runtime_sha256':INITIAL_FREEZE,'binding_sha256':sha(P/'BINDING.json'),'result_sha256':sha(out/'RESULT.json')})
 except BaseException as e:failure=e
 finally:
  try:pins(True);origins(f);resources()
  except BaseException as e:
   if failure is None:failure=e
   else:failure.add_note('final closure/resource '+repr(e))
 if failure is not None:
  record={'error':repr(failure),'seconds':time.monotonic()-START}
  try:sys.modules['worker'].atomic(out/'DISPATCH_FAILURE.json',record)
  except BaseException as retention:
   failure.add_note('output retention '+repr(retention));print(json.dumps(record),file=sys.stderr)
  raise failure
if __name__=='__main__':main()
