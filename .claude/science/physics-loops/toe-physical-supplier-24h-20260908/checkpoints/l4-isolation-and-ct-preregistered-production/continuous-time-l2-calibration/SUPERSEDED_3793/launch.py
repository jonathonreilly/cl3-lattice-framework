import time,sys,json,subprocess,os,signal
from pathlib import Path
START=time.monotonic()
import config
from preflight import verify,sha

def main():
 if len(sys.argv)!=2:raise ValueError('fresh output parent')
 freeze=verify();out=Path(sys.argv[1]);out.mkdir(parents=False,exist_ok=False);ledger=[]
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
 (out/'STARTED.json').write_text(json.dumps(dict(freeze=freeze,pid=os.getpid(),jobs=32,chains=128,prior_cost_seconds=config.MICRO_LEDGER,concurrency=1)))
 try:
  for a in range(8):
   for s in range(4):
    charged=config.MICRO_LEDGER+time.monotonic()-START
    if charged+185>3600:raise TimeoutError('full next-job reserve unavailable; no coverage reduction')
    folder=out/f'a{a}_s{s}';tick=time.monotonic()
    command=['/usr/bin/time','-lp',sys.executable,'-OO',str(config.B/'producer.py'),str(a),str(s),str(folder)]
    try:
     proc=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=env,start_new_session=True)
     stdout,stderr=proc.communicate(timeout=180)
     p=subprocess.CompletedProcess(command,proc.returncode,stdout,stderr)
    except subprocess.TimeoutExpired as e:
     os.killpg(proc.pid,signal.SIGKILL);stdout,stderr=proc.communicate()
     (out/f'a{a}_s{s}.timeout.txt').write_text(str(e));(out/f'a{a}_s{s}.partial.stdout').write_text(stdout);(out/f'a{a}_s{s}.partial.stderr').write_text(stderr);raise
    elapsed=time.monotonic()-tick
    (out/f'a{a}_s{s}.stdout').write_text(p.stdout);(out/f'a{a}_s{s}.stderr').write_text(p.stderr)
    rec=dict(arm=a,shard=s,returncode=p.returncode,seconds=elapsed)
    if p.returncode or elapsed>180:raise RuntimeError('fixed job failed '+str(rec))
    rss=[int(line.split()[0]) for line in p.stderr.splitlines() if 'maximum resident set size' in line]
    if len(rss)!=1 or rss[0]>384*1048576:raise RuntimeError('outer RSS')
    rec.update(result_sha=sha(folder/'RESULT.json'),outer_rss_bytes=rss[0]);(folder/'OUTER.json').write_text(json.dumps(rec));ledger.append(rec)
    (out/'LEDGER.json').write_text(json.dumps(dict(jobs=ledger,charged_seconds=config.MICRO_LEDGER+time.monotonic()-START),indent=2))
  # Analyzer startup and complete serialization remain inside global ledger.
  p=subprocess.run([sys.executable,'-OO',str(config.B/'analyze.py'),str(out)],capture_output=True,text=True,timeout=min(180,3600-config.MICRO_LEDGER-(time.monotonic()-START)),env=env)
  (out/'ANALYSIS.stdout').write_text(p.stdout);(out/'ANALYSIS.stderr').write_text(p.stderr)
  if p.returncode:raise RuntimeError('analysis failed')
  (out/'ANALYSIS.json').write_text(p.stdout)
  if config.MICRO_LEDGER+time.monotonic()-START>3599:raise TimeoutError('final external-startup reserve')
  (out/'COMPLETE.json').write_text(json.dumps(dict(freeze=freeze,charged_seconds=config.MICRO_LEDGER+time.monotonic()-START,jobs=32,analysis_sha=sha(out/'ANALYSIS.json'))))
 except BaseException as e:
  (out/'FAILED.json').write_text(json.dumps(dict(error=str(e),type=type(e).__name__,completed_jobs=len(ledger),charged_seconds=config.MICRO_LEDGER+time.monotonic()-START)));raise
if __name__=='__main__':main()
