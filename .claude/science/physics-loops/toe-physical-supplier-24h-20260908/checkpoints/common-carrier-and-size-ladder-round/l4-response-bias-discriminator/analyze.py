from pathlib import Path
import json,hashlib,numpy as np
p=Path(__file__).resolve().parent
cases=[(.93,1,0),(.95,1,0),(.97,1,0),(.95,1,-.02),(.95,1,.02),(.95,2,-.02),(.95,2,.02),(.95,1,-.01),(.95,1,.01),(.95,2,-.01),(.95,2,.01)]
channels=[(1,.02,3,4,2/64),(2,.02,5,6,4/64),(1,.01,7,8,2/64),(2,.01,9,10,4/64)]
def se(x):return float(np.std(x,ddof=1)/np.sqrt(8))
def ratio(b,t,f):
 if not np.isfinite(np.r_[b,t]).all():raise ValueError('nonfinite')
 if t.mean()<=0:return None
 v=float(f*b.mean()/t.mean());i=f/t.mean()*(b-b.mean()*t/t.mean());return v,i
refs=p.parent/'detuned-l4-pilot';rc=[json.loads((refs/f'cell_g2_v{i}.json').read_text()) for i in range(3)];re=np.array([[x['mixed_energy'] for x in c['replicas']] for c in rc]).T;rb=.95*(re[:,2]-re[:,0])/.04-re[:,1];refrows=[];refinfs=[]
for h in [1,2]:
 for F in [12,24]:
  t=np.array([np.mean([sum(z['C0_12'][6*(h-1):6*h]) for z in x['blocks'] if z['F']==F]) for x in rc[1]['replicas']]);v,i=ratio(rb,t,(2 if h==1 else 4)/64);refrows.append(dict(harmonic=h,F=F,value=v,SE=se(i)));refinfs.append(i)
bind=json.loads((p/'REFERENCE_BINDING.json').read_text())
for path,h in bind.items():
 if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=h:raise ValueError('reference changed')
groups=[];allr={};diffcov={}
for g,pop in enumerate([1024,2048]):
 raw=[json.loads((p/f'g{g}_c{c}.json').read_text()) for c in range(11)];E=[];halves=[]
 for c,r in enumerate(raw):
  V,h,lam=cases[c]
  if (r['L'],r['V'],r['harmonic'],r['lambda_value'],r['population'],r['burn'],r['group'],r['case'])!=(4,V,h,lam,pop,320,g,c) or len(r['replicas'])!=8 or not 0<r['seconds']<180 or not 0<r['rss_mib']<384:raise ValueError('metadata/resources')
  if not np.isfinite(r['shift']) or abs(r['shift']-96*abs(lam))>1e-12:raise ValueError('shift metadata')
  for path,d in r['hashes'].items():
   if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=d:raise ValueError('source')
  vals=[];half=[]
  for j,x in enumerate(r['replicas']):
   n=np.array(x['Nf_window']);z=np.array(x['X_window']);e=np.array(x['energy_window'])
   if x['seed']!=6000000+10000*g+j or x['replica']!=j or x['postconditions'] is not True or e.shape!=(40,) or n.shape!=(40,) or z.shape!=(40,) or not np.isfinite(np.r_[e,n,z]).all():raise ValueError('replica')
   if max(abs(e-((V-1)*n+lam*z)))>1e-12 or abs(e.mean()-x['physical_energy'])>1e-12 or abs(x['shifted_energy']+96*abs(lam)-e.mean())>1e-12:raise ValueError('energy')
   if not all(np.isfinite(x[k]) and 0<=x[k]<=1e-10 for k in ['cache_drift','final_literal_error']):raise ValueError('cache receipt')
   vals.append(e.mean());half.append([e[:20].mean(),e[20:].mean()])
  E.append(vals);halves.append(half)
 E=np.array(E).T;halves=np.array(halves).transpose(1,0,2);B=.95*(E[:,2]-E[:,0])/.04-E[:,1];rows=[];infs=[]
 for j,(h,step,mi,pl,f) in enumerate(channels):
  T=(E[:,pl]-E[:,mi])/(2*step);r=ratio(B,T,f);row=dict(harmonic=h,step=step,primary=step==.02,replica_B=B.tolist(),replica_T=T.tolist(),negative_B=int(np.sum(B<0)),nonpositive_T=int(np.sum(T<=0)),source_forward_secants=((E[:,pl]-E[:,1])/step).tolist(),source_backward_secants=((E[:,1]-E[:,mi])/step).tolist(),reversed_secants=int(np.sum((E[:,pl]-E[:,1])/step>(E[:,1]-E[:,mi])/step)),valid=r is not None)
  if r is not None:
   v,i=r;allr[g,j]=r;infs.append(i);row.update(value=v,SE=se(i),precision=bool(v>0 and 4*se(i)<=.1*v));comps=[]
   for k,rr in enumerate(refrows):
    if rr['harmonic']==h:
     err=np.hypot(se(i),rr['SE']);comps.append(dict(F=rr['F'],difference=v-rr['value'],SE=float(err),compatible=bool(abs(v-rr['value'])<=4*err+1e-8)))
   row['old_reference_comparisons']=comps
   bh=.95*(halves[:,2]-halves[:,0])/.04-halves[:,1];th=(halves[:,pl]-halves[:,mi])/(2*step);ra=ratio(bh[:,0],th[:,0],f);rbh=ratio(bh[:,1],th[:,1],f)
   row['half_window_valid']=ra is not None and rbh is not None
   if row['half_window_valid']:row['half_window']=dict(difference=ra[0]-rbh[0],SE=se(ra[1]-rbh[1]),compatible=bool(abs(ra[0]-rbh[0])<=4*se(ra[1]-rbh[1])+1e-8))
  rows.append(row)
 groups.append(dict(population=pop,energy_vectors=E.tolist(),energy_covariance=np.cov(E,rowvar=False).tolist(),rows=rows,ratio_mean_covariance=(np.cov(infs)/8).tolist() if len(infs)==4 else None))
