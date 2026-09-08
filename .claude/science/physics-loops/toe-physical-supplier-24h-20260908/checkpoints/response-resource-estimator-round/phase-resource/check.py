from pathlib import Path
import sympy as s,numpy as np,json,runpy,contextlib,io,hashlib,itertools
p=Path(__file__).resolve().parent;src=Path('/private/tmp/toe-24h-probes-20260908/phase-preparation')
copy=p/'dimer_input_copy.py';copy.write_bytes((src/'check.py').read_bytes())
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(copy))
checks={}
def ck(n,b):checks[n]=bool(b);assert b,n
rho,P=d['rho'],d['P'];r=s.Rational(3,5);den=(1+r*r)**2
ck('direct_thermal_conjugate_product',rho*s.conjugate(rho)==r**4/den**2*P)
rootF=4*r*r/den;Ig=(1-rootF)/2
ck('dimer_Ig',Ig==s.Rational(32,289));ck('dimer_weighted_Ig',d['weight']*Ig==s.Rational(32,625))
# Exact standard pure conversion calibration, explicit complete instrument.
psi=s.Matrix([s.sqrt(24)/5,s.I/5]);phi=s.Matrix([s.Rational(4,5),3*s.I/5]);K=s.diag(2/(3*s.sqrt(6)),1);L=s.diag(s.sqrt(s.Rational(25,27)),0)
ck('complete_real_filter',K.T*K+L.T*L==s.eye(2));ck('exact_pure_success',s.simplify(K*psi-phi/3)==s.zeros(2,1))
ck('failure_real',s.im((L*psi)[0])==0 and (L*psi)[1]==0)
ck('optimal_Ig_ratio',s.Rational(1,25)/s.Rational(9,25)==s.Rational(1,9))
ck('dropping_success_weight_wrong',s.Rational(9,25)>s.Rational(1,25))
# Rare strong phase: mean phase squared is NOT a valid replacement for worst-layer budget.
rare=s.Rational(1,100);ck('mean_budget_square_counterexample',float(rare/2)>float((rare*s.pi/4)**2))
rows=[]
for family,weights in enumerate([(1,2,3),(2,1,2)]):
 h=np.diag(weights,1)+np.diag(weights,-1);eps=np.linalg.eigvalsh(h)
 energies=np.array([sum(eps[j] for j in range(4) if mask>>j&1) for mask in range(16)])
 for beta in [0.,.7,2.]:
  Z=float(sum(np.exp(-beta*energies)));ig=(1-16/Z)/2
  prod=float(np.prod(1+np.exp(-beta*eps)));ck(f'partition_census_{family}_{beta}',abs(Z-prod)<1e-8)
  probs=np.exp(-beta*energies)/Z;reverse=np.exp(beta*energies)/Z
  R=float(np.sum(abs(probs-reverse))/2)
  directig=float(sum((np.cosh(beta*e)-1)/Z for e in energies if e>1e-12))
  ck(f'real_blocks_Ig_{family}_{beta}',abs(ig-directig)<1e-13)
  ck(f'robustness_lower_{family}_{beta}',ig+1e-13>=(1-np.sqrt(max(0,1-R*R)))/2)
  success=float(np.prod((1+np.exp(-beta*abs(eps)))/2))
  lower=float(np.arcsin(np.sqrt(success*ig))) if beta else 0.
  rows.append({'family':family,'beta':beta,'dimension':16,'partition':Z,'Ig':ig,'robustness':R,'actual_success':success,'necessary_layer_phase_budget':lower,'denominator_zero':beta==0})
ck('wrong_Gibbs_dimension_rejected',float((1-8/rows[1]['partition'])/2)!=rows[1]['Ig'])
out={'status':'PASS','checks':checks,'count':len(checks),'exact_dimer_Ig':str(Ig),'exact_dimer_pIg':str(d['weight']*Ig),'pure_calibration_success':'1/9','rows':rows,'input_dimer_sha256':hashlib.sha256((src/'check.py').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(out,indent=2))
