import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import argparse,hashlib,json,pathlib,resource,signal,sys,time
import numpy as np
from core import count
from initialize import initialize
from checkpoint import save,load
P=pathlib.Path(__file__).resolve().parent
ARMS=[(12,2048,32),(36,2048,8),(36,2048,32)]
def req(c,m):
 if not c:raise ValueError(m)
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def config(arm,cid,smoke=False):
 req(type(arm)is int and 0<=arm<3 and type(cid)is int and 0<=cid<16,'arm/chain')
 tau,rk,b=ARMS[arm];L=8;n=3072*tau;burn=b*n;updates=32*n;cap=24*n
 if smoke:L=2;n=48;rk=0;burn=48;updates=96;cap=31
 return dict(arm=arm,chain=cid,L=L,n=n,rk=rk,burn=burn,updates=updates,cap=cap,seed=202609230000+32*arm+cid,initseed=202609240000+32*arm+cid,smoke=smoke)
def initial(c):
 a,im=initialize(c['L'],c['n'],np.random.default_rng(c['initseed']),c['rk']);r=np.random.default_rng(c['seed'])
 s=dict(step=0,batch=np.zeros((16,9)).tolist(),self_proposals=0,rejections=0,accepted=0,accepted_self=0,runs=[],run=0,u=0,lo=0,hi=0,tagged=0,first_escape=None,burn_tags=None,initializer=im)
 return a,r,s
def advance(a,r,s,c,stop):
 batch=np.array(s['batch']);n=c['n'];burn=c['burn'];updates=c['updates'];req(s['step']<=stop<=burn+updates,'step interval')
 for step in range(s['step'],stop):
  d=a.direction;f,ok=a.step(r)
  if ok:s['u']+=d;s['lo']=min(s['lo'],s['u']);s['hi']=max(s['hi'],s['u']);s['run']+=1
  else:s['runs'].append(s['run']);s['run']=0
  inside=s['hi']<=s['u']+n//2<=n+s['lo']
  if not inside and s['first_escape'] is None:s['first_escape']=step+1
  if step+1==burn:s['burn_tags']=max(0,n+s['lo']-s['hi']+1)
  if step>=burn:
   s['self_proposals']+=int(f<0);s['rejections']+=int(not ok);s['accepted']+=int(ok);s['accepted_self']+=int(ok and f<0);s['tagged']+=int(inside)
   o=a.O[1];x1=float(np.vdot(o[:6],o[:6]).real);x2=float(np.vdot(o[6:],o[6:]).real) if len(o)>6 else 0.;hl=-.05*a.nf[0];hr=-.05*a.nf[2];e=(hl+hr)/2
   batch[(step-burn)//(updates//16)]+=[a.nf[1],x1,x2,e,hl*hr,x1*e,x2*e,x1*x1,x2*x2]
 s['step']=stop;s['batch']=batch.tolist()
 return a,r,s
def finalrow(s,c):
 req(s['step']==c['burn']+c['updates'],'final step');b=np.array(s['batch']);n=c['n'];updates=c['updates']
 return dict(cid=c['chain'],seed=c['seed'],initseed=c['initseed'],initializer=s['initializer'],mean=(b.sum(0)/updates).tolist(),batch_means=(b/(updates//16)).tolist(),memory=dict(tagged_measurements=s['tagged'],fraction=s['tagged']/updates,burn_end_tags=s['burn_tags'],final_tags=max(0,n+s['lo']-s['hi']+1),first_escape=s['first_escape'],u=s['u'],lo=s['lo'],hi=s['hi']),counters=dict(self_proposals=s['self_proposals'],rejections=s['rejections'],accepted=s['accepted'],accepted_self=s['accepted_self'],run_lengths_including_burn=s['runs'],unfinished_run=s['run'],window_traversals_including_burn=sum(z//n for z in s['runs']+[s['run']])))
def verify_freeze():
 f=json.loads((P/'PRODUCTION_FREEZE.json').read_text())
 for name,h in f.items():req(sha(P/name)==h,'freeze '+name)
 runtime=json.loads((P/'RUNTIME.json').read_text())
 req(sys.version==runtime['python_version'] and np.__version__==runtime['numpy_version'],'runtime versions')
 for name,h in runtime['files'].items():req(sha(name)==h,'runtime '+name)
 return sha(P/'PRODUCTION_FREEZE.json')
def segment(arm,cid,seg,out,smoke=False):
 start=time.monotonic();signal.alarm(30 if smoke else 180);freeze=verify_freeze();c=config(arm,cid,smoke);total=c['burn']+c['updates'];req(type(seg)is int and 0<=seg<(total+c['cap']-1)//c['cap'],'segment')
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True);stem=f'arm{arm}_chain{cid}_segment{seg}';receipt=out/(stem+'.json');state=out/(stem+'.npz');req(not receipt.exists() and not state.exists(),'immutable output exists')
 prev=None
 if seg==0:a,r,s=initial(c)
 else:
  old=out/f'arm{arm}_chain{cid}_segment{seg-1}.json';z=json.loads(old.read_text());req(z['config']==c and z['freeze']==freeze and z['segment']==seg-1,'predecessor identity');oldstate=out/f'arm{arm}_chain{cid}_segment{seg-1}.npz';req(sha(oldstate)==z['state_sha'],'predecessor state hash');a,r,s=load(oldstate,expected=c);req(s['step']==seg*c['cap']==z['stop'],'predecessor boundary');prev=sha(old)
 begin=s['step'];a,r,s=advance(a,r,s,c,min(total,begin+c['cap']))
 for j,x in enumerate(a.states):req(a.nf[j]==count(x,a.faces) and np.max(abs(a.O[j]-a.coeff@(x.astype(float)-.5)))<1e-9,'final cache')
 save(state,a,r,c['L'],s)
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);elapsed=time.monotonic()-start;req(0<rss<384 and elapsed<(30 if smoke else 180),'resources')
 z=dict(config=c,segment=seg,begin=begin,stop=s['step'],freeze=freeze,previous_receipt_sha=prev,state_sha=sha(state),seconds=elapsed,rss_mib=rss,final=s['step']==total)
 if z['final']:z['row']=finalrow(s,c)
 with receipt.open('x') as f:json.dump(z,f,indent=2,allow_nan=False)
 return z
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--arm',type=int,required=True);ap.add_argument('--chain',type=int,required=True);ap.add_argument('--segment',type=int,required=True);ap.add_argument('--out',required=True);ap.add_argument('--smoke',action='store_true');v=ap.parse_args();print(json.dumps(segment(v.arm,v.chain,v.segment,v.out,v.smoke)))
