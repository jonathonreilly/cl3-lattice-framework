from pathlib import Path
import json,hashlib,types,copy
B=Path(__file__).resolve().parent;R=B.parent/'native-minimal-first-action-append-root-review';X=B/'SYNTHETIC';X.mkdir(exist_ok=False);O=X/'OUT';O.mkdir();P=X/'native-minimal-first-action-append-design';P.mkdir();S=1<<192
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x)+'\n')
rf=json.loads((R/'ROOT_FREEZE.json').read_text());m=types.ModuleType('schema');m.__file__=str(R/'schema.py');exec(compile((R/'schema.py').read_bytes(),m.__file__,'exec'),m.__dict__)
# Independently written synthetic metadata and zero cross values. No core/worker/binder imported.
orbits=[[1,1,0],[1,0,0],[0,1,0],[0,0,2],[0,0,1]];lines=[]
for oi in range(5):
 for a in range(3):
  for node in range(66):
   for sig in (-1,1):
    lines.append(dict(orbit_id=oi,type='bare_to_pole',append_index=399+a,pole_id=node,sigma=sig,entries=[[6*node+(0 if sig==-1 else 3)+v,0,0,0,0] for v in range(3)]))
  lines.append(dict(orbit_id=oi,type='bare_to_insertion',append_index=399+a,entries=[[396+v,0,0,0,0] for v in range(3)]))
 for a in range(3):
  lines.append(dict(orbit_id=oi,type='bare_self',append_index=399+a,entries=[[399+b,(S//2 if a<2 else 3*S//2) if a==b else 0,(S//2 if a<2 else 3*S//2) if a==b else 0,0,0] for b in range(a,3)]))
stream=O/'FIRST_ACTION_APPEND.ndjson';stream.write_text(''.join(json.dumps(x)+'\n' for x in lines));assert len(lines)==2010 and sum(len(x['entries']) for x in lines)==6015
old={'orbits':[dict(orbit=o,raw_rows=399,closed_rows=798,closed_trace=[2*S,2*S],arithmetic_radius='0') for o in orbits]};mu={'interval':['2','2']};save(X/'OLD.json',old);save(X/'MU.json',mu);save(P/'BINDING.json',{'ward':{'result':str(X/'OLD.json')},'mu':{'result':str(X/'MU.json')}})
new=[dict(orbit=o,data_raw_rows=402,data_closed_rows=804,original_raw_rows=399,original_closed_rows=798,closed_trace=[7*S,7*S],arithmetic_radius='0') for o in orbits]
result=dict(status='COMPLETE_FIRST_ACTION_DATA_APPEND_MIDPOINT_ONLY',entries=6015,rows=2010,denominator=S,append_sha256=sha(stream),seconds=.1,maximum_width=0,append_closed_traces=[[5*S,5*S] for _ in orbits],append_arithmetic_radius=0,orbits=new,physical_input_metadata={'eta_mu':'0','mu_interval':['2','2']},generator_assembled=False,leakage_computed=False,propagation_computed=False)
partial=dict(stage='combined_gates',rows=2010,entries=6015,current={k:v for k,v in lines[-1].items() if k!='entries'},orbit_gates=new,mu_metadata=result['physical_input_metadata'])
worker=dict(status='COMPLETE_FIRST_ACTION_DATA_APPEND_ONLY',freeze_sha256=rf['worker_freeze'],binding_sha256=sha(P/'BINDING.json'),seconds=.2,rss_bytes=10000,generator_assembled=False,leakage_computed=False)
save(O/'STARTED.json',rf['authorization'])
def emit(r,p):
 save(O/'RESULT.json',r);save(O/'PARTIAL.json',p);w=dict(worker,result_sha256=sha(O/'RESULT.json'));save(O/'WORKER_COMPLETE.json',w)
emit(result,partial);m.check(O,rf,.3);passed=1;names=[]
def adverse(name,change):
 global passed
 r=copy.deepcopy(result);p=copy.deepcopy(partial);change(r,p);emit(r,p)
 try:m.check(O,rf,.3)
 except (ValueError,KeyError,TypeError):passed+=1;names.append(name)
 else:raise AssertionError('accepted adverse '+name)
adverse('floating census',lambda r,p:r.update(rows=2010.0))
adverse('trace mismatch',lambda r,p:r['orbits'][0].update(closed_trace=[8*S,8*S]))
adverse('radius underestimate',lambda r,p:r['orbits'][0].update(arithmetic_radius='-1'))
adverse('false domain',lambda r,p:r['orbits'][0].update(original_closed_rows=804))
adverse('scientific promotion',lambda r,p:r.update(leakage_computed=True))
adverse('partial count',lambda r,p:p.update(entries=6014))
adverse('NaN time',lambda r,p:r.update(seconds=float('nan')))
adverse('mu mismatch',lambda r,p:r.update(physical_input_metadata={'eta_mu':'0','mu_interval':['3','3']}))
original=stream.read_bytes();changed=copy.deepcopy(lines);changed[0]['orbit_id']=False;stream.write_text(''.join(json.dumps(x)+'\n' for x in changed));r=copy.deepcopy(result);r['append_sha256']=sha(stream);emit(r,partial)
try:m.check(O,rf,.3)
except (ValueError,KeyError,TypeError):passed+=1;names.append('rehashed bool orbit')
else:raise AssertionError('accepted bool orbit')
stream.write_bytes(original);emit(result,partial)
print(json.dumps(dict(status='PASS_SYNTHETIC_COMPLETE_SCHEMA',cases=passed,adverses=names,rows=2010,entries=6015,native_entry_calls=0,native_binder_calls=0,scope='fabricated schema fields only; not a native full-stream mock')))
