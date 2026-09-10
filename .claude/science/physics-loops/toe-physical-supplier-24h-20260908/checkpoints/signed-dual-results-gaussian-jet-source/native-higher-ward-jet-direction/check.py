import json
from itertools import combinations
n=0
assert 2*4+2==10;n+=1
assert 2*3+2+2==10;n+=1
assert 2*4+2+2==12;n+=1
labels=list(combinations(range(6),2));pairs=[(a,b)for a in labels for b in labels if not set(a)&set(b)]
assert len(pairs)==90;n+=1
assert len(pairs)*4*4*2==2880;n+=1
assert sum(1 for i in range(4)for j in range(i,4))*2*2==40;n+=1
print(json.dumps({'status':'PASS','exact_degree_count_checks':n,'native_values_loaded':0}))
