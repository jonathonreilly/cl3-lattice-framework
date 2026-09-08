import json,math,sys
from pathlib import Path
from fractions import Fraction
import config
from runtime import NAMES,Runtime
from preflight import verify,sha

def mean(rows):return [sum(r[j] for r in rows)/len(rows) for j in range(len(rows[0]))]
def covariance(rows):
 m=mean(rows);n=len(rows)
 return [[sum((r[i]-m[i])*(r[j]-m[j]) for r in rows)/(n-1) for j in range(len(m))] for i in range(len(m))]
def derived(m):
 nf,x,x2,e,hh,xh=m[:6]
 if x<=0:return None
 D=(.95*nf-e)/(2*x);C=xh/x-e
 return [D,C,D+C,hh-e*e,x2-x*x]
def gradients(m):
 nf,x,x2,e,hh,xh=m[:6];d=(.95*nf-e)/(2*x)
 a=[0.]*12;a[0]=.95/(2*x);a[1]=-d/x;a[3]=-1/(2*x)
 b=[0.]*12;b[1]=-xh/x**2;b[3]=-1;b[5]=1/x
 c=[u+v for u,v in zip(a,b)];h=[0.]*12;h[3]=-2*e;h[4]=1
 v=[0.]*12;v[1]=-2*x;v[2]=1
 return [a,b,c,h,v]
def raw_stats(vectors):
 m=mean(vectors);cov=covariance(vectors);n=len(vectors)
 return dict(mean=m,chain_covariance=cov,se=[math.sqrt(max(0,cov[j][j]/n)) for j in range(len(m))])

def stats(vectors):
 m=mean(vectors);cov=covariance(vectors);n=len(vectors);se=[math.sqrt(max(0,cov[j][j]/n)) for j in range(12)];d=derived(m)
 result=dict(mean=m,chain_covariance=cov,mean_covariance=[[x/n for x in row] for row in cov],se=se,denominator_positive=m[1]>0)
 if d is not None:
  g=gradients(m);iv=[[sum(gj[k]*(row[k]-m[k]) for k in range(12)) for gj in g] for row in vectors];ic=covariance(iv);dc=[[x/n for x in row] for row in ic]
  joint=[[row[k]-m[k] for k in range(12)]+v for row,v in zip(vectors,iv)];jc=covariance(joint)
  result.update(joint_raw_derived_mean_covariance=[[x/n for x in row] for row in jc],derived=d,derived_names=['D','correction','R','VarH','VarX'],derived_se=[math.sqrt(max(0,dc[j][j])) for j in range(5)],derived_covariance=dc,chain_influences=iv)
 return result

def validate(z,a,c):
 if z['chain']!=c or z['seed']!=config.seed(a['arm'],c) or z['arm']!=a or z['raw_names']!=list(NAMES):raise ValueError('identity/T/names')
 rows=z['rows']
 if len(rows)!=128 or any(len(r)!=12 or any(type(x) not in (int,float) or not math.isfinite(x) for x in r) for r in rows):raise ValueError('raw cadence/shape/finite')
 if len(z['batch_means'])!=16:raise ValueError('batches')
 expected=[mean(rows[i:i+8]) for i in range(0,128,8)]
 if z['batch_means']!=expected:raise ValueError('batch reconstruction')
 count=24*(a['burn']+128)
 if len(z['face_histogram'])!=24 or any(type(x) is not int or x<0 for x in z['face_histogram']) or sum(z['face_histogram'])!=count or z['completed_blocks']!=count:raise ValueError('blocks')
 for name,total in [('burn_face_histogram',24*a['burn']),('measured_face_histogram',24*128)]:
  h=z[name]
  if len(h)!=24 or any(type(x) is not int or x<0 for x in h) or sum(h)!=total:raise ValueError('split face counts')
 if any(b+m!=h for b,m,h in zip(z['burn_face_histogram'],z['measured_face_histogram'],z['face_histogram'])):raise ValueError('histogram decomposition')
 # Coverage is a scientific failure retained in the report, not discarded data.
 for key in ('selected_events_sum','tape_used_sum','max_path_events','bit_calls'):
  if type(z[key]) is not int or z[key]<0:raise ValueError('counter')
 if not 0<=z['selected_events_sum']<=4096*count or not count<=z['tape_used_sum']<=4096*count:raise ValueError('budget counters')
 if z['numerical_failures']!=0 or not math.isfinite(z['bracket_width_sum']) or z['bracket_width_sum']<0:raise ValueError('numerical failure')
 for nf,x,x2,e,hh,xh,tnf,over,events,activity,corner,plane in rows:
  if not(0<=nf<=24 and 0<=x<=12 and x2==x*x and -1.2<=e<=0 and 0<=hh<=1.44 and 0<=tnf<=24 and -1<=over<=1 and type(events) is int and events>=0 and activity==events/(6*a['T']) and 0<=corner<=.75 and 0<=plane<=2/3):raise ValueError('physical raw bounds')
 return rows

