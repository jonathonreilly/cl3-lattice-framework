import time,signal,json,sys,resource,hashlib
from pathlib import Path
start=time.monotonic();signal.alarm(180)
import sympy as s
p=Path(__file__).parent/'result.json';r=json.loads(p.read_text())
import ast
X=[(e+1)*s.diag(1,-1,0)+(1+e%3)*s.Matrix([[0,1,0],[1,0,0],[0,0,0]])+(1+e%2)*s.Matrix([[0,-s.I,0],[s.I,0,0],[0,0,0]]) for e in range(17)]
direct=[0]*5
for word,w in zip(r['words'],r['weights']):
 A=[s.eye(3)]+[s.zeros(3) for _ in range(4)]
 for e,sg in word:
  F=[(s.I*sg)**n*X[e]**n/s.factorial(n) for n in range(5)]
  A=[sum((A[k]*F[n-k] for k in range(n+1)),s.zeros(3)) for n in range(5)]
 for n in (3,4):direct[n]-=s.Rational(w)*s.re(s.trace(A[n]))/3
cubic=0
for key,c in r['cubic_coefficients'].items():
 u,v,w=ast.literal_eval(key);cubic+=s.Rational(c)*s.trace(X[u]*(X[v]*X[w]-X[w]*X[v]))/s.I
quartic=0
for key,c in r['quartic_coefficients'].items():
 a,b,c1,d=ast.literal_eval(key);quartic+=s.Rational(c)*s.re(s.trace(X[a]*X[b]*X[c1]*X[d]))
assert s.simplify(cubic-direct[3])==0
assert s.simplify(quartic-direct[4])==0
out=dict(status='PASS',TOTAL=2,checks=['all22 ordered face cubic matches direct matrix-series convolution','all22 ordered face quartic matches direct matrix-series convolution'],direct_cubic=str(direct[3]),direct_quartic=str(direct[4]),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),actual_input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),seconds=time.monotonic()-start,rss_MiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024))
assert out['seconds']<180 and out['rss_MiB']<180
print(json.dumps(out,indent=2))
