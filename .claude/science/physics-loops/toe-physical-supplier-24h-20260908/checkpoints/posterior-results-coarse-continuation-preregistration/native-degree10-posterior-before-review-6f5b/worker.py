from pathlib import Path
from fractions import Fraction as F
import json,hashlib,time,os,math
import posterior

def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return[encode(v)for v in x]
 if isinstance(x,dict):return{k:encode(v)for k,v in x.items()}
 return x
def atomic(p,x):
 tmp=p.with_suffix(p.suffix+'.tmp')
 with tmp.open('w')as f:json.dump(encode(x),f,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
 tmp.replace(p)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def need(x,m):
 if not x:raise ValueError(m)
def run(b,out):
 start=time.monotonic();current={};rows=[]
 def progress(stage,data):
  nonlocal current
  current={'stage':stage,'data':data};atomic(out/'PARTIAL.json',{'current':current,'completed':len(rows),'seconds':time.monotonic()-start})
 def read(role):
  p=b['files'][role];progress('before_input',{'role':role});need(sha(p['path'])==p['sha256'],'source hash '+role);return json.loads(Path(p['path']).read_text())
 try:
  a=read('acceptance');rroot=read('root_freeze');r=read('result');w=read('worker_complete')
  need(a['status']=='ACCEPTED_NEW_DEGREE10_WARD_CERTIFICATE_ONCE'and a['result_sha256']==b['files']['result']['sha256']and a['worker_freeze']==b['worker_freeze']and a['root_freeze']==b['files']['root_freeze']['sha256']and rroot['worker_freeze']==a['worker_freeze'],'accepted chain')
  for value in [a['external_seconds'],w['seconds']]:need(type(value)in(int,float)and math.isfinite(value)and 0<value<20,'original seconds')
  for key in ['external_rss_bytes','sampled_whole_tree_peak']:need(type(a[key])is int and 0<a[key]<=384*1048576,'original RSS')
  need(w['status']=='COMPLETE_NEW_DEGREE10_ONLY'and w['runtime_sha256']==b['worker_freeze']and w['result_sha256']==a['result_sha256']and w['seconds']<=a['external_seconds'],'worker identity')
  need(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'worker RSS')
  need(r['status']=='COMPLETE_FIXED_DEGREE10_CERTIFICATE'and type(r['events'])is int and r['events']==205 and type(r['choices'])is int and r['choices']==2,'original census')
  need(type(r['rows'])is list and len(r['rows'])==2,'original rows')
  p=b['files']['events'];progress('before_events',{});need(sha(p['path'])==p['sha256'],'events hash');states={mode:{'s0':{},'q':{},'gate':None}for mode in ['residual','variational']}
  with Path(p['path']).open()as stream:
   count=0
   for line in stream:
    count+=1;progress('before_event',{'sequence':count});e=json.loads(line);need(type(e['sequence'])is int and e['sequence']==count,'event order');stage=e['stage'];mode=e['choice']
    if stage in ['source_moments','residual_raw','gate_inputs']:
     need(mode in states,'choice');s=states[mode];d=e['data']
     if stage=='source_moments':need(d['kind']in ['P','O']and d['kind']not in s['s0'],'source uniqueness');s['s0'][d['kind']]=d['s0']
     elif stage=='residual_raw':need(d['kind']in ['P','O']and d['kind']not in s['q'],'coefficient uniqueness');s['q'][d['kind']]=d['q']
     else:need(s['gate']is None,'gate uniqueness');s['gate']=d
  need(count==205,'event complete')
  for mode,original in zip(['residual','variational'],r['rows']):
   s=states[mode];need(set(s['s0'])=={'P','O'}and set(s['q'])=={'P','O'}and s['gate']is not None,'complete saved norms');need(original['mode']==mode and original['nominal']==s['gate']['nominal'],'nominal source relation')
   for k in ['P','O']:need(s['q'][k]==s['gate']['rows'][k]['q'],'q source relation')
   progress('saved_inputs',{'mode':mode,'inputs':s});atomic(out/(mode+'_INPUT.json'),s)
   def retain_norm(stage,data):
    atomic(out/(mode+'_NORMS.json'),data);progress(stage,dict(mode=mode,**data))
   ans=posterior.evaluate(s['s0'],s['q'],s['gate'],retain_norm);ans['mode']=mode;atomic(out/(mode+'_ARITHMETIC.json'),ans);rows.append(ans);progress('choice_complete',{'mode':mode})
  need(not ({x['status']for x in rows}>={'POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE'}),'contradictory signs')
  result={'status':'COMPLETE_NEW_POSTERIOR_WARD_ESTIMATOR','rows':rows,'choices':2,'source_events':205,'old_moments_recomputed':0,'new_error_estimator':True,'seconds':time.monotonic()-start};atomic(out/'RESULT.json',result);progress('complete',{})
 except BaseException as e:
  try:atomic(out/'FAILURE.json',{'error':repr(e),'current':current,'completed':len(rows)})
  except BaseException as z:e.add_note('retention '+repr(z))
  raise
