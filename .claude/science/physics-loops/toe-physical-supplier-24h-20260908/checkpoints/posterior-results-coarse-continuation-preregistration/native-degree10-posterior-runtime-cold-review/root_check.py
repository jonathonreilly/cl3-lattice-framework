from pathlib import Path
import types,json,hashlib
S=Path('/private/tmp/toe-24h-probes-20260908');E=S/'native-degree10-posterior-runtime-cold-review/root-fixture';E.mkdir(exist_ok=True);O=E/'output';O.mkdir(exist_ok=True);W=E/'worker';W.mkdir(exist_ok=True);R=S/'native-degree10-posterior-root-review'
m=types.ModuleType('schema');m.__file__=str(E/'schema.py');exec(compile((R/'schema.py').read_bytes(),str(R/'schema.py'),'exec'),m.__dict__)
p=types.ModuleType('posterior');exec(compile((S/'native-degree10-posterior-certificate-design/posterior.py').read_bytes(),'<posterior>','exec'),p.__dict__)
def write(path,v):path.write_text(json.dumps(v)+'\n')
ev=[]
def emit(stage,choice,data):ev.append({'sequence':len(ev)+1,'stage':stage,'choice':choice,'data':data})
emit('binding',None,{});emit('scalar_inputs',None,{});rows=[];original=[]
for mode in ['residual','variational']:
 emit('choice_start',mode,{'mode':mode});s={'s0':{},'q':{},'gate':None}
 for k in ['P','O']:
  for stage in ['moments','polynomial','source_moments','residual_raw']:
   d={'kind':k}
   if stage=='source_moments':d['s0']=['8','8'];s['s0'][k]=d['s0']
   if stage=='residual_raw':d['q']='0';s['q'][k]='0'
   emit(stage,mode,d)
 for i in range(1,91):emit('ordered_word',mode,{'index':i})
 g={'E':['0','0'],'F':['0','0'],'nominal':['2','2'],'rows':{'P':{'q':'0'},'O':{'q':'0'}}};s['gate']=g;emit('gate_inputs',mode,g);emit('choice_complete',mode,{})
 ans=p.evaluate(s['s0'],s['q'],g);ans['mode']=mode;ans=m.enc(ans);rows.append(ans);original.append({'mode':mode,'nominal':g['nominal']});write(O/(mode+'_INPUT.json'),s);write(O/(mode+'_ARITHMETIC.json'),ans);write(O/(mode+'_NORMS.json'),{k:ans[k]for k in ['a_squared_upper','b_squared_upper','a_upper','b_upper']})
emit('complete',None,{});assert len(ev)==205
src=E/'source_events';src.write_text(''.join(json.dumps(x)+'\n'for x in ev));orig=E/'source_result';write(orig,{'rows':original});write(W/'BINDING.json',{'files':{'events':{'path':str(src),'sha256':m.sha(src)},'result':{'path':str(orig),'sha256':m.sha(orig)}}})
auth={'synthetic':True};write(E/'WORKER_AUTHORIZATION.json',auth);write(O/'STARTED.json',auth);write(O/'RESULT.json',{'status':'COMPLETE_NEW_POSTERIOR_WARD_ESTIMATOR','choices':2,'source_events':205,'old_moments_recomputed':0,'new_error_estimator':True,'rows':rows,'seconds':1});write(O/'PARTIAL.json',{'current':{'stage':'complete','data':{}},'completed':2,'seconds':1.1});write(O/'WORKER_COMPLETE.json',{'status':'COMPLETE_NEW_POSTERIOR_ONLY','runtime_sha256':'fake','binding_sha256':m.sha(W/'BINDING.json'),'result_sha256':m.sha(O/'RESULT.json'),'seconds':2,'rss_bytes':1000000});rf={'worker_path':str(W),'worker_freeze':'fake'}
def check(t=3):return m.check(O,rf,t,lambda _:None)
check();n=1
for mode in ['time','failure','norm','copy']:
 path=O/'residual_NORMS.json';old=path.read_bytes();part=O/'PARTIAL.json';oldp=part.read_bytes()
 if mode=='failure':write(O/'FAILURE.json',{})
 if mode=='norm':v=json.loads(old);v['a_squared_upper']='16';write(path,v)
 if mode=='copy':v=json.loads(oldp);v['completed']=2.0;write(part,v)
 try:check(1 if mode=='time' else 3)
 except ValueError:n+=1
 else:raise AssertionError(mode)
 if mode=='failure':(O/'FAILURE.json').unlink()
 path.write_bytes(old);part.write_bytes(oldp)
print(json.dumps({'status':'PASS','checks':n,'synthetic_source_events':205,'actual_saved_values_loaded':0,'original_moments_computed':0}))

# Independent chronological and authenticated saved-input adversaries.
path=O/'residual_INPUT.json';old=path.read_bytes();v=json.loads(old);v['q']['P']='1';write(path,v)
try:check()
except ValueError:pass
else:raise AssertionError('altered selected input accepted')
path.write_bytes(old)
oldsrc=src.read_bytes();oldbinding=(W/'BINDING.json').read_bytes();lines=[json.loads(z)for z in oldsrc.splitlines()];lines[2]['choice']='variational';src.write_text(''.join(json.dumps(z)+'\n'for z in lines));binding=json.loads(oldbinding);binding['files']['events']['sha256']=m.sha(src);write(W/'BINDING.json',binding);done=json.loads((O/'WORKER_COMPLETE.json').read_text());olddone=(O/'WORKER_COMPLETE.json').read_bytes();done['binding_sha256']=m.sha(W/'BINDING.json');write(O/'WORKER_COMPLETE.json',done)
try:check()
except ValueError:pass
else:raise AssertionError('rehash wrong chronology accepted')
src.write_bytes(oldsrc);(W/'BINDING.json').write_bytes(oldbinding);(O/'WORKER_COMPLETE.json').write_bytes(olddone)
print('INDEPENDENT_EXTRA_ADVERSES_PASS=2')
