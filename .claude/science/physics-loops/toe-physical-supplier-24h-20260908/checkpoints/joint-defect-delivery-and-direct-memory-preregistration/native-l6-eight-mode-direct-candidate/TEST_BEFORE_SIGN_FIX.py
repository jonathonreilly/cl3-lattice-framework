import sys,types,math,json
from pathlib import Path
import numpy as np
P=Path(__file__).parent
for name in ('plane','resolvent','active'):
 m=types.ModuleType(name);m.__file__=str(P/(name+'.py'));sys.modules[name]=m;exec(compile((P/(name+'.py')).read_bytes(),m.__file__,'exec'),m.__dict__)
import active
count=0;wrong=0;neg=0;worst=0
for n,lengths in [(4,[4]),(5,[3,2]),(6,[3,3]),(7,[4,3]),(8,[3,3,2])]:
 groups=[];start=0
 for length in lengths:groups.append(list(range(start,start+length)));start+=length
 omega=np.zeros(n);a=np.zeros(n);b=np.array([.19*math.sin(i+.7) for i in range(n)])
 for k,g in enumerate(groups):omega[g]=1+k*.7;a[g[0]]=.3;b[g[0]]=-.4
 # Both signs of a/b interaction tested; choose negative b-center to keep positive vacuum shift.
 d=1<<n;cs=[]
 for j in range(n):
  c=np.zeros((d,d))
  for col in range(d):
   if col&(1<<j):c[col^(1<<j),col]=(-1)**sum((col>>k)&1 for k in range(j))
  cs.append(c)
 A=[c+c.T for c in cs];B=[c-c.T for c in cs];H=sum(omega[j]*(cs[j].T@cs[j]) for j in range(n));H+=sum(a[j]*B[j] for j in range(n))@sum(b[j]*A[j] for j in range(n))
 for sec in (0,1):
  idx=[i|((i.bit_count()%2^sec)<<(n-1)) for i in range(1<<(n-1))];h=H[np.ix_(idx,idx)];rhs=np.array([math.sin(i+.3) for i in idx]);old=rhs.copy();x,r=active.solve(omega,a,b,groups,rhs,sec);truth=np.linalg.solve(h,rhs);err=float(np.max(np.abs(x-truth)));worst=max(worst,err)
  if err>1e-10 or np.max(np.abs(h@x-rhs))>1e-10 or not np.array_equal(rhs.view(np.uint64),old.view(np.uint64)):raise ValueError('solve/source/residual')
  # Actual implementation mutant removes all spectator energies; occupied source must detect it.
  source=(P/'active.py').read_text().replace('for j in spectator:den=np.add(den,np.multiply((bits>>j)&1,omega[j]))','for j in spectator:pass')
  bad=types.ModuleType('bad');exec(compile(source,'omit_Es','exec'),bad.__dict__)
  try:y,_=bad.solve(omega,a,b,groups,rhs,sec)
  except ValueError:wrong+=1
  else:
   if np.max(np.abs(h@y-rhs))<1e-6:raise ValueError('omit Es mutant survived')
   wrong+=1
  count+=1;neg+=any(v<0 for v in r['signed_sigma'])
print(json.dumps({'status':'PASS','dense_cases':count,'omit_spectator_mutants':wrong,'max_error':worst,'negative_signed_cases':neg,'max_modes':8,'native_calls':0},indent=2))
