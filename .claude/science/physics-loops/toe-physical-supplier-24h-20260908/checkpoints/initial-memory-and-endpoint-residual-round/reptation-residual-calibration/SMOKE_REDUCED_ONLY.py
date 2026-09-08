import os,sys,time,signal,resource,pathlib,json,argparse,hashlib
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
t=time.monotonic();signal.alarm(30);sys.dont_write_bytecode=True
import numpy as np
p=pathlib.Path(__file__).resolve().parent;sys.path.insert(0,str(p.parent/'detuned-reptation-l2'));import graph as g
ap=argparse.ArgumentParser();ap.add_argument('--shard',type=int,choices=range(4),required=True);args=ap.parse_args();rows=[]
for rep in range(1):
 cid=args.shard*8+rep;rng=np.random.default_rng(202609180000+cid);path=[0]*3;direction=1;batch=np.zeros((1,6));counts=dict(accepted=0,rejected=0,self_proposals=0,accepted_self=0)
 for step in range(64+64):
  old=path[-1] if direction==1 else path[0];second=path[1];u=rng.random()*(24+.05*g.nf[old]);f=int(u) if u<24 else -1;y=g.T[old,f] if f>=0 else -1;selfmove=y<0;y=y if y>=0 else old;ok=rng.random()<min(1,g.b[old]/g.b[second])
  if ok:path=path[1:]+[int(y)] if direction==1 else [int(y)]+path[:-1]
  else:direction=-direction
  if step>=64:
   mid=path[1];x=g.S[mid];hl=-.05*g.nf[path[0]];hr=-.05*g.nf[path[-1]];e=(hl+hr)/2;batch[(step-64)//64]+=[g.nf[mid],x,e,hl*hr,x*e,x*x];counts['accepted']+=int(ok);counts['rejected']+=int(not ok);counts['self_proposals']+=int(selfmove);counts['accepted_self']+=int(ok and selfmove)
 rows.append(dict(cid=cid,seed=202609180000+cid,mean=(batch.sum(0)/64).tolist(),batch_means=(batch/64).tolist(),counts=counts))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
if not 0<rss<384 or time.monotonic()-t>=180:raise RuntimeError('resources')
print(json.dumps(dict(smoke_only=True,shard=args.shard,V=.95,n=2,burn=64,chains=1,updates=64,rows=rows,seconds=time.monotonic()-t,rss_mib=rss,source_sha=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),graph_sha=hashlib.sha256(pathlib.Path(g.__file__).read_bytes()).hexdigest()),indent=2,allow_nan=False))
