from fractions import Fraction as F
import json
# Three-mode compressed parity map and ordinary JW gamma squares.
c=0
for p in (0,1):
 for compressed in range(4):
  b=compressed|(((compressed.bit_count()%2)^p)<<2)
  for j in range(3):
   a=b^(1<<j);target=compressed^(1<<j) if j<2 else compressed
   rebuilt=target|(((target.bit_count()%2)^(1-p))<<2)
   if a!=rebuilt:raise ValueError('parity compression')
   sg=(-1)**((b&((1<<j)-1)).bit_count());sg2=(-1)**((a&((1<<j)-1)).bit_count())
   if sg*sg2!=1:raise ValueError('gamma square')
   c+=1
print(json.dumps({'toy_cases':c,'physical_actions':0}))
