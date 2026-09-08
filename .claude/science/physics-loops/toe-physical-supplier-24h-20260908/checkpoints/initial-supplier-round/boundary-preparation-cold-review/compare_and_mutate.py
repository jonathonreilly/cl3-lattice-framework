from pathlib import Path
import json, subprocess, sys, difflib, hashlib
p=Path(__file__).resolve().parent;a=Path('/private/tmp/toe-24h-probes-20260908/boundary-preparation')
x=json.loads((p/'result.json').read_text());y=json.loads((a/'operational_results.json').read_text())
for r,t in zip(x['rows'],y['rows']):
 assert r['family']==t['family']
 for k,l in [('p','prior_reservoir_occupation'),('success','record45_success'),('posterior','record04_occupied_given_success')]:assert r[k]==t[l]
source=(p/'check.py').read_text();rows=[]
for name,old,new in [('nonunitary_angle','b=s.Rational(4,5)','b=s.Rational(3,5)'),('wrong_antiunitary','for v in [1,3,4]','for v in []')]:
 assert source.count(old)==1
 mutant=source.replace(old,new);target=p/(name+'.py');target.write_text(mutant)
 (p/(name+'.diff')).write_text(''.join(difflib.unified_diff(source.splitlines(True),mutant.splitlines(True),fromfile='check.py',tofile=target.name)))
 proc=subprocess.run([sys.executable,str(target)],capture_output=True,text=True,timeout=30)
 (p/(name+'.stdout')).write_text(proc.stdout);(p/(name+'.stderr')).write_text(proc.stderr)
 assert proc.returncode!=0 and 'AssertionError' in proc.stderr
 rows.append({'case':name,'returncode':proc.returncode,'last_error':proc.stderr.strip().splitlines()[-1]})
files=['DERIVATION.md','check.py','operational.py','results.json','operational_results.json','PREREGISTRATION.md','OPERATIONAL_SUPPLEMENT_PREREGISTRATION.md','SHA256.json','OPEN_PR_SEARCH.json','mutations/results.json','mutations/bad_filter_angle.py','mutations/erase_failure.py','mutations/bad_filter_angle.stderr','mutations/erase_failure.stderr']
out={'comparison':'two families, all three rational observables match','mutations':rows,'reviewed_author_files':{f:hashlib.sha256((a/f).read_bytes()).hexdigest() for f in files}}
(p/'comparison_mutations.json').write_text(json.dumps(out,indent=2)+'\n')
