import time,sys,os,subprocess,signal,json,math
from pathlib import Path
from verify import verify,sha
start=time.monotonic();B=Path(__file__).parent
if len(sys.argv)!=2:raise ValueError('fresh output')
freeze=verify();out=Path(sys.argv[1]);out.mkdir(exist_ok=False);plan=json.loads((B/'PLAN.json').read_text());prior=plan['prior_seconds'];ledger=[]
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
try:
 for s in range(16):
  if prior+time.monotonic()-start+185>1200:raise TimeoutError('next shard reserve')
  tick=time.monotonic();cmd=['/usr/bin/time','-lp',sys.executable,'-OO',str(B/'run_shard.py'),str(s),str(out/f's{s}.json')];p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=env,start_new_session=True)
  try:stdout,stderr=p.communicate(timeout=180)
  except subprocess.TimeoutExpired:
   os.killpg(p.pid,signal.SIGKILL);stdout,stderr=p.communicate();(out/f's{s}.timeout').write_text(stderr);raise
  elapsed=time.monotonic()-tick;(out/f's{s}.stdout').write_text(stdout);(out/f's{s}.stderr').write_text(stderr)
  rss=[int(x.split()[0]) for x in stderr.splitlines() if 'maximum resident set size' in x]
  if p.returncode or elapsed>180 or len(rss)!=1 or not 0<rss[0]<=384*1048576:raise ValueError('external shard guard')
  ledger.append(dict(shard=s,seconds=elapsed,rss_bytes=rss[0],sha=sha(out/f's{s}.json')));(out/'LEDGER.json').write_text(json.dumps(ledger,indent=2))
 rows=[]
 for s in range(16):
  r=json.loads((out/f's{s}.json').read_text())
  if r['freeze']!=freeze or r['shard']!=s or [x['mask'] for x in r['rows']]!=plan['shards'][s]['masks']:raise ValueError('coverage')
  rows+=r['rows']
 from fractions import Fraction
 if len(rows)!=1534 or len({x['mask'] for x in rows})!=1534:raise ValueError('total coverage')
 for r in rows:
  if r['positive']!=(Fraction(r['gap_lower'])>0):raise ValueError('exact sign')
 charged=prior+time.monotonic()-start
 if charged>1199:raise TimeoutError('final startup reserve')
 (out/'COMPLETE.json').write_text(json.dumps(dict(freeze=freeze,charged_seconds=charged,positive=sum(x['positive'] for x in rows),indeterminate=sum(not x['positive'] for x in rows),rows=rows,scope='all fixed prefix bounds; negative values preserved, no retuning'),indent=2))
except BaseException as e:
 (out/'FAILED.json').write_text(json.dumps(dict(error=repr(e),completed_shards=len(ledger),charged_seconds=prior+time.monotonic()-start)));raise
