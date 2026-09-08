from pathlib import Path
import json,sympy as s,subprocess,sys,difflib,hashlib
p=Path(__file__).resolve().parent
r=json.loads((p/'physical_result.json').read_text());f=json.loads((p/'supplement_result.json').read_text())
R=s.sympify(f['R'],locals={'Matrix':s.Matrix})
assert r['response'][1]==[str(x) for x in R]
base=(p/'physical_check.py').read_text();out=[]
for name,old,new in [('omit_preparation_phase','phase=E+(s.I-1)*N[0]','phase=E'),('wrong_record_decoding','(1-signs[0]*signs[1])//2','(1+signs[0]*signs[1])//2')]:
 assert base.count(old)==1
 text=base.replace(old,new);path=p/(name+'.py');path.write_text(text)
 (p/(name+'.diff')).write_text(''.join(difflib.unified_diff(base.splitlines(True),text.splitlines(True),fromfile='physical_check.py',tofile=path.name)))
 z=subprocess.run([sys.executable,str(path)],capture_output=True,text=True,timeout=30)
 (p/(name+'.stdout')).write_text(z.stdout);(p/(name+'.stderr')).write_text(z.stderr)
 assert z.returncode!=0 and 'AssertionError' in z.stderr
 out.append({'case':name,'exit':z.returncode,'last_error':z.stderr.strip().splitlines()[-1]})
(p/'comparison_mutations.json').write_text(json.dumps({'direct_even_Fock_vs_physical_Pauli':'all 16 response entries match exactly','mutations':out},indent=2)+'\n')
