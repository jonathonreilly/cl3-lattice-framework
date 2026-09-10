"""Explicit future worker, streaming new rows only. No executable launcher."""
import json,time
from fractions import Fraction as F
import interval as iv,append_core as core,binder

def run(plan,out):
 start=time.monotonic();progress={'stage':'binding','rows':0,'entries':0,'current':None}
 def save(): (out/'PARTIAL.json').write_text(json.dumps(progress)+'\n')
 save()
 try:
  poles,values,alpha,a0,c,cache=binder.load(plan)
  progress['stage']='append';save()
  with (out/'APPEND.ndjson').open('x') as f:
   def emit(row):
    # An offending computed row survives before all arithmetic/scientific gates.
    progress['current']={k:v for k,v in row.items() if k!='entries'}
    f.write(json.dumps(row,separators=(',',':'))+'\n');f.flush()
    progress['rows']+=1;progress['entries']+=len(row['entries']);save()
   def before(case):
    progress['current']=case;save()
   result=core.stream(poles,values,alpha,a0,c,emit,before)
  progress['stage']='gates';save()
  if result['entries']!=5970 or result['rows']!=1995:raise ValueError('fixed append census')
  orbits=[]
  for i,(old,extra) in enumerate(zip(cache['orbits'],result['append_closed_traces'])):
   if old['orbit']!=list(core.ORBITS[i]) or old['denominator']!=iv.S:raise ValueError('orbit identity')
   trace=iv.add(tuple(old['closed_trace']),tuple(extra))
   old_radius=F(old['arithmetic_radius']) # cache52536 stores an exact rational string
   total_radius=old_radius+F(result['append_arithmetic_radius'],iv.S)
   row={'orbit':list(core.ORBITS[i]),'closed_trace':trace,'arithmetic_radius':str(total_radius),'raw_rows':399,'closed_rows':798}
   orbits.append(row);progress['orbit_gates']=orbits;save()
   if trace[0]<0 or trace[1]>=531*iv.S or total_radius>F(1,2**60):raise ValueError('augmented trace/arithmetic gate')
  result.update(status='COMPLETE_APPEND_MIDPOINT_ARITHMETIC',orbits=orbits,append_sha256=binder.sha(out/'APPEND.ndjson'),seconds=time.monotonic()-start,physical_radius_metadata={'eta_A_max':'1/1000000000000000000000000000000','eta_B_max':'1/10000000000000000000','eta_c_max':'1/10000000000000000000','eta_a0_max':'1/1000000000000000000000000000000','input_factor_bound':'21/5000','compression_separate':True},pure_state_computed=False,time_generator_computed=False)
  (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 except BaseException as e:
  progress.update(error=repr(e),seconds=time.monotonic()-start);save();(out/'FAILURE.json').write_text(json.dumps(progress)+'\n');raise
