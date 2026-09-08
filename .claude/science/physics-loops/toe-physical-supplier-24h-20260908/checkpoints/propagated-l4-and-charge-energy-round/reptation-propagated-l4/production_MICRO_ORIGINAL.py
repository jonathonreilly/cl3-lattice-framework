import os,sys,time,signal,resource,json,argparse,hashlib
from pathlib import Path
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
start=time.monotonic()
import numpy as np
from initialize import initialize
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--cell',type=int,choices=range(4),default=0);ap.add_argument('--shard',type=int,choices=range(16),default=0);ap.add_argument('--micro',action='store_true');args=ap.parse_args();signal.alarm(30 if args.micro else 180)
cells=[(12,128,32),(12,512,32),(36,512,8),(36,512,32)];tau,rks,burn=cells[args.cell];n=13824 if args.micro else 384*tau;updates=4096 if args.micro else 32*n;burn=0 if args.micro else burn;rks=128 if args.micro else rks;rows=[];init_total=0;hot_total=0
for rep in range(1 if args.micro else 2):
 cid=32*args.cell+2*args.shard+rep;seed=202609199999 if args.micro else 202609190000+cid;rng=np.random.default_rng(seed);t=time.monotonic();a,initmeta=initialize(4,n,np.random.default_rng(202609209999 if args.micro else 202609200000+cid),rks);init_total+=time.monotonic()-t;batch=np.zeros((16,9));c=dict(self_proposals=0,rejections=0,accepted=0,accepted_self=0);runs=[];run=0;u=lo=hi=0;tagged=0;first_escape=None;burn_tags=None;t=time.monotonic()
 for step in range(burn*n+updates):
  direction=a.direction;f,ok=a.step(rng)
  if ok:u+=direction;lo=min(lo,u);hi=max(hi,u)
  retained=max(0,n+lo-hi+1);is_tagged=hi<=u+n//2<=n+lo
  if not is_tagged and first_escape is None:first_escape=step+1
  if step+1==burn*n:burn_tags=retained
  if ok:run+=1
  else:runs.append(run);run=0
  if step>=burn*n:
   c['self_proposals']+=int(f<0);c['rejections']+=int(not ok);c['accepted']+=int(ok);c['accepted_self']+=int(ok and f<0)
   tagged+=int(is_tagged);o=a.O[1];x1=float(np.vdot(o[:6],o[:6]).real);x2=float(np.vdot(o[6:],o[6:]).real);hl=-.05*a.nf[0];hr=-.05*a.nf[2];e=(hl+hr)/2;v=[a.nf[1],x1,x2,e,hl*hr,x1*e,x2*e,x1*x1,x2*x2];batch[(step-burn*n)//(updates//16)]+=v
 hot_total+=time.monotonic()-t
 # Direct final caches, without retaining a production full path.
 from core import count
 for j,x in enumerate(a.states):
  if a.nf[j]!=count(x,a.faces) or np.max(abs(a.O[j]-a.coeff@(x.astype(float)-.5)))>1e-9:raise RuntimeError('final cache drift')
 c.update(run_lengths_including_burn=runs,unfinished_run=run,window_traversals_including_burn=sum(z//n for z in runs+[run]))
 rows.append(dict(cid=cid,seed=seed,initializer=initmeta,memory=dict(tagged_measurements=tagged,fraction=tagged/updates,burn_end_tags=burn_tags,final_tags=retained,first_escape=first_escape,u=u,lo=lo,hi=hi),mean=(batch.sum(0)/updates).tolist(),batch_means=(batch/(updates//16)).tolist(),counters=c))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<384 or time.monotonic()-start>=(30 if args.micro else 180):raise RuntimeError('resources')
out=dict(micro=args.micro,cell=args.cell,shard=args.shard,L=4,V=.95,harmonics=[1,2],n=n,tau=36 if args.micro else tau,rk_sweeps=rks,burn_multiplier=burn,updates=updates,chains=len(rows),rows=rows,initialization_seconds=init_total,hot_seconds=hot_total,seconds=time.monotonic()-start,rss_mib=rss,source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),core_sha=hashlib.sha256((p/'core.py').read_bytes()).hexdigest(),initializer_sha=hashlib.sha256((p/'initialize.py').read_bytes()).hexdigest());print(json.dumps(out,indent=2,allow_nan=False))
