"""Guarded caller of new high-jet arithmetic; source imports are inert."""
import json,os,time
from pathlib import Path
from fractions import Fraction as F
import engine,loader,core
atomic=engine.atomic
TARGET=F(1,10**6)
def run(binding,out):
 start=time.monotonic();seq=0;current={}
 with(out/'EVENTS.ndjson').open('x')as stream:
  def emit(stage,data):
   nonlocal seq,current
   seq+=1;current={'sequence':seq,'stage':stage,'data':data};stream.write(json.dumps(current,sort_keys=True)+'\n');stream.flush();os.fsync(stream.fileno());atomic(out/'PARTIAL.json',{'current':current,'seconds':time.monotonic()-start})
  try:
   packet=loader.load_packet(binding,emit);atomic(out/'TABLES.json',packet);r=engine.compute(packet,emit)
   for row in r['rows']:
    widths={str(n):str(F(x[0][1]-x[0][0],core.S))for n,x in row['moments'].items()};row['widths']=widths;row['target_full_width']=str(TARGET);row['width_gate']=all(F(v)<=TARGET for v in widths.values());row['status']='CERTIFIED_PILOT_WIDTH'if row['width_gate']else'INDETERMINATE_PRECISION';emit('class_width_gate',row)
   r['status']='COMPLETE_NEW_HIGH_MOMENT_PILOT';r['scope']='only m7..10; absolute width pilot, no downstream Ward sufficiency';r['seconds']=time.monotonic()-start;r['events']=seq+1;emit('complete',{'result':r});atomic(out/'RESULT.json',r)
  except BaseException as e:
   try:atomic(out/'FAILURE.json',{'error':repr(e),'current':current,'seconds':time.monotonic()-start})
   except BaseException as err:e.add_note('retention '+repr(err))
   raise
