"""Saved-only fixed B66 receipt/schema checks. No contractions."""
import json,math,hashlib
from pathlib import Path
from fractions import Fraction as F
TARGET=F(2,10**19);LIMIT=384*1048576

def req(x,msg):
 if not x:raise ValueError(msg)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def read(p):return json.loads(Path(p).read_text())
def positive(t):return isinstance(t,(int,float)) and math.isfinite(t) and t>0
def interval(x):
 req(isinstance(x,list) and len(x)==2,'two interval endpoints');a,b=map(F,x);req(a<=b,'ordered interval');return a,b
def rounded_sum(x,y):
 S=1<<192;a=x[0]+y[0];b=x[1]+y[1];return F((a*S).__floor__(),S),F((b*S).__ceil__(),S)
def check_row(row,i,pole):
 req(row['id']==i and F(row['s_midpoint'])==F(pole['s_midpoint']),'pole midpoint');req(F(row['target'])==TARGET,'fixed precision target');req(len(row['widths'])==2,'two widths')
 widths=[]
 for name,w in zip(('B','Bprime'),row['widths']):
  a,b=interval(row[name]);req(b-a==F(w),'exact width');widths.append(b-a)
 status='CERTIFIED_TARGET' if max(widths)<=TARGET else 'INDETERMINATE';req(row['status']==status,'precision classification');return status

def shard(path,j,poles,pf,bf,elapsed):
 path=Path(path);r=read(path/'RESULT.json');w=read(path/'WORKER_COMPLETE.json');part=read(path/'PARTIAL.json');ids=list(range(6*j,6*j+6))
 req(w['status']=='COMPLETE' and w['shard']==j and w['freeze_sha256']==pf and w['binding_sha256']==bf and w['result_sha256']==sha(path/'RESULT.json'),'worker binding')
 req(r['status']=='COMPLETE_FIXED_CASES' and r['selected_ids']==ids and len(r['rows'])==6 and r['pairs']==10452,'shard census')
 req(r['exact_gauss_root_values'] is False and r['midpoint_displacement_requires_separate_ledger'] is True and r['matrix_computed'] is False and r['alpha_computed'] is False,'scientific scope')
 statuses=[check_row(row,i,poles[i]) for row,i in zip(r['rows'],ids)];req(r['all_targets_met']==all(x=='CERTIFIED_TARGET' for x in statuses),'target summary')
 expectedpanels=[{'panel':k,'path':f'PANELS/{k+64:02d}.json'} for k in range(-64,3)]
 req(part['completed_panels']==expectedpanels and part['rows']==r['rows'] and part['stage']=='finish' and part['current']=={'pole':ids[-1]},'retained partial')
 req({x.name for x in (path/'PANELS').iterdir()}=={f'{k:02d}.json' for k in range(67)},'panel membership');req({x.name for x in (path/'POLES').iterdir()}=={f'{i:02d}.json' for i in ids},'pole membership')
 acc={str(i):[(F(0),F(0)),(F(0),F(0))] for i in ids}
 for k in range(-64,3):
  p=read(path/f'PANELS/{k+64:02d}.json');req(p['panel']==k and set(p['values'])==set(acc)==set(p['cumulative']),'panel identities')
  for i in acc:
   req(len(p['values'][i])==len(p['cumulative'][i])==2,'panel observable count')
   for z in (0,1):
    v=interval(p['values'][i][z]);c=interval(p['cumulative'][i][z]);req(c==rounded_sum(acc[i][z],v),'cumulative panel algebra');acc[i][z]=c
 for row in r['rows']:req(read(path/f"POLES/{row['id']:02d}.json")==row,'pole retained')
 req(all(positive(t) for t in (r['seconds'],w['seconds'],part['seconds'],elapsed)) and part['seconds']<=r['seconds']<=w['seconds']<=elapsed and elapsed<=180,'shard inclusive timing')
 req(isinstance(w['rss_bytes'],int) and 0<w['rss_bytes']<=LIMIT,'worker RSS')
 files={str(x.relative_to(path)):sha(x) for x in path.rglob('*') if x.is_file()};req(set(files)=={'RESULT.json','PARTIAL.json','WORKER_COMPLETE.json'}|{x['path'] for x in expectedpanels}|{f'POLES/{i:02d}.json' for i in ids},'complete output membership')
 return {'shard':j,'rows':r['rows'],'files':files,'all_targets_met':r['all_targets_met'],'worker_seconds':w['seconds']}

def summary(path,accepted):
 d=read(path);rows=[x for sh in accepted for x in sh['rows']];req(d['status']=='COMPLETE_FIXED_11_SHARDS' and d['rows']==rows and [x['id'] for x in rows]==list(range(66)),'summary complete66');req(d['pairs']==114972 and d['matrix_computed'] is False and d['resource_acceptance_not_checked_here'] is True,'summary scope');req(d['all_targets_met']==all(x['status']=='CERTIFIED_TARGET' for x in rows),'summary precision')
 req(d['receipts']==[{'shard':j,'worker_sha256':sh['files']['WORKER_COMPLETE.json'],'result_sha256':sh['files']['RESULT.json']} for j,sh in enumerate(accepted)],'summary receipt binding')
 return d
