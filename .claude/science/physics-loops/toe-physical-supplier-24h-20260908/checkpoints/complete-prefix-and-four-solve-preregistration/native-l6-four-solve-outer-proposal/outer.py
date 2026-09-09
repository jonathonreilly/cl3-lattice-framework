"""Unlaunched outer group watchdog. No authorization is created."""
import time
START=time.monotonic()
import sys,os,json,hashlib,subprocess,signal,re,math
from pathlib import Path
B=Path(__file__).resolve().parent;LIMIT=384*1048576

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def main():
 if not sys.flags.isolated or not sys.dont_write_bytecode or not sys.flags.no_site or len(sys.argv)!=4:raise ValueError('-I -B -S outer.py AUTH OUTPUT FRESH_LOGS')
 auth=Path(sys.argv[1]).resolve();output=Path(sys.argv[2]).resolve();logs=Path(sys.argv[3]).resolve()
 if not auth.is_file() or output.exists() or logs.exists():raise ValueError('auth/fresh paths')
 for n,h in json.loads((B/'FREEZE.json').read_text())['files'].items():
  if sha(B/n)!=h:raise ValueError('outer source '+n)
 r=json.loads((B/'RUNTIME.json').read_text())
 if str(Path(sys.executable).resolve())!=r['interpreter']:raise ValueError('interpreter')
 for p,h in r['inputs'].items():
  if sha(p)!=h:raise ValueError('runtime '+p)
 marker=B/'ATTEMPT_STARTED.json'
 with marker.open('x') as f:json.dump({'utc':time.time(),'authorization_sha256':sha(auth),'output':str(output)},f)
 logs.mkdir();p=None;known={os.getpid()};failure=None;peak=0;rc=None
 try:
  with (logs/'stdout').open('x') as out,(logs/'stderr').open('x') as err:
   p=subprocess.Popen(['/usr/bin/time','-lp',r['interpreter'],'-I','-B','-S',str(B/'bootstrap.py'),'run',str(auth),str(output)],stdout=out,stderr=err,start_new_session=True)
   known.add(p.pid)
   while p.poll() is None:
    raw=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3);rows=[tuple(map(int,l.split())) for l in raw.splitlines() if len(l.split())==3];ids={os.getpid(),p.pid}
    while True:
     new=ids|{pid for pid,ppid,rss in rows if ppid in ids}
     if new==ids:break
     ids=new
    known|=ids;rss=sum(rss*1024 for pid,ppid,rss in rows if pid in known);peak=max(peak,rss)
    if time.monotonic()-START>=1789:raise TimeoutError('outer wall')
    if rss>LIMIT:raise MemoryError('aggregate sampled RSS')
    time.sleep(.02)
   rc=p.wait()
   if rc!=0:raise RuntimeError('bootstrap exit '+str(rc))
 except BaseException as e:failure=repr(e)
 finally:
  if p is not None:
   if failure or p.poll() is None:
    for pid in known-{os.getpid()}:
     try:os.killpg(pid,signal.SIGKILL)
     except ProcessLookupError:pass
     except PermissionError:pass
     try:os.kill(pid,signal.SIGKILL)
     except ProcessLookupError:pass
   rc=p.wait()
 elapsed=time.monotonic()-START;text=(logs/'stderr').read_text();walls=re.findall(r'^real\s+([0-9.]+)\s*$',text,re.M);rsses=re.findall(r'^\s*(\d+)\s+maximum resident set size\s*$',text,re.M)
 wall=float(walls[-1]) if walls else None;high=int(rsses[-1]) if rsses else None
 valid=failure is None and rc==0 and 0<elapsed<1789 and wall is not None and math.isfinite(wall) and 0<wall<1789 and high is not None and 0<high<=LIMIT and 0<peak<=LIMIT and (output/'COMPLETE.json').is_file()
 for n,h in json.loads((B/'FREEZE.json').read_text())['files'].items():
  if sha(B/n)!=h:valid=False;failure='post source change'
 elapsed=time.monotonic()-START
 valid=valid and elapsed<1789
 write(logs/'RECEIPT.json',{'pass':valid,'failure':failure,'seconds':elapsed,'seconds_with_prior10':elapsed+10,'external_seconds':wall,'external_rss':high,'sampled_aggregate_rss':peak,'returncode':rc,'scope':'outer timer begins after its interpreter startup; root shell reconciliation required'})
 if not valid:raise SystemExit(1)
if __name__=='__main__':main()
