import sys,os,json,hashlib,importlib.util,time,signal,resource
from pathlib import Path
P=Path(__file__).resolve().parent;start=time.monotonic()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
if not sys.flags.isolated or not sys.dont_write_bytecode or len(sys.argv)!=4 or sys.argv[1] not in ('readiness','replay'):raise ValueError('-I -B run.py readiness|replay INPUT OUTPUT')
f=json.loads((P/'FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(str(p.relative_to(P)) for p in P.rglob('*') if p.is_file() and p.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('executable membership')
for p,h in f['inputs'].items():
 if sha(p)!=h:raise ValueError('pin '+p)
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
 if os.environ.get(key)!='1':raise ValueError('single thread')
for name in ('envelope','transport','fp_guard','validate_coefficients','review'):
 s=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m)
import numpy as np
import numpy.lib.format,numpy.lib.npyio,pickle,ast,tokenize,shutil,zlib,bz2,lzma
if str(Path(np.__file__).resolve())!=f['numpy_origin']:raise ValueError('numpy origin')
def origins():
 for m in list(sys.modules.values()):
  p=getattr(m,'__file__',None)
  if p:
   p=str(Path(p).resolve())
   if p not in f['inputs'] or sha(p)!=f['inputs'][p]:raise ValueError('loaded origin '+p)
origins()
if sys.argv[1]=='readiness':print(json.dumps({'status':'PASS','physical_calls':0}));raise SystemExit
out=Path(sys.argv[3]).resolve();inp=Path(sys.argv[2]).resolve()
if out.exists() or out==inp or P==out or P in out.parents:raise ValueError('fresh external output')
out.mkdir();signal.alarm(390)
try:
 result=sys.modules['review'].replay(inp);origins();rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if rss>384*1048576 or time.monotonic()-start>=400:raise ValueError('resource cap')
 result.update(seconds=time.monotonic()-start,rss_bytes=rss,source_freeze=sha(P/'FREEZE.json'),input_result_sha256=sha(inp/'RESULT.json'))
 (out/'REVIEW.json').write_text(json.dumps(result,indent=2)+'\n')
 if not result['scientific_pass']:raise ValueError('Echi scientific failure retained')
except BaseException as e:
 (out/'FAILED.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-start})+'\n');raise
