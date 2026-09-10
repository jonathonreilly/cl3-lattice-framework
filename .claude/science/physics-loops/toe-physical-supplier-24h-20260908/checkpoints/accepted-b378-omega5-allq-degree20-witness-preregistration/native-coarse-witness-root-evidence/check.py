from pathlib import Path
import types,json,hashlib
S=Path('/private/tmp/toe-24h-probes-20260908');E=S/'native-coarse-witness-root-evidence';O=E/'fixture';O.mkdir(exist_ok=True);W=E/'worker';W.mkdir(exist_ok=True);R=S/'native-coarse-witness-root-review';m=types.ModuleType('schema');m.__file__=str(R/'schema.py');exec(compile((R/'schema.py').read_bytes(),m.__file__,'exec'),m.__dict__)
def write(p,x):p.write_text(json.dumps(x)+'\n')
def mat(n,k):return [[['0','0']for _ in range(k)]for _ in range(n)]
write(W/'BINDING.json',{'files':{'T_'+str(i):{'sha256':str(i)}for i in range(5)}});ev=[]
def event(stage,case,data):ev.append({'current':{'stage':stage,'case':case},'data':data})
for i in range(5):event('mapped_T',0,{'orbit':i,'source_sha256':str(i),'mapped':mat(48,48),'operator_squared_upper':'1'})
rows=[]
for c in range(10):
 event('factorization',c,{'local':mat(7,48),'projector_columns':mat(48,7)})
 for p in range(18):event('witness_panel',c,{'completed':21*(p+1),'direct':mat(7,7),'mixed':mat(7,7)})
 b=mat(7,7)
 if c==0:b[0][0]=['1/10','1/10']
 event('witness_block',c,{'block':b});r={'orbit':c//2,'impurity':c%2+1,'squared_block_lower':'1/100'if c==0 else'0','excludes_tau_1e9':c==0,'status':'EXCLUDED_BY_COARSE_WITNESS'if c==0 else'INDETERMINATE_COARSE_WITNESS','stored_operator':'minus_i_times_positive_projector_difference','metric_and_tail_charged':True};rows.append(r);write(O/f'CASE_{c:02d}.json',r)
(O/'BLOCKS.jsonl').write_text(''.join(json.dumps(x)+'\n'for x in ev));write(O/'RESULT.json',{'status':'COMPLETE_FIXED_COARSE_WITNESS','rows':rows,'seconds':1,'cases':10,'native_Gaussian_solve':False,'fine_consumer_certified':False});write(O/'PARTIAL.json',{'current':{'stage':'complete','case':10},'completed':10});write(O/'WORKER_COMPLETE.json',{'status':'COMPLETE','freeze_sha256':'fake','result_sha256':m.sha(O/'RESULT.json'),'seconds':2,'rss_bytes':1000000});rf={'worker_path':str(W),'worker_freeze':'fake'}
def check(t=3):return m.check(O,rf,t,lambda _:None)
check();n=1
for kind in ['time','extra','missing','bool']:
 p=O/'BLOCKS.jsonl';old=p.read_bytes();case=O/'CASE_00.json';oldcase=case.read_bytes()
 if kind=='extra':write(O/'FAILURE.json',{})
 if kind=='missing':p.write_text(''.join(json.dumps(x)+'\n'for x in ev[:-1]))
 if kind=='bool':x=json.loads(oldcase);x['orbit']=False;write(case,x)
 try:check(1 if kind=='time'else 3)
 except ValueError:n+=1
 else:raise AssertionError(kind)
 if kind=='extra':(O/'FAILURE.json').unlink()
 p.write_bytes(old);case.write_bytes(oldcase)
print(json.dumps({'status':'PASS','checks':n,'fixture_cases':10,'events':205,'native_inputs':0,'scope':'fabricated shape/gate schema; no adapter or producer calls'}))
