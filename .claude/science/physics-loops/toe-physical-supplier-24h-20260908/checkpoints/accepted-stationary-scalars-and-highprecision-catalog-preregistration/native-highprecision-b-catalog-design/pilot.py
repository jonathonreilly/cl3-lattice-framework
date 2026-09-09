import json,time,hashlib
from fractions import Fraction as F
from pathlib import Path
from elliptic import oracle

def run(out):
 out.mkdir();(out/'ORACLES').mkdir();rows=[];stage='initial';current=None;start=time.monotonic()
 def save(name,x):(out/name).write_text(json.dumps(x,indent=2)+'\n')
 def partial():save('PARTIAL.json',{'stage':stage,'completed_rows':len(rows),'current':current,'last_retained_row':rows[-1] if rows else None,'seconds':time.monotonic()-start})
 partial()
 try:
  geometry=json.loads((Path(__file__).parent/'CATALOG_GEOMETRY.json').read_text())
  for p in geometry['endpoints']:
   current=p;stage='oracle_'+str(p['id']);partial();t=time.monotonic();raw=oracle(F(p['s']));seconds=time.monotonic()-t
   raw['seconds']=seconds;raw['catalog_endpoint']=p
   name=f"ORACLES/{p['id']:04d}.json";save(name,raw)
   row={'id':p['id'],'path':name,'sha256':hashlib.sha256((out/name).read_bytes()).hexdigest(),'seconds':seconds,'gate':'PENDING'}
   rows.append(row);stage='gate_'+str(p['id']);partial()
   if raw['s']!=p['s'] or max(map(F,raw['widths']))>F(1,10**30):raise ValueError('oracle identity/precision')
   row['gate']='PASS';partial()
  if len(rows)!=3484 or any(r['gate']!='PASS' for r in rows):raise ValueError('complete census')
  stage='complete';partial()
  save('RESULT.json',{'status':'COMPLETE_FIXED_3484_CATALOG','rows':rows,'seconds':time.monotonic()-start,'oracle_count':len(rows),'B_computed':False,'matrix_computed':False,'alpha_computed':False,'A66_results_bound':False})
 except BaseException as e:save('FAILURE.json',{'stage':stage,'current':current,'rows':rows,'error':repr(e)});raise
