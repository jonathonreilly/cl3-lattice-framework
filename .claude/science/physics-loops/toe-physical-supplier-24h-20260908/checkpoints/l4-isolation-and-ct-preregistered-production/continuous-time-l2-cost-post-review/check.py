from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import json,hashlib,math
src=Path('/private/tmp/toe-24h-probes-20260908/continuous-time-l2-cost-profile');out=src/'PROFILE_OUTPUT';N=0
def need(c,m):
 global N
 N+=1
 if not c:raise RuntimeError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
freeze=json.loads((src/'FINAL_FREEZE.json').read_text())
for name,h in freeze['files'].items():need(sha(src/name)==h,'source hash '+name)
for name,h in json.loads((src/'RUNTIME.json').read_text())['files'].items():need(sha(Path(name))==h,'runtime '+name)
dis=json.loads((out/'DISPATCH.json').read_text());need(dis['freeze']==sha(src/'FINAL_FREEZE.json'),'dispatchfreeze');need(sha(out/'RESULT.json')==dis['result_sha'],'resultpin')
for f,h in dis['paths'].items():need(sha(out/f)==h,'rawpin')
vs=list(product(range(2),repeat=3));edges=[(v,a) for v in vs for a in range(3)];ei={e:i for i,e in enumerate(edges)}
def step(v,a):s=list(v);s[a]=1-s[a];return tuple(s)
faces=[(ei[v,a],ei[step(v,a),b],ei[step(v,b),a],ei[v,b]) for a,b in combinations(range(3),2) for v in vs]
seed=tuple(v[a] for v,a in edges)
def decode(x):return tuple((x>>e)&1 for e in range(24))
def legal(x,p):return all(x[faces[p][j]]!=x[faces[p][(j+1)%4]] for j in range(4))
def flip(x,p):
 need(legal(x,p),'literal event legality');y=list(x)
 for e in faces[p]:y[e]=1-y[e]
 for v in vs:need(sum(y[e] for e,(r,a) in enumerate(edges) if r==v or step(r,a)==v)==3,'literal degree')
 return tuple(y)
def nf(x):return sum(legal(x,p) for p in range(24))
r=json.loads((out/'RESULT.json').read_text());rows=[]
for cid in range(4):
 data=json.loads((out/f'path{cid}.json').read_text());initial=decode(int(data['initial'],16));x=seed
 for p in data['witness']:x=flip(x,p)
 need(x==initial,'witnessendpoint');T=F(float.fromhex(data['T']));events=[(F(float.fromhex(t)),p) for t,p in data['events']];last=F(0);integral=F(0);mid=x
 for t,p in events:
  need(last<t<T,'strict time');integral+=(t-last)*nf(x);x=flip(x,p)
  if t<=T/2:mid=x
  last=t
 integral+=(T-last)*nf(x);n=nf(mid);h0=F(-nf(initial),20);h1=F(-nf(x),20);eh=(h0+h1)/2
 X=F(sum(sum((-1)**(sum(v)+v[a])*(2*mid[e]-1) for e,(v,c) in enumerate(edges) if c==b)**2 for a in range(3) for b in range(3) if a!=b),32)
 overlap=F(sum((2*i-1)*(2*j-1) for i,j in zip(initial,x)),24)
 corner=F(sum(sum(2*mid[e]-1 for e,(_,a) in enumerate(edges) if a==b)**2 for b in range(3)),256)
 planes=[sum(legal(mid,p) for p in range(a*8,(a+1)*8)) for a in range(3)];aniso=F(3*sum(a*a for a in planes)-n*n,192)
 names=['mid_NF','mid_X','mid_X2','endpoint_h','hL_hR','mid_X_endpoint_h','time_average_NF','endpoint_overlap','physical_event_count','hamming_activity_per_time','electric_corner_intensity','plane_anisotropy'];vals=[n,X,X*X,eh,h0*h1,X*eh,integral/T,overlap,len(events),F(len(events),1)/(6*T),corner,aniso]
 measured=r['cases'][cid]['measurements'][-1]
 for name,v in zip(names,vals):need(abs(float(v)-measured[name])<1e-12,'literal measure '+name)
 c=r['cases'][cid];need(len(c['blocks'])==384 and len(c['measurements'])==4,'coverage')
 sy=json.loads((out/f'synthetic{cid}.json').read_text());need(len(sy['rows'])==128 and all(v==c['measurements'][j%4] for j,v in enumerate(sy['rows'])),'syntheticnotnewdata')
 for j,batch in enumerate(sy['batch_means']):
  for k,v in batch.items():need(abs(v-sum(z[k] for z in sy['rows'][8*j:8*j+8])/8)<1e-12,'syntheticbatch')
 need(sy['face_histogram']==[sum(z['face']==p for z in c['blocks']) for p in range(24)],'facehist')
 rows.append({'cid':cid,'events':len(events),'witness_length':len(data['witness']),'values':dict(zip(names,map(float,vals)))})
# Independently reconstruct cost formula; no author analyzer imports.
load=r['runtime_load_seconds'];accounted=load+sum(c['initialization_seconds']+c['io_seconds']+c['synthetic_output_seconds']+sum(c['interval_seconds']) for c in r['cases']);upper=.58+.01+1.;overhead=upper-accounted;arms=[]
for c in r['cases']:
 same=[z for z in r['cases'] if z['T']==c['T']];sweep=max((z['interval_seconds'][j]-z['measurement_seconds'][j])/4 for z in same for j in range(4));measurement=max(t for z in same for t in z['measurement_seconds'])
 for burn in [16,64]:
  chain=c['initialization_seconds']+c['io_seconds']+c['synthetic_output_seconds']+(burn+128)*sweep+128*measurement+overhead;arms.append(4*chain+load)
f=json.loads((out/'FORECAST.json').read_text());need(abs(sum(4*a for a in arms)-f['aggregate'])<1e-10,'forecast aggregate');need(abs(max(arms)-f['max_shard'])<1e-12,'forecast max');need(abs(overhead-f['unallocated_outer_seconds_charged_each_chain'])<1e-12,'overhead')
for a,z in zip(arms,f['arms']):need(abs(a-z['four_chain_shard'])<1e-12 and z['measurement_count']==128,'allarmscadence')
Path(__file__).with_name('RESULT.json').write_text(json.dumps({'checks':N,'final_replays':rows,'forecast_aggregate':sum(4*a for a in arms),'forecast_max':max(arms),'accounted':accounted,'overhead_each_chain':overhead,'source_freeze':sha(src/'FINAL_FREEZE.json'),'earlier12vectors':'source-read only, no saved complete states','no_author_imports':True},indent=2)+'\n')
