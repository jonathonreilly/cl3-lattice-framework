from fractions import Fraction as F
import stages as s
count=0
values=list(range(-4,5))+[-s.S-1,-s.S,-s.S+1,-s.S//2,s.S//2,s.S-1,s.S,s.S+1,3*s.S+17]
values=sorted(set(values));intervals=[(a,b)for a in values for b in values if a<=b]
for a in intervals:
 for b in intervals:
  corners=[F(x*y,s.S)for x in a for y in b]
  low=min(corners);high=max(corners)
  expected=(low.numerator//low.denominator,-((-high.numerator)//high.denominator))
  got=s.Arithmetic().mul(a,b)
  assert got==expected,(a,b,got,expected)
  count+=1
print('{"status":"PASS","signed_interval_cases":%d,"scope":"exhaustive finite endpoint set plus256-grid boundaries; no matrices or native inputs"}'%count)
