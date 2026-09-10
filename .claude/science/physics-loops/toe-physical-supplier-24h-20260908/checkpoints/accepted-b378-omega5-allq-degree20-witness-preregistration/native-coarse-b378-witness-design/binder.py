"""B-stage binder only. Pending geometry overlay is mandatory, no import side effects."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
from interval import rnd

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
 accepted={}
 for role in plan['acceptance_roles']:
  x=read(role);accepted[role]=x
  if x['status']!=plan['accepted_status'][role]:raise ValueError('accepted status '+role)
  rule=plan['receipt_rules'][role];seconds=x[rule['seconds_key']]
  if type(seconds) not in (int,float) or not math.isfinite(seconds) or not 0<seconds<=rule['seconds_cap']:raise ValueError('receipt seconds')
  for key in (rule['rss_key'],'sampled_whole_tree_peak'):
   if type(x[key])is not int or not 0<x[key]<=rule['rss_cap']:raise ValueError('receipt RSS')
  root=read(rule['root_role'])
  if x['worker_freeze']!=rule['worker_freeze'] or root['worker_freeze']!=x['worker_freeze'] or plan['files'][rule['root_role']]['sha256']!=rule['root_sha256']:raise ValueError('receipt worker/root')
  if 'root_freeze' in x and x['root_freeze']!=rule['root_sha256']:raise ValueError('receipt root freeze')
 ga=accepted['geometry_acceptance'];na=accepted['new_acceptance'];ca=accepted['catalog_acceptance']
 if ga['result_sha256']!=plan['files']['geometry_result']['sha256'] or ga['worker_freeze']!=plan['files']['geometry_freeze']['sha256'] or ga['root_freeze']!=plan['geometry_root_freeze'] or ga['once'] is not True or ga['B_or_witness_certified'] is not False:raise ValueError('geometry root relation')
 if na['result_sha256']!=plan['files']['new_result']['sha256'] or na['nodes_sha256']!=plan['files']['new_nodes']['sha256'] or na['all_A_width_gates'] is not True or ca['result_sha256']!=plan['files']['catalog_result']['sha256']:raise ValueError('scalar root relation')
 gb=read('geometry_binding');gf=read('geometry_freeze')
 if gb['geometry']['new']!=plan['files']['new_nodes'] or gb['geometry']['outer']!=plan['files']['catalog_geometry'] or gf['inputs'].get(plan['files']['geometry_binding']['path'])!=plan['files']['geometry_binding']['sha256']:raise ValueError('same authenticated family')
 nr=read('new_result')
 if nr['status']!='COMPLETE' or type(nr['count'])is not int or nr['count']!=378 or nr['all_targets_met'] is not True:raise ValueError('new result completion')
 nodes=read('new_nodes')['rows'];geom=read('catalog_geometry')['nodes'];ledger=read('geometry_result')
 if len(nodes)!=378 or len(geom)!=1742 or ledger['status']!='COMPLETE_GEOMETRY_GAIN_LEDGER' or ledger['counts']!=[24948,658476]:raise ValueError('geometry census')
 targets=[]
 for i,row in enumerate(ledger['rows']):
  if type(row['id'])is not int or row['id']!=i:raise ValueError('ledger order')
  if row['actual_A_meets_quarter_budget'] is not True:raise ValueError('A feasibility')
  targets.append(F(row['required_B_radius']))
 if len(targets)!=378 or min(targets)<=0:raise ValueError('positive target census')
 old_result=read('catalog_result');catalog=[]
 if old_result['status']!='COMPLETE_FIXED_3484_CATALOG' or type(old_result['oracle_count'])is not int or old_result['oracle_count']!=3484 or len(old_result['rows'])!=3484:raise ValueError('catalog count')
 for i,node in enumerate(geom):
  emit('before_catalog_node',{'id':i});ends=[]
  if type(node['id'])is not int or node['id']!=i or node['endpoint_ids']!=[2*i,2*i+1] or any(type(e)is not int for e in node['endpoint_ids']):raise ValueError('catalog node identity')
  for eid in node['endpoint_ids']:
   record=old_result['rows'][eid]
   if type(record['id'])is not int or record['id']!=eid or record['path']!='ORACLES/%04d.json'%eid or record['gate']!='PASS':raise ValueError('catalog record identity')
   path=Path(plan['catalog_directory'])/record['path']
   if sha(path)!=record['sha256']:raise ValueError('oracle record pin')
   raw=json.loads(path.read_text());aa=tuple(map(F,raw['A']))
   if len(aa)!=2 or not 0<aa[0]<=aa[1] or aa[1]-aa[0]>F(1,10**30) or F(raw['s'])!=F(node['t_interval'][eid%2]):raise ValueError('endpoint scalar relation')
   ends.append(aa)
  at=(ends[1][0],ends[0][1])
  if not 0<at[0]<=at[1] or at[1]-at[0]>F(1,10**45):raise ValueError('actual catalog enclosure cap')
  original={'t':tuple(map(F,node['t_interval'])),'weight':tuple(map(F,node['weight'])),'A':at}
  mapped={k:rnd(*box) for k,box in original.items()}
  if any(len(box)!=2 or not 0<box[0]<=box[1] for box in original.values()):raise ValueError('positive catalog boxes')
  if any(not mapped[k][0]<=box[0]<=box[1]<=mapped[k][1] for k,box in original.items()):raise ValueError('outward catalog mapping')
  emit('mapped_catalog',{'id':i,'endpoint_ids':node['endpoint_ids'],'endpoint_hashes':[old_result['rows'][e]['sha256'] for e in node['endpoint_ids']],'geometry_sha256':plan['files']['catalog_geometry']['sha256'],'mapped':mapped})
  catalog.append(mapped)
 new=[]
 for i,node in enumerate(nodes):
  emit('before_new_A',{'id':i});path=Path(plan['new_directory'])/('RAW_%03d.json'%i)
  if sha(path)!=plan['new_raw_hashes'][str(i)]:raise ValueError('new raw pin')
  doc=json.loads(path.read_text())
  if type(node['id'])is not int or node['id']!=i or type(doc['id'])is not int or doc['id']!=i:raise ValueError('new node identity')
  raw=doc['raw'];a=tuple(map(F,raw['A']))
  if F(raw['s'])!=F(node['s']) or not 0<a[0]<=a[1] or a[1]-a[0]>F(1,10**30):raise ValueError('new scalar relation')
  mapped_a=rnd(*a);emit('mapped_new_A',{'id':i,'raw_sha256':plan['new_raw_hashes'][str(i)],'mapped_A':mapped_a})
  new.append({'id':i,'s':node['s'],'A':mapped_a,'target_radius':targets[i]})
 return new,catalog
