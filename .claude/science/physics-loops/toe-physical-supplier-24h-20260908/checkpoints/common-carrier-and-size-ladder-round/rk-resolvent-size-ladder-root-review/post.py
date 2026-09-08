import pathlib,json,numpy as np,hashlib,math
p=pathlib.Path('/private/tmp/toe-24h-probes-20260908/rk-resolvent-size-ladder')
a=json.loads((p/'ANALYSIS.json').read_text());checks=0;worst=0.0;rowsout=[]
def check(v,msg):
 global checks
 checks+=1
 if not v:raise RuntimeError(msg)
def close(x,y,msg,atol=1e-8):
 global worst
 e=float(np.max(np.abs(np.asarray(x)-np.asarray(y))));worst=max(worst,e)
 check(e<=atol,msg+': '+str(e))
for idx,cell in enumerate(a['cells']):
 L,b=cell['L'],cell['burn'];M=3*L**3;chains=[];clips=np.zeros(6,dtype=int)
 alpha=np.array([v*2*np.sin(np.pi/L)**2 for v in [.25,.5,1]]+[.25,.5,1])
 for sh in range(4):
  meta=json.loads((p/f'L{L}_b{b}_shard{sh}.json').read_text())
  for rep in range(32):
   cid=20000+idx*128+sh*32+rep;f=p/f'L{L}_b{b}_shard{sh}'/f'chain{cid}.npz'
   check(hashlib.sha256(f.read_bytes()).hexdigest()==meta['rows'][rep]['sha'],'chain bytes')
   with np.load(f,allow_pickle=False) as d:
    o=d['origins'];y=d['products'];n=d['Nf'];lags=d['lags'];clip=d['clipped']
    u=np.random.default_rng(800000000+cid).random((64,6))
    # Independent inverse-CDF expression; match the implemented rounded geometric q.
    expected=np.floor(np.log1p(-u)/np.log(M/(M+alpha))).astype(np.int64)
    check(np.array_equal(expected,lags),'all geometric lag draws')
    check(np.array_equal(clip,lags>np.array(meta['caps'])) and np.all(y[clip]==0),'clipping semantics')
    clips+=clip.sum(axis=0)
    norms=[np.mean(np.einsum('ij,ij->i',o[:,6*h:6*h+6].conj(),o[:,6*h:6*h+6]).real) for h in range(2)]
    re=[];im=[]
    for h in range(2):
     for j in range(3):
      z=np.mean(np.sum(y[:,3*h+j,6*h:6*h+6],axis=1));re.append(z.real);im.append(z.imag)
    chains.append([n.mean(),*norms,*re,*im])
 X=np.array(chains);m=X.mean(axis=0);cov=np.cov(X,rowvar=False);N=128
 close(X,cell['joint_chain_means'],'raw chain statistics')
 close(cov,cell['joint_sample_covariance'],'joint sample covariance')
 close(clips,cell['clipped'],'clipping counts')
 gradients=[];rrows=[]
 for h in range(2):
  q2=4*np.sin(np.pi*[1,L//4][h]/L)**2;si=1+h
  av=q2*m[0]/(L**3*m[si]);ga=np.zeros(15);ga[0]=q2/(L**3*m[si]);ga[si]=-av/m[si]
  for j in range(3):
   al=alpha[3*h+j];yi=3+3*h+j;rv=m[yi]/(al*m[si]);gr=np.zeros(15);gr[yi]=1/(al*m[si]);gr[si]=-rv/m[si]
   vals=[av,rv,1/rv-al,(av+al)*rv];grads=[ga,gr,-gr/rv**2,rv*ga+(av+al)*gr]
   reported=cell['rows'][3*h+j]
   for name,val,grad in zip(['a','r','b_plugin','C_plugin'],vals,grads):
    se=np.sqrt(grad@cov@grad/N)
    close(val,reported[name],name+' value');close(se,reported[name+'_SE'],name+' SE')
    gradients.append(grad)
   check(reported['precision_nominal']==bool(4*np.sqrt(gr@cov@gr/N)<=.1*rv),'precision')
   rrows.append((rv,np.sqrt(gr@cov@gr/N)))
   if cell['primary']:
    rowsout.append(dict(L=L,burn=b,harmonic=[1,L//4][h],alpha=al,a=av,a_SE=reported['a_SE'],r=rv,r_SE=reported['r_SE'],q2=q2,scaled_a=av/q2,scaled_r=rv*q2,C=vals[3],C_SE=reported['C_plugin_SE']))
 gradients=np.array(gradients)
 close(gradients@cov@gradients.T,cell['influence_sample_covariance'],'full24gradient covariance',1e-7)
 # Exact chain-centered linearization, including correlations shared by all regulators.
 close((X-m)@gradients.T,cell['influences'],'all chain influence values')
for c in a['burn_comparisons']:
 candidates=[x for x in a['cells'] if x['L']==c['L'] and x['burn'] in [c['burn'],c['primary_burn']]]
 r,s=[next(z for z in x['rows'] if z['harmonic']==c['harmonic'] and z['alpha']==c['alpha']) for x in candidates]
 close(r['r']-s['r'],c['difference'],'burn contrast');close(math.hypot(r['r_SE'],s['r_SE']),c['SE'],'burn SE')
out=dict(status='PASS',checks=checks,max_absolute_error=worst,primary_rows=rowsout,scope='Raw chain gradients, lag generation and covariance independently reproduced; this is not a stationarity or provenance-closure certificate.',script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest())
pathlib.Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
