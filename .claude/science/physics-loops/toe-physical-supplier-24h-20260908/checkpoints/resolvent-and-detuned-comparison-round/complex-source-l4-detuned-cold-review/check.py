from pathlib import Path
import numpy as np,json,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/complex-source-l4-detuned');q=p.parent/'detuned-l4-pilot';a=json.loads((p/'ANALYSIS.json').read_text());res=[];ratios={};walls=[]
def calc(b,t,f):
 v=f*np.mean(b)/np.mean(t);i=f/np.mean(t)*(b-np.mean(b)*t/np.mean(t));return v,i,np.std(i,ddof=1)/np.sqrt(8)
def eq(x,y):
 if np.max(abs(np.array(x)-np.array(y)))>1e-10:raise AssertionError((x,y))
for g in range(3):
 c=[json.loads((p/f'cell_g{g}_c{i}.json').read_text()) for i in range(7)];E=np.array([[np.mean(c[j]['replicas'][r]['energy_window']) for j in range(7)] for r in range(8)]);half=np.array([[[np.mean(c[j]['replicas'][r]['energy_window'][s:s+20]) for s in [0,20]] for j in range(7)] for r in range(8)]);B=.95*(E[:,2]-E[:,0])/.04-E[:,1];eq(np.cov(E,rowvar=False),a['groups'][str(g)]['energy_sample_covariance']);infs=[]
 rc=[json.loads((q/f'cell_g{g}_v{i}.json').read_text()) for i in range(3)];RE=np.array([[x['mixed_energy'] for x in z['replicas']] for z in rc]).T;RB=.95*(RE[:,2]-RE[:,0])/.04-RE[:,1]
 for j,(mi,pl,f) in enumerate([(3,4,2/64),(5,6,4/64)]):
  T=(E[:,pl]-E[:,mi])/.04;v,inf,se=calc(B,T,f);r=a['groups'][str(g)]['moments'][j];eq([v,se],[r['value'],r['SE']]);eq(B,r['replica_B']);eq(T,r['replica_T']);infs.append(inf);ratios[g,j]=(v,se)
  for n,F in enumerate([24,12]):
   RT=np.array([np.mean([sum(z['C0_12'][6*j:6*j+6]) for z in x['blocks'] if z['F']==F]) for x in rc[1]['replicas']]);rv,ri,rse=calc(RB,RT,f);rr=r['reference_comparisons'][n];eq([rv,rse,v-rv,np.hypot(se,rse)],[rr['value'],rr['SE'],rr['difference'],rr['combined_SE']]);res.append(dict(group=g,harmonic=j+1,F=F,z=float((v-rv)/np.hypot(se,rse))))
  bh=.95*(half[:,2]-half[:,0])/.04-half[:,1];th=(half[:,pl]-half[:,mi])/.04;x,ii,_=calc(bh[:,0],th[:,0],f);y,jj,_=calc(bh[:,1],th[:,1],f);eq([x-y,np.std(ii-jj,ddof=1)/np.sqrt(8)],[r['window']['difference'],r['window']['SE']])
 eq(np.cov(infs)/8,a['groups'][str(g)]['ratio_mean_covariance'])
 for z in c:
  walls.append(z['seconds'])
  if not 0<z['rss_mib']<384 or not 0<z['seconds']<180:raise AssertionError('resources')
  for path,h in z['hashes'].items():
   if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=h:raise AssertionError('hash')
for g1,g2,name in [(0,1,'population'),(1,2,'burn')]:
 for j in [0,1]:
  v,s=ratios[g1,j];w,t=ratios[g2,j];r=next(r for r in a['group_comparisons'] if r['kind']==name and r['harmonic']==j+1);eq([v-w,np.hypot(s,t)],[r['difference'],r['SE']])
print(json.dumps(dict(all_recomputations_match=True,tolerance=1e-10,comparisons=res,max_child_seconds=max(walls),hashes={n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ['PRODUCTION_REPORT.md','ANALYSIS.json','analyze.py']}),indent=2))
