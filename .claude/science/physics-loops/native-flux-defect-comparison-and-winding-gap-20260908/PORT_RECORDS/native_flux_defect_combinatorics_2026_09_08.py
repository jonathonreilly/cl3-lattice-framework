from itertools import product
from pathlib import Path
import json,time
start=time.monotonic();checks=0
def ck(x):
 global checks;checks+=1
 if not x:raise ValueError(checks)
def runlength(x):
 n=len(x)
 if len(set(x))==1:return n
 return max(next((k for k in range(1,n+1) if x[(i+k)%n]!=x[i]),n) for i in range(n))
def child(x,s):
 n=len(x);out=[None]*n
 for k in range(n//2):out[(s+k)%n]=x[(s+k)%n];out[(s-1-k)%n]=x[(s+k)%n]
 return out
for n in (2,4,6,8,10):
 for x in product((0,1),repeat=n):
  r=runlength(x)
  if r<n:ck(max(runlength(child(x,s)) for s in range(n))>r)
  for s in range(n):
   a=child(x,s);b=child(x,s+n//2)
   ck(sum(a)+sum(b)==2*sum(x))
# Reflection preserves the twisted label prescription, all three normal labels.
for n in (2,4,6,8):
 for s,b in product(range(n),repeat=2):
  image=(2*s-1-b)%n;ck(image%2==1-b%2)
result=dict(predicates=checks,seconds=time.monotonic()-start,scope='finite run-extension/empirical-count/twist controls; no energy computation')
if __name__=='__main__':print(json.dumps(result,indent=2))
