from pathlib import Path
import hashlib,json,subprocess,difflib,time,os
root=Path('/private/tmp/toe-native-record-probes-20260907');out=root/'mutation-checks'
cases=[
('native_cycle_sign','native-instrument/probe.py','S=-A[0]@A[1]@A[2]@A[3]','S=A[0]@A[1]@A[2]@A[3]'),
('native_post_normalization','native-instrument/probe.py','post=Q[f,z]@rho@Q[f,z]*2','post=Q[f,z]@rho@Q[f,z]*1'),
('probability_coefficient','probability-family/check.py','return F(1,2)+k*sum(c)/12','return F(1,2)+k*sum(c)/6'),
('improper_cubic_group','probability-family/check.py','if parity(perm)*signs[0]*signs[1]*signs[2]!=1:continue','if parity(perm)*signs[0]*signs[1]*signs[2]!=-1:continue'),
('action_transfer_polynomial','action-measure/check_square_frozen.py','F=lambda t:E-s.Rational(3,4)*t+s.Rational(1,4)*t*t','F=lambda t:E-s.Rational(1,4)*t+s.Rational(1,4)*t*t'),
('reservoir_occupation_sign','action-measure/check_reservoir.py','n4=(E-B[4])/2','n4=(E+B[4])/2'),
('relay_wrong_copy','record-relay-review/check.py','pp=F(ns.count(1),len(ns)) if ns else F(1,2)','pp=F(ns.count(-1),len(ns)) if ns else F(1,2)')]
# Mutation plan frozen in machine-readable form before any subprocess executes.
(out/'PLAN.json').write_text(json.dumps(cases,indent=2)+'\n')
pins={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for _,f,_,_ in cases};rows=[]
for name,f,old,new in cases:
 s=(root/f).read_text();assert s.count(old)==1,(name,s.count(old));m=s.replace(old,new);d=out/name;d.mkdir(exist_ok=True)
 (d/'mutant.py').write_text(m);(d/'delta.patch').write_text(''.join(difflib.unified_diff(s.splitlines(True),m.splitlines(True),fromfile=f,tofile=name+'/mutant.py')))
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1');t=time.monotonic()
 try:
  p=subprocess.run(['python3',str(d/'mutant.py')],cwd=d,capture_output=True,text=True,timeout=60,env=env)
  stdout,stderr,code=p.stdout,p.stderr,p.returncode
 except subprocess.TimeoutExpired as e:stdout=str(e.stdout or '');stderr=str(e.stderr or '')+'\nTIMEOUT';code=None
 (d/'stdout.txt').write_text(stdout);(d/'stderr.txt').write_text(stderr)
 killed=code not in (0,None) and 'AssertionError' in stderr
 r={'name':name,'original':f,'original_sha256':pins[f],'mutant_sha256':hashlib.sha256(m.encode()).hexdigest(),'returncode':code,'math_assertion_detected':killed,'elapsed_sec':time.monotonic()-t,'last_error':stderr.splitlines()[-1] if stderr else '', 'integrity_bypass':'No source-integrity assertion exists in these frozen probes; source hashes are output metadata only. Mutant was executed directly and no integrity check was used as detection.'}
 (d/'receipt.json').write_text(json.dumps(r,indent=2)+'\n');rows.append(r)
for f,h in pins.items():assert hashlib.sha256((root/f).read_bytes()).hexdigest()==h,f
(out/'RESULT.json').write_text(json.dumps({'originals_unchanged':True,'cases':rows,'detected':sum(r['math_assertion_detected'] for r in rows),'total':len(rows)},indent=2)+'\n');print(json.dumps(rows,indent=2))
