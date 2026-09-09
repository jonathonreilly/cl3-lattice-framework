import json,hashlib,math,re
from pathlib import Path
from fractions import Fraction as F

def need(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def scalar(x):
 need(type(x)is str and len(x)<=20000 and re.fullmatch(r'-?\d+(?:/\d+)?',x)is not None,'rational syntax');v=F(x);need(str(v)==x and max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=32768,'bounded canonical rational');return v
def pair(x):
 need(type(x)is list and len(x)==2,'pair');a,b=map(scalar,x);need(a<=b,'ordered pair');return a,b
def literal(x,n):need(type(x)is int and x==n,'literal integer')
def check(out,rf,elapsed,progress=lambda x:None):
 out=Path(out);rd=lambda n:json.loads((out/n).read_text());r=rd('RESULT.json');w=rd('WORKER_COMPLETE.json');p=rd('PARTIAL.json')
 need(rd('STARTED.json')==rf['authorization'],'STARTED');need(w['status']=='COMPLETE_NEW_RHO5_ONLY'and w['runtime_sha256']==rf['worker_freeze']and w['binding_sha256']==rf['binding_sha256']and w['result_sha256']==sha(out/'RESULT.json'),'worker binding')
 for x in [r['seconds'],w['seconds'],p['seconds'],elapsed]:need(type(x)in(int,float)and math.isfinite(x)and 0<x<30,'finite time')
 need(p['seconds']<=r['seconds']<=w['seconds']<29 and w['seconds']<=elapsed,'nested time');need(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'RSS')
 need(r['status']=='COMPLETE_NEW_RHO5_COMPONENT_CERTIFICATES','status');literal(r['oracle_calls'],0);literal(r['node_integrands_recomputed'],0);need(type(r['rows'])is list and len(r['rows'])==3 and p['rows']==r['rows']and p['stage']=='complete','three rows/partial')
 b=json.loads(Path(rf['binding_path']).read_text());need(sha(rf['binding_path'])==rf['binding_sha256'],'binding file')
 def source(path):need(b['inputs'].get(str(path))==sha(path),'source pin');return json.loads(Path(path).read_text())
 seq=0
 def event(expected):
  nonlocal seq
  seq+=1;got=rd(f'EVENT_{seq:04d}.json');need(got==expected,'event payload '+str(seq))
  # Python equality allows bool/int aliases: reject them recursively for index fields.
  if 'index'in got:literal(got['index'],expected['index'])
  if 'panel'in got:literal(got['panel'],expected['panel'])
  if 'input'in got:literal(got['input']['panel'],expected['input']['panel'])
 event({'stage':'binding'});flags=[]
 for k,name in enumerate(['cminus','mu','nu']):
  row=r['rows'][k];need(row['observable']==name and rd(name+'.json')==row,'row binding');a,z=pair(row['interval']);lo,hi=pair(row['original_interval']);width=scalar(row['width']);need(lo<=a<=z<=hi and width==z-a and scalar(row['target'])==F(2,10**28),'interval and target');need(type(row['target_met'])is bool and row['target_met']==(width<=F(2,10**28)),'flag');literal(row['oracle_calls'],0);literal(row['node_integrands_recomputed'],0);flags.append(row['target_met'])
  family=b['families']['dual'if k<2 else'nu'];base=Path(family['result']).parent;old=source(family['result']);tail=source(base/('TAILS.json'if k<2 else'TAIL.json'));panels=[]
  event({'stage':name})
  for j in range(67):
   event({'stage':'load_panel','kind':name,'panel':j});raw=source(base/f'PANELS/{j:02d}.json');literal(raw['panel'],j-64);v=raw['values'][k]if k<2 else raw['value'];c=raw['cumulatives'][k]if k<2 else raw['cumulative'];pair(v);pair(c);panels.append({'panel':j-64,'value':v,'cumulative':c})
  for j,x in enumerate(panels):event({'stage':'panel','index':j,'input':x})
  low=tail['low_intervals'][k]if k<2 else tail['low_interval'];high=[tail['high_partials'][k],tail['high_remainders'][k]]if k<2 else[tail['high_partial'],tail['high_remainder']];pair(low);[scalar(x)for x in high]
  oldrad=tail['quadrature_radii'][k]if k<2 else tail['quadrature_radius'];newrad=str([F(85,6*5**52),F(50,5**52),F(300,5**52)][k]);need(scalar(oldrad)==[F(544,45*4**52),F(128,3*4**52),F(256,4**52)][k],'old radius')
  middle=panels[-1]['cumulative'];need(row['original_interval']==(old['rows'][k]['interval']if k<2 else old['interval']),'original source interval')
  event({'stage':'components','middle':middle,'low':low,'high':high,'old_radius':oldrad,'new_radius':newrad});event({'stage':'new_interval','interval':row['interval']});event({'stage':'row_complete','kind':name})
 event({'stage':'complete'});need(type(r['all_targets_met'])is bool and r['all_targets_met']==all(flags),'overall target');literal(p['event'],416);need(seq==416,'schedule length')
 expected={'RESULT.json','WORKER_COMPLETE.json','STARTED.json','PARTIAL.json','cminus.json','mu.json','nu.json'}|{f'EVENT_{i:04d}.json'for i in range(1,417)};need({x.name for x in out.iterdir()}==expected,'membership');progress({'stage':'verified_saved_receipts'})
 return {'status':'PASS_NEW_CERTIFICATE_SCHEMA','all_targets_met':all(flags),'rows':3,'events':416,'node_formulas_replayed':0,'scope':'all event/source/target bindings; worker performs arithmetic'}
