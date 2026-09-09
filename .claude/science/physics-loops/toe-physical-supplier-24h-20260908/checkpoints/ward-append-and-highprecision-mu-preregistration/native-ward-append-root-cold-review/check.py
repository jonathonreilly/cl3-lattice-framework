from pathlib import Path
import json,hashlib,types,sys,tempfile
base=Path('/private/tmp/toe-24h-probes-20260908');root=base/'native-ward-append-root-review';runtime=base/'native-ward-insertion-append-runtime';here=Path(__file__).parent
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,path):
 m=types.ModuleType(name);sys.modules[name]=m;exec(compile(path.read_bytes(),str(path),'exec'),m.__dict__);return m
schema=load('schema',root/'schema.py');iv=load('interval',runtime/'interval.py')
# Stub ONLY stream/binder. No native original entry formula or actual inputs called.
core=types.ModuleType('append_core');core.ORBITS=schema.ORBITS
last=[None]
def stream(poles,values,alpha,a0,c,emit,before):
 for meta,indices in schema.expected():
  before(meta);emit(dict(meta,entries=[[i,0,0,0,0] for i in indices]));last[0]=meta
 return {'entries':5970,'rows':1995,'maximum_width':0,'append_closed_traces':[[0,0]]*5,'denominator':iv.S,'append_arithmetic_radius':0,'radius_denominator':iv.S}
core.stream=stream;sys.modules['append_core']=core
binder=types.ModuleType('binder');binder.sha=h
old={'orbits':[{'orbit':list(o),'closed_trace':[10*iv.S,10*iv.S],'arithmetic_radius':'0','denominator':iv.S} for o in schema.ORBITS]}
binder.load=lambda plan:(None,None,None,None,None,old);sys.modules['binder']=binder
worker=load('stubbed_worker',runtime/'worker.py');cases=0
with tempfile.TemporaryDirectory(dir=here) as td:
 p=Path(td);out=p/'OUTPUT';out.mkdir();pd=p/'native-ward-insertion-append-runtime';pd.mkdir();oldpath=p/'OLD.json';oldpath.write_text(json.dumps(old));planpath=pd/'BINDING.json';planpath.write_text(json.dumps({'roles':{'common_cache':{'result':str(oldpath)}}}))
 worker.run({},out)
 w={'status':'COMPLETE_APPEND_MIDPOINT_ONLY','freeze_sha256':'toy','result_sha256':h(out/'RESULT.json'),'binding_sha256':h(planpath),'seconds':1,'rss_bytes':100}
 (out/'WORKER_COMPLETE.json').write_text(json.dumps(w));schema.check(out,'toy',2);cases+=1
 original=(out/'RESULT.json').read_text();partial=(out/'PARTIAL.json').read_text()
 for field,bad in [('entries',5969),('rows',1994),('maximum_width',1),('append_arithmetic_radius',1),('pure_state_computed',True),('seconds',True)]:
  r=json.loads(original);r[field]=bad;(out/'RESULT.json').write_text(json.dumps(r));w['result_sha256']=h(out/'RESULT.json');(out/'WORKER_COMPLETE.json').write_text(json.dumps(w))
  try:schema.check(out,'toy',2)
  except (ValueError,TypeError):cases+=1
  else:raise ValueError(field)
 (out/'RESULT.json').write_text(original);w['result_sha256']=h(out/'RESULT.json');(out/'WORKER_COMPLETE.json').write_text(json.dumps(w))
 badp=json.loads(partial);badp['stage']='complete';(out/'PARTIAL.json').write_text(json.dumps(badp))
 try:schema.check(out,'toy',2)
 except ValueError:cases+=1
 else:raise ValueError('partial stage')
rf=json.loads((root/'ROOT_FREEZE.json').read_text())
for p,v in rf['files'].items():
 if h(root/p)!=v:raise ValueError('root pin')
if rf['worker_freeze']!=h(runtime/'RUNTIME_FREEZE.json'):raise ValueError('workerpin')
print(json.dumps({'status':'PASS_STUB_SCHEMA','cases':cases,'fabricated_rows':1995,'actual_worker_with_stub_stream':True,'native_formula_calls':0,'actual_input_loads':0},indent=2))
