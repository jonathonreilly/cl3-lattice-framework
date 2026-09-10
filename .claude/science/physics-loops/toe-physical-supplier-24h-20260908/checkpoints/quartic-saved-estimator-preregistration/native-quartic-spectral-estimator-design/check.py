"""Exact fabricated atomic spectral measure; no native/saved inputs."""
from fractions import Fraction as F
import json
import core as C
import interval as I
checks=0
# Independent elementary-symmetric coefficient identity, including degeneracy.
for t,u in C.PAIRS:
 coeff=C.quartic(C.DELTA,t,u);d=C.DELTA
 e1=d+2*t+2*u;e2=t*t+u*u+4*t*u+2*d*(t+u);e3=2*t*u*(t+u)+d*(t*t+u*u+4*t*u);e4=t*t*u*u+2*d*t*u*(t+u)
 B=1/(d*t*t*u*u);A=B*(1/d+2/t+2/u)
 assert coeff==(A*e4-B*e3,B*e2-A*e3,A*e2-B*e1,B-A*e1,A);checks+=1
 for x in(d,F(1,3),F(1),F(9)):
  Q=sum(c*x**j for j,c in enumerate(coeff))
  assert Q-1/x**2==(x-d)*(x-t)**2*(x-u)**2*(A*x+B)/x**2>=0;checks+=1
atoms=[(F(1,2),F(1,5)),(F(2),F(3,10)),(F(7),F(1,2))];p=[F(2,3),F(-1,7),F(1,49)]
m=[I.point(sum(w*x**j for x,w in atoms))for j in range(11)]
r=lambda x:1-x*sum(v*x**i for i,v in enumerate(p))
exact=[sum(w*r(x)**2*x**j for x,w in atoms)for j in range(5)]
events=[];rho=C.residual_moments(m,p,I.point(exact[0]),lambda s,v:events.append((s,v)))
assert all(v==(q,q)for v,q in zip(rho,exact));checks+=1
old=exact[0]/C.DELTA**2;upper=C.best_bound(rho,old,lambda s,v:events.append((s,v)))
truth=sum(w*r(x)**2/x**2 for x,w in atoms)
assert truth<=upper<=old;checks+=1
# Signed endpoint enclosure with independently perturbed original rho boxes.
wide=[(q-F(1,100000),q+F(1,100000))for q in exact]
for t,u in C.PAIRS:
 coeff=C.quartic(C.DELTA,t,u);z=I.point(0)
 for c,v in zip(coeff,wide):z=I.add(z,I.scale(v,c))
 exactsum=sum(c*q for c,q in zip(coeff,exact));assert z[0]<=exactsum<=z[1];checks+=1
row={'moments':m,'p':p,'r2':I.point(exact[0]),'t2':I.point(F(1)),'old_first_squared_upper':old}
out=C.evaluate({'P':row,'O':row},I.point(0),(-F(1000000),F(1000000)),I.point(3),I.point(2),lambda s,v:events.append((s,v)))
assert out['status']=='INDETERMINATE_SIGN'and out['new_alpha'][0]<=0<=out['new_alpha'][1];checks+=1
for x in (F(0),F(-1)):
 try:C.quartic(C.DELTA,x,F(1))
 except ValueError:checks+=1
 else:raise AssertionError('nonpositive proposal')
assert len(C.PAIRS)==15;checks+=1
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':checks,'fixed_pairs_per_class':15,'pairs_per_choice':30,'native_values':0,'new_native_moments':0},indent=2))
