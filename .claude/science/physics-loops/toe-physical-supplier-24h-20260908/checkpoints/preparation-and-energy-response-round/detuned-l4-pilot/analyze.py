import json
from pathlib import Path
import numpy as np
p=Path(__file__).resolve().parent
load=lambda f:json.loads((p/f).read_text(),parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
se=lambda x:float(np.std(x,ddof=1)/np.sqrt(len(x)))
internal={};groups={}
for gi in range(3):
 cells=[load(f'cell_g{gi}_v{vi}.json') for vi in range(3)]
 for vi,c in enumerate(cells):
  assert c['group']==gi and c['V']==[.93,.95,.97][vi] and len(c['replicas'])==8
  assert 0<c['rss_mib']<384 and c['elapsed_seconds']<180
  for r in c['replicas']:assert all(all(v is True for v in f.values()) for f in r['postconditions'])
 E=np.array([[r['mixed_energy'] for r in c['replicas']] for c in cells]).T
 B=.95*(E[:,2]-E[:,0])/.04-E[:,1];rows=[]
 for harmonic in [1,2]:
  indices=[i for i,m in enumerate(cells[1]['modes']) if m[0]==harmonic];assert len(indices)==6
  for F in [12,24]:
   blocks=[[b for b in r['blocks'] if b['F']==F] for r in cells[1]['replicas']];assert all(len(b)==4 for b in blocks)
   raw=np.array([[np.array(b['C0_12'])[indices] for b in rb] for rb in blocks]);T=raw.sum(2).mean(1)
   factor=(2 if harmonic==1 else 4)/64;b=float(B.mean());t=float(T.mean());valid=b>0 and t>0
   row={'harmonic':harmonic,'q':'pi/2' if harmonic==1 else 'pi','F':F,'kinetic':b,'kinetic_SE':se(B),'S_six_means':raw.mean((0,1)).tolist(),'S_sum':t,'S_sum_SE':se(T),'minimum_origin_sum':float(raw.sum(2).min()),'nonpositive_origin_count':int((raw.sum(2)<=0).sum()),'valid':valid}
   if valid:
    mu=factor*b/t;infl=factor/t*((B-b)-(b/t)*(T-t));row.update(moment=mu,SE=se(infl),precision_nominal=4*se(infl)<=.1*abs(mu));internal[gi,harmonic,F]=(mu,infl)
   else:row['reason']='nonpositive numerator or denominator'
   rows.append(row)
 half=[]
 for vi,c in enumerate(cells):
  d=np.array([r['half_window_energy'][0]-r['half_window_energy'][1] for r in c['replicas']]);half.append({'V':c['V'],'difference':float(d.mean()),'SE':se(d),'exceeds4SE':bool(abs(d.mean())>4*se(d)+1e-8)})
 groups[str(gi)]={'population':cells[0]['population'],'burn':cells[0]['burn'],'energy_means':E.mean(0).tolist(),'energy_SE':[se(E[:,j]) for j in range(3)],'energy_covariance':np.cov(E,rowvar=False).tolist(),'moments':rows,'half_window':half}
comparisons=[]
for h in [1,2]:
 for name,a,b,paired in [('population',(0,h,24),(1,h,24),False),('burn',(1,h,24),(2,h,24),False),('forward',(2,h,12),(2,h,24),True)]:
  if a not in internal or b not in internal:comparisons.append({'name':name,'harmonic':h,'valid':False});continue
  x,ix=internal[a];y,iy=internal[b];s=se(ix-iy) if paired else float(np.hypot(se(ix),se(iy)))
  comparisons.append({'name':name,'harmonic':h,'difference':x-y,'SE':s,'exceeds4SE':abs(x-y)>4*s+1e-8,'paired':paired})
# Both momenta share a numerator and origins; report their paired covariance.
cross={}
for gi in range(3):
 if (gi,1,24) in internal and (gi,2,24) in internal:cross[str(gi)]=np.cov(internal[gi,1,24][1],internal[gi,2,24][1],ddof=1).tolist()
out={'groups':groups,'comparisons':comparisons,'harmonic_influence_covariance':cross,'scope':'No exact L4 consistency test; nominal precision/sensitivity only. Finite h, population, burn and forward errors unresolved.'}
(p/'ANALYSIS.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,indent=2))
