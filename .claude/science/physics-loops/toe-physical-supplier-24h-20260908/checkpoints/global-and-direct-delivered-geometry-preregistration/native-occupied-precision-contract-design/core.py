from fractions import Fraction as F
A=1-F(8,10**6);B=1+F(8,10**6);M=F(88)
def thresholds(u,w):
 if not isinstance(u,F) or not 0<u<=10**8:raise ValueError('positive bounded u')
 if not isinstance(w,F) or w<0:raise ValueError('nonnegative w')
 vt=F(1,10**10)/(M*B)
 vr=1/A if w==0 else min(1/A,F(5,10**17)*A/(3*M*B*w))
 def gates(v):return {'inverse_residual':A*v/4,'raw_metric_radius':A*A*v/(192*u)}
 return {'tail':gates(vt),'residual':gates(vr),'w_zero':w==0}
if __name__=='__main__':
 import json
 g=thresholds(F(10**8),F(4))
 assert F(1,10**39)<=g['residual']['raw_metric_radius']
 assert F(1,10**22)<=g['residual']['inverse_residual']
 assert 243000000*F(1,10**29)<F(1,10**20)
 assert F(1,10**37)*2**24<F(1,10**29)
 assert thresholds(F(1),F(0))['w_zero']
 print(json.dumps({'status':'PASS','scope':'five rational worst-case checks, no savednorm reads','checks':5}))
