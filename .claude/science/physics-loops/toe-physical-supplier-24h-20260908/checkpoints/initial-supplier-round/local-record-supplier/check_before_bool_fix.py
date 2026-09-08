import sympy as S,json,hashlib
from pathlib import Path
I=S.eye(2);P0=S.diag(1,0);P1=S.diag(0,1);X=S.Matrix([[0,1],[1,0]]);Y=S.Matrix([[0,-S.I],[S.I,0]]);Z=S.diag(1,-1)
checks=[]
def ck(n,b):
 if not b:raise AssertionError(n)
 checks.append(n)
def channel(a,ks):return sum((k*a*k.H for k in ks),S.zeros(a.rows))
t=S.symbols('t',nonnegative=True);c,s=S.symbols('c s',real=True)
K0=S.diag(1,t);K1=S.Matrix([[0,S.sqrt(1-t*t)],[0,0]])
R=S.Matrix([[c,-s],[s,c]])
a=S.symbols('a',real=True);K1formal=S.Matrix([[0,a],[0,0]])
E=S.expand(K0.H*R.H*P1*R*K0+K1formal.H*R.H*P1*R*K1formal).subs(a*a,1-t*t)
expected=S.Matrix([[s*s,c*s*t],[c*s*t,s*s+(c*c-s*s)*t*t]])
ck('symbolic effective measured effect',S.simplify(E-expected)==S.zeros(2))
ck('symbolic diameter squared',S.expand((E[0,0]-E[1,1])**2+4*E[0,1]**2-(4*s*s*c*c*t*t+(c*c-s*s)**2*t**4))==0)
rows=[]
for cv,sv in [(S.Rational(3,5),S.Rational(4,5)),(S.Rational(4,5),S.Rational(3,5))]:
 for tv in [S.Integer(0),S.Rational(3,5),S.Integer(1)]:
  ks=[k.subs(t,tv) for k in [K0,K1]];rr=R.subs({c:cv,s:sv});ee=E.subs({c:cv,s:sv,t:tv})
  ck('Kraus complete'+str((cv,tv)),sum((k.H*k for k in ks),S.zeros(2))==I)
  ck('rotation unitary'+str((cv,tv)),rr.H*rr==I)
  ck('effect positive and bounded'+str((cv,tv)),all(v.is_nonnegative for v in ee.eigenvals()) and all((1-v).is_nonnegative for v in ee.eigenvals()))
  rows.append({'cos':str(cv),'sin':str(sv),'residual_amplitude':str(tv),'effect':str(ee),'probability_diameter':str(S.sqrt(4*sv**2*cv**2*tv**2+(cv**2-sv**2)**2*tv**4))})
# Exact complete-reference replacement identity on full basis of target plus reference.
reset=[K0.subs(t,0),K1.subs(t,0)]
for i in range(2):
 for j in range(2):
  e=S.zeros(2);e[i,j]=1
  for a in range(2):
   for b in range(2):
    f=S.zeros(2);f[a,b]=1
    actual=channel(S.kronecker_product(e,f),[S.kronecker_product(k,I) for k in reset])
    ck('reference matrixunit '+str((i,j,a,b)),actual==S.kronecker_product(P0,f)*(i==j))
# Actual local exchange isometry target,sink, followed by copying target to fragment.
for tv in [S.Integer(0),S.Rational(3,5),S.Integer(1)]:
 av=S.sqrt(1-tv**2);U=S.Matrix([[1,0,0,0],[0,tv,av,0],[0,-av,tv,0],[0,0,0,1]])
 ck('exchange unitary'+str(tv),U.H*U==S.eye(4))
 # selected columns for input sink0: |00>,|10>; extracted sink Kraus equal K0/K1.
 ck('exchange realizes Kraus'+str(tv),U.extract([0,2],[0,2])==K0.subs(t,tv) and U.extract([1,3],[0,2])==K1.subs(t,tv))
V=S.Matrix([[1,0],[0,0],[0,0],[0,1]])
Qbad=S.kronecker_product(P0,P1)+S.kronecker_product(P1,P0)
ck('copy isometry',V.H*V==I);ck('zero mismatch operator allinputs',Qbad*V==S.zeros(4,2))
# Actual BKSF square vacuum and code, root geometry already established.
Ssq=-S.kronecker_product(X,Y,X,Y);Pc=(S.eye(16)+Ssq)/2
om=S.zeros(16,1);om[0]=om[15]=1/S.sqrt(2);rho=om*om.H
ck('initial actual cycle code',Pc*om==om)
leaked=channel(rho,[S.kronecker_product(k,S.eye(8)) for k in reset])
ck('replacement cycle survival exactlyhalf',S.trace(Pc*leaked)==S.Rational(1,2))
ck('replacement original vacuum survival exactlyquarter',S.trace(rho*leaked)==S.Rational(1,4))
# Reconnecting discarded memory can undo the causal break: exact SWAP twice.
SW=S.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
ck('returned sink restores old bit',SW*SW*S.Matrix([0,0,1,0])==S.Matrix([0,0,1,0]))
ck('sink not fresh changes reset result',SW*S.Matrix([0,1,0,0])==S.Matrix([0,0,1,0]))
# Wrong pointer gives same fair marginal but anti-correlated joint outcomes.
Vwrong=S.kronecker_product(I,X)*V
ck('wrong calibration actual mismatch',Qbad*Vwrong==Vwrong)
# Nonzero residual amplitude retains distinguishability (all chosen nontrivial settings).
ck('partial reset history alias remains',all(r['probability_diameter']!='0' for r in rows if r['residual_amplitude']!='0'))
out={'status':'PASS','assertions':len(checks),'checks':checks,'rows':rows,'native_code_survival':'1/2','native_vacuum_survival':'1/4','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(out,indent=2))
