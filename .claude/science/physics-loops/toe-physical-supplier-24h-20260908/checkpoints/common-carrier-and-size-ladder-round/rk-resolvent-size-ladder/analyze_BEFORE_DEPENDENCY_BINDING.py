import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import json,pathlib,hashlib,math
from fractions import Fraction as F
import numpy as np
P=pathlib.Path(__file__).resolve().parent
CELLS=[(8,32),(8,128),(8,512),(16,32),(16,128),(16,2048)]
def require(c,msg):
 if not c:raise ValueError(msg)
def decode(path):
 def pairs(items):
  d={}
  for k,v in items:
   require(k not in d,'duplicate JSON key');d[k]=v
  return d
 return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=lambda s: (_ for _ in ()).throw(ValueError('nonfinite JSON')))
def validate(m,d,L,b,sh,rep):
 cid=20000+128*CELLS.index((L,b))+32*sh+rep
 require(m['L']==L and m['burn']==b and m['shard']==sh and m['profile'] is False and m['chains']==32 and m['origins_per_chain']==64,'cell binding')
 require(m['source_sha']==hashlib.sha256((P/'stream.py').read_bytes()).hexdigest(),'source hash')
 require(0<m['total_seconds']<180 and 0<m['rss_mib']<384,'resources')
 require(len(m['rows'])==32 and [r['cid'] for r in m['rows']]==list(range(cid-rep,cid-rep+32)),'chain coverage')
 expected_modes=[[h,a,b_] for h in [1,L//4] for a in range(3) for b_ in range(3) if a!=b_]
 require(m['modes']==expected_modes,'modes')
 alphas=[k*2*np.sin(np.pi/L)**2 for k in [.25,.5,1]]+[.25,.5,1.]
 require(np.array_equal(m['alphas'],alphas),'regulators')
 caps=[]
 for j,alpha in enumerate(alphas):
  aa=F(float(alpha));n=0
  while F(1,2**n)/aa>F(1,1000):n+=1
  z=(3*L**3+aa)/aa*F(7*n,10);kp=(z.numerator+z.denominator-1)//z.denominator;caps.append(kp-1)
  require(m['certificates'][j]==dict(n=n,alpha_num=aa.numerator,alpha_den=aa.denominator,bound=float(F(1,2**n)/aa)),'tail certificate')
 require(m['caps']==caps,'caps')
 require(set(d)=={'origins','products','Nf','lags','clipped'},'raw keys')
 o,y,nf,k,c=[d[n] for n in ['origins','products','Nf','lags','clipped']]
 require(o.shape==(64,12) and y.shape==(64,6,12) and nf.shape==(64,) and k.shape==(64,6) and c.shape==k.shape,'raw coverage')
 require(np.iscomplexobj(o) and np.iscomplexobj(y) and np.isfinite(o).all() and np.isfinite(y).all(),'finite complex')
 require(np.issubdtype(nf.dtype,np.integer) and np.all((nf>=0)&(nf<=3*L**3)) and np.issubdtype(k.dtype,np.integer) and np.all(k>=0) and c.dtype==np.bool_,'integer raw')
 require(np.array_equal(c,k>caps) and np.all(y[c]==0),'discard semantics')
 return cid

def summarize(N,S,Y,I,L):
 # Shapes chain, harmonic[,regulator]; independent chain units only.
 rows=[];raw=np.column_stack([N,S,Y.reshape(len(N),6),I.reshape(len(N),6)]);infs=[];labels=[]
 for h in range(2):
  sm=S[:,h].mean();qh=4*np.sin(np.pi*([1,L//4][h])/L)**2;validS=sm>0
  am=qh*N.mean()/L**3/sm if validS else None
  ia=(qh*(N-N.mean())/L**3-am*(S[:,h]-sm))/sm if validS else None
  for j,kappa in enumerate([.25,.5,1]):
   alpha=kappa*qh/2 if h==0 else kappa;ym=Y[:,h,j].mean();valid=validS and ym>0
   r=dict(harmonic=[1,L//4][h],alpha=alpha,S=float(sm),Nf=float(N.mean()),Y=float(ym),negative_chain_Y=int(sum(Y[:,h,j]<0)),imaginary_mean=float(I[:,h,j].mean()),valid=bool(valid))
   if valid:
    rr=ym/(alpha*sm);ir=(Y[:,h,j]-ym-alpha*rr*(S[:,h]-sm))/(alpha*sm);ic=rr*ia+(am+alpha)*ir;ib=-ir/rr**2
    vals=[am,rr,1/rr-alpha,(am+alpha)*rr];vec=[ia,ir,ib,ic]
    for name,val,iv in zip(['a','r','b_plugin','C_plugin'],vals,vec):
     se=float(np.std(iv,ddof=1)/np.sqrt(len(N)));r[name]=float(val);r[name+'_SE']=se;infs.append(iv);labels.append([h,j,name])
    r['precision_nominal']=bool(4*r['r_SE']<=.1*rr)
   rows.append(r)
 return dict(rows=rows,joint_chain_means=raw.tolist(),joint_labels=['Nf','S1','Smatched']+[f'Y{h}{j}' for h in range(2) for j in range(3)]+[f'ImY{h}{j}' for h in range(2) for j in range(3)],joint_sample_covariance=np.cov(raw,rowvar=False).tolist(),influence_labels=labels,influence_sample_covariance=np.cov(infs).tolist() if infs else [],influences=np.array(infs).T.tolist() if infs else [])
def main():
 allout=[]
 for L,b in CELLS:
  N=[];S=[];Y=[];I=[];clips=np.zeros(6,int)
  for sh in range(4):
   folder=P/f'L{L}_b{b}_shard{sh}';m=decode(P/f'L{L}_b{b}_shard{sh}.json')
   for rep,row in enumerate(m['rows']):
    f=folder/f"chain{row['cid']}.npz";require(hashlib.sha256(f.read_bytes()).hexdigest()==row['sha'],'raw hash')
    with np.load(f,allow_pickle=False) as d:
     validate(m,d,L,b,sh,rep);o=d['origins'];y=d['products'];N.append(d['Nf'].mean());clips+=d['clipped'].sum(0)
     S.append([np.sum(abs(o[:,h*6:(h+1)*6])**2,axis=1).mean() for h in range(2)])
     Y.append([[y[:,h*3+j,h*6:(h+1)*6].real.sum(1).mean() for j in range(3)] for h in range(2)])
     I.append([[y[:,h*3+j,h*6:(h+1)*6].imag.sum(1).mean() for j in range(3)] for h in range(2)])
  require(len(N)==128,'logical coverage');out=summarize(np.array(N),np.array(S),np.array(Y),np.array(I),L);out.update(L=L,burn=b,primary=b in [512,2048],clipped=clips.tolist());allout.append(out)
 comparisons=[]
 for L in [8,16]:
  group=[c for c in allout if c['L']==L];primary=group[-1]
  for control in group[:-1]:
   for r,s in zip(control['rows'],primary['rows']):
    if r['valid'] and s['valid']:
     diff=r['r']-s['r'];se=math.hypot(r['r_SE'],s['r_SE']);comparisons.append(dict(L=L,burn=control['burn'],primary_burn=primary['burn'],harmonic=r['harmonic'],alpha=r['alpha'],difference=diff,SE=se,flag=abs(diff)>4*se))
 (P/'ANALYSIS.json').write_text(json.dumps(dict(cells=allout,burn_comparisons=comparisons,scope='finite-regulator finite-chain diagnostics, no certified spectral bounds'),indent=2,allow_nan=False)+'\n')
if __name__=='__main__':main()
