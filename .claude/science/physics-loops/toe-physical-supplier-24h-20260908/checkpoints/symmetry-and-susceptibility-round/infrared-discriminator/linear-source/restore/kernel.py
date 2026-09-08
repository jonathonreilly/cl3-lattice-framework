import numpy as np
def branch(nf,F,V,xi,volume):
 shift=abs(xi)*np.sqrt(volume)/2
 return 1+((1-V)*nf+shift-xi*F)/(3*volume)
def step(x,F,face,uniform,faces,coeff,nf,V,xi,volume):
 b=branch(nf,F,V,xi,volume)
 if not np.isfinite(b) or b<1-1e-13:raise ValueError('invalid branching')
 bits=[(x>>int(j))&1 for j in faces[face]]
 if bits[0]==bits[2] and bits[1]==bits[3] and bits[0]!=bits[1] and uniform<1/b:
  for j in faces[face]:
   j=int(j);F+=coeff[j]*(1-2*((x>>j)&1));x^=1<<j
 return x,F,b

def restore(shifted,xi,volume):return shifted-abs(xi)*np.sqrt(volume)/2
