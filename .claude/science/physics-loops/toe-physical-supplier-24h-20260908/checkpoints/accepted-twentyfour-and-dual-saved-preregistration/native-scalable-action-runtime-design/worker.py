"""Prospective only; binder is unconditionally disabled."""
import json,time,os
from pathlib import Path
import binder,adapter,old_reader,coefficients,core

def save(p,x):
 t=p.with_suffix('.tmp');t.write_text(json.dumps(x)+'\n');os.replace(t,p)
def compute(plan,out,prepared=False):
 if plan.get('status')!='ROOT_REVIEWED_SCALABLE_ACCEPTED_HISTORY':raise ValueError('NOTREADY')
 out=Path(out)
 if prepared:
  if not out.is_dir() or sorted(x.name for x in out.iterdir())!=['STARTED.json']:raise ValueError('prepared output')
 else:out.mkdir(exist_ok=False)
 start=time.monotonic();opened=[];rows=[];current={'stage':'binding'};save(out/'PARTIAL.json',current)
 try:
  cp,ap,np,radii,states,poles,alpha,etamu=binder.load(plan)
  if len(states)!=5:raise ValueError('five accepted orbit states')
  ss,aa=adapter.exact_midpoint_family(poles,alpha)
  save(out/'FAMILY.json',{'poles':list(map(str,poles)),'alpha':list(map(str,alpha)),'same_exact_rational_midpoint_family':True,'quadrature_displacement_separate':True})
  for path,kind in((cp,'cache'),(ap,'append'),(np,'new')):
   current={'stage':'index','kind':kind};save(out/'PARTIAL.json',current)
   opened.append(adapter.NewIndex(path,plan['inputs'][path]) if kind=='new' else old_reader.Indexed(path,plan['inputs'][path],kind))
  for oi,state in enumerate(states):
   current={'stage':'orbit','orbit':oi};save(out/'PARTIAL.json',current);od=out/f'ORBIT_{oi}';od.mkdir();save(od/'RESTORED_STATE.json',state)
   hist=state['history'];diag=state['checkpoint']['diagonals']
   if type(state['orbit'])is not int or state['orbit']!=oi or not 12<=len(hist)<=24 or type(state['checkpoint']['pairs'])is not int or state['checkpoint']['pairs']!=len(hist):raise ValueError('accepted cumulative history')
   entry=adapter.Entries(old_reader.Entries(opened[0],opened[1],old_reader.ORBITS[oi],**radii),opened[2],oi,etaA=radii['etaA'],etaB=radii['etaB'],etac=radii['etac'],etamu=etamu)
   with(od/'EVENTS.ndjson').open('x') as log:
    def persist(e):
     nonlocal current
     current={'orbit':oi,**e};log.write(json.dumps(current)+'\n');log.flush();save(out/'PARTIAL.json',current)
    try:
     cols,R=coefficients.coefficients(hist,persist)
     for col in cols:
      for k in col:adapter.key(k)
     save(od/'COEFFICIENTS.json',{'columns':[coefficients.encode(c) for c in cols],'R':R})
     result=core.bound(cols,R,diag,entry,ss,aa,persist)
    except coefficients.Indeterminate as exc:
     result={'status':'INDETERMINATE_CONDITIONING','error':repr(exc),'current':current,'leakage_pass':False};persist({'stage':'indeterminate','error':repr(exc)})
   save(od/'RESULT.json',result);rows.append({'orbit':oi,'pairs':len(hist),'status':result['status'],'result_sha256':binder.sha(od/'RESULT.json'),'events_sha256':binder.sha(od/'EVENTS.ndjson')});save(out/'PARTIAL.json',{'stage':'orbit_complete','completed_orbits':rows})
 except BaseException as exc:
  save(out/'FAILURE.json',{'current':current,'completed_orbits':rows,'error':repr(exc),'seconds':time.monotonic()-start});raise
 finally:
  errors=[]
  for x in opened:
   try:x.verify()
   except BaseException as exc:errors.append('verify '+repr(exc))
   finally:
    try:x.close()
    except BaseException as exc:errors.append('close '+repr(exc))
  if errors:save(out/'IMMUTABILITY_FAILURE.json',{'errors':errors,'current':current});raise ValueError('descriptor closure')
 r={'status':'COMPLETE_SCALABLE_SUFFICIENT_BOUND','orbits':rows,'seconds':time.monotonic()-start,'new_pivots':0,'midpoint_isometry_claim':False,'scope':'upper bound or conditioning indeterminate; not propagation/no-go'};save(out/'PARTIAL.json',{'stage':'complete','completed_orbits':rows});save(out/'RESULT.json',r);return r
