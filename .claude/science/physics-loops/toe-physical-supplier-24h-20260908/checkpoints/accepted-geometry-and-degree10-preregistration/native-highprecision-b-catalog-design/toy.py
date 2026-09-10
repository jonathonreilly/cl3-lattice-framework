"""Synthetic bad-width retention test. Never imports the real oracle."""
from pathlib import Path
import tempfile,types,sys,json,hashlib
P=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='stationary-catalog-toy-') as td:
 p=Path(td);(p/'CATALOG_GEOMETRY.json').write_text(json.dumps({'endpoints':[{'id':0,'s':'1'},{'id':1,'s':'2'}]}))
 fake=types.ModuleType('elliptic')
 fake.oracle=lambda s:{'s':str(s),'A':['0','0'],'Aprime':['0','0'],'widths':['0','0'] if s==1 else ['1','0']}
 old=sys.modules.get('elliptic');sys.modules['elliptic']=fake
 m=types.ModuleType('tested');m.__file__=str(p/'pilot.py');exec(compile((P/'pilot.py').read_bytes(),str(P/'pilot.py'),'exec'),m.__dict__)
 try:m.run(p/'output');raise RuntimeError('bad width accepted')
 except ValueError as e:
  if 'precision' not in str(e):raise
 f=json.loads((p/'output/FAILURE.json').read_text());part=json.loads((p/'output/PARTIAL.json').read_text());n=0
 checks=[len(f['rows'])==2,f['stage']=='gate_1',f['current']['id']==1,f['rows'][0]['gate']=='PASS',f['rows'][1]['gate']=='PENDING',part['completed_rows']==2,part['last_retained_row']['id']==1,not(p/'output/RESULT.json').exists()]
 for r in f['rows']:
  checks.append(hashlib.sha256((p/'output'/r['path']).read_bytes()).hexdigest()==r['sha256'])
 for x in checks:
  if not x:raise RuntimeError('retention check')
  n+=1
 if old is None:del sys.modules['elliptic']
 else:sys.modules['elliptic']=old
 print(json.dumps({'status':'PASS','predicates':n,'physical_oracle_calls':0,'scope':'actual pilot control flow with two synthetic rows and forced second width failure'}))
