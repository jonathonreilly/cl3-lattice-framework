import json,time
from pathlib import Path
from fractions import Fraction
import binder,old_reader,principal,candidate,dyadic_residual
from events import Events
def dump(path,x):path.write_text(json.dumps(x,default=lambda x:str(x)if isinstance(x,Fraction)else None)+'\n')
def compute(plan,out,prepared=False):
 if plan['status']!='ROOT_REVIEWED_SELECTED_PRINCIPAL':raise ValueError('NOT_READY')
 out=Path(out)
 if prepared:
  if not out.is_dir() or {x.name for x in out.iterdir()}!={'STARTED.json'}:raise ValueError('prepared output')
 else:out.mkdir(exist_ok=False)
 opened=[];rows=[];current={'stage':'binding'};start=time.monotonic()
 def state(x):
  nonlocal current
  current=x;dump(out/'PARTIAL.json',{'current':current,'rows':rows})
 state(current)
 try:
  cp,ap,radii,selected=binder.load(plan)
  for path,mode in ((cp,'cache'),(ap,'append')):
   state({'stage':'index','mode':mode});opened.append(old_reader.Indexed(path,plan['inputs'][path],mode))
  for oi,ids in enumerate(selected):
   od=out/f'ORBIT_{oi}';od.mkdir();dump(od/'SELECTED.json',ids);log=Events(od/'EVENTS.ndjson')
   def persist(stage,data):state({'stage':stage,'orbit':oi});log(stage,data)
   try:
    G,r,E=principal.assemble(ids,old_reader.Entries(*opened,old_reader.ORBITS[oi],**radii),persist)
    T=candidate.propose(G,persist);dump(od/'CANDIDATE.json',T)
    ans=dyadic_residual.verify(G,r,T,E,persist);dump(od/'RESULT.json',ans)
   except (candidate.CandidateFailure,dyadic_residual.Limit)as exc:
    ans={'status':'INDETERMINATE_LIMIT_OR_CANDIDATE','error':repr(exc),'failure_kind':type(exc).__name__,'current':current};dump(od/'RESULT.json',ans)
   finally:log.close()
   rows.append({'orbit':oi,'status':ans['status']});state({'stage':'orbit_complete','orbit':oi})
  for path,h in plan['inputs'].items():
   if binder.sha(path)!=h:raise ValueError('final input pin')
  state({'stage':'complete'});dump(out/'RESULT.json',{'status':'COMPLETE_SELECTED_PRINCIPAL_ATTEMPT','orbits':rows,'seconds':time.monotonic()-start})
 except BaseException as exc:dump(out/'FAILURE.json',{'error':repr(exc),'failure_kind':type(exc).__name__,'current':current,'rows':rows});raise
 finally:
  errors=[]
  for x in opened:
   try:x.verify()
   except BaseException as exc:errors.append(repr(exc))
   try:x.close()
   except BaseException as exc:errors.append(repr(exc))
  if errors:dump(out/'CLEANUP_FAILURE.json',errors);raise ValueError('descriptor verification/close failure')
