import json,time
from pathlib import Path
from fractions import Fraction as F
from core import oracle

def run(out):
 out.mkdir();start=time.monotonic();rows=[];stage='initial';baseline=json.loads((Path(__file__).parent/'RETURN_BASELINE.json').read_text())['rows']
 def save(n,x):(out/n).write_text(json.dumps(x,indent=2)+'\n')
 save('PARTIAL.json',{'stage':stage,'rows':rows})
 try:
  for s in (F(0),F(1,10**9),F(1,2),F(1),F(2)):
   stage=str(s);save('PARTIAL.json',{'stage':stage,'rows':rows});t=time.monotonic();row=oracle(s);row['seconds']=time.monotonic()-t;row['return_overlap']='PENDING';rows.append(row);save('PARTIAL.json',{'stage':stage,'rows':rows})
   if s in (F(1,2),F(1),F(2)):
    b=[r for r in baseline if r['s']==str(s) and r['target']=='1/1000000000000']
    if len(b)!=1:raise ValueError('baseline membership')
    for key in ('A','Aprime'):
     a0,a1=map(F,row[key]);b0,b1=map(F,b[0][key])
     if max(a0,b0)>min(a1,b1):raise ValueError('return-series disagreement '+key)
    row['return_overlap']='PASS'
   else:row['return_overlap']='not_applicable'
   save('PARTIAL.json',{'stage':stage,'rows':rows})
  save('RESULT.json',{'status':'COMPLETE_FIXED_CASES','rows':rows,'seconds':time.monotonic()-start,'all_targets_met':all(r['status']=='CERTIFIED_TARGET' for r in rows),'alpha_computed':False})
 except BaseException as e:save('FAILURE.json',{'stage':stage,'rows':rows,'error':repr(e)});raise
