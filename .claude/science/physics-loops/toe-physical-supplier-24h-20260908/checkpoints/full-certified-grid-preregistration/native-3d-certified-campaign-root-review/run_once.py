import time
START=time.monotonic()
from pathlib import Path
import subprocess,os,signal,json,hashlib,math
B=Path(__file__).resolve().parent;BASE=B.parent
S=BASE/'native-3d-certified-grid-production';P=BASE/'native-3d-certified-production-post-review'
O=BASE/'native-certified-grid-run-09bc556a';R=BASE/'native-certified-grid-replays-09bc556a'
F='09bc556a79a4a64488bfa1a59caef7b97afee37f298273d97fb4a2d817dda636'
PF='2e6398d594376aa40f713c65f7494c9be778483eea181e1eed7f5a8b47519206'
PRIOR=40.;CAP=3600.;RSS=384*1048576

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def check(ok,msg):
 if not ok:raise RuntimeError(msg)
def validate():
 check(sha(S/'FREEZE.json')==F and sha(P/'PRE_DATA_FREEZE.json')==PF,'frozen source changed')
 for root,name in [(S,'FREEZE.json'),(P,'PRE_DATA_FREEZE.json')]:
  for f,h in read(root/name)['files'].items():
   p=Path(f);p=p if p.is_absolute() else root/p;check(sha(p)==h,'changed input '+str(p))
 check(read(S/'FREEZE.json')['cost_gate']['passed'] is True,'cost gate')
 for p,h in read(S/'RUNTIME.json')['files'].items():check(sha(Path(p))==h,'runtime changed')
 check(not O.exists() and not R.exists(),'fresh output required')
 return read(S/'RUNTIME.json')['interpreter']

def run(command,label,cap,env):
 begin=time.monotonic();peak=0;failure=None;ids=set()
 with (B/(label+'.stdout')).open('x') as stdout,(B/(label+'.time.stderr')).open('x') as stderr:
  p=subprocess.Popen(['/usr/bin/time','-lp']+command,stdout=stdout,stderr=stderr,env=env,start_new_session=True);ids={p.pid}
  try:
   while p.poll() is None:
    raw=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3);rows=[tuple(map(int,x.split())) for x in raw.splitlines() if len(x.split())==3];ids={p.pid,os.getpid()}
    while True:
     new=ids|{pid for pid,ppid,rss in rows if ppid in ids}
     if new==ids:break
     ids=new
    resident=sum(rss*1024 for pid,ppid,rss in rows if pid in ids);peak=max(peak,resident)
    if resident>RSS:raise MemoryError('whole descendant tree')
    if time.monotonic()-begin>cap-.5:raise TimeoutError('phase reserve')
    if PRIOR+time.monotonic()-START>CAP-1:raise TimeoutError('shared campaign cap')
    time.sleep(.02)
  except BaseException as e:failure=type(e).__name__+': '+str(e)
  finally:
   if failure or p.poll() is None:
    try:os.killpg(p.pid,signal.SIGKILL)
    except ProcessLookupError:pass
    for pid in ids-{os.getpid()}:
     try:os.kill(pid,signal.SIGKILL)
     except ProcessLookupError:pass
  rc=p.wait()
 seconds=time.monotonic()-begin;lines=(B/(label+'.time.stderr')).read_text().splitlines()
 high=[int(x.split()[0]) for x in lines if 'maximum resident set size' in x];wall=[float(x.split()[1]) for x in lines if x.startswith('real ')]
 if len(high)!=1 or len(wall)!=1 or not math.isfinite(wall[0]) or not 0<wall[0]<=cap or not 0<high[0]<=RSS:failure=failure or 'external phase receipt'
 if not 0<seconds<=cap:failure=failure or 'complete phase timing'
 rec=dict(label=label,returncode=rc,seconds=seconds,external_seconds=wall[0] if len(wall)==1 else None,external_peak_bytes=high[0] if len(high)==1 else None,observed_tree_peak_bytes=peak,failure=failure,shared_charged_seconds=PRIOR+time.monotonic()-START)
 (B/(label+'.receipt.json')).write_text(json.dumps(rec,indent=2)+'\n')
 check(rc==0 and failure is None,'fixed campaign stopped at '+label)
 (B/'PROGRESS.json').write_text(json.dumps(dict(completed=label,charged_seconds=PRIOR+time.monotonic()-START),indent=2)+'\n')
 print(json.dumps(dict(completed=label,charged_seconds=PRIOR+time.monotonic()-START)),flush=True)
 return rec

def main():
 interpreter=validate()
 with (B/'LAUNCH_STARTED.json').open('x') as f:json.dump(dict(source_freeze=F,replay_freeze=PF,utc=time.time(),prior_seconds=PRIOR,shared_cap_seconds=CAP,production=str(O),replays=str(R)),f)
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
 R.mkdir(exist_ok=False);receipts=[]
 try:
  receipts.append(run([interpreter,'-I','-OO',str(S/'dispatch.py'),'--output',str(O)],'production',CAP-PRIOR-2000,env))
  check(not (O/'FAILURE.json').exists() and read(O/'COMPLETE.json')['freeze']==F,'production complete')
  for job in range(24):
   check(CAP-PRIOR-(time.monotonic()-START)>=370,'complete replay and final reserve unavailable')
   receipts.append(run([interpreter,'-I','-OO',str(P/'replay.py'),'--job',str(job),'--production',str(O),'--output',str(R/f'job{job:02d}.json')],f'replay{job:02d}',180,env))
  check(CAP-PRIOR-(time.monotonic()-START)>=190,'final reserve unavailable')
  receipts.append(run([interpreter,'-I','-OO',str(P/'replay.py'),'--aggregate','--production',str(O),'--replays',str(R),'--output',str(R/'FINAL.json')],'independent_aggregate',180,env))
  final=read(R/'FINAL.json');check(final['status']=='PASS' and final['nodes']==24576 and final['all_exact_replays'] is True,'independent completion')
  check(PRIOR+time.monotonic()-START<CAP-1,'final shared cap')
  (B/'COMPLETE.json').write_text(json.dumps(dict(source_freeze=F,replay_freeze=PF,seconds=time.monotonic()-START,prior_charge_seconds=PRIOR,total_charged_seconds=PRIOR+time.monotonic()-START,phases=len(receipts),all_five_positive=final['all_five_positive'],independent_final_sha=sha(R/'FINAL.json'),external_shell_reconciliation_pending=True),indent=2)+'\n')
 except BaseException as e:
  (B/'FAILURE.json').write_text(json.dumps(dict(type=type(e).__name__,message=str(e),charged_seconds=PRIOR+time.monotonic()-START),indent=2)+'\n');raise
if __name__=='__main__':main()
