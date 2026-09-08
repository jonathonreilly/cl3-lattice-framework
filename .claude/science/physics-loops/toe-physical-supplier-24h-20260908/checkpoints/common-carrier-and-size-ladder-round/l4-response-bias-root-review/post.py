import pathlib,json,numpy as np,hashlib
p=pathlib.Path('/private/tmp/toe-24h-probes-20260908/l4-response-bias-discriminator')
a=json.loads((p/'ANALYSIS.json').read_text())
checks=0;worst=0.0
def equal(x,y,label):
 global checks,worst
 checks+=1
 err=float(np.max(np.abs(np.asarray(x)-np.asarray(y))))
 worst=max(worst,err)
 if err>1e-9:raise RuntimeError((label,err))
def ratio(E,b,t,f):
 m=E.mean(axis=0); cov=np.cov(E,rowvar=False)/len(E)
 B=b@m;T=t@m
 if T<=0:raise RuntimeError('nonpositive pooled response')
 grad=f*(b*T-B*t)/T**2
 return f*B/T,grad,cov
b=np.zeros(11);b[:3]=[-.95/.04,-1,.95/.04]
channels=[(3,4,.02,2/64),(5,6,.02,4/64),(7,8,.01,2/64),(9,10,.01,4/64)]
group_data=[]
for g in range(2):
 raw=[json.loads((p/f'g{g}_c{c}.json').read_text()) for c in range(11)]
 E=np.array([[r['energy_window'] for r in c['replicas']] for c in raw]).transpose(1,0,2)
 equal(E.mean(axis=2),a['groups'][g]['energy_vectors'],'actual window means')
 vals=[];grads=[]
 for j,(lo,hi,h,f) in enumerate(channels):
  t=np.zeros(11);t[lo]=-1/(2*h);t[hi]=1/(2*h)
  val,grad,cov=ratio(E.mean(axis=2),b,t,f);vals.append(val);grads.append(grad)
  row=a['groups'][g]['rows'][j]
  equal(val,row['value'],'ratio of energy responses')
  equal(np.sqrt(grad@cov@grad),row['SE'],'matrix delta SE')
  equal(E.mean(axis=2)@b,row['replica_B'],'replica B')
  equal(E.mean(axis=2)@t,row['replica_T'],'replica T')
  if row['precision']!=(4*np.sqrt(grad@cov@grad)<=.1*val):raise RuntimeError('precision')
  el=E[:,:,:20].mean(axis=2);er=E[:,:,20:].mean(axis=2)
  vl,gl,_=ratio(el,b,t,f);vr,gr,_=ratio(er,b,t,f)
  joint=np.cov(np.c_[el,er],rowvar=False)/8
  jointgrad=np.r_[gl,-gr]
  equal(vl-vr,row['half_window']['difference'],'half-window contrast')
  equal(np.sqrt(jointgrad@joint@jointgrad),row['half_window']['SE'],'joint half-window SE')
 grads=np.array(grads);rcov=grads@cov@grads.T
 equal(rcov,a['groups'][g]['ratio_mean_covariance'],'all four ratio covariance')
 group_data.append((np.array(vals),rcov))
for row in a['comparisons']:
 if row['kind']=='paired_step':
  g=[1024,2048].index(row['population']);j=row['harmonic']-1;vals,cov=group_data[g]
  v=np.zeros(4);v[j]=1;v[j+2]=-1
  d=v@vals;var=v@cov@v
 elif row['kind']=='population':
  j=row['channel'];d=group_data[0][0][j]-group_data[1][0][j];var=sum(z[1][j,j] for z in group_data)
 else:
  j=row['harmonic']-1;v=np.zeros(4);v[j]=1;v[j+2]=-1
  d=v@(group_data[0][0]-group_data[1][0]);var=sum(v@z[1]@v for z in group_data)
 equal(d,row['difference'],'sensitivity contrast');equal(np.sqrt(var),row['SE'],'sensitivity covariance')
refs=pathlib.Path('/private/tmp/toe-24h-probes-20260908/detuned-l4-pilot')
old=[json.loads((refs/f'cell_g2_v{i}.json').read_text()) for i in range(3)]
oldE=np.array([[r['mixed_energy'] for r in c['replicas']] for c in old]).T
oldB=oldE@np.array([-.95/.04,-1,.95/.04]);oldT=[]
for h in [1,2]:
 for F in [12,24]:
  oldT.append([np.mean([sum(z['C0_12'][6*(h-1):6*h]) for z in r['blocks'] if z['F']==F]) for r in old[1]['replicas']])
joint=np.c_[oldB,np.array(oldT).T];means=joint.mean(axis=0);jointcov=np.cov(joint,rowvar=False)/8;oldgrads=[]
for k,row in enumerate(a['old_references']):
 f=(2 if k<2 else 4)/64;den=means[k+1]
 grad=np.zeros(5);grad[0]=f/den;grad[k+1]=-f*means[0]/den**2;oldgrads.append(grad)
 equal(f*means[0]/den,row['value'],'old reference value');equal(np.sqrt(grad@jointcov@grad),row['SE'],'old reference SE')
oldcov=np.array(oldgrads)@jointcov@np.array(oldgrads).T
equal(oldcov,a['old_reference_mean_covariance'],'old shared covariance')
labels=a['method_difference_labels'];full=np.zeros((len(labels),len(labels)))
for i,(g,c,F) in enumerate(labels):
 k=(c%2)*2+[12,24].index(F)
 for j,(gg,cc,FF) in enumerate(labels):
  kk=(cc%2)*2+[12,24].index(FF)
  full[i,j]=oldcov[k,kk]+(group_data[g][1][c,cc] if g==gg else 0)
equal(full,a['method_difference_mean_covariance'],'full shared-reference comparison covariance')
out=dict(status='PASS',checks=checks,max_absolute_error=worst,scope='Independent energy-space gradients and joint covariance reproduce ratios, step/population/interaction and old shared-reference errors. No resolved bias mechanism.',script_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest())
pathlib.Path(__file__).with_name('POST_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
