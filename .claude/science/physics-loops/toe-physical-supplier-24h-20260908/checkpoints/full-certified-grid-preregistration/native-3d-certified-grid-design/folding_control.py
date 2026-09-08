from itertools import product
from collections import Counter
import json
counts=Counter(tuple(min(j,31-j) for j in x) for x in product(range(32),repeat=3))
if len(counts)!=4096 or set(counts.values())!={8} or sum(counts.values())!=32768:raise ValueError('full grid multiplicity')
# Exact rational argument identity: theta_j/pi + theta_(31-j)/pi=1.
if any((2*j+1)+(2*(31-j)+1)!=64 for j in range(32)):raise ValueError('exact reflected sine argument')
print(json.dumps(dict(unique_per_class=len(counts),multiplicity=8,original_per_class=sum(counts.values()),classes=6,unique_total=24576,original_total=196608,proof='sin(pi-theta)=sin(theta); no interval-overlap inference')))
