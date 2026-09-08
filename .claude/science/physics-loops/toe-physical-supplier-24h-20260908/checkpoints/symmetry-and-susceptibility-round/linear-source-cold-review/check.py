import json,hashlib
import numpy as np
from pathlib import Path
p=Path('/private/tmp/toe-24h-probes-20260908/infrared-discriminator/linear-source');a=json.loads((p/'ANALYSIS.json').read_text());out=[];checks=0
for pop in (128,256):
 cells=[json.loads((p/f'population_p{pop}_c{i}.json').read_text()) for i in range(7)];E=[]
 for c in cells:
  es=[]
  for r in c['rows']:
   e=-.05*np.array(r['Nf_window'])+c['xi']*np.array(r['F_window']);assert len(e)==40 and np.max(abs(e-r['energy_window']))<1e-12;es.append(e.mean());checks+=1
  E.append(es)
 E=np.array(E).T
 for j,h in enumerate((.01,.005,.0025)):
  z=(2*E[:,0]-E[:,2*j+1]-E[:,2*j+2])/h**2;mean=z.mean();se=z.std(ddof=1)/4;r=a['populations'][str(pop)]['curvatures'][j]
  assert abs(mean-r['chi'])<1e-8 and abs(se-r['SE'])<1e-8;checks+=1
  out.append(dict(population=pop,h=h,mean=mean,SE=se,precision=bool(mean>0 and 4*se<=.1*mean),negative=bool(mean<0)))
res=dict(checks=checks,rows=out,hashes={n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ['PRODUCTION_REPORT.md','ANALYSIS.json','POPULATION_STATUS.json']});Path(__file__).with_name('RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
