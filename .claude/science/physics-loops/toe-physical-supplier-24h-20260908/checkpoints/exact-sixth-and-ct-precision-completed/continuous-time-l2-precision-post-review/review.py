"""Independent fixed-study postreview; no author imports or trajectory generation."""
from pathlib import Path
from itertools import product,combinations
import json,hashlib,math,sys,signal,resource,time
from fractions import Fraction
BASE=Path(__file__).parent
SOURCE=Path('/private/tmp/toe-24h-probes-20260908/continuous-time-l2-precision-followup')
FREEZE='22ab56cb8ac792a01e857b66d69b21b25e083f626f7664a6a0c4b351ed670741'
NAMES=['mid_NF','mid_X','mid_X2','endpoint_h','hL_hR','mid_X_endpoint_h','time_average_NF','endpoint_overlap','physical_event_count','hamming_activity_per_time','electric_corner_intensity','plane_anisotropy']
checks=0
def need(c,m):
 global checks
 checks+=1
 if not c:raise RuntimeError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def close(a,b):return abs(a-b)<=2e-10*max(1,abs(a),abs(b))
def mean(rows):return [sum(row[j] for row in rows)/len(rows) for j in range(len(rows[0]))]
def covmean(rows):
 m=mean(rows);n=len(rows)
 return [[sum((r[i]-m[i])*(r[j]-m[j]) for r in rows)/(n*(n-1)) for j in range(len(m))] for i in range(len(m))]
def derived(m):
 n,x,x2,e,hh,xh=m[:6]
 if x<=0:return None
 d=(.95*n-e)/(2*x);c=xh/x-e
 return [d,c,d+c,hh-e*e,x2-x*x]
def summarize(rows):
 m=mean(rows);C=covmean(rows);se=[math.sqrt(max(0,C[j][j])) for j in range(len(m))];d=derived(m)
 out=dict(mean=m,se=se,covariance=C,derived=d)
 if d is not None:
  n,x,x2,e,hh,xh=m[:6];g=[[0.]*12 for _ in range(5)];g[0][0]=.95/(2*x);g[0][1]=-d[0]/x;g[0][3]=-1/(2*x);g[1][1]=-xh/x**2;g[1][3]=-1;g[1][5]=1/x;g[2]=[u+v for u,v in zip(g[0],g[1])];g[3][3]=-2*e;g[3][4]=1;g[4][1]=-2*x;g[4][2]=1
  joint=[]
  for row in rows:
   z=[v-u for u,v in zip(m,row)];joint.append(z+[sum(v*w for v,w in zip(z,gg)) for gg in g])
  J=covmean(joint);out.update(joint=J,derived_se=[math.sqrt(max(0,J[12+j][12+j])) for j in range(5)])
 return out
vs=list(product(range(2),repeat=3));edges=[(v,a) for v in vs for a in range(3)];ei={v:i for i,v in enumerate(edges)}
def step(v,a):z=list(v);z[a]=1-z[a];return tuple(z)
faces=[(ei[v,a],ei[step(v,a),b],ei[step(v,b),a],ei[v,b]) for a,b in combinations(range(3),2) for v in vs]
seed=tuple(v[a] for v,a in edges)
def legal(x,p):return all(x[faces[p][k]]!=x[faces[p][(k+1)%4]] for k in range(4))
def nf(x):return sum(legal(x,p) for p in range(24))
def flip(x,p):
 need(type(p) is int and 0<=p<24 and legal(x,p),'literal flip gate');y=list(x)
 for e in faces[p]:y[e]=1-y[e]
 for v in vs:need(sum(y[e] for e,(r,a) in enumerate(edges) if r==v or step(r,a)==v)==3,'literal degree')
 return tuple(y)
def path_values(file):
 z=json.loads(file.read_text());packed=int(z['initial'],16);need(0<=packed<2**24,'packed state');initial=tuple((packed>>e)&1 for e in range(24));x=seed
 for p in z['witness']:x=flip(x,p)
 need(x==initial,'initial witness');T=float.fromhex(z['T']);need(math.isfinite(T) and T>0,'T');mid=x;integral=0.;last=0.;events=z['events']
 for raw,p in events:
  t=float.fromhex(raw);need(math.isfinite(t) and last<t<T,'event times');integral+=(t-last)*nf(x);x=flip(x,p)
  if t<=T/2:mid=x
  last=t
 integral+=(T-last)*nf(x);n=nf(mid);h0=-nf(initial)/20;h1=-nf(x)/20;e=(h0+h1)/2
 X=sum(sum((-1)**(sum(v)+v[a])*(2*mid[k]-1) for k,(v,c) in enumerate(edges) if c==b)**2 for a in range(3) for b in range(3) if a!=b)/32
 over=sum((2*i-1)*(2*j-1) for i,j in zip(initial,x))/24
 corner=sum(sum(2*mid[k]-1 for k,(_,a) in enumerate(edges) if a==b)**2 for b in range(3))/256
 planes=[sum(legal(mid,p) for p in range(8*a,8*a+8)) for a in range(3)]
 return T,[n,X,X*X,e,h0*h1,X*e,integral/T,over,len(events),len(events)/(6*T),corner,(3*sum(v*v for v in planes)-n*n)/192]
