from fractions import Fraction as F

def census(raw,n=48):
 if not isinstance(raw,list) or len(raw)!=n or any(not isinstance(r,list) or len(r)!=n for r in raw):raise ValueError('square shape')
 t=[]
 for i,row in enumerate(raw):
  r=[]
  for j,x in enumerate(row):
   if not isinstance(x,str) or len(x)>20000:raise ValueError('rational string')
   q=F(x)
   if max(abs(q.numerator).bit_length(),q.denominator.bit_length())>32768:raise ValueError('coefficient bits')
   if i>j and q!=0:raise ValueError('upper triangular')
   if i==j and q<=0:raise ValueError('positive diagonal')
   r.append(q)
  t.append(r)
 rows=[sum(map(abs,r)) for r in t];cols=[sum(abs(t[i][j]) for i in range(n)) for j in range(n)]
 f2=sum(x*x for r in t for x in r);bound=min(f2,max(rows)*max(cols))
 return {'frobenius_squared':f2,'row_l1':rows,'column_l1':cols,'operator_norm_squared_upper':bound,'dimension':n}

def budgets(c):
 # Entrywise Gram error transforms by at most n||T||².
 gain=c['dimension']*c['operator_norm_squared_upper']
 return {'metric_gain':gain,'eta_metric_for_unit_trace_tau':F(1,10**9)/gain,'eta_metric_for_unit_trace_r2':F(1,10**16)/gain,'scope':'unit-trace PSD consumer only; actual consumer multiplier remains required'}
