from pathlib import Path
import shutil,subprocess,json,hashlib,sys
src=Path('/private/tmp/toe-native-record-bridge-20260907/.claude/science/physics-loops/native-record-bridge-20260907')
out=Path(__file__).resolve().parent
records=[]
for mode in ['baseline','math_mutation_detected','subprocess_failure','missing_program']:
 p=out/mode
 if p.exists():shutil.rmtree(p)
 shutil.copytree(src,p)
 target='probes/action-measure/check_square_frozen.py'; f=p/target
 m=json.loads((p/'FROZEN_PROBE_SHA256.json').read_text())
 if mode=='math_mutation_detected':
  s=f.read_text();assert 's.Rational(1,4)*t*t' in s
  f.write_text(s.replace('s.Rational(1,4)*t*t','s.Rational(2,4)*t*t'))
 elif mode=='subprocess_failure':f.write_text('import sys\nsys.exit(7)\n')
 elif mode=='missing_program':f.unlink();m.pop(target)
 if mode in ['math_mutation_detected','subprocess_failure']:m[target]=hashlib.sha256(f.read_bytes()).hexdigest()
 (p/'FROZEN_PROBE_SHA256.json').write_text(json.dumps(m))
 r=subprocess.run([sys.executable,str(p/'run_probes.py')],capture_output=True,text=True,timeout=180)
 (out/(mode+'.stdout')).write_text(r.stdout);(out/(mode+'.stderr')).write_text(r.stderr)
 assert (r.returncode==0)==(mode=='baseline'),(mode,r.returncode,r.stdout)
 if mode=='baseline':
  x=json.loads(r.stdout);assert x['probe_programs']==7 and x['executed_named_assertions']==166
 if mode=='math_mutation_detected':assert 'AssertionError' in r.stderr and 'Frozen input changed' not in r.stderr
 if mode=='subprocess_failure':assert 'exited 7' in r.stderr
 if mode=='missing_program':assert 'exited 2' in r.stderr
 records.append({'case':mode,'exit_code':r.returncode,'expected_outcome_confirmed':True})
print(json.dumps(records,indent=2))
