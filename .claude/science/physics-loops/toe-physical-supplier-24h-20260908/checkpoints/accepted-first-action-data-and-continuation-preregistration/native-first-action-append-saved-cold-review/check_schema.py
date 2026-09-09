from pathlib import Path
import types,json,hashlib,copy
D=Path(__file__).resolve().parent;R=D.parent/'native-first-action-append-saved-root-review';O=D/'SYNTHETIC';O.mkdir(exist_ok=False);rf=json.loads((R/'ROOT_FREEZE.json').read_text());m=types.ModuleType('schema');exec(compile((R/'schema.py').read_bytes(),str(R/'schema.py'),'exec'),m.__dict__)
v=dict(status='PASS_ALL_SAVED_APPEND_ENTRIES',checks=10,entries=6015,rows=2010,scope='exact midpoint arithmetic; physical scalar error ledger separate',oracle_calls=0,append_calls=0,seconds=.1);p=dict(error=None,stage='row_arithmetic',row=2009,entries=6014);w=dict(status='COMPLETE_SAVED_ONLY',runtime_sha256=rf['worker_freeze'],binding_sha256=rf['authorization']['binding_sha256'],seconds=.2,rss_bytes=10000)
def emit(v,p):
 (O/'RESULT.json').write_text(json.dumps(v));(O/'PARTIAL.json').write_text(json.dumps(p));(O/'WORKER_COMPLETE.json').write_text(json.dumps(dict(w,result_sha256=hashlib.sha256((O/'RESULT.json').read_bytes()).hexdigest())))
emit(v,p);m.check(O,rf,.3);n=1
for key,value,target in [('row',2010,'p'),('entries',6015,'p'),('checks',True,'v'),('seconds',float('nan'),'v'),('oracle_calls',1,'v'),('entries',6015.0,'v')]:
 vv=copy.deepcopy(v);pp=copy.deepcopy(p);(vv if target=='v' else pp)[key]=value;emit(vv,pp)
 try:m.check(O,rf,.3)
 except ValueError:n+=1
 else:raise AssertionError(key)
emit(v,p);print(json.dumps(dict(status='PASS_TINY_SAVED_SCHEMA',cases=n,native_calls=0,saved_arithmetic_calls=0)))
