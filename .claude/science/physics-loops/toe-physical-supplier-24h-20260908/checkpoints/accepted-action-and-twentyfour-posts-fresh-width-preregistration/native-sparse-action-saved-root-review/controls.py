"""Fabricated schema metadata only. No checker arithmetic or physical inputs."""
import tempfile,json,types
from pathlib import Path
p=Path(__file__).resolve().parent;s=types.ModuleType('schema');exec(compile((p/'schema.py').read_bytes(),str(p/'schema.py'),'exec'),s.__dict__)
def write(p,x):p.write_text(json.dumps(x)+'\n')
with tempfile.TemporaryDirectory()as t:
 p=Path(t);out=p/'out';old=p/'old';out.mkdir();old.mkdir();auth={'binding_sha256':'b'};rf={'authorization':auth,'worker_freeze':'w','binding_path':str(p/'B.json')};write(p/'B.json',{'output':str(old),'inputs':{}});write(out/'STARTED.json',auth);rows=[]
 for oi in range(5):
  d=old/f'ORBIT_{oi}';d.mkdir();events=[]
  for stage in s.STAGES:
   for key in (range(4) if stage.startswith('coefficient') else(399,400)):
    e={'stage':stage,'orbit':oi,('pair' if stage.startswith('coefficient')else'impurity_bare_index'):key};j=len(events);events.append(e);write(out/f'ORBIT_{oi}_{j}_{stage}.json',{k:v for k,v in e.items()if k not in('stage','orbit')})
  (d/'EVENTS.ndjson').write_text('\n'.join(map(json.dumps,events))+'\n');rows.append({'orbit':oi,'original_pairs':4,'arithmetic_events':16,'leakage_pass':[False,False]})
 r={'status':'PASS_SAVED_FOUR_ACTION_ARITHMETIC','seconds':1,'native_calls':0,'events_checked':80,'orbits':rows};write(out/'RESULT.json',r);write(out/'PARTIAL.json',{'stage':'orbit_complete','rows':rows});w={'status':'COMPLETE_SAVED_ONLY','runtime_sha256':'w','binding_sha256':'b','result_sha256':s.sha(out/'RESULT.json'),'seconds':2,'rss_bytes':100};write(out/'WORKER_COMPLETE.json',w);s.check(out,rf,3);checks=1
 for name in ('count','native','optional','pairs','time','missing_stage'):
  rr=json.loads(json.dumps(r));ww=dict(w)
  if name=='count':rr['events_checked']=79
  if name=='native':rr['native_calls']=False
  if name=='optional':rr['orbits'][0]['leakage_pass'][0]=True
  if name=='pairs':rr['orbits'][0]['original_pairs']=12
  if name=='time':ww['seconds']=120
  if name=='missing_stage':(out/'ORBIT_0_0_coefficient.json').rename(out/'unexpected.json')
  write(out/'RESULT.json',rr);ww['result_sha256']=s.sha(out/'RESULT.json');write(out/'WORKER_COMPLETE.json',ww)
  try:s.check(out,rf,3)
  except (ValueError,FileNotFoundError):checks+=1
  else:raise AssertionError(name)
 print(json.dumps({'status':'PASS_FABRICATED_SCHEMA','checks':checks,'native_calls':0,'saved_arithmetic_calls':0}))
