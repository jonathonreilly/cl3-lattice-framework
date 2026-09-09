"""UNAUTHORIZED proposal. No worker import; explicit external authorization required."""
import time
START=time.monotonic()
import sys,os,json,hashlib,subprocess,signal,math,re
from pathlib import Path
B=Path(__file__).resolve().parent
LIMIT=384*1048576

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def require(x,s):
 if not x:raise ValueError(s)
def pins(path,expected):
 require(sha(path)==expected,'freeze '+str(path));f=json.loads(path.read_text())
 for p,h in f['inputs'].items():require(sha(p)==h,'input '+p)
 return f

def tree(root):
 rows=[tuple(map(int,l.split())) for l in subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3).splitlines() if len(l.split())==3]
 ids={root,os.getpid()}
 while True:
  new=ids|{pid for pid,ppid,rss in rows if ppid in ids}
  if new==ids:break
  ids=new
 return ids,sum(rss*1024 for pid,ppid,rss in rows if pid in ids)
def kill(p,known):
 try:os.killpg(p.pid,signal.SIGKILL)
 except ProcessLookupError:pass
 for pid in known-{os.getpid()}:
  try:os.kill(pid,signal.SIGKILL)
  except ProcessLookupError:pass

def stage(name,command,cap,logs,env):
 began=time.monotonic();p=None;known=set();peak=0;failure=None;rc=None
 write(logs/(name+'.STARTED.json'),{'stage':name,'command':command,'utc':time.time(),'cap':cap})
 try:
  with (logs/(name+'.stdout')).open('x') as out,(logs/(name+'.stderr')).open('x') as err:
   p=subprocess.Popen(['/usr/bin/time','-lp']+command,stdout=out,stderr=err,env=env,start_new_session=True);known.add(p.pid)
   while p.poll() is None:
    ids,rss=tree(p.pid);known|=ids;peak=max(peak,rss)
    require(time.monotonic()-began<cap,'stage wall cap')
    require(time.monotonic()-START+10<1800,'aggregate wall cap')
    require(rss<=LIMIT,'sampled aggregate RSS cap')
    time.sleep(.02)
   rc=p.wait();require(rc==0,'child exit '+str(rc))
 except BaseException as e:failure=repr(e)
 finally:
  if p is not None:
   if failure or p.poll() is None:kill(p,known)
   rc=p.wait()
 elapsed=time.monotonic()-began
 text=(logs/(name+'.stderr')).read_text() if (logs/(name+'.stderr')).exists() else ''
 walls=re.findall(r'^real\s+([0-9.]+)\s*$',text,re.M);peaks=re.findall(r'^\s*(\d+)\s+maximum resident set size\s*$',text,re.M)
 external=float(walls[-1]) if walls else None;high=int(peaks[-1]) if peaks else None
 valid=(failure is None and rc==0 and math.isfinite(elapsed) and 0<elapsed<cap and external is not None and math.isfinite(external) and 0<external<cap and high is not None and 0<high<=LIMIT and 0<peak<=LIMIT and time.monotonic()-START+10<1800)
 receipt={'stage':name,'returncode':rc,'elapsed':elapsed,'external_seconds':external,'external_maxrss':high,'sampled_aggregate_peak':peak,'failure':failure,'pass':valid}
 write(logs/(name+'.RECEIPT.json'),receipt);require(valid,'stage failed '+name);return receipt

def output_snapshot(p):return {str(q.relative_to(p)):sha(q) for q in sorted(p.rglob('*')) if q.is_file()}
def verify_outputs(p,freeze,contract):
 r=json.loads((p/'RESULT.json').read_text());c=json.loads((p/'WORKER_COMPLETE.json').read_text())
 require(r['passes_Echi'] is True and c['status']=='PRODUCTION_ONLY_COMPLETE','production status')
 require(c['source_freeze']==freeze and c['contract_sha256']==contract and c['result_sha256']==sha(p/'RESULT.json'),'completion binding')
 require(math.isfinite(c['seconds']) and 0<c['seconds']<1390 and 0<c['rss_bytes']<=LIMIT,'worker resources')
 finals={'firstP','firstO','secondP','secondO','sourceP','sourceO','chi_real'};seen=set()
 for row in r['vector_manifest']:
  name=row['file'];require(Path(name).name==name,'manifest path');q=p/name;require(sha(q)==row['sha256'],'vector hash')
  if q.stem in finals:
   require(q.stem not in seen,'duplicate vector');seen.add(q.stem);raw=row['raw'];b=p/(q.stem+'.bin')
   require(raw['phase']==('real' if q.stem.startswith('first') else 'i') and raw['entries']==1<<20 and raw['bytes']==b.stat().st_size==16*(1<<20) and raw['sha256']==sha(b),'raw binding')
 require(seen==finals,'seven vectors');return r

