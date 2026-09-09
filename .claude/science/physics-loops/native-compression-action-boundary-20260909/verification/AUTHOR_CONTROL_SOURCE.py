from pathlib import Path
import tempfile,shutil,subprocess,json,hashlib,time
W=Path('/private/tmp/toe-native-compression-action-boundary-20260909');rel=Path('.claude/science/physics-loops/native-compression-action-boundary-20260909');P=W/rel;mf=rel/'verification/INPUT_MANIFEST.json';manifest=json.loads((W/mf).read_text());exe='/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12';runner='scripts/native_compression_action_boundary_2026_09_09.py'
def setup():
 d=Path(tempfile.mkdtemp(prefix='native-boundary-tiny-'))
 for r in list(manifest['files'])+[str(mf)]:
  p=d/r;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(W/r,p)
 return d
def rebind(d):
 # Deliberately refresh local manifest AND original-copy metadata so arithmetic claim, not hashes, is tested.
 rp=d/rel/'verification/RECOVERY_MANIFEST.json';r=json.loads(rp.read_text())
 for x in r['local_copies']:
  p=d/x['local_path'];x['sha256']=hashlib.sha256(p.read_bytes()).hexdigest();x['bytes']=p.stat().st_size
  for a in x['archive_matches']:a['sha256']=x['sha256']
 rp.write_text(json.dumps(r,indent=2)+'\n');m=json.loads((d/mf).read_text())
 for path in m['files']:m['files'][path]=hashlib.sha256((d/path).read_bytes()).hexdigest()
 (d/mf).write_text(json.dumps(m,indent=2)+'\n')
results=[]
for kind in ['isolation','leakage_flag','diagonal_lower','fresh_witness','unknown_cli','positional_cli']:
 d=setup()
 try:
  if kind in ['leakage_flag','diagonal_lower']:
   p=d/rel/'verification/evidence/native-sparse-pivot-action-root-review/ROOT_ACCEPTANCE.json';x=json.loads(p.read_text())
   x['orbits'][0]['impurities'][0]['leakage_pass' if kind=='leakage_flag' else 'delta_squared_lower_from_diagonal']=True if kind=='leakage_flag' else '0'
   p.write_text(json.dumps(x)+'\n');rebind(d)
  elif kind=='fresh_witness':
   p=d/rel/'verification/evidence/native-fresh-pivot-width-run/RESULT.json';x=json.loads(p.read_text());r=min([r for r in x['rows'] if r['orbit']==0 and r['must_fail_width']],key=lambda r:r['row']);r['exact_image_width_lower_bound']='0';p.write_text(json.dumps(x)+'\n')
   # Refresh the two explicit output hash references too.
   p2=d/rel/'verification/evidence/native-fresh-pivot-width-root-review/ROOT_ACCEPTANCE.json';a=json.loads(p2.read_text());a['result_sha256']=hashlib.sha256(p.read_bytes()).hexdigest();p2.write_text(json.dumps(a)+'\n');rebind(d)
  args=['--unknown'] if kind=='unknown_cli' else ['unexpected'] if kind=='positional_cli' else ['--verify'];t=time.monotonic();r=subprocess.run([exe,'-I','-B','-S','-OO',str(d/runner),*args],capture_output=True,text=True,timeout=10)
  want={'leakage_flag':'all ten leakage outcomes false','diagonal_lower':'certified trial-space diagonal lower','fresh_witness':'exact image obstruction'}
  passed=r.returncode==0 if kind=='isolation' else r.returncode!=0 and (want[kind] in r.stderr if kind in want else 'unrecognized arguments' in r.stderr)
  results.append({'case':kind,'pass':passed,'returncode':r.returncode,'seconds':time.monotonic()-t,'stdout':r.stdout,'stderr':r.stderr})
 finally:shutil.rmtree(d)
(P/'verification/SEMANTIC_CONTROLS.json').write_text(json.dumps({'status':'PASS' if all(x['pass'] for x in results) else 'FAIL','scope':'compact verifier synthetic altered claims only, no native calls','cases':results},indent=2)+'\n')
print([(x['case'],x['pass'])for x in results])
