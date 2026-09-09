import ast,json,sys,subprocess,time,signal,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
signal.alarm(28)
d=Path(__file__).resolve().parent;root=Path(sys.argv[1]);start=time.monotonic();rows=[]
stage='binding'
try:
 freeze=json.loads((d/'FREEZE.json').read_text())
 for path,expected in freeze['files'].items():
  if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=expected:raise ValueError('source binding '+path)
 def save(): (d/'RESULT.json').write_text(json.dumps(dict(rows=rows,seconds=time.monotonic()-start),indent=2)+'\n')
 for name in ('baseline','wrong_native_normalization','wrong_inverse_term'):
  stage=name
  q=subprocess.run([sys.executable,'-I','-B','-S','-OO',str(d/'worker.py'),name,str(root)],capture_output=True,text=True,timeout=9)
  rows.append(dict(name=name,exit=q.returncode,stdout=q.stdout,stderr=q.stderr));save()
  if (q.returncode==0)!=(name=='baseline'):raise ValueError('semantic control outcome')
 stage='singleton branch controls'
 primary=root/'scripts/native_l6_sixth_prefix_gap_certificate_2026_09_08.py'
 # Execute the actual singleton branch body, not a rewritten mathematical analogue.
 tree=ast.parse(primary.read_text());branch=next(n for n in ast.walk(tree) if isinstance(n,ast.If) and isinstance(n.test,ast.Compare) and ast.unparse(n.test)=="case['singleton'] is not None")
 source=ast.unparse(ast.Module(body=branch.body,type_ignores=[]));case=json.loads((d/'CASES.json').read_text())['singleton']
 for name,body in [('singleton_actual',source),('singleton_unrestricted_parity',source.replace('F(2 * isqrt(3 * 10 ** 60), 10 ** 30)','F(0)'))]:
  if name.endswith('parity') and body==source:raise ValueError('mutation absent')
  (d/(name+'.py')).write_text(body+'\n');ns=dict(F=F,isqrt=isqrt,case=case);exec(compile(body,name,'exec'),ns)
  good=ns['gap']==F(case['gap_lower']) and ns['gap']>F(1,3)
  rows.append(dict(name=name,actual=str(ns['gap']),matches=good));save()
  if good!=(name=='singleton_actual'):raise ValueError('singleton discriminator')
 for flag in ('--unknown-control','--json=wrong'):
  stage='CLI '+flag
  q=subprocess.run([sys.executable,'-I','-B','-S','-OO',str(primary),flag],capture_output=True,text=True,timeout=2)
  rows.append(dict(name='CLI '+flag,exit=q.returncode,stdout=q.stdout,stderr=q.stderr));save()
  if q.returncode!=2:raise ValueError('CLI rejection')
except BaseException as exc:
 (d/'FAILURE.json').write_text(json.dumps(dict(status='FAILED',stage=stage,error=repr(exc),rows=rows,seconds=time.monotonic()-start),indent=2)+'\n')
 raise
