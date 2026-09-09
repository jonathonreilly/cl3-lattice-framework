"""Actual candidate versus independently built dense ordered CAR, modes<=6."""
import importlib.util,sys,math,json
from pathlib import Path
import numpy as np
p=Path(__file__).parent;sp=importlib.util.spec_from_file_location('plane',p/'plane.py');m=importlib.util.module_from_spec(sp);exec(compile((p/'plane.py').read_bytes(),str(p/'plane.py'),'exec'),m.__dict__)
checks=0;maxerr=0.;adverse=0
for modes in range(2,7):
 size=1<<modes;cs=[]
 for j in range(modes):
  c=np.zeros((size,size))
  for col in range(size):
   if col&(1<<j):c[col^(1<<j),col]=(-1)**sum((col>>k)&1 for k in range(j))
  cs.append(c)
 A=[c+c.T for c in cs];B=[c-c.T for c in cs]
 for sec in (0,1):
  idx=[i|((i.bit_count()%2^sec)<<(modes-1)) for i in range(1<<(modes-1))]
  x=np.array([math.sin(i+.3)+(-1)**i*.17 for i in range(len(idx))])
  for a in range(modes):
   for b in range(a+1,modes):
    for kind,gens in [('AA',A),('BB',B)]:
     G=(gens[a]@gens[b])[np.ix_(idx,idx)]
     if not np.array_equal(G@G,-np.eye(len(idx))):raise ValueError('generator square')
     for angle in (0.,.37,-1.123,math.pi,2*math.pi):
      expected=math.cos(angle/2)*x+math.sin(angle/2)*(G@x);out=x.copy();returned=m.apply(out,modes,sec,a,b,angle,kind,chunk=3)
      err=float(np.max(np.abs(out-expected)));maxerr=max(maxerr,err)
      if returned is not out or err>3e-15:raise ValueError('dense action')
      if abs(float(out@out-x@x))>5e-13:raise ValueError('norm')
      m.apply(out,modes,sec,a,b,angle,kind,inverse=True,chunk=3)
      if np.max(np.abs(out-x))>3e-15:raise ValueError('inverse')
      if angle==0 and not np.array_equal(out.view(np.uint64),x.view(np.uint64)):raise ValueError('identity bits')
      checks+=1
     # Wrong oriented generator is not accepted by this actual reference.
     bad=math.cos(.37/2)*x-math.sin(.37/2)*(G@x);out=x.copy();m.apply(out,modes,sec,a,b,.37,kind,chunk=3)
     if np.max(np.abs(out-bad))<1e-3:raise ValueError('sign mutant not discriminated')
     adverse+=1
print(json.dumps({'status':'PASS','actual_dense_cases':checks,'wrong_orientation_controls':adverse,'max_error':maxerr,'max_modes':6,'physical_arrays':0},indent=2))
