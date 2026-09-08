import runpy,contextlib,io,json
import sympy as s
from pathlib import Path
p=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(p/'initial_check.py'))
E,N,T,U,V,v=[d[k] for k in ['E','N','T','U','V','v']]
v=(E+(s.I-1)*N[0])*U(T[1],s.Rational(7,25),s.Rational(24,25))*v
R=s.Matrix(4,4,lambda i,j:s.simplify(s.I*(v.H*(V.H*N[i]*V*N[j]-N[j]*V.H*N[i]*V)*v)[0]))
B=s.Matrix([[1,0],[0,1],[-1,-1],[0,0]])
print(json.dumps({'R':str(R),'neutral_response':str(B.T*R*B),'symmetric':R==R.T,'v':str(v),'probabilities':[str((v.H*V.H*n*V*v)[0]) for n in N]},indent=2))
