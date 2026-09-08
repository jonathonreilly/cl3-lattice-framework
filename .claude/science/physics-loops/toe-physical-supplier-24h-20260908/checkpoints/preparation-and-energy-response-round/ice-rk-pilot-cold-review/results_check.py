from pathlib import Path
import numpy as np,json,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/ice-spectral-moments/pilot');out=Path(__file__).parent
summary=json.loads((p/'SUMMARY.json').read_text()); result=[]; checks=0
for L in (2,4):
 for burn in (32,128):
  r=json.loads((p/f'L{L}_b{burn}.json').read_text());d=np.load(p/f'L{L}_b{burn}.npz');x=d['values']; rows=next(v['modes'] for v in summary['rows'] if v['L']==L and v['burn']==burn)
  ratios=[];thresholds=[];common=[];rel=[]
  for m,row in enumerate(rows):
   means=x[:,:,m,:].mean(axis=1);S=means[:,2].mean()
   for slot,name in ((3,'mu1'),(4,'mu2')):
    mu=means[:,slot].mean()/S;se=np.sqrt(np.sum((means[:,slot]-mu*means[:,2])**2)/(31*32))/S
    assert abs(mu-row[name]['ratio'])<1e-12 and abs(se-row[name]['chain_delta_SE'])<1e-12;checks+=1
   mu=row['mu1']['ratio'];ss=x[:,:64,m,2].reshape(-1)
   va=np.var(d['all_face_numerator'][:,m]-mu*ss,ddof=1);vo=np.var(d['one_face_numerator'][:,m]-mu*ss,ddof=1);a=va/vo
   c=float(r['timing_seconds_per_snapshot']['2']);o=float(r['timing_seconds_per_snapshot']['1']);u=r['update_only_sweep_seconds_per_snapshot']
   assert abs(a*c/o-row['ratio_influence_variance_cost']['count_over_one'])<1e-12;checks+=1
   ratios.append(a);thresholds.append((a*c-o)/(1-a));common.append(a*(u+c)/(u+o));rel.append(row['mu1']['chain_delta_SE']/mu)
  result.append({'L':L,'burn':burn,'snapshot_influence_variance_ratio_range':[min(ratios),max(ratios)],'break_even_common_cost_seconds_range':[min(thresholds),max(thresholds)],'update_plus_numerator_snapshot_proxy_range':[min(common),max(common)],'mu1_relative_SE_range':[min(rel),max(rel)]})
names=['pilot.py','analyze.py','REPORT.md','SUMMARY.json']+[f'L{L}_b{b}.{ext}' for L in (2,4) for b in (32,128) for ext in ('json','npz')]
payload={'checks':checks,'rows':result,'hashes':{n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in names},'scope':'Raw statistics independently recomputed; common-cost proxy is not MCMC asymptotic efficiency.'}
(out/'RESULTS_CHECK.json').write_text(json.dumps(payload,indent=2,allow_nan=False)+'\n');print(json.dumps(payload,indent=2))
