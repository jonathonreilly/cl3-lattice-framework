"""One worker; prospective execution requires a separately reviewed contract/auth."""
import sys,os,json,time,hashlib,types,argparse,signal,resource,math
from pathlib import Path
P=Path(__file__).resolve().parent;START=time.monotonic()
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','run']);ap.add_argument('output');args=ap.parse_args()
if not sys.flags.isolated or not sys.dont_write_bytecode:raise ValueError('-I -B')
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as stream:
  for b in iter(lambda:stream.read(1048576),b''):h.update(b)
 return h.hexdigest()
f=json.loads((P/'RUN_FREEZE.json').read_text())
if str(Path(sys.executable).resolve())!=f['interpreter']:raise ValueError('interpreter')
if sorted(q.name for q in P.iterdir() if q.is_dir() or q.suffix in ('.py','.pyc','.so','.dylib'))!=f['membership']:raise ValueError('membership')
for path,h in f['inputs'].items():
 if sha(path)!=h:raise ValueError('source/runtime pin '+path)
if any(os.environ.get(k)!='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')):raise ValueError('threads')
for name in ('exact_square','envelope','real_kernel','transport','fp_guard','norms','formats','validate_coefficients','plane','resolvent','active','worker'):
 path=P/(name+'.py');data=path.read_bytes()
 if hashlib.sha256(data).hexdigest()!=f['inputs'][str(path)]:raise ValueError('verified local bytes')
 m=types.ModuleType(name);m.__file__=str(path);sys.modules[name]=m;exec(compile(data,str(path),'exec'),m.__dict__)
import numpy as np
import numpy.lib.format,numpy.lib.npyio,pickle,ast,tokenize,shutil,zlib,bz2,lzma
if str(Path(np.__file__).resolve())!=f['numpy_origin'] or np.__version__!=f['numpy_version']:raise ValueError('NumPy origin/version')
def origins():
 for m in list(sys.modules.values()):
  q=getattr(m,'__file__',None)
  if q:
   q=str(Path(q).resolve())
   if q not in f['inputs'] or sha(q)!=f['inputs'][q]:raise ValueError('loaded origin '+q)
origins()
# A fixed two-dimensional, non-native SVD exercises the actual lazy backend path.
toy=np.array([[2.,.25],[.125,1.]])
u,s,vh=np.linalg.svd(toy)
if not np.isfinite(s).all() or np.max(np.abs((u*s)@vh-toy))>1e-12:raise ValueError('tiny SVD readiness')
origins()
if args.mode=='readiness':print(json.dumps({'status':'PASS','actual_parser_late_imports':True,'toy_svd_dimension':2,'native_calls':0,'algorithm':'direct_gaussian_once'}));raise SystemExit
contract=P/'CONTRACT.json';auth=P/'ROOT_AUTHORIZATION.json'
if not contract.exists() or not auth.exists():raise RuntimeError('UNLAUNCHED: contract and authorization absent')
c=json.loads(contract.read_text());a=json.loads(auth.read_text());fh=sha(P/'RUN_FREEZE.json');ch=sha(contract);ah=sha(auth)
if a.get('authorized') is not True or a.get('source_freeze')!=fh or a.get('contract_sha256')!=ch:raise ValueError('authorization')
if c.get('algorithm')!='direct_gaussian_once' or c.get('candidate_attempts_per_stage')!=1:raise ValueError('algorithm contract')
if c.get('first_rho')!='1/10000000000' or c.get('second_rho')!='1/1000000000' or c.get('Echi')!='1/1000000':raise ValueError('threshold contract')
if (c.get('production_seconds'),c.get('internal_seconds'),c.get('replay_seconds'),c.get('replay_internal_seconds'),c.get('prior_seconds'),c.get('aggregate_seconds'))!=(180,175,150,145,14,360):raise ValueError('fixed resource schedule')
if type(c.get('internal_seconds')) is not int or not 0<c['internal_seconds']<c['production_seconds'] or not math.isfinite(c['production_seconds']) or c.get('rss_bytes')!=384*1048576:raise ValueError('future resource contract')
out=Path(args.output).resolve()
if out.exists() or out==P or P in out.parents:raise ValueError('fresh external output')
def timeout(sig,frame):raise TimeoutError('worker internal cap')
signal.signal(signal.SIGALRM,timeout);signal.alarm(c['internal_seconds'])
try:
 result=sys.modules['worker'].planned_worker(np,out);origins()
 if not result.get('passes_Echi') or result.get('algorithm')!='direct_gaussian_once':raise ValueError('scientific failure')
 if set(result.get('candidate_diagnostics',{}))!={'firstP','firstO','secondP','secondO'} or any(d.get('spin_passes',165)>164 for d in result['candidate_diagnostics'].values()):raise ValueError('candidate coverage')
 if sha(P/'RUN_FREEZE.json')!=fh or sha(contract)!=ch or sha(auth)!=ah:raise ValueError('final binding')
 elapsed=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if elapsed>=c['production_seconds'] or rss>c['rss_bytes']:raise ValueError('resource')
 (out/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'PRODUCTION_ONLY_COMPLETE','algorithm':'direct_gaussian_once','seconds':elapsed,'rss_bytes':rss,'source_freeze':fh,'contract_sha256':ch,'result_sha256':sha(out/'RESULT.json'),'independent_replay':'PENDING'},indent=2)+'\n')
except BaseException as e:
 out.mkdir(exist_ok=True);(out/'DISPATCH_FAILURE.json').write_text(json.dumps({'error':repr(e),'seconds':time.monotonic()-START,'source_freeze':fh,'contract_sha256':ch,'stages_exist':(out/'STAGES.json').exists(),'partial_exists':(out/'PARTIAL.json').exists()},indent=2)+'\n');raise
