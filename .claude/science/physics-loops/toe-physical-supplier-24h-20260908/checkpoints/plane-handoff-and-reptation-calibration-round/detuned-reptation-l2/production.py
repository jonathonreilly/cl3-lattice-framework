import os,sys,time,signal,resource,json,argparse,hashlib
from pathlib import Path
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
start=time.monotonic();signal.alarm(180)
import numpy as np
import graph as g
from initializer import powers,initialize
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--cell',type=int,choices=range(9),required=True);args=ap.parse_args()
cells=[(48,8),(48,32),(48,0),(192,8),(192,32),(192,0),(768,8),(768,32),(768,0)];bonds,mult=cells[args.cell];means=[];batches=[];counts=[]
psi,scales=powers(bonds) if mult==0 else (None,None)
for rep in range(32):
 cid=args.cell*32+rep;rng=np.random.default_rng(202609120000+cid);init_rng=np.random.default_rng(202609130000+cid);buf=initialize(bonds,init_rng,psi) if mult==0 else np.zeros(bonds+1,int);head=0;direction=(1 if init_rng.random()<.5 else -1) if mult==0 else 1;batch=np.zeros((16,3));c=dict(cid=cid,self_proposals=0,accepted_self=0,rejections=0,accepted=0,window_traversals=0);run=0;runlengths=[]
 for step in range(mult*bonds+65536):
  old=buf[(head+bonds)%(bonds+1)] if direction==1 else buf[head];second=buf[(head+1)%(bonds+1)] if direction==1 else buf[(head+bonds-1)%(bonds+1)]
  u=rng.random()*(24+.05*g.nf[old]);f=int(u) if u<24 else -1;y=g.T[old,f] if f>=0 else -1;label=f if y>=0 else -1;y=y if y>=0 else old;accept=rng.random()<min(1,g.b[old]/g.b[second])
  if accept:
   if direction==1:buf[head]=y;head=(head+1)%(bonds+1)
   else:head=(head-1)%(bonds+1);buf[head]=y
   run+=1
  else:direction=-direction;runlengths.append(run);run=0
  if step>=mult*bonds:
   c['self_proposals']+=int(label<0);c['accepted_self']+=int(label<0 and accept);c['rejections']+=int(not accept);c['accepted']+=int(accept)
   mid=buf[(head+bonds//2)%(bonds+1)];batch[(step-mult*bonds)//4096]+=[g.nf[mid],g.S[mid],-.05*(g.nf[buf[head]]+g.nf[buf[(head+bonds)%(bonds+1)]])/2]
 # Runs intentionally cover burn+measurement; counters explicitly measurement only.
 c['window_traversals']=sum(k//bonds for k in runlengths+[run]);c['run_lengths_including_burn']=runlengths;c['unfinished_run']=run
 means.append((batch.sum(0)/65536).tolist());batches.append((batch/4096).tolist());counts.append(c)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<384 or time.monotonic()-start>=180:raise RuntimeError('resource')
print(json.dumps(dict(cell=args.cell,n=bonds,burn_multiplier=mult,chains=32,updates=65536,batches=16,means=means,batch_means=batches,counters=counts,seconds=time.monotonic()-start,rss_mib=rss,source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),graph_sha=hashlib.sha256((p/'graph.py').read_bytes()).hexdigest(),initializer_sha=hashlib.sha256((p/'initializer.py').read_bytes()).hexdigest()),indent=2,allow_nan=False))
