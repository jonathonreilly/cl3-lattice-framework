import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import pathlib,json,hashlib,math
import numpy as np
P=pathlib.Path(__file__).resolve().parent;ARMS=[(12,128,32),(12,512,32),(36,512,8),(36,512,32)]
def req(c,s):
 if not c:raise ValueError(s)
def replay(n,runs,last,burn,updates):
 req(type(runs) is list and all(type(z) is int and z>=0 for z in runs+[last]),'run domains')
 req(sum(runs)+len(runs)+last==burn+updates,'attempt total')
 u=lo=hi=a=tagged=rejects=0;d=1;escape=None;bt=None
 for j,r in enumerate(runs+[last]):
  lower=hi-n//2;upper=lo+n//2
  left,right=(lower-u,upper-u) if d==1 else (u-upper,u-lower)
  left=max(1,left);right=min(r,right)
  tagged+=max(0,right-max(left,burn-a+1)+1)
  if escape is None and r:
   t=1 if left>1 or right<1 else right+1
   if t<=r:escape=a+t
  if a<burn<=a+r:
   ub=u+d*(burn-a);bt=max(0,n+min(lo,ub)-max(hi,ub)+1)
  u+=d*r;lo=min(lo,u);hi=max(hi,u);a+=r
  if j<len(runs):
   a+=1;inside=hi<=u+n//2<=n+lo
   if escape is None and not inside:escape=a
   if a==burn:bt=max(0,n+lo-hi+1)
   if a>burn:tagged+=int(inside);rejects+=1
   d=-d
 return dict(tagged_measurements=tagged,fraction=tagged/updates,burn_end_tags=bt,final_tags=max(0,n+lo-hi+1),first_escape=escape,u=u,lo=lo,hi=hi),rejects

