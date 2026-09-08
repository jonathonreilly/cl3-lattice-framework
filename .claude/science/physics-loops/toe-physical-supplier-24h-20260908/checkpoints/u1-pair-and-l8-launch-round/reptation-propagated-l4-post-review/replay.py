import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import pathlib,json,hashlib,numpy as np,math
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/reptation-propagated-l4');O=pathlib.Path(__file__).parent
for name in ('PRODUCTION_FREEZE.json','FINAL_RESULTS_HASHES.json'):
 for n,h in json.loads((P/name).read_text()).items():
  if hashlib.sha256((P/n).read_bytes()).hexdigest()!=h:raise RuntimeError('hash '+n)
def vals(x):
 N,S,T,E,H2,SE,TE,S2,T2=x;out=[]
 for q,z,ze,z2 in ((2,S,SE,S2),(4,T,TE,T2)):
  d=q*(.95*N-E)/(64*z);c=ze/z-E;out.extend([d,d+c,c,H2-E*E,z2-z*z])
 return np.array(out)
def memory(r,n,burn,updates):
 c=r['counters'];runs=c['run_lengths_including_burn'];last=c['unfinished_run'];u=lo=hi=step=tagged=rejects=0;d=1;first=None;bt=None
 for j,l in enumerate(runs+[last]):
  us=u+d*np.arange(1,l+1);los=np.minimum(lo,us);his=np.maximum(hi,us);inside=(his<=us+n//2)&(us+n//2<=n+los);times=step+np.arange(1,l+1)
  tagged+=int(np.sum(inside[times>burn]))
  if first is None and np.any(~inside):first=int(times[np.flatnonzero(~inside)[0]])
  if step<burn<=step+l:
   k=burn-step-1;bt=max(0,int(n+los[k]-his[k]+1))
  if l:u=int(us[-1]);lo=int(los[-1]);hi=int(his[-1])
  step+=l
  if j<len(runs):
   step+=1;inside=hi<=u+n//2<=n+lo
   if step==burn:bt=max(0,n+lo-hi+1)
   if first is None and not inside:first=step
   if step>burn:tagged+=inside;rejects+=1
   d=-d
 expected=dict(tagged_measurements=tagged,fraction=tagged/updates,burn_end_tags=bt,final_tags=max(0,n+lo-hi+1),first_escape=first,u=u,lo=lo,hi=hi)
 if expected!=r['memory'] or step!=burn+updates or c['rejections']!=rejects or c['accepted']!=updates-rejects:raise RuntimeError('memory')
 return tagged/updates
orig=json.loads((P/'ANALYSIS.json').read_text());arms=[];maxerr=0.;maxcov=0.;maxrss=0.
for arm,(tau,rk,burn) in enumerate(((12,128,32),(12,512,32),(36,512,8),(36,512,32))):
 raw=[];fractions=[];n=384*tau
 for sh in range(8):
  x=json.loads((P/f'arm{arm}_shard{sh}.json').read_text());maxrss=max(maxrss,x['rss_mib'])
  if not (x['n']==n and x['rk_sweeps']==rk and x['burn_multiplier']==burn and x['seconds']<180 and 0<x['rss_mib']<384):raise RuntimeError('metadata')
  for j,r in enumerate(x['rows']):
   if r['cid']!=32*arm+2*sh+j or r['seed']!=202609190000+r['cid']:raise RuntimeError('seed')
   b=np.array(r['batch_means'])
   if b.shape!=(16,9) or not np.isfinite(b).all() or max(abs(b.mean(0)-r['mean']))>1e-8:raise RuntimeError('batch')
   raw.append(b.mean(0));fractions.append(memory(r,n,burn*n,32*n))
 a=np.array(raw);m=a.mean(0);v=vals(m);J=np.empty((10,9))
 for j in range(9):
  z=m.astype(complex);z[j]+=1e-25j;J[:,j]=vals(z).imag/1e-25
 cov=J@np.cov(a,rowvar=False)@J.T/16;se=np.sqrt(np.diag(cov));old=orig['arms'][arm];ov=np.array([r[k] for r in old['rows'] for k in ('D','R','correction','VarH','VarX')]);ose=np.array([r[k+'_SE'] for r in old['rows'] for k in ('D','R','correction','VarH','VarX')]);maxerr=max(maxerr,float(max(abs(v-ov))),float(max(abs(se-ose))));maxcov=max(maxcov,float(np.max(abs(cov-old['estimator_covariance']))))
 for h,r in enumerate(old['rows']):
  k=5*h
  if r['D_precision']!=bool(v[k]>0 and 4*se[k]<=.1*v[k]) or r['residual_status']!=('resolved' if abs(v[k+2])>4*se[k+2] else 'indeterminate') or r['variance_status']!=('positive_resolved' if v[k+3]>4*se[k+3] else 'indeterminate'):raise RuntimeError('gate')
  bound=None if v[k+3]<0 or v[k+4]<0 else float(np.sqrt(v[k+3]*v[k+4])/m[h+1])
  if bound is None:
   if r['bound_plugin'] is not None:raise RuntimeError('negative clipping')
  elif abs(bound-r['bound_plugin'])>1e-10:raise RuntimeError('bound')
 if fractions!=old['tag_fractions'] or old['memory_flag']!=(max(fractions)>.01):raise RuntimeError('memory gate')
 arms.append(dict(values=v.tolist(),SE=se.tolist(),max_tag_fraction=max(fractions)))
flags=[]
for old in orig['comparisons']:
 i,j=old['arms'];k=5*(old['harmonic']-1)+{'D':0,'R':1,'correction':2}[old['quantity']];d=arms[i]['values'][k]-arms[j]['values'][k];se=math.hypot(arms[i]['SE'][k],arms[j]['SE'][k]);flag=abs(d)>4*se
 if abs(d-old['difference'])>1e-10 or abs(se-old['SE'])>1e-10 or flag!=old['flag']:raise RuntimeError('comparison')
 flags.append(flag)
if maxerr>1e-10 or maxcov>1e-10:raise RuntimeError('residual')
out=dict(arms=arms,max_estimate_SE_residual=maxerr,max_covariance_residual=maxcov,comparisons=len(flags),flags=sum(flags),maxRSS=maxrss,scope='Independent raw batch/CAR-free statistic replay, no author imports or production; memory vectorized literal accepted coordinates.')
(O/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='arms'},indent=2))
