"""Single root monitor plus one numerical worker at a time. No implicit retry."""
import time
START=time.monotonic()
import sys,os,json,hashlib,subprocess,signal,math,re,struct,ast,argparse
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent
P=B/'native-l6-direct-four-solve-runtime-package';Q=B/'native-l6-direct-four-solve-replay';O=B/'native-l6-direct-full-run-4060'
PF='4060a2b4ff1bf2d7316677acf034b6ab9be8c82fcb3c13ed9095f99444c891e2';QF='2956446eb32d8a9dfa24307329f244d762830b864fa26a2ce0a71233ae21fc34';CH='62f0bae2d78c512987e0841ac7e0d3b38a5c7dede2b78059099889355d4246ac';LIMIT=384*1048576

def require(x,s):
 if not x:raise ValueError(s)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def pins():
 rf=json.loads((R/'ROOT_FREEZE.json').read_text())
 for n,h in rf['files'].items():require(sha(R/n)==h,'root source '+n)
 fs=[]
 for folder,name,expected in ((P,'RUN_FREEZE.json',PF),(Q,'FREEZE.json',QF)):
  require(sha(folder/name)==expected,'freeze');f=json.loads((folder/name).read_text())
  for n,h in f['inputs'].items():require(sha(n)==h,'source/runtime '+n)
  fs.append(f)
 require(sha(P/'CONTRACT.json')==CH,'contract')
 require(str(Path(sys.executable).resolve())==fs[0]['interpreter'],'root interpreter')
 for m in list(sys.modules.values()):
  n=getattr(m,'__file__',None)
  if n:
   n=str(Path(n).resolve())
   if n==str(R/'run_once.py'):require(sha(n)==rf['files']['run_once.py'],'root main')
   else:require(n in fs[0]['inputs'] and sha(n)==fs[0]['inputs'][n],'root origin '+n)
 require(sha(P/'ROOT_AUTHORIZATION.json')==rf['production_authorization_sha256'],'fixed authorization hash');a=json.loads((P/'ROOT_AUTHORIZATION.json').read_text());require(a.get('authorized') is True and a.get('source_freeze')==PF and a.get('contract_sha256')==CH,'authorization')
 return fs

def parse_time(text,cap):
 walls=re.findall(r'^real\s+([0-9.]+)\s*$',text,re.M);high=re.findall(r'^\s*(\d+)\s+maximum resident set size\s*$',text,re.M)
 require(bool(walls) and bool(high),'time fields');wall=float(walls[-1]);rss=int(high[-1]);require(math.isfinite(wall) and 0<wall<cap and 0<rss<=LIMIT,'external resource');return wall,rss

def stage(name,cmd,cap):
 began=time.monotonic();p=None;known={os.getpid()};peak=0;perpid={};failure=None;rc=None
 write(R/(name+'.STARTED.json'),{'utc':time.time(),'command':cmd,'cap':cap})
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',NUMEXPR_NUM_THREADS='1')
 try:
  with (R/(name+'.stdout')).open('x') as out,(R/(name+'.stderr')).open('x') as err:
   p=subprocess.Popen(['/usr/bin/time','-lp']+cmd,stdout=out,stderr=err,env=env,start_new_session=True);known.add(p.pid)
   while p.poll() is None:
    rows=[tuple(map(int,l.split())) for l in subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3).splitlines() if len(l.split())==3];ids={os.getpid(),p.pid}
    while True:
     new=ids|{pid for pid,ppid,rss in rows if ppid in ids}
     if new==ids:break
     ids=new
    known|=ids;resident=sum(rss*1024 for pid,ppid,rss in rows if pid in ids)
    for pid,ppid,rss in rows:
     if pid in ids:perpid[pid]=max(perpid.get(pid,0),rss*1024)
    if resident>peak:
     peak=resident;write(R/(name+'.PEAK.json'),{'rss_bytes':peak,'processes':[{'pid':pid,'ppid':ppid,'rss_bytes':rss*1024} for pid,ppid,rss in rows if pid in ids],'per_pid_highwater':perpid})
    require(time.monotonic()-START<345.5,'aggregate watchdog');require(time.monotonic()-began<cap,'stage watchdog');require(resident<=LIMIT,'aggregate RSS');time.sleep(.02)
   rc=p.wait();require(rc==0,'child exit '+str(rc))
 except BaseException as e:failure=repr(e)
 finally:
  if p is not None:
   if failure or p.poll() is None:
    try:os.killpg(p.pid,signal.SIGKILL)
    except ProcessLookupError:pass
    for pid in known-{os.getpid()}:
     try:os.kill(pid,signal.SIGKILL)
     except ProcessLookupError:pass
   rc=p.wait()
 elapsed=time.monotonic()-began;wall=rss=None
 try:wall,rss=parse_time((R/(name+'.stderr')).read_text(),cap)
 except BaseException as e:failure=failure or repr(e)
 okay=failure is None and rc==0 and 0<elapsed<cap and 0<peak<=LIMIT
 write(R/(name+'.RECEIPT.json'),{'pass':okay,'error':failure,'returncode':rc,'seconds':elapsed,'external_seconds':wall,'external_rss':rss,'aggregate_peak':peak,'per_pid_highwater':perpid});require(okay,'failed '+name)

