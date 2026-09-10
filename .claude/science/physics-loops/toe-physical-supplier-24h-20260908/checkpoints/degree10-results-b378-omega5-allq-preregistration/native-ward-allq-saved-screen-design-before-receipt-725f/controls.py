import tempfile,json
from pathlib import Path
from fractions import Fraction as F
import compute,worker,interval as I
checks=0
def ok(x):
 global checks
 if not x:raise AssertionError(checks)
 checks+=1
ok(compute.screen(I.point(10),I.point(1),I.point(1))['excluded'])
ok(not compute.screen((F(0),F(100)),I.point(1),I.point(1))['excluded'])
ok(not compute.screen(I.point(10),(F(0),F(10000)),(F(0),F(10000)))['excluded'])
try:compute.screen((F(-1),F(1)),I.point(1),I.point(1))
except ValueError:ok(True)
else:ok(False)
# Entire synthetic205-event source sequence, no original input or moments.
with tempfile.TemporaryDirectory(prefix='allq-metadata-synthetic-')as td:
 p=Path(td);events=[];rows=[{'mode':x,'status':'INDETERMINATE_SIGN'}for x in ['residual','variational']]
 def add(stage,choice,data):events.append({'sequence':len(events)+1,'stage':stage,'choice':choice,'data':data})
 add('binding',None,{});add('scalar_inputs',None,{})
 for n,mode in enumerate(['residual','variational']):
  add('choice_start',mode,{})
  for kind in ['P','O']:
   for stage in ['moments','polynomial','source_moments','residual_raw']:add(stage,mode,{'kind':kind,'s0':['1','1']})
  for i in range(1,91):add('ordered_word',mode,{'index':i})
  add('gate_inputs',mode,{'E':['10','10']});add('choice_complete',mode,{'row':rows[n]})
 add('complete',None,{});f=p/'events';f.write_text(''.join(json.dumps(x)+'\n'for x in events));out=p/'out';out.mkdir()
 old=worker.load_metadata
 try:
  worker.load_metadata=lambda b:{'rows':rows};worker.run({'files':{'events':str(f)}},out)
 finally:worker.load_metadata=old
 r=json.loads((out/'RESULT.json').read_text());ok(r['saved_events']==205 and r['modes']==2 and r['all_fixed_first_polynomials_excluded']is True)
 ok(json.loads((out/'PARTIAL.json').read_text())['source_sequence']==205)
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':checks,'accepted_values_read':False,'native_calls':0},indent=2))
