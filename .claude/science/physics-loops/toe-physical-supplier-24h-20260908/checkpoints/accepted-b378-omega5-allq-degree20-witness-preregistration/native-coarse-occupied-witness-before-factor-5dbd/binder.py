from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from interval import const

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def pair(xs):
 if type(xs)is not list or len(xs)!=2 or any(type(x)is not str for x in xs):raise ValueError('pair')
 lo,hi=map(F,xs)
 if lo>hi:raise ValueError('interval')
 return lo,hi
def load(plan,emit):
 if plan['status']!='BOUND_ACCEPTED_NEW_B378_WITNESS':raise ValueError('B378 acceptance pending')
 def read(role):
  x=plan['files'][role];emit('before_input',{'role':role})
  if sha(x['path'])!=x['sha256']:raise ValueError('pin '+role)
  return json.loads(Path(x['path']).read_text())
 for role,status in plan['acceptance_status'].items():
  if read(role)['status']!=status:raise ValueError('acceptance '+role)
 bnew=read('B378_result')
 if bnew['status']!='COMPLETE_NEW_B378_ONLY' or bnew['all_targets_met']is not True or len(bnew['rows'])!=378:raise ValueError('accepted B378 census')
 nodes=read('new_nodes')['rows'];oldpoles=read('old_poles')['rows'];olda=read('old_A')['rows'];oldb=read('old_B')['rows'];poleplan=read('original_pole_binding')
 oldpi=sum(map(F,poleplan['pi_interval']))/2
 old=[]
 if any(len(x)!=66 for x in (oldpoles,olda,oldb)):raise ValueError('old census')
 for i,(p,a,b) in enumerate(zip(oldpoles,olda,oldb)):
  s=F(p['s_midpoint'])
  if F(a['oracle']['s'])!=s or F(b['s_midpoint'])!=s:raise ValueError('old midpoint identity')
  old.append({'s':s,'A':pair(a['oracle']['A']),'B':pair(b['B']),'alpha':const(35*sum(map(F,p['weight']))/(4*oldpi))})
 c=pair(read('cminus')['interval']);mu=pair(read('mu')['interval'])
 coefficients={};pi=None
 x=plan['files']['coefficient_events'];emit('before_input',{'role':'coefficient_events'})
 if sha(x['path'])!=x['sha256']:raise ValueError('coefficient events pin')
 with Path(x['path']).open() as f:
  for line in f:
   event=json.loads(line)
   if event['stage']=='node_operator':
    r=event['payload'];coefficients[(r['index'],r['kind'])]=[[const(F(x)) for x in rr] for rr in r['positive_imaginary']]
   elif event['stage']=='reciprocal_pi':pi=pair(event['payload']['interval'])
 if len(coefficients)!=756 or pi is None:raise ValueError('coefficient census')
 new=[]
 for i,(n,b) in enumerate(zip(nodes,bnew['rows'])):
  if n['id']!=i or b['id']!=i or F(n['s'])!=F(b['s']):raise ValueError('new identity')
  x=plan['new_A_raw'][str(i)];raw=Path(x['path']).read_bytes()
  if hashlib.sha256(raw).hexdigest()!=x['sha256']:raise ValueError('new A pin')
  a=json.loads(raw)['raw'];new.append({'s':F(n['s']),'A':pair(a['A']),'B':pair(b['B']),'index':i})
 selected=[]
 for i in range(5):
  ids=read('selected_'+str(i));raw=read('T_'+str(i))
  if len(ids)!=24 or len(set(ids))!=24 or any(type(x)is not int or not 0<=x<399 for x in ids):raise ValueError('selected IDs')
  if len(raw)!=48 or any(len(r)!=48 for r in raw):raise ValueError('T shape')
  t=[[F(x) for x in r] for r in raw]
  if any((x*2**256).denominator!=1 for r in t for x in r):raise ValueError('T dyadic')
  selected.append((ids,[[const(x) for x in r] for r in t]))
 return old,new,selected,c,mu,coefficients,pi
