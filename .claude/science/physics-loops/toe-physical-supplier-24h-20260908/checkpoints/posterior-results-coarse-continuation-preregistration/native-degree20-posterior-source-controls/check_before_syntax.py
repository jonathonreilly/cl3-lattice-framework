from pathlib import Path
import json,types,sys,hashlib
B=Path('/private/tmp/toe-24h-probes-20260908');S=B/'native-degree20-posterior-certificate-design';E=Path(__file__).parent
for name in ['posterior','worker']:
 m=types.ModuleType(name);sys.modules[name]=m;exec(compile((S/(name+'.py')).read_bytes(),str(S/(name+'.py')),'exec'),m.__dict__)
w=sys.modules['worker'];events=[];counters={};gate={'E':['0','0'],'F':['0','0'],'nominal':['2','2'],'rows':{'P':{'q':'0'},'O':{'q':'0'}}
for i,(stage,mode)in enumerate(w.schedule(),1):
 data={}
 if stage=='choice_start':data={'mode':mode};counters[mode]=0
 if stage=='vacuum_inputs':counters[mode]+=1
 if stage=='source_moment_raw':
  k='P'if counters[mode]==1 else'O';idx=sum(e['stage']==stage and e['choice']==mode and e['data']['kind']==k for e in events);data={'kind':k,'index':idx,'real':['8','8'],'imaginary':['0','0']}
 if stage=='residual_raw':data={'kind':'P'if counters[mode]==1 else'O','q':'0'}
 if stage=='gate_inputs':data=gate
 events.append({'sequence':i,'stage':stage,'choice':mode,'data':data})
assert len(events)==255
F=E/'fake';F.mkdir(exist_ok=True)
def put(n,x,raw=False):
 p=F/n;p.write_text(x if raw else json.dumps(x));return {'path':str(p),'sha256':w.sha(p)}
res={'status':'COMPLETE_FIXED_DEGREE20_CERTIFICATE','events':255,'choices':2,'rows':[{'mode':m,'nominal':gate['nominal']}for m in ['residual','variational']]};files={};files['result']=put('result',res);files['root_freeze']=put('root',{'worker_freeze':'fake'});files['events']=put('events',''.join(json.dumps(e)+'\n'for e in events),True)
files['acceptance']=put('acceptance',{'status':'ACCEPTED_NEW_NATIVE_DEGREE20_WARD_ROOT_REVIEW_ONCE','result_sha256':files['result']['sha256'],'worker_freeze':'fake','root_freeze':files['root_freeze']['sha256'],'external_seconds':3,'external_rss_bytes':1000000,'sampled_whole_tree_peak':2000000})
files['worker_complete']=put('complete',{'status':'COMPLETE_NEW_DEGREE20_ONLY','runtime_sha256':'fake','result_sha256':files['result']['sha256'],'seconds':1,'rss_bytes':1000000})
files['root_receipt']=put('receipt',{'pass':True,'returncode':0,'worker_freeze':'fake','seconds':2,'sampled_whole_tree_peak':2000000})
b={'files':files,'worker_freeze':'fake'};out=E/'output';out.mkdir();w.run(b,out);r=json.loads((out/'RESULT.json').read_text());assert r['source_events']==255 and r['choices']==2;assert all(x['status']=='POSITIVE_CERTIFICATE'for x in r['rows'])
# Coherently rehashed schedule failure must retain the offending source stage.
events[3]['stage']='bad';files['events']=put('events',''.join(json.dumps(e)+'\n'for e in events),True);out2=E/'bad-output';out2.mkdir()
try:w.run(b,out2)
except ValueError:assert (out2/'FAILURE.json').exists()
else:raise AssertionError('bad chronology accepted')
print(json.dumps({'checks':3,'status':'PASS_SYNTHETIC_ONLY','fake_events':255,'actual_values_loaded':0}))
