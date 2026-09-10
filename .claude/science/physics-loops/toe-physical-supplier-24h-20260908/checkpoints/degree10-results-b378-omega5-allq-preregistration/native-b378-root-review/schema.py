from pathlib import Path
from fractions import Fraction as F
from math import comb,isfinite
import json,hashlib,re
S=1<<192

def req(v,s):
 if not v:raise ValueError(s)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def rat(x):
 req(type(x)is str and len(x)<=40000 and re.fullmatch(r'-?\d+(?:/\d+)?',x)is not None,'rational syntax');q=F(x);req(str(q)==x and max(abs(q.numerator).bit_length(),q.denominator.bit_length())<=65536,'canonical rational');return q
def box(x):
 req(type(x)is list and len(x)==2,'box shape');a,b=map(rat,x);req(a<=b,'box order');return(a,b)
def rnd(a):return(F(a[0].numerator*S//a[0].denominator,S),F(-((-a[1].numerator*S)//a[1].denominator),S))
def add(a,b):return rnd((a[0]+b[0],a[1]+b[1]))
def mul(a,b):
 v=[x*y for x in a for y in b];return rnd((min(v),max(v)))
def scale(a,q):return mul(a,(q,q))
def sub(a,b):return add(a,(-b[1],-b[0]))
def pi():
 def at(q,n):
  a=sum((F((-1)**k,(2*k+1)*q**(2*k+1))for k in range(n)),F(0));z=a+F((-1)**n,(2*n+1)*q**(2*n+1));return min(a,z),max(a,z)
 a,b=at(5,40),at(239,12);return 16*a[0]-4*b[1],16*a[1]-4*b[0]
def moments(n=40):
 # Independent binomial convolution of three one-axis moment sequences.
 axis=[comb(2*k,k)for k in range(n+1)];v=[1]+[0]*n
 for _ in range(3):v=[sum(comb(k,j)*v[j]*axis[k-j]for j in range(k+1))for k in range(n+1)]
 return v
def integer(x,n=None):req(type(x)is int and (n is None or x==n),'literal integer')
def stream(p):
 with Path(p).open()as f:
  for line in f:yield json.loads(line)
def check(O,rf,elapsed,progress):
 O=Path(O);names={'B_%03d.json'%i for i in range(378)}|{'RESULT.json','WORKER_COMPLETE.json','PARTIAL.json','PANELS.jsonl','MAPPED_INPUTS.jsonl'};req(set(x.name for x in O.iterdir())==names,'output membership')
 r=json.loads((O/'RESULT.json').read_text());done=json.loads((O/'WORKER_COMPLETE.json').read_text());part=json.loads((O/'PARTIAL.json').read_text());req(r['status']=='COMPLETE_NEW_B378_ONLY'and r['witness_computed']is False,'result scope');req(type(r['rows'])is list and len(r['rows'])==378,'result rows')
 req(done['status']=='COMPLETE'and done['freeze_sha256']==rf['worker_freeze']and done['result_sha256']==sha(O/'RESULT.json'),'completion pins');integer(done['rss_bytes']);req(0<done['rss_bytes']<=384*1048576,'RSS')
 for x in (r['seconds'],done['seconds']):req(type(x)in(int,float)and isfinite(x)and 0<x<299,'time')
 req(r['seconds']<=done['seconds']<=elapsed<299.5,'time order');integer(part['completed'],378);integer(part['current']['pole'],378);req(part=={'current':{'stage':'complete','pole':378,'data':{}},'completed':378},'final partial')
 P=Path(rf['worker_path']);binding=json.loads((P/'BINDING.json').read_text())
 def read(role):
  item=binding['files'][role];req(sha(item['path'])==item['sha256'],'source '+role);return json.loads(Path(item['path']).read_text())
 nodes=read('new_nodes')['rows'];geom=read('catalog_geometry')['nodes'];catalog=read('catalog_result')['rows'];ledger=read('geometry_result')['rows'];req(len(nodes)==378 and len(geom)==1742 and len(catalog)==3484 and len(ledger)==378,'source census')
 maps=iter(stream(O/'MAPPED_INPUTS.jsonl'));mapped_A=[];mapcount=0
 for i,node in enumerate(geom):
  progress({'stage':'schema_catalog_map','id':i});integer(node['id'],i);req(node['endpoint_ids']==[2*i,2*i+1],'endpoint ids');ends=[];hashes=[]
  for side,eid in enumerate(node['endpoint_ids']):
   integer(eid);rec=catalog[eid];integer(rec['id'],eid);req(rec['path']=='ORACLES/%04d.json'%eid and rec['gate']=='PASS','endpoint record');p=Path(binding['catalog_directory'])/rec['path'];req(sha(p)==rec['sha256'],'endpoint pin');raw=json.loads(p.read_text());req(rat(raw['s'])==rat(node['t_interval'][side]),'endpoint argument');ends.append(box(raw['A']));hashes.append(rec['sha256'])
  original={'t':box(node['t_interval']),'weight':box(node['weight']),'A':(ends[1][0],ends[0][1])};req(all(0<a<=b for a,b in original.values()),'positive original')
  e=next(maps);integer(e['pole'],0);d=e['data'];integer(d['id'],i);req(e['stage']=='mapped_catalog'and d['endpoint_ids']==node['endpoint_ids']and d['endpoint_hashes']==hashes and d['geometry_sha256']==binding['files']['catalog_geometry']['sha256'],'map provenance');req(set(d['mapped'])==set(original),'map keys')
  for k,v in original.items():req(box(d['mapped'][k])==rnd(v),'exact outward mapping')
  mapcount+=1
 for i,node in enumerate(nodes):
  integer(node['id'],i);p=Path(binding['new_directory'])/('RAW_%03d.json'%i);req(sha(p)==binding['new_raw_hashes'][str(i)],'new raw pin');doc=json.loads(p.read_text());integer(doc['id'],i);raw=doc['raw'];req(rat(raw['s'])==rat(node['s']),'new argument');a=rnd(box(raw['A']));e=next(maps);integer(e['pole'],0);d=e['data'];integer(d['id'],i);req(e['stage']=='mapped_new_A'and d['raw_sha256']==sha(p)and box(d['mapped_A'])==a,'new mapping');mapped_A.append(a);mapcount+=1
 req(next(maps,None)is None and mapcount==2120,'mapped exhaustion')
 panels=iter(stream(O/'PANELS.jsonl'));ms=moments();pc=0
 for n,value in enumerate(ms):
  e=next(panels);integer(e['pole'],0);integer(e['data']['n'],n);req(e['stage']=='moment'and rat(e['data']['value'])==value,'moment convolution');pc+=1
 pl,pu=pi();inverse=rnd((1/pu,1/pl));factor=scale(inverse,F(2));flags=[]
 for i,row in enumerate(r['rows']):
  progress({'stage':'schema_B','id':i});integer(row['id'],i);req(row==json.loads((O/('B_%03d.json'%i)).read_text()),'B copies');req(row['s']==nodes[i]['s'],'pole copy');integer(ledger[i]['id'],i);target=rat(ledger[i]['required_B_radius']);req(target>0 and rat(row['required_radius'])==target,'target copy')
  total=None
  for j in range(67):
   e=next(panels);integer(e['pole'],i);integer(e['data']['completed'],26*(j+1));req(e['stage']=='panel','panel stage');total=box(e['data']['sum']);pc+=1
  s=rat(row['s']);ss=mul((s,s),(s,s));eps=F(1,2**64);low=add(scale(mapped_A[i],eps),(-eps**3*F(17,60)/(3*ss[0]),F(0)));c=sub((F(1),F(1)),mul(ss,mapped_A[i]));high=(F(0),F(0))
  for n in range(40):high=add(high,scale(c,F((-1)**n,(2*n+1)*8**(2*n+1))));c=sub((F(ms[n+1]),F(ms[n+1])),mul(ss,c))
  high=add(high,(F(0),F(12**40,81*8**81)));quad=F(128,4**52);full=add(add(add(total,low),high),(-quad,quad));answer=mul(full,factor)
  e=next(panels);integer(e['pole'],i);req(e['stage']=='final_interval','final stage');d=e['data'];req(box(d['low'])==low and box(d['high'])==high and rat(d['quadrature_radius'])==quad and box(d['B'])==answer==box(row['B']),'low/high/final arithmetic');pc+=1
  req(type(row['target_met'])is bool and row['target_met']==((answer[1]-answer[0])/2<=target),'target gate');flags.append(row['target_met'])
 req(next(panels,None)is None and pc==25745,'panel exhaustion');req(type(r['all_targets_met'])is bool and r['all_targets_met']==all(flags),'all target summary');req(elapsed<299.5,'root input time')
 return {'status':'ACCEPTED_B378_SCHEMA','count':378,'mapped_rows':mapcount,'panel_records':pc,'result_sha256':sha(O/'RESULT.json'),'mapped_sha256':sha(O/'MAPPED_INPUTS.jsonl'),'panels_sha256':sha(O/'PANELS.jsonl'),'target_pass_count':sum(flags),'all_targets_met':all(flags),'independent_original_integrands_replayed':0,'independent_maps_moments_and_final_reconciliation':True,'witness_certified':False}
