from fractions import Fraction as F
import json
A=F(5439,160);B=F(867,32)
def low(j):return F(2,9)*A*F(1,2**(j+j//2))+F(1,6)*B*F(1,2**(2*j))
def high(n):return F(1,8)*F(9,64)**n*(1+F(18,64*(2*n+3)))
def quad(p):return 429*F(4,25)**p
rows=[]
for exponent in [6,8,10,12]:
 target=F(1,10**exponent);budget=target/4
 j=next(j for j in range(7,80)if low(j)<=budget);n=next(n for n in range(1,40)if high(n)<=budget);p=next(p for p in range(1,40)if quad(p)<=budget);nodes=p*(j+4);raw=6*nodes+3+3*(2*n-1)
 total=low(j)+high(n)+quad(p)+budget
 assert total<=target
 rows.append(dict(target=str(target),Jlo=j,Jhi=4,Gauss_degree=p,high_terms=n,nodes=nodes,low_bound=str(low(j)),high_bound=str(high(n)),quadrature_bound=str(quad(p)),numerical_allocation=str(budget),total_bound=str(total),raw_common_per_orbit_upper=raw,closed_upper=2*raw,raw_triangle=raw*(raw+1)//2))
print(json.dumps({'status':'PASS_ANALYTIC_PARAMETERS_ONLY','rows':rows,'native_calls':0},indent=2))
