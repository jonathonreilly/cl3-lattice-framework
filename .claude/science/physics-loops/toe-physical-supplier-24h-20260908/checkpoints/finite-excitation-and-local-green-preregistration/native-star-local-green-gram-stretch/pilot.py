import json,time
from fractions import Fraction as F
from core import integrate

def run(out):
 out.mkdir();start=time.monotonic();rows=[];stage='initial'
 def save(name,data):(out/name).write_text(json.dumps(data,indent=2)+'\n')
 save('PARTIAL.json',{'stage':stage,'rows':rows})
 try:
  for s,kind,cap in [(F(1),'A',1024),(F(1),'B',4096),(F(2),'A',1024),(F(2),'B',4096)]:
   stage=f'{s}-{kind}';save('PARTIAL.json',{'stage':stage,'rows':rows})
   def progress(state):save('PARTIAL.json',{'stage':stage,'rows':rows,'current':state})
   t0=time.monotonic();row=integrate(s,kind,cap,progress=progress);row['seconds']=time.monotonic()-t0;rows.append(row);save('PARTIAL.json',{'stage':stage,'rows':rows})
  save('RESULT.json',{'status':'COMPLETE_FIXED_COST_AND_ENCLOSURES','rows':rows,'seconds':time.monotonic()-start,'all_width_targets_met':all(r['status']=='CERTIFIED_TARGET' for r in rows),'gram_matrix_computed':False,'alpha_computed':False})
 except BaseException as e:save('FAILURE.json',{'stage':stage,'rows':rows,'error':repr(e),'seconds':time.monotonic()-start});raise
