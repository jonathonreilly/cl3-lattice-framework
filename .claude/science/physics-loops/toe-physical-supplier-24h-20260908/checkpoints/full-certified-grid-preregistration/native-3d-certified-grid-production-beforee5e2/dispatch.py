import time
START=time.monotonic()
import sys
if not sys.flags.isolated:raise RuntimeError('Python -I required')
from pathlib import Path
import argparse,subprocess,os,signal,json,runpy,math
B=Path(__file__).resolve().parent;PRIOR=40.;CAP=3600.

def run_child(command,name,out):
 begin=time.monotonic();failure=None;peak=0;ids=set();proc=None
 with (out/(name+'.stdout')).open('x') as stdout,(out/(name+'.time.stderr')).open('x') as stderr:
  proc=subprocess.Popen(['/usr/bin/time','-lp']+command,stdout=stdout,stderr=stderr,start_new_session=True)
  ids={proc.pid}
  try:
   while proc.poll() is None:
    raw=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3);rows=[tuple(map(int,x.split())) for x in raw.splitlines() if len(x.split())==3];ids={proc.pid,os.getpid()}
    while True:
     new=ids|{pid for pid,ppid,rss in rows if ppid in ids}
     if new==ids:break
     ids=new
    rss=sum(rss*1024 for pid,ppid,rss in rows if pid in ids);peak=max(peak,rss)
    if rss>384*1048576:raise MemoryError('observed tree RSS')
    if time.monotonic()-begin>179.5:raise TimeoutError('job wall reserve')
    if PRIOR+time.monotonic()-START>CAP-2:raise TimeoutError('aggregate wall')
    time.sleep(.02)
  except BaseException as e:failure=type(e).__name__+': '+str(e)
  finally:
   if failure or proc.poll() is None:
    try:os.killpg(proc.pid,signal.SIGKILL)
    except ProcessLookupError:pass
    for pid in ids-{os.getpid()}:
     try:os.kill(pid,signal.SIGKILL)
     except ProcessLookupError:pass
  rc=proc.wait()
 seconds=time.monotonic()-begin
 lines=(out/(name+'.time.stderr')).read_text().splitlines();high=[int(x.split()[0]) for x in lines if 'maximum resident set size' in x];wall=[float(x.split()[1]) for x in lines if x.startswith('real ')]
 if len(high)!=1 or len(wall)!=1 or high[0]>384*1048576 or wall[0]>180:failure=failure or 'external time/high-water receipt'
 if seconds>180:failure=failure or 'full job wall'
 receipt=dict(name=name,returncode=rc,seconds=seconds,tree_peak_bytes=peak,external_peak_bytes=high[0] if len(high)==1 else None,external_seconds=wall[0] if len(wall)==1 else None,failure=failure)
 (out/(name+'.receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n')
 if rc or failure:raise RuntimeError('fixed run closed at '+name)
 return receipt

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args();out=Path(args.output).resolve()
 if B==out or B in out.parents:raise ValueError('output must be outside frozen source')
 freeze=runpy.run_path(str(B/'verify.py'))['verify']();f=json.loads((B/'FREEZE.json').read_text())
 if f.get('cost_gate',{}).get('passed') is not True:raise ValueError('reviewed cost gate not bound')
 out.mkdir(exist_ok=False)
 (out/'STARTED.json').write_text(json.dumps(dict(freeze=freeze,utc=time.time(),prior_charge_seconds=PRIOR,aggregate_cap=CAP,jobs=24))+'\n')
 try:
  for job in range(24):
   if CAP-PRIOR-(time.monotonic()-START)<180+180+10:raise TimeoutError('complete job+analysis reserve unavailable')
   run_child([sys.executable,'-I','-OO',str(B/'producer.py'),'--job',str(job),'--output',str(out/f'job{job:02d}')],f'job{job:02d}',out)
  if CAP-PRIOR-(time.monotonic()-START)<190:raise TimeoutError('analysis reserve unavailable')
  run_child([sys.executable,'-I','-OO',str(B/'analyze.py'),str(out)],'analysis',out)
  seconds=time.monotonic()-START
  if PRIOR+seconds>CAP-1:raise TimeoutError('aggregate final cap')
  (out/'COMPLETE.json').write_text(json.dumps(dict(freeze=freeze,elapsed_seconds=seconds,prior_charge_seconds=PRIOR,total_charged_seconds=PRIOR+seconds,external_shell_reconciliation_pending=True),indent=2)+'\n')
 except BaseException as e:
  (out/'FAILURE.json').write_text(json.dumps(dict(error=type(e).__name__,message=str(e),elapsed_seconds=time.monotonic()-START))+'\n');raise
if __name__=='__main__':main()
