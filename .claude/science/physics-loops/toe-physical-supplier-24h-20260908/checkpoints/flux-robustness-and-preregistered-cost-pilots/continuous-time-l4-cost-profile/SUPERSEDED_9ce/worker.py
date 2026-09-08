import sys,json,time,resource
from pathlib import Path
from preflight import verify,sha
if len(sys.argv)!=2:raise ValueError('one output directory')
freeze=verify();out=Path(sys.argv[1])
from profile import main
r=main(out);r['worker_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
(out/'RESULT.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n')
(out/'WORKER_RECEIPT.json').write_text(json.dumps(dict(freeze=freeze,result_sha=sha(out/'RESULT.json'),artifacts={p.name:sha(p) for p in out.glob('*.json') if p.name!='WORKER_RECEIPT.json'}),indent=2)+'\n')