def timeout(signum,frame):raise TimeoutError('aggregate internal watchdog')

def main():
 signal.signal(signal.SIGALRM,timeout);signal.alarm(max(1,int(1785-(time.monotonic()-START))))
 require(sys.flags.isolated and sys.dont_write_bytecode,'-I -B required')
 require(len(sys.argv)==3,'supervise.py AUTHORIZATION.json FRESH_OUTPUT')
 cfg=json.loads((B/'DESIGN.json').read_text());require(cfg['replay_freeze']!='UNAUTHORIZED_PENDING_FINAL_REPLAY','replay not frozen')
 authorization_path=Path(sys.argv[1]);authorization_hash=sha(authorization_path);auth=json.loads(authorization_path.read_text());require(auth.get('authorized') is True and auth.get('supervisor_freeze')==sha(B/'FREEZE.json'),'authorization')
 for n,h in json.loads((B/'FREEZE.json').read_text())['files'].items():require(sha(B/n)==h,'supervisor source')
 o=Path(sys.argv[2]).resolve();require(not o.exists() and o!=B and B not in o.parents,'fresh external output');o.mkdir();write(o/'STARTED.json',{'utc':time.time(),'design':cfg,'scope':'single attempt, no retries'})
 try:
  prod=Path(cfg['production_dir']);rep=Path(cfg['replay_dir']);pf=pins(prod/'RUNTIME_FREEZE.json',cfg['production_freeze']);rf=pins(rep/'FREEZE.json',cfg['replay_freeze']);require(sha(prod/'CONTRACT.json')==cfg['contract_sha256'],'contract')
  # Worker authorization is separately supplied by root; this supervisor never creates it.
  worker_authorization_hash=sha(prod/'ROOT_AUTHORIZATION.json');a=json.loads((prod/'ROOT_AUTHORIZATION.json').read_text());require(a.get('authorized') is True and a.get('source_freeze')==cfg['production_freeze'] and a.get('contract_sha256')==cfg['contract_sha256'],'worker authorization')
  env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
  stage('production',[pf['interpreter'],'-I','-B',str(prod/'run.py'),'run',str(o/'production')],1390,o,env)
  pins(prod/'RUNTIME_FREEZE.json',cfg['production_freeze']);result=verify_outputs(o/'production',cfg['production_freeze'],cfg['contract_sha256']);before=output_snapshot(o/'production');write(o/'PRODUCTION_MEMBERSHIP.json',before)
  binding=o/'REPLAY_BINDING.json';write(binding,{'result_sha256':sha(o/'production/RESULT.json'),'worker_complete_sha256':sha(o/'production/WORKER_COMPLETE.json'),'production_source_freeze':cfg['production_freeze'],'production_contract_sha256':cfg['contract_sha256']})
  stage('replay',[rf['interpreter'],'-I','-B',str(rep/'run.py'),'replay',str(o/'production'),str(o/'replay'),str(binding)],400,o,env)
  pins(rep/'FREEZE.json',cfg['replay_freeze']);require(before==output_snapshot(o/'production'),'replay modified input')
  review=json.loads((o/'replay/REVIEW.json').read_text());require(review['status']=='PASS' and review['scientific_pass'] is True and review['source_freeze']==cfg['replay_freeze'] and review['input_result_sha256']==sha(o/'production/RESULT.json'),'replay receipt')
  require(review['worker_complete_sha256']==sha(o/'production/WORKER_COMPLETE.json') and review['input_binding_sha256']==sha(binding),'replay external binding')
  require(math.isfinite(review['seconds']) and 0<review['seconds']<400 and 0<review['rss_bytes']<=LIMIT,'replay resources')
  require(review['Echi']==result['Echi'] and review['particle_intervals']==result['particle_intervals'],'replayed values')
  pins(prod/'RUNTIME_FREEZE.json',cfg['production_freeze']);pins(rep/'FREEZE.json',cfg['replay_freeze'])
  require(sha(prod/'CONTRACT.json')==cfg['contract_sha256'] and sha(prod/'ROOT_AUTHORIZATION.json')==worker_authorization_hash and sha(authorization_path)==authorization_hash,'final contract/authorization immutability')
  require(time.monotonic()-START+10<1800,'final aggregate cap')
  write(o/'COMPLETE.json',{'status':'INTERNAL_COMPLETE_EXTERNAL_SHELL_PENDING','seconds_including_prior':time.monotonic()-START+10,'production_freeze':cfg['production_freeze'],'replay_freeze':cfg['replay_freeze'],'review_sha256':sha(o/'replay/REVIEW.json')})
 except BaseException as e:write(o/'FAILED.json',{'error':repr(e),'seconds_including_prior':time.monotonic()-START+10});raise
if __name__=='__main__':main()
