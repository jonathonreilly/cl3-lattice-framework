from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,math
B=Path('/private/tmp/toe-24h-probes-20260908');R=B/'native-l6-direct-full-root-review';P=B/'native-l6-direct-four-solve-runtime-package';Q=B/'native-l6-direct-four-solve-replay';O=B/'native-l6-direct-full-run-4060';checks=0

def need(x,name):
 global checks
 if not x:raise ValueError(name)
 checks+=1

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(p):return json.loads(p.read_text())
for folder,name in ((P,'RUN_FREEZE.json'),(Q,'FREEZE.json')):
 f=read(folder/name)
 for name,h in f['inputs'].items():need(sha(Path(name))==h,'source pin')
f=read(R/'ROOT_FREEZE.json')
for n,h in f['files'].items():need(sha(R/n)==h,'root pin')
need(sha(P/'ROOT_AUTHORIZATION.json')==f['production_authorization_sha256'],'root auth')
need(not(R/'FAILED.json').exists(),'root failure absent')
complete=read(R/'COMPLETE.json');prod=read(O/'production/RESULT.json');replay=read(O/'replay/REVIEW.json');worker=read(O/'production/WORKER_COMPLETE.json');binding=read(R/'REPLAY_BINDING.json')
need(worker['source_freeze']==sha(P/'RUN_FREEZE.json') and worker['contract_sha256']==sha(P/'CONTRACT.json') and worker['result_sha256']==sha(O/'production/RESULT.json'),'worker binding')
need(binding=={'result_sha256':sha(O/'production/RESULT.json'),'worker_complete_sha256':sha(O/'production/WORKER_COMPLETE.json'),'production_source_freeze':sha(P/'RUN_FREEZE.json'),'production_contract_sha256':sha(P/'CONTRACT.json')},'input binding')
need(replay['source_freeze']==sha(Q/'FREEZE.json') and replay['input_binding_sha256']==sha(R/'REPLAY_BINDING.json') and replay['input_result_sha256']==sha(O/'production/RESULT.json') and replay['worker_complete_sha256']==sha(O/'production/WORKER_COMPLETE.json'),'replay binding')
need(complete['review_hash']==sha(O/'replay/REVIEW.json'),'complete binding')
snapshot=read(R/'PRODUCTION_MEMBERSHIP.json');now={str(p.relative_to(O/'production')):sha(p) for p in sorted((O/'production').rglob('*')) if p.is_file()};need(snapshot==now,'all immutable production files')
need(prod['algorithm']=='direct_gaussian_once' and prod['physical_global_phase']=='i','algorithm phase')
need(prod['passes_Echi'] is True and replay['scientific_pass'] is True and replay['status']=='PASS','science flags')
need(F(prod['Echi'])==F(replay['Echi'])<=F(1,10**6),'Echi')
need(prod['particle_intervals']==replay['particle_intervals'] and set(prod['particle_intervals'])=={str(k) for k in range(1,22,2)}|{'all_ge3'},'all odd intervals')
for key,bounds in prod['particle_intervals'].items():need(F(0)<=F(bounds[0])<=F(bounds[1]),'interval ordering')
for name,c in prod['representative_certificates'].items():need(c['candidate_attempts']=='1' and F(0)<=F(c['rho'])<=(F(1,10**10) if name.startswith('first') else F(1,10**9)),'one candidate residual')
need(len(prod['vector_manifest'])==11,'eleven saved NPY')
for row in prod['vector_manifest']:
 need(sha(O/'production'/row['file'])==row['sha256'],'NPY hash')
 if row['raw']:
  raw=O/'production'/(Path(row['file']).stem+'.bin');need(sha(raw)==row['raw']['sha256'] and raw.stat().st_size==row['raw']['bytes']==16*(1<<20),'raw hash/size')
receipts={}
for name,cap in [('production',180),('replay',150)]:
 r=read(R/(name+'.RECEIPT.json'));need(r['pass'] is True and r['error'] is None and r['returncode']==0,'stage complete')
 for key in ('seconds','external_seconds'):need(math.isfinite(r[key]) and 0<r[key]<cap,'stage wall')
 need(0<r['aggregate_peak']<=384*1048576 and 0<r['external_rss']<=384*1048576,'stage memory');receipts[name]={k:r[k] for k in ('seconds','external_seconds','aggregate_peak','external_rss')}
shell=(R/'ROOT_SHELL.stderr').read_text();wall=float(re.findall(r'^real\s+([0-9.]+)',shell,re.M)[-1]);rss=int(re.findall(r'^\s*(\d+)\s+maximum resident set size',shell,re.M)[-1]);need(0<wall<346 and wall+14<360 and 0<rss<=384*1048576,'whole shell')
summary={'status':'PASS_READ_ONLY','checks':checks,'Echi':float(F(prod['Echi'])),'positive_odd_lower_sectors':[k for k in range(1,22,2) if F(prod['particle_intervals'][str(k)][0])>0],'particle_intervals_display':{k:[float(F(v)) for v in x] for k,x in prod['particle_intervals'].items()},'receipts':receipts,'root_external_seconds':wall,'charged_seconds':wall+14,'root_external_rss':rss,'production_file_count':len(now),'production_RESULT_sha256':sha(O/'production/RESULT.json'),'replay_REVIEW_sha256':sha(O/'replay/REVIEW.json'),'scope':'stream hashes and exact scalar reconciliation; no raw arithmetic replay or physical actions'}
print(json.dumps(summary,indent=2))
