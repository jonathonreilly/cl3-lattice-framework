from pathlib import Path
import sympy as s,json,hashlib
m=5;d=1<<m;I=s.eye(d)
def annihilate(j):
 a=s.zeros(d)
 for bits in range(d):
  if bits>>j&1:a[bits^(1<<j),bits]=(-1)**((bits&((1<<j)-1)).bit_count())
 return a
c=[annihilate(j) for j in range(m)];n=[a.H*a for a in c]
def hop(i,j):return c[i].H*c[j]+c[j].H*c[i]
def pulse(t,co,si):return I+(co-1)*t*t-s.I*si*t
T=hop(0,1);D=n[0]-n[1];Ua=pulse(hop(0,2),s.Rational(3,5),s.Rational(4,5));Ub=pulse(hop(1,3),s.Rational(3,5),s.Rational(4,5))
U=pulse(T,s.sqrt(2)/2,s.sqrt(2)/2);R=pulse(D,s.sqrt(2)/2,s.sqrt(2)/2);W=s.simplify(R*U)
idx=[x for x in range(d) if x.bit_count()%2==0 and not (x>>2&1) and x>>3&1];J=I[:,idx];P=J*J.H
r=s.Rational(3,5);F=(T*T-T)/2+r*(I-T*T)+r*r*(T*T+T)/2
checks={}
def eq(name,a,b):checks[name]=s.simplify(a-b)==s.zeros(*a.shape);assert checks[name],name
eq('CAR_phase_rotation_sign',W*D*W.H,T)
# Direct survival projections independently give diagonal occupation attenuations.
eq('vacant_leaf_survival', (I-n[2])*Ua*J, (I+(r-1)*n[0])*J)
eq('filled_leaf_survival',n[3]*Ub*J,(r*I+(1-r)*n[1])*J)
branch={}
for a in [0,1]:
 for b in [0,1]:
  Qa=n[2] if a else I-n[2]; Qb=n[3] if b else I-n[3]
  K=s.simplify(W*Qb*Ub*Qa*Ua*W.H*J);branch[str(a)+str(b)]=K
  eq('leaf2_permanent_'+str(a)+str(b),n[2]*K,a*K)
  eq('leaf3_permanent_'+str(a)+str(b),n[3]*K,b*K)
eq('all_four_CAR_branch_completeness',sum((K.H*K for K in branch.values()),s.zeros(4)),s.eye(4))
eq('whole_success_CAR_Kraus',branch['01'],F*J)
N=sum(n,s.zeros(d));eq('all_pulses_preserve_N',N*W,W*N)
eq('second_pulse_preserves_first_leaf_record',Ub*n[2],n[2]*Ub)
eq('final_rotation_preserves_leaf2',W*n[2],n[2]*W)
eq('final_rotation_preserves_leaf3',W*n[3],n[3]*W)
# Entangled ready input: half of an unnormalized four-dimensional identity-vector.
def vec_columns(A):return s.Matrix([A[i,j]/2 for j in range(4) for i in range(d)])
eq('maximally_entangled_reference_success',vec_columns(branch['01']),vec_columns(F*J))
prob={k:s.simplify(s.trace(K.H*K)/4) for k,K in branch.items()}
checks['complete_probabilities']=prob=={'00':s.Rational(136,625),'01':s.Rational(289,625),'10':s.Rational(64,625),'11':s.Rational(136,625)};assert checks['complete_probabilities']
rho=branch['01']*branch['01'].H/(4*prob['01']); energy=s.simplify(s.trace(T*rho))
checks['initial_not_target_thermal']=s.trace(T*P/4)==0 and energy==-s.Rational(8,17);assert checks['initial_not_target_thermal']
out={'representation':'independent occupation-bit CAR, no author matrix import','checks':checks,'TOTAL':len(checks),'ready_occupation_indices':idx,'probabilities':{k:str(v) for k,v in prob.items()},'conditional_energy':str(energy),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('INDEPENDENT_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
