from pathlib import Path
import tempfile,json,hashlib
p=Path('/private/tmp/toe-24h-probes-20260908/native-coordinate-free-root-review');n={};exec(compile((p/'schema.py').read_bytes(),str(p/'schema.py'),'exec'),n)
def save(p,x):p.write_text(json.dumps(x))
with tempfile.TemporaryDirectory()as tmp:
 d=Path(tmp);o=d/'out';o.mkdir();src=d/'selected';src.mkdir();rows=[]
 for i in range(5):
  od=o/f'ORBIT_{i}';od.mkdir();sd=src/f'ORBIT_{i}';sd.mkdir();save(sd/'SELECTED.json',[]);save(sd/'CANDIDATE.json',[[str(int(a==z))for z in range(48)]for a in range(48)])
  record={'orbit':i,'pairs':24,'candidate_bits':256,'indices':[],'T':[[int(a==z)*(1<<256)for z in range(48)]for a in range(48)]};ans={'status':'INDETERMINATE_CERTIFICATE','error':'synthetic','leakage_pass':False}
  save(od/'00000_selected_candidate.json',record);save(od/'00001_indeterminate.json',ans);save(od/'RESULT.json',ans);rows.append({'orbit':i,'status':ans['status'],'stage_files':2})
 r={'status':'COMPLETE_SAME_SPAN_LEAKAGE_ATTEMPT','orbits':rows,'seconds':1,'target_squared':'1/1000000000000','C_width_gate_required':False,'h':1,'new_scalar_recenter':False};save(o/'RESULT.json',r);save(o/'PARTIAL.json',{'stage':'complete','completed_orbits':rows})
 w={'status':'COMPLETE_GENERALIZED_LEAKAGE_ATTEMPT','runtime_sha256':'toy','result_sha256':n['sha'](o/'RESULT.json'),'seconds':2,'rss_bytes':100};save(o/'WORKER_COMPLETE.json',w)
 rf={'worker_freeze':'toy','selected_output':str(src)};n['check'](o,rf,3);count=1
 for mutation in ('flag','membership','candidate'):
  f=o/'ORBIT_4'/'RESULT.json';a=json.loads(f.read_text())
  if mutation=='flag':a['leakage_pass']=True;save(f,a)
  if mutation=='membership':save(o/'FAILURE.json',{})
  if mutation=='candidate':save(src/'ORBIT_4'/'SELECTED.json',[1])
  try:n['check'](o,rf,3)
  except ValueError:count+=1
  else:raise AssertionError(mutation)
  a['leakage_pass']=False;save(f,a)
  if (o/'FAILURE.json').exists():(o/'FAILURE.json').unlink()
 print(json.dumps({'synthetic_multiorbit_checks':count,'scientific_loads':0,'schema_only':True}))
