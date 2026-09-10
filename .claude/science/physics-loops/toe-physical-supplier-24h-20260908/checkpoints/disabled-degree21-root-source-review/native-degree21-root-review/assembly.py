"""Independent new-q assembly from supplied certified boxes; no data loader."""
from fractions import Fraction as F
from math import factorial,isqrt
import independent as I
from tables import SIGS
CAP=16384
def guard(q):
 if type(q)is not F or max(abs(q.numerator).bit_length(),q.denominator.bit_length())>CAP:raise ValueError('proposal rational cap')
 return q
def positive(z):
 I.checked(z)
 if not z[1][0]<=0<=z[1][1]or z[0][1]<0:raise ValueError('norm contradiction')
 return((max(0,z[0][0]),z[0][1]),(0,0))
def scale(z,q):return I.mul(z,I.c(guard(q)))
def inner(jet,p,old,emit):
 s=[positive(z)for z in old]
 if len(s)!=3 or len(p)!=3:raise ValueError('same quadratic source')
 for k in[3,4]:
  z=I.ZERO
  for i in range(3):
   for j in range(3):z=I.add(z,scale(jet[i,j,k],guard(guard(p[i]*p[j])*F(8*(-1)**(i+j+k)*factorial(i)*factorial(j)*factorial(k)))))
  emit('new_inner_raw',{'order':k,'value':z});s.append(positive(z))
 return s
def proposal(s,old):
 mid=[F(z[0][0]+z[0][1],2*I.GRID)for z in s];det=guard(guard(mid[2]*mid[4])-guard(mid[3]*mid[3]))
 if mid[2]<=0 or det<=0:return(old,F(0)),'FALLBACK_NONPOSITIVE_MIDPOINT'
 q0=guard(guard(guard(mid[1]*mid[4])-guard(mid[2]*mid[3]))/det);q1=guard(guard(guard(mid[2]*mid[2])-guard(mid[1]*mid[3]))/det)
 def dyadic(q):
  q=min(F(16),max(F(-16),q));return F((q.numerator*(1<<64))//q.denominator,1<<64)
 return(dyadic(q0),dyadic(q1)),'PROPOSED'
def forms(s,q):
 x,y=q;c=[F(1),guard(-2*x),guard(guard(x*x)-guard(2*y)),guard(2*guard(x*y)),guard(y*y)];eta=I.ZERO
 for z,v in zip(s,c):eta=I.add(eta,scale(z,v))
 norm=I.add(I.add(scale(s[0],guard(x*x)),scale(s[1],guard(2*guard(x*y)))),scale(s[2],guard(y*y)))
 return eta,norm
def choose(s,old,emit):
 candidates=[(old,F(0))]
 try:q,status=proposal(s,old)
 except ValueError:q,status=(old,F(0)),'FALLBACK_CAP';emit('proposal_refusal',{'error':"Refused('proposal rational cap')"})
 emit('proposal',{'q':q,'status':status,'bits':64,'clip_abs':F(16)})
 if q not in candidates:candidates.append(q)
 all=[]
 for i,q in enumerate(candidates):
  eta,b=forms(s,q);emit('trial_forms_raw',{'index':i,'q':q,'eta':eta,'trial_norm':b});all.append((positive(eta),positive(b),q,i))
 best=min(all,key=lambda z:(z[0][0][1],z[3]));emit('selected_trial',{'q':best[2],'eta':best[0],'trial_norm':best[1],'index':best[3]});return{'q':best[2],'eta':best[0],'trial_norm':best[1]}
def nominal(jet,left,right,q,emit):
 z=I.ZERO
 for i in range(3):
  for j in range(3):
   c=guard(guard(left[i]*right[j])*F((-1)**(i+j)*factorial(i)*factorial(j)));z=I.add(z,scale(jet[i,j,0,0],c))
   for k in range(2):z=I.add(z,scale(jet[i,j,k,1],guard(c*guard(q[k]*F((-1)**k)))))
 emit('new_nominal_signature_raw',{'complex_value':z});return z

def rb(z):return F(z[0][0],I.GRID),F(z[0][1],I.GRID)
def root(z):
 lo,hi=z
 if hi<0:raise ValueError('negative root')
 lo=max(F(0),lo);S=1<<128
 def fl(v):return isqrt(v.numerator*S*S//v.denominator)
 a,b=fl(lo),fl(hi)
 if b*b*hi.denominator<hi.numerator*S*S:b+=1
 return F(a,S),F(b,S)
def finish(p,trials,jets,first,a2,old,emit):
 total=I.ZERO
 for left,right,o,m in SIGS:total=I.add(total,scale(nominal(jets[left,right,o],p[left],p[right],trials[right]['q'],emit),F(m)))
 emit('ordered_sum_raw',{'complex_value':total,'words':90});E2=F(0);F2=F(0);b2=[F(0),F(0)];jn=root((F(8),F(8)))
 for kind,m in [('P',12),('O',3)]:
  e=root((F(0),first[kind]));eta=root(rb(trials[kind]['eta']));v=(4*(jn[0]*e[0]+eta[0]),4*(jn[1]*e[1]+eta[1]));E2+=m*first[kind];F2+=m*v[1]**2;bb=rb(trials[kind]['trial_norm']);b2=[b2[i]+m*bb[i]for i in[0,1]];emit('new_q_channel_bounds',{'kind':kind,'first':e,'inner':eta,'full_F':v})
 E=root((E2,E2))[1];FF=root((F2,F2))[1];a=root(a2)[1];b=root(b2)[1];chi=min(4*root((F(15),F(15)))[1],a+E);psi=min(32*root((F(30),F(30)))[1],b+FF);error=guard(6*(E*(a+chi)+min(E*b+chi*FF,E*psi+a*FF)));nom=rb(total);new=(guard((nom[0]-error)/8),guard((nom[1]+error)/8));inter=(max(new[0],old[0]),min(new[1],old[1]));r={'new_nominal':nom,'E_upper':E,'F_upper':FF,'new_trial_b_squared':tuple(b2),'error_upper':error,'new_alpha':new,'intersection':inter};emit('new_q_posterior_raw',r)
 if inter[0]>inter[1]:raise ValueError('empty intersection')
 return dict(r,status='POSITIVE_CERTIFICATE'if inter[0]>0 else'NEGATIVE_CERTIFICATE'if inter[1]<0 else'INDETERMINATE_SIGN')
