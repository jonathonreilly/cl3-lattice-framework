from pathlib import Path
import hashlib,json,difflib
p=Path(__file__).parent
for f in ['analyze.py','PROTOCOL.md','PRODUCTION_FREEZE.json']:
 (p/(f+'.BEFORE_INTEGRITY_REPAIR')).write_bytes((p/f).read_bytes())
s=(p/'production.py').read_text();old=s.replace('choices=range(8)','choices=range(16)')
assert hashlib.sha256(old.encode()).hexdigest()=='a8f042d735538de473295111dc3a318110f029f85694b930927cf079f24f88fe'
(p/'production_MICRO_ORIGINAL.py').write_text(old)
(p/'MICRO_PRODUCER_DELTA.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile='micro original',tofile='production proposed')))
insert='''def replay(n,runs,last,burn,updates):
 req(type(runs) is list and all(type(z) is int and z>=0 for z in runs+[last]),'run domains')
 req(sum(runs)+len(runs)+last==burn+updates,'attempt total')
 u=lo=hi=a=tagged=rejects=0;d=1;escape=None;bt=None
 for j,r in enumerate(runs+[last]):
  lower=hi-n//2;upper=lo+n//2
  left,right=(lower-u,upper-u) if d==1 else (u-upper,u-lower)
  left=max(1,left);right=min(r,right)
  tagged+=max(0,right-max(left,burn-a+1)+1)
  if escape is None and r:
   t=1 if left>1 or right<1 else right+1
   if t<=r:escape=a+t
  if a<burn<=a+r:
   ub=u+d*(burn-a);bt=max(0,n+min(lo,ub)-max(hi,ub)+1)
  u+=d*r;lo=min(lo,u);hi=max(hi,u);a+=r
  if j<len(runs):
   a+=1;inside=hi<=u+n//2<=n+lo
   if escape is None and not inside:escape=a
   if a==burn:bt=max(0,n+lo-hi+1)
   if a>burn:tagged+=int(inside);rejects+=1
   d=-d
 return dict(tagged_measurements=tagged,fraction=tagged/updates,burn_end_tags=bt,final_tags=max(0,n+lo-hi+1),first_escape=escape,u=u,lo=lo,hi=hi),rejects

def validate_history(r,n,rk,burn,updates):
 c=r['counters'];runs=c['run_lengths_including_burn'];last=c['unfinished_run']
 mem,rejects=replay(n,runs,last,burn,updates)
 req(r['memory']==mem,'replayed memory')
 for k in ['self_proposals','rejections','accepted','accepted_self','window_traversals_including_burn']:
  req(type(c[k]) is int and c[k]>=0,'counter domains')
 req(c['rejections']==rejects and c['accepted']==updates-rejects,'measured counters')
 req(c['accepted_self']<=min(c['accepted'],c['self_proposals']) and c['self_proposals']<=updates and c['self_proposals']-c['accepted_self']<=rejects,'self counters')
 req(c['window_traversals_including_burn']==sum(z//n for z in runs+[last]),'traversals')
 z=r['initializer'];req(z['rk_sweeps']==rk and z['rk_proposals']==rk*192 and z['Q_steps']==n and type(z['nonself_Q_steps']) is int and 0<=z['nonself_Q_steps']<=n and z['law']=='finite RK start followed by productQ; not equilibrium productG path law','initializer')
'''
s=(p/'analyze.py').read_text();s=s.replace('def validate(x,arm,sh):',insert+'\ndef validate(x,arm,sh):')
needle="mem=r['memory'];req(0<=mem['tagged_measurements']<=32*n and mem['fraction']==mem['tagged_measurements']/(32*n) and mem['final_tags']==max(0,n+mem['lo']-mem['hi']+1),'memory')"
assert needle in s;s=s.replace(needle,'validate_history(r,n,rk,burn*n,32*n)');(p/'analyze.py').write_text(s)
with (p/'PROTOCOL.md').open('a') as f:f.write('\nPreproduction integrity repair: all stored accepted runs are replayed to validate memory and measured acceptance/rejection counts; self-label counts have consistency bounds only, since runs do not identify proposal labels. Initializer metadata is checked. R and Epsi identities apply to the stationary product-G path law; nonstationary observed ratios are diagnostic estimates, not exact Rayleigh quotients of an inferred state. The micro producer is preserved byte-for-byte separately; its only later change was shard choices range(16) to range(8). No sampler or statistical formula changed.\n')
