import json,time,math
from pathlib import Path
from fractions import Fraction as F
import arithmetic as a
import schema

def write(p,x):p.write_text(json.dumps(x)+'\n')
def same(x,y):return json.dumps(x,sort_keys=True)==json.dumps(y,sort_keys=True)
def run(binding,out):
 out=Path(out);start=time.monotonic();current={'stage':'binding'};rows=[];count=0
 def require(x,m):a.demand(x,m)
 try:
  for p,h in binding['inputs'].items():require(schema.sha(p)==h,'binding '+p)
  old=Path(binding['output']);root=Path(binding['root']);accept=schema.read(root/'ROOT_ACCEPTANCE.json');receipt=schema.read(root/'RECEIPT.json');rf=schema.read(root/'ROOT_FREEZE.json')
  require(accept['status']=='ACCEPTED_COMPLETE_ORIGINAL_FOUR_PAIR_ACTION_ENCLOSURE','acceptance')
  require(accept['result_sha256']==schema.sha(old/'RESULT.json') and accept['worker_freeze']==rf['worker_freeze'] and accept['root_freeze']==schema.sha(root/'ROOT_FREEZE.json'),'accepted hashes')
  require(receipt['pass'] is True and receipt['worker_freeze']==rf['worker_freeze'],'root receipt')
  for x,cap in ((accept['external_seconds'],120),(accept['external_max_rss'],384*1048576),(accept['sampled_whole_tree_peak'],384*1048576),(receipt['seconds'],120),(receipt['sampled_whole_tree_peak'],384*1048576)):
   require(type(x)in(int,float) and math.isfinite(x) and 0<x<=cap,'resource')
  schema.check(old,rf,receipt['seconds']) # Explicit reuse: structural checks, not arithmetic independence.
  family=schema.read(old/'FAMILY.json');poles=list(map(F,family['poles']));alpha=list(map(F,family['alpha']));require(len(poles)==len(alpha)==66,'family')
  for oi in range(5):
   d=old/f'ORBIT_{oi}';events=[json.loads(l) for l in(d/'EVENTS.ndjson').read_text().splitlines()];used=set();current={'stage':'orbit','orbit':oi};write(out/'PARTIAL.json',current)
   def emit(stage,body):
    nonlocal current,count
    matches=[(j,e) for j,e in enumerate(events) if j not in used and e['stage']==stage and all(e.get(k)==v for k,v in body.items() if k in('pair','impurity_bare_index'))]
    require(len(matches)==1,'unique saved stage '+stage);j,e=matches[0];current={'orbit':oi,'stage':stage,'saved_event':j};write(out/'PARTIAL.json',current)
    write(out/f'ORBIT_{oi}_{j}_{stage}.json',body) # Preserve independently computed intermediate before comparison.
    require(same(e,{'orbit':oi,'stage':stage,**body}),'saved arithmetic '+stage);used.add(j);count+=1
   state=schema.read(d/'RESTORED_STATE.json');require(len(state['history'])==4,'original4');cols,R=a.coefficients(state['history'],emit);require(same(schema.read(d/'COEFFICIENTS.json'),{'columns':[a.encode(c) for c in cols],'R':R}),'coefficients')
   ps=[e for e in events if e['stage']=='principal_gram_complete'];require(len(ps)==1,'principal record');p=ps[0];U=tuple(sorted(set(R)|{(r,g) for r in(396,399,400,401) for g in(0,1)}));require(same(p['U'],U),'principal support');M={}
   for i,j,k,l,lo,hi in p['entries']:M[(i,j),(k,l)]=M[(k,l),(i,j)]=a.box((lo,hi))
   require(len(p['entries'])==len(U)*(len(U)+1)//2 and all((i,j)in M for i in U for j in U),'principal census')
   results=[]
   for imp in (399,400):
    z=a.action(cols,M,poles,alpha,imp,emit);emit('action_enclosed',z);results.append(z)
   expected={'status':'COMPLETE_CONDITIONAL_ACTION_ENCLOSURE','R':R,'U':U,'results':results,'midpoint_isometry_claim':False};require(same(expected,schema.read(d/'RESULT.json')),'final action')
   rows.append({'orbit':oi,'original_pairs':4,'arithmetic_events':len(used),'leakage_pass':[r['leakage_pass'] for r in results]});write(out/'PARTIAL.json',{'stage':'orbit_complete','rows':rows})
  for p,h in binding['inputs'].items():require(schema.sha(p)==h,'final immutable '+p)
  result={'status':'PASS_SAVED_FOUR_ACTION_ARITHMETIC','orbits':rows,'events_checked':count,'seconds':time.monotonic()-start,'native_calls':0,'scope':'Saved principal Gram assumed authenticated; independent Fraction/isqrt coefficient and action contractions, no original Gram recomputation'};write(out/'RESULT.json',result)
 except BaseException as e:write(out/'FAILURE.json',{'current':current,'completed':rows,'error':repr(e),'seconds':time.monotonic()-start});raise
