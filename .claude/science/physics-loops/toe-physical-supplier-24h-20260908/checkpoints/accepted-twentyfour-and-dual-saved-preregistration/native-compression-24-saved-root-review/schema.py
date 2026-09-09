import json,hashlib,math
from pathlib import Path
def check(out,rf,elapsed):
 def req(x,m):
  if not x:raise ValueError(m)
 def read(n):return json.loads((out/n).read_text())
 w=read('WORKER_COMPLETE.json');v=read('RESULT.json');p=read('PARTIAL.json')
 req(not any((out/n).exists() for n in ('FAILURE.json','DISPATCH_FAILURE.json')),'failure files')
 req(read('STARTED.json')==rf['authorization'],'started authorization')
 req(w['status']=='COMPLETE_SAVED_ONLY' and w['runtime_sha256']==rf['worker_freeze'] and w['binding_sha256']==rf['authorization']['binding_sha256'],'worker binding')
 req(w['result_sha256']==hashlib.sha256((out/'RESULT.json').read_bytes()).hexdigest(),'result hash')
 req(type(w['seconds'])in(int,float) and type(elapsed)in(int,float) and math.isfinite(w['seconds']) and math.isfinite(elapsed) and 0<w['seconds']<29 and w['seconds']<=elapsed<30,'timing')
 req(type(w['rss_bytes'])is int and 0<w['rss_bytes']<=384*1048576,'RSS')
 req(v['status']=='PASS_NEW_SAVED_HISTORY_COORDINATES' and v['source_result_sha256']==rf['source_result_sha256'],'saved status/source')
 req(v['native_entries_replayed'] is False and v['new_pivots_selected'] is False and v['original_gram_loaded'] is False and v['all_scientific_targets_met'] is False,'literal scope flags')
 req(type(v['predicates'])is int and v['predicates']>0 and type(v['histories'])is int and v['histories']==60 and type(v['coordinates'])is int and v['coordinates']==885780,'counts')
 req(len(v['orbits'])==5,'orbits')
 for i,row in enumerate(v['orbits']):
  req(type(row['orbit'])is int and row['orbit']==i and type(row['histories'])is int and row['histories']==24 and type(row['events'])is int and row['events']==9649,'orbit records')
 req(p['stage']=='complete' and p['current'] is None and p['completed_orbits']==v['orbits'] and type(p['predicates'])is int and p['predicates']==v['predicates'] and type(p['coordinates'])is int and p['coordinates']==885780 and type(p['histories'])is int and p['histories']==60,'final partial')
 req(v['prior_pilot_seconds']=='17.94' and v['continuation_seconds']=='21.25' and v['cumulative_physical_seconds']=='39.19','preserved physical costs')
 return {'status':'ACCEPTED_SAVED_HISTORY_COORDINATE_SCHEMA','result_sha256':w['result_sha256'],'source_result_sha256':v['source_result_sha256'],'histories':60,'coordinates':885780,'all_scientific_targets_met':False,'native_entries_replayed':False,'external_pending':True}
