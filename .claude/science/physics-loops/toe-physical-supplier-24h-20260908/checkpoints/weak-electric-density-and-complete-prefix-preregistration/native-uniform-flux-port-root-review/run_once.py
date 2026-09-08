from pathlib import Path
import time,subprocess,os,signal,json,hashlib
B=Path(__file__).resolve().parent;C=B.parent/'native-uniform-flux-isolated-44d34663'
F='cbb782ff7c27b457e63eaca4297500a112180a0957699c9cf6ff2f5feb6033a7'
start=time.monotonic()
if hashlib.sha256((B/'SOURCE_FREEZE.json').read_bytes()).hexdigest()!=F:raise RuntimeError('closure freeze changed')
for n,h in json.loads((B/'SOURCE_FREEZE.json').read_text())['files'].items():
 if hashlib.sha256((C/n).read_bytes()).hexdigest()!=h:raise RuntimeError('isolated input changed: '+n)
with (B/'LAUNCH_STARTED.json').open('x') as f:json.dump(dict(freeze=F,utc=time.time(),whole_seconds=180,whole_rss_mib=384),f)
r={'interpreter':'/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12'}
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
failed=None;peak=0
with (B/'OUTER.stdout').open('w') as out,(B/'OUTER.stderr').open('w') as err:
 p=subprocess.Popen([r['interpreter'],'-I','-OO',str(C/'scripts/native_uniform_cubic_flux_defect_stiffness_2026_09_08.py'),'--json'],stdout=out,stderr=err,env=env,start_new_session=True)
 ids={p.pid}
 try:
  while p.poll() is None:
   raw=subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3);rows=[tuple(map(int,x.split())) for x in raw.splitlines() if len(x.split())==3];ids={p.pid,os.getpid()}
   while True:
    new=ids|{pid for pid,ppid,rss in rows if ppid in ids}
    if new==ids:break
    ids=new
   resident=sum(rss*1024 for pid,ppid,rss in rows if pid in ids);peak=max(peak,resident)
   if time.monotonic()-start>179.5:failed='whole launch wall watchdog'
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
rec=dict(freeze=F,returncode=rc,seconds=seconds,observed_peak_whole_tree_bytes=peak,watchdog_failure=failed,result_exists=(C/'outputs/native_uniform_cubic_flux_defect_stiffness_2026_09_08.json').exists(),external_shell_reconciliation_pending=True)
rec['provisional_resource_accept']=rc==0 and failed is None and seconds<180 and peak<=384*1048576 and rec['result_exists']
(B/'OUTER.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
if not rec['provisional_resource_accept']:raise SystemExit(1)
