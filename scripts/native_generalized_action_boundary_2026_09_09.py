#!/usr/bin/env python3
"""Compact exact checks only; not archived native matrix replay."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parents[1]/'.claude/science/physics-loops/native-generalized-action-boundary-20260909'
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--json',action='store_true');args=ap.parse_args();d=json.loads((P/'EXACT_SUMMARY.json').read_text());n=0
 def check(x):
  nonlocal n
  if not x:raise ValueError('compact predicate '+str(n))
  n+=1
 root=json.loads((P/'receipts/SELECTED_ROOT.json').read_text());check(d['selected']==root['orbits'])
 archive=json.loads((P/'ARCHIVE_MANIFEST.json').read_text())['inputs']
 original=[]
 for i in range(5):
  source=json.loads((P/f'receipts/GENERALIZED_ORBIT_{i}.json').read_text())
  check(hashlib.sha256((P/f'receipts/GENERALIZED_ORBIT_{i}.json').read_bytes()).hexdigest()==archive[f'/private/tmp/toe-24h-probes-20260908/native-coordinate-free-run-prospective/ORBIT_{i}/RESULT.json'])
  check(source['status']=='COMPLETE_SOURCE_ONLY_ALGEBRA' and len(source['results'])==2 and source['C_width_gate_required']is False)
  for imp,v in zip((399,400),source['results']):original.append({'orbit':i,'impurity':imp,**v})
 check(d['generalized']==original)
 post=json.loads((P/'receipts/GENERALIZED_POST.json').read_text());saved=json.loads((P/'receipts/GENERALIZED_SAVED_RESULT.json').read_text())
 digest=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
 check(post['status']=='ACCEPTED_FIRST_GENERALIZED_24_ACTION_AND_ALL_SAVED_STAGES');check(post['post_result_sha256']==digest(P/'receipts/GENERALIZED_SAVED_RESULT.json'));check(post['original_root_acceptance_sha256']==digest(P/'receipts/GENERALIZED_ROOT.json'));check(post['native_entry_truth_inherited']is True);check(len(saved['rows'])==5)
 compact=json.loads((P/'COMPACT_INPUTS.json').read_text())
 for name,h in compact.items():check(digest(P/name)==h)
 recovery=json.loads((P/'REMOTE_RECOVERY_MAP.json').read_text());platform=json.loads((P/'PLATFORM_RUNTIME_PINS.json').read_text())['inputs']
 check(not recovery['unmapped']);check(set(archive)==set(recovery['mapped'])|set(platform));check(not(set(recovery['mapped'])&set(platform)))
 for original,entry in recovery['mapped'].items():check(entry['sha256']==archive[original] and len(entry['commit'])==40 and entry['path'].startswith('.claude/science/physics-loops/'))
 selected_post=json.loads((P/'receipts/SELECTED_POST.json').read_text());generalized_root=json.loads((P/'receipts/GENERALIZED_ROOT.json').read_text())
 check(selected_post['status']=='ACCEPTED_DIRECT_SELECTED_PRINCIPAL_AND_SAVED_MATRICES');check(selected_post['original_root_acceptance_sha256']==digest(P/'receipts/SELECTED_ROOT.json'));check(selected_post['result_sha256']==root['result_sha256'])
 check(post['result_sha256']==generalized_root['result_sha256']);check(post['worker_freeze']==generalized_root['worker_freeze']);check(post['root_freeze']==generalized_root['root_freeze'])
 check(len(d['selected'])==5);check(len(d['generalized'])==10)
 for i,r in enumerate(d['selected']):
  check(type(r['orbit'])is int and r['orbit']==i);check(0<=F(r['e'])<F(8,10**6));check(r['width_pass']is False);check(r['l1_pass']is True)
 for j,r in enumerate(d['generalized']):
  check((r['orbit'],r['impurity'])==(j//2,(399,400)[j%2]));check(r['status']=='CERTIFIED_GENERALIZED_LEAKAGE_BOUND');check(F(r['delta_squared_lower'])>F(53,100));check(F(r['delta_squared_upper'])>=F(r['delta_squared_lower']));check(r['target_excluded']is True);check(r['leakage_pass']is False);check(F(r['target_squared'])==F(1,10**12))
 # W=(2,0), K=[[0,-3],[3,0]]. H=4,A=0,Z=36; normalized leakage9.
 H,A,Z=F(4),F(0),F(36);N=Z+A*A/H;check(N/H==9);check(N>=0)
 print(json.dumps({'status':'PASS_COMPACT_EXACT_SUPPORT','predicates':n,'native_matrix_replay':False,'generalized_saved_post':d['generalized_saved_post']},indent=2))
if __name__=='__main__':main()
