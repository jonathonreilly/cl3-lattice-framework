import json,time
from pathlib import Path
from fractions import Fraction as F
from highorder import run_case

def run(out):
 out=Path(out);out.mkdir();rows=[];stage='initial';start=time.monotonic()
 def save(name,obj):(out/name).write_text(json.dumps(obj,indent=2)+'\n')
 save('PARTIAL.json',{'stage':stage,'rows':rows})
 try:
  for s,target in [(F(1),F(1,10000)),(F(1),F(1,1000000)),(F(2),F(1,10000)),(F(2),F(1,1000000))]:
   stage=f'{s}:{target}';save('PARTIAL.json',{'stage':stage,'rows':rows});t=time.monotonic()
   row=run_case(s,target,lambda x:save('PARTIAL.json',{'stage':stage,'rows':rows,'progress':x}));row['seconds']=time.monotonic()-t;rows.append(row);save('PARTIAL.json',{'stage':stage,'rows':rows})
  save('RESULT.json',{'status':'COMPLETE_FIXED_CASES','rows':rows,'seconds':time.monotonic()-start,'all_targets_met':all(r['status']=='CERTIFIED_TARGET' for r in rows),'alpha_computed':False})
 except BaseException as e:save('FAILURE.json',{'stage':stage,'rows':rows,'error':repr(e)});raise
