import pathlib,json,hashlib,math,sys
import numpy as np
from checkpoint import load
P=pathlib.Path(__file__).parent;O=P/'PROFILE_OUTPUT';r=json.loads((O/'RESULT.json').read_text());d=json.loads((O/'DISPATCH.json').read_text());checks=0
def req(c,m):
 global checks
 checks+=1
 if not c:raise ValueError(m)
freeze=hashlib.sha256((P/'FINAL_FREEZE.json').read_bytes()).hexdigest();req(r['freeze']==d['freeze']==freeze,'freeze');req(d['exit']==0 and 0<r['seconds']<=d['external_seconds']<30 and 0<r['rss_mib']<384,'resources');f=json.loads((P/'FINAL_FREEZE.json').read_text())
for n,h in f.items():req(hashlib.sha256((P/n).read_bytes()).hexdigest()==h,'source '+n)
req(len(r['cases'])==2,'case count');total=0
for i,(c,V) in enumerate(zip(r['cases'],(.95,0.))):
 req((c['V'],c['L'],c['n'])==(V,8,110592),'fixed case');im=c['initializer'];req(im['V']==V and im['rk_sweeps']==2048 and im['rk_proposals']==3145728 and im['Q_steps']==110592 and type(im['nonself_Q_steps'])is int and 0<=im['nonself_Q_steps']<=110592,'initializer')
 times=[c[k] for k in ['initialization_seconds','warmup_seconds','measured_seconds','checkpoint_seconds']];req(all(math.isfinite(t) and t>0 for t in times),'positive timings');total+=sum(times)
 path=O/f'case{i}.npz';req(hashlib.sha256(path.read_bytes()).hexdigest()==c['checkpoint_sha'],'checkpoint hash');a,rr,ss=load(path,expected=dict(L=8,n=110592,V=V));req(ss['step']==12288 and ss['snapshots']==5,'checkpoint cadence')
 s=c['state'];req(s['step']==28672 and s['snapshots']==16,'final cadence');raw=np.array(s['raw']);batch=np.array(s['batch']);req(raw.shape==(16,154) and batch.shape==(4,154) and np.isfinite(raw).all() and np.isfinite(batch).all(),'finite arrays');req(np.array_equal(raw[:5],np.array(ss['raw'])),'checkpoint raw prefix');req(np.max(abs(batch-raw.reshape(4,4,154).sum(1)))<1e-12,'actual batch sums')
 for n in ['self_proposals','rejections','accepted','accepted_self','run','u','lo','hi','tagged_snapshots']:req(type(s[n])is int,'integer '+n)
 req(0<=s['self_proposals']<=28672 and 0<=s['accepted_self']<=s['accepted'] and s['accepted']+s['rejections']==28672,'counter bounds');req(all(type(t)is int and t>=0 for t in s['runs']) and len(s['runs'])==s['rejections'] and sum(s['runs'])+s['run']==s['accepted'],'run accounting')
 u=lo=hi=step=tagged=0;direction=1;snaps=0
 for j,run in enumerate(s['runs']+[s['run']]):
  for _ in range(run):
   u+=direction;lo=min(lo,u);hi=max(hi,u);step+=1
   if step>4096 and (step-4096)%1536==0:snaps+=1;tagged+=int(hi<=u+110592//2<=110592+lo)
  if j<len(s['runs']):
   step+=1;direction=-direction
   if step>4096 and (step-4096)%1536==0:snaps+=1;tagged+=int(hi<=u+110592//2<=110592+lo)
 req((step,u,lo,hi,snaps,tagged)==(28672,s['u'],s['lo'],s['hi'],16,s['tagged_snapshots']),'full run/tag replay')
req(total<=r['seconds'],'component wall accounting');out=dict(predicates=checks,component_seconds=total,external_seconds=d['external_seconds'],unallocated_external_seconds=d['external_seconds']-total,sha={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in O.iterdir() if f.is_file()},scope='complete cost-profile receipt/checkpoint/raw validation, no physics inference');(P/'PROFILE_VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