comparisons=[]
for g in [0,1]:
 for j in [0,1]:
  if (g,j) in allr and (g,j+2) in allr:
   a,i=allr[g,j];b,k=allr[g,j+2];comparisons.append(dict(kind='paired_step',population=[1024,2048][g],harmonic=j+1,difference=a-b,SE=se(i-k)))
for j in range(4):
 if (0,j) in allr and (1,j) in allr:
  a,i=allr[0,j];b,k=allr[1,j];comparisons.append(dict(kind='population',channel=j,difference=a-b,SE=float(np.hypot(se(i),se(k)))))
for j in [0,1]:
 if all(key in allr for key in [(0,j),(0,j+2),(1,j),(1,j+2)]):
  a,i=allr[0,j];b,k=allr[0,j+2];c,l=allr[1,j];d,m=allr[1,j+2];comparisons.append(dict(kind='step_population_interaction',harmonic=j+1,difference=(a-b)-(c-d),SE=float(np.hypot(se(i-k),se(l-m)))))
for r in comparisons:r['compatible']=bool(abs(r['difference'])<=4*r['SE']+1e-8)
# Shared old reference adds SAME reference covariance to any cross-comparison.
labels=[];cinfs=[];ridx=[]
for (g,j),(v,i) in sorted(allr.items()):
 for k,rr in enumerate(refrows):
  if rr['harmonic']==channels[j][0]:labels.append([g,j,rr['F']]);cinfs.append((g,i));ridx.append(k)
cov=np.empty((len(labels),len(labels)))
for a,(ga,ia) in enumerate(cinfs):
 for b,(gb,ib) in enumerate(cinfs):cov[a,b]=(np.cov(ia,ib,ddof=1)[0,1]/8 if ga==gb else 0)+np.cov(refinfs[ridx[a]],refinfs[ridx[b]],ddof=1)[0,1]/8
print(json.dumps(dict(groups=groups,comparisons=comparisons,old_references=refrows,old_reference_mean_covariance=(np.cov(refinfs)/8).tolist(),method_difference_labels=labels,method_difference_mean_covariance=cov.tolist(),scope='finite diagnostic; no direct F-bias resolution; shifted energy algebraic'),indent=2,allow_nan=False))
