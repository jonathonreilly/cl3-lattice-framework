import json,hashlib
from pathlib import Path
from fractions import Fraction as F
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as file:
  for chunk in iter(lambda:file.read(1<<20),b''):h.update(chunk)
 return h.hexdigest()
def validate(path):
 path=Path(path);before=sha(path);b=json.loads(path.read_text());docs={};hashes={str(path):before}
 for role in ['production','completion','replay','acceptance']:
  entry=b['receipts'][role];p=Path(entry['path']).resolve();h=sha(p)
  if h!=entry['sha256']:raise ValueError('receipt hash '+role)
  docs[role]=json.loads(p.read_text());hashes[str(p)]=h
 prod,comp,rep,acc=[docs[k] for k in ['production','completion','replay','acceptance']]
 ph=b['receipts']['production']['sha256'];rh=b['receipts']['replay']['sha256'];ch=b['receipts']['completion']['sha256']
 if prod.get('algorithm')!='direct_gaussian_once' or prod.get('passes_Echi') is not True or prod.get('physical_global_phase')!='i':raise ValueError('accepted production')
 if comp.get('status')!='PRODUCTION_ONLY_COMPLETE' or comp.get('result_sha256')!=ph or comp.get('source_freeze')!=b['production_source_freeze'] or comp.get('contract_sha256')!=b['production_contract_sha256']:raise ValueError('completion')
 if rep.get('status')!='PASS' or rep.get('scientific_pass') is not True or rep.get('input_result_sha256')!=ph or rep.get('worker_complete_sha256')!=ch or rep.get('source_freeze')!=b['replay_source_freeze']:raise ValueError('accepted replay')
 if acc.get('accepted') is not True or acc.get('production_result_sha256')!=ph or acc.get('independent_replay_sha256')!=rh:raise ValueError('root acceptance')
 if F(prod['Echi'])!=F(rep['Echi']) or not 0<=F(prod['Echi'])<=F(1,10**6):raise ValueError('Echi')
 rows=[r for r in prod['vector_manifest'] if r['file']=='chi_real.npy']
 if len(rows)!=1 or rows[0]['raw']['phase']!='i':raise ValueError('chi manifest')
 if b['raw_sha256']!=rows[0]['raw']['sha256']:raise ValueError('raw binding')
 return {'Echi':prod['Echi'],'raw_sha256':b['raw_sha256'],'hashes':hashes,'binding_sha256':before}
