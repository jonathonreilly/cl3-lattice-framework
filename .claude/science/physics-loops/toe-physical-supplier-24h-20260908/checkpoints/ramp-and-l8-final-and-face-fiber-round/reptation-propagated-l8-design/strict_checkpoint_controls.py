import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,hashlib
from pathlib import Path
from checkpoint import load
p=Path(__file__).parent
with np.load(p/'ROUNDTRIP.npz',allow_pickle=False) as f:original={k:f[k].copy() for k in f.files}
killed=[]
for name in ['nan_O','float_labels','short_states','float_NF','wrong_L']:
 z={k:v.copy() for k,v in original.items()}
 if name=='nan_O':z['O'][0,0]=np.nan
 elif name=='float_labels':z['labels']=z['labels'].astype(float)
 elif name=='short_states':z['states']=z['states'][:2]
 elif name=='float_NF':z['nf']=z['nf'].astype(float)
 else:
  m=json.loads(str(z['metadata']));m['L']=4;z['metadata']=np.array(json.dumps(m))
 f=p/(name+'.npz');np.savez_compressed(f,**z)
 # Recomputed checksum is deliberately accepted; semantic validation must still fail.
 checksum=hashlib.sha256(f.read_bytes()).hexdigest()
 try:load(f,expected=dict(L=2,n=48))
 except ValueError:killed.append(dict(name=name,updated_sha=checksum))
 else:raise RuntimeError('mutant passed '+name)
(p/'STRICT_CHECKPOINT_CONTROLS.json').write_text(json.dumps(dict(killed=killed,not_production=True),indent=2)+'\n')
print(len(killed))
