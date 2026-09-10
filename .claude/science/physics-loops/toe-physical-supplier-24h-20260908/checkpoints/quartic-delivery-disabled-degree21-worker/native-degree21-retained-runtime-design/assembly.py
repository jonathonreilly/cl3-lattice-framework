"""Symbolic fixed strategy and bounded contractions. No native loader."""
from fractions import Fraction as F
from math import factorial
import arithmetic as a
import core
PROPOSAL_BITS=64;PROPOSAL_ABS=F(16);RATIONAL_CAP=16384
SIGNATURES=(('P','P',1,48),('P','P',2,12),('P','O',0,12),('O','P',0,12),('O','O',0,6))

def defects(kind):
 V={(0,1):a.imaginary(2),(1,0):a.imaginary(-2)}
 if kind=='inner21':return {1:V,2:{(0,1):a.imaginary(-2),(1,0):a.imaginary(2),(1,2):a.point(-1),(2,1):a.point(-1)}}
 if kind=='nominal21':return {1:{(0,2):a.imaginary(2),(2,0):a.imaginary(-2)},2:{(0,1):a.imaginary(-2),(1,0):a.imaginary(2),(0,3):a.point(-2),(3,0):a.point(-2)},3:V}
 raise a.Refused('literal profile')
def guard(v):
 if type(v)is not F or max(abs(v.numerator).bit_length(),v.denominator.bit_length())>RATIONAL_CAP:raise a.Refused('proposal rational cap')
 return v
def plus(x,y):return guard(x+y)
def times(x,y):return guard(x*y)
def divide(x,y):
 if y==0:raise a.Refused('zero proposal denominator')
 return guard(x/y)
def scaled(x,q):
 guard(q);return a.mul(x,a.point(q.numerator,q.denominator))
def norm(x):
 core.box(x)
 if not x[1][0]<=0<=x[1][1]or x[0][1]<0:raise a.Refused('norm contradiction')
 return ((max(0,x[0][0]),x[0][1]),(0,0))
def new_inner(jet,p,accepted_s,emit=lambda *_:None):
 if len(p)!=3 or len(accepted_s)!=3:raise a.Refused('same quadratic source')
 out=[norm(x)for x in accepted_s]
 for k in(3,4):
  total=a.ZERO
  for i in range(3):
   for j in range(3):
    q=times(times(p[i],p[j]),F(8*(-1)**(i+j+k)*factorial(i)*factorial(j)*factorial(k)))
    total=a.add(total,scaled(jet[i,j,k],q))
  emit('new_inner_raw',{'order':k,'value':total});out.append(norm(total))
 return out

def proposal(s,old_q):
 """Fixed midpoint normal equation; clipped64-grid candidate plus old constant."""
 guard(old_q);mid=[]
 for x in s:
  core.box(x);mid.append(F(x[0][0]+x[0][1],2*a.S))
 determinant=plus(times(mid[2],mid[4]),-times(mid[3],mid[3]))
 if mid[2]<=0 or determinant<=0:return (old_q,F(0)),'FALLBACK_NONPOSITIVE_MIDPOINT'
 q0=divide(plus(times(mid[1],mid[4]),-times(mid[2],mid[3])),determinant)
 q1=divide(plus(times(mid[2],mid[2]),-times(mid[1],mid[3])),determinant)
 def fixed(q):
  q=max(-PROPOSAL_ABS,min(PROPOSAL_ABS,q));return F((q.numerator*(1<<PROPOSAL_BITS))//q.denominator,1<<PROPOSAL_BITS)
 return (fixed(q0),fixed(q1)),'PROPOSED'

def forms(s,q):
 x,y=q;coeff=[F(1),times(F(-2),x),plus(times(x,x),-times(F(2),y)),times(F(2),times(x,y)),times(y,y)]
 eta=a.ZERO
 for v,c in zip(s,coeff):eta=a.add(eta,scaled(v,c))
 bnorm=a.add(a.add(scaled(s[0],times(x,x)),scaled(s[1],times(F(2),times(x,y)))),scaled(s[2],times(y,y)))
 return eta,bnorm

def choose(s,old_q,emit=lambda *_:None):
 candidates=[(old_q,F(0))]
 try:q,status=proposal(s,old_q)
 except a.Refused as error:q=(old_q,F(0));status='FALLBACK_CAP';emit('proposal_refusal',{'error':repr(error)})
 emit('proposal',{'q':q,'status':status,'bits':PROPOSAL_BITS,'clip_abs':PROPOSAL_ABS})
 if q not in candidates:candidates.append(q)
 results=[]
 for i,q in enumerate(candidates):
  eta,bnorm=forms(s,q);emit('trial_forms_raw',{'index':i,'q':q,'eta':eta,'trial_norm':bnorm});results.append((norm(eta),norm(bnorm),q,i))
 best=min(results,key=lambda r:(r[0][0][1],r[3]));emit('selected_trial',{'q':best[2],'eta':best[0],'trial_norm':best[1],'index':best[3]})
 return {'q':best[2],'eta':best[0],'trial_norm':best[1]}

def nominal(jet,pC,pA,qA,emit=lambda *_:None):
 total=a.ZERO
 for i in range(3):
  for j in range(3):
   c=times(times(pC[i],pA[j]),F((-1)**(i+j)*factorial(i)*factorial(j)))
   total=a.add(total,scaled(jet[i,j,0,0],c))
   for k in range(2):total=a.add(total,scaled(jet[i,j,k,1],times(c,times(qA[k],F((-1)**k)))))
 emit('new_nominal_signature_raw',{'complex_value':total})
 # Ordered words may be complex. The Ward nominal uses their real parts.
 return total
