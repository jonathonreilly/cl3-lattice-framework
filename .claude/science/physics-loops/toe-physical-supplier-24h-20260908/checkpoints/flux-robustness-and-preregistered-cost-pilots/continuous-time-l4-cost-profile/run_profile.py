"""Single attempt; external shell receipt is mandatory for final acceptance."""
import time
START=time.monotonic()
import sys,os,json,signal,subprocess,resource
from pathlib import Path
from preflight import verify,sha,B
from forecast import calculate
if len(sys.argv)!=2:raise ValueError('one fresh output directory')
out=Path(sys.argv[1]).resolve();out.mkdir(exist_ok=False)
child=None
try:
 freeze=verify()
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
 with (out/'worker.stdout').open('w') as stdout,(out/'worker.time.stderr').open('w') as stderr:
  child=subprocess.Popen(['/usr/bin/time','-lp',sys.executable,'-OO',str(B/'worker.py'),str(out)],stdout=stdout,stderr=stderr,env=env,start_new_session=True)
  while child.poll() is None:
   if time.monotonic()-START>27:raise TimeoutError('whole dispatch internal reserve')
   time.sleep(.02)
 if child.returncode:raise RuntimeError('cost worker failed '+str(child.returncode))
 lines=(out/'worker.time.stderr').read_text().splitlines();rss=[int(s.split()[0]) for s in lines if 'maximum resident set size' in s]
 if len(rss)!=1 or rss[0]>384*1048576:raise ValueError('worker high water')
 receipt=json.loads((out/'WORKER_RECEIPT.json').read_text())
 if receipt['freeze']!=freeze:raise ValueError('freeze receipt')
 for p,h in receipt['artifacts'].items():
  if sha(out/p)!=h:raise ValueError('output integrity')
 result=json.loads((out/'RESULT.json').read_text())
 for case in result['cases']:
  for record in case['postblock_paths']:
   if sha(out/record['file'])!=record['sha']:raise ValueError('post-block path binding')
 forecast=calculate(result,30.)
 forecast['profile_charge_convention']='entire 30s envelope, conservative over actual; includes startup and finalization'
 (out/'FORECAST.json').write_text(json.dumps(forecast,indent=2)+'\n')
 final=dict(freeze=freeze,internal_seconds=time.monotonic()-START,worker_peak_bytes=rss[0],parent_peak_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,external_acceptance_pending=True,files={p.name:sha(p) for p in out.iterdir() if p.is_file()})
 if final['parent_peak_bytes']>384*1048576 or final['internal_seconds']>29:raise ValueError('parent cap')
 (out/'DISPATCH.json').write_text(json.dumps(final,indent=2)+'\n')
except BaseException as e:
 if child is not None and child.poll() is None:
  os.killpg(child.pid,signal.SIGKILL);child.wait()
 (out/'FAILURE.json').write_text(json.dumps(dict(type=type(e).__name__,message=str(e),seconds=time.monotonic()-START))+'\n')
 raise
