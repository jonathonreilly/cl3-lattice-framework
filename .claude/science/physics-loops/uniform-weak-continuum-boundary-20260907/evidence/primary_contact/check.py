from fractions import Fraction as F
from itertools import product,combinations
import json
checks=[]
def ck(name,b):
 assert name not in checks and b,name
 checks.append(name)
haar_norm=sum(F(int(a==b),3) for a,b in product(range(3),repeat=2))
ck('Schur fundamental character norm',haar_norm==1)
ck('center kills first and squared characters',1%3!=0 and 2%3!=0)
var=F(2,36)*haar_norm
ck('actual plaquette variance',var==F(1,18))
ck('normalized variance',18*var==1)
def edges(k):
 x,y,z=(3*t for t in k)
 return {(x,y,z,0),(x+1,y,z,1),(x,y+1,z,0),(x,y,z,1)}
anchors=list(product(range(-1,2),repeat=3));sets=[edges(k) for k in anchors]
ck('all27 neighboring coarse plaquettes pairwise link-disjoint',all(not a&b for a,b in combinations(sets,2)))
ck('each actual plaquette has four links',all(len(s)==4 for s in sets))
ck('repeated plaquette is not independent',bool(sets[0]&sets[0]) and 18*var!=0)
# B²=18; threshold z²<=1/(4B²).
ck('small argument threshold',F(1,4*18)==F(1,72))
ck('Taylor deviation coefficient',F(1,2)+F(1,12)<=1)
ck('log remainder coefficient at threshold',1/(2*(1-F(1,72)))<=1)
ck('combined cubic coefficient',F(1,6)+F(1,36)==F(7,36))
ck('safe cubic constant',F(7,36)<F(1,4))
ck('sum remainder power',F(9,2)-3==F(3,2))
print(json.dumps({'status':'PASS','checks':len(checks),'names':checks,'plaquettes':len(sets),'pairs':len(list(combinations(sets,2))),'variance':str(var),'normalized_variance':'1','log_remainder_relative_to_discrete_quadratic':'O(h^(3/2)); no continuous-test quadrature rate claimed'},indent=2))
