#!/usr/bin/env python3
"""Compact immutable evidence checks; no native acquisition or coefficient replay."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
P=Path(__file__).resolve().parents[1]/'.claude/science/physics-loops/native-global-projector-certificate-20260910'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--json',action='store_true');ap.parse_args()
 n=0
 def check(ok,label):
  nonlocal n
  if not ok:raise ValueError(label)
  n+=1
 pins=json.loads((P/'IMPORT_PROVENANCE.json').read_text())
 for name,row in pins.items():check(sha(P/name)==row['sha256'],'import '+name)
 read=lambda d,f:json.loads((P/'receipts'/d/f).read_text())
 d='native-global-projector-coefficient-run-prospective';r=read(d,'RESULT.json');ledger=r['ledger'];root=read('native-global-projector-coefficient-root-review','ROOT_ACCEPTANCE.json');schema=read('native-global-projector-coefficient-root-review','SCHEMA_ACCEPTANCE.json')
 check(root['result_sha256']==schema['result_sha256']==sha(P/'receipts'/d/'RESULT.json'),'result lineage')
 check(root['schema_sha256']==sha(P/'receipts/native-global-projector-coefficient-root-review/SCHEMA_ACCEPTANCE.json'),'schema lineage')
 check(root['once'] is True and root['independent_coefficient_reconciliation'] is True,'root scope')
 check(r['nodes']==schema['count']==378 and r['coefficient_blocks']==root['blocks']==schema['coefficient_blocks']==756,'node/block census')
 check(r['events']==schema['events']==root['events']==3407,'event census')
 check(r['native_oracle_calls']==0 and r['physical_columns_evaluated'] is False and r['gaussian_consumer_certified'] is False,'actual scope')
 check(root['gaussian_consumer_certified'] is False and schema['native_oracle_replay'] is False,'inherited truth')
 total=F(ledger['total_error']);check(total==F(root['total_error'])==F(schema['total_error']),'total copies')
 low=F(2,9)*F(5439,160)*F(1,2**48)+F(1,6)*F(867,32)*F(1,2**64)
 high=F(1,8)*F(9,64)**15*(1+F(18,64*33));quad=6139*F(4,25)**21
 check(total==low+high+quad+F(ledger['input_error']),'analytic sum')
 check(F(ledger['input_error'])>=0 and 0<total<F(2,10**13),'certified error')
 check(4*378+2+(4*15-2)==1572,'rank bound')
 check(root['external_seconds']==4.73 and root['external_seconds']<120,'external wall')
 check(0<root['external_rss_bytes']<384*1024**2 and 0<root['sampled_whole_tree_peak']<384*1024**2,'external memory')
 a=read('native-global-a378-root-review','ROOT_ACCEPTANCE.json');check(a['status']=='ACCEPTED_NEW_A378_ACQUISITION_ONCE' and a['points']==378 and a['all_A_width_gates'] is True,'A once')
 recovery=json.loads((P/'REMOTE_RECOVERY_MAP.json').read_text());events=[v for k,v in recovery.items()if k.endswith('/EVENTS.ndjson')]
 check(len(events)==1 and events[0]['sha256']==schema['events_sha256'],'event recovery')
 checkpoints=[json.loads((P/'receipts'/f'CHECKPOINT{x}_REMOTE_VERIFICATION.json').read_text())for x in (78,79)]
 check(all(x['sha256_and_remote_git_blob_match'] is True for x in checkpoints),'remote verification')
 check(root['preregistration_commit']==checkpoints[0]['head'],'coefficient preregistration')
 print(json.dumps({'status':'PASS_COMPACT_EVIDENCE_ONLY','predicates':n,'total_error_upper_approx':float(total),'rank_upper':1572,'native_reruns':0,'full_alpha_established':False},indent=2))
if __name__=='__main__':main()
