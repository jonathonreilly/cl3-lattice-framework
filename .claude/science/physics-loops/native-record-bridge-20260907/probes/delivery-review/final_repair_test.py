from pathlib import Path
import shutil,subprocess,os,json,hashlib,difflib
src=Path('/private/tmp/toe-native-record-bridge-20260907/.claude/science/physics-loops/native-record-bridge-20260907');out=Path(__file__).resolve().parent
old=(src/'probes/probability-family-cold-review/independent.py').read_text();new=(src/'probes/probability-family-cold-review/independent_portable.py').read_text()
assert new==old.replace("root=Path('/private/tmp/toe-native-record-probes-20260907/probability-family')","root=Path(__file__).resolve().parents[1]/'probability-family'")
rows=[];env=dict(os.environ);env['PYTHONOPTIMIZE']='1'
for case in ['baseline','math_mutation']:
 p=out/('final_'+case)
 if p.exists():shutil.rmtree(p)
 shutil.copytree(src,p)
 if case=='math_mutation':
  n='probes/action-measure/check.py';f=p/n;s=f.read_text();assert 's.Rational(1,4)*t*t' in s
  f.write_text(s.replace('s.Rational(1,4)*t*t','s.Rational(2,4)*t*t'))
  m=json.loads((p/'FROZEN_PROBE_SHA256.json').read_text());m[n]=hashlib.sha256(f.read_bytes()).hexdigest();(p/'FROZEN_PROBE_SHA256.json').write_text(json.dumps(m))
 r=subprocess.run(['python3',str(p/'run_probes.py')],capture_output=True,text=True,env=env,timeout=180)
 (out/('final_'+case+'.stdout')).write_text(r.stdout);(out/('final_'+case+'.stderr')).write_text(r.stderr)
 if case=='baseline':
  x=json.loads(r.stdout);assert r.returncode==0 and x['executed_named_assertions']==186 and x['probe_programs']==7 and x['additional_independent_probability_rows']==1458
 else:assert r.returncode!=0 and 'AssertionError' in r.stderr and 'Frozen input changed' not in r.stderr
 rows.append({'case':case,'parent_PYTHONOPTIMIZE':'1','exit_code':r.returncode,'expected_result_confirmed':True})
names=['run_probes.py','probes/action-measure/check.py','probes/action-measure/check_reservoir.py','probes/probability-family-cold-review/independent.py','probes/probability-family-cold-review/independent_portable.py','FROZEN_PROBE_SHA256.json']
hashes={n:hashlib.sha256((src/n).read_bytes()).hexdigest() for n in names}
(out/'FINAL_REPAIR_RESULTS.json').write_text(json.dumps({'cases':rows,'portable_change':'one path assignment only','hashes':hashes},indent=2)+'\n');print(json.dumps(hashes,indent=2))
