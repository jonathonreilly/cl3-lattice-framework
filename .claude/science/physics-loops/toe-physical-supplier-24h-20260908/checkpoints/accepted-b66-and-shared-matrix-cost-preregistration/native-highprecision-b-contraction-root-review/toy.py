"""Synthetic saved-schema controls. No worker, oracle or contraction import."""
from pathlib import Path
import json,types,sys,copy,tempfile
P=Path(__file__).resolve().parent;m=types.ModuleType('schema');exec(compile((P/'schema.py').read_bytes(),'schema.py','exec'),m.__dict__);count=0
with tempfile.TemporaryDirectory(prefix='B66-root-schema-') as td:
 p=Path(td);poles=[{'s_midpoint':str(i+1)} for i in range(66)];accepted=[]
 for j in range(11):
  d=p/f'SHARD_{j:02d}';d.mkdir();(d/'PANELS').mkdir();(d/'POLES').mkdir();ids=list(range(6*j,6*j+6));rows=[]
  for i in ids:
   row={'id':i,'s_midpoint':str(i+1),'B':['1','1'] if i%2==0 else ['0','1'],'Bprime':['-1','-1'],'widths':['0' if i%2==0 else '1','0'],'target':'1/5000000000000000000','status':'CERTIFIED_TARGET' if i%2==0 else 'INDETERMINATE'};rows.append(row);(d/f'POLES/{i:02d}.json').write_text(json.dumps(row))
  panels=[]
  for k in range(-64,3):
   name=f'PANELS/{k+64:02d}.json';panels.append({'panel':k,'path':name});v={str(i):[['0','0'],['0','0']] for i in ids};(d/name).write_text(json.dumps({'panel':k,'values':v,'cumulative':v}))
  result={'status':'COMPLETE_FIXED_CASES','rows':rows,'selected_ids':ids,'pairs':10452,'all_targets_met':False,'seconds':.1,'exact_gauss_root_values':False,'midpoint_displacement_requires_separate_ledger':True,'matrix_computed':False,'alpha_computed':False};(d/'RESULT.json').write_text(json.dumps(result));(d/'WORKER_COMPLETE.json').write_text(json.dumps({'status':'COMPLETE','shard':j,'seconds':.2,'rss_bytes':20000000,'freeze_sha256':'f','binding_sha256':'b','result_sha256':m.sha(d/'RESULT.json')}));(d/'PARTIAL.json').write_text(json.dumps({'stage':'finish','current':{'pole':ids[-1]},'rows':rows,'completed_panels':panels,'seconds':.09}));accepted.append(m.shard(d,j,poles,'f','b',.3));count+=1
 summary={'status':'COMPLETE_FIXED_11_SHARDS','rows':[x for a in accepted for x in a['rows']],'receipts':[{'shard':j,'worker_sha256':a['files']['WORKER_COMPLETE.json'],'result_sha256':a['files']['RESULT.json']} for j,a in enumerate(accepted)],'all_targets_met':False,'pairs':114972,'resource_acceptance_not_checked_here':True,'matrix_computed':False};(p/'SUMMARY.json').write_text(json.dumps(summary));m.summary(p/'SUMMARY.json',accepted);count+=1
 # Concrete post-schema corruptions retain source result hash where applicable by changing separate files.
 for name,change in [('PARTIAL.json',lambda x:x.update(rows=[])),('PANELS/00.json',lambda x:x['cumulative']['0'].__setitem__(0,['1','1'])),('WORKER_COMPLETE.json',lambda x:x.update(seconds=float('nan'))),('POLES/00.json',lambda x:x.update(status='INDETERMINATE'))]:
  q=p/'SHARD_00'/name;raw=q.read_bytes();d=json.loads(raw);change(d);q.write_text(json.dumps(d))
  try:m.shard(p/'SHARD_00',0,poles,'f','b',.3)
  except ValueError:count+=1
  else:raise ValueError('corruption accepted '+name)
  q.write_bytes(raw)
 for row in [dict(accepted[0]['rows'][0],target='1'),dict(accepted[0]['rows'][1],status='CERTIFIED_TARGET')]:
  try:m.check_row(row,row['id'],poles[row['id']])
  except ValueError:count+=1
  else:raise ValueError('row corruption accepted')
print(json.dumps({'status':'PASS_SYNTHETIC_SCHEMA','checks':count,'physical_calls':0,'scope':'11 synthetic shards include INDETERMINATE; six corruptions reject; no process launch'},indent=2))
