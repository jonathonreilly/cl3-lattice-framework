from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re,math
B=Path('/private/tmp/toe-24h-probes-20260908');R=B/'native-l6-vertex-energy-bins-v2-root-review';P=B/'native-l6-vertex-energy-bins-v2';O=B/'native-l6-vertex-energy-bins-v2-run-4b771'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
assert sha(R/'ROOT_FREEZE.json')=='d79f4a831b598c2b5b3e328ff25512a3646d002810b03d268501d8d27db83cfe';rf=json.loads((R/'ROOT_FREEZE.json').read_text())
for n,h in rf['files'].items():assert sha(R/n)==h,n
for n,h in rf['accepted_inputs'].items():assert sha(n)==h,n
assert sha(P/'FREEZE.json')=='4b7714ad6290c898845dc8a3921e614728d1e55c898b571d8e60abe809b32059';f=json.loads((P/'FREEZE.json').read_text())
for n,h in f['inputs'].items():assert sha(n)==h,n
r=json.loads((O/'RESULT.json').read_text());bins=json.loads((O/'BINS.json').read_text());outer=json.loads((R/'OUTER.json').read_text());binding=json.loads((R/'BINDING.json').read_text());text=(R/'ROOT_SHELL.stderr').read_text();wall=float(re.findall(r'^real\s+([0-9.]+)\s*$',text,re.M)[-1]);rss=int(re.findall(r'^\s*(\d+)\s+maximum resident set size\s*$',text,re.M)[-1]);limit=384*1048576
assert 0<wall<30 and math.isfinite(wall) and 0<rss<=limit and outer['provisional_resource_accept'] is True and outer['returncode']==0 and 0<outer['observed_whole_tree_rss']<=limit
assert r['status']=='PASS' and r['source_freeze']==sha(P/'FREEZE.json') and r['binding_sha256']==sha(R/'BINDING.json') and r['input_sha256']==binding['raw_sha256']==bins['input_sha256'] and r['entries']==bins['entries']==1<<20
assert r['bins']==bins['bins'] and len(r['bins'])==686 and r['denominator_exponent']==bins['denominator_exponent']==2148
assert len({tuple(x['counts']) for x in r['bins']})==686
for x in r['bins']:assert all(0<=v<=m for v,m in zip(x['counts'],(6,6,6,3))) and sum(x['counts'])%2==1 and int(x['numerator'])>=0
for key,criterion in [('one',lambda n:n==1),('higher',lambda n:n>=3),('total',lambda n:True)]+[(str(k),lambda n,k=k:n==k) for k in range(1,22,2)]:
 w=F(sum(int(x['numerator']) for x in r['bins'] if criterion(sum(x['counts']))),1<<2148);assert F(r['summary'][key]['stored_weight'])==w
 for field in ('true_weight_interval','stored_susceptibility_interval','true_susceptibility_interval'):
  lo,hi=map(F,r['summary'][key][field]);assert 0<=lo<=hi
assert not (O/'FAILURE.json').exists()
a=dict(status='PASS',accepted=True,external_seconds=wall,root_external_rss=rss,observed_whole_tree_rss=outer['observed_whole_tree_rss'],source_freeze=sha(P/'FREEZE.json'),root_freeze=sha(R/'ROOT_FREEZE.json'),source_pins=len(f['inputs']),result_sha256=sha(O/'RESULT.json'),bins_sha256=sha(O/'BINS.json'),binding_sha256=sha(R/'BINDING.json'),input_sha256=r['input_sha256'],entries=r['entries'],bin_count=len(r['bins']),scope='One accepted finiteL6 local singleton susceptibility; not full sixth-order coefficient. Independent scalar arithmetic review recorded separately.')
(R/'ACCEPTANCE.json').write_text(json.dumps(a,indent=2)+'\n');print(json.dumps(a));print('acceptance_sha256',sha(R/'ACCEPTANCE.json'))
