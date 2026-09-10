import json,time,os,hashlib,math
from pathlib import Path
from fractions import Fraction as F
import interval as I
import compute

def need(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
def atomic(p,data):
 t=p.with_suffix(p.suffix+'.tmp')
 with t.open('w')as f:json.dump(I.encode(data),f,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
 t.replace(p)
def load_base(b):
 def rd(k):
  path=b['files'][k];need(sha(path)==b['inputs'][path],'input hash '+k);return json.loads(Path(path).read_text())
 a=rd('acceptance');need(a['status']=='ACCEPTED_NEW_RHO5_MOMENT_COMPONENT_CERTIFICATES','accepted status');need(a['result_sha256']==b['inputs'][b['files']['result']]and a['worker_freeze']==b['producer_worker']and a['root_freeze']==b['producer_root'],'accepted provenance')
 v=a['external_seconds'];need(type(v)in(int,float)and math.isfinite(v)and v>0,'accepted seconds')
 for k in ['external_rss_bytes','sampled_whole_tree_peak']:
  v=a[k];need(type(v)is int and v>0,'accepted integer resources')
 need(a['external_seconds']<30 and a['external_rss_bytes']<=384*1048576 and a['sampled_whole_tree_peak']<=384*1048576,'accepted cap')
 r=rd('result');w=rd('worker_receipt');need(w['status']=='COMPLETE_NEW_RHO5_ONLY'and w['result_sha256']==a['result_sha256']and w['runtime_sha256']==a['worker_freeze'],'producer completion')
 need(r['status']=='COMPLETE_NEW_RHO5_COMPONENT_CERTIFICATES'and r['all_targets_met']is True,'producer scientific status');need(type(r['oracle_calls'])is int and r['oracle_calls']==0 and type(r['node_integrands_recomputed'])is int and r['node_integrands_recomputed']==0,'producer scope')
 need(type(r['rows'])is list and len(r['rows'])==3,'producer row count');values={}
 for name,row in zip(['cminus','mu','nu'],r['rows']):
  need(row['observable']==name and row['target_met']is True,'producer observable');v=I.box(row['interval']);need(I.parse(row['width'])==v[1]-v[0]and I.parse(row['target'])==F(2,10**28)and v[1]-v[0]<=F(2,10**28),'accepted width');values[name]=v
 return I.scale(values['mu'],F(1,3)),values['nu']
def load(b):
 if b.get('omega5')is None:raise ValueError('NOT_READY: omega5 acceptance absent')
 c,nu=load_base(b);o=b['omega5']
 def rd(name):
  path=o[name];need(b['inputs'].get(path)==sha(path),'omega5 immutable input');return json.loads(Path(path).read_text())
 a=rd('acceptance');r=rd('result');w=rd('worker_receipt')
 need(a['status']==o['accepted_status']and a['result_sha256']==sha(o['result'])and a['worker_freeze']==o['worker_freeze'],'omega5 acceptance')
 need(w['status']=='COMPLETE_NEW_OMEGA5_ONLY'and w['runtime_sha256']==o['worker_freeze']and w['result_sha256']==sha(o['result']),'omega5 worker')
 need(r['observable']=='omega5=E_X_power_5_over_2'and r['status']=='CERTIFIED_TARGET','omega5 scientific result')
 interval=I.box(r['interval']);need(I.parse(r['width'])==interval[1]-interval[0]and I.parse(r['target'])==F(1,10**24)and interval[1]-interval[0]<=F(1,10**24),'omega5 target')
 need(type(r['oracle_calls'])is int and r['oracle_calls']==0,'omega5 no oracle');need(0<interval[0]<=interval[1]<168,'omega5 analytic range')
 return c,nu,interval
def run(b,out):
 start=time.monotonic();rows=[];seq=0;current='start';mode=None
 with (out/'EVENTS.ndjson').open('x')as log:
  def emit(stage,data):
   nonlocal seq,current
   current=stage;seq+=1;event={'sequence':seq,'choice':mode,'stage':stage,'data':I.encode(data)}
   log.write(json.dumps(event,sort_keys=True)+'\n');log.flush();os.fsync(log.fileno())
   atomic(out/'PARTIAL.json',{'stage':stage,'sequence':seq,'choice':mode,'rows':rows,'seconds':time.monotonic()-start,'event':event})
  try:
   emit('binding',{'binding_sha256':b['_binding_file_sha256'],'native_oracle_calls':0})
   c,nu,omega5=load(b);emit('scalar_inputs',{'c':c,'nu':nu,'omega5':omega5})
   need(F(3,4)<c[0]<=c[1]<F(49,60)and 0<nu[0]<=nu[1]<16,'native analytic ranges')
   for mode in ['residual','variational']:
    emit('choice_start',{'mode':mode})
    try:row=compute.run_choice(c,nu,omega5,mode,emit)
    except (ValueError,ZeroDivisionError)as e:row={'mode':mode,'status':'INDETERMINATE_ARITHMETIC','error':repr(e),'failed_stage':current}
    rows.append(I.encode(row));atomic(out/(mode+'.json'),rows[-1]);emit('choice_complete',{'row':rows[-1]})
   mode=None
   statuses=[r['status']for r in rows];need(not('POSITIVE_CERTIFICATE'in statuses and'NEGATIVE_CERTIFICATE'in statuses),'contradictory signs')
   result={'status':'COMPLETE_FIXED_DEGREE11_CERTIFICATE','rows':rows,'choices':2,'oracle_calls':0,'new_covariance_calls':0,'scope':'dimensionless h=1 original native Ward boundary certificate','binding_sha256':b['_binding_file_sha256'],'sign_certified':any(x in ['POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE']for x in statuses),'seconds':time.monotonic()-start}
   emit('complete',{'rows':rows});result['events']=seq;result['seconds']=time.monotonic()-start;atomic(out/'RESULT.json',result)
  except BaseException as e:
   try:atomic(out/'FAILURE.json',{'error':repr(e),'stage':current,'choice':mode,'rows':rows,'sequence':seq,'seconds':time.monotonic()-start})
   except BaseException as er:e.add_note('failure retention '+repr(er))
   raise
