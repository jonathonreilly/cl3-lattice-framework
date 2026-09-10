from pathlib import Path
import sys,json,hashlib,copy,tempfile,importlib.util
B=Path('/private/tmp/toe-24h-probes-20260908');W=B/'native-degree10-reduced-dual-design';R=B/'native-reduced-dual-root-review'
def load(name,p):
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
I=load('interval',W/'interval.py')
for name in ['degree10','wick','algebra']:load(name,W/(name+'.py'))
g=load('dual',W/'dual.py');s=load('test_schema',R/'schema.py')
# Stub ONLY raw covariance/operator construction and Wick contractions.
# Actual dual proposal/scaling/aggregation code still executes on synthetic boxes.
def prepare(label,rows,c,nu):
 cl=g.kind(label);sizes={'w':2,'Hw':4,'Ju':2,'HJu':6,'u':2,'Hu':3,'r':4,'s':4};z=[['0','0'],['0','0']];raw={'G':[[z for _ in range(9)]for _ in range(9)],'operators':{k:[[[],[[('1'if cl=='P'else'2')]*2,['0','0']]]for _ in range(v)]for k,v in sizes.items()}};key=hashlib.sha256(json.dumps(raw,sort_keys=True,separators=(',',':')).encode()).hexdigest();return None,None,key,raw
def acquire(G,ops,emit):
 A=[[I.point(1+int(i==j))for j in range(4)]for i in range(4)];B2=[[I.point(1+int(i==j))for j in range(2)]for i in range(2)];cs=[I.point(I.F(1,8)),I.point(I.F(-1,7)),I.point(I.F(1,9))];counts={'wick_states':0,'complex_products':0}
 for left,right in s.ENTRY_ORDER:
  emit('before_dual_entry',{'left':left,'right':right});value=cs[s.ENTRY_ORDER.index((left,right))-13]if s.ENTRY_ORDER.index((left,right))>=13 else I.point(1+int(left==right));emit('dual_entry',{'left':left,'right':right,'value':(value,I.point(0)),'counts':counts})
 return {'A':A,'B':B2,'correction':cs,'words':171,'counts':counts}
