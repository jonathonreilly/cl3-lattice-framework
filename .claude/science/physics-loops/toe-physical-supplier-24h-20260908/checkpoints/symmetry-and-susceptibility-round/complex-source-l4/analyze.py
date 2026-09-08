import json,hashlib
from pathlib import Path
import numpy as np
p=Path(__file__).resolve().parent

def require(v,msg):
 if not v:raise ValueError(msg)
def load(f):return json.loads(f.read_text(),parse_constant=lambda v:(_ for _ in ()).throw(ValueError(v)))
def se(x):return np.std(x,ddof=1)/np.sqrt(len(x))
def compare(diff,error):return bool(abs(diff)<=4*error+1e-8)

def main():
 refpath=p.parent/'ice-spectral-moments/pilot/L4_b128.npz';raw=np.load(refpath)['values'];ref=np.stack([raw[:,:,:6,2].sum(2).mean(1),raw[:,:,6:,2].sum(2).mean(1)],axis=1)
 require(ref.shape==(32,2) and np.isfinite(ref).all(),'reference');refcov=np.cov(ref,rowvar=False,ddof=1)/32
 result={};derivatives={};allpass=True
 for pop in (512,1024):
  cells=[load(p/f'production_p{pop}_c{c}.json') for c in range(8)];E=[];half=[]
  for c,r in enumerate(cells):
   h=1+c//4;lam=(-.02,.02,-.01,.01)[c%4]
   require((r['L'],r['V'],r['harmonic'],r['lambda_value'],r['case'],r['population'])==(4,1.,h,lam,c,pop),'cell metadata')
   require(r['shift']==96*abs(lam) and len(r['replicas'])==8 and 0<r['seconds']<180 and 0<r['rss_mib']<384,'cell limits')
   for path,digest in r['hashes'].items():require(hashlib.sha256(Path(path).read_bytes()).hexdigest()==digest,'source changed')
   es=[];hs=[]
   for j,v in enumerate(r['replicas']):
    require(v['replica']==j and v['seed']==4500000+10000*(pop==1024)+j and v['postconditions'] is True,'replica')
    x=np.array(v['X_window']);e=np.array(v['energy_window']);n=np.array(v['Nf_window'])
    require(x.shape==e.shape==n.shape==(40,) and np.isfinite(np.r_[x,e,n]).all(),'windows')
    require(np.max(abs(lam*x-e))<1e-12 and abs(e.mean()-v['physical_energy'])<1e-12 and abs(v['shifted_energy']+r['shift']-e.mean())<1e-12,'energy shift')
    require(np.isfinite(v['cache_drift']) and v['cache_drift']<=1e-10 and np.isfinite(v['final_literal_error']) and v['final_literal_error']<=1e-10,'cache')
    es.append(e.mean());hs.append([e[:20].mean(),e[20:].mean()])
   E.append(es);half.append(hs)
  E=np.array(E).T;half=np.array(half).transpose(1,0,2);T=np.stack([(E[:,i+1]-E[:,i])/(2*h) for i,h in ((0,.02),(2,.01),(4,.02),(6,.01))],axis=1);derivatives[pop]=T
  rows=[]
  for m,(i,h) in enumerate(((0,.02),(2,.01),(4,.02),(6,.01))):
   harmonic=1+m//2;v=T[:,m];mean=v.mean();err=se(v);reference=ref[:,harmonic-1].mean();combined=np.sqrt(err**2+refcov[harmonic-1,harmonic-1]);diff=mean-reference
   valid=bool(np.isfinite(mean) and mean>0);consistent=valid and compare(diff,combined);precise=bool(valid and 4*err<=.1*mean)
   hd=((half[:,i+1,0]-half[:,i,0])-(half[:,i+1,1]-half[:,i,1]))/(2*h);windowpass=compare(hd.mean(),se(hd));allpass=allpass and consistent and precise and windowpass
   rows.append(dict(harmonic=harmonic,h=h,mean=float(mean),SE=float(err),valid=valid,minimum_replica=float(v.min()),nonpositive_replicas=int(sum(v<=0)),reference=float(reference),combined_SE=float(combined),consistency=consistent,precision=precise,window_difference=float(hd.mean()),window_SE=float(se(hd)),window_pass=windowpass))
  steps=[]
  for j in (0,2):
   d=T[:,j]-T[:,j+1];ok=compare(d.mean(),se(d));allpass=allpass and ok;steps.append(dict(harmonic=1+j//2,difference=float(d.mean()),SE=float(se(d)),pass_nominal=ok))
  result[str(pop)]=dict(rows=rows,energy_sample_covariance=np.cov(E,rowvar=False,ddof=1).tolist(),derivative_sample_covariance=np.cov(T,rowvar=False,ddof=1).tolist(),replica_derivatives=T.tolist(),paired_steps=steps)
 comparisons=[]
 for m in range(4):
  x=derivatives[512][:,m];y=derivatives[1024][:,m];err=np.hypot(se(x),se(y));ok=compare(x.mean()-y.mean(),err);allpass=allpass and ok;comparisons.append(dict(channel=m,difference=float(x.mean()-y.mean()),SE=float(err),pass_nominal=ok))
 out=dict(populations=result,reference_means=ref.mean(0).tolist(),reference_mean_covariance=refcov.tolist(),reference_sha256=hashlib.sha256(refpath.read_bytes()).hexdigest(),population_comparisons=comparisons,all_nominal_gates_pass=bool(allpass),scope='Finite paired-replica diagnostics, no mixing/source-bias certificate; no automatic next stage')
 (p/'ANALYSIS.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(out,allow_nan=False))
if __name__=='__main__':main()
