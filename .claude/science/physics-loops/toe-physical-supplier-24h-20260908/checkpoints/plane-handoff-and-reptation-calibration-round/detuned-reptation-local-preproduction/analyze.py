import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import pathlib,json,hashlib,math
import numpy as np
P=pathlib.Path(__file__).resolve().parent;CELLS=[(4,8),(4,32),(12,8),(12,32),(36,8),(36,32)]
def req(c,s):
 if not c:raise ValueError(s)
def read(path):
 def pairs(items):
  d={}
  for k,v in items:req(k not in d,'duplicate JSON');d[k]=v
  return d
 return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=lambda s: (_ for _ in ()).throw(ValueError('nonfinite JSON')))
def validate(x,cell,sh):
 tau,burn=CELLS[cell];n=384*tau;req(x['micro'] is False and x['cell']==cell and x['shard']==sh and x['L']==4 and x['V']==.95 and x['harmonics']==[1,2] and x['n']==n and x['tau']==tau and x['burn_multiplier']==burn and x['updates']==64*n and x['chains']==2,'metadata')
 req(x['source_sha']==hashlib.sha256((P/'production.py').read_bytes()).hexdigest() and x['core_sha']==hashlib.sha256((P/'core.py').read_bytes()).hexdigest(),'source');req(0<x['seconds']<180 and 0<x['rss_mib']<384,'resources');req(len(x['rows'])==2,'rows')
 for rep,r in enumerate(x['rows']):
  cid=32*cell+2*sh+rep;req(r['cid']==cid and r['seed']==202609160000+cid,'seed');a=np.array(r['mean']);b=np.array(r['batch_means']);req(a.shape==(4,) and b.shape==(16,4) and np.isfinite(a).all() and np.isfinite(b).all(),'finite');req(np.max(abs(a-b.mean(0)))<1e-9,'batchmean');c=r['counters'];req(0<=c['accepted']<=64*n and 0<=c['rejections']<=64*n and c['accepted']+c['rejections']==64*n and 0<=c['accepted_self']<=min(c['accepted'],c['self_proposals']) and c['self_proposals']<=64*n,'counts')
def main():
 cells=[]
 for cell,(tau,burn) in enumerate(CELLS):
  rows=[]
  for sh in range(16):
   x=read(P/f'cell{cell}_shard{sh}.json');validate(x,cell,sh);rows+=x['rows']
  a=np.array([r['mean'] for r in rows]);b=np.array([r['batch_means'] for r in rows]);m=a.mean(0);rr=[];ivs=[]
  for h,q2 in [(1,2.),(2,4.)]:
   valid=m[h]>0 and .95*m[0]-m[3]>0;r=dict(harmonic=h,valid=bool(valid),nonpositive_chain_S=int(sum(a[:,h]<=0)),nonpositive_batch_S=int(np.sum(b[:,:,h]<=0)))
   if valid:
    ratio=q2*(.95*m[0]-m[3])/(64*m[h]);iv=(q2*(.95*(a[:,0]-m[0])-(a[:,3]-m[3]))/64-ratio*(a[:,h]-m[h]))/m[h];se=iv.std(ddof=1)/np.sqrt(32);r.update(ratio=float(ratio),SE=float(se),precision=bool(4*se<=.1*ratio));ivs.append(iv)
   rr.append(r)
  if len(ivs)==2:req(np.allclose(np.diag(np.cov(ivs)/32),[r['SE']**2 for r in rr],rtol=1e-13,atol=1e-20),'estimator covariance diagonal')
  split=b[:,:8].mean(1)-b[:,8:].mean(1);cells.append(dict(cell=cell,tau=tau,burn_multiplier=burn,mean=m.tolist(),chain_vectors=a.tolist(),covariance=np.cov(a,rowvar=False).tolist(),ratios=rr,chain_ratio_influences=np.array(ivs).T.tolist() if ivs else [],chain_ratio_influence_covariance=np.cov(ivs).tolist() if len(ivs)==2 else [],joint_ratio_estimator_covariance=(np.cov(ivs)/32).tolist() if len(ivs)==2 else [],split_difference=split.mean(0).tolist(),split_SE=(split.std(0,ddof=1)/np.sqrt(32)).tolist()))
 comparisons=[]
 for i,j in [(0,1),(2,3),(4,5),(1,3),(3,5),(1,5)]:
  for r,s in zip(cells[i]['ratios'],cells[j]['ratios']):
   if r['valid'] and s['valid']:
    d=r['ratio']-s['ratio'];se=math.hypot(r['SE'],s['SE']);comparisons.append(dict(cells=[i,j],harmonic=r['harmonic'],difference=d,SE=se,flag=abs(d)>4*se))
 (P/'ANALYSIS.json').write_text(json.dumps(dict(cells=cells,comparisons=comparisons,scope='finite projection and overlapping-chain diagnostics; no exact L4 oracle'),indent=2,allow_nan=False)+'\n')
if __name__=='__main__':main()
