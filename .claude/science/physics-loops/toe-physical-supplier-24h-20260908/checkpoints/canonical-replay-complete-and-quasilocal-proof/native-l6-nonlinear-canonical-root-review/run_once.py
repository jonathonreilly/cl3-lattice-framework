"""Single root monitor plus one replay worker. No solver, no retries."""
from pathlib import Path
import time,subprocess,os,signal,json,hashlib,sys,re,math,argparse
START=time.monotonic();R=Path(__file__).resolve().parent;LIMIT=384*1048576

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def require(x,s):
 if not x:raise ValueError(s)
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def receipt(text):
 walls=re.findall(r'^real\s+(\S+)\s*$',text,re.M);rsses=re.findall(r'^\s*(\d+)\s+maximum resident set size\s*$',text,re.M)
 require(len(walls)==1 and len(rsses)==1,'receipt cardinality');w=float(walls[0]);rss=int(rsses[0]);require(math.isfinite(w) and 0<w<180 and 0<rss<=LIMIT,'external resource receipt');return w,rss

def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','run']);a=ap.parse_args();require(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site,'-I -B -S')
 freeze_sha=sha(R/'ROOT_FREEZE.json');rf=json.loads((R/'ROOT_FREEZE.json').read_text());f=json.loads((R/'INPUTS.json').read_text());C=Path(f['isolated_root'])
 def pins():
  require(sha(R/'ROOT_FREEZE.json')==freeze_sha,'immutable root freeze')
  for n,h in rf['files'].items():require(sha(R/n)==h,'root source '+n)
  for p,h in f['runtime'].items():require(sha(p)==h,'runtime '+p)
  for p,h in f['science'].items():require(sha(C/p)==h,'science '+p)
  require(str(Path(sys.executable).resolve())==f['interpreter'],'interpreter')
  for mod in list(sys.modules.values()):
   q=getattr(mod,'__file__',None)
   if q:
    q=str(Path(q).resolve())
    if q==str(R/'run_once.py'):require(sha(q)==rf['files']['run_once.py'],'root origin')
    else:require(q in f['runtime'] and sha(q)==f['runtime'][q],'runtime origin '+q)
 pins()
 if a.mode=='readiness':
  receipt('real 1.25\n12345 maximum resident set size\n')
  for text in ('real nan\n123 maximum resident set size\n','real -1\n123 maximum resident set size\n','real 1\n0 maximum resident set size\n','real 1\n123 maximum resident set size\nreal 2\n'):
   try:receipt(text)
   except ValueError:continue
   raise ValueError('receipt mutant survived')
  print(json.dumps(dict(status='ROOT_READINESS_PASS',receipt_controls=5,physical_replay=False)));return
 require(not (R/'LAUNCH_STARTED.json').exists(),'exclusive attempt');require(not (C/'outputs/native_l6_nonlinear_star_vertex_2026_09_09.json').exists(),'fresh result');require(not (R/'WORKER_COMPLETE.json').exists(),'fresh worker completion')
 with (R/'LAUNCH_STARTED.json').open('x') as fp:json.dump(dict(utc=time.time(),root_freeze=sha(R/'ROOT_FREEZE.json'),canonical_freeze=f['canonical_freeze']),fp)
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',NUMEXPR_NUM_THREADS='1');p=None;known={os.getpid()};peaks={};peak=0;failure=None;rc=None;w=None;rss=None
 try:
  with (R/'WORKER.stdout').open('x') as out,(R/'WORKER.stderr').open('x') as err:
   p=subprocess.Popen(['/usr/bin/time','-lp',f['interpreter'],'-I','-B','-S',str(R/'worker.py'),'verify'],env=env,stdout=out,stderr=err,start_new_session=True)
   while p.poll() is None:
    raw=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3);rows=[tuple(map(int,x.split())) for x in raw.splitlines() if len(x.split())==3];ids={os.getpid(),p.pid}
    while True:
     new=ids|{pid for pid,ppid,rss in rows if ppid in ids}
     if ids==new:break
     ids=new
    known|=ids;resident=sum(rss*1024 for pid,ppid,rss in rows if pid in ids);peak=max(peak,resident)
    for pid,ppid,rss in rows:
     if pid in ids:peaks[str(pid)]=max(peaks.get(str(pid),0),rss*1024)
    write(R/'PEAK.json',dict(whole_tree_peak=peak,per_pid_peak=peaks,seconds=time.monotonic()-START))
    require(time.monotonic()-START<179.5,'total wall');require(resident<=LIMIT,'whole-tree RSS');time.sleep(.02)
   rc=p.wait();require(rc==0,'worker exit')
  pins();w,rss=receipt((R/'WORKER.stderr').read_text());result=C/'outputs/native_l6_nonlinear_star_vertex_2026_09_09.json';done=json.loads((R/'WORKER_COMPLETE.json').read_text());require(done['status']=='PASS' and done['result_sha256']==sha(result) and done['canonical_freeze']==f['canonical_freeze'],'completion binding');require(json.loads(result.read_text())['status']=='PASS','canonical pass')
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
 elapsed=time.monotonic()-START;passed=failure is None and elapsed<180 and 0<peak<=LIMIT
 write(R/'COMPLETE.json',dict(status='PASS' if passed else 'FAIL',failure=failure,seconds=elapsed,whole_tree_peak=peak,per_pid_peak=peaks,returncode=rc,worker_external_seconds=w,worker_external_rss=rss,root_freeze=freeze_sha,external_root_shell_reconciliation_pending=True))
 if not passed:raise SystemExit(1)
if __name__=='__main__':main()
