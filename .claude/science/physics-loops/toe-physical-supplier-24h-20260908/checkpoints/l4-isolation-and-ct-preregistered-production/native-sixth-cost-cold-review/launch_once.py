import os,sys,time,json,subprocess,signal,hashlib,math
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'native-zero-penalty-sixth-spectator-coefficient'
expected='465b706a66f1737ccc701ebd699e7189d4eef4d42753264e5c6014cf12fc2750'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
if sha(S/'COST_FREEZE.json')!=expected:raise ValueError('freeze')
for name,h in json.loads((S/'COST_FREEZE.json').read_text()).items():
 if sha(S/name)!=h:raise ValueError('source pin '+name)
if (S/'frame_control.py').read_text().count('signal.alarm(180);start=time.monotonic();count=0')!=1:raise ValueError('alarm replacement')
# Exclusive started marker precludes any second execution through this wrapper.
with (B/'STARTED.json').open('x') as f:json.dump(dict(freeze=expected,root_authorized='single cost fixture after independent review',utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())),f)
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
cmd=['/usr/bin/time','-lp','/usr/local/bin/python3','-OO',str(S/'cost_fixture.py')]
t=time.monotonic();peak=0;reason=None
with (B/'STDOUT').open('w') as stdout,(B/'STDERR').open('w') as stderr:
 p=subprocess.Popen(cmd,stdout=stdout,stderr=stderr,env=env,start_new_session=True)
 while p.poll() is None:
  if time.monotonic()-t>=30:reason='external30s';os.killpg(p.pid,signal.SIGKILL);break
  snap=subprocess.run(['/bin/ps','-axo','pgid=,rss='],capture_output=True,text=True,timeout=1)
  rss=sum(int(row.split()[1])*1024 for row in snap.stdout.splitlines() if len(row.split())==2 and int(row.split()[0])==p.pid)
  peak=max(peak,rss)
  if rss>384*1048576:reason='observed group RSS384MiB';os.killpg(p.pid,signal.SIGKILL);break
  time.sleep(.01)
 rc=p.wait();elapsed=time.monotonic()-t
result=dict(returncode=rc,external_watchdog_seconds=elapsed,max_observed_group_rss_bytes=peak,failure_reason=reason,freeze=expected,stdout_sha=sha(B/'STDOUT'),stderr_sha=sha(B/'STDERR'),scope='one cost-only attempt; no retries')
if rc==0:
 data=json.loads((B/'STDOUT').read_text());result['fixture']=data
 if not all(math.isfinite(data[k]) and data[k]>=0 for k in ('seconds','build_seconds','solve_seconds','rss_mib','residual_norm')):raise ValueError('invalid output')
 if elapsed>30 or data['rss_mib']>384:result['failure_reason']='postcap'
(B/'RECEIPT.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
