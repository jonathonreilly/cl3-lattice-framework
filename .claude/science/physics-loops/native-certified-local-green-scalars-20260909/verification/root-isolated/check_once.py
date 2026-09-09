import time
START=time.monotonic()
import sys,json,hashlib,subprocess,signal,os,shutil,resource
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parent; W=Path('/private/tmp/toe-native-certified-local-green-scalars-20260909'); NAME='native_certified_local_green_scalars_2026_09_09'; IN=Path('outputs')/(NAME+'_inputs'); SCRIPT=Path('scripts')/(NAME+'.py'); LIMIT=384*1048576

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
def need(v,msg):
 if not v:raise ValueError(msg)
def alarm(*_):raise TimeoutError('30s controller')
signal.signal(signal.SIGALRM,alarm);signal.alarm(30)
need(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site,'isolated');freeze=json.loads((R/'FREEZE.json').read_text())
for name,h in freeze.items():need(sha(R/name)==h,'controller pin')
with (R/'STARTED.json').open('x') as f:json.dump({'seconds':30,'rss_bytes':LIMIT,'physical_calls':0},f)
source=json.loads((R/'SOURCE_FREEZE.json').read_text());manifest=json.loads((W/IN/'MANIFEST.json').read_text());files=set(source)|set(manifest)
for path,h in {**source,**manifest}.items():need(sha(W/path)==h,'source pin')
base=R/'BASELINE';base.mkdir()
for name in files:
 d=base/name;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/name,d)
peak=0;rows=[]
def call(root,label):
 global peak
 out=R/(label+'.stdout');err=R/(label+'.stderr');start=time.monotonic();proc=None
 try:
  with out.open('x') as o,err.open('x') as e:
   proc=subprocess.Popen([sys.executable,'-I','-B','-S',str(root/SCRIPT),'--json'],stdout=o,stderr=e,start_new_session=True)
   while proc.poll() is None:
    need(time.monotonic()-start<5 and time.monotonic()-START<30,'bounded time')
    ps=[tuple(map(int,line.split())) for line in subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.4).splitlines() if len(line.split())==3];ids={os.getpid(),proc.pid}
    while True:
     new=ids|{a for a,b,c in ps if b in ids}
     if new==ids:break
     ids=new
    rss=sum(c*1024 for a,b,c in ps if a in ids);peak=max(peak,rss);need(rss<=LIMIT,'RSS');time.sleep(.01)
   rc=proc.wait()
  return rc
 finally:
  if proc is not None and proc.poll() is None:os.killpg(proc.pid,signal.SIGKILL);proc.wait()
rc=call(base,'baseline');need(rc==0,'baseline');result=json.loads((R/'baseline.stdout').read_text());need(result['status']=='PASS_SAVED_CERTIFICATE_CHECKS' and result['physical_calls']==result['oracle_calls']==0,'scope')
for label,error in [('missing_width','two widths'),('wrong_target','fixed target'),('positive_derivative','known sign'),('disjoint_methods','independent overlap'),('wrong_completion','accepted execution'),('duplicate_pole','fixed rows')]:
 t=R/label;shutil.copytree(base,t);rp=t/IN/'elliptic_RESULT.json';d=json.loads(rp.read_text());row=d['rows'][3]
 if label=='missing_width':row['widths']=row['widths'][:1]
 elif label=='wrong_target':row['target']='1/1000'
 elif label=='positive_derivative':
  lo,hi=map(F,row['Aprime']);row['Aprime']=[str(-hi),str(-lo)]
 elif label=='disjoint_methods':row['A']=[str(F(x)+F(1,100)) for x in row['A']]
 elif label=='duplicate_pole':row['s']='2'
 save(rp,d);rh=sha(rp)
 for suffix in ['ROOT_ACCEPTANCE','WORKER_COMPLETE']:
  receipt=t/IN/('elliptic_'+suffix+'.json');a=json.loads(receipt.read_text());a['result_sha256']=rh
  if label=='wrong_completion' and suffix=='WORKER_COMPLETE':a['status']='INCOMPLETE'
  save(receipt,a)
 m=json.loads((t/IN/'MANIFEST.json').read_text())
 for path in m:m[path]=sha(t/path)
 save(t/IN/'MANIFEST.json',m)
 rc=call(t,label);stderr=(R/(label+'.stderr')).read_text();need(rc!=0 and ('ValueError: '+error) in stderr,'effective rejection '+label);rows.append({'case':label,'returncode':rc,'actual_rejection':error,'physical_calls':0})
need(0<peak<=LIMIT and time.monotonic()-START<30,'aggregate caps')
save(R/'ROOT_RECEIPT.json',{'status':'PASS','files':len(files),'baseline_checks':result['checks'],'effective_altered_data_rejections':rows,'seconds':time.monotonic()-START,'sampled_whole_tree_peak':peak,'root_rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'physical_evaluations':0,'source_freeze':sha(R/'SOURCE_FREEZE.json')})
print(json.dumps({'status':'PASS','checks':result['checks'],'altered_data_controls':len(rows),'seconds':time.monotonic()-START,'rss':peak}));signal.alarm(0)
