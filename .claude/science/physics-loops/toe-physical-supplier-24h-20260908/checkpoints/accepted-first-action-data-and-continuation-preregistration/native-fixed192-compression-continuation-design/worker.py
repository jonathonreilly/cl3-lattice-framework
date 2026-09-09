"""UNLAUNCHED body: caller must impose reviewed wall/RSS/source guards."""
import json,os,time
from pathlib import Path
import binder,reader,pivot

def save(path,obj):
 tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(obj,sort_keys=True)+'\n');os.replace(tmp,path)

def compute(plan,out,*,prepared=False):
 # Binder is disabled pending source/POST review. Once supplied it must
 # authenticate complete history and the terminal four-pair checkpoint.
 if plan.get('status')!='ROOT_REVIEWED_FOUR_TO_TWELVE_CONTINUATION':raise ValueError('source design: native execution disabled')
 out=Path(out)
 if prepared:
  if not out.is_dir() or sorted(x.name for x in out.iterdir())!=['STARTED.json']:raise ValueError('dispatcher prepared output')
 else:out.mkdir(exist_ok=False)
 beg=time.monotonic();opened=[];rows=[];current={'stage':'binding'}
 save(out/'PARTIAL.json',current)
 try:
  cp,ap,radii,states=binder.load(plan)
  if len(states)!=5:raise ValueError("five authenticated restored states")
  context={'binding_sha256':binder.sha(plan['self_path']),'source_freeze_sha256':plan['source_freeze_sha256'],'radii':{k:str(v) for k,v in radii.items()}}
  save(out/'CONTEXT.json',context)
  for path,mode in ((cp,'cache'),(ap,'append')):
   current={'stage':'index','mode':mode};save(out/'PARTIAL.json',current)
   opened.append(reader.Indexed(path,plan['inputs'][path],mode))
  for oi,orbit in enumerate(reader.ORBITS):
   od=out/('ORBIT_%d'%oi);od.mkdir();state=states[oi]
   if state['orbit']!=oi or len(state['history'])!=4:raise ValueError('fixed restored orbit')
   history=list(state['history'])
   save(od/'RESTORED_STATE.json',state)
   with (od/'EVENTS.ndjson').open('x') as events:
    def persist(item):
     nonlocal current
     current={'orbit':oi,**item};events.write(json.dumps(current,sort_keys=True)+'\n');events.flush()
     # Every current index is durable before evaluating its entry. Completed
     # rows/checkpoints are in append-only EVENTS before positivity/width gates.
     save(out/'PARTIAL.json',current)
     if item['stage']=='pivot_saved':
      history.append({k:item[k] for k in ('index','chirality','r','g','j')})
      save(od/'HISTORY.json',{'context':context,'orbit':oi,'history':history})
    entry=reader.Entries(*opened,orbit,**radii)
    r=pivot.run(entry,entry.lab,persist,native=True,max_pairs=12,resume=state['history'],initial_checkpoint=state['checkpoint'])
    save(od/'RESULT.json',r);rows.append({'orbit':oi,'status':r['status'],'pairs':r['pairs'],'result_sha256':binder.sha(od/'RESULT.json'),'events_sha256':binder.sha(od/'EVENTS.ndjson')})
  result={'status':'COMPLETE_FIXED_CONTINUATION_PROBE','scope':'continuation cost/precision probe, target only where both gates pass; original pilot unchanged','orbits':rows,'seconds':time.monotonic()-beg}
 except BaseException as exc:
  save(out/'FAILURE.json',{'status':'FAILED','current':current,'completed_orbits':rows,'error':repr(exc),'seconds':time.monotonic()-beg});raise
 finally:
  failures=[]
  for obj in opened:
   try:obj.verify()
   except BaseException as exc:failures.append(repr(exc))
   finally:obj.close()
  if failures:
   save(out/'IMMUTABILITY_FAILURE.json',{'errors':failures,'current':current});raise ValueError('final immutable inputs failed')
 save(out/'RESULT.json',result)
 return result
