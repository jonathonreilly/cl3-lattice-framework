import itertools,json,hashlib
from pathlib import Path
from analyze import replay
checks=0
for n in [2,4,6]:
 for bits in itertools.product([0,1],repeat=10):
  for burn in [1,3,7]:
   u=lo=hi=0;d=1;r=0;runs=[];tag=rej=0;esc=bt=None
   for i,ok in enumerate(bits,1):
    if ok:u+=d;lo=min(lo,u);hi=max(hi,u);r+=1
    else:runs.append(r);r=0;d=-d
    inside=hi<=u+n//2<=n+lo
    if not inside and esc is None:esc=i
    if i==burn:bt=max(0,n+lo-hi+1)
    if i>burn:tag+=inside;rej+=not ok
   m=dict(tagged_measurements=tag,fraction=tag/(10-burn),burn_end_tags=bt,final_tags=max(0,n+lo-hi+1),first_escape=esc,u=u,lo=lo,hi=hi)
   assert replay(n,runs,r,burn,10-burn)==(m,rej)
   checks+=1
p=Path(__file__).parent
(p/'REPAIR_CONTROLS.json').write_text(json.dumps(dict(actual_exhaustive_run_replay_comparisons=checks,production_executed=False),indent=2)+'\n')
f=json.loads((p/'PRODUCTION_FREEZE.json').read_text())
for name in ['production_MICRO_ORIGINAL.py','MICRO_PRODUCER_DELTA.diff','repair_controls.py','REPAIR_CONTROLS.json']:f[name]=''
for name in f:f[name]=hashlib.sha256((p/name).read_bytes()).hexdigest()
(p/'PRODUCTION_FREEZE.json').write_text(json.dumps(f,indent=2)+'\n')
print(checks,hashlib.sha256((p/'PRODUCTION_FREEZE.json').read_bytes()).hexdigest())