def targets():
 base=Runtime().oracle;sup=json.loads((Path(__file__).parent/'SUPPLEMENT.json').read_text());ans={}
 for r,s in zip(base['targets'],sup['derived_targets']):
  if r['T_total']!=s['T_total']:raise ValueError('oracle times')
  m=[];err=[]
  for name in NAMES:
   if name in r['moments']:m.append(r['moments'][name]['float']);err.append(r['absolute_CT_truncation_error_upper'][name]['float'])
   else:m.append(float(Fraction(s['half_polynomial_order_reference'][name])));err.append(float(Fraction(s['order_CT_error_upper'][name])))
  ans[float(Fraction(r['T_total']))]=dict(raw=m,error=err,D=s['D'],R=s['R'],D_interval=s['D_interval'],R_interval=s['R_interval'])
 return ans

def assess(st,t):
 raw=[abs(a-b)<=4*s+e+1e-12 for a,b,s,e in zip(st['mean'],t['raw'],st['se'],t['error'])]
 precision={NAMES[j]:st['mean'][j]>0 and 4*st['se'][j]<=.15*st['mean'][j] for j in (0,1,6,9)}
 precision.update({NAMES[j]:4*st['se'][j]<=.05 for j in (7,10,11)})
 dgate={}
 if st['denominator_positive']:
  for name,j in [('D',0),('R',2)]:
   lo,hi=t[name+'_interval'];v=st['derived'][j];se=st['derived_se'][j];dgate[name]=lo-4*se-1e-12<=v<=hi+4*se+1e-12
 else:dgate={'D':False,'R':False}
 return dict(raw_4SE_consistency=raw,derived_4SE_consistency=dgate,precision=precision,pass_all=all(raw) and all(dgate.values()) and all(precision.values()))

def acceptance(arms,contrasts):
 long=(1,3,5,7)
 # Every measured chain must cover all24 faces, including short arms.
 coverage=all(all(a['measured_face_coverage']) for a in arms)
 starts=[c for c in contrasts if c['arms'] in ([1,3],[5,7])]
 if len(starts)!=2:return False
 return coverage and all(arms[i]['gates']['pass_all'] and not any(arms[i]['half_flags']) for i in long) and all(not any(c['flags']) and 'derived_flags' in c and not any(c['derived_flags']) for c in starts)

