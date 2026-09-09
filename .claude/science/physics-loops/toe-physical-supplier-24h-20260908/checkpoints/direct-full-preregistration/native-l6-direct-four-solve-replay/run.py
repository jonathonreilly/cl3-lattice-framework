import sys,os,json,hashlib,importlib.util,types,time,signal,resource
from pathlib import Path
P=Path(__file__).resolve().parent;start=time.monotonic()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as stream:
  for block in iter(lambda:stream.read(1048576),b''):h.update(block)
 return h.hexdigest()
if not sys.flags.isolated or not sys.dont_write_bytecode or len(sys.argv)!=5 or sys.argv[1] not in ('readiness','replay'):raise ValueError('-I -B run.py readiness|replay INPUT OUTPUT BINDING_JSON')
f=json.loads((P/'FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(str(p.relative_to(P)) for p in P.rglob('*') if p.is_file() and p.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('executable membership')
for p,h in f['inputs'].items():
 if sha(p)!=h:raise ValueError('pin '+p)
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
 if os.environ.get(key)!='1':raise ValueError('single thread')
for name in ('envelope','transport','fp_guard','validate_coefficients','review'):
 path=P/(name+'.py');data=path.read_bytes()
 if hashlib.sha256(data).hexdigest()!=f['inputs'][str(path)]:raise ValueError('source bytes '+name)
 m=types.ModuleType(name);m.__file__=str(path);m.__package__='';sys.modules[name]=m;exec(compile(data,str(path),'exec'),m.__dict__)
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
out.mkdir();signal.alarm(145)
progress_rows=[]
def progress(stage,**detail):
 progress_rows.append(dict(stage=stage,seconds=time.monotonic()-start,**detail));(out/'PARTIAL.json').write_text(json.dumps(progress_rows,indent=2)+'\n')
try:
 progress('input_binding')
 binding_path=Path(sys.argv[4]).resolve();binding_hash=sha(binding_path);binding=json.loads(binding_path.read_text())
 initial_result_hash=sha(inp/'RESULT.json');initial_complete_hash=sha(inp/'WORKER_COMPLETE.json');complete=json.loads((inp/'WORKER_COMPLETE.json').read_text())
 if initial_result_hash!=binding['result_sha256'] or initial_complete_hash!=binding['worker_complete_sha256']:raise ValueError('external input hash binding')
 if complete.get('status')!='PRODUCTION_ONLY_COMPLETE' or complete.get('result_sha256')!=initial_result_hash or complete.get('source_freeze')!=binding['production_source_freeze'] or complete.get('contract_sha256')!=binding['production_contract_sha256']:raise ValueError('worker completion binding')
 progress('input_binding_complete',result_sha256=initial_result_hash,worker_complete_sha256=initial_complete_hash,binding_sha256=binding_hash)
 result=sys.modules['review'].replay(inp,progress);origins()
 if sha(inp/'RESULT.json')!=initial_result_hash or sha(inp/'WORKER_COMPLETE.json')!=initial_complete_hash or sha(binding_path)!=binding_hash:raise ValueError('input changed during replay')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if rss>384*1048576 or time.monotonic()-start>=150:raise ValueError('resource cap')
 result.update(seconds=time.monotonic()-start,rss_bytes=rss,source_freeze=sha(P/'FREEZE.json'),input_result_sha256=initial_result_hash,worker_complete_sha256=initial_complete_hash,input_binding_sha256=binding_hash)
 (out/'REVIEW.json').write_text(json.dumps(result,indent=2)+'\n')
 if not result['scientific_pass']:raise ValueError('Echi scientific failure retained')
except BaseException as e:
 (out/'FAILED.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-start,'last_stage':progress_rows[-1] if progress_rows else None,'completed_records':len(progress_rows)})+'\n');raise
