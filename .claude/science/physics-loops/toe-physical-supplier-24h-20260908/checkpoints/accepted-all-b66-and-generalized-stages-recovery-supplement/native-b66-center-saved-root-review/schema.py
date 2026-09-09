import json,hashlib,math
from pathlib import Path
def check(out,rf,elapsed,progress=lambda x:None):
 out=Path(out);r=json.loads((out/'RESULT.json').read_text());w=json.loads((out/'WORKER_COMPLETE.json').read_text());p=json.loads((out/'PARTIAL.json').read_text())
 if {x.name for x in out.iterdir()}!={'RESULT.json','WORKER_COMPLETE.json','PARTIAL.json'}:raise ValueError('membership')
 if r['status']!='PASS_ALL_SAVED_CENTER_FORMULAS'or w['status']!='COMPLETE_SAVED_CENTER_REPLAY':raise ValueError('status')
 for k,n in [('node_pairs',114972),('panels',4422),('tail_terms',40),('oracle_calls',0)]:
  if type(r[k])is not int or r[k]!=n:raise ValueError(k)
 if r['inherited_width_radii']is not True or len(r['poles'])!=66:raise ValueError('scope')
 for i,v in enumerate(r['poles']):
  if type(v['pole'])is not int or v['pole']!=i or type(v['target_met'])is not bool:raise ValueError('pole')
 if p!={'stage':'complete','node_pairs':114972}:raise ValueError('partial')
 if w['worker_freeze']!=rf['worker_freeze']or w['result_sha256']!=hashlib.sha256((out/'RESULT.json').read_bytes()).hexdigest():raise ValueError('binding')
 if type(w['seconds'])not in(int,float)or not math.isfinite(w['seconds'])or not 0<w['seconds']<119 or w['seconds']>elapsed or type(w['rss_bytes'])is not int or not 0<w['rss_bytes']<=384*1048576:raise ValueError('resources')
 return {'status':'PASS_SAVED_CENTER_REPLAY_SCHEMA','node_pairs':114972,'independent_formula_replay':True}
