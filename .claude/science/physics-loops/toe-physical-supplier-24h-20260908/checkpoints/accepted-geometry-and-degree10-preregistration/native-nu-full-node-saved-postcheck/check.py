"""Saved-only arithmetic reconstruction; no producer imports; saved-node contractions only."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib,json,math,re
S=1<<192
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def rnd(a,b):
 a*=S;b*=S;lo,rem=divmod(a.numerator,a.denominator);hi,rem=divmod(b.numerator,b.denominator);return F(lo,S),F(hi+(rem!=0),S)
def add(a,b):return rnd(a[0]+b[0],a[1]+b[1])
def mul(a,b):
 p=[x*y for x in a for y in b];return rnd(min(p),max(p))
def pair(x):
 if not isinstance(x,list) or len(x)!=2:raise ValueError('interval shape')
 a,b=map(F,x)
 if a>b:raise ValueError('interval order')
 return a,b
def run(binding,out):
 stage='pins';checks=0;done=[];current=None
 def ck(v,msg):
  nonlocal checks
  if not v:raise ValueError(msg)
  checks+=1
 def save():
  (out/'PARTIAL.json').write_text(json.dumps({'stage':stage,'predicates':checks,'panels':done,'current':current})+'\n')
 def read(p):
  ck(p in binding['inputs'] and sha(p)==binding['inputs'][p],'bound input');return json.loads(Path(p).read_text())
 save()
 try:
  ck(binding['status']=='ACCEPTED_RESULT_BOUND','unbound result')
  for p,h in binding['inputs'].items():ck(sha(p)==h,'input hash')
  rf=read(binding['root_freeze']);wf=read(binding['worker_freeze']);root=Path(binding['root_freeze']).parent
  for name,h in rf['files'].items():ck(str(root/name) in binding['inputs'] and sha(root/name)==h,'root source closure')
  ck(sha(binding['worker_freeze'])==rf['worker_freeze'],'worker freeze')
  for p,h in wf['inputs'].items():ck(binding['inputs'].get(p)==h,'full raw/source/runtime closure')
  accept=read(binding['acceptance']);r=read(binding['result']);w=read(binding['worker']);part=read(binding['partial']);receipt=read(binding['root_receipt'])
  ck(accept['status']=='ACCEPTED_CATALOG_NU_INTEGRAL' and accept['result_sha256']==sha(binding['result']),'accepted result status/binding')
  ck(receipt['pass'] is True and receipt['failure'] is None and receipt['returncode']==0 and receipt['worker_freeze']==sha(binding['worker_freeze']),'root completion')
  ck(all(isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x) and x>0 for x in (receipt['seconds'],receipt['sampled_whole_tree_peak'],w['seconds'],w['rss_bytes'])),'finite positive resources')
  ck(w['seconds']<=receipt['seconds']<=30 and receipt['sampled_whole_tree_peak']<=384*1048576 and w['rss_bytes']<=384*1048576,'resource caps')
  ck(w['status']=='COMPLETE_CATALOG_INTEGRAL' and w['runtime_sha256']==sha(binding['worker_freeze']) and w['result_sha256']==sha(binding['result']),'worker result')
  ck(accept['worker_freeze']==sha(binding['worker_freeze']) and accept['root_freeze']==sha(binding['root_freeze']),'acceptance source')
  shellpath=binding['external_stderr'];ck(shellpath in binding['inputs'] and sha(shellpath)==binding['inputs'][shellpath],'external receipt hash');shell=Path(shellpath).read_text()
  real=re.findall(r'^real\s+([0-9]+(?:\.[0-9]+)?)$',shell,re.M);rss=re.findall(r'^\s*([0-9]+)\s+maximum resident set size$',shell,re.M)
  ck(len(real)==len(rss)==1 and 0<F(real[0])<=30 and 0<int(rss[0])<=384*1048576,'external resources')
  ck(F(real[0])==F(str(accept['external_seconds'])) and int(rss[0])==accept['external_max_rss'] and accept['sampled_whole_tree_peak']==receipt['sampled_whole_tree_peak'],'external acceptance matching')
  ck(part['stage']=='complete' and part['current']==2 and part['panels']==[f'PANELS/{j:02d}.json' for j in range(67)],'final partial semantics')
  ck(isinstance(part['seconds'],(int,float)) and math.isfinite(part['seconds']) and 0<part['seconds']<=w['seconds'],'partial time')
  ck(r['panels']==67 and r['nodes']==1742 and r['oracle_calls']==0,'scope')
  base=Path(binding['result']).parent;stage='panels';total=(F(0),F(0))
  ck({x.name for x in (base/'PANELS').iterdir()}=={f'{j:02d}.json' for j in range(67)},'panel membership')
  # New independent data reader: accepted raw endpoint JSON only; never calls loader.
  pb=read(binding['producer_binding']);geom=read(pb['catalog_geometry_path']);cat=read(str(Path(pb['catalog']['directory'])/'RESULT.json'))
  ck(len(geom['nodes'])==1742 and len(geom['endpoints'])==3484 and len(cat['rows'])==3484,'catalog census')
  endpoints=[]
  for i,(e,row) in enumerate(zip(geom['endpoints'],cat['rows'])):
   current={'endpoint':i};save();ck(type(row['id'])is int and row['id']==i and row['gate']=='PASS' and row['path']==f'ORACLES/{i:04d}.json','raw row')
   path=str(Path(pb['catalog']['directory'])/row['path']);raw=read(path);ck(sha(path)==row['sha256'] and raw['catalog_endpoint']==e and raw['s']==e['s'],'raw identity');ck(len(raw['widths'])==2 and max(map(F,raw['widths']))<=F(1,10**30),'raw widths');endpoints.append(pair(raw['A']))
  count=0;weight_sum=F(0)
  for j in range(67):
   current={'panel':j};save();nodes=[n for n in geom['nodes']if n['panel']==j-64];ck(len(nodes)==26,'26 nodes');value=(F(0),F(0))
   for node in nodes:
    current={'panel':j,'node':node['id']};save();l,u=node['endpoint_ids'];ck(type(l)is int and type(u)is int and 0<=l<u<3484,'endpoint IDs');tl,tu=map(F,node['t_interval']);wl,wu=map(F,node['weight']);A=(endpoints[u][0],endpoints[l][1])
    ck(type(node['id'])is int and node['id']==count and 0<tl<tu<=8 and tu-tl<=F(1,2**140) and 0<wl<=wu and wu-wl<=F(1,10**38) and A[0]<=A[1],'node enclosures')
    weight=rnd(wl,wu);weight_sum+=weight[1];t2=mul((tl,tu),(tl,tu));t4=mul(t2,t2);q=add(add((F(6),F(6)),(-t2[1],-t2[0])),mul(t4,A));contribution=mul(weight,q);value=add(value,contribution);count+=1
   (out/f'PANEL_{j:02d}.json').write_text(json.dumps({'panel':j-64,'independent_value':list(map(str,value))})+'\n')
   d=read(str(base/f'PANELS/{j:02d}.json'));ck(d['panel']==j-64 and pair(d['value'])==value,'all node contractions');total=add(total,value);ck(total==pair(d['cumulative']),'cumulative');done.append(j);save()
  ck(count==1742 and weight_sum<=9,'all nodes/weights')
  ck(total==pair(r['middle'])==pair(part['sum']),'middle')
  middle_ok=total[1]-total[0]<=F(2,10**25)
  ck(type(r['middle_width_gate']) is bool and r['middle_width_gate']==middle_ok,'middle width gate')
  ck(r['observable']=='nu=E_X_power_3_over_2','nu normalization')
  stage='independent_moments';save()
  # Exponential-generating convolution of independent coordinate moments.
  # This differs from the producer's triple multinomial loop.
  one=[F(comb(2*n,n)) for n in range(42)];mom=[F(1)]+[F(0)]*41
  for axis in range(3):mom=[sum((F(comb(n,k))*mom[k]*one[n-k] for k in range(n+1)),F(0)) for n in range(42)]
  tail=sum(((-1)**n*mom[n+2]/F((2*n+1)*8**(2*n+1)) for n in range(40)),F(0))
  rem=F(12**42,81*8**81);eps=F(1,2**64);low=6*eps-eps**3/3;lowhi=low+F(17,60)*eps**5/5;rad=F(256,4**52)
  tt=read(str(base/'TAIL.json'));ck(set(tt['moments'])=={str(k)for k in range(2,42)} and all(F(tt['moments'][str(k)])==mom[k]for k in range(2,42)),'all40 moments')
  for key,val in [('high_partial',tail),('high_remainder',rem),('quadrature_radius',rad)]:ck(F(r[key])==F(tt[key])==val,key)
  ck(pair(r['low_interval'])==pair(tt['low_interval'])==(low,lowhi) and type(r['tail_terms'])is int and r['tail_terms']==40,'low/tail count')
  def atan(q,n):
   a=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0));e=F(1,(2*n+1)*q**(2*n+1));return(a,a+e) if n%2==0 else(a-e,a)
  a=atan(5,32);b=atan(239,10);pl,pu=16*a[0]-4*b[1],16*a[1]-4*b[0]
  ans=mul(add(add(total,(tail,tail+rem)),(low-rad,lowhi+rad)),(2/pu,2/pl));ck(ans==pair(r['interval']),'full final interval');width=ans[1]-ans[0];ck(width==F(r['width']) and F(r['target'])==F(2,10**19),'target arithmetic');ck(r['status']==('CERTIFIED_TARGET' if middle_ok and width<=F(2,10**19) else 'INDETERMINATE'),'classification')
  stage='final_pins';save()
  for path,digest in binding['inputs'].items():ck(sha(path)==digest,'final immutable input')
  stage='complete';save();(out/'RESULT.json').write_text(json.dumps({'status':'PASS_SAVED_RECONSTRUCTION','predicates':checks,'interval':list(map(str,ans)),'scientific_status':r['status'],'panels':67,'tail_terms':40,'saved_nodes_reconstructed':1742,'new_oracle_calls':0,'oracle_calls':0,'moments':'independent binomial convolution','source_result_sha256':sha(binding['result']),'observable':'nu=E_X_power_3_over_2','middle_width_gate':middle_ok},indent=2)+'\n')
 except BaseException as e:
  save();(out/'FAILURE.json').write_text(json.dumps({'stage':stage,'predicates':checks,'error':repr(e),'panels':done,'current':current})+'\n');raise
