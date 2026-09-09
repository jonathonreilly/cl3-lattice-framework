import json,math,hashlib
from pathlib import Path
from fractions import Fraction as F
from retention import validate
def req(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(O,rf,elapsed):
 O=Path(O);r=json.loads((O/'RESULT.json').read_text());w=json.loads((O/'WORKER_COMPLETE.json').read_text());p=json.loads((O/'PARTIAL.json').read_text())
 req({x.name for x in O.iterdir()}=={'RESULT.json','WORKER_COMPLETE.json','PARTIAL.json'}|{f'ORBIT_{i}'for i in range(5)},'output membership')
 req(w['status']=='COMPLETE_GENERALIZED_LEAKAGE_ATTEMPT' and w['runtime_sha256']==rf['worker_freeze'] and w['result_sha256']==sha(O/'RESULT.json'),'worker binding')
 for x in(w['seconds'],r['seconds'],elapsed):req(type(x)in(int,float)and math.isfinite(x)and 0<x<180,'time')
 req(r['seconds']<=w['seconds']<=elapsed and w['seconds']<179 and type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'resources')
 req(r['status']=='COMPLETE_SAME_SPAN_LEAKAGE_ATTEMPT' and len(r['orbits'])==5 and r['target_squared']=='1/1000000000000' and r['C_width_gate_required']is False and type(r['h'])is int and r['h']==1 and r['new_scalar_recenter']is False,'scope')
 req(p=={'stage':'complete','completed_orbits':r['orbits']},'final partial')
 for oi,row in enumerate(r['orbits']):
  req(type(row['orbit'])is int and row['orbit']==oi and type(row['stage_files'])is int and 0<row['stage_files']<=4096,'orbit')
  d=O/f'ORBIT_{oi}';files=sorted(x for x in d.iterdir()if x.name!='RESULT.json');req(len(files)==row['stage_files'],'event count');events=[]
  for j,f in enumerate(files):
   req(f.is_file()and f.name.startswith(f'{j:05d}_')and f.suffix=='.json','serial')
   events.append((f.name.split('_',1)[1][:-5],json.loads(f.read_text())))
  ans=json.loads((d/'RESULT.json').read_text());req(ans['status']==row['status'],'orbit status')
  req(events[0][0]=='selected_candidate','first candidate')
  source=Path(rf['selected_output'])/f'ORBIT_{oi}'
  ids=json.loads((source/'SELECTED.json').read_text());T=json.loads((source/'CANDIDATE.json').read_text())
  converted=[]
  req(len(T)==48 and all(len(row)==48 for row in T),'candidate48')
  for rowT in T:
   rr=[]
   for x in rowT:
    req(type(x)is str,'rational candidate string');q=F(x)*(1<<256)
    req(q.denominator==1 and abs(q.numerator).bit_length()<=4096,'exact256 candidate');rr.append(q.numerator)
   converted.append(rr)
  T=converted
  req(events[0][1]=={'orbit':oi,'pairs':24,'candidate_bits':256,'indices':ids,'T':T},'bound candidate')
  validate(events,ans,oi,req)
  if ans['status']=='INDETERMINATE_CERTIFICATE':req(events[-1]==('indeterminate',ans)and ans['leakage_pass']is False and type(ans['error'])is str,'retained indeterminate');continue
  req(ans['status']=='COMPLETE_SOURCE_ONLY_ALGEBRA'and len(ans['results'])==2,'two impurities')
  for imp,v in zip((399,400),ans['results']):
   if v['status']=='INDETERMINATE_FRAME':req(F(v['e'])>=1 and ('frame_residual',{'impurity':imp,'data':{'e':v['e']}})in events,'frame event');continue
   req(v['status']=='CERTIFIED_GENERALIZED_LEAKAGE_BOUND' and ('result',{'impurity':imp,'data':v})in events,'verdict event')
   lo,hi=F(v['delta_squared_lower']),F(v['delta_squared_upper']);target=F(1,10**12)
   req(0<=lo<=hi and F(v['target_squared'])==target and type(v['leakage_pass'])is bool and v['leakage_pass']==(hi<=target)and type(v['target_excluded'])is bool and v['target_excluded']==(lo>target),'target')
 return {'status':'PASS_GENERALIZED_OUTPUT_SCHEMA','orbits':5,'arithmetic_replay':False}
