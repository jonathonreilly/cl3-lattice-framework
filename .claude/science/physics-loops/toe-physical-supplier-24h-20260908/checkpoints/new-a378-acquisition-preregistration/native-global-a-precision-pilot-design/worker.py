"""Unlaunched fixed new precision pilot. Importing does not call an oracle."""
from fractions import Fraction as F
from pathlib import Path
import json,time
POINTS=('3/17179869184','5/33554432','7/65536','11/257','17/19','31/2')
def save(p,x):
 p.write_text(json.dumps(x,indent=2)+'\n')
def run(out,oracle,target):
 if not isinstance(target,F) or target<=0:raise ValueError('positive exact target')
 out=Path(out);out.mkdir(exist_ok=False);start=time.monotonic();rows=[];current=None
 try:
  for i,s in enumerate(POINTS):
   current={'index':i,'s':s,'stage':'before_oracle'};save(out/'PARTIAL.json',{'current':current,'completed':len(rows)})
   t=time.monotonic();raw=oracle(F(s));row={'index':i,'s':s,'seconds':time.monotonic()-t,'raw':raw}
   save(out/f'RAW_{i}.json',row)
   aa=list(map(F,raw['A']));dd=list(map(F,raw['Aprime']))
   if not(len(aa)==len(dd)==2 and aa[0]<=aa[1] and dd[0]<=dd[1]):raise ValueError('ordered pair')
   row['target_met']=max(aa[1]-aa[0],dd[1]-dd[0])<=target
   rows.append(row);save(out/'PARTIAL.json',{'current':{'index':i,'s':s,'stage':'retained'},'completed':len(rows),'target_met':row['target_met']})
  save(out/'RESULT.json',{'status':'COMPLETE','scope':'new fixed precision cost pilot only','rows':rows,'target':str(target),'all_targets_met':all(x['target_met'] for x in rows),'seconds':time.monotonic()-start})
 except BaseException as error:
  try:save(out/'FAILURE.json',{'current':current,'completed':len(rows),'error':repr(error),'seconds':time.monotonic()-start})
  except BaseException as retention:error.add_note('retention failed: '+repr(retention))
  raise
