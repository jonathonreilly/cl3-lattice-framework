"""New-q posterior assembly from certified inert inputs; no saved-data access."""
from fractions import Fraction as F
import arithmetic as a
import interval as I
import assembly as A

def real(x):return F(x[0][0],a.S),F(x[0][1],a.S)
def finish(p,trials,jets,first_squared,a_squared,old_alpha,emit=lambda *_:None):
 nominal=a.ZERO
 for left,right,opposite,multiplicity in A.SIGNATURES:
  # Signature identifiers are (left C,right A,opposite count).
  key=(left,right,opposite)
  value=A.nominal(jets[key],p[left],p[right],trials[right]['q'],emit)
  nominal=a.add(nominal,A.scaled(value,F(multiplicity)))
 emit('ordered_sum_raw',{'complex_value':nominal,'words':90})
 E2=I.point(0);F2=I.point(0);b2=I.point(0)
 for kind,mult in(('P',12),('O',3)):
  e2=first_squared[kind]
  if type(e2)is not F or e2<0:raise ValueError('same-p first bound')
  u=I.root((F(0),e2));eta=I.root(I.nonnegative(real(trials[kind]['eta'])))
  v=I.scale(I.add(I.mul(I.root(I.point(8)),u),eta),F(4))
  E2=I.add(E2,I.scale(I.point(e2),mult));F2=I.add(F2,I.scale(I.square(v),mult));b2=I.add(b2,I.scale(I.nonnegative(real(trials[kind]['trial_norm'])),mult))
  emit('new_q_channel_bounds',{'kind':kind,'first':u,'inner':eta,'full_F':v})
 E=I.root(E2)[1];FF=I.root(F2)[1];aa=I.root(I.nonnegative(a_squared))[1];bb=I.root(b2)[1]
 X=I.scale(I.root(I.point(15)),F(4))[1];V=I.scale(I.root(I.point(30)),F(32))[1]
 chi=min(X,A.plus(aa,E));psi=min(V,A.plus(bb,FF))
 mixed=min(A.plus(A.times(E,bb),A.times(chi,FF)),A.plus(A.times(E,psi),A.times(aa,FF)))
 error=A.times(F(6),A.plus(A.times(E,A.plus(aa,chi)),mixed));nom=real(nominal)
 new=(A.divide(A.plus(nom[0],-error),F(8)),A.divide(A.plus(nom[1],error),F(8)))
 intersection=(max(new[0],old_alpha[0]),min(new[1],old_alpha[1]))
 result={'new_nominal':nom,'E_upper':E,'F_upper':FF,'new_trial_b_squared':b2,'error_upper':error,'new_alpha':new,'intersection':intersection}
 emit('new_q_posterior_raw',result)
 if intersection[0]>intersection[1]:raise ValueError('disjoint physical-target certificates')
 result['status']='POSITIVE_CERTIFICATE'if intersection[0]>0 else'NEGATIVE_CERTIFICATE'if intersection[1]<0 else'INDETERMINATE_SIGN'
 return result
