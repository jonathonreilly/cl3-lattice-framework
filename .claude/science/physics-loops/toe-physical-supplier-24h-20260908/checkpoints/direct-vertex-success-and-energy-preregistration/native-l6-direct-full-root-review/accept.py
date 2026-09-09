from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,math
R=Path(__file__).resolve().parent;B=R.parent;O=B/'native-l6-direct-full-run-4060';P=B/'native-l6-direct-four-solve-runtime-package';Q=B/'native-l6-direct-four-solve-replay';limit=384*1048576
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
assert sha(R/'ROOT_FREEZE.json')=='e4a72e2956d296d80c5b11db6e10c558fee8479a6f1c042300fffd5c5908fcae'
rf=json.loads((R/'ROOT_FREEZE.json').read_text())
for n,h in rf['files'].items():assert sha(R/n)==h,n
assert sha(P/'ROOT_AUTHORIZATION.json')==rf['production_authorization_sha256']
counts=[]
for folder,name,h in ((P,'RUN_FREEZE.json','4060a2b4ff1bf2d7316677acf034b6ab9be8c82fcb3c13ed9095f99444c891e2'),(Q,'FREEZE.json','2956446eb32d8a9dfa24307329f244d762830b864fa26a2ce0a71233ae21fc34')):
 assert sha(folder/name)==h;f=json.loads((folder/name).read_text())
 for n,k in f['inputs'].items():assert sha(n)==k,n
 counts.append(len(f['inputs']))
text=(R/'ROOT_SHELL.stderr').read_text();wall=float(re.findall(r'^real\s+([0-9.]+)\s*$',text,re.M)[-1]);rss=int(re.findall(r'^\s*(\d+)\s+maximum resident set size\s*$',text,re.M)[-1]);assert math.isfinite(wall) and 0<wall<346 and wall+14<360 and 0<rss<=limit
complete=json.loads((R/'COMPLETE.json').read_text());assert complete['status']=='PASS_EXTERNAL_SHELL_PENDING'
peak=0
for n,cap in [('production',180),('replay',150)]:
 c=json.loads((R/(n+'.RECEIPT.json')).read_text());assert c['pass'] is True and c['returncode']==0 and 0<c['external_seconds']<cap and 0<c['external_rss']<=limit and 0<c['aggregate_peak']<=limit;peak=max(peak,c['aggregate_peak'])
assert not (R/'FAILED.json').exists()
manifest=json.loads((R/'PRODUCTION_MEMBERSHIP.json').read_text());actual={str(f.relative_to(O/'production')):sha(f) for f in (O/'production').rglob('*') if f.is_file()};assert actual==manifest
result=json.loads((O/'production/RESULT.json').read_text());review=json.loads((O/'replay/REVIEW.json').read_text());wc=json.loads((O/'production/WORKER_COMPLETE.json').read_text());assert wc['result_sha256']==sha(O/'production/RESULT.json');assert review['input_result_sha256']==wc['result_sha256'] and review['worker_complete_sha256']==sha(O/'production/WORKER_COMPLETE.json')
assert result['passes_Echi'] is True and review['scientific_pass'] is True and review['status']=='PASS';assert result['Echi']==review['Echi'] and result['particle_intervals']==review['particle_intervals'];assert 0<=F(result['Echi'])<=F(1,10**6)
for name,c in result['representative_certificates'].items():assert F(c['candidate_attempts'])==1 and F(c['rho'])<=(F(1,10**10) if name.startswith('first') else F(1,10**9))
assert all(F(v[0])<=F(v[1]) for v in result['particle_intervals'].values())
a=dict(accepted=True,status='PASS',external_seconds=wall,prior_seconds=14,total_charged_seconds=wall+14,root_external_rss=rss,observed_whole_tree_rss=peak,source_pin_counts=counts,root_freeze=sha(R/'ROOT_FREEZE.json'),production_source_freeze=sha(P/'RUN_FREEZE.json'),replay_source_freeze=sha(Q/'FREEZE.json'),production_contract_sha256=sha(P/'CONTRACT.json'),production_result_sha256=sha(O/'production/RESULT.json'),independent_replay_sha256=sha(O/'replay/REVIEW.json'),worker_complete_sha256=sha(O/'production/WORKER_COMPLETE.json'),Echi=result['Echi'],particle_intervals=result['particle_intervals'],immutable_production_files=len(actual),scope='Finite supplied native L6 star vertex; floating operation and imported model assumptions remain. Not full sixth order or bulk physics.')
(R/'ACCEPTANCE.json').write_text(json.dumps(a,indent=2)+'\n');print(json.dumps({k:a[k] for k in ('accepted','external_seconds','total_charged_seconds','observed_whole_tree_rss','source_pin_counts','immutable_production_files')}));print('acceptance_sha256',sha(R/'ACCEPTANCE.json'))