def validate_history(r,n,rk,burn,updates):
 c=r['counters'];runs=c['run_lengths_including_burn'];last=c['unfinished_run']
 mem,rejects=replay(n,runs,last,burn,updates)
 req(r['memory']==mem,'replayed memory')
 for k in ['self_proposals','rejections','accepted','accepted_self','window_traversals_including_burn']:
  req(type(c[k]) is int and c[k]>=0,'counter domains')
 req(c['rejections']==rejects and c['accepted']==updates-rejects,'measured counters')
 req(c['accepted_self']<=min(c['accepted'],c['self_proposals']) and c['self_proposals']<=updates and c['self_proposals']-c['accepted_self']<=rejects,'self counters')
 req(c['window_traversals_including_burn']==sum(z//n for z in runs+[last]),'traversals')
 z=r['initializer'];req(z['rk_sweeps']==rk and z['rk_proposals']==rk*192 and z['Q_steps']==n and type(z['nonself_Q_steps']) is int and 0<=z['nonself_Q_steps']<=n and z['law']=='finite RK start followed by productQ; not equilibrium productG path law','initializer')

def validate(x,arm,sh):
 tau,rk,burn=ARMS[arm];n=384*tau;req(x['micro'] is False and x['cell']==arm and x['shard']==sh and x['L']==4 and x['V']==.95 and x['harmonics']==[1,2] and x['n']==n and x['tau']==tau and x['rk_sweeps']==rk and x['burn_multiplier']==burn and x['updates']==32*n and x['chains']==2,'metadata')
 for key,file in [('source_sha','production.py'),('core_sha','core.py'),('initializer_sha','initialize.py')]:req(x[key]==hashlib.sha256((P/file).read_bytes()).hexdigest(),'source')
 req(0<x['seconds']<180 and 0<x['rss_mib']<384 and len(x['rows'])==2,'resource/rows')
 for j,r in enumerate(x['rows']):
  cid=32*arm+2*sh+j;req(r['cid']==cid and r['seed']==202609190000+cid,'seeds');a=np.array(r['mean']);b=np.array(r['batch_means']);req(a.shape==(9,) and b.shape==(16,9) and np.isfinite(a).all() and np.isfinite(b).all(),'finite');req(np.max(abs(a-b.mean(0)))<1e-8,'batch');validate_history(r,n,rk,burn*n,32*n)
def stats(a):
 m=a.mean(0);rows=[];ivs=[];labels=[]
 for h,q in [(1,2),(2,4)]:
  S=m[h];valid=S>0;r=dict(harmonic=h,valid=bool(valid),negative_chain_S=int(sum(a[:,h]<=0)))
  if valid:
   D=q*(.95*m[0]-m[3])/(64*S);C=m[4+h]/S-m[3];VH=m[4]-m[3]**2;VX=m[6+h]-S*S
   gd=np.zeros(9);gd[0]=q*.95/(64*S);gd[3]=-q/(64*S);gd[h]=-D/S;gc=np.zeros(9);gc[4+h]=1/S;gc[h]=-m[4+h]/S**2;gc[3]=-1;gh=np.zeros(9);gh[4]=1;gh[3]=-2*m[3];gx=np.zeros(9);gx[6+h]=1;gx[h]=-2*S
   for name,value,grad in [('D',D,gd),('R',D+C,gd+gc),('correction',C,gc),('VarH',VH,gh),('VarX',VX,gx)]:
    iv=(a-m)@grad;se=iv.std(ddof=1)/np.sqrt(16);r[name]=float(value);r[name+'_SE']=float(se);ivs.append(iv);labels.append([h,name])
   r['D_precision']=bool(D>0 and 4*r['D_SE']<=.1*D);r['residual_status']='resolved' if abs(C)>4*r['correction_SE'] else 'indeterminate';r['variance_status']='positive_resolved' if VH>4*r['VarH_SE'] else 'indeterminate';r['bound_plugin']=None if VH<0 or VX<0 else float(np.sqrt(VH*VX)/S)
  rows.append(r)
 iv=np.array(ivs).T;cov=np.cov(iv,rowvar=False)/16 if iv.shape[1] else []
 return dict(mean=m.tolist(),chain_covariance=np.cov(a,rowvar=False).tolist(),rows=rows,influence_labels=labels,chain_influences=iv.tolist(),estimator_covariance=np.asarray(cov).tolist())
def main():
 f=json.loads((P/'PRODUCTION_FREEZE.json').read_text())
 for n,h in f.items():req(hashlib.sha256((P/n).read_bytes()).hexdigest()==h,'freeze')
 out=[]
 for arm in range(4):
  raw=[]
  for sh in range(8):
   x=json.loads((P/f'arm{arm}_shard{sh}.json').read_text());validate(x,arm,sh);raw+=x['rows']
  a=np.array([r['mean'] for r in raw]);s=stats(a);memory=[r['memory']['fraction'] for r in raw];s.update(arm=arm,parameters=ARMS[arm],chain_vectors=a.tolist(),tag_fractions=memory,memory_flag=bool(max(memory)>.01));out.append(s)
 comparisons=[]
 for i,j in [(0,1),(2,3),(1,3)]:
  for a,b in zip(out[i]['rows'],out[j]['rows']):
   if a['valid'] and b['valid']:
    for name in ['D','R','correction']:
     d=a[name]-b[name];se=math.hypot(a[name+'_SE'],b[name+'_SE']);comparisons.append(dict(arms=[i,j],harmonic=a['harmonic'],quantity=name,difference=d,SE=se,flag=abs(d)>4*se))
 status='fails_diagnostics' if any(s['memory_flag'] or any(not r.get('D_precision',False) for r in s['rows']) for s in out) or any(c['flag'] for c in comparisons) else 'passes_limited_diagnostics_not_convergence'
 (P/'ANALYSIS.json').write_text(json.dumps(dict(arms=out,comparisons=comparisons,status=status),indent=2,allow_nan=False)+'\n')
if __name__=='__main__':main()
