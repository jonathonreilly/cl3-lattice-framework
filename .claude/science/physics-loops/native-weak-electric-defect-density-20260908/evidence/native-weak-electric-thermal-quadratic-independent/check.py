from fractions import Fraction as F
from pathlib import Path
import json
# Rational cases set the square-root coefficient b=beta*U*sqrt75 directly.
# Test completing-square equivalence, including zero coupling and zero floor.
count=0;wrong=0
for s in (F(1,2),F(1),F(3)):
 for b in (F(0),F(1,3),F(2)):
  for A in (F(0),F(1,7),F(2)):
   for y in (F(0),F(1,5),F(1),F(3)):
    original=s*y*y-b*y<=A
    transformed=(2*s*y-b<=0) or ((2*s*y-b)**2<=b*b+4*s*A)
    if original!=transformed:raise ValueError('quadratic equivalence')
    count+=1
    bad=(2*s*y-b<=0) or ((2*s*y-b)**2<=b*b+2*s*A)
    wrong+=original!=bad
if not wrong:raise ValueError('weak mutant')
Path(__file__).with_name('RESULT.json').write_text(json.dumps({'exact_cases':count,'wrong_discriminant_mismatches':wrong,'physical_run':False},indent=2)+'\n')
