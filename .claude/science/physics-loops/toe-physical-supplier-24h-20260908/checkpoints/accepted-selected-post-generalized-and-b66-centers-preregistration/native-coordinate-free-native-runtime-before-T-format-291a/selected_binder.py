"""Future accepted selected extraction; no I/O at import; pending POST blocks load."""
import json,math
from pathlib import Path
import data_binder
sha=data_binder.sha

def load(plan):
 if plan.get('post_status')!='BOUND_REVIEWED_POST':raise ValueError('NOTREADY: selected independent POST pending')
 pins=plan['inputs']
 def read(p):
  if p not in pins or sha(p)!=pins[p]:raise ValueError('selected pin '+p)
  return json.loads(Path(p).read_text())
 for p,h in pins.items():
  if sha(p)!=h:raise ValueError('selected closure')
 root=read(plan['root']);w=read(plan['worker']);source=read(plan['source_binding']);runtime=read(plan['runtime']);result=read(plan['result'])
 if root['status']!='ACCEPTED_DIRECT_SELECTED_PRINCIPAL_ENCLOSURES' or root['result_sha256']!=sha(plan['result']) or root['worker_freeze']!=sha(plan['runtime']):raise ValueError('selected root')
 if w['status']!='COMPLETE_SELECTED_PRINCIPAL' or w['result_sha256']!=sha(plan['result']) or w['runtime_sha256']!=sha(plan['runtime']) or w['binding_sha256']!=sha(plan['source_binding']):raise ValueError('selected worker')
 if source['original_family_binding']!=plan['original_family_binding']:raise ValueError('same original family')
 for collection in (source['inputs'],runtime['inputs']):
  for p,h in collection.items():
   if pins.get(p)!=h:raise ValueError('selected transitive closure')
 post=read(plan['post'])
 if post['status']!='ACCEPTED_DIRECT_SELECTED_PRINCIPAL_AND_SAVED_MATRICES' or post['original_root_acceptance_sha256']!=sha(plan['root']) or post['result_sha256']!=sha(plan['result']) or post['worker_freeze']!=sha(plan['runtime']):raise ValueError('selected POST')
 if sha(post['post_result_path'])!=post['post_result_sha256'] or post['post_result_path'] not in pins:raise ValueError('POST result pin')
 for x in (post['post_external_seconds'],root['external_seconds'],w['seconds']):
  if type(x)not in(int,float) or not math.isfinite(x) or not 0<x<=180:raise ValueError('selected time')
 for x in (post['post_sampled_whole_tree_peak'],root['sampled_whole_tree_peak'],w['rss_bytes']):
  if type(x)is not int or not 0<x<=384*1048576:raise ValueError('selected RSS')
 return extract_bound_records(plan,root)

def extract_bound_records(plan,root):
 """Called only after a future reviewed POST gate; not called by current load."""
 import binder
 records=[];base=Path(plan['result']).parent
 if len(root['orbits'])!=5:raise ValueError('five selected orbits')
 for oi,row in enumerate(root['orbits']):
  if type(row['orbit'])is not int or row['orbit']!=oi or row['status']!='CERTIFIED_ENCLOSURE':raise ValueError('selected status')
  vals={}
  for name,key in (('SELECTED.json','selected_sha256'),('CANDIDATE.json','candidate_sha256')):
   path=str(base/f'ORBIT_{oi}'/name)
   if plan['inputs'].get(path)!=row[key] or sha(path)!=row[key]:raise ValueError('selected output identity')
   vals[name]=json.loads(Path(path).read_text())
  record={'orbit':oi,'pairs':24,'candidate_bits':256,'indices':vals['SELECTED.json'],'T':vals['CANDIDATE.json']}
  binder.selected_record(record,oi);records.append(record)
 return records
