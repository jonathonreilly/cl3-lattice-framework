from fractions import Fraction as F
import math,json
import bridge
N=0
def need(c,msg):
 global N
 N+=1
 if not c:raise ValueError(msg)
for d,a,b in [(3,F(1),F(4)),(-3,F(4),F(1))]:
 m=F(2);h=(F(1),a/m);B=((F(0),m),(m,F(-d)))
 for i in (0,1):need(sum(B[i][j]*h[j] for j in (0,1))==a*h[i],'exact eigenvector')
 Q=[[B[i][j]*h[j]/h[i]-(a if i==j else 0) for j in (0,1)] for i in (0,1)]
 need(Q==[[-a,a],[b,-b]],'exact Doob generator')
 need(a*b==m*m and a+b==5,'exact rates')
 need(b*Q[0][1]==a*Q[1][0],'stationary balance')
den=math.hypot(-1e16,2.)-1e16
need(den==0.,'naive denominator cancellation')
try:naive=2./den
except ZeroDivisionError:failed=True
else:failed=False
need(failed,'actual naive formula fails')
a,b,r=bridge.rates(-1e16,1.)
need(a>0 and b>0 and abs(a*b-1)<1e-14,'piecewise formula remains finite')
print(json.dumps(dict(checks=N,naive_formula_failed=failed,piecewise_rates=[a,b],scope='exact rational/cancellation controls only'),indent=2))
