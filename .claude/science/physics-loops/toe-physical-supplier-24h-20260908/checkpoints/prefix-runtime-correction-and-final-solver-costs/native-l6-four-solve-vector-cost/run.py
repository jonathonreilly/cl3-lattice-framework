import sys,os,json,hashlib,time,signal,resource,importlib.util,argparse
from pathlib import Path
P=Path(__file__).resolve().parent;start=time.monotonic()
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['preflight','cost']);ap.add_argument('output');args=ap.parse_args()
if not sys.flags.isolated or not sys.dont_write_bytecode:raise ValueError('-I -B')
f=json.loads((P/'FREEZE.json').read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(x.name for x in P.iterdir() if x.is_dir() or x.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for p,h in f['inputs'].items():
 if sha(p)!=h:raise ValueError('pin '+p)
if any(os.environ.get(k)!='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')):raise ValueError('threads')
for name in ('exact_square','envelope','norms','formats','fp_guard','micro'):
 spec=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m)
import numpy as np
# Fixture-independent late imports used by NPY I/O, parser, hashing and errors.
import numpy.lib.format, numpy.lib.npyio, pickle, ast, tokenize, shutil, zlib, bz2, lzma
if str(Path(np.__file__).resolve())!=f['numpy_origin'] or np.__version__!=f['numpy_version']:raise ValueError('numpy')
def guard():
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:
   p=str(Path(p).resolve())
   if p not in f['inputs'] or sha(p)!=f['inputs'][p]:raise ValueError('loaded '+p)
guard()
if args.mode=='preflight':print(json.dumps({'status':'PASS','parser_and_late_imports':True,'physical_calls':0}));raise SystemExit
target=Path(args.output).resolve()
if target.exists() or target==P or P in target.parents:raise ValueError("fresh external output")
signal.alarm(29)
try:
 sys.modules['micro'].run(np,args.output,sys.modules['formats'],sys.modules['norms'].scan,sys.modules['fp_guard']);guard()
 if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>384*1048576:raise MemoryError('RSS')
except BaseException as e:
 out=Path(args.output);out.mkdir(exist_ok=True);(out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-start})+'\n');raise
