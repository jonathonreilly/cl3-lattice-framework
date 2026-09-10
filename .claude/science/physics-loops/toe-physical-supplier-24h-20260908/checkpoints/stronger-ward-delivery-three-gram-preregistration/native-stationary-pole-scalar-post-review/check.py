"""Post-hoc saved certificate validation. No imports of the oracle or worker."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math,re,signal
signal.alarm(25)
s=Path('/private/tmp/toe-24h-probes-20260908');p=s/'native-stationary-pole-scalar-batch-design';r=s/'native-stationary-pole-scalar-root-review';o=s/'native-stationary-pole-scalar-run-9845c';checks=0
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def req(x,label):
 global checks
 if not x:raise ValueError(label)
 checks+=1
req(sha(p/'FREEZE.json')=='9845c5473716c7477c0833e9741b531dda4f80ff74ece0c0f16a8e515a7c043d','sourcefreeze')
req(sha(o/'RESULT.json')=='bcf9237ac533d84406504bb6f6495b7952855b3545282060276a2e31271bf3ae','result binding')
req(sha(r/'run_once.py')=='b3d851804aa7745874c32a32f4d6aedec36c6653f73efaab97bbeaf4dca58e52','original failed monitor')
f=json.loads((p/'FREEZE.json').read_text())
for k,v in f['inputs'].items():req(sha(Path(k))==v,'pin '+k)
d=json.loads((o/'RESULT.json').read_text());w=json.loads((o/'WORKER_COMPLETE.json').read_text());rr=json.loads((r/'RECEIPT.json').read_text());ps=json.loads((p/'POLES.json').read_text())['rows'];partial=json.loads((o/'PARTIAL.json').read_text())
req(w['status']=='COMPLETE' and w['freeze_sha256']==sha(p/'FREEZE.json') and w['result_sha256']==sha(o/'RESULT.json'),'completion')
req(d['status']=='COMPLETE_FIXED_66_ORACLES' and d['B_computed'] is False and d['matrix_computed'] is False and d['alpha_computed'] is False,'scope')
req(len(d['rows'])==len(ps)==66,'66 rows');widthmax={k:F(0) for k in ('A','Aprime')}
for i,(row,pole) in enumerate(zip(d['rows'],ps)):
 req(row['id']==i and row['pole']==pole and row['gate']=='PASS','pole row')
 a=row['oracle'];req(F(a['s'])==F(pole['s_midpoint']) and a['status']=='CERTIFIED_TARGET' and a['terms']==160 and a['derivative_side']=='ordinary','oracle identity')
 req(len(a['widths'])==2,'width shape')
 lo,hi=map(F,pole['s_interval']);req(F(pole['A_midpoint_inflation'])==(hi-lo)/6 and F(pole['Aprime_midpoint_inflation'])==3*(hi-lo)/lo**4,'independent inflation')
 for k,inf,j in [('A','A_midpoint_inflation',0),('Aprime','Aprime_midpoint_inflation',1)]:
  req(len(a[k])==len(row[k+'_whole_bracket'])==2,'endpoint shape');l,u=map(F,a[k]);req(0<=u-l==F(a['widths'][j])<=F(1,10**30),'original precision')
  x,y=map(F,row[k+'_whole_bracket']);e=F(pole[inf]);req((x,y)==(l-e,u+e),'whole bracket');req(x>0 if k=='A' else y<0,'sign');widthmax[k]=max(widthmax[k],y-x)
 req(isinstance(row['seconds'],(int,float)) and math.isfinite(row['seconds']) and 0<row['seconds']<=d['seconds'],'actual row clock')
req(partial['rows']==d['rows'],'all partial rows retained')
for t in [d['seconds'],w['seconds'],rr['seconds']]:req(isinstance(t,(int,float)) and math.isfinite(t) and 0<t<30,'finite resource clock')
req(d['seconds']<=w['seconds']<=rr['seconds'],'nested times')
req(rr['pass'] is False and rr['failure']=="KeyError('seconds')" and rr['returncode']==0,'original failure retained')
shell=(r/'ROOT.stderr').read_text();real=re.findall(r'^real\s+(\d+(?:\.\d+)?)$',shell,re.M);rss=re.findall(r'^\s*(\d+)\s+maximum resident set size$',shell,re.M);req(len(real)==len(rss)==1,'shell receipt schema');t=F(real[0]);mem=int(rss[0]);req(0<t+F(1,100)<=30,'shell conservative elapsed');req(rr['seconds']<=float(t)+.01,'outer reconciliation')
for m in [mem,w['rss_bytes'],rr['sampled_whole_tree_peak']]:req(isinstance(m,int) and 0<m<=384*1048576,'memory bound')
req(sum(row['seconds'] for row in d['rows'])<=d['seconds'],'oracle sum accounting')
print(json.dumps({'status':'PASS_COMPLETED_WORKER_SAVED_CERTIFICATES','original_monitor_pass':False,'original_monitor_failure':rr['failure'],'checks':checks,'rows':66,'source_freeze':sha(p/'FREEZE.json'),'result_sha256':sha(o/'RESULT.json'),'whole_bracket_max_widths':{k:str(v) for k,v in widthmax.items()},'external_conservative_seconds':str(t+F(1,100)),'sampled_tree_peak_bytes':rr['sampled_whole_tree_peak'],'oracle_calls':0,'resource_note':'sampled tree and shell receipts, not continuous RSS','scope':'post-hoc independent certificate check; no oracle arithmetic reevaluation'},indent=2))
