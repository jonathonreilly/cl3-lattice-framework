import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import pathlib,json,hashlib,numpy as np,math,time
start=time.monotonic()
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/reptation-propagated-l8-design');O=pathlib.Path(__file__).parent;D=P/'PRODUCTION_OUTPUT'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def req(c,m):
 if not c:raise RuntimeError(m)
freeze=json.loads((P/'PRODUCTION_FREEZE.json').read_text())
for n,h in freeze.items():req(sha(P/n)==h,'freeze '+n)
for n,h in json.loads((P/'RUNTIME.json').read_text())['files'].items():req(sha(pathlib.Path(n))==h,'runtime '+n)
req(sha(D/'ANALYSIS.json')=='bee6e3e7ea412d8866c63ce7da75b840964e591c372dc5e4837a13c796b25022','analysis hash')
def vals(x):
 N,S,T,E,H2,SE,TE,S2,T2=x;out=[]
 for q,z,ze,z2 in ((2-np.sqrt(2),S,SE,S2),(2,T,TE,T2)):
  d=q*(.95*N-E)/(512*z);c=ze/z-E;out.extend([d,d+c,c,H2-E*E,z2-z*z])
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

orig=json.loads((D/'ANALYSIS.json').read_text());arms=[];maxerr=maxcov=0.;segments=0;maxrss=0.;hashes={};resources=[]
for arm,(tau,rk,burnmul) in enumerate(((12,2048,32),(36,2048,8),(36,2048,32))):
 raw=[];fractions=[];n=3072*tau;burn=burnmul*n;updates=32*n;cap=24*n;total=burn+updates
 for cid in range(16):
  expected=dict(arm=arm,chain=cid,L=8,n=n,rk=rk,burn=burn,updates=updates,cap=cap,seed=202609230000+32*arm+cid,initseed=202609240000+32*arm+cid,smoke=False);prev=None;prevstate=None
  for seg in range((total+cap-1)//cap):
   stem=f'arm{arm}_chain{cid}_segment{seg}';file=D/(stem+'.json');npz=D/(stem+'.npz');z=json.loads(file.read_text());segments+=1;hashes[file.name]=sha(file);hashes[npz.name]=sha(npz)
   req(z['config']==expected and z['freeze']==sha(P/'PRODUCTION_FREEZE.json'),'config');req(z['previous_receipt_sha']==prev and z['state_sha']==sha(npz),'chain');req(z['begin']==seg*cap and z['stop']==min(total,(seg+1)*cap) and z['final']==(z['stop']==total),'interval');req(0<z['seconds']<180 and 0<z['rss_mib']<384,'resources');resources.append(z['seconds']);maxrss=max(maxrss,z['rss_mib']);req(json.loads((D/(stem+'.stdout')).read_text())==z,'stdout');req(not (D/(stem+'.stderr')).read_text(),'stderr')
   with np.load(npz,allow_pickle=False) as zz:
    meta=json.loads(str(zz['metadata']));s=meta['accumulator'];req(meta['L']==8 and meta['n']==n and meta['direction'] in (-1,1) and 0<=meta['head']<n,'saved meta');req(zz['labels'].shape==(n,) and np.issubdtype(zz['labels'].dtype,np.integer) and np.all((zz['labels']>=-1)&(zz['labels']<1536)),'labels');req(zz['states'].shape==(3,1536) and np.all((zz['states']==0)|(zz['states']==1)) and np.isfinite(zz['O']).all(),'states')
   req(s['step']==z['stop'] and sum(s['runs'])+len(s['runs'])+s['run']==s['step'],'accumulator');batch=np.array(s['batch']);req(batch.shape==(16,9) and np.isfinite(batch).all(),'batch');done=max(0,s['step']-burn);width=updates//16;req(np.all(batch[(done+width-1)//width:]==0),'future batches')
   if prevstate is not None:
    req(s['runs'][:len(prevstate['runs'])]==prevstate['runs'],'run prefix');oldcompleted=max(0,prevstate['step']-burn)//width;req(np.array_equal(batch[:oldcompleted],np.array(prevstate['batch'])[:oldcompleted]),'completed batches immutable')
   prev=sha(file);prevstate=s
  row=z['row'];req(row['cid']==cid and row['seed']==expected['seed'] and row['initseed']==expected['initseed'],'seed');b=batch/width;req(np.allclose(b,row['batch_means'],atol=0,rtol=0) and np.allclose(batch.sum(0)/updates,row['mean'],atol=0,rtol=0),'final accum');raw.append(b.mean(0));fractions.append(memory(row,n,burn,updates));req(row['initializer']['rk_sweeps']==2048 and row['initializer']['rk_proposals']==2048*1536 and row['initializer']['Q_steps']==n,'init')
 a=np.array(raw);m=a.mean(0);v=vals(m);J=np.empty((10,9))
 for j in range(9):
  zz=m.astype(complex);zz[j]+=1e-25j;J[:,j]=vals(zz).imag/1e-25
 influences=(a-m)@J.T;cov=J@np.cov(a,rowvar=False)@J.T/16;se=np.sqrt(np.diag(cov));old=orig['arms'][arm];ov=np.array([r[k] for r in old['rows'] for k in ('D','R','correction','VarH','VarX')]);ose=np.array([r[k+'_SE'] for r in old['rows'] for k in ('D','R','correction','VarH','VarX')]);maxerr=max(maxerr,float(max(abs(v-ov))),float(max(abs(se-ose))));maxcov=max(maxcov,float(np.max(abs(cov-old['estimator_covariance']))));req(np.max(abs(influences-old['chain_influences']))<1e-9,'influences');req(np.max(abs(np.cov(a,rowvar=False)-old['chain_covariance']))<1e-9,'raw covariance')
 for h,r in enumerate(old['rows']):
  k=5*h;req(r['D_precision']==bool(v[k]>0 and 4*se[k]<=.1*v[k]),'precision');req(r['residual_status']==('resolved' if abs(v[k+2])>4*se[k+2] else 'indeterminate'),'residual');req(r['variance_status']==('positive_resolved' if v[k+3]>4*se[k+3] else 'indeterminate'),'variance')
 req(fractions==old['tag_fractions'] and old['memory_flag']==(max(fractions)>.01),'tag gate');arms.append(dict(values=v.tolist(),SE=se.tolist(),tags=fractions,precision=[r['D_precision'] for r in old['rows']]))
flags=[]
for c in orig['comparisons']:
 i,j=c['arms'];k=5*(c['harmonic']-1)+{'D':0,'R':1,'correction':2}[c['quantity']];delta=arms[i]['values'][k]-arms[j]['values'][k];se=math.hypot(arms[i]['SE'][k],arms[j]['SE'][k]);flag=abs(delta)>4*se;req(abs(delta-c['difference'])<1e-10 and abs(se-c['SE'])<1e-10 and flag==c['flag'],'comparison');flags.append(flag)
req(maxerr<1e-9 and maxcov<1e-9 and segments==128,'totals');req(orig['status']=='fails_diagnostics','status')
status=json.loads((D/'STATUS.json').read_text());req(len(status)==128 and all(x['exit']==0 and 0<x['seconds']<180 for x in status),'dispatch');out=dict(segments=segments,chains=48,arms=arms,max_estimate_SE_error=maxerr,max_covariance_error=maxcov,flags=sum(flags),comparisons=len(flags),max_rss=maxrss,external_seconds=sum(x['seconds'] for x in status),elapsed=time.monotonic()-start,scope='Independent full receipt/checkpoint accumulator and raw statistics replay; no author imports or sampling')
(O/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');(O/'RAW_HASHES.json').write_text(json.dumps(hashes,indent=2)+'\n');print({k:v for k,v in out.items() if k!='arms'})
