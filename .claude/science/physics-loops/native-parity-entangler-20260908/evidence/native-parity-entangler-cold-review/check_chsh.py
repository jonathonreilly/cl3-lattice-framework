import runpy,contextlib,io,json,hashlib
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(Path(__file__).with_name('check.py')))
s=d['s'];U=d['U'];z=d['z'];bell=d['bell']
def obs(k,t):
 a=U(k,s.cos(t),s.sin(t));return s.simplify(a.H*z[k]*a)
A=[obs(0,0),obs(0,s.pi/4)];B=[obs(2,s.pi/8),obs(2,-s.pi/8)];C=s.Matrix([[s.simplify((bell.H*a*b*bell)[0]) for b in B] for a in A]);target=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
if not d['eq'](C,target):raise AssertionError('exact correlations')
if any(not d['eq'](a*b,b*a) for a in A for b in B):raise AssertionError('commutation')
value=s.simplify(C[0,0]+C[0,1]+C[1,0]-C[1,1]);print(json.dumps(dict(exact_correlations=[[str(x) for x in C.row(i)] for i in range(2)],CHSH=str(value),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2))
