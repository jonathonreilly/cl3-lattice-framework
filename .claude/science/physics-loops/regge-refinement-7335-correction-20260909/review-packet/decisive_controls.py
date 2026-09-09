import sys,numpy as np,json
from pathlib import Path
W=Path('/Users/jonreilly/Projects/Physics-worktrees/review-backlog-regge-refinement-7335-20260909');sys.path.insert(0,str(W/'scripts'))
import admissibility_regge_tt_record_observable_inverse_amplification_refinement_gate_2026_08_23 as p
# Analytic independent formula: metric edge integration, gauge = M sym(ik tensor xi).
worst=0.
for L in [5,7,9,11]:
 for m in [1,2]:
  for ax in [0,1]:
   k=np.eye(4)[ax]*2*np.pi*m/L; M=p.regge.metric_map(k); G=p.regge.gauge_map(k)
   T=np.array([[1j*(k[a]*(b==j)+k[b]*(a==j)) for j in range(4)] for a,b in p.regge.HCOMPS])
   worst=max(worst,float(np.linalg.norm(M@T-G)))
   assert np.linalg.matrix_rank(M)==10
assert worst<1e-12
print('independent metric-to-displacement factorization residual',worst,flush=True)
# Dense block inverse identity with indefinite Schur and negative definite fixed block.
A=-np.diag([2.,3.,4.]); B=np.arange(6).reshape(3,2)/7; S=np.diag([-1.,2.]);D=S+B.T@np.linalg.solve(A,B)
O=np.arange(10).reshape(5,2)/9; F=O[:3].T@np.linalg.solve(A,O[:3]); Z=O[3:]-B.T@np.linalg.solve(A,O[:3]); C=Z.T@np.linalg.solve(S,Z)
assert np.allclose(O.T@np.linalg.solve(np.block([[A,B],[B.T,D]]),O),F+C)
lo,hi,gap=p.generalized_phase_spectrum(F,C); assert np.isfinite([lo,hi]).all()
print('indefinite Schur / negative definite phase control',lo,hi,flush=True)
# The final L5 runner is bounded, unlike predecessor long period campaigns.
raise SystemExit(p.main())
