import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,hashlib
from pathlib import Path
p=Path('/private/tmp/toe-24h-probes-20260908/complex-source-l4');a=json.loads((p/'ANALYSIS.json').read_text());raw=np.load(p.parent/'ice-spectral-moments/pilot/L4_b128.npz')['values'];ref=np.array([[raw[r,:,6*k:6*k+6,2].sum(axis=1).mean() for k in range(2)] for r in range(32)]);checks=[];T={};maxres=0
for pop in [512,1024]:
 cells=[json.loads((p/f'production_p{pop}_c{i}.json').read_text()) for i in range(8)];X=np.array([[np.mean(cells[c]['replicas'][r]['energy_window']) for c in range(8)] for r in range(8)]);W=np.array([[np.mean(cells[c]['replicas'][r]['energy_window'][:20])-np.mean(cells[c]['replicas'][r]['energy_window'][20:]) for c in range(8)] for r in range(8)])
 ts=[]
 for j,(i,h) in enumerate([(0,.02),(2,.01),(4,.02),(6,.01)]):
  z=(X[:,i+1]-X[:,i])/(2*h);ts.append(z);mean=z.mean();se=np.sqrt(np.sum((z-mean)**2)/56);q=a['populations'][str(pop)]['rows'][j];rr=ref[:,j//2];err=np.sqrt(se**2+rr.var(ddof=1)/32);wd=(W[:,i+1]-W[:,i])/(2*h);gates=[abs(mean-rr.mean())<=4*err+1e-8,4*se<=.1*mean,abs(wd.mean())<=4*wd.std(ddof=1)/np.sqrt(8)+1e-8]
  if gates!=[q['consistency'],q['precision'],q['window_pass']]:raise AssertionError('gates')
  maxres=max(maxres,abs(mean-q['mean']),abs(se-q['SE']));checks+=gates
 T[pop]=np.array(ts).T
 for c,r in enumerate(cells):
  if not 0<r['seconds']<180 or not 0<r['rss_mib']<384:raise AssertionError('caps')
  for path,h in r['hashes'].items():
   if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=h:raise AssertionError('hash')
  for j,v in enumerate(r['replicas']):
   if v['seed']!=4500000+10000*(pop==1024)+j or not v['postconditions']:raise AssertionError('protocol')
   en=np.array(v['energy_window']);xx=np.array(v['X_window'])
   if len(en)!=40 or not np.isfinite(en).all() or max(abs(en-r['lambda_value']*xx))>1e-12:raise AssertionError('raw')
 for j in [0,2]:
  z=T[pop][:,j]-T[pop][:,j+1];checks.append(abs(z.mean())<=4*z.std(ddof=1)/np.sqrt(8)+1e-8)
for j in range(4):
 z=T[512][:,j];w=T[1024][:,j];checks.append(abs(z.mean()-w.mean())<=4*np.sqrt((z.var(ddof=1)+w.var(ddof=1))/8)+1e-8)
old=(p/'analyze_BEFORE_JSON_BOOL_FIX.py').read_text();new=(p/'analyze.py').read_text();assert old.replace('precise=valid and 4*err<=.1*mean','precise=bool(valid and 4*err<=.1*mean)')==new
print(json.dumps(dict(max_residual=maxres,nominal_gates=len(checks),all_pass=all(checks),reference_means=ref.mean(0).tolist(),hashes={n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ['PRODUCTION_REPORT.md','analyze.py','analyze_BEFORE_JSON_BOOL_FIX.py']}),indent=2))
