"""Exact physical edge-qubit preparation probe; all physical controls are supplied."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NATIVE_PRODUCT_GIBBS_PREPARATION_NOTE_2026-09-08.md",
    "docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/NATIVE_EDGE_RECORD_LOCAL_CYCLE_TRANSPORT_AND_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md",
)
import os
for resource_variable in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[resource_variable] = "1"
from pathlib import Path
receipt = Path(__file__).resolve().parents[1] / "outputs" / "native_product_gibbs_dimer_2026_09_08.json"
receipt.parent.mkdir(parents=True, exist_ok=True)
from pathlib import Path
import hashlib,json
import sympy as s
from functools import reduce

I2=s.eye(2); X=s.Matrix([[0,1],[1,0]]); Z=s.diag(1,-1)
edges=[(0,1),(0,2),(1,3),(0,4)]
coords=[(0,0,0),(1,0,0),(0,1,0),(1,1,0),(0,0,1)]
L=len(edges); Id=s.eye(2**L)
def site(op,k):
 return s.kronecker_product(*[op if j==k else I2 for j in range(L)])
zz=[site(Z,k) for k in range(L)];xx=[site(X,k) for k in range(L)]
B=[]
for v in range(5):
 B.append(reduce(lambda a,b:a*b,[zz[k] for k,e in enumerate(edges) if v in e],Id))
n=[(Id-b)/2 for b in B]
T=[];AA=[]
for k,(i,j) in enumerate(edges):
 a=xx[k]
 for v,w in ((i,j),(j,i)):
  for q,e in enumerate(edges):
   if v in e and e!=edges[k]:
    other=e[1] if e[0]==v else e[0]
    if other<w:a=a*zz[q]
 AA.append(a)
 T.append(s.I*a*(B[i]-B[j])/2)
checks={}
def zero(m):return all(s.simplify(x)==0 for x in m)
def check(name,p):
 checks[name]=bool(p)
 if not p:raise AssertionError(name)

def pulse(t,c,v):return Id+(c-1)*t*t-s.I*v*t
r=s.Rational(3,5);v=s.Rational(4,5)
for k,t in enumerate(T):
 check(f'hopping_{k}_hermitian',zero(t-t.H))
 check(f'hopping_{k}_cubic',zero(t**3-t))
 check(f'hopping_{k}_imaginary',zero(t+s.conjugate(t)))
check('global_even_parity',zero(reduce(lambda a,b:a*b,B,Id)-Id))
centers=[tuple(coords[i][a]+coords[j][a] for a in range(3)) for i,j in edges]
check('physical_centers_distinct',len(set(centers))==L)
check('virtual_edges_nearest_neighbor',all(sum(abs(coords[i][a]-coords[j][a]) for a in range(3))==1 for i,j in edges))
P=(Id-n[2])*n[3]
check('ready_rank_four',s.trace(P)==4)
check('ready_projector',zero(P*P-P))
check('leaf_occupation_is_single_physical_Z',zero(B[2]-zz[1]) and zero(B[3]-zz[2]))
D=n[0]-n[1];t=T[0]
U=pulse(t,s.sqrt(2)/2,s.sqrt(2)/2)
R=Id+(s.sqrt(2)/2-1)*D*D-s.I*s.sqrt(2)/2*D
W=s.simplify(R*U)
check('basis_rotation_unitary',zero(W.H*W-Id))
check('basis_rotation_D_to_hopping',zero(W*D*W.H-t))
Ua=pulse(T[1],r,v);Ub=pulse(T[2],r,v)
check('vacant_leaf_pulse_unitary',zero(Ua.H*Ua-Id))
check('filled_leaf_pulse_unitary',zero(Ub.H*Ub-Id))
Pm=(t*t-t)/2;Pp=(t*t+t)/2;Pz=Id-t*t
F=Pm+r*Pz+r*r*Pp
for label,eig,proj,mult in [('minus',-1,Pm,1),('zero',0,Pz,r),('plus',1,Pp,r*r)]:
 check(f'projector_{label}',zero(proj*proj-proj) and zero(t*proj-eig*proj))
 check(f'transfer_{label}',zero(F*proj-mult*proj))
 check(f'ready_multiplicity_{label}',s.trace(P*proj)==(2 if eig==0 else 1))
branches={};normal=Id*0
for a in (0,1):
 for b in (0,1):
  Qa=(Id-n[2]) if a==0 else n[2]
  Qb=(Id-n[3]) if b==0 else n[3]
  K=s.simplify(W*Qb*Ub*Qa*Ua*W.H*P)
  key=f'{a}{b}';branches[key]=K;normal+=K.H*K
  check(f'branch_{key}_output_leaf_values',zero(Qa*K-K) and zero(Qb*K-K))
check('complete_instrument_on_ready_inputs',zero(normal-P))
K=branches['01']
check('success_actual_Kraus_operator',zero(K-F*P))
check('old_leaf_records_commute_final_rotation',zero(W*zz[1]-zz[1]*W) and zero(W*zz[2]-zz[2]*W))
check('success_Kraus_positive_on_ready',zero(K-K.H) and all(e>=0 for e in K.eigenvals()))
weight=s.simplify(s.trace(K*K.H)/4)
check('success_probability_from_spectral_target',weight==s.Rational(289,625))
rho=s.simplify(K*K.H/(4*weight))
check('successful_density_normalized',s.trace(rho)==1)
check('successful_energy',s.simplify(s.trace(t*rho))==-s.Rational(8,17))
check('output_has_nonreal_coherence',not zero(rho-s.conjugate(rho)))
check('thermal_spectral_identity',zero(rho-F*F*P/s.trace(F*F*P)))
prob={k:s.simplify(s.trace(x*x.H)/4) for k,x in branches.items()}
check('all_outcome_probabilities_sum_one',sum(prob.values())==1)
# Actual control changes, retaining the same independently specified target.
K_no_phase=s.simplify(U*n[3]*Ub*(Id-n[2])*Ua*U.H*P)
K_wrong_phase=s.simplify((R.H*U)*n[3]*Ub*(Id-n[2])*Ua*(R.H*U).H*P)
check('adverse_missing_phase_changes_Kraus',not zero(K_no_phase-F*P))
check('adverse_wrong_phase_changes_Kraus',not zero(K_wrong_phase-F*P))
Ua_bad=pulse(T[1],s.Rational(4,5),s.Rational(3,5))
K_bad=s.simplify(W*n[3]*Ub*(Id-n[2])*Ua_bad*W.H*P)
check('adverse_changed_attenuation_changes_Kraus',not zero(K_bad-F*P))
Pswap=n[2]*(Id-n[3])
Kswap=s.simplify(W*(Id-n[3])*Ub*n[2]*Ua*W.H*Pswap)
check('adverse_swapped_ready_values_changes_Kraus',not zero(Kswap-F*Pswap))
result={'status':'PASS','source_main':'2b42ebe4b6b4ee76b0fa1b8e668ad7775e946307','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'TOTAL':{'PASS':len(checks),'FAIL':0},'physical_edge_centers':centers,'ready_rank':str(s.trace(P)),'success_probability':str(weight),'conditional_energy':str(s.simplify(s.trace(t*rho))),'all_branch_probabilities':{k:str(p) for k,p in prob.items()},'physical_scope':'Supplied phase/hopping pulses, diagonal ready preparation and native Born/Lueders leaf events; no primitive formation or action selection derived.'}
receipt.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
