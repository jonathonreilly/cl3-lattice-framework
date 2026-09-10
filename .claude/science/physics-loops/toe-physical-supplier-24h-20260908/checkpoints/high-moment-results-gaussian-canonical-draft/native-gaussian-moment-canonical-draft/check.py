"""Portable semantic certificate check; no native/event arithmetic replay."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math,copy
P=Path(__file__).resolve().parent
N=0
def need(x,m):
 global N
 if not x:raise ValueError(m)
 N+=1
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def integer(x,n):need(type(x)is int and x==n,'literal count')
def rational(x):
 need(type(x)is str and len(x)<20000,'rational string');v=F(x);need(str(v)==x,'canonical rational');return v
def interval(x):
 need(type(x)is list and len(x)==2,'interval shape');a,b=map(rational,x);need(a<=b,'ordered interval');return a,b
def duration(x,cap):need(type(x)in(int,float)and math.isfinite(x)and 0<x<cap,'duration')
def memory(x):need(type(x)is int and 0<x<=384*1048576,'memory')
def validate(tag,r,a,w,receipt,runtime,root,result_hash):
 cap=60 if tag=='high' else 30
 need(a['result_sha256']==result_hash==w['result_sha256'],'result identity')
 need(a['worker_freeze']==receipt['worker_freeze']==w['runtime_sha256'],'worker identity')
 need(a['once']is True and receipt['pass']is True and receipt['failure']is None,'accepted once')
 integer(receipt['returncode'],0);duration(a['external_seconds'],cap);duration(receipt['seconds'],cap-.5);duration(w['seconds'],cap-1);memory(a['external_rss_bytes']);memory(a['sampled_whole_tree_peak']);memory(w['rss_bytes'])
 need(receipt['sampled_whole_tree_peak']==a['sampled_whole_tree_peak'],'tree receipt');need(a['schema']['result_sha256']==result_hash,'schema identity')
 need(a['output_hashes']['RESULT.json']==result_hash,'output result');need(root['worker_freeze']==a['worker_freeze'],'root worker');need(runtime['execution_enabled']is True and root['execution_enabled']is True,'executed source')
 need(len(r['rows'])==2,'two rows')
 need(w['status']==('COMPLETE_NEW_HIGH_MOMENTS_ONLY' if tag=='high' else 'COMPLETE_NEW_OMEGA79_ONLY'),'worker status')
 need(a['schema']['status']==('PASS_INDEPENDENT_HIGH_JET_ARITHMETIC' if tag=='high' else 'ACCEPTED_NEW_OMEGA79_SCHEMA'),'schema status')
 need(r['seconds']<=w['seconds']<=receipt['seconds']<=a['external_seconds'],'resource chronology')
 if tag=='high':
  need(a['status']=='ACCEPTED_NEW_NATIVE_HIGH_MOMENT_PILOT_ONCE'and r['status']=='COMPLETE_NEW_HIGH_MOMENT_PILOT','high status')
  integer(r['events'],189);integer(r['first_order'],7);integer(r['native_lower_moments_recomputed'],0);integer(r['native_oracle_calls'],0)
  need(a['schema']['new_jet_arithmetic_reconciled']is True and a['schema']['lower_native_replay']is False,'independent scope');integer(a['schema']['events'],189);integer(a['schema']['count'],2)
  need(r['scope']=='only m7..10; absolute width pilot, no downstream Ward sufficiency','pilot scope')
  need([x['kind']for x in r['rows']]==['P','O'],'class order')
  for row in r['rows']:
   need(row['orders']==[7,8,9,10]and all(type(x)is int for x in row['orders']),'orders');need(row['status']=='CERTIFIED_PILOT_WIDTH'and row['width_gate']is True,'width status');need(rational(row['target_full_width'])==F(1,10**6),'fixed target')
   need(set(row['moments'])==set(row['widths'])==set(row['real_width_grid_units'])=={'7','8','9','10'},'moment census')
   for k,z in row['moments'].items():
    need(len(z)==2 and all(len(x)==2 and all(type(v)is int for v in x)and x[0]<=x[1]for x in z),'fixed grid boxes');need(z[1][0]<=0<=z[1][1],'real moments');need(type(row['real_width_grid_units'][k])is int and row['real_width_grid_units'][k]==z[0][1]-z[0][0],'stored width');width=rational(row['widths'][k]);need(width==F(z[0][1]-z[0][0],2**256)and 0<=width<=F(1,10**6),'width semantics')
 else:
  need(a['status']=='ACCEPTED_NEW_OMEGA79_ONCE'and r['status']=='COMPLETE_NEW_OMEGA79','omega status')
  for key,num in [('nodes',1742),('panels',67),('oracle_calls',0),('endpoint_oracles_reused',3484),('tail_terms_each',40)]:integer(r[key],num)
  need(a['schema']['independent_node_tail_final_arithmetic']is True,'omega review scope')
  need([x['observable']for x in r['rows']]==['omega7','omega9'],'observable census')
  for row,target in zip(r['rows'],[F(1,10**22),F(1,10**20)]):
   need(row['status']=='CERTIFIED_TARGET'and row['middle_width_gate']is True and row['weighted_power_gate']is True,'omega gates');lo,hi=interval(row['interval']);need(rational(row['target'])==target and rational(row['width'])==hi-lo<=target,'omega width')

def main():
 imports=json.loads((P/'IMPORTS.json').read_text())
 for name,entry in imports.items():need(sha(P/name)==entry['sha256'],'import '+name)
 packets=[]
 for tag in ['omega','high']:
  rd=lambda name:json.loads((P/tag/name).read_text())
  args=[tag,rd('RESULT.json'),rd('ROOT_ACCEPTANCE.json'),rd('WORKER_COMPLETE.json'),rd('RECEIPT.json'),rd('RUNTIME_FREEZE.json'),rd('ROOT_FREEZE.json'),sha(P/tag/'RESULT.json')]
  need(sha(P/tag/'ROOT_FREEZE.json')==args[2]['root_freeze'],'root source hash');need(sha(P/tag/'RUNTIME_FREEZE.json')==args[2]['worker_freeze'],'worker source hash')
  for name in ['RESULT.json','WORKER_COMPLETE.json','STARTED.json','PARTIAL.json']:
   need(sha(P/tag/name)==args[2]['output_hashes'][name],'accepted compact output')
  if tag=='high':
   for name in ['EVENTS.ndjson','TABLES.json']:need(sha(P/tag/name)==args[2]['output_hashes'][name],'opaque retained output')
  start=rd('STARTED.json');need(start['runtime_sha256']==args[2]['worker_freeze'] and start['binding_sha256']==args[3]['binding_sha256'] and start['no_retry']is True,'start binding')
  need(start['output']==args[6]['authorization']['output'],'authorized output')
  need(sha(P/tag/'BINDING.json')==args[3]['binding_sha256'],'binding bytes')
  partial=rd('PARTIAL.json');duration(partial['seconds'],59 if tag=='high' else 29);need(args[1]['seconds']<=partial['seconds']<=args[3]['seconds'],'partial chronology')
  validate(*args);packets.append(args)
 # Hash-coherent mutations bypass static pins deliberately to exercise semantics.
 mutants=0
 for mut in ['false_accept','bool_count','reversed','false_scope','oversize_rss']:
  q=copy.deepcopy(packets[1])
  if mut=='false_accept':q[2]['status']='ACCEPTED_ALPHA_SIGN'
  if mut=='bool_count':q[1]['first_order']=True
  if mut=='reversed':q[1]['rows'][0]['moments']['7'][0].reverse()
  if mut=='false_scope':q[1]['scope']='certified Ward sign'
  if mut=='oversize_rss':q[3]['rss_bytes']=True
  try:validate(*q)
  except ValueError:mutants+=1
  else:raise ValueError('surviving semantic mutant '+mut)
 # Exact synthetic half-log identity: sqrt(det(exp(t I_2)))=exp(t).
 # Euler reconstruction from ell_1=1, ell_n=0 has coefficients 1/n!.
 z=[F(1)]
 for n in range(1,11):z.append(z[-1]/n);need(z[n]==F(1,math.factorial(n)),'half-log coefficient')
 wrong=[F(1)]
 for n in range(1,4):wrong.append(2*wrong[-1]/n)
 need(wrong[1]!=z[1],'missing half mutant')
 print(json.dumps({'status':'PASS_COMPACT_ONLY','checks':N,'semantic_mutants_rejected':mutants,'algebra_mutants_rejected':1,'native_replays':0,'event_arithmetic_replays':0}))
if __name__=='__main__':main()
