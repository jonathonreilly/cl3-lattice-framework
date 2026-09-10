import sys,json,copy,importlib.util
from pathlib import Path
from fractions import Fraction as F
sys.dont_write_bytecode=True
S=Path('/private/tmp/toe-24h-probes-20260908');R=S/'native-gaussian-jet-root-review';P=S/'native-gaussian-high-moment-runtime-design';sys.path.insert(0,str(R));import independent as I,schema
for name in ['core','engine','adapter']:
 spec=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m)
# Native loader never imported or called. Nonzero rational-width source boxes.
M={str(j):['1',str(F(1)+F(j,1<<260))]for j in range(11)};M['0']=['1','1'];low={k:{str(j):I.point(1)for j in range(7)}for k in['P','O']};absolute={k:schema.grid(v)for k,v in M.items()};packet={'first_order':7,'grid_bits':256,'units':'dimensionless_h1','classes':{}};events=[]
def emit(stage,data):events.append(json.loads(json.dumps({'sequence':len(events)+1,'stage':stage,'data':data})))
for family in['degree20','omega79']:
 for role in['acceptance','worker','receipt','root_freeze','result']:emit('before_input',{'family':family,'role':role})
for family,role in[('degree20','events'),('omega79','reused')]:emit('before_input',{'family':family,'role':role})
emit('absolute_moment_source_map',{'rational':M,'old_even_indices':{'6':3,'8':4,'10':5}});emit('absolute_moment_grid',{'grid_bits':256,'moments':absolute})
for kind in['P','O']:
 D,B=sys.modules['adapter'].tables(json.loads(json.dumps(absolute)),kind);packet['classes'][kind]={'D':D,'B':B,'accepted_m':json.loads(json.dumps(low[kind]))};emit('native_table',{'kind':kind,**packet['classes'][kind]})
r=sys.modules['engine'].compute(packet,emit)
for row in r['rows']:
 widths={str(n):str(F(v[0][1]-v[0][0],I.Q))for n,v in row['moments'].items()};g=all(F(v)<=F(1,10**6)for v in widths.values());row.update(widths=widths,target_full_width='1/1000000',width_gate=g,status='CERTIFIED_PILOT_WIDTH'if g else'INDETERMINATE_PRECISION');emit('class_width_gate',row)
r.update(status='COMPLETE_NEW_HIGH_MOMENT_PILOT',scope='only m7..10; absolute width pilot, no downstream Ward sufficiency',seconds=1,events=len(events)+1);emit('complete',{'result':r});r=json.loads(json.dumps(r));assert schema.reconcile(packet,events,r,M,low)==2;checks=1
for tag in ['missing','coefficient','bool','width','scale']:
 e=copy.deepcopy(events);rr=copy.deepcopy(r)
 if tag=='missing':e.pop(20)
 elif tag=='coefficient':next(x for x in e if x['stage']=='operator_order')['data']['A'][0][2][1][0]+=1
 elif tag=='bool':rr['first_order']=True
 elif tag=='width':rr['rows'][0]['width_gate']=not rr['rows'][0]['width_gate']
 else:next(x for x in e if x['stage']=='absolute_moment_grid')['data']['grid_bits']=192
 try:schema.reconcile(packet,e,rr,M,low);raise AssertionError(tag+' accepted')
 except I.Invalid:checks+=1
print(json.dumps({'status':'PASS','full_two_class_fixture_and_adverses':checks,'events':len(events),'native_data':0,'producer_loader_calls':0}))
# Whole six-file output schema, with only source-file authentication substituted.
# The arithmetic remains the real independent verifier above.
import tempfile,hashlib
with tempfile.TemporaryDirectory()as temp:
 base=Path(temp);out=base/'out';out.mkdir();wp=base/'worker';wp.mkdir();(wp/'BINDING.json').write_text('{}');schema.P=wp;schema.source_packet=lambda _: (M,low);rf={'worker_freeze':'0'*64};auth={'runtime_sha256':'0'*64,'binding_sha256':schema.sha(wp/'BINDING.json'),'output':str(out.resolve()),'no_retry':True}
 def write(n,v):(out/n).write_text(json.dumps(v))
 write('STARTED.json',auth);write('TABLES.json',packet);write('RESULT.json',r);(out/'EVENTS.ndjson').write_text('\n'.join(json.dumps(x)for x in events)+'\n');write('PARTIAL.json',{'current':events[-1],'seconds':2});done={'status':'COMPLETE_NEW_HIGH_MOMENTS_ONLY','runtime_sha256':'0'*64,'binding_sha256':auth['binding_sha256'],'result_sha256':schema.sha(out/'RESULT.json'),'seconds':3,'rss_bytes':1000000};write('WORKER_COMPLETE.json',done);assert schema.check(out,rf,4)['count']==2;checks+=1
 for tag in ['false_rss','late_time','failure_file']:
  d=dict(done)
  if tag=='false_rss':d['rss_bytes']=False
  elif tag=='late_time':d['seconds']=5
  else:write('FAILURE.json',{})
  write('WORKER_COMPLETE.json',d)
  try:schema.check(out,rf,4);raise AssertionError(tag+' accepted')
  except I.Invalid:checks+=1
  if(out/'FAILURE.json').exists():(out/'FAILURE.json').unlink()
  write('WORKER_COMPLETE.json',done)
 # Add an output only after the initial census; final census must catch it.
 def inject(_):write('LATE_FAILURE.json',{})
 try:schema.check(out,rf,4,inject);raise AssertionError('late file accepted')
 except I.Invalid:checks+=1
print(json.dumps({'status':'PASS_FULL_SCHEMA','total_fixture_controls':checks,'source_file_authentication_stubbed_only_for_synthetic_fixture':True,'new_jet_arithmetic_stubbed':False,'native_values':0}))
