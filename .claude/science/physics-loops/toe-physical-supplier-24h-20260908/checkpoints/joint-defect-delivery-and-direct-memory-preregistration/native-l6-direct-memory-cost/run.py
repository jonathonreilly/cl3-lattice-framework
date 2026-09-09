import sys,os,json,hashlib,time,signal,resource,types,argparse
from pathlib import Path
P=Path(__file__).resolve().parent;start=time.monotonic()
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','cost']);ap.add_argument('output');args=ap.parse_args()
if not sys.flags.isolated or not sys.dont_write_bytecode:raise ValueError('-I -B required')
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for chunk in iter(lambda:f.read(1<<20),b''):h.update(chunk)
 return h.hexdigest()
f=json.loads((P/'FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(p.name for p in P.iterdir() if p.is_dir() or p.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for p,h in f['inputs'].items():
 if sha(p)!=h:raise ValueError('pin '+p)
if any(os.environ.get(k)!='1' for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']):raise ValueError('threads')
for name in ['exact_square','envelope','norms','formats','fp_guard','validate_coefficients','plane','real_kernel','pilot']:
 path=P/(name+'.py');data=path.read_bytes()
 if hashlib.sha256(data).hexdigest()!=f['inputs'][str(path)]:raise ValueError('source bytes')
 m=types.ModuleType(name);m.__file__=str(path);sys.modules[name]=m;exec(compile(data,str(path),'exec'),m.__dict__)
import numpy as np
import numpy.lib.format,numpy.lib.npyio,pickle,ast,tokenize,shutil,zlib,bz2,lzma
if str(Path(np.__file__).resolve())!=f['numpy_origin'] or np.__version__!=f['numpy_version']:raise ValueError('numpy')
def guard():
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:
   p=str(Path(p).resolve())
   if p not in f['inputs'] or sha(p)!=f['inputs'][p]:raise ValueError('loaded '+p)
guard()
if args.mode=='readiness':print(json.dumps({'status':'PASS','actual_parser_late_imports':True,'physical_calls':0}));raise SystemExit
out=Path(args.output).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
signal.alarm(44)
try:
 sys.modules['pilot'].run(np,out,sys.modules['plane'],sys.modules['real_kernel'],sys.modules['norms'],sys.modules['formats'],sys.modules['fp_guard'],sys.modules['validate_coefficients'].validate,P);guard()
 if time.monotonic()-start>45 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise ValueError('whole worker resource')
 (out/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE','seconds':time.monotonic()-start,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'freeze':sha(P/'FREEZE.json'),'result_sha256':sha(out/'RESULT.json')},indent=2)+'\n')
except BaseException as e:
 out.mkdir(exist_ok=True);(out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-start})+'\n');raise
