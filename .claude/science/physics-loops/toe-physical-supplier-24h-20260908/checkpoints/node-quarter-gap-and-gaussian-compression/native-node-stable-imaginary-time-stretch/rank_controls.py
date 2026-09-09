"""Exact arithmetic for a proved rank bound only; no physical quadrature."""
from fractions import Fraction as F
import json
rows=[]
for eps in [F(1,1000),F(1,10**6),F(1,10**9)]:
 jl=jh=p=0
 while F(357,25)*F(1,2)**jl>eps/3:jl+=1
 while 2*F(1,2)**jh>eps/3:jh+=1
 while 429*F(4,25)**p>eps/3:p+=1
 bound=F(357,25)*F(1,2)**jl+2*F(1,2)**jh+429*F(4,25)**p
 if bound>eps:raise ValueError('rank error budget')
 rows.append({'epsilon':str(eps),'Jlo':jl,'Jhi':jh,'nodes_per_interval':p,'rank_bound':4*p*(jl+jh),'trace_error_bound':str(bound)})
print(json.dumps({'status':'PASS','physical_quadratures':0,'rows':rows},indent=2))
