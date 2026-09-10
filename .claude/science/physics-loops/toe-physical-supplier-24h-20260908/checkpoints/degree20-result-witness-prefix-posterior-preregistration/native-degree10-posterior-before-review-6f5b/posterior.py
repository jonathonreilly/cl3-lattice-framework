"""New posterior estimator only; no original moment or Wick implementation."""
from fractions import Fraction as F
from math import isqrt
import re
BITS=32768

def rat(x):
 if type(x)is not str or len(x)>20000 or re.fullmatch(r'-?\d+(?:/\d+)?',x)is None:raise ValueError('canonical rational syntax')
 q=F(x)
 if str(q)!=x:raise ValueError('canonical rational')
 return guard(q)
def guard(q):
 if max(abs(q.numerator).bit_length(),q.denominator.bit_length())>BITS:raise ValueError('posterior rational cap')
 return q
def box(x):
 if type(x)is not list or len(x)!=2:raise ValueError('box shape')
 a,b=map(rat,x)
 if a>b:raise ValueError('box order')
 return a,b
def upper_root(q):
 if q<0:raise ValueError('negative norm upper')
 scale=1<<256;n=isqrt((q.numerator*scale*scale)//q.denominator)
 if F(n*n,scale*scale)<q:n+=1
 return F(n,scale)
def evaluate(s0,q,gate,emit=lambda *args:None):
 norm={k:box(s0[k]) for k in ['P','O']};coeff={k:rat(q[k])for k in ['P','O']}
 if any(v[1]<0 for v in norm.values()):raise ValueError('source norm contradiction')
 a2=guard((12*norm['P'][1]+3*norm['O'][1])/8);b2=guard(12*coeff['P']**2*norm['P'][1]+3*coeff['O']**2*norm['O'][1])
 a=upper_root(a2);b=upper_root(b2);emit('trial_norms',{'a_squared_upper':a2,'b_squared_upper':b2,'a_upper':a,'b_upper':b});EE=box(gate['E']);FF=box(gate['F'])
 if EE[0]<0 or FF[0]<0:raise ValueError('negative residual bound')
 E=EE[1];Fv=FF[1];X=4*upper_root(F(15));V=32*upper_root(F(30));chi=min(X,a+E);psi=min(V,b+Fv)
 first=guard(E*(a+chi));mix1=guard(E*b+chi*Fv);mix2=guard(E*psi+a*Fv);err=guard(6*(first+min(mix1,mix2)));nom=box(gate['nominal']);alpha=(guard((nom[0]-err)/8),guard((nom[1]+err)/8))
 return {'a_squared_upper':a2,'b_squared_upper':b2,'a_upper':a,'b_upper':b,'E_upper':E,'F_upper':Fv,'X_upper':X,'V_upper':V,'chi_upper':chi,'psi_upper':psi,'quadratic_term':first,'mixed_bounds':[mix1,mix2],'error_upper':err,'nominal':nom,'alpha_interval':alpha,'status':'POSITIVE_CERTIFICATE'if alpha[0]>0 else('NEGATIVE_CERTIFICATE'if alpha[1]<0 else'INDETERMINATE_SIGN')}
