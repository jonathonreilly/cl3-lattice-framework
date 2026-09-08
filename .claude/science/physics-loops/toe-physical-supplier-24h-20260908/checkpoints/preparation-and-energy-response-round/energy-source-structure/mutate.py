from pathlib import Path
import subprocess,sys,json,difflib
p=Path(__file__).resolve().parent;s=(p/'check.py').read_text();cases=[('omit_shift_restore','mixed=float(psi@((V-1)*nf+lam*X)/psi.sum())','mixed=float(psi@((V-1)*nf+lam*X)/psi.sum())-shift'),('old_branch','branch=1+((1-V)*nf+shift-lam*X)/M','branch=1+(1-V)*nf/M'),('omit_stagger','(-1)**(sum(r)+r[a])/np.sqrt(vol)','(-1)**r[a]/np.sqrt(vol)')];rows=[]
for name,a,b in cases:
 assert s.count(a)==1;t=s.replace(a,b);f=p/(name+'.py');f.write_text(t);(p/(name+'.diff')).write_text(''.join(difflib.unified_diff(s.splitlines(True),t.splitlines(True))))
 r=subprocess.run([sys.executable,str(f)],capture_output=True,text=True,timeout=180);(p/(name+'.stdout')).write_text(r.stdout);(p/(name+'.stderr')).write_text(r.stderr);rows.append({'case':name,'returncode':r.returncode,'actual_assertion_failure':'AssertionError' in r.stderr,'last_line':r.stderr.splitlines()[-1] if r.stderr else ''})
(p/'MUTATIONS.json').write_text(json.dumps(rows,indent=2)+'\n')
