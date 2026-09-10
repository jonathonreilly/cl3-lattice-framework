from pathlib import Path
from fractions import Fraction as F
import types,sys,json,hashlib,tempfile
P=Path(__file__).resolve().parent;b=P.parent;src=b/'native-ward-allq-saved-screen-design'
for name in ['interval','compute']:
 m=types.ModuleType(name);m.__file__=str(src/(name+'.py'));exec(compile((src/(name+'.py')).read_bytes(),m.__file__,'exec'),m.__dict__);sys.modules[name]=m
I=sys.modules['interval'];C=sys.modules['compute'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(I.encode(x))+'\n')
with tempfile.TemporaryDirectory(dir=P)as tmp:
 t=Path(tmp);out=t/'out';out.mkdir();w=t/'worker';w.mkdir();events=[]
 def ev(stage,choice,data):events.append({'sequence':len(events)+1,'stage':stage,'choice':choice,'data':data})
 ev('binding',None,{});ev('scalar_inputs',None,{})
 rows=[];ex={}
 for mode,E in [('residual',I.point(20)),('variational',I.point(0))]:
  ev('choice_start',mode,{})
  for kind in ['P','O']:
   for stage in ['moments','polynomial','source_moments','residual_raw']:ev(stage,mode,{'kind':kind,'s0':['8','8']}if stage=='source_moments'else{'kind':kind})
  for k in range(90):ev('ordered_word',mode,{'index':k+1})
  ev('gate_inputs',mode,{'E':I.encode(E)});seq=len(events);row=C.screen(E,I.point(8),I.point(8));row.update(mode=mode,source_gate_event=seq);rows.append(row);ex[mode]={'E':E,'s0P':I.point(8),'s0O':I.point(8),'gate_event':seq};ev('choice_complete',mode,{})
 ev('complete',None,{});original=t/'events';original.write_text(''.join(json.dumps(x)+'\n'for x in events));save(w/'BINDING.json',{'files':{'events':str(original)},'inputs':{str(original):sha(original)}});save(t/'WORKER_AUTHORIZATION.json',{});save(out/'STARTED.json',{})
 result={'status':'COMPLETE_SAVED_ALLQ_SCREEN','rows':rows,'modes':2,'saved_events':205,'all_fixed_first_polynomials_excluded':all(x['excluded']for x in rows),'native_calls':0,'original_moments_recomputed':0,'scope':'unchanged degree1 first polynomials and e858 error functional only; not alpha no-go','seconds':1}
 partial={'stage':'complete','source_sequence':205,'choice':None,'rows':rows,'current':{'rows':rows},'extracted':ex,'seconds':0.5}
 def write():
  save(out/'RESULT.json',result);save(out/'PARTIAL.json',partial)
  for row in rows:save(out/(row['mode']+'.json'),row)
  save(out/'WORKER_COMPLETE.json',{'status':'COMPLETE_SAVED_ALLQ_SCREEN_ONLY','runtime_sha256':'FAKE','binding_sha256':sha(w/'BINDING.json'),'result_sha256':sha(out/'RESULT.json'),'rss_bytes':100,'seconds':2})
 m=types.ModuleType('schema');m.__file__=str(t/'schema.py');source=b/'native-allq-saved-screen-root-review/schema.py';exec(compile(source.read_bytes(),str(source),'exec'),m.__dict__);rf={'worker_path':str(w),'worker_freeze':'FAKE'};write();m.check(out,rf,3,lambda x:None)
 rows[0]['excluded']=False;rows[0]['status']='INDETERMINATE_SCREEN';result['all_fixed_first_polynomials_excluded']=False;write()
 try:m.check(out,rf,3,lambda x:None)
 except ValueError:pass
 else:raise AssertionError('coherent false screen survived')
 save(P/'CONTROLS.json',{'valid_full_two_mode_fixture':'PASS','coherent_false_screen':'REJECTED','original_events':'205FABRICATED','accepted_events_read':0,'native_calls':0})
print('PASS')
