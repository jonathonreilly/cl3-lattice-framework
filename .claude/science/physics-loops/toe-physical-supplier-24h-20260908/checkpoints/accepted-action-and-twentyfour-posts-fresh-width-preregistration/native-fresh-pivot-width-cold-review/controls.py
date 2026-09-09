import types,pathlib,tempfile,json,hashlib
P=pathlib.Path('/private/tmp/toe-24h-probes-20260908');m=types.ModuleType('candidate');m.__file__=str(P/'native-fresh-pivot-width-diagnostic/check.py');exec(compile(pathlib.Path(m.__file__).read_bytes(),m.__file__,'exec'),m.__dict__)
n=0
for a in (1,2,3,7):
 for b in (a,a+1,a+4):
  for half in (False,True):
   r=m.scalar(a*a*m.S,b*b*m.S,half);f=2 if half else 1
   assert r['forced_lower']==m.S//(f*b);assert r['forced_upper']==-((-m.S)//(f*a));n+=2
for i in range(0,396,2):assert m.support(i)==m.support(i+1);n+=1
s=types.ModuleType('schema');exec((P/'native-fresh-pivot-width-root-review/schema.py').read_bytes(),s.__dict__)
with tempfile.TemporaryDirectory() as td:
 p=pathlib.Path(td);row={'orbit':0,'row':0,'must_fail_width':False,'divisor_failure':False};r={'status':'COMPLETE_SAVED_SCALAR_DIAGNOSTIC','rows':[row],'forced_blockers':[]};(p/'RESULT.json').write_text(json.dumps(r));(p/'ROWS.json').write_text(json.dumps([row]));w={'runtime_sha256':'x','binding_sha256':'y','result_sha256':hashlib.sha256((p/'RESULT.json').read_bytes()).hexdigest(),'status':'COMPLETE_SAVED_ONLY','rss_bytes':100,'seconds':1};(p/'WORKER_COMPLETE.json').write_text(json.dumps(w));rf={'worker_freeze':'x','authorization':{'binding_sha256':'y'}}
 s.check(p,rf,2);(p/'FAILURE.json').write_text('{}');(p/'PARTIAL.json').write_text('{"stage":"pins"}');s.check(p,rf,2)
print(json.dumps({'exact_scalar_support_predicates':n,'bad_failure_stale_partial_accepted':True,'actual_saved_calls':0}))
