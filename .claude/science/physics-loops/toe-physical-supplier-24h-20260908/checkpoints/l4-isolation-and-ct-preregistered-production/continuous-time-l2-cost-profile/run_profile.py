import sys,time,signal,json,resource
from pathlib import Path
START=time.monotonic()
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('28 second internal reserve')));signal.alarm(28)
from preflight import verify,sha
if len(sys.argv)!=2:raise ValueError('one fresh output directory')
out=Path(sys.argv[1]);out.mkdir(parents=False,exist_ok=False)
freeze=verify()
from profile import main
try:
 result=main(out)
 if result['rss_mib']>384:raise ValueError('observed RSS')
 (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 receipt=dict(freeze=freeze,result_sha=sha(out/'RESULT.json'),paths={p.name:sha(p) for p in list(out.glob('path*.json'))+list(out.glob('synthetic*.json'))},internal_seconds=time.monotonic()-START)
 (out/'DISPATCH.json').write_text(json.dumps(receipt,indent=2)+'\n')
except BaseException as e:
 (out/'FAILURE.json').write_text(json.dumps(dict(type=type(e).__name__,message=str(e),seconds=time.monotonic()-START)))
 raise
