"""Exact finite support and summability controls, not a proof by enumeration."""
from fractions import Fraction as F

def check():
 count=0
 def req(ok,msg):
  nonlocal count
  if not ok:raise ValueError(msg)
  count+=1
 def step(state,L=None):
  out={}
  for r,value in state.items():
   for axis in range(3):
    eta=(-1)**sum(r[:axis])
    for sign in (-1,1):
     s=list(r);s[axis]+=sign;phase=sign*eta
     if L:
      if s[axis]>=L//2:s[axis]-=L;phase=-phase
      if s[axis]<-L//2:s[axis]+=L;phase=-phase
     s=tuple(s);out[s]=out.get(s,0)+phase*value
  return {r:v for r,v in out.items() if v}
 for L in (8,12,16):
  a={(0,0,0):1};b=a.copy()
  for order in range(1,L//2):
   a=step(a);b=step(b,L);req(a==b,'finite-hop boundary independence')
 # Exact CAR monomial action verifies local quadratic commutator.
 def gamma(j,x):return x^(1<<(j//2)),(-1)**((x&((1<<(j//2))-1)).bit_count())*(1 if j%2==0 else 1j*(1-2*((x>>(j//2))&1)))
 def word(indices,x):
  c=1
  for j in reversed(indices):x,a=gamma(j,x);c*=a
  return x,c
 for a,b in ((0,1),(0,3),(2,5)):
  for j in range(6):
   for x in range(8):
    u,c=word((a,b,j),x);v,d=word((j,a,b),x);actual={}
    actual[u]=actual.get(u,0)+c;actual[v]=actual.get(v,0)-d;actual={k:z for k,z in actual.items() if z}
    expected={}
    if j==b:
     k,z=gamma(a,x);expected[k]=2*z
    elif j==a:
     k,z=gamma(b,x);expected[k]=-2*z
    req(actual==expected,'CAR quadratic commutator')
 for q in range(9):
  p=q+4;r=F(2)**(q+3-p)
  for start in range(12):
   finite=sum(r**n for n in range(start,start+20));tail=r**start/(1-r)
   req(finite<tail and tail-finite==r**(start+20)/(1-r),'weighted dyadic tail')
 return {'status':'PASS','checks':count,'physical_runs':0,'scope':'finite-hop locality, exact CAR and weighted coefficient tails'}
if __name__=='__main__':
 import signal,json
 signal.alarm(180);print(json.dumps(check(),indent=2))
