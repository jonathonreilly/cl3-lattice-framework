from pathlib import Path
import time,subprocess,os,signal,json,hashlib
B=Path(__file__).resolve().parent;C=B.parent/'native-independent-dyadic-norm-replay';O=B.parent/'native-independent-dyadic-norm-run-8dc8d'
INPUT=B.parent/'native-l6-exact-norm-scanner-run-a5852'/'FIXED.bin'
F='8dc8d204769100be6ac19e1947e5d0c6d3da7fea83afe879c64fd64c9e641206'
start=time.monotonic()
if hashlib.sha256((C/'FINAL_FREEZE.json').read_bytes()).hexdigest()!=F:raise RuntimeError('freeze changed')
with (B/'LAUNCH_STARTED.json').open('x') as f:json.dump(dict(freeze=F,utc=time.time(),whole_seconds=30,whole_rss_mib=384),f)
f=json.loads((C/'FINAL_FREEZE.json').read_text())
for n,h in f['files'].items():
 if hashlib.sha256((C/n).read_bytes()).hexdigest()!=h:raise RuntimeError('source hash '+n)
if sorted(str(p.relative_to(C)) for p in C.rglob('*') if p.is_file() and p.suffix in ('.py','.pyc','.so','.dylib'))!=sorted(n for n in f['files'] if Path(n).suffix in ('.py','.pyc','.so','.dylib')):raise RuntimeError('source executable membership')
if INPUT.stat().st_size!=16777216 or hashlib.sha256(INPUT.read_bytes()).hexdigest()!='7ab4aab49683c76ea991b9dcd65245ebbbf979323d75b626bcfe6ab0321691b4':raise RuntimeError('fixed existing fixture hash')
r=json.loads((C/'RUNTIME.json').read_text())
if O.exists():raise RuntimeError('fresh output required')
O.mkdir()
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
failed=None;peak=0
with (B/'OUTER.stdout').open('w') as out,(B/'OUTER.stderr').open('w') as err:
 p=subprocess.Popen([r['interpreter'],'-I','-B','-S',str(C/'replay.py'),'--input',str(INPUT),'--modes','21','--parity','1','--output',str(O/'RESULT.json')],stdout=out,stderr=err,env=env,start_new_session=True)
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
seconds=time.monotonic()-start
rec=dict(freeze=F,returncode=rc,seconds=seconds,observed_peak_whole_tree_bytes=peak,watchdog_failure=failed,result_exists=(O/'RESULT.json').exists(),external_shell_reconciliation_pending=True)
rec['provisional_resource_accept']=rc==0 and failed is None and seconds<30 and peak<=384*1048576 and rec['result_exists']
(B/'OUTER.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
if not rec['provisional_resource_accept']:raise SystemExit(1)
