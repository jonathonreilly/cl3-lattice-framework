import os,sys,time,signal,resource,json,argparse,hashlib
from pathlib import Path
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
start=time.monotonic()
import numpy as np
from core import Path as Chain
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--cell',type=int,choices=range(6),default=0);ap.add_argument('--shard',type=int,choices=range(16),default=0);ap.add_argument('--micro',action='store_true');args=ap.parse_args();signal.alarm(30 if args.micro else 180)
cells=[(4,8),(4,32),(12,8),(12,32),(36,8),(36,32)];tau,burn=cells[args.cell];n=384 if args.micro else 384*tau;updates=4096 if args.micro else 64*n;burn=0 if args.micro else burn;rows=[];init_total=0;hot_total=0
for rep in range(1 if args.micro else 2):
 cid=32*args.cell+2*args.shard+rep;seed=202609169999 if args.micro else 202609160000+cid;rng=np.random.default_rng(seed);t=time.monotonic();a=Chain(4,n,(1,2));init_total+=time.monotonic()-t;batch=np.zeros((16,4));c=dict(self_proposals=0,rejections=0,accepted=0,accepted_self=0);runs=[];run=0;t=time.monotonic()
 for step in range(burn*n+updates):
  f,ok=a.step(rng)
  if ok:run+=1
  else:runs.append(run);run=0
  if step>=burn*n:
   c['self_proposals']+=int(f<0);c['rejections']+=int(not ok);c['accepted']+=int(ok);c['accepted_self']+=int(ok and f<0)
   o=a.O[1];v=[a.nf[1],float(np.vdot(o[:6],o[:6]).real),float(np.vdot(o[6:],o[6:]).real),-.05*(a.nf[0]+a.nf[2])/2];batch[(step-burn*n)//(updates//16)]+=v
 hot_total+=time.monotonic()-t
 # Direct final caches, without retaining a production full path.
 from core import count
 for j,x in enumerate(a.states):
  if a.nf[j]!=count(x,a.faces) or np.max(abs(a.O[j]-a.coeff@(x.astype(float)-.5)))>1e-9:raise RuntimeError('final cache drift')
 c.update(run_lengths_including_burn=runs,unfinished_run=run,window_traversals_including_burn=sum(z//n for z in runs+[run]))
 rows.append(dict(cid=cid,seed=seed,mean=(batch.sum(0)/updates).tolist(),batch_means=(batch/(updates//16)).tolist(),counters=c))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<384 or time.monotonic()-start>=(30 if args.micro else 180):raise RuntimeError('resources')
out=dict(micro=args.micro,cell=args.cell,shard=args.shard,L=4,V=.95,harmonics=[1,2],n=n,tau=1 if args.micro else tau,burn_multiplier=burn,updates=updates,chains=len(rows),rows=rows,initialization_seconds=init_total,hot_seconds=hot_total,seconds=time.monotonic()-start,rss_mib=rss,source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),core_sha=hashlib.sha256((p/'core.py').read_bytes()).hexdigest());print(json.dumps(out,indent=2,allow_nan=False))