def main():
 freeze=verify();base=Path(sys.argv[1]);r=Runtime();T=targets();arms=[]
 if (base/'FAILED.json').exists() or len([p for p in base.glob('a*_s*') if p.is_dir()])!=32:raise ValueError('failed or missing study')
 for a in config.ARMS:
  chains=[];coverage=[]
  for s in range(4):
   folder=base/f'a{a["arm"]}_s{s}';z=json.loads((folder/'RESULT.json').read_text())
   receipt=json.loads((folder/'OUTER.json').read_text())
   if z['freeze']!=freeze or z['arm']!=a['arm'] or z['shard']!=s or receipt['returncode']!=0 or receipt['result_sha']!=sha(folder/'RESULT.json'):raise ValueError('shard identity/receipt')
   if not math.isfinite(receipt['seconds']) or not 0<receipt['seconds']<=180 or not math.isfinite(z['rss_mib']) or not 0<z['rss_mib']<=384:raise ValueError('resource')
   if len(z['chains'])!=4:raise ValueError('chain coverage')
   for c,entry in zip(range(4*s,4*s+4),z['chains']):
    rows=validate(entry,a,c);coverage.append(all(x>0 for x in entry['measured_face_histogram']));file=folder/entry['final_path']
    if file.name!=f'chain{c}.path.json' or sha(file)!=entry['final_path_sha']:raise ValueError('final path binding')
    p=r.load(file)
    init=entry['initialization'];initial=int(init['state_hex'],16)
    import hashlib
    if initial not in r.index or hashlib.sha256(initial.to_bytes(3,'little')).hexdigest()!=init['state_sha']:raise ValueError('initial state binding')
    if type(init['auxiliary_count']) is not int or type(init['physical_events']) is not int or not 0<=init['physical_events']<=entry['max_path_events'] or not 0<=init['physical_events']<=init['auxiliary_count']<=r.target(a['T'])['K']:raise ValueError('initial count')
    if a['start']=='constant' and (initial!=r.g.seed or init['auxiliary_count']!=0):raise ValueError('constant initializer')
    if p.T!=a['T'] or [r.measure(p)[n] for n in NAMES]!=rows[-1]:raise ValueError('final readout')
    chains.append(rows)
  vectors=[mean(x) for x in chains];st=stats(vectors);half=[ [v-u for u,v in zip(mean(x[:64]),mean(x[64:]))] for x in chains]
  hs=raw_stats(half)
  st.update(measured_face_coverage=coverage,arm=a,chain_vectors=vectors,gates=assess(st,T[a['T']]),half_raw_difference=hs['mean'],half_raw_se=hs['se'],half_flags=[abs(x)>4*y for x,y in zip(hs['mean'],hs['se'])],raw_nonpositive_S=sum(row[1]<=0 for ch in chains for row in ch))
  if st['denominator_positive']:st['resolution']={name:dict(estimate=st['derived'][j],se=st['derived_se'][j],resolved=abs(st['derived'][j])>4*st['derived_se'][j]) for name,j in [('correction',1),('VarH',3),('VarX',4)]}
  arms.append(st)
 contrasts=[]
 for i,j in [(1,3),(5,7),(0,1),(2,3),(4,5),(6,7)]:
  a,b=arms[i],arms[j];delta=[y-x for x,y in zip(a['mean'],b['mean'])];se=[math.hypot(x,y) for x,y in zip(a['se'],b['se'])]
  record=dict(arms=[i,j],raw_delta=delta,raw_se=se,flags=[abs(x)>4*y for x,y in zip(delta,se)])
  if a['denominator_positive'] and b['denominator_positive']:
   dd=[y-x for x,y in zip(a['derived'],b['derived'])];ds=[math.hypot(x,y) for x,y in zip(a['derived_se'],b['derived_se'])];record.update(derived_delta=dd,derived_se=ds,derived_flags=[abs(x)>4*y for x,y in zip(dd,ds)])
  contrasts.append(record)
 print(json.dumps(dict(freeze=freeze,arms=arms,contrasts=contrasts,scientific_accept=acceptance(arms,contrasts),all_eight_arm_descriptive_gates=all(a['gates']['pass_all'] for a in arms),scope='nominal independent-chain uncertainty; no machine-TV, ground or mixing certificate'),allow_nan=False,indent=2))
if __name__=='__main__':main()
