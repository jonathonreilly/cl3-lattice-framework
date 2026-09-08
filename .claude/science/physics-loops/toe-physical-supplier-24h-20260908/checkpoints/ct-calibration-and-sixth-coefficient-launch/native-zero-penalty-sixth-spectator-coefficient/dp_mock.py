from itertools import combinations,permutations
from fractions import Fraction
import json,time,signal
signal.alarm(180);start=time.monotonic()
# Mock exact noncommuting 2x2 resolvents. This tests ordering and merging,
# independently against explicit sums of all legal occurrence orderings.
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mv(A,x):return (A[0]*x[0]+A[1]*x[1],A[2]*x[0]+A[3]*x[1])
def inv(A):
 d=A[0]*A[3]-A[1]*A[2];return (A[3]/d,-A[1]/d,-A[2]/d,A[0]/d)
# Tiny path with three edges. Electric pairs (0,1),(1,2), bridge1 twice,
# target boundary edges0,2 once. Two orders differ noncommutatively.
terms=[(0,1),(1,2)];target=(1,2,1)
def R(s):
 p=sum((x%2)<<i for i,x in enumerate(s));return inv((Fraction(4+p),Fraction(1),Fraction(1),Fraction(7+2*p)))
def rec(target,terms):
 zero=tuple(0 for _ in target);layers=[{zero:(Fraction(1),Fraction(2))}]
 for k in range(sum(target)//2):
  sums={}
  for s,x in layers[-1].items():
   for e,f in terms:
    q=list(s);q[e]+=1;q[f]+=1;q=tuple(q)
    if any(a>b for a,b in zip(q,target)):continue
    sums[q]=add(sums.get(q,(0,0)),x)
  layers.append({s:(x if s==target else mv(R(s),x)) for s,x in sums.items()})
 return layers[-1][target]
actual=rec(target,terms);expected=(0,0)
for order in permutations(terms):
 s=[0]*3;x=(Fraction(1),Fraction(2))
 for k,(e,f) in enumerate(order):
  s[e]+=1;s[f]+=1
  if k<1:x=mv(R(s),x)
 expected=add(expected,x)
if actual!=expected:raise RuntimeError('DP order')
# Different matrices are mandatory; constant-resolvent mock would hide bug.
if mv(R((1,1,0)),(1,2))==mv(R((0,1,1)),(1,2)):raise RuntimeError('nondiscriminating')
print(json.dumps({'PASS':True,'DP':list(map(str,actual)),'explicit':list(map(str,expected)),'scope':'exact reduced mock, not physical resolvent','seconds':time.monotonic()-start},indent=2))
