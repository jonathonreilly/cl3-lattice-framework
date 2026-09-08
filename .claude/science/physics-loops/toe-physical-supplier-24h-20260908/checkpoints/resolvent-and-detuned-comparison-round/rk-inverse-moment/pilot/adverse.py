from pathlib import Path
import subprocess,sys,json,difflib
p=Path(__file__).resolve().parent;s=(p/'kernel.py').read_text();verify=(p/'verify.py').read_text();rows=[]
for name,a,b in [('wrong_sweep','range(steps):','range(steps*len(faces)):'),('wrong_lag_offset','np.floor(np.log1p(-U)/np.log(q)).astype(np.int64)','np.floor(np.log1p(-U)/np.log(q)).astype(np.int64)+1')]:
 if s.count(a)!=1:raise AssertionError('mutation target')
 t=s.replace(a,b);(p/(name+'.py')).write_text(t);(p/(name+'.diff')).write_text(''.join(difflib.unified_diff(s.splitlines(True),t.splitlines(True))));f=p/('verify_'+name+'.py');f.write_text(verify.replace('from kernel import','from '+name+' import'));r=subprocess.run([sys.executable,str(f)],capture_output=True,text=True,timeout=180);(p/(name+'.stdout')).write_text(r.stdout);(p/(name+'.stderr')).write_text(r.stderr);rows.append({'case':name,'exit':r.returncode,'actual_assertion':'AssertionError' in r.stderr,'last_line':r.stderr.splitlines()[-1] if r.stderr else ''})
(p/'ADVERSE.json').write_text(json.dumps(rows,indent=2)+'\n')
