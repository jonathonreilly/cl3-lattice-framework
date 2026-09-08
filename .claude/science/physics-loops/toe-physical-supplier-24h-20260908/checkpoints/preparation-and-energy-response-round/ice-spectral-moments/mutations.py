from pathlib import Path
import subprocess,sys,json,difflib
p=Path(__file__).resolve().parent;source=(p/'check.py').read_text();rows=[]
for name,old,new in [('missing_dirichlet_half','F(int(sum(sq)),2*z)','F(int(sum(sq)),z)'),('wrong_detuned_weight','correct1=float(sum(prob*O*ell)/Zd)','correct1=float(mom[1])')]:
 assert source.count(old)==1;x=source.replace(old,new);f=p/(name+'.py');f.write_text(x);(p/(name+'.diff')).write_text(''.join(difflib.unified_diff(source.splitlines(True),x.splitlines(True),fromfile='check.py',tofile=f.name)))
 r=subprocess.run([sys.executable,str(f)],capture_output=True,text=True,timeout=180);(p/(name+'.stdout')).write_text(r.stdout);(p/(name+'.stderr')).write_text(r.stderr)
 assert r.returncode and 'AssertionError' in r.stderr;rows.append({'mutation':name,'exit':r.returncode,'error':r.stderr.strip().splitlines()[-1]})
rows.append({'mutation':'collapse_geometric_multiplicity','outcome':'non-discriminating: all actual L2 adjacency multiplicities are1; altered operator equals original. Not counted as a killed mutation.'})
(p/'mutation_results.json').write_text(json.dumps(rows,indent=2)+'\n')
