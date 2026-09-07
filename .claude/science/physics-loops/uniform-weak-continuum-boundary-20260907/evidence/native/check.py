from fractions import Fraction as F
from math import factorial
import json,time,resource,sys,signal,hashlib
from pathlib import Path
started=time.monotonic();signal.alarm(180);checks=[]
def ck(name,b):
 if name in checks or not b:raise AssertionError(name)
 checks.append(name)
certs=[]
for P,N,c in [(0,0,F(1,2)),(3,2,F(3,7)),(12,5,F(2,3))]:
 m=P+N+1;C=F(factorial(m))/c**m
 ck('unit_inverse_power_'+str((P,N)),m-P-N==1)
 ck('positive_exact_coefficient_'+str((P,N)),C>0 and C.denominator>0)
 certs.append({'P':P,'N':N,'c':str(c),'m':m,'coefficient':str(C),'bound':'coefficient/n; from the analytic exponential-series inequality, not evaluated exponentials'})
ck('wrong_series_degree_not_decay',(3+2)-3-2==0)
budgets=[]
for n in [2,5,11]:
 value=n**3*F(1,n**3)*n**2;ck('weighted_Riemann_budget_'+str(n),value==n*n);budgets.append({'n':n,'weighted_norm':str(value)})
clock=[]
for i,(ell,a,b,u) in enumerate([(F(1,8),F(2),F(3),F(1,10)),(F(1,16),F(1,32),F(4),F(1,20)),(F(1,7),F(3,5),F(2,3),F(1,9))]):
 v=u/a;V_e=32*ell*v/b;G=2/(a*b)
 ck('clock_ratio_'+str(i),V_e/G==16*ell*u)
 clock.append({'ell':str(ell),'a':str(a),'b':str(b),'u':str(u),'V_over_e':str(V_e),'G_lower':str(G),'ratio_over_e':str(V_e/G)})
ell,a,b,u=F(1,8),F(2),F(3),F(1,10)
ck('wrong_clock_direction_adverse',32*ell*(u/a)*b!=32*ell*(u/a)/b)
e1,e2=F(1,8),F(1,16);u=F(1,10)
ck('fixed_kinetic_scale_halves_LR_upper',32*e2*u==32*e1*u/2)
ck('fixed_LR_upper_diverging_gap_adverse',32*e1*u/e1==32*e2*u/e2 and 2/e2==2*(2/e1))
ck('bounded_actual_gap_extra_premise_needed',2/e1>10 and 2/e2>10)
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
ck('positive_resources',0<rss<180 and time.monotonic()-started<180)
out={'TOTAL':len(checks),'checks':checks,'exponential_series_certificates':certs,'weighted_budgets':budgets,'clock_cases':clock,'seconds':time.monotonic()-started,'rss_MiB':rss,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact scaling and clock-ratio bookkeeping/adverse controls. No finite calculation proves clustering, continuum convergence, actual propagation speed or a numerical coupling threshold.'}
print(json.dumps(out,indent=2,allow_nan=False))
