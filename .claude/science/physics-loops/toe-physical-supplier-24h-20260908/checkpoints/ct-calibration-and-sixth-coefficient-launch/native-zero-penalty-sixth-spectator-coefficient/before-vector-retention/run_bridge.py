import time,signal
START=time.monotonic();signal.alarm(180)
import os,sys,json,hashlib,argparse,resource
from pathlib import Path
p=Path(__file__).resolve().parent
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS'):
 if os.environ.get(key)!='1':raise RuntimeError('one thread required: '+key)
a=argparse.ArgumentParser();a.add_argument('--bridge',type=int,required=True,choices=(0,3,9,12,36,96));a.add_argument('--output',type=Path,required=True);args=a.parse_args()
if args.output.exists():raise RuntimeError('refuse output overwrite')
f=json.loads((p/'COMPUTATION_FREEZE.json').read_text())
for name,sha in f['inputs'].items():
 if hashlib.sha256((p/name).read_bytes()).hexdigest()!=sha:raise RuntimeError('changed source '+name)
import solver_core as c
raw=json.loads((p/'PREFIXES.json').read_text());model=c.Model(raw);row=next(x for x in raw['rows'] if x['bridge_edge']==args.bridge);result=c.solve_bridge(model,row)
seconds=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
if seconds>=180 or not 0<rss<384:raise RuntimeError('resource cap')
result.update(seconds=seconds,rss_mib=rss,input_hashes=f['inputs'],numpy_version=c.np.__version__,numpy_init_sha256=hashlib.sha256(Path(c.np.__file__).read_bytes()).hexdigest(),python_executable=sys.executable,freeze_sha256=hashlib.sha256((p/'COMPUTATION_FREEZE.json').read_bytes()).hexdigest())
args.output.parent.mkdir(parents=True,exist_ok=True)
with args.output.open('x') as q:json.dump(result,q,indent=2,allow_nan=False);q.write('\n')
print(json.dumps({'bridge':args.bridge,'coefficient':result['coefficient'],'error':result['absolute_error_bound'],'interval':result['interval'],'seconds':seconds,'rss_mib':rss,'output_sha256':hashlib.sha256(args.output.read_bytes()).hexdigest()},allow_nan=False))
