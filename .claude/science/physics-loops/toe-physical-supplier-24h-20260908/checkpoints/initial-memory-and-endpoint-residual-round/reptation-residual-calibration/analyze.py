import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import json,pathlib,hashlib
import numpy as np
P=pathlib.Path(__file__).resolve().parent
NAMES=['D','R','correction','VarH','VarX']
def req(c,s):
 if not c:raise ValueError(s)
def values_grad(m):
 N,S,E,H2,XE,X2=m;req(S>0,'nonpositive pooled S');D=.5*(.95*N-E)/S;C=XE/S-E;VH=H2-E*E;VX=X2-S*S;gd=np.array([.475/S,-D/S,-.5/S,0,0,0]);gc=np.array([0,-XE/S**2,-1,0,1/S,0]);return np.array([D,D+C,C,VH,VX]),np.array([gd,gd+gc,gc,[0,0,-2*E,1,0,0],[0,-2*S,0,0,0,1]])
def validate(x,sh,graphsha):
 req(x['shard']==sh and x['V']==.95 and x['n']==2 and x['burn']==64 and x['chains']==8 and x['updates']==32768,'metadata');req(x['source_sha']==hashlib.sha256((P/'production.py').read_bytes()).hexdigest() and x['graph_sha']==graphsha,'sources');req(0<x['seconds']<180 and 0<x['rss_mib']<384,'resources');req(len(x['rows'])==8,'rows')
 for rep,r in enumerate(x['rows']):
  cid=8*sh+rep;req(r['cid']==cid and r['seed']==202609180000+cid,'seed');a=np.array(r['mean']);b=np.array(r['batch_means']);req(a.shape==(6,) and b.shape==(16,6) and np.isfinite(a).all() and np.isfinite(b).all(),'finite');req(np.max(abs(a-b.mean(0)))<1e-12,'batchmean');c=r['counts'];req(0<=c['accepted']<=32768 and 0<=c['rejected']<=32768 and c['accepted']+c['rejected']==32768 and 0<=c['accepted_self']<=min(c['accepted'],c['self_proposals']) and c['self_proposals']<=32768,'counts')
def main():
 f=json.loads((P/'PRODUCTION_FREEZE.json').read_text())
 for n,h in f.items():req(hashlib.sha256((P/n).read_bytes()).hexdigest()==h,'freeze')
 graphsha=f[str(P.parent/'detuned-reptation-l2/graph.py')];rows=[]
 for sh in range(4):
  x=json.loads((P/f'shard{sh}.json').read_text());validate(x,sh,graphsha);rows+=x['rows']
 a=np.array([r['mean'] for r in rows]);b=np.array([r['batch_means'] for r in rows]);m=a.mean(0);val,J=values_grad(m);iv=(a-m)@J.T;cov=np.cov(iv,rowvar=False)/32;SE=iv.std(0,ddof=1)/np.sqrt(32);req(np.allclose(np.diag(cov),SE**2,rtol=1e-13),'covariance')
 targetrow=next(r for r in json.loads((P/'MICRO.json').read_text())['oracle'] if r['n']==2);target,_=values_grad(targetrow['vector']);results=[]
 for i,n in enumerate(NAMES):results.append(dict(name=n,value=float(val[i]),SE=float(SE[i]),target=float(target[i]),consistency=bool(abs(val[i]-target[i])<=4*SE[i]),precision=bool(4*SE[i]<=(.25 if n in ['correction','VarH'] else .1)*abs(target[i]))))
 split=b[:,:8].mean(1)-b[:,8:].mean(1);out=dict(results=results,mean_vector=m.tolist(),chain_vectors=a.tolist(),chain_covariance=np.cov(a,rowvar=False).tolist(),chain_influences=iv.tolist(),estimator_covariance=cov.tolist(),nonpositive_chain_S=int(sum(a[:,1]<=0)),nonpositive_batch_S=int(np.sum(b[:,:,1]<=0)),bound_plugin=None if val[3]<0 or val[4]<0 else float(np.sqrt(val[3]*val[4])/m[1]),split_difference=split.mean(0).tolist(),split_SE=(split.std(0,ddof=1)/np.sqrt(32)).tolist(),scope='finite n2,Epsi reference; signed variances; no certified bound')
 (P/'ANALYSIS.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
if __name__=='__main__':main()
