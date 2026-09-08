import sympy as s,json
# Independently construct occupation response in the one-active-particle sector.
I=s.eye(3);n=[s.diag(*[int(i==j) for i in range(3)]) for j in range(3)]
def hop(i,j):
 a=s.zeros(3);a[i,j]=a[j,i]=1;return a
def pulse(i,j,c,r):
 t=hop(i,j);return I-s.I*r*t+(c-1)*t*t
U=pulse(0,1,s.Rational(3,5),s.Rational(4,5));W=pulse(1,2,s.Rational(7,25),s.Rational(24,25));V=pulse(0,1,s.Rational(5,13),s.Rational(12,13))*W
psi=s.diag(s.I,1,1)*W*U*s.Matrix([1,0,0]);q=s.symbols('s0:3',real=True);l=s.symbols('l0:3',real=True)
a=V*s.diag(*[s.exp(s.I*x) for x in q])*psi;p=[s.expand(x*s.conjugate(x)) for x in a];z=dict.fromkeys(q,0);ck={}
def check(k,b):ck[k]=bool(b);assert b,k
check('all_sources_normalized',s.simplify(sum(p)-1)==0)
R=s.Matrix(3,3,lambda i,j:s.simplify(s.diff(p[i],q[j]).subs(z)));C=s.Matrix([[1,0],[0,1],[-1,-1]]);N=C.T*R*C
check('neutral_curl',N[1,0]-N[0,1]==s.Rational(497664,528125));check('neutral_symmetric_determinant',((N+N.T)/2).det()==-s.Rational(61917364224,278916015625))
check('row_and_column_zero',R*s.ones(3,1)==s.zeros(3,1) and s.ones(1,3)*R==s.zeros(1,3))
F=sum(s.exp(s.I*l[i])*p[i] for i in range(3))
check('all_mixed_derivatives',all(s.simplify(-s.I*s.diff(F,l[i],q[j]).subs({**z,**dict.fromkeys(l,0)}))==R[i,j] for i in range(3) for j in range(3)))
x,y=s.symbols('x y',real=True);neutral=dict(zip(q,C*s.Matrix([x,y])));m=C.T*s.Matrix(p);curl=s.diff(m[1].subs(neutral),x)-s.diff(m[0].subs(neutral),y)
check('actual_neutral_function_curl',s.simplify(curl.subs({x:0,y:0}))==N[1,0]-N[0,1])
# Actual derivative of doubled amplitude kernel, not just positive p0 assertion.
t=s.symbols('t',real=True);r=s.symbols('r0:3',real=True);ar=a.subs(dict(zip(q,r)));Gamma=sum(a[i]*s.conjugate(ar[i]) for i in range(3));Gamma2=Gamma+(s.exp(s.I*t*(q[0]-r[0]))-1)*a[0]*s.conjugate(ar[0]);origin={**z,**dict.fromkeys(r,0)}
check('cross_kernel_derivative',s.simplify(s.diff(Gamma2-Gamma,q[0]).subs(origin))==s.I*t*s.Rational(727778241,1650390625))
check('equal_source_kernel_unchanged',s.simplify((Gamma2-Gamma).subs(dict(zip(r,q))))==0)
# Literal Pauli/Fock full-space equivalence via an independently solved basis phase map.
z2=s.diag(1,-1);x2=s.Matrix([[0,1],[1,0]]);eye=s.eye(2);Z=[s.kronecker_product(*[z2 if k==j else eye for k in range(3)]) for j in range(3)];X=[s.kronecker_product(*[x2 if k==j else eye for k in range(3)]) for j in range(3)]
B=[Z[0],Z[0]*Z[1],Z[1]*Z[2],Z[2]];A=[X[0],X[1]*Z[0],X[2]*Z[1]];T=[s.I*A[j]*(B[j]-B[j+1])/2 for j in range(3)]
basis=[b for b in range(16) if b.bit_count()%2==0];phys={b:next(k for k in range(8) if all(B[j][k,k]==1-2*((b>>j)&1) for j in range(4))) for b in basis}
phases={};Ts=[]
for j in range(3):
 mat=s.zeros(8)
 for c,b in enumerate(basis):
  if ((b>>j)&1)!=((b>>(j+1))&1):mat[basis.index(b^(3<<j)),c]=1
 Ts.append(mat)
for seed in basis:
 if seed in phases:continue
 phases[seed]=1;todo=[seed]
 while todo:
  b=todo.pop()
  for j in range(3):
   if ((b>>j)&1)==((b>>(j+1))&1):continue
   dest=b^(3<<j);value=T[j][phys[dest],phys[b]]*phases[b]
   if dest in phases:assert phases[dest]==value
   else:phases[dest]=value;todo.append(dest)
S=s.zeros(8)
for col,b in enumerate(basis):S[phys[b],col]=phases[b]
check('full_intertwiner_unitary',S.H*S==s.eye(8))
for j in range(3):check('native_hop_'+str(j),S.H*T[j]*S==Ts[j])
for j in range(4):check('native_occupation_'+str(j),S.H*(s.eye(8)-B[j])*S/2==s.diag(*[(b>>j)&1 for b in basis]))
check('all_eight_history_dictionary',len(set(phys.values()))==8)
# Adverse controls: index transpose and omitted preparation phase must fail exact response.
check('transpose_mutation_detected',R!=R.T)
ps0=W*U*s.Matrix([1,0,0]);R0=s.Matrix(3,3,lambda i,j:s.simplify(s.I*(ps0.H*(V.H*n[i]*V*n[j]-n[j]*V.H*n[i]*V)*ps0)[0]));check('omitted_phase_mutation_detected',R0==s.zeros(3) and R0!=R)
print(json.dumps({'count':len(ck),'checks':ck,'R':str(R),'neutral':str(N),'intertwiner':str(S),'probabilities':[str(s.simplify(v.subs(z))) for v in p]},indent=2))
