from pathlib import Path
import json,hashlib,re,math
B=Path('/private/tmp/toe-24h-probes-20260908');R=B/'native-l6-nonlinear-canonical-root-review';C=B/'native-l6-nonlinear-canonical-isolated-4d625'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
assert sha(R/'ROOT_FREEZE.json')=='98668ca3ef3f4e2a375604b69c8ee83556f722a95c6ee42f85da7cea557a164d';rf=json.loads((R/'ROOT_FREEZE.json').read_text());f=json.loads((R/'INPUTS.json').read_text())
for n,h in rf['files'].items():assert sha(R/n)==h,n
for n,h in f['runtime'].items():assert sha(n)==h,n
for n,h in f['science'].items():assert sha(C/n)==h,n
text=(R/'ROOT_SHELL.stderr').read_text();wall=float(re.findall(r'^real\s+([0-9.]+)\s*$',text,re.M)[-1]);rss=int(re.findall(r'^\s*(\d+)\s+maximum resident set size\s*$',text,re.M)[-1]);limit=384*1048576;assert math.isfinite(wall) and 0<wall<180 and 0<rss<=limit
c=json.loads((R/'COMPLETE.json').read_text());w=json.loads((R/'WORKER_COMPLETE.json').read_text());out=C/'outputs/native_l6_nonlinear_star_vertex_2026_09_09.json';r=json.loads(out.read_text());prior=json.loads((C/'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/INDEPENDENT_REVIEW.json').read_text())
assert c['status']=='PASS' and c['returncode']==0 and c['failure'] is None and 0<c['whole_tree_peak']<=limit and c['root_freeze']==sha(R/'ROOT_FREEZE.json');assert w['status']=='PASS' and w['result_sha256']==sha(out) and w['canonical_freeze']==f['canonical_freeze'];assert r['status']=='PASS' and r['replay']['scientific_pass'] is True
for k,v in prior.items():
 if k in ('status','scientific_pass','Echi','particle_intervals','full_vectors','fresh_residuals','transports','exact_norm_scans'):assert r['replay'][k]==v,k
assert r['geometry']['predicates']==11997 and r['claims']['full_linear_modes']==108 and r['claims']['positive_particle_sectors']==[3,5,7]
assert r['input_hashes']==json.loads((C/'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/SOURCE_MANIFEST.json').read_text());assert not (R/'WORKER_FAILURE.json').exists()
a=dict(accepted=True,status='PASS',source_freeze=f['canonical_freeze'],root_freeze=sha(R/'ROOT_FREEZE.json'),external_seconds=wall,external_rss=rss,observed_whole_tree_rss=c['whole_tree_peak'],runtime_pins=len(f['runtime']),isolated_science_files=len(f['science']),output_sha256=sha(out),geometry_predicates=11997,exact_accepted_scientific_payload=True,full_vectors=7,fresh_residuals=4,transports=27,exact_norm_scans=9,scope='Separate complete portable replay of accepted finiteL6 candidates; no new inverse solve. As-run source4d625 retained.')
(R/'ACCEPTANCE.json').write_text(json.dumps(a,indent=2)+'\n');print(json.dumps(a));print('acceptance_sha256',sha(R/'ACCEPTANCE.json'))