g.prepare=prepare;g.acquire=acquire
checks=[]
def write(p,o):p.write_text(json.dumps(o)+'\n')
def run():
 with tempfile.TemporaryDirectory(prefix='three-gram-SYNTHETIC-')as td:
  T=Path(td);O=T/'output';O.mkdir();worker=T/'worker';worker.mkdir();events=[];old=[];rows=[];sr=[]
  def emit(stage,data,mode=None):events.append({'sequence':len(events)+1,'choice':mode,'stage':stage,'data':I.encode(data)})
  old.append({'stage':'scalar_inputs','choice':None,'data':{'c':['1/2','1/2'],'nu':['2','2']}})
  for mode in s.MODES:
   coef={'P':{'p0':'1','p1':'0','q':'0'},'O':{'p0':'1','p1':'0','q':'0'}};nom=['1','1'] if mode=='residual'else['0','0'];gate={'nominal':nom}
   old.append({'stage':'gate_inputs','choice':mode,'data':gate})
   for k in ['P','O']:
    old.append({'stage':'polynomial','choice':mode,'data':{'kind':k,'p0':'1','p1':'0'}});old.append({'stage':'residual_raw','choice':mode,'data':{'kind':k,'q':'0'}})
   sr.append({'mode':mode,'nominal':nom,'E_upper':'1','F_upper':'1','alpha_interval':['-1000','1000']})
  while len(old)<205:old.append({'stage':'SYNTHETIC_PLACEHOLDER','choice':None,'data':{}})
  oldpath=T/'original-events';oldpath.write_text(''.join(json.dumps(x)+'\n'for x in old));sp=T/'spectral.json';write(sp,{'rows':sr});desc=lambda p:{'path':str(p),'sha256':s.sha(p)};write(worker/'BINDING.json',{'degree10':{'events':desc(oldpath)},'spectral':{'result':desc(sp)}})
  for k in ['acceptance','receipt','root_freeze','worker','result','binding','acceptance','worker','receipt','root_freeze','result']:emit('before_input',{'role':k})
  for i in range(1,206):emit('before_source_event',{'index':i})
  for mode,x in zip(s.MODES,sr):
   inp={'c':['1/2','1/2'],'nu':['2','2'],'coefficients':coef,'nominal':x['nominal'],'E_upper':x['E_upper'],'F_upper':x['F_upper'],'spectral_alpha_interval':x['alpha_interval']};write(O/(mode+'_INPUT.json'),inp);emit('new_inputs',inp,mode);ans=g.evaluate(inp,lambda a,b:emit(a,b,mode));ans['mode']=mode;ans=I.encode(ans);rows.append(ans);write(O/(mode+'.json'),ans);emit('choice_complete',ans,mode)
  emit('complete',{});(O/'EVENTS.ndjson').write_text(''.join(json.dumps(x)+'\n'for x in events));write(O/'PARTIAL.json',{'current':events[-1],'completed':2})
  result={'status':'COMPLETE_NEW_REDUCED_DUAL_ESTIMATOR','rows':rows,'choices':2,'max_unique_gram_sets':4,'max_actual_Wick_words':684,'logical_Wick_words':5130,'native_oracle_calls':0,'old_moments_recomputed':0,'old_nominal_recomputed':0,'seconds':1,'events':len(events)};write(O/'RESULT.json',result);rf={'worker_freeze':'synthetic','worker_path':str(worker)}
  wr={'status':'COMPLETE_NEW_REDUCED_DUAL_ONLY','seconds':2,'rss_bytes':1000,'runtime_sha256':'synthetic','binding_sha256':s.sha(worker/'BINDING.json'),'result_sha256':s.sha(O/'RESULT.json')};write(O/'WORKER_COMPLETE.json',wr);write(O/'STARTED.json',{'runtime_sha256':'synthetic','binding_sha256':wr['binding_sha256'],'output':str(O.resolve()),'no_retry':True})
  s.check(O,rf,3,lambda x:None);checks.append('full763 events five-scale two-mode cached-Gram')
  original={p.name:p.read_bytes()for p in O.iterdir()}
  def restore():
   for name,data in original.items():(O/name).write_bytes(data)
  def reject(name,mut):
   restore();mut();wr= json.loads((O/'WORKER_COMPLETE.json').read_text());wr['result_sha256']=s.sha(O/'RESULT.json');write(O/'WORKER_COMPLETE.json',wr)
   try:s.check(O,rf,3,lambda x:None)
   except ValueError:checks.append(name);return
   raise AssertionError(name+' accepted')
  def wrong_scale():
   ev=copy.deepcopy(events);next(e for e in ev if e['stage']=='raw_channel_forms')['data']['lambda']='1';(O/'EVENTS.ndjson').write_text(''.join(json.dumps(x)+'\n'for x in ev))
  reject('wrong declared scale',wrong_scale)
  def wrong_pair():
   ev=copy.deepcopy(events);next(e for e in ev if e['stage']=='dyadic_proposal')['data']['t']='1';(O/'EVENTS.ndjson').write_text(''.join(json.dumps(x)+'\n'for x in ev))
  reject('wrong deterministic proposal',wrong_pair)
  def falsefinal():
   r=copy.deepcopy(result);r['rows'][0]['status']='POSITIVE_CERTIFICATE';r['rows'][0]['alpha_interval']=['1','2'];write(O/'RESULT.json',r);write(O/'residual.json',r['rows'][0]);ev=copy.deepcopy(events)
   for x in ev:
    if x['choice']=='residual'and x['stage']=='choice_complete':x['data']=r['rows'][0]
   (O/'EVENTS.ndjson').write_text(''.join(json.dumps(x)+'\n'for x in ev))
  reject('coherently rehashed false final sign',falsefinal)
  def badcount():
   r=copy.deepcopy(result);r['choices']=True;write(O/'RESULT.json',r)
  reject('bool count',badcount)
  reject('failure output',lambda:write(O/'FAILURE.json',{}));(O/'FAILURE.json').unlink()
  reject('zero worker seconds',lambda:write(O/'WORKER_COMPLETE.json',{**wr,'seconds':0}))
  restore()
  # Honest retained arithmetic prefix at the first raw form, with second choice complete.
  ev=copy.deepcopy(events);cut=next(i for i,x in enumerate(ev)if x['stage']=='raw_channel_forms');rr=copy.deepcopy(result);ans={'status':'INDETERMINATE_ARITHMETIC','error':'ValueError(synthetic retained refusal)','stage':'raw_channel_forms','unique_gram_sets':None,'actual_Wick_words':None,'mode':'residual'};rr['rows'][0]=ans
  tail=[x for x in ev if x['choice']=='variational'or x['stage']=='complete'];ev=ev[:cut+1]+[{'sequence':0,'choice':'residual','stage':'choice_complete','data':ans}]+tail
  for i,x in enumerate(ev,1):x['sequence']=i
  rr['events']=len(ev);write(O/'RESULT.json',rr);write(O/'residual.json',ans);(O/'EVENTS.ndjson').write_text(''.join(json.dumps(x)+'\n'for x in ev));write(O/'PARTIAL.json',{'current':ev[-1],'completed':2});write(O/'WORKER_COMPLETE.json',{**wr,'result_sha256':s.sha(O/'RESULT.json')});s.check(O,rf,3,lambda x:None);checks.append('retained arithmetic prefix with second choice complete')

run();print(json.dumps({'checks':checks,'native_inputs':False,'raw_Wick_only_stubbed':True,'old205_truth_is_synthetic_placeholder_not_validated_here':True},indent=2))
