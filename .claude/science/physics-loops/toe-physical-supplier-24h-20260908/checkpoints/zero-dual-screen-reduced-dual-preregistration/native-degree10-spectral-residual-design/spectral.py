"""New signed residual-moment bounds; input acquisition intentionally absent."""
from fractions import Fraction as F
import interval as I
import proposal
TAUS=tuple(map(F,[1,2,4,8,16]));DELTA=F(1,4)
def first_moments(m,p0,p1,emit):
 if len(m)!=7:raise ValueError('seven vacuum moments')
 c=[F(1),I.check(-p0),I.check(-p1)];out=[]
 for j in range(3):
  r=I.point(0)
  for i in range(3):
   for k in range(3):r=I.add(r,I.scale(m[i+k+j],I.check(c[i]*c[k])))
  emit('first_residual_moment',{'j':j,'interval':r});out.append(I.nonnegative(r))
 return out

def inner_moments(s,q,emit):
 if len(s)!=5:raise ValueError('five source moments')
 out=[]
 for j in range(3):
  r=I.add(I.add(s[j],I.scale(s[j+1],I.check(-2*q))),I.scale(s[j+2],I.check(q*q)))
  emit('inner_residual_moment',{'j':j,'interval':r});out.append(I.nonnegative(r))
 return out

def inverse_squared(rho,emit):
 if len(rho)!=3:raise ValueError('three residual moments')
 choices=[I.check(rho[0][1]/DELTA**2)];emit('gap_bound',{'upper':choices[0]})
 try:
  candidate=proposal.propose([I.mid(x)for x in rho]);proposal_status='PROPOSED'
 except (ValueError,ZeroDivisionError)as error:
  candidate=F(1);proposal_status='FALLBACK_FIXED_ONE';emit('proposal_refusal',{'error':repr(error),'fallback':candidate})
 emit('tau_proposal',{'tau':candidate,'status':proposal_status})
 candidates=list(TAUS)
 if candidate not in candidates:candidates.append(candidate)
 for tau in candidates:
  a=(tau+2*DELTA)/(DELTA**2*tau**3);b=-2/tau**3-2*tau*a;c=3/tau**2+tau*tau*a
  # Interval scaling automatically selects LOWER rho1 for negative b.
  box=I.add(I.add(I.scale(rho[2],a),I.scale(rho[1],b)),I.scale(rho[0],c))
  emit('majorant',{'tau':tau,'A':a,'B':b,'C':c,'interval':box})
  if box[1]<0:raise ValueError('negative majorant upper contradiction')
  choices.append(box[1])
 if min(choices)<0:raise ValueError('negative gap upper contradiction')
 return I.check(min(choices))

def combined(rows,emit):
 e2=I.point(0);f2=I.point(0);joverdelta=I.scale(I.root(I.point(2)),8)
 for kind,mult in [('P',12),('O',3)]:
  u2,v2=rows[kind];u=I.root((F(0),u2));v=I.root((F(0),v2));f=I.add(I.mul(joverdelta,u),v)
  e2=I.add(e2,I.scale(I.point(u2),mult));f2=I.add(f2,I.scale(I.square(f),mult))
 result={'E':I.root(e2),'F':I.root(f2)};emit('new_residual_norms',result);return result
