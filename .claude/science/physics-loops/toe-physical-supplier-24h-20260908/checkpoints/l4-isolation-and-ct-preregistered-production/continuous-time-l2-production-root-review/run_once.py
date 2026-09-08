from pathlib import Path
import time,subprocess,os,signal,json,hashlib,sys
B=Path(__file__).resolve().parent
C=B.parent/'continuous-time-l2-calibration'
F='555f59fa753ff6718361dbdd33520d1a1e952db77cf26d06960e840ee1f63ad4'
assert hashlib.sha256((C/'FINAL_FREEZE.json').read_bytes()).hexdigest()==F
O=B.parent/'continuous-time-l2-production-555f59fa'
start=time.monotonic()
with (B/'LAUNCH_STARTED.json').open('x') as f:json.dump(dict(freeze=F,output=str(O),utc=time.time(),prior_cost_seconds=.6609131669974886),f)
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
failed=None;peak=0
with (B/'OUTER.stdout').open('w') as out,(B/'OUTER.stderr').open('w') as err:
 p=subprocess.Popen(['/usr/bin/time','-lp',sys.executable,'-OO',str(C/'launch.py'),str(O)],stdout=out,stderr=err,env=env,start_new_session=True)
 while p.poll() is None:
  raw=subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True)
  rows=[tuple(map(int,x.split())) for x in raw.splitlines() if len(x.split())==3]
  ids={p.pid}
  while True:
   new=ids|{pid for pid,ppid,rss in rows if ppid in ids}
   if new==ids:break
   ids=new
  resident=[rss*1024 for pid,ppid,rss in rows if pid in ids];peak=max(peak,max(resident,default=0))
  if time.monotonic()-start+.6609131669974886>3598:failed='aggregate watchdog'
  if max(resident,default=0)>384*1048576:failed='observed per-process RSS watchdog'
  if failed:
   for pid in ids:
    try:os.kill(pid,signal.SIGKILL)
    except ProcessLookupError:pass
   break
  time.sleep(.25)
 rc=p.wait()
charged=time.monotonic()-start+.6609131669974886
record=dict(freeze=F,returncode=rc,charged_seconds=charged,observed_max_process_rss_bytes=peak,watchdog_failure=failed,complete=(O/'COMPLETE.json').exists())
record['resource_accept']=rc==0 and failed is None and charged<=3600 and peak<=384*1048576 and record['complete']
(B/'OUTER.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record),flush=True)
if not record['resource_accept']:raise SystemExit(1)
