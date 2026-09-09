from pathlib import Path
import time,subprocess,os,signal,json,hashlib
B=Path(__file__).resolve().parent;W=Path('/private/tmp/toe-native-l6-sixth-prefix-gap-certificate-20260908');C=Path('/private/tmp/toe-native-l6-sixth-prefix-gap-certificate-20260908/.claude/science/physics-loops/native-l6-sixth-prefix-gap-certificate-20260908/SEMANTIC_CONTROLS');O=B.parent/'native-l6-prefix-semantic-run-6fa5e'
F='6fa5e98ecf3dc549ee9c85ff3b4e361c8a5ce890a3a009543bbb39f2ba1221fd'
start=time.monotonic()
if hashlib.sha256((C/'FREEZE.json').read_bytes()).hexdigest()!=F:raise RuntimeError('freeze changed')
with (B/'LAUNCH_STARTED.json').open('x') as f:json.dump(dict(freeze=F,utc=time.time(),whole_seconds=30,whole_rss_mib=384),f)
r=json.loads((C.parent/'SOURCE_FREEZE.json').read_text())
if hashlib.sha256((C.parent/'SOURCE_FREEZE.json').read_bytes()).hexdigest()!='55f22549adcffc55b7d065b72745107d7b9307101b1db41e155fb9266d4f1349':raise RuntimeError('canonical source changed')
for path,h in r['runtime'].items():
 if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=h:raise RuntimeError('runtime changed')
if O.exists() or (C/'RESULT.json').exists() or (C/'FAILURE.json').exists():raise RuntimeError('fresh output required')
O.mkdir()
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
failed=None;peak=0
with (B/'OUTER.stdout').open('w') as out,(B/'OUTER.stderr').open('w') as err:
 p=subprocess.Popen([r['interpreter'],'-I','-B','-S','-OO',str(C/'run.py'),str(W)],stdout=out,stderr=err,env=env,start_new_session=True)
 ids={p.pid}
 try:
  while p.poll() is None:
   raw=subprocess.check_output(['ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3);rows=[tuple(map(int,x.split())) for x in raw.splitlines() if len(x.split())==3];ids={p.pid,os.getpid()}
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
if (C/'RESULT.json').exists():(O/'RESULT.json').write_bytes((C/'RESULT.json').read_bytes())
if (C/'FAILURE.json').exists():(O/'FAILURE.json').write_bytes((C/'FAILURE.json').read_bytes())
seconds=time.monotonic()-start
rec=dict(freeze=F,returncode=rc,seconds=seconds,observed_peak_whole_tree_bytes=peak,watchdog_failure=failed,result_exists=(O/'RESULT.json').exists(),external_shell_reconciliation_pending=True)
rec['provisional_resource_accept']=rc==0 and failed is None and seconds<30 and peak<=384*1048576 and rec['result_exists']
(B/'OUTER.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
if not rec['provisional_resource_accept']:raise SystemExit(1)
