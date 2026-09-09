"""Prospective childless stream body. No dispatcher/native launch enabled."""
import json,time,os
from fractions import Fraction as F
import interval as iv,core,binder

def run(plan,out):
 if plan.get('status')!='ROOT_REVIEWED_FIRST_ACTION_APPEND':raise ValueError('NOTREADY')
 start=time.monotonic();progress={'stage':'binding','current':None,'rows':0,'entries':0}
 def save(name='PARTIAL.json'):
  p=out/name;t=p.with_suffix('.tmp');t.write_text(json.dumps(progress)+'\n');os.replace(t,p)
 save()
 try:
  poles,values,alpha,c,mu,old,physical=binder.load(plan)
  progress.update(stage='append',mu_metadata=physical);save()
  with (out/'FIRST_ACTION_APPEND.ndjson').open('x') as f:
   def emit(row):
    f.write(json.dumps(row,separators=(',',':'))+'\n');f.flush()
    progress.update(current={k:v for k,v in row.items() if k!='entries'},rows=progress['rows']+1,entries=progress['entries']+len(row['entries']));save()
   def before(row):progress.update(current=row);save()
   result=core.stream(poles,values,alpha,c,mu,emit,before)
  progress['stage']='combined_gates';save()
  if result['rows']!=2010 or result['entries']!=6015:raise ValueError('fixed census')
  orbits=[]
  for i,(prior,extra) in enumerate(zip(old['orbits'],result['append_closed_traces'])):
   if prior['orbit']!=list(core.ORBITS[i]) or prior['raw_rows']!=399 or prior['closed_rows']!=798:raise ValueError('original domain')
   trace=iv.add(tuple(prior['closed_trace']),tuple(extra));radius=F(prior['arithmetic_radius'])+F(result['append_arithmetic_radius'],iv.S)
   row={'orbit':list(core.ORBITS[i]),'data_raw_rows':402,'data_closed_rows':804,'original_raw_rows':399,'original_closed_rows':798,'closed_trace':trace,'arithmetic_radius':str(radius)}
   orbits.append(row);progress['orbit_gates']=orbits;save()
   if extra!=iv.rational(5) or not 0<=trace[0]<=trace[1]<536*iv.S or radius>F(1,2**60):raise ValueError('complete804 trace/arithmetic')
  result.update(status='COMPLETE_FIRST_ACTION_DATA_APPEND_MIDPOINT_ONLY',orbits=orbits,append_sha256=binder.sha(out/'FIRST_ACTION_APPEND.ndjson'),physical_input_metadata=physical,seconds=time.monotonic()-start,generator_assembled=False,leakage_computed=False,propagation_computed=False)
  (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 except BaseException as e:
  progress.update(error=repr(e),seconds=time.monotonic()-start);save();save('FAILURE.json');raise
