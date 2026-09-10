"""Closed degree10 joint forms, h=1; new saved-data estimator only."""
from fractions import Fraction as F
from itertools import combinations
import interval as I
P=I.point
LABELS=list(combinations(range(6),2))
def kind(a):return 'O'if a[0]//2==a[1]//2 else'P'
def plus(*xs):
 z=P(0)
 for x in xs:z=I.add(z,x)
 return z

def kernels(C,A,c,n):
 u,w,q=C;v,z,t=A;VC=I.scale(w,4);VA=I.scale(z,4)
 xx=plus(I.mul(u,v),I.mul(c,plus(I.mul(u,z),I.mul(w,v))),I.scale(I.mul(w,z),n))
 vv=I.mul(I.mul(q,t),plus(I.scale(I.mul(u,v),4*n),I.mul(VC,VA),I.scale(I.mul(c,plus(I.mul(u,VA),I.mul(VC,v))),2)))
 xgv=I.neg(I.mul(t,plus(I.scale(I.mul(v,plus(I.mul(c,u),I.scale(w,n))),2),I.mul(VA,plus(u,I.mul(c,w))))))
 return xx,vv,xgv

def lower(E,Fv):
 if min(E,Fv)<0:raise ValueError('negative errors')
 if Fv<=2*E:return I.check(-3*E*E-3*E*Fv)
 if Fv<=4*E:return I.check(-6*E*E-F(3,4)*Fv*Fv)
 return I.check(6*E*E-6*E*Fv)

def evaluate(inputs,emit):
 c=I.box(inputs['c']);nom=I.box(inputs['nominal']);old=I.box(inputs['spectral_alpha_interval']);E=I.parse(inputs['E_upper']);Fv=I.parse(inputs['F_upper']);L=lower(E,Fv)
 necessary=I.check(nom[1]+L);emit('necessary_screen',{'E':E,'F':Fv,'L':L,'nominal':nom,'upper_W0_plus_L':necessary})
 if necessary<=0:return {'status':'ZERO_DUAL_POSITIVE_CERTIFICATE_EXCLUDED','alpha_interval':old,'screen_upper':necessary,'L':L,'ordered_pairs':0,'kernel_values':0,'true_alpha_excluded':False,'other_duals_excluded':False}
 rows={}
 for k in ['P','O']:
  xs=[I.parse(inputs['coefficients'][k][f])for f in ['p0','p1','q']]
  rows[k]=tuple(P(x)for x in xs)
 G=[P(0),P(0),P(0)];count=0
 for C in LABELS:
  for A in LABELS:
   emit('before_pair',{'index':count,'C':C,'A':A});n=len(set(C)&set(A));weight=6 if C==A else 1 if n==0 else 3
   vals=kernels(rows[kind(C)],rows[kind(A)],c,n)
   for j in range(3):G[j]=I.add(G[j],I.scale(vals[j],weight))
   count+=1;emit('joint_pair',{'index':count,'C':C,'A':A,'overlap':n,'weight':weight,'values':vals,'cumulative':G})
 if count!=225:raise ValueError('fixed pair count')
 emit('joint_grams',{'G':G,'pairs':count})
 w2=I.nonnegative(I.sub(plus(I.scale(G[0],4),G[1]),I.scale(G[2],4)));u2=I.nonnegative(G[0]);w=I.root(w2)[1];u=I.root(u2)[1]
 lin=I.check(I.check(E*w)+I.check(Fv*u));lo=I.check((nom[0]-lin+L)/8);hi=I.check((nom[1]+lin+6*E*E+6*E*Fv)/8)
 final=(max(lo,old[0]),min(hi,old[1]))
 if final[0]>final[1]:raise ValueError('contradictory intervals')
 return {'status':'POSITIVE_CERTIFICATE'if final[0]>0 else'NEGATIVE_CERTIFICATE'if final[1]<0 else'INDETERMINATE_SIGN','alpha_interval':final,'spectral_alpha_interval':old,'G':G,'gradient_squared':w2,'adjoint_squared':u2,'L':L,'linear_error':lin,'ordered_pairs':count,'kernel_values':3*count,'screen_upper':necessary,'true_alpha_excluded':False,'other_duals_excluded':False}
