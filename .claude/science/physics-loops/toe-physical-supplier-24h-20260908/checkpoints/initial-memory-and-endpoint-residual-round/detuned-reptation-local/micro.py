import os,sys,time,signal,resource,json,pathlib,hashlib,importlib.util
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
start=time.monotonic();signal.alarm(60);sys.dont_write_bytecode=True
import numpy as np
from core import Path,count,flip
p=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('exact_reference',p.parent/'detuned-reptation-l2/graph.py');g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
def need(c,s):
 if not c:raise RuntimeError(s)
# L2 independent exact-graph event stream, same random numbers and face order.
a=Path(2,192);rng=np.random.default_rng(202609140201);rr=np.random.default_rng(202609140201);ids=[0]*193;direction=1
for step in range(256):
 old=ids[-1] if direction==1 else ids[0];second=ids[1] if direction==1 else ids[-2];u=rr.random()*(24+.05*g.nf[old]);f=int(u) if u<24 else -1;y=g.T[old,f] if f>=0 else -1;label=f if y>=0 else -1;y=y if y>=0 else old;accepted=rr.random()<min(1,g.b[old]/g.b[second])
 got=a.step(rng);need(got==(label,accepted),'L2 event')
 if accepted:ids=ids[1:]+[int(y)] if direction==1 else [int(y)]+ids[:-1]
 else:direction=-direction
 need(a.direction==direction,'L2 direction')
 for state,idx in zip(a.states,[ids[0],ids[96],ids[-1]]):need(sum(int(z)<<j for j,z in enumerate(state))==g.states[idx],'L2 state')
# Single authorized L4 micro with literal full path maintained separately.
a=Path(4,384);rng=np.random.default_rng(202609140401);rr=np.random.default_rng(202609140401);full=[a.states[0].copy() for _ in range(385)];direction=1;reject=0;selfmoves=0;maxdrift=0.;fullchecks=0;t=time.monotonic()
def directnf(x):
 return sum(int(x[f[0]]==x[f[2]] and x[f[1]]==x[f[3]] and x[f[0]]!=x[f[1]]) for f in a.faces)
for step in range(4096):
 old=full[-1] if direction==1 else full[0];second=full[1] if direction==1 else full[-2];nn=directnf(old);u=rr.random()*(192+.05*nn);f=int(u) if u<192 else -1
 label=f if f>=0 and old[a.faces[f,0]]==old[a.faces[f,2]] and old[a.faces[f,1]]==old[a.faces[f,3]] and old[a.faces[f,0]]!=old[a.faces[f,1]] else -1
 accepted=rr.random()<min(1,(1+.05*nn/192)/(1+.05*directnf(second)/192));need(a.step(rng)==(label,accepted),'L4 event')
 if accepted:
  y=old.copy()
  if label>=0:y[a.faces[label]]^=1
  full=full[1:]+[y] if direction==1 else [y]+full[:-1]
 else:direction=-direction;reject+=1
 selfmoves+=label<0;need(a.direction==direction,'direction')
 for k,x in enumerate([full[0],full[192],full[-1]]):
  need(np.array_equal(a.states[k],x) and a.nf[k]==directnf(x),'state/Nf drift');drift=np.max(abs(a.O[k]-a.coeff@(x.astype(float)-.5)));maxdrift=max(maxdrift,float(drift));need(drift<1e-11,'complex cache drift')
 if step%64==0:
  x=a.states[0].copy()
  for j,label0 in enumerate(np.roll(a.labels,-a.head)):
   x=flip(x,int(label0),a.faces);need(np.array_equal(x,full[j+1]),'full label reconstruction')
  fullchecks+=1
hot=time.monotonic()-t;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);need(rss<384 and time.monotonic()-start<60,'resources')
np.savez_compressed(p/'MICRO_RAW.npz',labels=np.roll(a.labels,-a.head),left=a.states[0],mid=a.states[1],right=a.states[2],Nf=a.nf,O=a.O)
print(json.dumps(dict(mode='nonequilibrated local-port diagnostic',L2_events=256,L4_updates=4096,seed=202609140401,n=384,tau=1,rejections=reject,self_proposals=int(selfmoves),max_complex_drift=maxdrift,full_reconstructions=fullchecks,hot_seconds=hot,seconds=time.monotonic()-start,rss_mib=rss),indent=2))
