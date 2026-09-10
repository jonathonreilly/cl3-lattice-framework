"""Independent source-map and new-jet arithmetic reconciliation."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
import independent as I
need=I.need;eq=I.compare
P=Path(__file__).resolve().parent.parent/'native-gaussian-high-moment-runtime-design'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def rat(x):
 need(type(x)is str and len(x)<=20000,'rational token');v=F(x);need(str(v)==x and max(abs(v.numerator).bit_length(),v.denominator.bit_length())<=32768,'canonical rational');return v
def box(x):
 need(type(x)is list and len(x)==2,'box');a,b=map(rat,x);need(a<=b,'box order');return a,b
def grid(x):
 a,b=box(x);return((I.bound(a.numerator*I.Q//a.denominator),I.bound(I.ceildiv(b.numerator*I.Q,b.denominator))),(0,0))
def complexbox(x):
 need(type(x)is list and len(x)==2,'complex shape');out=[]
 for v in x:
  need(type(v)is list and len(v)==2,'pair shape');a,b=map(I.bound,v);need(a<=b,'pair order');out.append((a,b))
 return tuple(out)
def timecheck(x,c):need(type(x)in(int,float)and math.isfinite(x)and 0<x<c,'finite time')
def source_packet(binding):
 def get(family,role,lines=False):
  p=binding[family]['files'][role];need(sha(p['path'])==p['sha256'],'source hash');text=Path(p['path']).read_text();return [json.loads(v)for v in text.splitlines()]if lines else json.loads(text)
 ev=get('degree20','events',True);need(len(ev)==255,'original255')
 for i,e in enumerate(ev,1):need(type(e['sequence'])is int and e['sequence']==i,'original sequence')
 scalars=[e['data']for e in ev if e['stage']=='scalar_inputs'and e['choice']is None];need(len(scalars)==1,'scalar uniqueness');s=scalars[0];reused=get('omega79','reused');omega=get('omega79','result');M={'0':['1','1'],'2':['6','6'],'4':['42','42']}
 for j,k in [(6,3),(8,4),(10,5)]:
  v=rat(reused[str(k)]);need(v.denominator==1 and v>0,'even integer');M[str(j)]=[str(v)]*2
 a,b=box(s['c']);M['1']=[str(3*a),str(3*b)];M['3']=s['nu'];M['5']=s['omega5']
 for name,row in zip(['omega7','omega9'],omega['rows']):need(row['observable']==name and row['status']=='CERTIFIED_TARGET','omega row');M[name[5:]]=row['interval']
 low={}
 for kind in ['P','O']:
  both=[]
  for mode in ['residual','variational']:
   rows=[e['data']for e in ev if e['stage']=='vacuum_moment_raw'and e['choice']==mode and e['data']['kind']==kind];need(len(rows)==7,'old moment count')
   for j,row in enumerate(rows):need(type(row['index'])is int and row['index']==j,'old index');a,b=box(row['imaginary']);need(a<=0<=b,'old reality')
   both.append(rows)
  eq(both[0],both[1],'old exact copies');low[kind]={str(j):grid(row['real'])for j,row in enumerate(both[0])};eq(low[kind]['0'],I.point(1),'m0')
 return M,low

def reconcile(packet,events,result,M,low,progress=lambda _:None):
 pos=0
 def take(stage,data=None):
  nonlocal pos
  need(pos<len(events),'missing event');e=events[pos];pos+=1;need(type(e['sequence'])is int and e['sequence']==pos and e['stage']==stage,'exact chronology '+stage)
  if data is not None:eq(e['data'],data,'event '+stage)
  progress({'stage':stage,'sequence':pos});return e['data']
 for family in ['degree20','omega79']:
  for role in ['acceptance','worker','receipt','root_freeze','result']:take('before_input',{'family':family,'role':role})
 take('before_input',{'family':'degree20','role':'events'});take('before_input',{'family':'omega79','role':'reused'})
 take('absolute_moment_source_map',{'rational':M,'old_even_indices':{'6':3,'8':4,'10':5}});absolute={k:grid(v)for k,v in M.items()};take('absolute_moment_grid',{'grid_bits':256,'moments':absolute})
 expected={'first_order':7,'grid_bits':256,'units':'dimensionless_h1','classes':{}}
 for kind in ['P','O']:
  D,B=I.source_tables({int(k):v for k,v in absolute.items()},kind);row={'D':{str(k):v for k,v in D.items()},'B':{str(k):v for k,v in B.items()},'accepted_m':low[kind]};expected['classes'][kind]=row;take('native_table',{'kind':kind,**row})
 eq(packet,expected,'complete physical packet');expectedrows=[]
 for kind in ['P','O']:
  row=expected['classes'][kind];D={int(k):v for k,v in row['D'].items()};B={int(k):v for k,v in row['B'].items()};take('accepted_lower_reused',{'kind':kind,'orders':list(range(7))})
  def emit(stage,data):take(stage,{'kind':kind,**data})
  high=I.high_logs(D,B,emit);hl=take('high_log_complete');eq(hl['kind'],kind,'high kind');eq(hl['ell'],high,'high logs');counts=hl['counts'];need(set(counts)=={'complex_products','operator_products'},'counter keys')
  for v in counts.values():need(type(v)is int and 0<=v<=300000,'counter cap')
  new=I.scalar_high({int(k):v for k,v in low[kind].items()},high,emit)
  expectedrows.append({'kind':kind,'orders':[7,8,9,10],'moments':new,'real_width_grid_units':{n:x[0][1]-x[0][0]for n,x in new.items()},'counts':counts})
 for row in expectedrows:
  widths={str(n):str(F(v[0][1]-v[0][0],I.Q))for n,v in row['moments'].items()};gate=all(F(v)<=F(1,10**6)for v in widths.values());row.update(widths=widths,target_full_width='1/1000000',width_gate=gate,status='CERTIFIED_PILOT_WIDTH'if gate else'INDETERMINATE_PRECISION');take('class_width_gate',row)
 need(result['status']=='COMPLETE_NEW_HIGH_MOMENT_PILOT','result status');eq(result['rows'],expectedrows,'final rows');eq(result['native_lower_moments_recomputed'],0,'no lower replay');eq(result['native_oracle_calls'],0,'no oracle');eq(result['first_order'],7,'high mask');eq(result['scope'],'only m7..10; absolute width pilot, no downstream Ward sufficiency','scope');eq(result['events'],len(events),'event count');take('complete',{'result':result});need(pos==len(events),'no trailing event');return len(expectedrows)

def check(out,rf,elapsed,progress=lambda _:None):
 out=Path(out);names={'STARTED.json','WORKER_COMPLETE.json','EVENTS.ndjson','PARTIAL.json','TABLES.json','RESULT.json'};need({p.name for p in out.iterdir()}==names and all(p.is_file()for p in out.iterdir()),'exact six files')
 raw={p.name:p.read_bytes()for p in out.iterdir()};read=lambda n:json.loads(raw[n]);done=read('WORKER_COMPLETE.json');result=read('RESULT.json');partial=read('PARTIAL.json');packet=read('TABLES.json');events=[json.loads(x)for x in raw['EVENTS.ndjson'].splitlines()];binding=json.loads((P/'BINDING.json').read_text());auth={'runtime_sha256':rf['worker_freeze'],'binding_sha256':sha(P/'BINDING.json'),'output':str(out.resolve()),'no_retry':True};eq(read('STARTED.json'),auth,'start auth');eq(done['runtime_sha256'],rf['worker_freeze'],'worker source');eq(done['binding_sha256'],auth['binding_sha256'],'binding');eq(done['result_sha256'],hashlib.sha256(raw['RESULT.json']).hexdigest(),'result hash');need(done['status']=='COMPLETE_NEW_HIGH_MOMENTS_ONLY','worker status')
 for v in [done['seconds'],result['seconds'],partial['seconds']]:timecheck(v,59)
 need(result['seconds']<=partial['seconds']<=done['seconds']<=elapsed<59.5,'time ordering');need(type(done['rss_bytes'])is int and 0<done['rss_bytes']<=384*1048576,'RSS');eq(partial['current'],events[-1],'final partial');M,low=source_packet(binding);count=reconcile(packet,events,result,M,low,progress)
 hashes={name:hashlib.sha256(data).hexdigest()for name,data in raw.items()}
 for name,h in hashes.items():need(sha(out/name)==h,'final output hash')
 need({p.name for p in out.iterdir()}==names and all(p.is_file()for p in out.iterdir()),'final exact six files')
 return {'status':'PASS_INDEPENDENT_HIGH_JET_ARITHMETIC','count':count,'events':len(events),'result_sha256':hashes['RESULT.json'],'output_hashes':hashes,'lower_native_replay':False,'new_jet_arithmetic_reconciled':True,'raw_scalar_truth_inherited':True}
