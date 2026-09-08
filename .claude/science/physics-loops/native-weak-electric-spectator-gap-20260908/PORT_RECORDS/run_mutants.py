"""Two actual mathematical mutations; no baseline source is altered."""
from pathlib import Path
import ast,json,hashlib,shutil,subprocess,time,difflib,os
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'scripts/native_weak_electric_spectator_gap_2026_09_08.py').exists())
PRIMARY='scripts/native_weak_electric_spectator_gap_2026_09_08.py'
DATA='outputs/native_weak_electric_spectator_gap_2026_09_08_inputs'
paths=ast.literal_eval(next(n.value for n in ast.parse((ROOT/PRIMARY).read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in n.targets)))
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
reports=[]
for name in ('closing_factor','prefix_omission'):
 dest=HERE/('MUTANT_'+name)
 if dest.exists():raise RuntimeError('no overwrite')
 dest.mkdir()
 for n in (*paths,PRIMARY):
  target=dest/n;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/n,target)
 if name=='closing_factor':
  f=dest/'scripts/native_weak_electric_rational_replay_2026_09_08.py';old=f.read_text();new=old.replace('))/216;radius=u6*error/216','))/108;radius=u6*error/108')
  if new==old:raise ValueError('mutation missing')
  f.write_text(new)
 else:
  f=dest/DATA/'PREFIXES.json';old=f.read_text();z=json.loads(old);del z['rows'][0]['prefixes'][1];new=json.dumps(z,indent=2)+'\n';f.write_text(new)
 (dest/'source.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='frozen',tofile=name)))
 # Rebind intentionally changed input hashes to exercise mathematics, not self-integrity.
 manifest=dest/DATA/'INPUT_HASHES.json';pins=json.loads(manifest.read_text());manifest.write_text(json.dumps({n:sha(dest/n) for n in pins},indent=2)+'\n')
 t=time.monotonic()
 with (dest/'stdout').open('wb') as so,(dest/'stderr').open('wb') as se:
  r=subprocess.run(['/usr/bin/time','-lp','python3','-OO',str(dest/PRIMARY),'--json'],stdout=so,stderr=se,timeout=180,env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1'))
 text=(dest/'stderr').read_text();expected='exact coefficient certificate' if name=='closing_factor' else 'prefix coverage'
 reports.append({'name':name,'returncode':r.returncode,'seconds':time.monotonic()-t,'actual_mathematical_failure':r.returncode!=0 and expected in text,'expected_failure':expected,'stdout_sha':sha(dest/'stdout'),'stderr_sha':sha(dest/'stderr'),'diff_sha':sha(dest/'source.diff')})
 if not reports[-1]['actual_mathematical_failure']:raise RuntimeError('mutation survived or wrong failure')
(HERE/'MUTANT_RESULTS.json').write_text(json.dumps(reports,indent=2)+'\n')
