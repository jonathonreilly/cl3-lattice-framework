import sys,importlib.util,math,json
from pathlib import Path
import numpy as np
P=Path(__file__).parent
for name in ('plane','resolvent'):
 s=importlib.util.spec_from_file_location(name,P/(name+'.py'));m=importlib.util.module_from_spec(s);sys.modules[name]=m;exec(compile((P/(name+'.py')).read_bytes(),str(P/(name+'.py')),'exec'),m.__dict__)
import resolvent
count=0;negative=0;worst=0.;failures=[]
for n in range(2,7):
 d=1<<n;cs=[]
 for j in range(n):
  c=np.zeros((d,d))
  for col in range(d):
   if col&(1<<j):c[col^(1<<j),col]=(-1)**sum((col>>k)&1 for k in range(j))
  cs.append(c)
 A=[c+c.T for c in cs];B=[c-c.T for c in cs]
 matrices=[np.diag(np.arange(1,n+1,dtype=float)),np.array([[math.sin(1.3+i*2.1+j*.7)+(.8 if i==j else 0) for j in range(n)] for i in range(n)])]
 matrices.append(matrices[-1].copy());matrices[-1][:,0]*=-1
 for M in matrices:
  constant=1+float(np.sum(np.abs(M)))/2
  H=constant*np.eye(d)
  for i in range(n):
   for j in range(n):H-=.5*M[i,j]*(B[i]@A[j])
  for sec in (0,1):
   idx=[i|((i.bit_count()%2^sec)<<(n-1)) for i in range(1<<(n-1))];h=H[np.ix_(idx,idx)];rhs=np.array([math.cos(i+.27) for i in range(len(idx))]);old=rhs.copy();x,r=resolvent.solve(M,constant,rhs,sec);true=np.linalg.solve(h,rhs);res=h@x-rhs;err=float(np.max(np.abs(x-true)));worst=max(worst,err)
   if not np.array_equal(rhs.view(np.uint64),old.view(np.uint64)) or err>1e-11 or np.max(np.abs(res))>1e-11:raise ValueError('dense solve/residual/source')
   if any(z<0 for z in r['signed_sigma']):negative+=1
   count+=1
for c in (0.,1.):
 try:resolvent.solve(np.eye(2),c,np.ones(2),0)
 except ValueError as e:failures.append(str(e))
 else:raise ValueError('zero/negative denominator accepted')
if negative==0:raise ValueError('no signed case')
print(json.dumps({'status':'PASS','dense_solve_cases':count,'signed_negative_cases':negative,'max_error':worst,'denominator_failures':failures,'max_modes':6,'native_calls':0},indent=2))
