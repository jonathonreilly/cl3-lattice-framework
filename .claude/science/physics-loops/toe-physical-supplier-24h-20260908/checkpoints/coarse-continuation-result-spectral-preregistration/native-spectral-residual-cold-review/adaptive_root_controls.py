"""Reuse only author's identity-table synthetic outputs; no Wick rerun."""
from pathlib import Path
import types,tempfile,shutil,json,copy
B=Path('/private/tmp/toe-24h-probes-20260908');P=B/'native-spectral-residual-root-review';E=B/'native-spectral-runtime-synthetic/adaptive'
m=types.ModuleType('schema');exec(compile((P/'schema.py').read_text(),str(P/'schema.py'),'exec'),m.__dict__)
def wr(p,x):p.write_text(json.dumps(x))
with tempfile.TemporaryDirectory()as tmp:
 t=Path(tmp);o=t/'output';shutil.copytree(E/'normal',o);w=t/'worker';w.mkdir();m.__file__=str(t/'schema.py');wr(t/'WORKER_AUTHORIZATION.json',{});wr(o/'STARTED.json',{})
 bind={}
 for degree in [10,20]:
  lines=[json.loads(x)for x in(E/f'inputs/{degree}/events').read_text().splitlines()]
  if degree==20:lines[2]['stage']='choice_start' # restore author's deliberate last adversary in this private synthetic copy only
  f=t/str(degree);f.write_text(''.join(json.dumps(x)+'\n'for x in lines));bind['degree'+str(degree)]={'events':{'path':str(f),'sha256':m.sha(f)}}
 wr(w/'BINDING.json',bind);r=json.loads((o/'RESULT.json').read_text());part=json.loads((o/'PARTIAL.json').read_text());r['seconds']=1;part['seconds']=.9;wr(o/'RESULT.json',r);wr(o/'PARTIAL.json',part)
 def done():wr(o/'WORKER_COMPLETE.json',{'status':'COMPLETE_NEW_SPECTRAL_RESIDUAL_ONLY','runtime_sha256':'fake','binding_sha256':m.sha(w/'BINDING.json'),'result_sha256':m.sha(o/'RESULT.json'),'seconds':2,'rss_bytes':1000})
 done();rf={'worker_path':str(w),'worker_freeze':'fake'};m.check(o,rf,3,lambda _:None);checks=['adaptive event synthetic full arithmetic']
 row=r['rows'][0];row['status']='POSITIVE_CERTIFICATE';wr(o/'residual.json',row);wr(o/'RESULT.json',r);ev=[json.loads(x)for x in(o/'EVENTS.ndjson').read_text().splitlines()]
 for x in ev:
  if x['stage']=='choice_complete'and x['mode']=='residual':x['data']=row
 ev[-1]['data']['rows']=r['rows'];(o/'EVENTS.ndjson').write_text(''.join(json.dumps(x)+'\n'for x in ev));part['current']=ev[-1];part['completed']=r['rows'];wr(o/'PARTIAL.json',part);done()
 try:m.check(o,rf,3,lambda _:None)
 except ValueError as e:assert str(e)=='posterior answer';checks.append('coherent false posterior rejected')
 else:raise AssertionError('false sign accepted')
 print(json.dumps({'scope':'synthetic saved fixture only;0 native/scalar/Wick calls','passed':checks}))
