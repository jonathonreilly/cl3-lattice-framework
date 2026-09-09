import json,hashlib,time,re
from pathlib import Path
from fractions import Fraction as F
import core

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def scalar(x):
 if type(x)is not str or len(x)>20000 or not re.fullmatch(r'-?\d+(?:/\d+)?',x):raise ValueError('canonical scalar string')
 v=F(x)
 if str(v)!=x:raise ValueError('canonical rational')
 core.box((v,v));return v
def pair(x):
 if type(x)is not list or len(x)!=2:raise ValueError('pair')
 return core.box(tuple(map(scalar,x)))
def run(binding,out):
 start=time.monotonic();seq=0;rows=[];stage='binding'
 def encode(x):
  if type(x)is F:return str(x)
  raise TypeError(type(x).__name__)
 def save(n,x):
  p=out/n;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(x,default=encode)+'\n');t.replace(p)
 def emit(x):
  nonlocal seq
  seq+=1;save(f'EVENT_{seq:04d}.json',x);save('PARTIAL.json',{'stage':stage,'event':seq,'rows':rows,'seconds':time.monotonic()-start})
 def read(p):
  if binding['inputs'].get(str(p))!=sha(p):raise ValueError('bound read '+str(p))
  return json.loads(Path(p).read_text())
 emit({'stage':stage})
 try:
  for name,b in binding['families'].items():
   a=read(b['acceptance']);post=read(b['post_acceptance'])
   core.require(a['status']==b['acceptance_status']and post['status']==b['post_status'],'accepted status')
   core.require(a['result_sha256']==post['result_sha256']==sha(b['result']),'result binding')
   for key in ['worker_freeze','root_freeze']:core.require(a[key]==post[key]==sha(b[key]),'producer freeze')
   core.require(post['post_result_sha256']==sha(b['post_result'])and post['post_worker_freeze']==sha(b['post_worker_freeze'])and post['post_root_freeze']==sha(b['post_root_freeze']),'post binding')
  d=binding['families']['dual'];n=binding['families']['nu'];dr=read(d['result']);nr=read(n['result']);dt=read(str(Path(d['result']).parent/'TAILS.json'));nt=read(str(Path(n['result']).parent/'TAIL.json'))
  geom=read(binding['geometry']);first=geom['nodes'][0];core.require(type(first['id'])is int and first['id']==0 and first['panel']==-64,'first node identity');l,u=first['endpoint_ids'];cat=read(binding['catalog_result']);raw=[]
  for idx in [l,u]:
   core.require(type(idx)is int and 0<=idx<3484,'endpoint index');row=cat['rows'][idx];core.require(type(row['id'])is int and row['id']==idx and row['gate']=='PASS'and row['path']==f'ORACLES/{idx:04d}.json','endpoint row');p=Path(binding['catalog_result']).parent/row['path'];v=read(str(p));core.require(sha(p)==row['sha256']and v['catalog_endpoint']==geom['endpoints'][idx]and v['s']==geom['endpoints'][idx]['s'],'endpoint binding');raw.append(pair(v['A']))
  firstbox=(pair(first['t_interval']),(raw[1][0],raw[0][1]));pi=core.machin()
  for k,kind in enumerate(['cminus','mu','nu']):
   stage=kind;emit({'stage':stage});b=d if k<2 else n;base=Path(b['result']).parent;panels=[]
   for j in range(67):
    emit({'stage':'load_panel','kind':kind,'panel':j});p=read(str(base/f'PANELS/{j:02d}.json'));panels.append({'panel':p['panel'],'value':pair(p['values'][k]if k<2 else p['value']),'cumulative':pair(p['cumulatives'][k]if k<2 else p['cumulative'])})
   if k<2:saved={'middle':panels[-1]['cumulative'],'low':pair(dt['low_intervals'][k]),'high':(scalar(dt['high_partials'][k]),scalar(dt['high_remainders'][k])),'radius':scalar(dt['quadrature_radii'][k]),'interval':pair(dr['rows'][k]['interval'])}
   else:saved={'middle':pair(nr['middle']),'low':pair(nt['low_interval']),'high':(scalar(nt['high_partial']),scalar(nt['high_remainder'])),'radius':scalar(nt['quadrature_radius']),'interval':pair(nr['interval'])}
   answer=core.recertify(kind,panels,saved,pi,firstbox,emit);answer['observable']=kind;rows.append(answer);save(f'{kind}.json',answer);emit({'stage':'row_complete','kind':kind})
  stage='complete';emit({'stage':stage});save('RESULT.json',{'status':'COMPLETE_NEW_RHO5_COMPONENT_CERTIFICATES','rows':rows,'all_targets_met':all(r['target_met']for r in rows),'oracle_calls':0,'node_integrands_recomputed':0,'seconds':time.monotonic()-start})
 except BaseException as e:save('FAILURE.json',{'stage':stage,'event':seq,'error':repr(e)});raise
