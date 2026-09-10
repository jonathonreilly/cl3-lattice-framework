from pathlib import Path
import json,time,math
from source import atomic,sha,need,load_family,selected
import dual

def run(b,out):
 start=time.monotonic();current={};rows=[];mode=None;sequence=0
 with(out/'EVENTS.ndjson').open('x')as log:
  def emit(stage,data):
   nonlocal current,sequence
   from source import encode
   sequence+=1;current={'sequence':sequence,'choice':mode,'stage':stage,'data':encode(data)}
   log.write(json.dumps(current,sort_keys=True)+'\n');log.flush()
   # Every pair is small; durable current and accumulated stream before advancing.
   import os
   os.fsync(log.fileno());atomic(out/'PARTIAL.json',{'current':current,'completed':len(rows)})
  def read(role):
   p=b['spectral'][role];emit('before_input',{'role':role});need(sha(p['path'])==p['sha256'],'pin '+role);return json.loads(Path(p['path']).read_text())
  try:
   a=read('acceptance');rr=read('receipt');rf=read('root_freeze');w=read('worker');result=read('result');binding=read('binding')
   need(a['status']=='ACCEPTED_NEW_SPECTRAL_RESIDUAL_ESTIMATOR_ONCE'and a['once']is True,'accepted spectral')
   need(a['result_sha256']==b['spectral']['result']['sha256']==w['result_sha256']and a['worker_freeze']==b['spectral']['worker_freeze']==w['runtime_sha256']==rr['worker_freeze']==rf['worker_freeze'],'spectral source chain')
   need(a['root_freeze']==b['spectral']['root_freeze']['sha256']and w['binding_sha256']==b['spectral']['binding']['sha256']and binding['degree10']==b['degree10'],'same original degree10 family')
   need(w['status']=='COMPLETE_NEW_SPECTRAL_RESIDUAL_ONLY'and rr['pass']is True and type(rr['returncode'])is int and rr['returncode']==0,'completed source')
   for value,cap in [(w['seconds'],29),(rr['seconds'],29.5),(a['external_seconds'],30)]:need(type(value)in(int,float)and math.isfinite(value)and 0<value<cap,'source timing')
   need(w['seconds']<=rr['seconds']<=a['external_seconds'],'source timing order')
   for value in [w['rss_bytes'],rr['sampled_whole_tree_peak'],a['external_rss_bytes'],a['sampled_whole_tree_peak']]:need(type(value)is int and 0<value<=384*1048576,'source RSS')
   need(rr['sampled_whole_tree_peak']==a['sampled_whole_tree_peak'],'source RSS relation')
   need(result['status']=='COMPLETE_NEW_SPECTRAL_RESIDUAL_ESTIMATOR'and type(result['choices'])is int and result['choices']==2 and type(result['rows'])is list and len(result['rows'])==2,'source result')
   original,events=load_family(b['degree10'],emit);scalar=selected(events,'scalar_inputs',None)
   for mode,spectral in zip(['residual','variational'],result['rows']):
    need(spectral['mode']==mode and spectral['status']in ['POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE','INDETERMINATE_SIGN'],'usable source bound')
    gate=selected(events,'gate_inputs',mode);need(spectral['nominal']==gate['nominal'],'same nominal')
    coefficients={}
    for k in ['P','O']:
     p=selected(events,'polynomial',mode,k);q=selected(events,'residual_raw',mode,k)
     need(p['p0']==gate['rows'][k]['p0']and p['p1']==gate['rows'][k]['p1']and q['q']==gate['rows'][k]['q'],'original coefficient identity')
     coefficients[k]={'p0':p['p0'],'p1':p['p1'],'q':q['q']}
    inputs={'c':scalar['c'],'nu':scalar['nu'],'coefficients':coefficients,'nominal':gate['nominal'],'E_upper':spectral['E_upper'],'F_upper':spectral['F_upper'],'spectral_alpha_interval':spectral['alpha_interval']};atomic(out/(mode+'_INPUT.json'),inputs);emit('new_inputs',inputs)
    try:ans=dual.evaluate(inputs,emit)
    except(ValueError,ZeroDivisionError)as e:ans={'status':'INDETERMINATE_ARITHMETIC','error':repr(e),'stage':current['stage'],'unique_gram_sets':None,'actual_Wick_words':None}
    ans['mode']=mode;atomic(out/(mode+'.json'),ans);rows.append(ans);emit('choice_complete',ans)
   need(not {x['status']for x in rows}>={'POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE'},'contradictory signs');mode=None
   final={'status':'COMPLETE_NEW_REDUCED_DUAL_ESTIMATOR','rows':rows,'choices':2,'max_unique_gram_sets':4,'max_actual_Wick_words':684,'logical_Wick_words':5130,'native_oracle_calls':0,'old_moments_recomputed':0,'old_nominal_recomputed':0,'seconds':time.monotonic()-start};emit('complete',{});final['events']=sequence;atomic(out/'RESULT.json',final)
  except BaseException as e:
   try:atomic(out/'FAILURE.json',{'error':repr(e),'current':current,'completed':len(rows)})
   except BaseException as z:e.add_note('retention '+repr(z))
   raise
