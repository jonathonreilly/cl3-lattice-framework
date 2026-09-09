#!/usr/bin/env python3
"""Compact exact identities and saved-certificate binding; no oracle/full-node replay."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
V=ROOT/'.claude/science/physics-loops/native-rho4-moment-certificates-20260909/verification'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(folder,name):return json.loads((V/'evidence'/folder/name).read_text())
def residual(x,t,q,m):
 return x**q/(x+t*t)-sum(((-1)**n*x**(n+q)/t**(2*n+2)for n in range(m)),F(0))
def nu_polynomial(x,t):return x-t*t+t**4/(x+t*t)
def certificate(row,target):
 if type(row.get('interval'))is not list or len(row['interval'])!=2 or any(type(x)is not str for x in row['interval']):raise ValueError('two endpoints')
 lo,hi=map(F,row['interval'])
 if not 0<lo<=hi or F(row['width'])!=hi-lo or F(row['target'])!=target or hi-lo>target or row['status']!='CERTIFIED_TARGET':raise ValueError('fixed target interval')
 return lo,hi

def run():
 count=0
 def check(x):
  nonlocal count
  if not x:raise ValueError('predicate '+str(count))
  count+=1
 manifest=json.loads((V/'SOURCE_MANIFEST.json').read_text())
 for path,digest in manifest.items():check(sha(ROOT/path)==digest)
 recovery=json.loads((V/'RECOVERY_MANIFEST.json').read_text())
 for x in recovery['local_copies']:
  check(bool(x['recovery_paths']));check(sha(ROOT/x['local'])==x['sha256'])
 for x in recovery['archive_manifests']:check(sha(ROOT/x['local'])==x['sha256'])
 # Exact formula controls on three synthetic atoms, not native catalog evaluations.
 check(F(9,4)-F(514,256)==F(31,128)>0)
 check(F(16,3)*8*6==256);check(F(16,3)*8*F(17,60)==F(544,45))
 check(F(1,12)+F(1,54)+2<3) # pi>3 derivative bound
 for x in (F(1,3),F(2),F(11)):
  for t in (F(1,7),F(3),F(8)):
   check(nu_polynomial(x,t)==x*x/(x+t*t))
   for q in (0,1,2):
    for m in (2,4):check(residual(x,t,q,m)==x**(m+q)/(t**(2*m)*(x+t*t)))
 # Actual semantic alternatives rejected: wrong geometric sign and omitted subtraction.
 check(any(residual(x,F(8),0,2)!=-x*x/(F(8)**4*(x+64))for x in (F(1),F(2))))
 check(any(x+F(3)**4/(x+9)!=x*x/(x+9)for x in (F(1),F(2))))
 # Tiny torus moment identities, not M0..M41 regeneration.
 check(3*2==6);check(3*6+6*2*2==42)
 nu=read('native-nu-catalog-run-3ac6','RESULT.json');dual=read('native-rho4-two-moment-run-442f','RESULT.json')
 check(dual['status']=='COMPLETE_NEW_RHO4_TWO_MOMENT_CERTIFICATE');check(dual['all_targets_met'] is True)
 check(len(dual['rows'])==2 and [r['observable']for r in dual['rows']]==['cminus','mu'])
 results={r['observable']:certificate(r,F(2,10**28))for r in dual['rows']};results['nu']=certificate(nu,F(2,10**19))
 check(nu['middle_width_gate'] is True)
 check(json.loads((V/'SCALARS.json').read_text())['rows']==dual['rows']+[nu])
 for obj in (nu,dual):
  for field,value in [('panels',67),('nodes',1742),('tail_terms',40),('oracle_calls',0)]:check(type(obj[field])is int and obj[field]==value)
 for kind,producer,postrun,root,poststatus in (
  ('nu','native-nu-catalog-run-3ac6','native-nu-full-node-saved-run-4f93','native-nu-catalog-root-review','ACCEPTED_NU_EXECUTION_AND_FULL_SAVED_NODE_RECONSTRUCTION'),
  ('dual','native-rho4-two-moment-run-442f','native-rho4-two-moment-saved-run-3b86','native-rho4-two-moment-root-review','ACCEPTED_RHO4_TWO_MOMENT_CERTIFICATES_AND_ALL_SAVED_NODES')):
  r=read(producer,'RESULT.json');w=read(producer,'WORKER_COMPLETE.json');a=read(root,'ROOT_ACCEPTANCE.json');p=read(root,'POST_ACCEPTANCE.json');q=read(postrun,'RESULT.json')
  rh=sha(V/'evidence'/producer/'RESULT.json');ph=sha(V/'evidence'/postrun/'RESULT.json')
  check(w['result_sha256']==a['result_sha256']==p['result_sha256']==q['source_result_sha256']==rh)
  check(p['status']==poststatus and p['post_result_sha256']==ph)
  check(w.get('runtime_sha256',w.get('freeze_sha256'))==a['worker_freeze']==p['worker_freeze'])
  check(q['saved_nodes_reconstructed']==1742 and type(q['saved_nodes_reconstructed'])is int and q['panels']==67 and q['oracle_calls']==0)
  if kind=='nu':check(q['interval']==r['interval'] and q['status']=='PASS_SAVED_RECONSTRUCTION')
  else:check(q['status']=='PASS_SAVED_TWO_MOMENT_RECONSTRUCTION' and len(q['rows'])==2 and [z['interval']for z in q['rows']]==[z['interval']for z in r['rows']])
  check(0<F(str(a['external_seconds']))<=30 and 0<a['sampled_whole_tree_peak']<=384*1048576)
  check(0<F(str(p['post_external_seconds']))<=30 and 0<p['post_sampled_whole_tree_peak']<=384*1048576)
 for name,lo,hi,width in [('cminus',F('0.4553440516444301'),F('0.4553440516444302'),F('8e-31')),('mu',F('2.387'),F('2.389'),F('3e-30')),('nu',F('15.645'),F('15.647'),F('2e-29'))]:
  a,b=results[name];check(lo<a<=b<hi and b-a<width)
 # Actual altered saved-row guards, no raw computation.
 row=dict(dual['rows'][0]);mutants=[]
 for field,value in [('target','1'),('width','0'),('interval',row['interval'][:1]),('interval',[True,True])]:
  changed={**row,field:value}
  try:certificate(changed,F(2,10**28))
  except (ValueError,TypeError,KeyError):mutants.append(field)
  else:raise ValueError('mutant survived '+field)
 check(len(mutants)==4)
 return {'status':'PASS_COMPACT_IDENTITIES_AND_SAVED_BINDINGS','checks':count,'semantic_mutants_rejected':['wrong geometric remainder sign','nu subtraction omitted']+mutants,'scalar_intervals':{k:list(map(str,v))for k,v in results.items()},'full_node_replays':0,'oracle_calls':0,'integration':'NOT_RUN','audit':'NOT_RUN'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');a=p.parse_args();r=run()
 if a.json:print(json.dumps(r,indent=2))
 else:print('TOTAL: PASS=%d FAIL=0'%r['checks']);print(json.dumps(r,sort_keys=True))
if __name__=='__main__':main()
