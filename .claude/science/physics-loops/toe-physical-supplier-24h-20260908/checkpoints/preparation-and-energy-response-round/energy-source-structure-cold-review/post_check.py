from pathlib import Path
import json,numpy as np,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/energy-source-structure');a=json.loads((p/'PRODUCTION_ANALYSIS.json').read_text());checks=0;out=[];hashes={}
for pop in (1024,2048):
 cells=[]
 for c in range(7):
  f=p/f'production_p{pop}_c{c}.json';r=json.loads(f.read_text());hashes[f.name]=hashlib.sha256(f.read_bytes()).hexdigest();cells.append(r)
  assert len(r['replicas'])==16 and r['population']==pop
  for j,s in enumerate(r['replicas']):
   assert s['seed']==3400000+(pop==2048)*10000+j and s['postconditions'];checks+=1
   e=(r['V']-1)*np.array(s['Nf_window'])+r['lambda']*np.array(s['X_window']);assert len(e)==40 and np.max(abs(e-s['energy_window']))<1e-12 and abs(e.mean()-s['physical_energy'])<1e-12;checks+=1
 E=np.array([[s['physical_energy'] for s in c['replicas']] for c in cells]).T
 B=.95*(E[:,2]-E[:,0])/.04-E[:,1];rows=[];influences=[]
 for h,mi,pl in ((.02,3,4),(.01,5,6)):
  T=(E[:,pl]-E[:,mi])/(2*h);mu=.5*B.mean()/T.mean();grad=np.array([.5/T.mean(),-.5*B.mean()/T.mean()**2]);se=np.sqrt(grad@np.cov(np.stack([B,T]),ddof=1)@grad/16)
  target=next(x for x in a['populations'][str(pop)]['moments'] if x['h']==h);assert abs(mu-target['value'])<1e-12 and abs(se-target['SE'])<1e-12;checks+=1
  forward=(E[:,pl]-E[:,1])/h;back=(E[:,1]-E[:,mi])/h
  rows.append({'h':h,'mu':mu,'SE':se,'forward':forward.mean(),'backward':back.mean(),'reversed':int(sum(forward>back))});influences.append(grad[0]*(B-B.mean())+grad[1]*(T-T.mean()))
 ss=np.std(influences[0]-influences[1],ddof=1)/4;assert abs(ss-a['populations'][str(pop)]['paired_step_sensitivity']['SE'])<1e-12;checks+=1
 out.append({'population':pop,'rows':rows,'paired_step_SE':ss})
for n in ['PRODUCTION_REPORT.md','PRODUCTION_ANALYSIS.json','STOCHASTIC_PROTOCOL.md','tilted_kernel.py','production.py','analyze_production.py']:hashes[n]=hashlib.sha256((p/n).read_bytes()).hexdigest()
res={'checks':checks,'results':out,'hashes':hashes};Path(__file__).with_name('POST_RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({'checks':checks,'results':out,'report_hash':hashes['PRODUCTION_REPORT.md']}))
