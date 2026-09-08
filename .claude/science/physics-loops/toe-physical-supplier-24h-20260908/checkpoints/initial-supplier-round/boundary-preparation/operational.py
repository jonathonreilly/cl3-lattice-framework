# Independently specified operational supplement; reuses disclosed native matrices.
import contextlib,io,runpy,json,hashlib
from pathlib import Path
import sympy as s
p=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path(str(p/'check.py'))
E,P,N,T=d['E'],d['P'],d['N'],d['T'];Q0,Ufilter=d['Q0'],d['U'];checks={}
def ck(n,b):checks[n]=bool(b);assert b,n
rho=P
for v in range(6):rho=rho*(N[v] if v in [0,2] else E-N[v])
ck('supplied_input_rank1',s.trace(rho)==1 and rho*rho==rho)
pairs=[(3,5,4),(3,5,4),(5,13,12),(7,25,24),(20,29,21),(3,5,4)]
order=[(0,4),(0,1),(1,2),(2,3),(0,3),(0,4)]
rows=[]
for family in range(2):
 r=rho
 for j,(edge,(cn,den,sn)) in enumerate(zip(order,pairs)):
  if family and j==1:cn,den,sn=5,13,12
  c=s.Rational(cn,den);a=s.Rational(sn,den);t=T[edge];u=E-s.I*a*t+(c-1)*t*t
  ck('unitary_'+str(family)+'_'+str(j),u.H*u==E)
  r=u*r*u.H
 ck('reachable_real_'+str(family),r==s.conjugate(r))
 probability=s.trace(N[4]*r);branch=Q0*Ufilter*r*Ufilter.H*Q0;success=s.trace(branch)
 ck('filter_probability_'+str(family),success==1-s.Rational(16,25)*probability)
 ck('nontrivial_bothbranches_'+str(family),0<probability<1 and 0<success<1)
 # After record45=+, B4=Z04, so physical Record04 gives occupation.
 qocc=(E-d['zs'][2])/2
 ck('second_bridge_readout_'+str(family),qocc*Q0==N[4]*Q0)
 posterior=s.trace(qocc*branch)/success
 ck('posterior_odds_'+str(family),posterior==s.Rational(9,25)*probability/success)
 ck('q1_noattenuation_'+str(family),s.trace(Q0*r)==1)
 rows.append({'family':family,'prior_reservoir_occupation':str(probability),'record45_success':str(success),'record04_occupied_given_success':str(posterior)})
ck('family_dependence_not_tuned',rows[0]['record45_success']!=rows[1]['record45_success'])
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'rows':rows,'shared_matrix_source_sha256':hashlib.sha256((p/'check.py').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2))
