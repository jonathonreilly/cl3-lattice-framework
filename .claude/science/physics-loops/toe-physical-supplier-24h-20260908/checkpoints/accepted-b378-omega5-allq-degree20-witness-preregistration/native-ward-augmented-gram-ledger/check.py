from fractions import Fraction as F
import append_api as a
import json,time
start=time.monotonic();count=0

def require(x):
 global count
 if not x:raise ValueError('synthetic predicate failed')
 count+=1
# Exact squared checks avoid a floating square-root assertion.
def below(e,target):
 rem=target-1596*e
 return rem>0 and 4*531*1596*e<rem*rem
require(48166272+798*(514+512)==48985020)
require(F(48985020,10**19)<F(5,10**12))
require(below(F(5,10**12),F(412,100000)))
require(below(F(2**40,10**30),F(2,10**6)))
require(below(F(1,2**60),F(2,10**6)))
require(F(412,100000)+F(4,10**6)+F(1,10**9)+F(1,10**6)<F(42,10000))
require(F(529)+F(16,15)<531)
for orbit in ((1,1,0),(1,0,0),(0,1,0),(0,0,2),(0,0,1)):
 for i in range(3):
  for j in range(3):
   g,z=a.appended_pair(i,j,F(1,4),orbit)
   require((g,z)==a.appended_pair(j,i,F(1,4),orbit));require(z==0)
   if i==0 and j>0:require(g==F(1,12))
 for s in (F(1,128),F(1),F(16)):
  for sig in (-1,1):
   for i in range(3):
    for v in range(3):
     base=a.appended_to_pole(i,v,s,sig,F(1,5),F(2,7),F(3,8),orbit)
     twin=a.appended_to_pole(i,v,s,-sig,F(1,5),F(2,7),F(3,8),orbit)
     # Chiral selection: raw y at opposite poles transforms as -chi_v.
     chi=1 if v==0 else -1
     require(twin[0]==-chi*base[0]);require(twin[1]==chi*base[1])
     shifted=a.appended_to_pole(i,v,s,sig,F(1,5),F(2,7),F(3,8)+1,orbit)
     require(abs(shifted[1]-base[1])<=128)
try:a.native_append()
except RuntimeError:require(True)
else:require(False)
print(json.dumps({'scope':'synthetic rational formulas and prospective ledger only','predicates':count,'seconds':time.monotonic()-start,'native_calls':0},indent=2))
