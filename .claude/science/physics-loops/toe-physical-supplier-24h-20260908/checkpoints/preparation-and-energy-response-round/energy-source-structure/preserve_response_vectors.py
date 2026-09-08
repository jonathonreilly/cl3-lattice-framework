"""Transparent derived bookkeeping, no reweighting or sample exclusion."""
from pathlib import Path
import json,numpy as np
p=Path(__file__).resolve().parent;out={}
for pop in [1024,2048]:
 cells=[json.loads((p/f'production_p{pop}_c{c}.json').read_text()) for c in range(7)]
 E=np.array([[r['physical_energy'] for r in c['replicas']] for c in cells]).T
 B=.95*(E[:,2]-E[:,0])/.04-E[:,1];rows=[]
 for r in range(16):
  entry={'replica':r,'seed':cells[0]['replicas'][r]['seed'],'energies_all7':E[r].tolist(),'B':float(B[r]),'sources':[]}
  for h,minus,plus in [(.02,3,4),(.01,5,6)]:
   entry['sources'].append({'h':h,'T':float((E[r,plus]-E[r,minus])/(2*h)),'forward_secant':float((E[r,plus]-E[r,1])/h),'backward_secant':float((E[r,1]-E[r,minus])/h)})
  rows.append(entry)
 out[str(pop)]=rows
(p/'REPLICA_RESPONSE_VECTORS.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
