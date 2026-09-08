from pathlib import Path
import numpy as np,json,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/rk-inverse-moment/pilot');a=json.loads((p/'ANALYSIS.json').read_text());checks=0;largest=0.;precision=0;exact=0;records=[]
for cell in a['rows']:
 L,b=cell['L'],cell['burn'];name=f'L{L}_b{b}';raw=np.load(p/(name+'.npz'));meta=json.loads((p/(name+'.json')).read_text());orig=raw['origins'];prod=raw['products']
 for row in cell['rows']:
  idx=[j for j,m in enumerate(meta['modes']) if m[0]==row['harmonic']];j=meta['alphas'].index(row['alpha']);alpha=row['alpha'];S=np.mean(np.sum(np.abs(np.take(orig,idx,axis=-1))**2,axis=-1),axis=1);Y=np.mean(np.sum(np.take(prod[:,:,j,:],idx,axis=-1).real,axis=-1),axis=1)
  sm,ym=float(S.mean()),float(Y.mean());r=ym/(alpha*sm);cov=np.cov(np.stack([S,Y]),ddof=1)/32;g=np.array([-ym/(alpha*sm**2),1/(alpha*sm)]);se=float(np.sqrt(g@cov@g));error=max(abs(r-row['r_truncated']),abs(se-row['SE']))
  if error>1e-12:raise ValueError('independent ratio covariance')
  ok=bool(4*se<=.1*r)
  if ok!=row['precision_nominal']:raise ValueError('precision flag')
  precision+=ok;exact+=bool(row.get('consistency_nominal',False));largest=max(largest,error);checks+=1;records.append(dict(L=L,burn=b,h=row['harmonic'],alpha=alpha,r=r,SE=se))
 flags=raw['clipped'];K=raw['lags'];caps=np.array(meta['Kmax'])
 if not np.array_equal(flags,K>caps) or np.any(prod[flags]!=0):raise ValueError('tail handling')
 for cid,lag in zip(meta['chain_ids'],K):
  U=np.random.default_rng(400000000+cid).random((256,3));expected=np.floor(np.log1p(-U)/np.log(np.array(meta['q']))).astype(np.int64)
  if not np.array_equal(lag,expected):raise ValueError('actual lag seed binding')
  checks+=1
status=json.loads((p/'STATUS.json').read_text());total=sum(x['seconds'] for x in status)+json.loads((p/'MICRO.json').read_text())['seconds']
out=dict(status='PASS',checks=checks,ratio_rows=18,precision_passes=precision,L2_nominal_consistency_passes=exact,max_numerical_residual=largest,charged_seconds=total,rows=records,report_sha256=hashlib.sha256((p/'PRODUCTION_REPORT.md').read_bytes()).hexdigest(),scope='Raw paired covariance and fixed lag seed reconstruction; no new stationary or spectral certificate')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
