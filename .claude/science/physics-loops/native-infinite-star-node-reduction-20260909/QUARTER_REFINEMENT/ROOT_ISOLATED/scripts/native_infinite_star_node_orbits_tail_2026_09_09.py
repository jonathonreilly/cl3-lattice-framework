"""Exact ordered cube orbits and complete Laplace tail; no physical geometry."""
from itertools import combinations,permutations,product
from fractions import Fraction as F
import json,signal
if __name__=='__main__':signal.alarm(30)
count=0
def req(ok,msg):
 global count
 if not ok:raise ValueError(msg)
 count+=1
pairs=set((a,c) for a in combinations(range(6),2) for c in combinations(range(6),2) if not set(a)&set(c))
maps=[]
for perm in permutations(range(3)):
 for flips in product(range(2),repeat=3):
  maps.append(tuple(2*perm[j//2]+((j%2)^flips[j//2]) for j in range(6)))
reps=[((0,1),(2,3)),((0,1),(2,4)),((0,2),(4,5)),((0,2),(1,3)),((0,2),(1,4))]
seen=set();sizes=[]
for pair,expected in zip(reps,[6,12,12,12,48]):
 orbit={(tuple(sorted(m[x] for x in pair[0])),tuple(sorted(m[x] for x in pair[1]))) for m in maps}
 req(len(orbit)==expected,'orbit size');req(not seen&orbit,'orbit disjoint')
 for element in orbit:req(element in pairs,'actual disjoint pair')
 seen|=orbit;sizes.append(len(orbit))
req(seen==pairs and len(pairs)==90,'complete ordered coverage')
# Exact Taylor lower bound exp(delta*T), fixed h=1, delta=1/4, beta upper=3.
delta=F(1,4);T=F(100);beta=F(3);x=delta*T;term=F(1);lower=term
for n in range(1,161):term=term*x/n;lower+=term
tail=F(90,8)*(2/delta**2+beta*T/delta**2+2*beta/delta**3)/lower
req(tail<F(1,10**6),'complete improved tail')
print(json.dumps({'status':'PASS','checks':count,'orbit_sizes':sizes,'tail_upper_exact':str(tail),'tail_less_than':'1/1000000','physical_runs':0},indent=2))
