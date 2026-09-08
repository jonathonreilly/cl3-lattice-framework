"""Deterministic 2-state CT bridge arithmetic; no RNG or trajectory sampler."""
import math
NEG=-math.inf

def rates(d,m=1.):
 if not all(math.isfinite(z) for z in (d,m)) or m<=0:raise ValueError('finite d, positive m')
 r=math.hypot(d,2*m)
 if not math.isfinite(r):raise ValueError('spectral scale overflow')
 if d>=0:b=r/2+d/2;a=m*(m/b)
 else:a=r/2-d/2;b=m*(m/a)
 if not all(math.isfinite(z) and z>0 for z in (a,b,r)):raise ValueError('rate under/overflow')
 return a,b,r

def lse(x,y):
 if x==NEG:return y
 if y==NEG:return x
 z=max(x,y);return z+math.log1p(math.exp(min(x,y)-z))

def log1mexp(z):
 if z<0 or math.isnan(z):raise ValueError('positive exponential argument')
 if z==0:return NEG
 return math.log(-math.expm1(-z)) if z<=math.log(2) else math.log1p(-math.exp(-z))

def logP(d,m,t,i,j):
 if type(i) is not int or type(j) is not int or i not in (0,1) or j not in (0,1):raise ValueError('state index')
 if not math.isfinite(t) or t<0:raise ValueError('duration')
 a,b,r=rates(d,m)
 if t==0:return 0. if i==j else NEG
 z=r*t
 if z==0:raise ValueError('time product underflow')
 pi=(math.log(b)-math.log(r),math.log(a)-math.log(r))
 return lse(pi[i],pi[1-i]-z) if i==j else pi[j]+log1mexp(z)

def logE(d,m,t,i,j):
 p=logP(d,m,t,i,j)
 if p==NEG:return NEG
 a,b,r=rates(d,m);growth=a*t
 if not math.isfinite(growth):raise ValueError('absolute log transfer overflow')
 h=(0.,math.log(a)-math.log(m))
 return growth+h[i]-h[j]+p

def log_survival(d,m,T,s,j,u):
 if not math.isfinite(u) or not 0<=u<=T:raise ValueError('elapsed')
 denominator=logP(d,m,T,s,j)
 if denominator==NEG:raise ValueError('zero endpoint normalization')
 remaining=logP(d,m,T-u,s,j)
 if remaining==NEG:return NEG
 a,b,r=rates(d,m);q=(a,b)[s];holding=q*u
 if not math.isfinite(holding):raise ValueError('holding exponent overflow')
 return -holding+remaining-denominator

def inverse_first(d,m,T,s,j,level,tol=1e-12):
 if not math.isfinite(level) or not 0<=level<1 or not math.isfinite(tol) or tol<=0:raise ValueError('level/tolerance')
 denominator=logP(d,m,T,s,j)
 if denominator==NEG:raise ValueError('incompatible endpoint')
 target=math.log1p(-level)
 atom=log_survival(d,m,T,s,j,T)
 if s==j and target<=atom:return dict(no_event=True,bracket=None,log_atom=atom)
 if level==0:return dict(no_event=False,bracket=[0.,0.],log_atom=atom)
 lo=0.;hi=T
 for _ in range(256):
  mid=lo+(hi-lo)/2
  if mid==lo or mid==hi or hi-lo<=tol*T:break
  if log_survival(d,m,T,s,j,mid)>target:lo=mid
  else:hi=mid
 else:raise ValueError('inverse iteration budget')
 return dict(no_event=False,bracket=[lo,hi],log_atom=atom)

def singleton_bridge(compatible):
 if compatible is not True:raise ValueError('singleton compatibility zero')
 return dict(no_event=True)
