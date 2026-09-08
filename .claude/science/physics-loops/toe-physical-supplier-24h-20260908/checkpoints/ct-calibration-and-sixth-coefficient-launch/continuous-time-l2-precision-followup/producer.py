import time,json,random,signal,sys,resource
from pathlib import Path
import config
from preflight import verify,sha
from runtime import Runtime,Variates,NAMES

def chain(r,a,c,out):
 start=time.monotonic();rng=random.Random(config.seed(a['arm'],c));v=Variates(rng.getrandbits)
 if a['start']=='constant':path=r.seed(a['T']);init=dict(auxiliary_count=0,physical_events=0,scope='constant nonequilibrated seed path')
 else:path,init=r.stationary_truncated(a['T'],v)
 init['state_hex']=hex(path.initial);init['state_sha']=sha_bytes(path.initial);init_seconds=time.monotonic()-start
 rows=[];hist=[0]*24;burn_hist=[0]*24;measured_hist=[0]*24;selected=0;tape=0;error=0.;maxevents=len(path.events);completed=0
 try:
  for sweep in range(a['burn']+config.MEASURED):
   for _ in range(24):
    p=v.randbelow(24);path,rec=r.block(path,p,v);hist[p]+=1;completed+=1
    (burn_hist if sweep<a['burn'] else measured_hist)[p]+=1
    selected+=rec['selected_events'];tape+=rec['tape_used'];error+=rec['sum_local_bracket_widths'];maxevents=max(maxevents,len(path.events))
   if sweep>=a['burn']:
    measured=r.measure(path);rows.append([measured[n] for n in NAMES])
  file=out/f'chain{c}.path.json';r.save(path,file);back=r.load(file)
  if back.events!=path.events or back.initial!=path.initial or r.measure(back)!=r.measure(path):raise ValueError('lossless final path')
  batches=[[sum(rows[k][j] for k in range(i,i+16))/16 for j in range(12)] for i in range(0,config.MEASURED,16)]
  return dict(chain=c,seed=config.seed(a['arm'],c),arm=a,raw_names=NAMES,rows=rows,batch_means=batches,face_histogram=hist,burn_face_histogram=burn_hist,measured_face_histogram=measured_hist,completed_blocks=completed,selected_events_sum=selected,tape_used_sum=tape,bracket_width_sum=error,max_path_events=maxevents,numerical_failures=0,initialization=init,initialization_seconds=init_seconds,final_path=file.name,final_path_sha=sha(file),seconds=time.monotonic()-start,bit_calls=v.bit_calls)
 except BaseException as e:
  (out/f'chain{c}.failure.json').write_text(json.dumps(dict(chain=c,arm=a,completed_blocks=completed,rows=rows,face_histogram=hist,burn_face_histogram=burn_hist,measured_face_histogram=measured_hist,error_type=type(e).__name__,error=str(e),numerical_failures=1)))
  raise

def sha_bytes(x):
 import hashlib
 return hashlib.sha256(x.to_bytes(3,'little')).hexdigest()
def main():
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('175s internal cap')));signal.alarm(175);start=time.monotonic()
 if len(sys.argv)!=4:raise ValueError('arm shard fresh_dir')
 a=int(sys.argv[1]);s=int(sys.argv[2]);out=Path(sys.argv[3])
 if not 0<=a<4 or not 0<=s<16:raise ValueError('job domain')
 freeze=verify();out.mkdir(parents=False,exist_ok=False);r=Runtime();rows=[]
 try:
  for c in range(s*4,s*4+4):rows.append(chain(r,config.ARMS[a],c,out))
  rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576
  if rss>384:raise ValueError('observed RSS')
  result=dict(freeze=freeze,arm=a,shard=s,chains=rows,seconds=time.monotonic()-start,rss_mib=rss)
  (out/'RESULT.json').write_text(json.dumps(result,allow_nan=False)+'\n');print(json.dumps(dict(result_sha=sha(out/'RESULT.json'),seconds=result['seconds'],rss_mib=rss)))
 except BaseException as e:
  (out/'FAILURE.json').write_text(json.dumps(dict(type=type(e).__name__,error=str(e),completed_chains=len(rows))))
  raise
if __name__=='__main__':main()
