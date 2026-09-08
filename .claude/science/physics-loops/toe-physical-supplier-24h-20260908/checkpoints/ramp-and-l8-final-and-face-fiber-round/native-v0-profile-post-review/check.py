from pathlib import Path
import hashlib,json,math,itertools
import numpy as np
p=Path('/private/tmp/toe-24h-probes-20260908/native-v0-profile-design');d=p/'PROFILE_OUTPUT';checks=0
h=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
def req(x):
 global checks
 checks+=1
 if not x:raise RuntimeError('postreview failed')
f=json.loads((p/'FINAL_FREEZE.json').read_text());req(h(p/'FINAL_FREEZE.json')=='44a8b05bf0bbe99197d4a8d261c9dd20f40dd8dd0400dc475e702dec3c16ab3f')
for k,v in f.items():req(h(p/k)==v)
for k,v in json.loads((p/'RUNTIME.json').read_text())['files'].items():req(h(Path(k))==v)
r=json.loads((d/'RESULT.json').read_text());dispatch=json.loads((d/'DISPATCH.json').read_text());req(dispatch['exit']==0 and 0<dispatch['external_seconds']<30);req(0<r['rss_mib']<384);req(r==json.loads((d/'stdout').read_text()));req(r['freeze']==h(p/'FINAL_FREEZE.json'))
components=0.;rates=[]
for idx,(c,V) in enumerate(zip(r['cases'],(.95,0.))):
 req(c['V']==V and c['L']==8 and c['n']==110592);req(c['initializer']['rk_proposals']==2048*1536 and c['initializer']['Q_steps']==110592)
 for key in ('initialization_seconds','warmup_seconds','measured_seconds','checkpoint_seconds'):
  req(math.isfinite(c[key]) and c[key]>0);components+=c[key]
 req(h(d/f'case{idx}.npz')==c['checkpoint_sha'])
 with np.load(d/f'case{idx}.npz',allow_pickle=False) as z:
  meta=json.loads(str(z['metadata']));states=z['states'];nf=z['nf'];obs=z['O'];req(meta['V']==V and meta['n']==110592 and meta['L']==8)
  prefix=meta['accumulator'];req(prefix['step']==12288 and prefix['snapshots']==5);req(prefix['raw']==c['state']['raw'][:5])
  # Literal physical link formula, independently built from integer coordinates.
  L=8;rs=list(itertools.product(range(L),repeat=3));ix=lambda r,a:3*((r[0]*L+r[1])*L+r[2])+a
  faces=[]
  for a,b in ((0,1),(0,2),(1,2)):
   for t in rs:
    ta=list(t);tb=list(t);ta[a]=(ta[a]+1)%L;tb[b]=(tb[b]+1)%L;faces.append([ix(t,a),ix(ta,b),ix(tb,a),ix(t,b)])
  for j,x in enumerate(states):
   zbits=x[np.array(faces)];actual=((zbits[:,0]==zbits[:,2])&(zbits[:,1]==zbits[:,3])&(zbits[:,0]!=zbits[:,1])).sum();req(actual==nf[j])
   oo=[sum((-1)**sum(t)*np.exp(2j*np.pi*hh*t[a]/L)*(float(x[ix(t,pol)])-.5) for t in rs)/math.sqrt(L**3) for hh in (1,2) for a in range(3) for pol in range(3) if pol!=a];req(np.max(abs(obs[j]-oo))<1e-9)
 for s in (prefix,c['state']):
  raw=np.array(s['raw']);req(raw.shape==(s['snapshots'],154) and np.isfinite(raw).all());req(np.allclose(np.array(s['batch']).sum(0),raw.sum(0),atol=1e-8,rtol=0))
  req(s['accepted']+s['rejections']==s['step']);req(len(s['runs'])==s['rejections']);req(sum(s['runs'])+s['run']==s['accepted']);u=lo=hi=0;direction=1
  for length in s['runs']+[s['run']]:
   u+=direction*length;lo=min(lo,u);hi=max(hi,u);direction=-direction
  req((u,lo,hi)==(s['u'],s['lo'],s['hi']))
  step=u=lo=hi=tags=0;direction=1
  for k,length in enumerate(s['runs']+[s['run']]):
   for _ in range(length):
    step+=1;u+=direction;lo=min(lo,u);hi=max(hi,u)
    if step>4096 and (step-4096)%1536==0:tags+=int(hi<=u+110592//2<=110592+lo)
   if k<len(s['runs']):
    step+=1;direction=-direction
    if step>4096 and (step-4096)%1536==0:tags+=int(hi<=u+110592//2<=110592+lo)
  req(tags==s['tagged_snapshots'] and step==s['step'])
  req(np.allclose(raw[:,7],raw[:,1]**2) and np.allclose(raw[:,8],raw[:,2]**2));req(np.allclose(raw[:,5],raw[:,1]*raw[:,3]) and np.allclose(raw[:,6],raw[:,2]*raw[:,3]))
  req(np.allclose(raw[:,57:81],raw[:,9:33]**2) and np.allclose(raw[:,81:105],raw[:,33:57]**2));req(np.allclose(raw[:,105:129],raw[:,9:33]**4) and np.allclose(raw[:,129:153],raw[:,33:57]**4))
 req(c['state']['step']==28672 and c['state']['snapshots']==16)
req(components<=dispatch['external_seconds']);overhead=dispatch['external_seconds']-components;rows=[]
for c in r['cases']:
 for tau in (12,36):
  n=3072*tau;segments=[1.5*(c['measured_seconds']/24576*length+c['checkpoint_seconds']+overhead+(c['initialization_seconds'] if j==0 else 0)) for j,length in enumerate((24*n,24*n,16*n))];rows.append(segments)
total=16*sum(map(sum,rows));maximum=max(map(max,rows));forecast=json.loads((d/'FORECAST.json').read_text());req(abs(total-forecast['forecast_seconds'])<1e-9 and abs(maximum-forecast['max_segment_seconds'])<1e-9);req(forecast['gate']==(total<=11520 and maximum<=160))
out={'checks':checks,'forecast_seconds':total,'max_segment_seconds':maximum,'external_seconds':dispatch['external_seconds'],'scope':'Independent raw replay, no author code imported or stochastic execution','hashes':{x.name:h(x) for x in d.iterdir() if x.is_file()}};Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='hashes'})
