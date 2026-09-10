"""Inert quartic estimator. No moments, saved trials, or native loader."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from functools import lru_cache
import interval as I
DELTA=F(1,4)
TAUS=tuple(map(F,('1','2','4','8','16')))
PAIRS=tuple(combinations_with_replacement(TAUS,2))
def rat(x):
 if type(x)is not F:raise ValueError('exact Fraction required')
 return I.check(x)
def checked_box(x):
 if type(x)is not tuple or len(x)!=2:raise ValueError("internal interval shape")
 for v in x:rat(v)
 if x[0]>x[1]:raise ValueError("interval order")
 return x
def ra(x,y):return I.check(x+y)
def rm(x,y):return I.check(x*y)
def rd(x,y):
 if y==0:raise ValueError('zero rational denominator')
 return I.check(x/y)
def pmul(P,Q):
 R=[F(0)]*(len(P)+len(Q)-1)
 for i,x in enumerate(P):
  for j,y in enumerate(Q):R[i+j]=ra(R[i+j],rm(x,y))
 return R

@lru_cache(maxsize=30)
def quartic(delta,t,u):
 """Exact quotient coefficients, ascending powers; parent877664 / independent1500245."""
 for x in(delta,t,u):
  rat(x)
  if x<=0:raise ValueError('strictly positive parameter')
 P=[-delta,F(1)]
 for root in(t,t,u,u):P=pmul(P,[-root,F(1)])
 B=rd(F(1),rm(delta,rm(rm(t,t),rm(u,u))))
 A=rm(B,ra(rd(F(1),delta),ra(rd(F(2),t),rd(F(2),u))))
 numerator=pmul(P,[B,A]);numerator[0]=ra(numerator[0],F(1))
 if numerator[:2]!=[0,0]:raise ValueError('majorant quotient divisibility')
 return tuple(numerator[2:])

def residual_moments(m,p,rho0,emit):
 if len(m)!=11 or len(p)!=3:raise ValueError('eleven moments and degree-two trial')
 for x in p:rat(x)
 for x in m:checked_box(x)
 checked_box(rho0)
 # rho0 is inherited from the old accepted r2, not recomputed here.
 rho=[I.nonnegative(rho0)];v=[F(1)]+[-x for x in p];convolution=pmul(v,v)
 emit('residual_convolution',{'coefficients':convolution})
 for j in range(1,5):
  total=I.point(0)
  for i,x in enumerate(convolution):total=I.add(total,I.scale(m[i+j],x))
  emit('new_residual_moment_raw',{'j':j,'interval':total})
  rho.append(I.nonnegative(total))
 return rho

def best_bound(rho,old_upper,emit):
 if len(rho)!=5:raise ValueError('five residual moments')
 rat(old_upper)
 if old_upper<0:raise ValueError('negative inherited first bound')
 upper=min(old_upper,rd(rho[0][1],rm(DELTA,DELTA)))
 emit('inherited_first_bound',{'old_upper':old_upper,'gap_upper':rd(rho[0][1],rm(DELTA,DELTA))})
 for index,(t,u)in enumerate(PAIRS):
  coeff=quartic(DELTA,t,u);value=I.point(0)
  for x,moment in zip(coeff,rho):value=I.add(value,I.scale(moment,x))
  emit('quartic_candidate_raw',{'index':index,'tau1':t,'tau2':u,'coefficients':coeff,'interval':value})
  if value[1]<0:raise ValueError('negative majorant upper contradiction')
  upper=min(upper,value[1])
 return upper

def evaluate(rows,nominal,old_alpha,trial_a2,trial_b2,emit=lambda *_:None):
 """All arguments are inert certified descriptors, not paths. No acquisition."""
 if set(rows)!={'P','O'}:raise ValueError('pair classes')
 E2=I.point(0);F2=I.point(0)
 for x in(nominal,old_alpha,trial_a2,trial_b2):checked_box(x)
 Jnorm=I.root(I.point(8))
 for kind,mult in(('P',12),('O',3)):
  row=rows[kind];rho=residual_moments(row['moments'],row['p'],row['r2'],lambda stage,data:emit(stage,dict(data,kind=kind)))
  e2=best_bound(rho,row['old_first_squared_upper'],lambda stage,data:emit(stage,dict(data,kind=kind)))
  checked_box(row['t2']);e=I.root((F(0),e2));inner=I.root(I.nonnegative(row['t2']))
  f=I.scale(I.add(I.mul(Jnorm,e),inner),rd(F(1),DELTA))
  E2=I.add(E2,I.scale(I.point(e2),mult));F2=I.add(F2,I.scale(I.square(f),mult))
  emit('class_residual_bound',{'kind':kind,'first_squared_upper':e2,'first_root':e,'inherited_inner_squared':row['t2'],'F':f})
 E=I.root(E2)[1];FF=I.root(F2)[1]
 # The old certified trial norms are inputs, never rebuilt from old moments.
 a=I.root(I.nonnegative(trial_a2))[1];b=I.root(I.nonnegative(trial_b2))[1]
 X=I.scale(I.root(I.point(15)),4)[1];V=I.scale(I.root(I.point(30)),32)[1]
 chi=min(X,ra(a,E));psi=min(V,ra(b,FF))
 quadratic=rm(E,ra(a,chi));mix1=ra(rm(E,b),rm(chi,FF));mix2=ra(rm(E,psi),rm(a,FF))
 error=rm(F(6),ra(quadratic,min(mix1,mix2)))
 new=(rd(ra(nominal[0],-error),F(8)),rd(ra(nominal[1],error),F(8)))
 final=(max(new[0],old_alpha[0]),min(new[1],old_alpha[1]))
 payload={'E_upper':E,'F_upper':FF,'trial_a_upper':a,'trial_b_upper':b,'error_upper':error,'new_alpha':new,'old_alpha':old_alpha,'intersection':final}
 emit('posterior_raw',payload)
 if final[0]>final[1]:raise ValueError('disjoint certificates')
 return dict(payload,status='POSITIVE_CERTIFICATE'if final[0]>0 else'NEGATIVE_CERTIFICATE'if final[1]<0 else'INDETERMINATE_SIGN')
