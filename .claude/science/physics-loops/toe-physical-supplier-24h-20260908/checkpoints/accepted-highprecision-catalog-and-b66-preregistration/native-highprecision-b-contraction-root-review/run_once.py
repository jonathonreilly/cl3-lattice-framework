import time
START=time.monotonic()
import sys,os,json,hashlib,subprocess,signal,argparse,types
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'native-highprecision-b-contraction-design';O=R.parent/'native-highprecision-b-contraction-study';LIMIT=384*1048576

def req(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
def pins(full=True):
 rf=json.loads((R/'ROOT_FREEZE.json').read_text())
 for k,v in rf['files'].items():req(sha(R/k)==v,'root source '+k)
 b=json.loads((R/'ROOT_BINDING.json').read_text());req(b['worker_freeze'] is not None and b['binding_sha256'] is not None,'final input binding pending');req(sha(P/'RUNTIME_FREEZE.json')==b['worker_freeze'] and sha(P/'BINDING.json')==b['binding_sha256'],'worker/binding source')
 f=json.loads((P/'RUNTIME_FREEZE.json').read_text());req(f['binding_sha256']==b['binding_sha256'],'bound accepted input');req(str(Path(sys.executable).resolve())==f['interpreter'],'interpreter')
 if full:
  for k,v in f['inputs'].items():req(sha(k)==v,'input '+k)
 for m in list(sys.modules.values()):
  x=getattr(m,'__file__',None)
  if x:
   x=str(Path(x).resolve())
   if Path(x).parent==R:req(Path(x).name in rf['files'] and sha(x)==rf['files'][Path(x).name],'root loaded '+x)
   else:req(x in f['inputs'] and sha(x)==f['inputs'][x],'loaded '+x)
 binding=json.loads((P/'BINDING.json').read_text());req(binding['shards']==[list(range(6*j,6*j+6)) for j in range(11)],'fixed schedule')
 return b,f,binding

def main():
 ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['readiness','launch']);a=ap.parse_args();req(sys.flags.isolated and sys.dont_write_bytecode and sys.flags.no_site,'-I -B -S')
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('inclusive stage/study deadline')));signal.setitimer(signal.ITIMER_REAL,max(.001,1199.5-(time.monotonic()-START)))
 b,f,inputs=pins();data=(R/'schema.py').read_bytes();req(hashlib.sha256(data).hexdigest()==json.loads((R/'ROOT_FREEZE.json').read_text())['files']['schema.py'],'schema bytes');ns=types.ModuleType('schema');ns.__file__=str(R/'schema.py');exec(compile(data,ns.__file__,'exec'),ns.__dict__)
 if a.mode=='readiness':pins();print(json.dumps({'status':'PASS_SOURCE_READINESS','physical_calls':0}));return
 req(not O.exists(),'fresh study')
 with (R/'STARTED.json').open('x') as mark:json.dump({'start_epoch':time.time(),'seconds':1200,'rss_bytes':LIMIT,'worker_freeze':b['worker_freeze'],'binding_sha256':b['binding_sha256'],'no_retry':True},mark)
 O.mkdir();states=[{'shard':j,'status':'UNSTARTED'} for j in range(11)];accepted=[];stages=[];peak=0;failure=None;current=None
 def receipt():write(R/'PROGRESS.json',{'states':states,'stages':stages,'seconds':time.monotonic()-START,'peak_bytes':peak,'current':current})
 def child(command,label,cap):
  nonlocal peak
  start=time.monotonic();p=None;rc=None;err=None;localpeak=0;record={'stage':label,'status':'RUNNING'};stages.append(record);receipt()
  try:
   with (R/(label+'.stdout')).open('x') as out,(R/(label+'.stderr')).open('x') as error:
    p=subprocess.Popen(command,stdout=out,stderr=error,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),start_new_session=True)
    while p.poll() is None:
     lines=subprocess.check_output(['/bin/ps','-axo','pid=,ppid=,rss='],text=True,timeout=.3);rows=[tuple(map(int,l.split())) for l in lines.splitlines() if len(l.split())==3];ids={os.getpid(),p.pid}
     while True:
      nxt=ids|{pid for pid,ppid,rss in rows if ppid in ids}
      if nxt==ids:break
      ids=nxt
     rss=sum(mem*1024 for pid,ppid,mem in rows if pid in ids);localpeak=max(localpeak,rss);peak=max(peak,rss)
     req(rss<=LIMIT,'whole-tree RSS');req(time.monotonic()-start<cap,'stage deadline');req(time.monotonic()-START<1199.5,'study deadline');time.sleep(.02)
    rc=p.wait();req(rc==0,'child exit '+str(rc))
  except BaseException as e:err=repr(e)
  finally:
   if p is not None:
    if err or p.poll() is None:
     try:os.killpg(p.pid,signal.SIGKILL)
     except ProcessLookupError:pass
    rc=p.wait()
   record.update(status='FAILED' if err else 'COMPLETE',failure=err,returncode=rc,seconds=time.monotonic()-start,peak_bytes=localpeak);receipt()
  req(err is None,'stage failure '+str(err));req(record['seconds']<=cap+.5,'stage inclusive elapsed');return record['seconds']
 try:
  poles=json.loads(Path(inputs['poles_path']).read_text())['rows']
  for j in range(11):
   current=j;jobstart=time.monotonic();states[j]['status']='RUNNING';receipt();remaining=1199.5-(time.monotonic()-START)-5;req(remaining>0,'summary reserve');cap=min(179.5,remaining);signal.setitimer(signal.ITIMER_REAL,cap);pins(False)
   elapsed=child([f['interpreter'],'-I','-B','-S',str(P/'run.py'),'shard',str(O/f'SHARD_{j:02d}'),'--shard',str(j)],f'SHARD_{j:02d}',cap)
   checked=ns.shard(O/f'SHARD_{j:02d}',j,poles,b['worker_freeze'],b['binding_sha256'],time.monotonic()-jobstart);req(time.monotonic()-jobstart<=180,'inclusive shard validation deadline');signal.setitimer(signal.ITIMER_REAL,max(.001,1199.5-(time.monotonic()-START)));checked['inclusive_seconds']=time.monotonic()-jobstart;accepted.append(checked);states[j].update(status='COMPLETE',all_targets_met=checked['all_targets_met']);write(R/f'SHARD_{j:02d}_ACCEPTANCE.json',checked);receipt()
  current='summary';remaining=1199.5-(time.monotonic()-START);req(remaining>0,'summary time');child([f['interpreter'],'-I','-B','-S',str(R/'summary_worker.py'),str(O),str(O/'SUMMARY.json')],'SUMMARY',min(179.5,remaining));summary=ns.summary(O/'SUMMARY.json',accepted);pins();req(time.monotonic()-START<1199.5,'final study resource');write(O/'COMPLETE.json',{'status':'COMPLETE_FIXED_11_SHARDS','worker_freeze':b['worker_freeze'],'binding_sha256':b['binding_sha256'],'summary_sha256':sha(O/'SUMMARY.json'),'all_targets_met':summary['all_targets_met'],'original_scope':'B66 midpoint scalar contractions only','external_shell_acceptance_pending':True})
 except BaseException as e:
  failure=repr(e)
  if isinstance(current,int) and states[current]['status']=='RUNNING':states[current]['status']='FAILED'
  write(O/'FAILED.json',{'failure':failure,'current':current,'states':states,'unstarted':[x['shard'] for x in states if x['status']=='UNSTARTED']})
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);receipt();write(R/'RECEIPT.json',{'pass':failure is None,'failure':failure,'seconds':time.monotonic()-START,'sampled_whole_tree_peak':peak,'states':states,'stages':stages,'worker_freeze':b['worker_freeze'],'binding_sha256':b['binding_sha256'],'external_whole_shell_receipt_pending':True})
 req(failure is None,'study failed '+str(failure));print(json.dumps({'status':'PASS_EXTERNAL_SHELL_PENDING','seconds':time.monotonic()-START,'peak_bytes':peak}))
if __name__=='__main__':main()
