"""Durable caller for new quartic arithmetic only."""
import os,json,time
from pathlib import Path
import interval as I
import core,loader

def atomic(p,x):
 tmp=p.with_suffix(p.suffix+'.tmp')
 with tmp.open('w')as f:json.dump(I.encode(x),f,sort_keys=True);f.write('\n');f.flush();os.fsync(f.fileno())
 tmp.replace(p)
def run(binding,out):
 start=time.monotonic();current={};seq=0;rows=[];mode=None
 with(out/'EVENTS.ndjson').open('x')as log:
  def emit(stage,data):
   nonlocal seq,current
   seq+=1;current={'sequence':seq,'choice':mode,'stage':stage,'data':I.encode(data)}
   log.write(json.dumps(current,sort_keys=True)+'\n');log.flush();os.fsync(log.fileno());atomic(out/'PARTIAL.json',{'current':current,'completed':len(rows),'seconds':time.monotonic()-start})
  try:
   packet=loader.load(binding,emit);atomic(out/'INPUTS.json',packet)
   for mode in('residual','variational'):
    emit('choice_start',{'mode':mode});ans=core.evaluate(**packet[mode],emit=emit);ans['mode']=mode;atomic(out/(mode+'.json'),ans);rows.append(ans);emit('choice_complete',ans)
   if {r['status']for r in rows}>={'POSITIVE_CERTIFICATE','NEGATIVE_CERTIFICATE'}:raise ValueError('contradictory signs')
   mode=None;emit('complete',{'rows':rows});result={'status':'COMPLETE_NEW_QUARTIC_SPECTRAL_ESTIMATOR','rows':rows,'choices':2,'events':seq,'native_oracle_calls':0,'native_moments_recomputed':0,'old_trials_recomputed':0,'new_residual_moment_terms':112,'majorant_candidates':60,'seconds':time.monotonic()-start};atomic(out/'RESULT.json',result)
  except BaseException as error:
   try:atomic(out/'FAILURE.json',{'error':repr(error),'current':current,'rows':rows,'seconds':time.monotonic()-start})
   except BaseException as retention:error.add_note('retention '+repr(retention))
   raise
