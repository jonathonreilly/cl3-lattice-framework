import json,time
from fractions import Fraction as F
from pathlib import Path
from elliptic import oracle

def run(out):
 out.mkdir();rows=[];stage='initial';start=time.monotonic()
 def save(name,x):(out/name).write_text(json.dumps(x,indent=2)+'\n')
 save('PARTIAL.json',{'stage':stage,'rows':rows})
 try:
  for p in json.loads((Path(__file__).parent/'POLES.json').read_text())['rows']:
   stage='oracle_'+str(p['id']);t=time.monotonic();raw=oracle(F(p['s_midpoint']))
   row={'id':p['id'],'pole':p,'oracle':raw,'seconds':time.monotonic()-t,'gate':'PENDING'};rows.append(row)
   save('PARTIAL.json',{'stage':stage,'rows':rows})
   if max(map(F,raw['widths']))>F(1,10**30):raise ValueError('oracle input precision')
   for name,inf in [('A','A_midpoint_inflation'),('Aprime','Aprime_midpoint_inflation')]:
    e=F(p[inf]);l,u=map(F,raw[name]);row[name+'_whole_bracket']=[str(l-e),str(u+e)]
   row['gate']='PASS';save('PARTIAL.json',{'stage':stage,'rows':rows})
  save('RESULT.json',{'status':'COMPLETE_FIXED_66_ORACLES','rows':rows,'seconds':time.monotonic()-start,'B_computed':False,'matrix_computed':False,'alpha_computed':False})
 except BaseException as e:save('FAILURE.json',{'stage':stage,'rows':rows,'error':repr(e)});raise
