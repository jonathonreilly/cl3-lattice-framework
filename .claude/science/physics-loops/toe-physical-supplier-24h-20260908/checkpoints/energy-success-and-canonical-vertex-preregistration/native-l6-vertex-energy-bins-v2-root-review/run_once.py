from pathlib import Path
import time,subprocess,os,signal,json,hashlib,sys,re,math
START=time.monotonic();R=Path(__file__).resolve().parent;C=R.parent/'native-l6-vertex-energy-bins-v2';O=R.parent/'native-l6-vertex-energy-bins-v2-run-4b771'
F='4b7714ad6290c898845dc8a3921e614728d1e55c898b571d8e60abe809b32059';LIMIT=384*1048576
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def require(ok,msg):
 if not ok:raise ValueError(msg)
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
require(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site,'root -I -B -S')
rf=json.loads((R/'ROOT_FREEZE.json').read_text())
for n,h in rf['files'].items():require(sha(R/n)==h,'root source '+n)
require(sha(C/'FREEZE.json')==F,'pilot freeze');f=json.loads((C/'FREEZE.json').read_text())
require(str(Path(sys.executable).resolve())==f['interpreter'],'root interpreter')
def pins():
 require(sha(C/'FREEZE.json')==F,'pilot freeze')
 for p,h in rf['accepted_inputs'].items():require(sha(p)==h,'accepted input '+p)
 for p,h in f['inputs'].items():require(sha(p)==h,'pin '+p)
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:
   p=str(Path(p).resolve())
   if p==str(R/'run_once.py'):require(sha(p)==rf['files']['run_once.py'],'root main')
   else:require(p in f['inputs'] and sha(p)==f['inputs'][p],'root loaded origin '+p)
pins();require(sorted(x.name for x in R.iterdir() if x.is_dir() or x.suffix in ('.py','.pyc','.so','.dylib'))==['run_once.py'],'root executable membership');require(not O.exists(),'fresh output')
require(sys.argv[1:] in ([],['--readiness']),'CLI: no arguments or --readiness')
if sys.argv[1:]==['--readiness']:
 print(json.dumps({'status':'PASS','actual_root_cli':True,'physical_scans':0}));raise SystemExit
with (R/'LAUNCH_STARTED.json').open('x') as marker:json.dump({'utc':time.time(),'source_freeze':F,'seconds':30,'rss_bytes':LIMIT,'scope':'single monitor plus worker; no retries'},marker)
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
p=None;known={os.getpid()};peak=0;failure=None;rc=None;peak_rows=[]
try:
 with (R/'WORKER.stdout').open('x') as out,(R/'WORKER.stderr').open('x') as err:
  p=subprocess.Popen(['/usr/bin/time','-lp',f['interpreter'],'-I','-B','-S',str(C/'run.py'),str(R.parent/'native-l6-direct-full-run-4060/production/chi_real.bin'),str(R/'BINDING.json'),str(O)],env=env,stdout=out,stderr=err,start_new_session=True);known.add(p.pid)
  while p.poll() is None:
   raw=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3);rows=[tuple(map(int,x.split())) for x in raw.splitlines() if len(x.split())==3];ids={os.getpid(),p.pid}
   while True:
    new=ids|{pid for pid,ppid,rss in rows if ppid in ids}
    if ids==new:break
    ids=new
   known|=ids;resident=sum(rss*1024 for pid,ppid,rss in rows if pid in ids)
   if resident>peak:
    peak=resident;peak_rows=[{'pid':pid,'ppid':ppid,'rss_bytes':rss*1024} for pid,ppid,rss in rows if pid in ids];write(R/'PEAK_SAMPLE.json',{'utc':time.time(),'rss_bytes':peak,'processes':peak_rows})
   require(time.monotonic()-START<29.5,'root wall watchdog');require(resident<=LIMIT,'whole-tree RSS watchdog');time.sleep(.02)
  rc=p.wait();require(rc==0,'worker exit '+str(rc))
except BaseException as e:failure=repr(e)
finally:
 if p is not None:
  if failure or p.poll() is None:
   try:os.killpg(p.pid,signal.SIGKILL)
   except ProcessLookupError:pass
   for pid in known-{os.getpid()}:
    try:os.kill(pid,signal.SIGKILL)
    except ProcessLookupError:pass
  rc=p.wait()
try:pins()
except BaseException as e:failure=repr(e)
stderr=(R/'WORKER.stderr').read_text() if (R/'WORKER.stderr').exists() else '';walls=re.findall(r'^real\s+([0-9.]+)\s*$',stderr,re.M);rsses=re.findall(r'^\s*(\d+)\s+maximum resident set size\s*$',stderr,re.M);wall=float(walls[-1]) if walls else None;rss=int(rsses[-1]) if rsses else None;elapsed=time.monotonic()-START
passed=failure is None and rc==0 and elapsed<30 and wall is not None and math.isfinite(wall) and 0<wall<30 and rss is not None and 0<rss<=LIMIT and 0<peak<=LIMIT and (O/'RESULT.json').exists()
write(R/'OUTER.json',{'provisional_resource_accept':passed,'failure':failure,'returncode':rc,'seconds':elapsed,'worker_external_seconds':wall,'worker_external_rss':rss,'observed_whole_tree_rss':peak,'peak_processes':peak_rows,'source_freeze':F,'external_root_shell_reconciliation_pending':True})
if not passed:raise SystemExit(1)
