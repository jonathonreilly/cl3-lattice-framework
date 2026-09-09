import runpy,copy,json
from pathlib import Path
P=Path(__file__).resolve().parent;c=runpy.run_path(str(P/'common.py'));c['verify']();c['loaded_numpy']();checks=2
args=[c['read'](P/n) for n in ('PILOT_OUTER.json','PILOT_POST.json','PILOT_RESULT.json','PILOT_ACCEPTANCE.json')]+[(P/'PILOT_SHELL.stderr').read_text(),c['read'](P/'FORECAST.json')]
for idx,key,value in [(0,'seconds',float('nan')),(0,'seconds',31),(1,'seconds',171),(2,'rss_bytes',0),(3,'external_seconds',3),(5,'production_seconds_per_shard',float('inf')),(5,'aggregate_forecast_seconds',1)]:
 q=copy.deepcopy(args);q[idx][key]=value
 try:c['validate_cost'](*q)
 except ValueError:checks+=1
 else:raise ValueError('cost mutant survived')
for suffix in ('.pyc','.so','.dylib'):
 p=P/('UNDECLARED_CONTROL'+suffix)
 try:
  p.write_bytes(b'not executable')
  try:c['verify']()
  except ValueError as e:
   if 'membership' not in str(e):raise
   checks+=1
  else:raise ValueError('membership mutant survived')
 finally:p.unlink()
print(json.dumps({'status':'PASS','predicates':checks,'scope':'actual -I -B closure/NumPy imports, seven cost adversaries, three injected executable membership files; no core or gap imports'}))
