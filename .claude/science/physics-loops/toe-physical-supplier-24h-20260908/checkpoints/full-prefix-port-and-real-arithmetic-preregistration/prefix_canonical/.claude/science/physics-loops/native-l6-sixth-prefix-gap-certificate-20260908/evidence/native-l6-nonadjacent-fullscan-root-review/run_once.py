from pathlib import Path
import time,subprocess,os,signal,json,hashlib
B=Path(__file__).resolve().parent;C=B.parent/'native-l6-nonadjacent-fullscan-design';O=B.parent/'native-l6-nonadjacent-fullscan-run-450fe'
F='450fe097650c28e9a642a2ec5dcfc83a18d29cdec2f3c81460fcdeab726a87ef'
start=time.monotonic()
if hashlib.sha256((C/'FREEZE.json').read_bytes()).hexdigest()!=F:raise RuntimeError('freeze changed')
with (B/'LAUNCH_STARTED.json').open('x') as f:json.dump(dict(freeze=F,utc=time.time(),whole_seconds=1800,prior_charge_seconds=5,whole_rss_mib=384),f)
r=json.loads((C/'PILOT_FREEZE.json').read_text())
if O.exists():raise RuntimeError('fresh output required')
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
failed=None;peak=0
with (B/'OUTER.stdout').open('w') as out,(B/'OUTER.stderr').open('w') as err:
 p=subprocess.Popen([r['interpreter'],'-I','-B',str(C/'launch.py'),str(O)],stdout=out,stderr=err,env=env,start_new_session=True)
 ids={p.pid}
 try:
  while p.poll() is None:
   raw=subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3);rows=[tuple(map(int,x.split())) for x in raw.splitlines() if len(x.split())==3];ids={p.pid,os.getpid()}
   while True:
    new=ids|{pid for pid,ppid,rss in rows if ppid in ids}
    if new==ids:break
    ids=new
   resident=sum(rss*1024 for pid,ppid,rss in rows if pid in ids);peak=max(peak,resident)
   if time.monotonic()-start>1794.5:failed='whole launch wall watchdog'
   if resident>384*1048576:failed='observed whole-tree RSS watchdog'
   if failed:
    for pid in ids-{os.getpid()}:
     try:os.kill(pid,signal.SIGKILL)
     except ProcessLookupError:pass
    break
   time.sleep(.02)
 except BaseException as e:
  failed='watchdog exception: '+type(e).__name__+': '+str(e)
 finally:
  if failed or p.poll() is None:
   try:os.killpg(p.pid,signal.SIGKILL)
   except ProcessLookupError:pass
   for pid in ids-{os.getpid()}:
    try:os.kill(pid,signal.SIGKILL)
    except ProcessLookupError:pass
 rc=p.wait()
seconds=time.monotonic()-start
rec=dict(freeze=F,returncode=rc,seconds=seconds,observed_peak_whole_tree_bytes=peak,watchdog_failure=failed,result_exists=(O/'COMPLETE.json').exists(),external_shell_reconciliation_pending=True)
rec['provisional_resource_accept']=rc==0 and failed is None and seconds+5<1800 and peak<=384*1048576 and rec['result_exists']
(B/'OUTER.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
if not rec['provisional_resource_accept']:raise SystemExit(1)
