import sympy as s,json,hashlib
from pathlib import Path
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1)
edges=[(0,1),(0,3),(0,4),(1,2),(2,3),(4,5)];n=len(edges);E=s.eye(2**n)
def op(k,a):return s.kronecker_product(*[a if j==k else I for j in range(n)])
zs=[op(j,Z) for j in range(n)];xs=[op(j,X) for j in range(n)]
B={v:s.prod([zs[k] for k,e in enumerate(edges) if v in e],start=E) for v in range(6)}
def A(u,v):
 if u>v:return -A(v,u)
 k=edges.index((u,v));a=xs[k]
 for i,j in [(u,v),(v,u)]:
  for l,e in enumerate(edges):
   if i in e and e!=edges[k] and (e[1] if e[0]==i else e[0])<j:a=a*zs[l]
 return a
T={e:s.I*A(*e)*(B[e[0]]-B[e[1]])/2 for e in edges}
S=A(0,1)*A(1,2)*A(2,3)*A(3,0);P=(E+S)/2
N={v:(E-B[v])/2 for v in range(6)}
Pin=P*(E-N[5]);t=T[4,5];c=s.Rational(3,5);r=s.Rational(3,5)
U=E-s.I*r*t+(c-1)*t*t;Q0=E-N[5];Q1=N[5]
K=E+(c-1)*N[4];H=T[0,1]+2*T[1,2]+3*T[2,3]+4*T[0,3]
checks={}
def ck(k,b):checks[k]=bool(b);assert b,k
ck('code_real',s.conjugate(P)==P);ck('code_projector',P*P==P);ck('code_rank32',s.trace(P)==32);ck('empty_leaf_input_rank16',s.trace(Pin)==16)
ck('all_hops_pure_imaginary',all(s.conjugate(v)==-v for v in T.values()))
ck('all_hops_hermitian',all(v.H==v for v in T.values()))
ck('used_leaf_cubic',t**3==t);ck('leaf_unitary',U.H*U==E);ck('leaf_unitary_real',s.conjugate(U)==U)
ck('success_full_branch',Q0*U*Pin==K*Pin)
ck('failure_full_branch',Q1*U*Pin==-s.I*r*t*Pin)
ck('success_effect',Pin*U.H*Q0*U*Pin==Pin*(E+(c*c-1)*N[4]))
ck('failure_effect',Pin*U.H*Q1*U*Pin==r*r*Pin*N[4])
ck('complete_instrument',Pin*U.H*(Q0+Q1)*U*Pin==Pin)
ck('matter_hamiltonian_preserved',H*U==U*H and H*Q0==Q0*H)
ck('old_cycle_preserved',P*U==U*P)
ck('success_is_registered_Z',Q0==(E+zs[5])/2)
ck('q_half_amplitude_mutation_rejected',Q0*U*Pin!=(E+(c*c-1)*N[4])*Pin)
ck('unconditional_reset_mutation_rejected',Q1*U*Pin!=s.zeros(64))
h=s.zeros(4)
for (i,j),w in [((0,1),1),((1,2),2),((2,3),3),((0,3),4)]:h[i,j]=h[j,i]=w
x=s.symbols('x');poly=h.charpoly(x).as_expr();ck('connected_nondegenerate',s.gcd(poly,s.diff(poly,x))==1 and poly.subs(x,0)!=0)
# Exact Gibbs input comparison is evaluated, NOT declared physically prepared.
F1=lambda a:E-s.Rational(3,4)*a+s.Rational(1,4)*a*a
F2=lambda a:E-s.Rational(15,8)*a+s.Rational(9,8)*a*a
for idx,(a,F,beta) in enumerate([(T[0,1],F1,1),(T[2,3],F2,2)]):
 for lam,proj in [(-1,(a*a-a)/2),(0,E-a*a),(1,(a*a+a)/2)]:ck('exp_spectral_'+str(idx)+'_'+str(lam),F(a)*proj==2**s.Integer(-beta*lam)*proj)
G=Pin*F1(T[0,1])*F2(T[2,3]);z=s.trace(G);rho=G/z;hd=T[0,1]+2*T[2,3]
ck('thermal_nonreal',rho!=s.conjugate(rho));ck('thermal_conjugation_reverses_H',s.conjugate(G)==Pin*F1(-T[0,1])*F2(-T[2,3]))
energy=s.simplify(s.trace(hd*rho));ck('thermal_energy_negative',energy<0)
realrho=Pin/16;ck('real_input_energy_zero',s.trace(hd*realrho)==0)
p0=s.trace(Q0*U*rho*U.H);ck('born_q_formula',p0==1-(1-c*c)*s.trace(N[4]*rho))
ck('nonthermal_input_success',s.trace(Q0*U*realrho*U.H)==s.Rational(17,25))
# A diagonal phase is an explicitly supplied escape from the real control class.
V=E+(s.I-1)*N[4]
ck('diagonal_phase_outside_class',V!=s.conjugate(V) and V.H*V==E)
out={'status':'PASS','checks':checks,'count':len(checks),'connected_characteristic_polynomial':str(poly),'prereg_wrong_eigenvalue_radicand':221,'correct_radicand':200,'gibbs_comparison':{'trace':str(z),'energy':str(energy),'filter_success':str(p0)},'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(out,indent=2))
