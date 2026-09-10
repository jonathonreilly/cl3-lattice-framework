import json,time,os,hashlib,math
from pathlib import Path
import interval as I
import compute

def need(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def atomic(p,v):
 t=p.with_suffix(p.suffix+'.tmp')
 with t.open('w')as f:json.dump(I.encode(v),f,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
 t.replace(p)
def load_metadata(b):
 def rd(name):
  path=b['files'][name];need(sha(path)==b['inputs'][path],'accepted pin '+name);return json.loads(Path(path).read_text())
 a=rd('acceptance');r=rd('result');w=rd('worker_receipt');rr=rd('root_receipt');rf=rd('root_freeze')
 need(a['status']=='ACCEPTED_NEW_DEGREE10_WARD_CERTIFICATE_ONCE'and a['once']is True and a['independent_word_and_error_reconciliation']is True,'accepted original certificate')
 need(a['worker_freeze']==b['producer_worker']and a['root_freeze']==b['inputs'][b['files']['root_freeze']]and rf['worker_freeze']==b['producer_worker'],'producer root relation')
 need(a['result_sha256']==b['inputs'][b['files']['result']]and w['result_sha256']==a['result_sha256']and w['runtime_sha256']==a['worker_freeze']and w['status']=='COMPLETE_NEW_DEGREE10_ONLY','producer result relation')
 need(rr['pass']is True and type(rr['returncode'])is int and rr['returncode']==0 and rr['worker_freeze']==a['worker_freeze'],'producer root completion')
 for x in [a['external_seconds'],rr['seconds'],w['seconds']]:need(type(x)in(int,float)and math.isfinite(x)and 0<x<20,'original finite timing')
 for x in [a['external_rss_bytes'],a['sampled_whole_tree_peak'],rr['sampled_whole_tree_peak']]:need(type(x)is int and 0<x<=384*1048576,'original RSS')
 need(r['status']=='COMPLETE_FIXED_DEGREE10_CERTIFICATE'and type(r['events'])is int and r['events']==205 and type(r['choices'])is int and r['choices']==2,'original census')
 need([x['mode']for x in r['rows']]==['residual','variational']and len(r['rows'])==2,'fixed original modes')
 need(sha(b['files']['events'])==b['inputs'][b['files']['events']],'immutable205 events')
 return r

def run(b,out):
 start=time.monotonic();rows=[];current=0;mode=None;stage='initial';extracted={}
 def progress(s,data):
  nonlocal stage
  stage=s;atomic(out/'PARTIAL.json',{'stage':stage,'source_sequence':current,'choice':mode,'rows':rows,'extracted':extracted,'current':data,'seconds':time.monotonic()-start})
 try:
  progress('binding',{});r=load_metadata(b)
  with Path(b['files']['events']).open()as f:
   def event(expected_stage,expected_choice):
    nonlocal current
    current+=1;progress('before_saved_event',{'expected_stage':expected_stage,'expected_choice':expected_choice})
    line=f.readline(1048577);need(bool(line)and len(line)<=1048576,'bounded saved event');x=json.loads(line)
    need(type(x['sequence'])is int and x['sequence']==current and x['stage']==expected_stage and x['choice']==expected_choice,'saved chronology')
    return x['data']
   event('binding',None);event('scalar_inputs',None)
   for mode in ['residual','variational']:
    event('choice_start',mode);s0={}
    for kind in ['P','O']:
     for name in ['moments','polynomial','source_moments','residual_raw']:
      data=event(name,mode);need(data['kind']==kind,'saved class')
      if name=='source_moments':s0[kind]=I.box(data['s0'])
    for i in range(1,91):
     data=event('ordered_word',mode);need(type(data['index'])is int and data['index']==i,'saved word census')
    data=event('gate_inputs',mode);E=I.box(data['E']);extracted[mode]={'E':E,'s0P':s0['P'],'s0O':s0['O'],'gate_event':current}
    progress('extracted_before_arithmetic',extracted[mode]);row=compute.screen(E,s0['P'],s0['O']);row['mode']=mode;row['source_gate_event']=current
    atomic(out/(mode+'.json'),row);rows.append(I.encode(row));progress('screen_retained',row)
    data=event('choice_complete',mode);need(data['row']==r['rows'][len(rows)-1],'original result row binding')
   mode=None;event('complete',None);need(not f.read(1)and current==205,'saved final census')
  result={'status':'COMPLETE_SAVED_ALLQ_SCREEN','rows':rows,'modes':2,'saved_events':205,'all_fixed_first_polynomials_excluded':all(x['excluded']for x in rows),'native_calls':0,'original_moments_recomputed':0,'scope':'unchanged degree1 first polynomials and e858 error functional only; not alpha no-go','seconds':time.monotonic()-start}
  progress('complete',{'rows':rows});result['seconds']=time.monotonic()-start;atomic(out/'RESULT.json',result)
 except BaseException as e:
  try:atomic(out/'FAILURE.json',{'error':repr(e),'stage':stage,'source_sequence':current,'choice':mode,'rows':rows,'extracted':extracted,'seconds':time.monotonic()-start})
  except BaseException as er:e.add_note('retention '+repr(er))
  raise
