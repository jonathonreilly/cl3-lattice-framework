import time
START=time.monotonic()
import sys,os,json,hashlib,subprocess,signal,argparse,types
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'native-rho4-two-moment-design';O=R.parent/'native-rho4-two-moment-run-442f';LIMIT=384*1048576

def req(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def pins():
 rf=json.loads((R/'ROOT_FREEZE.json').read_text())
 req(sorted(p.name for p in R.iterdir()if p.is_dir()or p.suffix in('.py','.pyc','.so','.dylib'))==rf['membership'],'root membership')
 req(json.loads((R/'AUTHORIZATION.json').read_text())==rf['authorization'],'authorization')
 for n,h in rf['files'].items():req(sha(R/n)==h,'root source '+n)
 req(sha(P/'RUNTIME_FREEZE.json')==rf['worker_freeze'],'worker freeze');f=json.loads((P/'RUNTIME_FREEZE.json').read_text());req(str(Path(sys.executable).resolve())==f['interpreter'],'interpreter')
 for n,h in f['inputs'].items():req(sha(n)==h,'input '+n)
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:
   p=Path(p).resolve()
   if p.parent==R:req(p.name in rf['files'] and sha(p)==rf['files'][p.name],'root module')
   else:req(str(p) in f['inputs'] and sha(p)==f['inputs'][str(p)],'loaded origin '+str(p))
 return rf,f

def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','launch']);a=ap.parse_args();req(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site,'strict flags')
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('29.5s root deadline')));signal.setitimer(signal.ITIMER_REAL,max(.001,29.5-(time.monotonic()-START)))
 rf,f=pins();raw=(R/'schema.py').read_bytes();m=types.ModuleType('schema');m.__file__=str(R/'schema.py');sys.modules['schema']=m;exec(compile(raw,m.__file__,'exec'),m.__dict__)
 if a.mode=='readiness':pins();print(json.dumps({'status':'PASS_SOURCE_ONLY','integral_executed':False}));return
 req(not O.exists(),'fresh output')
 with(R/'STARTED.json').open('x') as mark:json.dump({'time':time.time(),'worker_freeze':rf['worker_freeze'],'no_retry':True,'new_two_moment_certificate':True},mark)
 p=None;peak=0;failure=None;rc=None
 try:
  with(R/'WORKER.stdout').open('x') as out,(R/'WORKER.stderr').open('x') as err:
   p=subprocess.Popen([f['interpreter'],'-I','-B','-S',str(P/'run.py'),'integral',str(O),'--authorization',str(R/'AUTHORIZATION.json')],stdout=out,stderr=err,start_new_session=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
   while p.poll() is None:
    rows=[tuple(map(int,l.split())) for l in subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3).splitlines() if len(l.split())==3];ids={os.getpid(),p.pid}
    while True:
     nxt=ids|{pid for pid,ppid,rss in rows if ppid in ids}
     if nxt==ids:break
     ids=nxt
    rss=sum(rss*1024 for pid,ppid,rss in rows if pid in ids);peak=max(peak,rss);req(rss<=LIMIT,'whole-tree RSS');req(time.monotonic()-START<29.5,'root deadline');time.sleep(.02)
   rc=p.wait();req(rc==0,'worker exit '+str(rc))
  pins();v=m.check(O,rf,time.monotonic()-START);req(time.monotonic()-START<29.5 and 0<peak<=LIMIT,'whole job resources');write(R/'SCHEMA_ACCEPTANCE.json',v)
 except BaseException as e:failure=repr(e)
 finally:
  if p is not None:
   if failure or p.poll() is None:
    try:os.killpg(p.pid,signal.SIGKILL)
    except ProcessLookupError:pass
   rc=p.wait()
  signal.setitimer(signal.ITIMER_REAL,0);write(R/'RECEIPT.json',{'pass':failure is None,'failure':failure,'returncode':rc,'seconds':time.monotonic()-START,'sampled_whole_tree_peak':peak,'worker_freeze':rf['worker_freeze'],'new_two_moment_certificate':True,'external_whole_shell_pending':True})
 req(failure is None,'fixed repaired-input nu integral attempt failed '+str(failure));print(json.dumps({'status':'PASS_EXTERNAL_PENDING','seconds':time.monotonic()-START}))
if __name__=='__main__':main()
