import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import pathlib,json,hashlib,math
import numpy as np
P=pathlib.Path(__file__).resolve().parent
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
 z=r['initializer'];req(z['rk_sweeps']==rk and z['rk_proposals']==rk*1536 and z['Q_steps']==n and type(z['nonself_Q_steps']) is int and 0<=z['nonself_Q_steps']<=n and z['law']=='finite RK start followed by productQ; not equilibrium productG path law','initializer')

def stats(a):
 m=a.mean(0);rows=[];ivs=[];labels=[]
 for h,q in [(1,2-np.sqrt(2)),(2,2)]:
  S=m[h];valid=S>0;r=dict(harmonic=h,valid=bool(valid),negative_chain_S=int(sum(a[:,h]<=0)))
  if valid:
   D=q*(.95*m[0]-m[3])/(512*S);C=m[4+h]/S-m[3];VH=m[4]-m[3]**2;VX=m[6+h]-S*S
   gd=np.zeros(9);gd[0]=q*.95/(512*S);gd[3]=-q/(512*S);gd[h]=-D/S;gc=np.zeros(9);gc[4+h]=1/S;gc[h]=-m[4+h]/S**2;gc[3]=-1;gh=np.zeros(9);gh[4]=1;gh[3]=-2*m[3];gx=np.zeros(9);gx[6+h]=1;gx[h]=-2*S
   for name,value,grad in [('D',D,gd),('R',D+C,gd+gc),('correction',C,gc),('VarH',VH,gh),('VarX',VX,gx)]:
    iv=(a-m)@grad;se=iv.std(ddof=1)/np.sqrt(16);r[name]=float(value);r[name+'_SE']=float(se);ivs.append(iv);labels.append([h,name])
   r['D_precision']=bool(D>0 and 4*r['D_SE']<=.1*D);r['residual_status']='resolved' if abs(C)>4*r['correction_SE'] else 'indeterminate';r['variance_status']='positive_resolved' if VH>4*r['VarH_SE'] else 'indeterminate';r['bound_plugin']=None if VH<0 or VX<0 else float(np.sqrt(VH*VX)/S)
  rows.append(r)
 iv=np.array(ivs).T;cov=np.cov(iv,rowvar=False)/16 if iv.shape[1] else []
 return dict(mean=m.tolist(),chain_covariance=np.cov(a,rowvar=False).tolist(),rows=rows,influence_labels=labels,chain_influences=iv.tolist(),estimator_covariance=np.asarray(cov).tolist())
