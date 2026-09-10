import time
START=time.monotonic()
import sys,os,json,hashlib,subprocess,signal,math,argparse
from pathlib import Path
R=Path(__file__).resolve().parent; P=R.parent/'native-stationary-pole-scalar-batch-design'; O=R.parent/'native-stationary-pole-scalar-run-9845c'
PF='9845c5473716c7477c0833e9741b531dda4f80ff74ece0c0f16a8e515a7c043d'; LIMIT=384*1048576

def require(ok,msg):
 if not ok:raise ValueError(msg)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def write(p,data):p.write_text(json.dumps(data,indent=2)+'\n')
def pins():
 require(sha(P/'FREEZE.json')==PF,'worker freeze'); f=json.loads((P/'FREEZE.json').read_text()); rf=json.loads((R/'ROOT_FREEZE.json').read_text())
 for name,h in rf['files'].items():require(sha(R/name)==h,'root source '+name)
 require(str(Path(sys.executable).resolve())==f['interpreter'],'root interpreter')
 for name,h in f['inputs'].items():require(sha(name)==h,'input '+name)
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:
   p=str(Path(p).resolve())
   if p!=str(R/'run_once.py'):require(p in f['inputs'] and sha(p)==f['inputs'][p],'root loaded origin '+p)
 return f

def timeout(*_):raise TimeoutError('root 29.5-second deadline')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','launch']);args=ap.parse_args(); require(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site,'-I -B -S')
 signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,max(.001,29.5-(time.monotonic()-START)))
 f=pins()
 if args.mode=='readiness':print(json.dumps({'status':'PASS','physical_calls':0}));return
 require(not O.exists(),'fresh output')
 with (R/'STARTED.json').open('x') as mark:json.dump({'epoch':time.time(),'worker_freeze':PF,'seconds':30,'rss_bytes':LIMIT,'no_retry':True},mark)
 p=None;peak=0;perpid={};known={os.getpid()};failure=None;rc=None
 try:
  env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
  with (R/'WORKER.stdout').open('x') as out,(R/'WORKER.stderr').open('x') as err:
   p=subprocess.Popen([f['interpreter'],'-I','-B','-S',str(P/'run.py'),'cost',str(O)],stdout=out,stderr=err,env=env,start_new_session=True);known.add(p.pid)
   while p.poll() is None:
    rows=[tuple(map(int,l.split())) for l in subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3).splitlines() if len(l.split())==3]; ids={os.getpid(),p.pid}
    while True:
     nxt=ids|{pid for pid,ppid,rss in rows if ppid in ids}
     if nxt==ids:break
     ids=nxt
    known|=ids;resident=sum(rss*1024 for pid,ppid,rss in rows if pid in ids)
    for pid,ppid,rss in rows:
     if pid in ids:perpid[pid]=max(perpid.get(pid,0),rss*1024)
    if resident>peak:
     peak=resident;write(R/'PEAK.json',{'rss_bytes':peak,'processes':[{'pid':pid,'ppid':ppid,'rss_bytes':rss*1024} for pid,ppid,rss in rows if pid in ids]})
    require(resident<=LIMIT,'whole-tree RSS');require(time.monotonic()-START<29.5,'root deadline');time.sleep(.02)
   rc=p.wait();require(rc==0,'worker exit '+str(rc))
  pins(); result=json.loads((O/'RESULT.json').read_text()); done=json.loads((O/'WORKER_COMPLETE.json').read_text())
  require(done['status']=='COMPLETE' and done['freeze_sha256']==PF and done['result_sha256']==sha(O/'RESULT.json'),'completion binding')
  from fractions import Fraction as F
  require(result['status']=='COMPLETE_FIXED_66_ORACLES' and result['B_computed'] is False and result['matrix_computed'] is False and result['alpha_computed'] is False,'scope')
  expected=json.loads((P/'POLES.json').read_text())['rows'];rows=result['rows'];require(len(expected)==len(rows)==66,'fixed66')
  for row,pole in zip(rows,expected):
   require(row['pole']==pole and row['id']==pole['id'] and row['gate']=='PASS','exact pole binding')
   raw=row['oracle'];require(F(raw['s'])==F(pole['s_midpoint']) and raw['status']=='CERTIFIED_TARGET' and raw['terms']==160,'oracle parameter')
   require(len(raw['widths'])==2,'two widths')
   for key,inf,width in zip(('A','Aprime'),('A_midpoint_inflation','Aprime_midpoint_inflation'),raw['widths']):
    lo,hi=map(F,raw[key]);require(lo<=hi and hi-lo==F(width)<=F(1,10**30),'oracle precision')
    x,y=map(F,row[key+'_whole_bracket']);e=F(pole[inf]);require(e>=0 and x==lo-e and y==hi+e,'actual whole-bracket inflation')
    require(x>0 if key=='A' else y<0,'physical sign')
   require(0<raw['seconds']<=row['seconds']<=result['seconds'],'row timing')
  partial=json.loads((O/'PARTIAL.json').read_text());require(partial['rows']==rows,'final partial retained')
  timings=[result['seconds'],done['seconds']];require(all(isinstance(t,(int,float)) and math.isfinite(t) and t>0 for t in timings),'finite positive timing')
  require(result['seconds']<=done['seconds']<=30,'nested cost receipts')
  pins()
  require(0<done['rss_bytes']<=LIMIT and 0<peak<=LIMIT and time.monotonic()-START<29.5,'resources')
 except BaseException as exc:failure=repr(exc)
 finally:
  if p is not None:
   if failure or p.poll() is None:
    try:os.killpg(p.pid,signal.SIGKILL)
    except ProcessLookupError:pass
   rc=p.wait()
  signal.setitimer(signal.ITIMER_REAL,0)
  write(R/'RECEIPT.json',{'pass':failure is None,'failure':failure,'returncode':rc,'seconds':time.monotonic()-START,'sampled_whole_tree_peak':peak,'per_pid_highwater':perpid,'worker_freeze':PF,'external_whole_shell_receipt_pending':True})
 require(failure is None,'attempt failed '+str(failure));print(json.dumps({'status':'PASS_EXTERNAL_SHELL_PENDING','seconds':time.monotonic()-START,'sampled_whole_tree_peak':peak}))
if __name__=='__main__':main()
