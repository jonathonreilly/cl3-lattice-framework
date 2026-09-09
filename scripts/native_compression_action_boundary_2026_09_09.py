"""Compact immutable evidence checks and tiny algebra; never a native replay."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'.claude/science/physics-loops/native-compression-action-boundary-20260909'
COUNT=0
def require(x,message):
 global COUNT
 if not x:raise ValueError(message)
 COUNT+=1
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(folder,name='RESULT.json'):
 return json.loads((PACK/'verification/evidence'/folder/name).read_text())
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--verify',action='store_true');ap.parse_args()
 manifest=json.loads((PACK/'verification/INPUT_MANIFEST.json').read_text())
 for path,h in manifest['files'].items():
  p=(ROOT/path).resolve();require(ROOT in p.parents,'repository-local input');require(sha(p)==h,'source/input hash '+path)
 rec=json.loads((PACK/'verification/RECOVERY_MANIFEST.json').read_text())
 require(rec['status']=='COMPACT_SNAPSHOT_WITH_REQUIRED_REMOTE_FORENSIC_RETRIEVAL','recovery scope')
 for row in rec['local_copies']:
  p=ROOT/row['local_path'];require(sha(p)==row['sha256'] and p.stat().st_size==row['bytes'],'original bytes')
  require(bool(row['archive_matches']) and all(x['sha256']==row['sha256'] and len(x['commit'])==40 for x in row['archive_matches']),'durable retrieval identity')
 action=load('native-sparse-pivot-action-root-review','ROOT_ACCEPTANCE.json');post=load('native-sparse-pivot-action-root-review','POST_ACCEPTANCE.json');saved=load('native-sparse-action-saved-post-run-593b')
 require(action['status']=='ACCEPTED_COMPLETE_ORIGINAL_FOUR_PAIR_ACTION_ENCLOSURE','action status')
 require(post['result_sha256']==action['result_sha256'] and post['post_result_sha256']==sha(PACK/'verification/evidence/native-sparse-action-saved-post-run-593b/RESULT.json'),'action post binding')
 require(saved['events_checked']==80 and saved['native_calls']==0 and len(saved['orbits'])==5,'saved action scope')
 require(len(action['orbits'])==5,'five action orbits')
 for i,o in enumerate(action['orbits']):
  require(type(o['orbit']) is int and o['orbit']==i and len(o['impurities'])==2,'action shape')
  for a in o['impurities']:
   require(a['leakage_pass'] is False and a['certified_diagonal_exceeds_optional_target'] is True,'all ten leakage outcomes false')
   require(F(a['delta_squared_lower_from_diagonal'])>F(3,10)>F(1,10**12),'certified trial-space diagonal lower')
   require(F(a['delta_squared_upper'])>=F(a['delta_squared_lower_from_diagonal']),'action enclosure order')
 four=load('native-fixed192-compression-root-review','ROOT_ACCEPTANCE.json');twelve=load('native-compression-continuation-root-review','ROOT_ACCEPTANCE.json');twentyfour=load('native-compression-24-root-review','ROOT_ACCEPTANCE.json')
 for k,r in [(4,four),(12,twelve),(24,twentyfour)]:
  require(len(r['orbits'])==5,'compression orbit census')
  for i,o in enumerate(r['orbits']):require(type(o['orbit']) is int and o['orbit']==i and o['pairs']==k and o['residual_pass'] is False and o['coordinate_pass'] is True,'fixed cap outcomes')
 for o in twentyfour['orbits']:
  require(F(o['raw_residual_upper'])>F(1,1062*10**6),'24 residual target remains unmet')
  require(F(o['coordinate_radius_squared'])<=F(1,40000**2),'24 coordinate target')
 for folder,h,c,n in [('native-compression-twelve-saved-post-run-02ca',40,271320,342930),('native-compression-24-saved-post-run-8522',60,885780,983426)]:
  p=load(folder);require(p['histories']==h and p['coordinates']==c and p['predicates']==n,'saved continuation scope')
 diag=load('native-fresh-pivot-width-run');dr=load('native-fresh-pivot-width-root-review','ROOT_ACCEPTANCE.json')
 require(diag['status']=='COMPLETE_SAVED_SCALAR_DIAGNOSTIC' and dr['result_sha256']==sha(PACK/'verification/evidence/native-fresh-pivot-width-run/RESULT.json'),'fresh result identity')
 rows=diag['rows'];require(len(rows)==78 and len(diag['forced_blockers'])==53,'fresh coverage')
 require(len({(x['orbit'],x['row']) for x in rows})==78,'unique fresh rows')
 first=[]
 for i in range(5):
  r=[x for x in rows if x['orbit']==i and x['must_fail_width']];require(bool(r),'orbit blocker')
  x=min(r,key=lambda x:x['row']);first.append(x['row']+1)
  require(F(x['exact_image_width_lower_bound'])>F(1,2**39),'exact image obstruction')
 for x in rows:
  require(x['threshold']==2**192//2**39 and x['width']==x['forced_upper']-x['forced_lower'],'saved scalar arithmetic metadata')
  require(x['must_fail_width']==(x['width']>x['threshold']),'saved width flag')
 require(first==[7,8,8,8,9],'one-based fresh witnesses')
 # Tiny independent scalar-width examples; no saved pivot r is recomputed.
 for a,b in [(1,2),(2,3),(3,7)]:
  l,u=F(a*a),F(b*b);w=1/(2*F(a))-1/(2*F(b));require(w==(u-l)/(2*a*b*(a+b)),'rationalized width')
  require(w>=(u-l)/(4*u*b),'width lower bound')
 S=2**16;l=S;u=4*S;lo=S*S//(2*isqrt(u*S));hi=-((-S*S)//(2*isqrt(l*S)))
 require((lo,hi)==(S//4,S//2),'toy directed endpoints')
 print('per_element: compact saved scalar witnesses and ten diagonal lower bounds checked; original numerical arithmetic not re-executed')
 print('per_site: checked and not executed — no sitewise physical assertion in this block')
 print('per_mode: checked and not executed — no full-band mode or propagation computation')
 print('per_block: five fixed compression orbits and ten four-pair action outcomes checked against immutable receipts')
 print('lattice_wide: checked and not executed — supplied-model implementation boundary, no physical no-go')
 print(json.dumps({'status':'PASS_COMPACT_BOUNDARY_EVIDENCE','checks':COUNT,'fresh_first_pairs':first,'native_calls':0,'saved_physics_replays':0,'remote_forensic_retrieval_required':True},sort_keys=True))
 print(f'TOTAL: PASS={COUNT} FAIL=0')
if __name__=='__main__':main()
