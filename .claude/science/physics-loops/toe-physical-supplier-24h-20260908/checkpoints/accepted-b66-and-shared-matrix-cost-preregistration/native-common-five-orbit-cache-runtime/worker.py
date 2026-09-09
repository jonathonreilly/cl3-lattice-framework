"""One cache, both inverse classes, all five trace certificates; explicit call only."""
import json,time
from fractions import Fraction as F
import interval as iv,core,cache,binder

def run(plan,out):
 start=time.monotonic();stage='binding';progress={'stage':stage,'completed_cache_rows':0,'coefficients':0}
 def save():
  (out/'PARTIAL.json').write_text(json.dumps(progress,sort_keys=True)+'\n')
 save()
 try:
  poles,values,alpha=binder.load(plan);stage='coefficients';progress['stage']=stage;save()
  with (out/'COEFFICIENTS.ndjson').open('x') as f:
   for kind in ('P','O'):
    for n,s in enumerate(poles):
     signed,det,res=core.woodbury(s,values[n],kind)
     row={'kind':kind,'id':n,'signed':signed,'det':det,'residual':res};f.write(json.dumps(row)+'\n');f.flush();progress['coefficients']+=1;save()
     if max(iv.width(x) for r in signed for x in r)>iv.S//2**40 or 2*max(abs(t) for r in res for x in r for t in x)>iv.S//2**40:raise ValueError('coefficient arithmetic')
  stage='cache';progress['stage']=stage;save();traces={t:iv.ZERO for t in ('cc','P','O')}
  with (out/'CACHE.ndjson').open('x') as f:
   def write(row):
    f.write(json.dumps(row,separators=(',',':'))+'\n');f.flush()
    if row['type'] in traces:
     e=next(e for e in row['entries'] if e[0]==row['i']);traces[row['type']]=iv.add(traces[row['type']],(e[1],e[2]))
    progress.update(completed_cache_rows=progress['completed_cache_rows']+1,entries=row['count'],maximum_width=row['max_width']);save()
   result=cache.stream(poles,values,alpha,write)
  if result['entries']!=52536 or progress['completed_cache_rows']!=660:raise ValueError('cache census')
  stage='five_orbit_gates';progress['stage']=stage;save();orbits=[]
  for oa,oc,k in cache.ORBITS:
   tr=iv.scale(iv.add(traces['cc'],iv.add(traces['O' if oa else 'P'],traces['O' if oc else 'P'])),2)
   orbits.append({'orbit':[oa,oc,k],'closed_trace':tr,'denominator':iv.S,'raw_rows':396,'closed_rows':792,'arithmetic_radius':result['arithmetic_radius']})
   if tr[0]<0 or tr[1]>=529*iv.S:raise ValueError('common trace')
  result.update(status='COMPLETE_COMMON_CACHE_MIDPOINT_ARITHMETIC',orbits=orbits,coefficients=132,seconds=time.monotonic()-start,cache_sha256=binder.sha(out/'CACHE.ndjson'),coefficient_sha256=binder.sha(out/'COEFFICIENTS.ndjson'),physical_error_ledger_certified=False,pure_projector_computed=False)
  (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 except BaseException as e:
  progress.update(stage=stage,error=repr(e),seconds=time.monotonic()-start);save();(out/'FAILURE.json').write_text(json.dumps(progress)+'\n');raise
