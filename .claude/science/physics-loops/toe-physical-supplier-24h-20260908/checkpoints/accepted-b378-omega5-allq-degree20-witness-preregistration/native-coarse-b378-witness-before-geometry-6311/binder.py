"""B-stage binder only. Pending geometry overlay is mandatory, no import side effects."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def load(plan,emit):
 if plan['status']!='BOUND_ACCEPTED_GEOMETRY_B378':raise ValueError('geometry acceptance pending')
 def read(role):
  item=plan['files'][role];emit('before_input',{'role':role})
  if sha(item['path'])!=item['sha256']:raise ValueError('input hash '+role)
  return json.loads(Path(item['path']).read_text())
 for role in plan['acceptance_roles']:
  x=read(role)
  if x['status']!=plan['accepted_status'][role]:raise ValueError('accepted status '+role)
 nodes=read('new_nodes')['rows'];geom=read('catalog_geometry')['nodes'];ledger=read('geometry_result')
 if len(nodes)!=378 or len(geom)!=1742 or ledger['status']!='COMPLETE_GEOMETRY_GAIN_LEDGER' or ledger['counts']!=[24948,658476]:raise ValueError('geometry census')
 targets=[]
 for i,row in enumerate(ledger['rows']):
  if type(row['id'])is not int or row['id']!=i:raise ValueError('ledger order')
  targets.append(F(row['required_B_radius']))
 if len(targets)!=378 or min(targets)<=0:raise ValueError('positive target census')
 old_result=read('catalog_result');catalog=[]
 if len(old_result['rows'])!=3484:raise ValueError('catalog count')
 for i,node in enumerate(geom):
  emit('before_catalog_node',{'id':i});ends=[]
  for eid in node['endpoint_ids']:
   record=old_result['rows'][eid];path=Path(plan['catalog_directory'])/record['path']
   if sha(path)!=record['sha256']:raise ValueError('oracle record pin')
   raw=json.loads(path.read_text());ends.append(tuple(map(F,raw['A'])))
  at=(ends[1][0],ends[0][1])
  if not 0<at[0]<=at[1] or at[1]-at[0]>F(1,10**45):raise ValueError('actual catalog enclosure cap')
  catalog.append({'t':tuple(map(F,node['t_interval'])),'weight':tuple(map(F,node['weight'])),'A':at})
 new=[]
 for i,node in enumerate(nodes):
  emit('before_new_A',{'id':i});path=Path(plan['new_directory'])/('RAW_%03d.json'%i)
  if sha(path)!=plan['new_raw_hashes'][str(i)]:raise ValueError('new raw pin')
  raw=json.loads(path.read_text())['raw'];a=tuple(map(F,raw['A']))
  if F(raw['s'])!=F(node['s']) or not 0<a[0]<=a[1]:raise ValueError('new scalar relation')
  new.append({'id':i,'s':node['s'],'A':a,'target_radius':targets[i]})
 return new,catalog
