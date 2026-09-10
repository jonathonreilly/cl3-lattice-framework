import time
START=time.monotonic()
import sys,os,json,hashlib,subprocess,signal,argparse,types,resource
from pathlib import Path
sys.set_int_max_str_digits(20000)
R=Path(__file__).resolve().parent;P=R.parent/'native-selected-t-sensitivity-design';LIMIT=384*1048576

def req(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def write(p,x):p.write_text(json.dumps(x,default=str,indent=2)+'\n')
ROOT_INITIAL_SHA=sha(R/'ROOT_FREEZE.json')
def pins(scientific):
 req(sha(R/'ROOT_FREEZE.json')==ROOT_INITIAL_SHA,'immutable root freeze')
 rf=json.loads((R/'ROOT_FREEZE.json').read_text());req(sorted(x.name for x in R.iterdir()if x.is_dir()or x.suffix in('.py','.pyc','.so','.dylib'))==rf['membership'],'root membership')
 for name,digest in rf['files'].items():req(sha(R/name)==digest,'root pin '+name)
 req(sha(P/'FREEZE.json')==rf['worker_freeze'],'worker freeze');f=json.loads((P/'FREEZE.json').read_text());req(sorted(x.name for x in P.iterdir() if x.is_dir() or x.suffix in('.py','.pyc','.so','.dylib'))==f['membership'],'worker final membership');req(str(Path(sys.executable).resolve())==f['interpreter'],'interpreter')
 for p,h in f['inputs'].items():req(sha(p)==h,'source '+p)
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:
   p=Path(p).resolve()
   if p.parent==R:req(p.name in rf['files']and sha(p)==rf['files'][p.name],'root loaded')
   else:req(str(p)in f['inputs']and sha(p)==f['inputs'][str(p)],'external loaded '+str(p))
 return rf,f

def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=('readiness','launch'));a=ap.parse_args();req(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site,'strict flags')
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in()).throw(TimeoutError('19.5s inclusive root deadline')));signal.setitimer(signal.ITIMER_REAL,max(.001,19.5-(time.monotonic()-START)))
 rf,f=pins(False);raw=(R/'schema.py').read_bytes();m=types.ModuleType('schema');m.__file__=str(R/'schema.py');sys.modules['schema']=m;exec(compile(raw,m.__file__,'exec'),m.__dict__)
 if a.mode=='readiness':pins(False);print(json.dumps({'status':'PASS_SOURCE_ONLY','root_sha256':sha(R/'ROOT_FREEZE.json'),'actual_T_parses':0,'accepted_loads':0}));return
 req(rf['execution_enabled']is True,'root NOTREADY');auth=json.loads((R/'AUTHORIZATION.json').read_text());req(auth==rf['authorization']and sha(R/'AUTHORIZATION.json')==rf['authorization_sha256'],'exact authorization');O=Path(rf['authorization']['output']);req(not O.exists(),'fresh output')
 req(json.loads((P/'AUTHORIZATION.json').read_text())=={'freeze_sha256':rf['worker_freeze'],'output':str(O.resolve()),'once':True},'worker exact authorization')
 with(R/'STARTED.json').open('x')as fp:json.dump({'worker_freeze':rf['worker_freeze'],'no_retry':True,'started':time.time()},fp)
 proc=None;peak=0;pid_peaks={};failure=None;rc=None
 def progress(d):
  nonlocal peak
  v=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;peak=max(peak,v);req(v<=LIMIT,'root post RSS');req(time.monotonic()-START<19.5,'root inclusive deadline');write(R/'PARTIAL.json',d)
 try:
  pins(True)
  with(R/'WORKER.stdout').open('x')as stdout,(R/'WORKER.stderr').open('x')as stderr:
   proc=subprocess.Popen([f['interpreter'],'-I','-B','-S',str(P/'run.py'),'census',str(O)],stdout=stdout,stderr=stderr,start_new_session=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
   while proc.poll()is None:
    lines=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3);rows=[tuple(map(int,l.split()))for l in lines.splitlines()if len(l.split())==3];ids={os.getpid(),proc.pid}
    while True:
     nxt=ids|{pid for pid,ppid,rss in rows if ppid in ids}
     if nxt==ids:break
     ids=nxt
    rss=sum(v*1024 for pid,ppid,v in rows if pid in ids);peak=max(peak,rss)
    for pid,ppid,v in rows:
     if pid in ids:pid_peaks[str(pid)]=max(pid_peaks.get(str(pid),0),v*1024)
    req(rss<=LIMIT,'whole tree RSS');req(time.monotonic()-START<19.5,'root deadline');time.sleep(.02)
   rc=proc.wait();req(rc==0,'worker exit '+str(rc))
  pins(True);v=m.check(O,rf,time.monotonic()-START,progress);progress({'stage':'schema_complete','count':v['count']});write(R/'SCHEMA_ACCEPTANCE.json',v)
 except BaseException as exc:failure=repr(exc)
 finally:
  if proc is not None:
   if failure or proc.poll()is None:
    try:os.killpg(proc.pid,signal.SIGKILL)
    except ProcessLookupError:pass
   rc=proc.wait()
  write(R/'RECEIPT.json',{'pass':False,'failure':failure or 'final closure in progress','returncode':rc,'seconds':time.monotonic()-START,'sampled_whole_tree_peak':peak,'worker_freeze':rf['worker_freeze'],'external_whole_shell_pending':True})
  signal.signal(signal.SIGALRM,lambda *_:os._exit(124));signal.setitimer(signal.ITIMER_REAL,max(.001,20-(time.monotonic()-START)))
  # Root closure is attempted for both success and failure, without replacing earlier reason.
  try:
   pins(True);v=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;peak=max(peak,v);req(v<=LIMIT,'final root RSS');req(time.monotonic()-START<19.5,'final inclusive root deadline')
  except BaseException as exc:failure=(failure+'; 'if failure else'')+'post pins '+repr(exc)
  signal.setitimer(signal.ITIMER_REAL,0);write(R/'RECEIPT.json',{'pass':failure is None,'failure':failure,'returncode':rc,'seconds':time.monotonic()-START,'sampled_whole_tree_peak':peak,'per_pid_peaks':pid_peaks,'worker_freeze':rf['worker_freeze'],'new_certificate_only':True,'external_whole_shell_pending':True})
 req(failure is None,'new savedT sensitivity attempt failed '+str(failure));print(json.dumps({'status':'PASS_ROOT_SCHEMA_EXTERNAL_PENDING','seconds':time.monotonic()-START}))
if __name__=='__main__':main()
