import sympy as s,json,hashlib
from pathlib import Path
I=s.eye(2);Z=s.diag(1,-1);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]])
c,v,t=s.symbols('c v t',real=True);a,b,z=s.symbols('a b z',real=True)
# Independent Bloch-form adjoint of attenuation: output z=1-t²+t²zin, x=t xin.
# R†P1R=(I+(2cv)X+(v²-c²)Z)/2 when c²+v²=1.
# Thus effect scalar midpoint v²+(c²-v²)t²/2, Bloch vector(cv*t,0,(v²-c²)t²/2).
mid=v*v+(c*c-v*v)*t*t/2
bloch=s.Matrix([[mid+(v*v-c*c)*t*t/2,c*v*t],[c*v*t,mid-(v*v-c*c)*t*t/2]])
checks={}
def ck(n,x):checks[n]=bool(x);assert x,n
ck('effect_from_Bloch',s.expand(bloch-s.Matrix([[v*v,c*v*t],[c*v*t,v*v+(c*c-v*v)*t*t]]))==s.zeros(2))
delta=4*c*c*v*v*t*t+(c*c-v*v)**2*t**4
ck('diameter_fixed',s.simplify(delta.subs({c:s.Rational(3,5),v:s.Rational(4,5),t:s.Rational(3,5)}))==s.Rational(81*1649,625**2))
# General local-code condition in sigma eigenbasis, minimal rest with both signs.
a,b,c1,d=s.symbols('a b c1 d');K=s.Matrix([[a,b],[c1,d]]);S=s.kronecker_product(Z,Z)
pp=(s.eye(4)+S)/2;pm=s.eye(4)-pp;leak=pm*s.kronecker_product(K,I)*pp
ck('local_leak_exact',set(x for x in leak if x!=0)=={b,c1})
# Reconstruct physical square from graph ordering, not hardcoded stabilizer.
edges=[(0,1),(1,2),(2,3),(0,3)];E=s.eye(16)
def w(k,M):return s.kronecker_product(*[M if j==k else I for j in range(4)])
zs=[w(k,Z) for k in range(4)];xs=[w(k,X) for k in range(4)]
def A(u,v):
 if u>v:return -A(v,u)
 k=edges.index((u,v));o=xs[k]
 for i,j in [(u,v),(v,u)]:
  for l,e in enumerate(edges):
   if i in e and e!=edges[k] and (e[1] if e[0]==i else e[0])<j:o=o*zs[l]
 return o
cycle=A(0,1)*A(1,2)*A(2,3)*A(3,0)
ck('native_cycle_dictionary',cycle==-s.kronecker_product(X,Y,X,Y))
P=(E+cycle)/2;vac=P
for vertex in range(4):
 B=s.prod([zs[j] for j,e in enumerate(edges) if vertex in e],start=E);vac=vac*(E+B)/2
om=s.zeros(16,1);om[0]=om[15]=1/s.sqrt(2)
ck('native_vacuum',vac==om*om.H)
# Direct density entries of the reduced rest, then replacement, not author Kraus routine.
rest=s.zeros(8)
for i in range(8):
 for j in range(8):rest[i,j]=vac[i,j]+vac[8+i,8+j]
out=s.kronecker_product(s.diag(1,0),rest)
ck('cycle_survival',s.trace(P*out)==s.Rational(1,2));ck('vacuum_survival',s.trace(vac*out)==s.Rational(1,4))
# Every target output density after replacement still has only half code weight.
x,y,z=s.symbols('x y z',real=True);sig=s.Matrix([[x,y+s.I*z],[y-s.I*z,1-x]])
ck('any_replacement_cycle_half',s.simplify(s.trace(P*s.kronecker_product(sig,rest)))==s.Rational(1,2))
residual=s.sqrt(2)*(s.kronecker_product(K,s.eye(8))*om-a*om)
ck('full_Schmidt_stabilizer_forces_scalar',set(s.simplify(x) for x in residual if x!=0)=={b,c1,d-a})
print(json.dumps({'status':'PASS','checks':checks,'count':len(checks),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
