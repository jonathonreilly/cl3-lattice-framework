import signal,time,json,sys,resource,hashlib
from pathlib import Path
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('175s')));signal.alarm(175);start=time.monotonic();B=Path(__file__).parent
from verify import verify
freeze=verify()
import core
if len(sys.argv)!=3:raise ValueError('shard fresh_output')
s=int(sys.argv[1]);out=Path(sys.argv[2]);plan=json.loads((B/'PLAN.json').read_text())
if not 0<=s<16 or out.exists():raise ValueError('domain/no overwrite')
rows=[]
try:
 for mask in plan['shards'][s]['masks']:
  if mask in plan['singletons']:
   lo=2*core.lowerroot(3);r=dict(mask=mask,gap_lower=str(lo),positive=True,display=float(lo),method='singleton initial-parity gap')
  else:r=core.certify(int(mask));r['method']='fixed c=5/2 Newton/Woodbury'
  rows.append(r)
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if not 0<rss<=384*1048576:raise ValueError('RSS')
 out.write_text(json.dumps(dict(freeze=freeze,shard=s,rows=rows,seconds=time.monotonic()-start,rss_bytes=rss),indent=2)+'\n')
except BaseException as e:
 out.with_suffix('.failure.json').write_text(json.dumps(dict(shard=s,error=repr(e),rows=rows),indent=2));raise