def target_table():
 oracle=json.loads((SOURCE.parent/'continuous-time-l2-calibration-design/ORACLE.json').read_text());supp=json.loads((SOURCE/'SUPPLEMENT.json').read_text());out={}
 for r,s in zip(oracle['targets'],supp['derived_targets']):
  need(r['T_total']==s['T_total'],'oracle alignment');m=[];errors=[]
  for name in NAMES:
   if name in r['moments']:m.append(r['moments'][name]['float']);errors.append(r['absolute_CT_truncation_error_upper'][name]['float'])
   else:m.append(float(Fraction(s['half_polynomial_order_reference'][name])));errors.append(float(Fraction(s['order_CT_error_upper'][name])))
  out[float(Fraction(r['T_total']))]=(m,errors,s)
 return out
def main(folder):
 start=time.monotonic();need(sha(SOURCE/'FINAL_FREEZE.json')==FREEZE,'source freeze')
 f=json.loads((SOURCE/'FINAL_FREEZE.json').read_text())
 for name,h in f['files'].items():need(sha(SOURCE/name)==h,'frozen '+name)
 for name,h in json.loads((SOURCE/'RUNTIME.json').read_text())['files'].items():need(sha(Path(name))==h,'runtime '+name)
 need(not (folder/'FAILED.json').exists(),'fixed study failed; no selective replay');need((folder/'COMPLETE.json').exists(),'incomplete fixed study');reported=json.loads((folder/'ANALYSIS.json').read_text());targets=target_table();arms=[];raw_hashes={}
 complete=json.loads((folder/'COMPLETE.json').read_text());ledger=json.loads((folder/'LEDGER.json').read_text());started=json.loads((folder/'STARTED.json').read_text());ar=json.loads((folder/'ANALYSIS.OUTER.json').read_text())
 need(complete['freeze']==FREEZE and complete['jobs']==64 and complete['analysis_sha']==sha(folder/'ANALYSIS.json'),'complete binding')
 need(180.930914<=complete['charged_seconds']<3600 and started['prior_cost_seconds']==180.930914 and started['jobs']==64 and started['chains']==256,'aggregate/prior')
 need(len(ledger['jobs'])==64 and len(list(folder.glob('a*_s*/RESULT.json')))==64 and len(reported['arms'])==4 and len(reported['contrasts'])==2,'full study shape')
 need(ar['returncode']==0 and 0<ar['seconds']<=180 and 0<ar['outer_rss_bytes']<=384*1048576 and ar['stdout_sha']==sha(folder/'ANALYSIS.stdout') and (folder/'ANALYSIS.stdout').read_bytes()==(folder/'ANALYSIS.json').read_bytes(),'analysis receipt')
 oracle_dir=SOURCE.parent/'continuous-time-l2-calibration-design';allowed_states=set(json.loads((oracle_dir/'BACKWARD_POWERS.json').read_text())['states']);oracle=json.loads((oracle_dir/'ORACLE.json').read_text());caps={float(Fraction(z['T_total'])):z['K'] for z in oracle['targets']}
 for arm,(T,kind,burn) in enumerate((t,s,b) for t in [.5,2.] for s in ['constant','bounded'] for b in [64]):
  chains=[];coverage=[]
  for shard in range(16):
   d=folder/f'a{arm}_s{shard}';z=json.loads((d/'RESULT.json').read_text());rec=json.loads((d/'OUTER.json').read_text());need(z['freeze']==FREEZE and z['arm']==arm and z['shard']==shard,'shard identity');need(rec['returncode']==0 and rec['result_sha']==sha(d/'RESULT.json'),'shard receipt');need(0<rec['seconds']<=180 and 0<rec['outer_rss_bytes']<=384*1048576,'external resources');need(len(z['chains'])==4,'four chains');need(rec==ledger['jobs'][arm*16+shard],'ledger receipt identity')
   for chain,r in zip(range(4*shard,4*shard+4),z['chains']):
    need(r['chain']==chain and r['seed']==202609360000+1000*arm+chain and r['arm']==dict(arm=arm,T=T,start=kind,burn=burn),'chain identity');need(r['raw_names']==NAMES,'names');rows=r['rows'];need(len(rows)==256 and all(len(x)==12 and all(type(v) in (int,float) and math.isfinite(v) for v in x) for x in rows),'raw coverage');need(r['batch_means']==[mean(rows[j:j+16]) for j in range(0,256,16)],'batch means')
    bh,mh,h=r['burn_face_histogram'],r['measured_face_histogram'],r['face_histogram'];need(all(len(x)==24 and all(type(v) is int and v>=0 for v in x) for x in [bh,mh,h]),'hist domain');need(sum(bh)==24*burn and sum(mh)==6144 and h==[x+y for x,y in zip(bh,mh)] and r['completed_blocks']==24*(burn+256),'hist totals');coverage.append(all(v>0 for v in mh))
    need(r['numerical_failures']==0 and 0<=r['selected_events_sum']<=4096*r['completed_blocks'] and r['completed_blocks']<=r['tape_used_sum']<=4096*r['completed_blocks'] and math.isfinite(r['bracket_width_sum']) and r['bracket_width_sum']>=0,'counters')
    for x in rows:
     n,X,X2,e,hh,xh,tnf,over,k,act,corner,plane=x;need(0<=n<=24 and 0<=X<=12 and X2==X*X and -1.2<=e<=0 and 0<=hh<=1.44 and 0<=tnf<=24 and -1<=over<=1 and type(k) is int and k>=0 and act==k/(6*T) and 0<=corner<=.75 and 0<=plane<=2/3,'raw bounds')
    init=r['initialization'];iv=int(init['state_hex'],16);need(iv in allowed_states and hashlib.sha256(iv.to_bytes(3,'little')).hexdigest()==init['state_sha'],'initial state binding');need(type(init['auxiliary_count']) is int and type(init['physical_events']) is int and 0<=init['physical_events']<=init['auxiliary_count']<=caps[T] and init['physical_events']<=r['max_path_events'],'initial counts');need(all(type(r[k]) is int and r[k]>=0 for k in ['max_path_events','bit_calls']),'counter integers')
    if kind=='constant':need(iv==sum(v<<i for i,v in enumerate(seed)) and init['auxiliary_count']==0,'constant initializer')
    file=d/r['final_path'];need(file.name==f'chain{chain}.path.json' and sha(file)==r['final_path_sha'],'pathhash');tt,v=path_values(file);need(tt==T and all(close(a,b) for a,b in zip(v,rows[-1])),'twelve final readouts');raw_hashes[str(file)]=sha(file);chains.append(rows)
  st=summarize([mean(x) for x in chains]);halves=[[v-u for u,v in zip(mean(x[:128]),mean(x[128:]))] for x in chains];hm=mean(halves);hc=covmean(halves);hs=[math.sqrt(max(0,hc[j][j])) for j in range(12)];hf=[abs(v)>4*s for v,s in zip(hm,hs)];target,err,sup=targets[T]
  raw=[abs(x-y)<=4*s+e+1e-12 for x,y,s,e in zip(st['mean'],target,st['se'],err)];precision=all(st['mean'][j]>0 and 4*st['se'][j]<=.15*st['mean'][j] for j in [0,1,6,9]) and all(4*st['se'][j]<=.05 for j in [7,10,11]);dg=[]
  for name,j in [('D',0),('R',2)]:
   lo,hi=sup[name+'_interval'];dg.append(st['derived'] is not None and lo-4*st['derived_se'][j]-1e-12<=st['derived'][j]<=hi+4*st['derived_se'][j]+1e-12)
  st.update(coverage=coverage,half=hm,half_se=hs,half_flags=hf,gate=all(raw) and all(dg) and precision);rep=reported['arms'][arm]
  for key in ['mean','se','derived','derived_se']:
   if st.get(key) is not None:need(all(close(x,y) for x,y in zip(st[key],rep[key])),'arm '+key)
  if 'joint' in st:need(all(close(x,y) for rr,ss in zip(st['joint'],rep['joint_raw_derived_mean_covariance']) for x,y in zip(rr,ss)),'joint covariance')
  need(hf==rep['half_flags'] and coverage==rep['measured_face_coverage'] and st['gate']==rep['gates']['pass_all'],'arm gates');arms.append(st)
 contrasts=[]
 for j,(a,b) in enumerate([(0,1),(2,3)]):
  x,y=arms[a],arms[b];dd=[v-u for u,v in zip(x['mean'],y['mean'])];se=[math.hypot(u,v) for u,v in zip(x['se'],y['se'])];flags=[abs(v)>4*s for v,s in zip(dd,se)];dflags=None
  if x['derived'] is not None and y['derived'] is not None:dflags=[abs(v-u)>4*math.hypot(s,t) for u,v,s,t in zip(x['derived'],y['derived'],x['derived_se'],y['derived_se'])]
  rep=reported['contrasts'][j];need(flags==rep['flags'] and (dflags is None or dflags==rep['derived_flags']),'contrast flags');contrasts.append((flags,dflags))
 accept=all(all(a['coverage']) for a in arms) and all(arms[i]['gate'] and not any(arms[i]['half_flags']) for i in [0,1,2,3]) and all(not any(f) and d is not None and not any(d) for f,d in contrasts[:2]);need(accept==reported['scientific_accept'],'acceptance')
 result=dict(checks=checks,freeze=FREEZE,scientific_accept=accept,final_paths_replayed=256,final_readouts_recomputed=3072,intermediate_raw_vectors='algebra/statistics only; no full intermediate paths saved',raw_path_sha256=raw_hashes,seconds=time.monotonic()-start,rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576)
 need(result['seconds']<180 and 0<result['rss_mib']<384,'review cap');(BASE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':
 signal.alarm(180)
 try:main(Path(sys.argv[1]))
 except BaseException as e:
  (BASE/'REVIEW_FAILURE.json').write_text(json.dumps({'type':type(e).__name__,'message':str(e),'checks':checks},indent=2)+'\n');raise