def bridge(npy,raw,phase):
 with npy.open('rb') as f,raw.open('rb') as g:
  require(f.read(6)==b'\x93NUMPY','NPY magic');version=f.read(2);require(version in (b'\x01\x00',b'\x02\x00'),'NPY version');width=2 if version[0]==1 else 4;length=int.from_bytes(f.read(width),'little');require(length<65536,'header bound');header=ast.literal_eval(f.read(length).decode('latin1'));require(header=={'descr':'<f8','fortran_order':False,'shape':(1<<20,)},'NPY schema')
  for lo in range(0,1<<20,4096):
   a=f.read(8*4096);b=g.read(16*4096);require(len(a)==8*4096 and len(b)==16*4096,'bridge length')
   for j in range(4096):
    left=b[16*j:16*j+8];right=b[16*j+8:16*j+16];require((left==a[8*j:8*j+8] and right==b'\0'*8) if phase=='real' else (right==a[8*j:8*j+8] and left==b'\0'*8),'bit bridge')
  require(not f.read(1) and not g.read(1),'trailing bytes')

def production_check():
 folder=O/'production';r=json.loads((folder/'RESULT.json').read_text());c=json.loads((folder/'WORKER_COMPLETE.json').read_text())
 require(r['algorithm']=='direct_gaussian_once' and r['passes_Echi'] is True,'production science')
 require(type(c['seconds']) in (int,float) and math.isfinite(c['seconds']) and 0<c['seconds']<180 and type(c['rss_bytes']) is int and 0<c['rss_bytes']<=LIMIT,'worker resource fields')
 require(c['status']=='PRODUCTION_ONLY_COMPLETE' and c['source_freeze']==PF and c['contract_sha256']==CH and c['result_sha256']==sha(folder/'RESULT.json'),'worker receipt')
 finals={'firstP','firstO','secondP','secondO','sourceP','sourceO','chi_real'};expected={n+'.npy' for n in finals}|{n+'_1.npy' for n in ('firstP','firstO','secondP','secondO')}
 rows=r['vector_manifest'];require(len(rows)==11 and {x['file'] for x in rows}==expected,'11 saved arrays');require({q.name for q in folder.glob('*.npy')}==expected,'NPY membership')
 for row in rows:
  name=row['file'];require(sha(folder/name)==row['sha256'],'NPY hash')
  if Path(name).stem in finals:
   phase='real' if name.startswith('first') else 'i';raw=folder/(Path(name).stem+'.bin');meta=row['raw'];require(meta['phase']==phase and meta['entries']==1<<20 and meta['bytes']==raw.stat().st_size==16*(1<<20) and meta['sha256']==sha(raw),'raw hash/schema');bridge(folder/name,raw,phase)
 return r

def snapshot():return {str(q.relative_to(O/'production')):sha(q) for q in sorted((O/'production').rglob('*')) if q.is_file()}
def timeout(sig,frame):raise TimeoutError('aggregate internal root deadline')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['preflight','launch']);args=ap.parse_args();require(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site,'-I -B -S');fs=pins()
 if args.mode=='preflight':print(json.dumps({'status':'PASS','physical_calls':0,'parser_origins':True}));return
 require(not O.exists(),'fresh output')
 with (R/'LAUNCH_STARTED.json').open('x') as f:json.dump({'utc':time.time(),'production':PF,'replay':QF,'prior':14,'aggregate':360,'no_retries':True},f)
 O.mkdir();authhash=sha(P/'ROOT_AUTHORIZATION.json');signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,max(.001,345.5-(time.monotonic()-START)))
 try:
  stage('production',[fs[0]['interpreter'],'-I','-B',str(P/'run.py'),'run',str(O/'production')],180);pins();result=production_check();before=snapshot();write(R/'PRODUCTION_MEMBERSHIP.json',before)
  binding=R/'REPLAY_BINDING.json';write(binding,{'result_sha256':sha(O/'production/RESULT.json'),'worker_complete_sha256':sha(O/'production/WORKER_COMPLETE.json'),'production_source_freeze':PF,'production_contract_sha256':CH})
  stage('replay',[fs[1]['interpreter'],'-I','-B',str(Q/'run.py'),'replay',str(O/'production'),str(O/'replay'),str(binding)],150);pins();require(before==snapshot(),'production mutation');review=json.loads((O/'replay/REVIEW.json').read_text())
  require(review['status']=='PASS' and review['scientific_pass'] is True and review['source_freeze']==QF and review['input_binding_sha256']==sha(binding) and review['input_result_sha256']==sha(O/'production/RESULT.json') and review['worker_complete_sha256']==sha(O/'production/WORKER_COMPLETE.json'),'replay receipt')
  require(type(review['seconds']) in (int,float) and math.isfinite(review['seconds']) and 0<review['seconds']<150 and type(review['rss_bytes']) is int and 0<review['rss_bytes']<=LIMIT,'replay resource fields')
  require(review['Echi']==result['Echi'] and review['particle_intervals']==result['particle_intervals'],'science comparison');require(sha(P/'ROOT_AUTHORIZATION.json')==authhash,'authorization changed');require(time.monotonic()-START<346,'final wall')
  write(R/'COMPLETE.json',{'status':'PASS_EXTERNAL_SHELL_PENDING','seconds':time.monotonic()-START,'seconds_with_prior':time.monotonic()-START+14,'production_freeze':PF,'replay_freeze':QF,'review_hash':sha(O/'replay/REVIEW.json'),'external_root_shell_reconciliation_pending':True})
 except BaseException as e:write(R/'FAILED.json',{'error':repr(e),'seconds':time.monotonic()-START,'seconds_with_prior':time.monotonic()-START+14});raise
if __name__=='__main__':main()
