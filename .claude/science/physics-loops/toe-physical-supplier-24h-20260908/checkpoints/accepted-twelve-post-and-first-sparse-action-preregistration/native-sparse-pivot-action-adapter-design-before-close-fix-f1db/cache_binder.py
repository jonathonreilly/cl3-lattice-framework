"""Future accepted-input binder; no scalar evaluation or matrix construction."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def load(plan):
 if plan['status']!='ACCEPTED_POSTREVIEW_BOUND':raise ValueError('independent POST_ACCEPTANCE pending')
 pins=plan['inputs']
 def read(path):
  if path not in pins or sha(path)!=pins[path]:raise ValueError('input pin '+path)
  return json.loads(Path(path).read_text())
 for path in pins:
  if sha(path)!=pins[path]:raise ValueError('input closure')
 # Required reviewed acceptance bytes are bound independently of scalar row checks.
 for role in ('root_acceptance','post_acceptance','a_acceptance','b_source_freeze','b_binding'):
  doc=read(plan[role])
  if not isinstance(doc,dict):raise ValueError('acceptance object')
 root=read(plan['root_acceptance']);post=read(plan['post_acceptance'])
 if root['status']!='ACCEPTED_EXECUTION_COMPLETE' or post['status']!='ACCEPTED_EXECUTION_AND_SAVED_RECONCILIATION' or not post['all_66_targets_met'] or post['original_root_acceptance_sha256']!=sha(plan['root_acceptance']) or root['summary_sha256']!=sha(plan['summary']) or post['result_sha256']!=sha(plan['summary']):raise ValueError('accepted result binding')
 summary=read(plan['summary']);poles=read(plan['poles'])['rows'];arows=read(plan['a_result'])['rows']
 if summary['status']!='COMPLETE_FIXED_11_SHARDS' or not summary['all_targets_met'] or summary['pairs']!=114972:raise ValueError('accepted66')
 brows=summary['rows']
 if any(len(x)!=66 for x in (poles,arows,brows)) or len(summary['receipts'])!=11:raise ValueError('census')
 for j,receipt in enumerate(summary['receipts']):
  base=Path(plan['study'])/('SHARD_%02d'%j);wp=str(base/'WORKER_COMPLETE.json');rp=str(base/'RESULT.json');w=read(wp);r=read(rp)
  if receipt!={'shard':j,'worker_sha256':sha(wp),'result_sha256':sha(rp)}:raise ValueError('receipt')
  if w['status']!='COMPLETE' or w['shard']!=j or w['result_sha256']!=sha(rp) or w['freeze_sha256']!=plan['b_runtime_sha256'] or w['binding_sha256']!=sha(plan['b_binding']):raise ValueError('worker provenance')
  if r['rows']!=brows[6*j:6*j+6] or r['selected_ids']!=list(range(6*j,6*j+6)) or r['status']!='COMPLETE_FIXED_CASES':raise ValueError('shard rows')
 def midpoint(xs,width):
  if len(xs)!=2:raise ValueError('interval length')
  lo,hi=map(F,xs)
  if not 0<=hi-lo<=width:raise ValueError('scalar width')
  return (lo+hi)/2
 values=[];ss=[];weights=[]
 for j,(p,a,b) in enumerate(zip(poles,arows,brows)):
  if [p['id'],a['id'],b['id']]!=[j]*3 or a['pole']!=p or b['status']!='CERTIFIED_TARGET':raise ValueError('row identity')
  s=F(p['s_midpoint'])
  if F(a['oracle']['s'])!=s or F(b['s_midpoint'])!=s:raise ValueError('midpoint scalar')
  ss.append(s);weights.append(midpoint(p['weight'],F(2,2**140)))
  values.append(tuple(midpoint(a['oracle'][k],F(2,10**30)) for k in ('A','Aprime'))+tuple(midpoint(b[k],F(2,10**19)) for k in ('B','Bprime')))
 if len(set(ss))!=66 or min(ss)<F(1,128) or max(ss)>16 or sum(weights)>=16 or min(weights)<=0:raise ValueError('geometry gates')
 pi=midpoint(plan['pi_interval'],F(2,2**140))
 if not 3<pi<4:raise ValueError('pi')
 return ss,values,[35*w/(2*pi) for w in weights]
