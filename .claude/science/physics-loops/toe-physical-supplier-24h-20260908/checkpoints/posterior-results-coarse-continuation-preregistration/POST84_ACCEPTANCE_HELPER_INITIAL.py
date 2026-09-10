from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,datetime,sys
sys.set_int_max_str_digits(20000);B=Path('/private/tmp/toe-24h-probes-20260908');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();pre=json.loads((B/'CHECKPOINT84_REMOTE_VERIFICATION.json').read_text());act=json.loads((B/'ACTIVATION84.json').read_text())['rows']
for row in act:
 R=B/row['root'];rf=json.loads((R/'ROOT_FREEZE.json').read_text());O=Path(rf['authorization']['output']);cap=rf['authorization']['external_seconds']
 if not(R/'RECEIPT.json').exists():print({'root':R.name,'status':'STILL_RUNNING'});continue
 if(R/'ROOT_ACCEPTANCE.json').exists():print({'root':R.name,'status':'ALREADY_ACCEPTED_NOT_REPLAYED'});continue
 receipt=json.loads((R/'RECEIPT.json').read_text());s=json.loads((R/'SCHEMA_ACCEPTANCE.json').read_text());err=(R/'EXTERNAL.stderr').read_text();wall=float(re.search(r'([0-9.]+) real',err)[1]);rss=int(re.search(r'(\d+)\s+maximum resident set size',err)[1]);assert receipt['pass']is True and receipt['failure']is None and receipt['returncode']==0 and 0<receipt['seconds']<=wall+.01<cap;assert 0<rss<384*1048576 and 0<receipt['sampled_whole_tree_peak']<384*1048576;assert sha(R/'ROOT_FREEZE.json')==row['root_freeze'];assert receipt['worker_freeze']==row['worker_freeze'] and s['result_sha256']==sha(O/'RESULT.json')
 result=json.loads((O/'RESULT.json').read_text());a={'status':'ACCEPTED_NEW_'+R.name.upper().replace('-','_')+'_ONCE','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'preregistration_commit':pre['head'],'preregistration_receipt_sha256':sha(B/'CHECKPOINT84_REMOTE_VERIFICATION.json'),'worker_freeze':row['worker_freeze'],'root_freeze':row['root_freeze'],'result_sha256':s['result_sha256'],'schema_sha256':sha(R/'SCHEMA_ACCEPTANCE.json'),'external_seconds':wall,'external_rss_bytes':rss,'sampled_whole_tree_peak':receipt['sampled_whole_tree_peak'],'once':True,'external_stdout_sha256':sha(R/'EXTERNAL.stdout'),'external_stderr_sha256':sha(R/'EXTERNAL.stderr'),'schema':s}
 (R/'ROOT_ACCEPTANCE.json').write_text(json.dumps(a,indent=2)+'\n');display={'root':R.name,'root_acceptance':sha(R/'ROOT_ACCEPTANCE.json'),'result':s['result_sha256'],'wall':wall,'rss':rss,'tree':receipt['sampled_whole_tree_peak']}
 for name,h in s['output_hashes'].items():assert sha(O/name)==h
 display.update(rows=[{'mode':x['mode'],'status':x['status'],'nominal':[float(F(v))for v in x['nominal']],'error_upper':float(F(x['error_upper'])),'alpha_interval':[float(F(v))for v in x['alpha_interval']]}for x in result['rows']])
 print(display)
