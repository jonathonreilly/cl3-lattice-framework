"""Saved-only arithmetic reconstruction; no producer imports or node integration."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib,json,math
S=1<<192
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def rnd(a,b):return F((a*S).__floor__(),S),F((b*S).__ceil__(),S)
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
  ck(accept['status']=='ACCEPTED_CATALOG_CMINUS_INTEGRAL' and accept['result_sha256']==sha(binding['result']),'accepted result status/binding')
  ck(receipt['pass'] is True and receipt['failure'] is None and receipt['returncode']==0 and receipt['worker_freeze']==sha(binding['worker_freeze']),'root completion')
  ck(all(isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x) and x>0 for x in (receipt['seconds'],receipt['sampled_whole_tree_peak'],w['seconds'],w['rss_bytes'])),'finite positive resources')
  ck(w['seconds']<=receipt['seconds']<=30 and receipt['sampled_whole_tree_peak']<=384*1048576 and w['rss_bytes']<=384*1048576,'resource caps')
  ck(w['status']=='COMPLETE_CATALOG_INTEGRAL' and w['runtime_sha256']==sha(binding['worker_freeze']) and w['result_sha256']==sha(binding['result']),'worker result')
  ck(r['panels']==67 and r['nodes']==1742 and r['oracle_calls']==0,'scope')
  base=Path(binding['result']).parent;stage='panels';total=(F(0),F(0))
  ck({x.name for x in (base/'PANELS').iterdir()}=={f'{j:02d}.json' for j in range(67)},'panel membership')
  for j in range(67):
   current=j;save()
   d=read(str(base/f'PANELS/{j:02d}.json'));ck(d['panel']==j-64,'panel order');total=add(total,pair(d['value']));ck(total==pair(d['cumulative']),'cumulative');done.append(j);save()
  ck(total==pair(r['middle'])==pair(part['sum']),'middle')
  stage='independent_moments';save()
  # Exponential-generating convolution of independent coordinate moments.
  # This differs from the producer's triple multinomial loop.
  one=[F(comb(2*n,n)) for n in range(26)];mom=[F(1)]+[F(0)]*25
  for axis in range(3):mom=[sum((F(comb(n,k))*mom[k]*one[n-k] for k in range(n+1)),F(0)) for n in range(26)]
  tail=sum(((-1)**n*mom[n]/F((2*n+1)*8**(2*n+1)) for n in range(26)),F(0))
  rem=F(12**26,53*8**53);low=F(1,3*2**64);rad=F(400,27)*F(4,25)**26
  for key,val in [('high_partial',tail),('high_remainder',rem),('low_bound',low),('quadrature_radius',rad)]:ck(F(r[key])==val,key)
  def atan(q,n):
   a=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0));e=F(1,(2*n+1)*q**(2*n+1));return(a,a+e) if n%2==0 else(a-e,a)
  a=atan(5,32);b=atan(239,10);pl,pu=16*a[0]-4*b[1],16*a[1]-4*b[0]
  ans=mul(add(add(total,(tail,tail+rem)),(-rad,rad+low)),(2/pu,2/pl));ck(ans==pair(r['interval']),'full final interval');width=ans[1]-ans[0];ck(width==F(r['width']) and F(r['target'])==F(2,10**19),'target arithmetic');ck(r['status']==('CERTIFIED_TARGET' if width<=F(2,10**19) else 'INDETERMINATE'),'classification')
  stage='complete';save();(out/'RESULT.json').write_text(json.dumps({'status':'PASS_SAVED_RECONSTRUCTION','predicates':checks,'interval':list(map(str,ans)),'scientific_status':r['status'],'node_integrals_replayed':False,'oracle_calls':0,'moments':'independent binomial convolution','source_result_sha256':sha(binding['result'])},indent=2)+'\n')
 except BaseException as e:
  save();(out/'FAILURE.json').write_text(json.dumps({'stage':stage,'predicates':checks,'error':repr(e),'panels':done,'current':current})+'\n');raise
