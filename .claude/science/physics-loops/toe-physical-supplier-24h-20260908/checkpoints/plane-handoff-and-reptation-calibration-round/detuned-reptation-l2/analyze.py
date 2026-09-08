import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import pathlib,json,hashlib,math
import numpy as np
P=pathlib.Path(__file__).resolve().parent
CELLS=[(48,8),(48,32),(48,0),(192,8),(192,32),(192,0),(768,8),(768,32),(768,0)]
def req(c,s):
 if not c:raise ValueError(s)
def validate(x,cell):
 n,m=CELLS[cell];req(x['cell']==cell and x['n']==n and x['burn_multiplier']==m and x['chains']==32 and x['updates']==65536 and x['batches']==16,'coverage')
 req(x['source_sha']==hashlib.sha256((P/'production.py').read_bytes()).hexdigest() and x['graph_sha']==hashlib.sha256((P/'graph.py').read_bytes()).hexdigest(),'sources')
 req(x['initializer_sha']==hashlib.sha256((P/'initializer.py').read_bytes()).hexdigest(),'initializer')
 req(0<x['seconds']<180 and 0<x['rss_mib']<384,'resources');a=np.asarray(x['means']);b=np.asarray(x['batch_means']);req(a.shape==(32,3) and b.shape==(32,16,3) and np.isfinite(a).all() and np.isfinite(b).all(),'finite shapes');req(np.max(abs(a-b.mean(1)))<1e-12,'batch consistency')
 req(len(x['counters'])==32 and [c['cid'] for c in x['counters']]==list(range(cell*32,(cell+1)*32)),'chain IDs')
 for c in x['counters']:req(0<=c['accepted']<=65536 and 0<=c['rejections']<=65536 and c['accepted']+c['rejections']==65536 and 0<=c['accepted_self']<=min(c['self_proposals'],c['accepted']) and c['self_proposals']<=65536,'events')
 return a,b
def main():
 freeze=json.loads((P/'PRODUCTION_FREEZE.json').read_text());req(hashlib.sha256((P/'MICRO.json').read_bytes()).hexdigest()==freeze['MICRO.json'],'oracle hash')
 oracle=json.loads((P/'MICRO.json').read_text())['oracle'];req([r['n'] for r in oracle]==[48,192,768] and all(np.isfinite(r['finite_dirichlet']) and r['finite_dirichlet']>0 for r in oracle),'oracle targets');out=[]
 for cell,(n,m) in enumerate(CELLS):
  x=json.loads((P/f'cell{cell}.json').read_text());a,b=validate(x,cell);mean=a.mean(0);valid=mean[1]>0;row=dict(cell=cell,n=n,burn_multiplier=m,mean=mean.tolist(),covariance=np.cov(a,rowvar=False).tolist(),valid=bool(valid),chain_means=a.tolist(),nonpositive_chain_S=int(sum(a[:,1]<=0)),minimum_chain_S=float(min(a[:,1])),nonpositive_batch_S=int(np.sum(b[:,:,1]<=0)))
  if valid:
   ratio=.5*(.95*mean[0]-mean[2])/mean[1];influence=(.5*(.95*(a[:,0]-mean[0])-(a[:,2]-mean[2]))-ratio*(a[:,1]-mean[1]))/mean[1];se=np.std(influence,ddof=1)/np.sqrt(32);target=next(t['finite_dirichlet'] for t in oracle if t['n']==n)
   row.update(ratio=float(ratio),SE=float(se),target=target,consistency=bool(abs(ratio-target)<=4*se),precision=bool(4*se<=.1*target),influence=influence.tolist())
  diff=b[:,:8].mean(1)-b[:,8:].mean(1);row['paired_split_difference']=diff.mean(0).tolist();row['paired_split_SE']=(diff.std(0,ddof=1)/np.sqrt(32)).tolist();out.append(row)
 comparisons=[]
 for i,j in [(0,1),(0,2),(1,2),(3,4),(3,5),(4,5),(6,7),(6,8),(7,8)]:
  a,b=out[i],out[j]
  if a['valid'] and b['valid']:
   d=a['ratio']-b['ratio'];se=math.hypot(a['SE'],b['SE']);comparisons.append(dict(n=a['n'],arms=[a['burn_multiplier'],b['burn_multiplier']],difference=d,SE=se,flag=abs(d)>4*se))
 (P/'ANALYSIS.json').write_text(json.dumps(dict(cells=out,burn_comparisons=comparisons),indent=2,allow_nan=False)+'\n')
if __name__=='__main__':main()
