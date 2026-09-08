import os,time,signal,resource,json,hashlib
start=time.monotonic();signal.alarm(180)
from pathlib import Path
from itertools import product
import numpy as np
p=Path(__file__).resolve().parent;source=Path('/private/tmp/toe-24h-probes-20260908/detuned-reptation-local')
checks=0
def req(c):
 global checks
 checks+=1
 if not c:raise RuntimeError('memory diagnostic invariant')
def reconstruct(n,runs,last,burn):
 u=lo=hi=attempt=seedcount=0;direction=1;first_escape=None;first_measured_escape=None;measured_rejects=0
 for j,r in enumerate(runs+[last]):
  a=attempt;lower=hi-n//2;upper=lo+n//2
  if direction==1:tlo=lower-u;thi=upper-u
  else:tlo=u-upper;thi=u-lower
  left=max(1,tlo);right=min(r,thi)
  ml=max(1,burn-a+1);mr=r
  seedcount+=max(0,min(right,mr)-max(left,ml)+1)
  # First outside time of accepted interval, allowing later returns to seed span.
  def outside(l,h):
   if l>h:return None
   if l<left or l>right:return l
   return right+1 if right<h else None
  e=outside(1,r)
  if first_escape is None and e is not None:first_escape=a+e
  e=outside(ml,mr)
  if first_measured_escape is None and e is not None:first_measured_escape=a+e
  u+=direction*r;lo=min(lo,u);hi=max(hi,u);attempt+=r
  if j<len(runs):
   attempt+=1;inside=hi<=u+n//2<=n+lo
   if not inside and first_escape is None:first_escape=attempt
   if attempt>burn:
    measured_rejects+=1;seedcount+=int(inside)
    if not inside and first_measured_escape is None:first_measured_escape=attempt
   direction=-direction
 return dict(attempts=attempt,seed_measurements=seedcount,first_escape_attempt=first_escape,first_measured_escape_attempt=first_measured_escape,end_unwrapped_head=u,min_head=lo,max_head=hi,surviving_original_vertices=max(0,n+lo-hi+1),measured_rejections=measured_rejects)
# Exhaustive tagged paths; no physical-state dynamics needed for this combinatorial identity.
for n in (2,4,6):
 for bits in product((0,1),repeat=10):
  path=list(range(n+1));d=1;runs=[];run=0;truth=[]
  for ok in bits:
   if ok:
    run+=1
    if d==1:path=path[1:]+[-1]
    else:path=[-1]+path[:-1]
   else:runs.append(run);run=0;d=-d
   truth.append(path[n//2]>=0)
  z=reconstruct(n,runs,run,3)
  req(z['attempts']==10);req(z['seed_measurements']==sum(truth[3:]));req(z['surviving_original_vertices']==sum(x>=0 for x in path));req(z['first_escape_attempt']==next((i+1 for i,x in enumerate(truth) if not x),None))
rows=[];hashes={};files=sorted(source.glob('cell*_shard*.json'));req(len(files)==96)
for file in files:
 raw=json.loads(file.read_text());hashes[file.name]=hashlib.sha256(file.read_bytes()).hexdigest();n=raw['n'];burn=raw['burn_multiplier']*n;updates=raw['updates']
 for row in raw['rows']:
  c=row['counters'];z=reconstruct(n,c['run_lengths_including_burn'],c['unfinished_run'],burn)
  req(z['attempts']==burn+updates);req(z['measured_rejections']==c['rejections']);req(updates-c['rejections']==c['accepted'])
  z.update(cid=row['cid'],cell=raw['cell'],n=n,burn=burn,updates=updates,seed_fraction=z['seed_measurements']/updates,mean=row['mean']);rows.append(z)
req(len(rows)==192 and len({r['cid'] for r in rows})==192)
summary=[]
for cell in range(6):
 rr=[r for r in rows if r['cell']==cell];frac=np.array([r['seed_fraction'] for r in rr]);m=np.array([r['mean'] for r in rr]);cor=[]
 for j in range(4):cor.append(float(np.corrcoef(frac,m[:,j])[0,1]) if np.std(frac)>0 and np.std(m[:,j])>0 else None)
 summary.append(dict(cell=cell,n=rr[0]['n'],burn_multiplier=rr[0]['burn']//rr[0]['n'],mean_seed_fraction=float(frac.mean()),min_seed_fraction=float(frac.min()),max_seed_fraction=float(frac.max()),chains_with_measured_seed=int(sum(frac>0)),chains_original_span_survives_end=sum(r['surviving_original_vertices']>0 for r in rr),pearson_seed_fraction_vs_NF_X1_X2_E=cor))
import sys
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024);req(0<rss<384)
result=dict(checks=checks,rows=rows,summary=summary,input_hashes=hashes,seconds=time.monotonic()-start,peak_MiB=rss)
(p/'RESULT.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(summary,indent=2))
