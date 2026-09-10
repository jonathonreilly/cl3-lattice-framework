"""Saved-only all11/all66 reconciliation. No contractions or oracle calls."""
import json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
ap=argparse.ArgumentParser();ap.add_argument('study');ap.add_argument('source_freeze_sha256');ap.add_argument('binding_sha256');ap.add_argument('output');args=ap.parse_args()
out=Path(args.output)
if out.exists():raise ValueError('fresh summary')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[];receipts=[];current=None
try:
 for j in range(11):
  current=j;p=Path(args.study)/f'SHARD_{j:02d}';w=json.loads((p/'WORKER_COMPLETE.json').read_text());r=json.loads((p/'RESULT.json').read_text())
  if w['status']!='COMPLETE' or w['shard']!=j or w['freeze_sha256']!=args.source_freeze_sha256 or w['binding_sha256']!=args.binding_sha256 or w['result_sha256']!=sha(p/'RESULT.json'):raise ValueError('shard binding')
  ids=list(range(6*j,6*j+6))
  if r['status']!='COMPLETE_FIXED_CASES' or r['selected_ids']!=ids or [x['id'] for x in r['rows']]!=ids or r['pairs']!=10452:raise ValueError('fixed shard census')
  for x in r['rows']:
   widths=[F(x[k][1])-F(x[k][0]) for k in ('B','Bprime')]
   if any(w<0 for w in widths) or widths!=list(map(F,x['widths'])):raise ValueError('width arithmetic')
   status='CERTIFIED_TARGET' if max(widths)<=F(2,10**19) else 'INDETERMINATE'
   if x['status']!=status:raise ValueError('target classification')
   rows.append(x)
  receipts.append({'shard':j,'worker_sha256':sha(p/'WORKER_COMPLETE.json'),'result_sha256':sha(p/'RESULT.json')})
 if [r['id'] for r in rows]!=list(range(66)):raise ValueError('complete66')
 out.write_text(json.dumps({'status':'COMPLETE_FIXED_11_SHARDS','rows':rows,'receipts':receipts,'all_targets_met':all(r['status']=='CERTIFIED_TARGET' for r in rows),'pairs':114972,'resource_acceptance_not_checked_here':True,'matrix_computed':False},indent=2)+'\n')
except BaseException as e:
 out.write_text(json.dumps({'status':'FAILED_RECONCILIATION','current_shard':current,'rows':rows,'receipts':receipts,'error':repr(e)},indent=2)+'\n');raise
