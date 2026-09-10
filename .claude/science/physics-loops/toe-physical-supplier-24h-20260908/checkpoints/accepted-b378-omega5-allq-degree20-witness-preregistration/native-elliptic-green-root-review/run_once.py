import time
START=time.monotonic()
import sys,os,json,hashlib,subprocess,signal,math,argparse
from pathlib import Path
R=Path(__file__).resolve().parent; P=R.parent/'native-elliptic-green-oracle-stretch'; O=R.parent/'native-elliptic-green-run-6d85f'
PF='6d85facf780f73e1dbaea0f98d2ef02e670eee0344ead6a5e9219e8234da4770'; LIMIT=384*1048576

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
  require(result['status']=='COMPLETE_FIXED_CASES' and result['alpha_computed'] is False,'scope')
  from fractions import Fraction as F
  rows=result['rows'];require([r['s'] for r in rows]==['0','1/1000000000','1/2','1','2'],'fixed coverage')
  baseline=json.loads((P/'RETURN_BASELINE.json').read_text())['rows']
  for row in rows:
   require(row['target']=='1/1000000000000' and row['terms']==96 and row['derivative_side']==('right' if row['s']=='0' else 'ordinary'),'design')
   require(len(row['A'])==len(row['Aprime'])==len(row['widths'])==2,'row schema');widths=[]
   for pair,width in zip([row['A'],row['Aprime']],row['widths']):
    lo,hi=map(F,pair);require(lo<=hi and hi-lo==F(width),'interval serialization');widths.append(hi-lo)
   require(row['status']==('CERTIFIED_TARGET' if max(widths)<=F(row['target']) else 'INDETERMINATE'),'target status')
   require(F(row['A'][0])>0 and F(row['Aprime'][1])<0,'known signs')
   if row['s'] in ('1/2','1','2'):
    ref=[v for v in baseline if v['s']==row['s'] and v['target']==row['target']];require(len(ref)==1 and row['return_overlap']=='PASS','reference membership')
    for key in ('A','Aprime'):
     a0,a1=map(F,row[key]);b0,b1=map(F,ref[0][key]);require(max(a0,b0)<=min(a1,b1),'independent exact series overlap')
   else:require(row['return_overlap']=='not_applicable','reference scope')
  require(result['all_targets_met']==all(r['status']=='CERTIFIED_TARGET' for r in rows),'target aggregate')
  timings=[r['seconds'] for r in rows]+[result['seconds'],done['seconds']]
  require(all(isinstance(t,(int,float)) and math.isfinite(t) and t>0 for t in timings),'finite positive timing')
  require(sum(r['seconds'] for r in rows)<=result['seconds']<=done['seconds']<=30,'nested cost receipts')
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
