import itertools,json
from fractions import Fraction
D=[tuple(s if j==i else 0 for j in range(3)) for i in range(3) for s in [-1,1]]
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def difference(x,S):return tuple(int(add(x,e) in S)-int(add(x,tuple(-a for a in e)) in S) for e in [(1,0,0),(0,1,0),(0,0,1)])
def frontier(S):return {x for a in S for e in D for x in [add(a,e)] if x not in S and any(difference(x,S))}
host=[(0,0,0),(2,0,0),(-1,2,0),(0,1,-2),(3,-1,1),(1,1,0),(0,-1,0)]
for mask in range(128):
 S={x for i,x in enumerate(host) if mask>>i&1};F=frontier(S);assert not(S&F) and len(F)<=6*len(S)
 if S:
  y=max(S);x=add(y,(1,0,0));assert x in F and difference(x,S)[0]==-1
seed={(0,0,0)};F=frontier(seed);extra=frontier(seed|{min(F)})-F;assert len(F)==6 and len(extra)==5
patch=set(itertools.product(range(3),range(2),range(2)));S=set(seed);waves=[]
for _ in range(5):
 f=frontier(S)&patch;waves.append(len(f));S|=f
assert waves==[3,4,3,1,0] and S==patch;outside=len(frontier(S));assert outside==32
S=set(seed);shells=[]
for t in range(1,7):
 F=frontier(S);shells.append(len(F));S|=F;B={x for x in itertools.product(range(-t,t+1),repeat=3) if sum(map(abs,x))<=t};assert S==B and len(F)==4*t*t+2
mass=sum((Fraction(2,3)**n)*(Fraction(1,3)**(6-n)) for signs in itertools.product([-1,1],repeat=6) for n in [signs.count(1)]);assert mass==1
print(json.dumps({'host_domains_checked':128,'extreme_witnesses':127,'first_frontier':6,'new_dynamic_sites':sorted(extra),'patch_waves':waves,'patch_outside_frontier':outside,'seed_shells':shells,'first_step_64_atom_mass':str(mass),'original_producers_run':False},indent=2))
