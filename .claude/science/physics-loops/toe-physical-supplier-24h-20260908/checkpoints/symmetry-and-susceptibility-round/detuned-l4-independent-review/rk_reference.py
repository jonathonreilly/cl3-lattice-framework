from pathlib import Path
import os,json,hashlib
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
p=Path(__file__).resolve().parent;s=p.parent/'ice-spectral-moments/pilot';out={}
for burn in [32,128]:
 raw=s/f'L4_b{burn}.npz';meta=json.loads((s/f'L4_b{burn}.json').read_text());v=np.load(raw)['values'];means=[]
 for h in [1,2]:
  ix=[i for i,m in enumerate(meta['modes']) if m[0]==h];means.append(v[:,:,ix,2].sum(2).mean(1))
 a=np.array(means);out[str(burn)]={'mean':a.mean(1).tolist(),'SE':(a.std(1,ddof=1)/np.sqrt(32)).tolist(),'chain_sample_covariance':np.cov(a,ddof=1).tolist(),'raw_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'scope':'independent-chain finite RK reference, not exact stationary oracle'}
(p/'RK_REFERENCE.json').write_text(json.dumps(out,indent=2)+'\n')
