from pathlib import Path
from fractions import Fraction as F
import hashlib,json,math,re
B=Path('/private/tmp/toe-24h-probes-20260908');P=B/'native-star-local-green-gram-stretch';R=B/'native-star-local-green-gram-root-review';O=B/'native-star-local-green-gram-run-41ebe';D=B/'native-star-local-green-gram-post-review'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(x,m):
 if not x:raise ValueError(m)
pf='41ebe55c0deb54f4219daa49c2ebf43d839d26637ae10d54edf2dbf4acec1080'
require(sha(P/'FREEZE.json')==pf,'freeze')
f=json.loads((P/'FREEZE.json').read_text()); hashes={}
for p,h in f['inputs'].items():require(sha(Path(p))==h,p);hashes[p]=h
rf=json.loads((R/'ROOT_FREEZE.json').read_text())
for p,h in rf['files'].items():require(sha(R/p)==h,p)
a=json.loads((R/'RECEIPT.json').read_text());w=json.loads((O/'WORKER_COMPLETE.json').read_text());d=json.loads((O/'RESULT.json').read_text())
require(w['result_sha256']==sha(O/'RESULT.json') and w['freeze_sha256']==pf,'completion')
require(a['pass'] and a['returncode']==0 and a['failure'] is None and a['worker_freeze']==pf,'receipt')
require(d['gram_matrix_computed'] is False and d['alpha_computed'] is False,'scope')
expected=[('1','A',1024),('1','B',4096),('2','A',1024),('2','B',4096)];out=[]
require(len(d['rows'])==4,'rows')
for r,e in zip(d['rows'],expected):
 require((r['s'],r['kind'],r['cap'])==e,'case'); require(r['target']=='1/32','target')
 require(r['leaves']==1+r['splits']*(3 if r['kind']=='A' else 7) and r['leaves']<=r['cap'],'partition')
 require(len(r['bounds'])==len(r['widths'])==2,'shape')
 widths=[]
 for pair,width in zip(r['bounds'],r['widths']):
  lo,hi=map(F,pair); z=hi-lo;require(0<=z<=F(1,32) and z==F(width),'width');widths.append(str(z))
 require(r['status']=='CERTIFIED_TARGET','status');out.append({'case':e,'widths':widths,'seconds':r['seconds']})
require(d['all_width_targets_met'] is True,'aggregate')
require(json.loads((O/'PARTIAL.json').read_text())['rows']==d['rows'],'partial final')
ts=[r['seconds'] for r in d['rows']]+[d['seconds'],w['seconds'],a['seconds']]
require(all(math.isfinite(x) and x>0 for x in ts),'finite times')
shell=(R/'ROOT.stderr').read_text();wall=F(re.search(r'([0-9.]+) real',shell).group(1));rss=int(re.search(r'(\d+)  maximum resident set size',shell).group(1))
require(sum(ts[:4])<=d['seconds']<=w['seconds']<=a['seconds']<=float(wall)+.01<30,'timing')
require(0<rss<=384*1048576 and 0<a['sampled_whole_tree_peak']<=384*1048576,'memory')
for folder in [R,O]:
 for p in folder.iterdir():
  if p.is_file():hashes[str(p)]=sha(p)
hashes[str(P/'FREEZE.json')]=sha(P/'FREEZE.json')
(D/'READ_HASHES.json').write_text(json.dumps(hashes,indent=2,sort_keys=True)+'\n')
(D/'RESULT.json').write_text(json.dumps({'status':'PASS_READ_ONLY_POSTCHECK','input_pins':len(f['inputs']),'rows':out,'external_wall':str(wall),'shell_rss':rss,'sampled_tree':a['sampled_whole_tree_peak'],'integral_reruns':0},indent=2)+'\n')
print('PASS',len(f['inputs']),float(wall),a['sampled_whole_tree_peak'])
