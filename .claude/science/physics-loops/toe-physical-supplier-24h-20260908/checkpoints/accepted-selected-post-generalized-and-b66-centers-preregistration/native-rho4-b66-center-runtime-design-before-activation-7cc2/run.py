import time
START=time.monotonic()
import sys,json,hashlib,types,argparse,signal,resource,math
from pathlib import Path
sys.set_int_max_str_digits(20000)
P=Path(__file__).resolve().parent

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def write(p,x):p.write_text(json.dumps(x,default=str)+'\n')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('source-readiness','native'));ap.add_argument('output');ap.add_argument('--authorization');a=ap.parse_args()
 if not(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):raise ValueError('require -I -B -S')
 f=json.loads((P/'RUNTIME_FREEZE.json').read_text());c=json.loads((P/'CONTRACT.json').read_text());native=a.mode=='native';out=Path(a.output).resolve();stage='startup'
 if c['external_seconds']!=120 or c['worker_seconds']!=119 or c['root_kill_seconds']!=119.5 or c['tree_rss_bytes']!=384*1048576 or c['no_retry']is not True:raise ValueError('fixed contract')
 if str(Path(sys.executable).resolve())!=f['interpreter']or sorted(x.name for x in P.iterdir())!=f['membership']:raise ValueError('origin/membership')
 if out.exists()or out==P or P in out.parents:raise ValueError('fresh external output')
 if native:
  if c['execution_enabled']is not True:raise ValueError('NOTREADY: contract not activated')
  if not a.authorization:raise ValueError('root authorization absent')
  auth=json.loads(Path(a.authorization).read_text());expected={'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':sha(P/'BINDING.json'),'contract_sha256':sha(P/'CONTRACT.json'),'output':str(out),'no_retry':True}
  if auth!=expected:raise ValueError('authorization')
  with P.with_name(P.name+'.ATTEMPT.json').open('x')as marker:json.dump(auth,marker)
  out.mkdir();write(out/'STARTED.json',auth)
  signal.signal(signal.SIGALRM,lambda *_:(_ for _ in()).throw(TimeoutError('119s inclusive worker')))
  signal.setitimer(signal.ITIMER_REAL,max(.001,119-(time.monotonic()-START)))
 try:
  def pins(which):
   for p,h in which.items():
    if sha(p)!=h:raise ValueError('pin '+p)
  pins(f['readiness_inputs'])
  def guard():
   for m in list(sys.modules.values()):
    x=getattr(m,'__file__',None)
    if x:
     x=str(Path(x).resolve())
     if x not in f['readiness_inputs']or sha(x)!=f['readiness_inputs'][x]:raise ValueError('loaded origin '+x)
  guard();stage='source_imports'
  for name in ('interval','interval_base','input_loader','core','binder','worker'):
   p=P/(name+'.py');data=p.read_bytes()
   if hashlib.sha256(data).hexdigest()!=f['readiness_inputs'][str(p)]:raise ValueError('source bytes')
   m=types.ModuleType(name);m.__file__=str(p);sys.modules[name]=m;exec(compile(data,str(p),'exec'),m.__dict__)
  guard()
  if not native:
   print(json.dumps({'status':'PASS_SOURCE_READINESS_NATIVE_DISABLED','runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'accepted_loads':0,'center_calls':0,'moment_calls':0,'oracle_calls':0}));return
  stage='accepted_hashes';pins(f['inputs']);b=json.loads((P/'BINDING.json').read_text());stage='new_center_certificates';r=sys.modules['worker'].run(out,b)
  stage='postclosure';guard();pins(f['inputs']);elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  if not math.isfinite(elapsed)or not 0<elapsed<119 or type(rss)is not int or not 0<rss<=384*1048576:raise ValueError('resources')
  if r['status']!='COMPLETE_NEW_RHO4_B66_CERTIFICATES'or len(r['rows'])!=66 or r['node_center_pairs']!=114972:raise ValueError('complete census')
  write(out/'WORKER_COMPLETE.json',{'status':'COMPLETE_NEW_CENTER_CERTIFICATES_ONLY','all_targets_met':r['all_targets_met'],'runtime_sha256':sha(P/'RUNTIME_FREEZE.json'),'binding_sha256':sha(P/'BINDING.json'),'result_sha256':sha(out/'RESULT.json'),'seconds':elapsed,'rss_bytes':rss})
 except BaseException as exc:
  if native and out.is_dir():
   try:write(out/'DISPATCH_FAILURE.json',{'stage':stage,'error':repr(exc),'seconds':time.monotonic()-START})
   except BaseException as retention:exc.add_note('dispatch retention '+repr(retention))
  raise
 finally:
  if native and out.is_dir():
   original=sys.exception();errors=[]
   for path,digest in f['inputs'].items():
    try:
     if sha(path)!=digest:raise ValueError('final immutable '+path)
    except BaseException as error:errors.append(repr(error))
   if errors:
    try:write(out/'CLOSURE_FAILURE.json',{'errors':errors})
    except BaseException as error:errors.append('retention '+repr(error))
    if original is not None:original.add_note('final closure '+repr(errors))
    else:raise ValueError('final closure '+repr(errors))
if __name__=='__main__':main()
