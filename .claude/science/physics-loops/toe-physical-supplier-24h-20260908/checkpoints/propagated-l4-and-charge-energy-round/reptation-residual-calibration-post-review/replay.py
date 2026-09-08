import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import pathlib,json,hashlib,numpy as np
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908/reptation-residual-calibration');O=pathlib.Path(__file__).parent
for manifest in ('PRODUCTION_FINAL_HASHES.json','PRODUCTION_FREEZE.json','SMOKE_HASHES.json'):
 for n,h in json.loads((P/manifest).read_text()).items():
  if hashlib.sha256((P/n).read_bytes()).hexdigest()!=h:raise RuntimeError('hash '+n)
raw=[];rss=[]
for sh in range(4):
 x=json.loads((P/f'shard{sh}.json').read_text());rss.append(x['rss_mib'])
 if not (x['shard']==sh and x['V']==.95 and x['n']==2 and x['burn']==64 and x['updates']==32768 and x['chains']==8):raise RuntimeError('metadata')
 if x['source_sha']!=hashlib.sha256((P/'production.py').read_bytes()).hexdigest():raise RuntimeError('source')
 if not 0<x['seconds']<180 or not 0<x['rss_mib']<384:raise RuntimeError('caps')
 for j,r in enumerate(x['rows']):
  if r['cid']!=8*sh+j or r['seed']!=202609180000+8*sh+j:raise RuntimeError('seed')
  b=np.array(r['batch_means']);c=r['counts']
  if b.shape!=(16,6) or not np.isfinite(b).all() or max(abs(b.mean(0)-r['mean']))>1e-12:raise RuntimeError('raw')
  if c['accepted']+c['rejected']!=32768 or not 0<=c['accepted_self']<=min(c['accepted'],c['self_proposals']):raise RuntimeError('counter')
  raw.append(b)
b=np.array(raw);a=b.mean(1);m=a.mean(0)
def calc(z):
 N,S,E,H2,XE,X2=z
 return np.array([(.95*N-E)/(2*S),(.95*N-E)/(2*S)+XE/S-E,XE/S-E,H2-E**2,X2-S**2])
v=calc(m);J=np.empty((5,6))
for i in range(6):
 z=m.astype(complex);z[i]+=1e-25j;J[:,i]=calc(z).imag/1e-25
cov6=(a-m).T@(a-m)/(31*32);cov=J@cov6@J.T;se=np.sqrt(np.diag(cov))
target=calc(np.array(next(z for z in json.loads((P/'MICRO.json').read_text())['oracle'] if z['n']==2)['vector']))
orig=json.loads((P/'ANALYSIS.json').read_text());rows=[]
for i,name in enumerate(('D','R','correction','VarH','VarX')):
 row=dict(name=name,value=float(v[i]),SE=float(se[i]),target=float(target[i]),consistency=bool(abs(v[i]-target[i])<=4*se[i]),precision=bool(4*se[i]<=(.25 if i in (2,3) else .1)*abs(target[i])))
 old=orig['results'][i]
 for k in ('value','SE','target'):
  if abs(row[k]-old[k])>2e-13:raise RuntimeError('estimate '+k)
 for k in ('consistency','precision'):
  if row[k]!=old[k]:raise RuntimeError('gate')
 rows.append(row)
if np.max(abs(cov-orig['estimator_covariance']))>1e-13:raise RuntimeError('covariance')
split=b[:,:8].mean(1)-b[:,8:].mean(1)
if max(abs(split.mean(0)-orig['split_difference']))>1e-13 or max(abs(split.std(0,ddof=1)/np.sqrt(32)-orig['split_SE']))>1e-13:raise RuntimeError('split')
bound=None if min(v[3:])<0 else float(np.sqrt(v[3]*v[4])/m[1])
if abs(bound-orig['bound_plugin'])>1e-13:raise RuntimeError('bound')
result=dict(rows=rows,covariance=cov.tolist(),max_estimate_residual=max(abs(v-np.array([r['value'] for r in orig['results']]))),max_SE_residual=max(abs(se-np.array([r['SE'] for r in orig['results']]))),signed_variances=v[3:].tolist(),bound_plugin=bound,nonpositive_chain_S=int(sum(a[:,1]<=0)),nonpositive_batch_S=int(sum((b[:,:,1]<=0).ravel())),max_RSS=max(rss),scope='Independent batch-to-chain replay, complex-step Jacobian, no author imports or production',source_hashes=json.loads((P/'PRODUCTION_FINAL_HASHES.json').read_text()))
(O/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ('source_hashes','covariance')},indent=2))
