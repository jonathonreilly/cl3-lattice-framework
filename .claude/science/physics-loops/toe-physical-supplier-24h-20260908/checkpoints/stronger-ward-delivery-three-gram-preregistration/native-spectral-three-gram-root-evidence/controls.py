from pathlib import Path
import sys,json,hashlib,copy,tempfile,importlib.util
B=Path('/private/tmp/toe-24h-probes-20260908');W=B/'native-spectral-three-gram-saved-design';R=B/'native-spectral-three-gram-root-review'
def load(name,p):
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
I=load('interval',W/'interval.py');g=load('gram',W/'gram.py');s=load('test_schema',R/'schema.py')
checks=[]
def write(p,o):p.write_text(json.dumps(o)+'\n')
def run():
 with tempfile.TemporaryDirectory(prefix='three-gram-SYNTHETIC-')as td:
  T=Path(td);O=T/'output';O.mkdir();worker=T/'worker';worker.mkdir();events=[];old=[];rows=[];sr=[]
  def emit(stage,data,mode=None):events.append({'sequence':len(events)+1,'choice':mode,'stage':stage,'data':I.encode(data)})
  old.append({'stage':'scalar_inputs','choice':None,'data':{'c':['1/2','1/2']}})
  for mode in s.MODES:
   coef={'P':{'p0':'1','p1':'0','q':'0'},'O':{'p0':'1','p1':'0','q':'0'}};nom=['1','1'] if mode=='residual'else['0','0'];gate={'nominal':nom}
   old.append({'stage':'gate_inputs','choice':mode,'data':gate})
   for k in ['P','O']:
    old.append({'stage':'polynomial','choice':mode,'data':{'kind':k,'p0':'1','p1':'0'}});old.append({'stage':'residual_raw','choice':mode,'data':{'kind':k,'q':'0'}})
   sr.append({'mode':mode,'nominal':nom,'E_upper':'0'if mode=='residual'else'1','F_upper':'0','alpha_interval':['-1000','1000']})
  while len(old)<205:old.append({'stage':'SYNTHETIC_PLACEHOLDER','choice':None,'data':{}})
  oldpath=T/'original-events';oldpath.write_text(''.join(json.dumps(x)+'\n'for x in old));sp=T/'spectral.json';write(sp,{'rows':sr});desc=lambda p:{'path':str(p),'sha256':s.sha(p)};write(worker/'BINDING.json',{'degree10':{'events':desc(oldpath)},'spectral':{'result':desc(sp)}})
  for k in ['acceptance','receipt','root_freeze','worker','result','binding','acceptance','worker','receipt','root_freeze','result']:emit('before_input',{'role':k})
  for i in range(1,206):emit('before_source_event',{'index':i})
  for mode,x in zip(s.MODES,sr):
   inp={'c':['1/2','1/2'],'coefficients':coef,'nominal':x['nominal'],'E_upper':x['E_upper'],'F_upper':x['F_upper'],'spectral_alpha_interval':x['alpha_interval']};write(O/(mode+'_INPUT.json'),inp);emit('new_inputs',inp,mode);ans=g.evaluate(inp,lambda a,b:emit(a,b,mode));ans['mode']=mode;ans=I.encode(ans);rows.append(ans);write(O/(mode+'.json'),ans);emit('choice_complete',ans,mode)
  emit('complete',{});(O/'EVENTS.ndjson').write_text(''.join(json.dumps(x)+'\n'for x in events));write(O/'PARTIAL.json',{'current':events[-1],'completed':2})
  result={'status':'COMPLETE_NEW_SAVED_THREE_GRAM_ESTIMATOR','rows':rows,'choices':2,'max_ordered_pairs':450,'max_kernel_values':1350,'native_oracle_calls':0,'old_moments_recomputed':0,'old_nominal_recomputed':0,'seconds':1,'events':len(events)};write(O/'RESULT.json',result);rf={'worker_freeze':'synthetic','worker_path':str(worker)}
  wr={'status':'COMPLETE_NEW_SAVED_THREE_GRAM_ONLY','seconds':2,'rss_bytes':1000,'runtime_sha256':'synthetic','binding_sha256':s.sha(worker/'BINDING.json'),'result_sha256':s.sha(O/'RESULT.json')};write(O/'WORKER_COMPLETE.json',wr);write(O/'STARTED.json',{'runtime_sha256':'synthetic','binding_sha256':wr['binding_sha256'],'output':str(O.resolve()),'no_retry':True})
  s.check(O,rf,3,lambda x:None);checks.append('full225-pair plus zero-pair screen')
  original={p.name:p.read_bytes()for p in O.iterdir()}
  def restore():
   for name,data in original.items():(O/name).write_bytes(data)
  def reject(name,mut):
   restore();mut();wr= json.loads((O/'WORKER_COMPLETE.json').read_text());wr['result_sha256']=s.sha(O/'RESULT.json');write(O/'WORKER_COMPLETE.json',wr)
   try:s.check(O,rf,3,lambda x:None)
   except ValueError:checks.append(name);return
   raise AssertionError(name+' accepted')
  def wrong_screen():
   r=copy.deepcopy(result);r['rows'][1]['screen_upper']='1';write(O/'RESULT.json',r);write(O/'variational.json',r['rows'][1]);ev=copy.deepcopy(events);[e.update(data=r['rows'][1])for e in ev if e['stage']=='choice_complete'and e['choice']=='variational'];(O/'EVENTS.ndjson').write_text(''.join(json.dumps(x)+'\n'for x in ev))
  reject('coherently false screen',wrong_screen)
  def wrong_pair():
   ev=copy.deepcopy(events);next(e for e in ev if e['stage']=='joint_pair')['data']['values'][0]=['-10','-9'];(O/'EVENTS.ndjson').write_text(''.join(json.dumps(x)+'\n'for x in ev))
  reject('wrong affine kernel',wrong_pair)
  def badcount():
   r=copy.deepcopy(result);r['choices']=True;write(O/'RESULT.json',r)
  reject('bool count',badcount)
  reject('failure output',lambda:write(O/'FAILURE.json',{}));(O/'FAILURE.json').unlink()
  reject('zero worker seconds',lambda:write(O/'WORKER_COMPLETE.json',{**wr,'seconds':0}))
run();print(json.dumps({'checks':checks,'native_inputs':False,'producer_gram_used_only_for_synthetic_fixture':True,'old205_truth_is_synthetic_placeholder_not_validated_here':True},indent=2))
