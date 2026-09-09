from pathlib import Path
import types,sys,json,tempfile,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/native-coordinate-free-native-runtime-design')
sha=lambda x:hashlib.sha256(Path(x).read_bytes()).hexdigest()
a=types.ModuleType('adapter');a.seeds=lambda ids:None;sys.modules['adapter']=a
b=types.ModuleType('binder');exec(compile((p/'binder.py').read_bytes(),str(p/'binder.py'),'exec'),b.__dict__);sys.modules['binder']=b
d=types.ModuleType('data_binder');d.sha=sha;sys.modules['data_binder']=d
m=types.ModuleType('selected_binder');exec(compile((p/'selected_binder.py').read_bytes(),str(p/'selected_binder.py'),'exec'),m.__dict__)
with tempfile.TemporaryDirectory()as td:
 q=Path(td);plan={'result':str(q/'RESULT.json'),'inputs':{}};root={'orbits':[]}
 for i in range(5):
  o=q/f'ORBIT_{i}';o.mkdir();(o/'SELECTED.json').write_text(json.dumps(list(range(24))));(o/'CANDIDATE.json').write_text(json.dumps([['1'if j==k else'0'for k in range(48)]for j in range(48)]))
  row=dict(orbit=i,status='CERTIFIED_ENCLOSURE')
  for n,k in [('SELECTED.json','selected_sha256'),('CANDIDATE.json','candidate_sha256')]:plan['inputs'][str(o/n)]=sha(o/n);row[k]=sha(o/n)
  root['orbits'].append(row)
 records=m.extract_bound_records(plan,root)
 assert all(r['T'][0][0]==2**256 and type(r['T'][0][0])is int for r in records)
 file=q/'ORBIT_0/CANDIDATE.json';x=json.loads(file.read_text());x[0][0]='1/3';file.write_text(json.dumps(x));plan['inputs'][str(file)]=sha(file);root['orbits'][0]['candidate_sha256']=sha(file)
 try:m.extract_bound_records(plan,root)
 except ValueError as e:assert 'exact256' in str(e)
 else:raise AssertionError('nondyadic accepted')
print(json.dumps({'status':'PASS','cases':2,'scope':'five synthetic rational identity T records and nondyadic rejection; seed validity stubbed; no native inputs'}))
