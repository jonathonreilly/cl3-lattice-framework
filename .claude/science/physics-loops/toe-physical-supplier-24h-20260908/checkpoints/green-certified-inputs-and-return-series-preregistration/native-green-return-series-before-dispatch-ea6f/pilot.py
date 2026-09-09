import json,time
from fractions import Fraction as F
from core import evaluate

def run(out):
 out.mkdir();rows=[];stage='initial';start=time.monotonic()
 def save(n,x):(out/n).write_text(json.dumps(x,indent=2)+'\n')
 save('PARTIAL.json',{'stage':stage,'rows':rows})
 try:
  for s in (F(1),F(2),F(1,2)):
   for target in (F(1,10**6),F(1,10**12)):
    stage=f'{s}:{target}';save('PARTIAL.json',{'stage':stage,'rows':rows});t=time.monotonic()
    row=evaluate(s,target,lambda x:save('PARTIAL.json',{'stage':stage,'rows':rows,'progress':x}));row['seconds']=time.monotonic()-t;rows.append(row);save('PARTIAL.json',{'stage':stage,'rows':rows})
  save('RESULT.json',{'status':'COMPLETE_FIXED_CASES','rows':rows,'seconds':time.monotonic()-start,'physical_Gram_computed':False,'alpha_computed':False})
 except BaseException as e:save('FAILURE.json',{'stage':stage,'rows':rows,'error':repr(e)});raise
