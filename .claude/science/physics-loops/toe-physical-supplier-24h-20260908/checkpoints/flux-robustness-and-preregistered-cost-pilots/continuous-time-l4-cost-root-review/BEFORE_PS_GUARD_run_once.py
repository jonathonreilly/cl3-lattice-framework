from pathlib import Path
import time,subprocess,os,signal,json,hashlib,sys,resource
B=Path(__file__).resolve().parent;C=B.parent/'continuous-time-l4-cost-profile';F='36551b8d91eccf89e658351a1db4f73efe600f0653a4c4ff473615cdc7f5e31d';O=B.parent/'continuous-time-l4-cost-production-36551b8d'
start=time.monotonic()
if hashlib.sha256((C/'FREEZE.json').read_bytes()).hexdigest()!=F:raise RuntimeError('freeze changed')
with (B/'LAUNCH_STARTED.json').open('x') as f:json.dump(dict(freeze=F,output=str(O),utc=time.time(),whole_seconds=30,whole_rss_mib=384),f)
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
failed=None;peak=0
with (B/'OUTER.stdout').open('w') as out,(B/'OUTER.stderr').open('w') as err:
 p=subprocess.Popen(['/bin/sh',str(C/'run_profile.sh'),str(O)],stdout=out,stderr=err,env=env,start_new_session=True)
 while p.poll() is None:
  raw=subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True);rows=[tuple(map(int,x.split())) for x in raw.splitlines() if len(x.split())==3];ids={p.pid,os.getpid()}
  while True:
   new=ids|{pid for pid,ppid,rss in rows if ppid in ids}
   if new==ids:break
   ids=new
  resident=sum(rss*1024 for pid,ppid,rss in rows if pid in ids);peak=max(peak,resident)
  if time.monotonic()-start>29.5:failed='whole launch wall watchdog'
  if resident>384*1048576:failed='observed whole-tree RSS watchdog'
  if failed:
   for pid in ids-{os.getpid()}:
    try:os.kill(pid,signal.SIGKILL)
    except ProcessLookupError:pass
   break
  time.sleep(.02)
 rc=p.wait()
seconds=time.monotonic()-start
rec=dict(freeze=F,returncode=rc,seconds=seconds,observed_peak_whole_tree_bytes=peak,watchdog_failure=failed,dispatch_complete=(O/'DISPATCH.json').exists(),failure_marker=(O/'FAILURE.json').exists(),external_shell_reconciliation_pending=True)
rec['provisional_resource_accept']=rc==0 and failed is None and seconds<30 and peak<=384*1048576 and rec['dispatch_complete'] and not rec['failure_marker']
(B/'OUTER.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
if not rec['provisional_resource_accept']:raise SystemExit(1)
