from pathlib import Path
import json,hashlib
import numpy as np
p=Path('/private/tmp/toe-24h-probes-20260908/detuned-reptation-local');report=json.loads((p/'ANALYSIS.json').read_text());errs=[];checks=0
for cell in report['cells']:
 rows=[]
 for sh in range(16):rows+=json.loads((p/f"cell{cell['cell']}_shard{sh}.json").read_text())['rows']
 raw=np.array([r['batch_means'] for r in rows]);a=raw.mean(1);m=a.mean(0);s=(a-m).T@(a-m)/31;grads=[]
 for h,q in [(1,2),(2,4)]:
  r=q*(.95*m[0]-m[3])/(64*m[h]);g=np.array([q*.95/(64*m[h]),-r/m[h] if h==1 else 0,-r/m[h] if h==2 else 0,-q/(64*m[h])]);se=np.sqrt(g@s@g/32);row=cell['ratios'][h-1];errs.extend([abs(r-row['ratio']),abs(se-row['SE'])]);grads.append(g);checks+=2
 cov=np.array(grads)@s@np.array(grads).T/32;errs.append(np.max(abs(cov-np.array(cell['joint_ratio_estimator_covariance']))));checks+=1
 errs.extend([np.max(abs(m-np.array(cell['mean']))),np.max(abs(s-np.array(cell['covariance'])))]);checks+=2
for row in report['comparisons']:
 a,b=[report['cells'][i]['ratios'][row['harmonic']-1] for i in row['cells']];d=a['ratio']-b['ratio'];se=np.hypot(a['SE'],b['SE']);errs.extend([abs(d-row['difference']),abs(se-row['SE'])]);checks+=2
 if bool(abs(d)>4*se)!=row['flag']:raise RuntimeError('flag')
if max(errs)>1e-10:raise RuntimeError(max(errs))
out={'status':'PASS','checks':checks,'maximum_residual':float(max(errs)),'analysis_sha':hashlib.sha256((p/'ANALYSIS.json').read_bytes()).hexdigest(),'flagged_comparisons':sum(r['flag'] for r in report['comparisons']),'precision_pass':sum(r['precision'] for c in report['cells'] for r in c['ratios']),'scope':'Recomputed all96rawshard batch-derived chain means, fulljoint covariance and frozen gates. Confirms failure; no dynamics rerun.'};q=Path(__file__).parent;(q/'POST.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
