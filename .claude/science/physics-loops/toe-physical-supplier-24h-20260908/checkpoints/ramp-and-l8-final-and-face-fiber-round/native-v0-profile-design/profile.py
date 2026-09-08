import time,signal
MODULE_START=time.monotonic()
if __name__=="__main__":signal.alarm(30)
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import pathlib,json,hashlib,signal,resource,sys,argparse
import numpy as np
from initialize import initialize
from checkpoint import save,load
from observables import OrderMenu
P=pathlib.Path(__file__).parent
def req(c,m):
 if not c:raise ValueError(m)
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def accumulator():return dict(step=0,snapshots=0,batch=np.zeros((4,154)).tolist(),self_proposals=0,rejections=0,accepted=0,accepted_self=0,runs=[],run=0,u=0,lo=0,hi=0,tagged_snapshots=0,raw=[])
def vector(a,menu):
 o=a.O[1];s1=float(np.vdot(o[:6],o[:6]).real);s2=float(np.vdot(o[6:],o[6:]).real) if len(o)>6 else 0.;hl=(a.V-1)*a.nf[0];hr=(a.V-1)*a.nf[2];e=(hl+hr)/2
 return np.concatenate([[a.nf[1],s1,s2,e,hl*hr,s1*e,s2*e,s1*s1,s2*s2],menu.vector(a.states[1])])
def advance(a,r,s,menu,stop,warmup=4096,measured=24576):
 M=3*menu.N;req(0<=s['step']<=stop<=warmup+measured,'step interval');batch=np.array(s['batch'])
 for t in range(s['step'],stop):
  d=a.direction;f,ok=a.step(r);s['self_proposals']+=int(f<0);s['rejections']+=int(not ok);s['accepted']+=int(ok);s['accepted_self']+=int(ok and f<0)
  if ok:s['u']+=d;s['lo']=min(s['lo'],s['u']);s['hi']=max(s['hi'],s['u']);s['run']+=1
  else:s['runs'].append(s['run']);s['run']=0
  # Half-open attempts t in [warmup,warmup+measured); sample after each M completed attempts.
  completed=t+1-warmup
  if completed>0 and completed%M==0:
   q=vector(a,menu);j=s['snapshots'];req(j<16,'snapshot count');batch[j//4]+=q;s['raw'].append(q.tolist());s['snapshots']+=1;s['tagged_snapshots']+=int(s['hi']<=s['u']+a.n//2<=a.n+s['lo'])
 s['step']=stop;s['batch']=batch.tolist();return s

def verify():
 f=json.loads((P/'FINAL_FREEZE.json').read_text())
 for n,h in f.items():req(sha(P/n)==h,'source freeze '+n)
 r=json.loads((P/'RUNTIME.json').read_text());req(sys.version==r['python'],'python')
 for n,h in r['files'].items():req(sha(n)==h,'runtime '+n)
 return sha(P/'FINAL_FREEZE.json')
def profile(out):
 freeze=verify();out=pathlib.Path(out);req(not out.exists(),'fresh output');out.mkdir(parents=True);rows=[]
 for idx,V in enumerate((.95,0.)):
  L=8;n=110592;begin=time.monotonic();a,im=initialize(L,n,np.random.default_rng(202609290100+idx),V,2048);init=time.monotonic()-begin;menu=OrderMenu(L);r=np.random.default_rng(202609290200+idx);s=accumulator()
  t=time.monotonic();advance(a,r,s,menu,4096);warm=time.monotonic()-t;t=time.monotonic();advance(a,r,s,menu,4096+8192);first=time.monotonic()-t
  req(s['snapshots']==5 and s['step']-4096-5*1536==512,'checkpoint cadence')
  t=time.monotonic();file=out/f'case{idx}.npz';save(file,a,r,L,s);b,rr,ss=load(file,expected=dict(L=L,n=n,V=V));req(ss==s and rr.bit_generator.state==r.bit_generator.state,'checkpoint accumulator/RNG');req(np.array_equal(a.labels,b.labels) and a.head==b.head and a.direction==b.direction,'checkpoint ring');a,r,s=b,rr,ss;io=time.monotonic()-t
  t=time.monotonic();advance(a,r,s,menu,4096+24576);last=time.monotonic()-t;req(s['snapshots']==16,'final snapshots');req(np.max(abs(np.array(s['batch']).sum(0)-np.array(s['raw']).sum(0)))<1e-8,'batch sum')
  rows.append(dict(V=V,L=L,n=n,initializer=im,initialization_seconds=init,warmup_seconds=warm,measured_seconds=first+last,checkpoint_seconds=io,checkpoint_sha=sha(file),state=s,scope='nonequilibrium timing fixture, not a physics chain'))
 elapsed=time.monotonic()-MODULE_START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024);req(elapsed<30 and rss<384,'resources');result=dict(freeze=freeze,cases=rows,seconds=elapsed,rss_mib=rss,scope='one paired cost profile only');(out/'RESULT.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args();print(json.dumps(profile(args.out),allow_nan=False))
