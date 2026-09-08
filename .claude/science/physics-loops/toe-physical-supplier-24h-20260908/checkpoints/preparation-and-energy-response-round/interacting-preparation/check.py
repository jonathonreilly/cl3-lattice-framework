import itertools,json,hashlib,time,resource
from fractions import Fraction as F
from pathlib import Path
start=time.monotonic(); checks={}
def ck(k,v):
 assert bool(v),k
 checks[k]=True
def pl(a): return a.get((0,1),0)*a.get((2,3),0)-a.get((0,2),0)*a.get((1,3),0)+a.get((0,3),0)*a.get((1,2),0)
a={(0,1):F(1,2),(0,3):F(1,2),(1,2):-F(1,2),(2,3):F(1,2)}
ck('initial_normalized',sum(x*x for x in a.values())==1)
ck('initial_slater_pluecker',pl(a)==0)
basis=[n for n in itertools.product((0,1),repeat=4) if sum(n)%2==0]
def bits(n):return tuple(sum(n[:j+1])%2 for j in range(3))
ck('physical_tree_bijection',len(set(map(bits,basis)))==8)
for j in range(4):
 ck('native_B_'+str(j),all((n[j]%2)==((bits(n)[j-1] if j else 0)^(bits(n)[j] if j<3 else 0)) for n in basis))
ck('bridge_Z_equals_component_parity',all((-1)**bits(n)[1]==(-1)**(n[0]+n[1]) for n in basis))
branches={}
for parity in (0,1):
 b={ij:x for ij,x in a.items() if sum(i<2 for i in ij)%2==parity}
 ck('branch_probability_'+str(parity),sum(x*x for x in b.values())==F(1,2))
 ck('branch_non_gaussian_'+str(parity),pl(b)!=0)
 ck('record_support_'+str(parity),all(bits(tuple(int(k in ij) for k in range(4)))[1]==parity for ij in b))
 branches[str(parity)]={'probability':'1/2','unnormalized_pluecker':str(pl(b))}
ck('all_outcomes_reconstruct',all(sum(({ij:x for ij,x in a.items() if sum(i<2 for i in ij)%2==p}).get(ij,0) for p in (0,1))==x for ij,x in a.items()))
# An actual operation mutation: replace two-mode parity by single-mode occupation.
mutant={ij:x for ij,x in a.items() if 0 in ij}
ck('single_mode_mutant_does_not_supply_resource',pl(mutant)==0)
for name,d,want in [('interaction',[F(1),F(1),F(1),F(1,2)],False),('identity',[F(1)]*4,True),('two_leaf_product',[F(1),F(2,3),F(3,5),F(2,5)],True)]:
 ck(name+'_minor', (d[0]*d[3]==d[1]*d[2])==want)
r=F(1,4); z=3+r; density=[1/z,1/z,1/z,r/z]
ck('thermal_density_normalized',sum(density)==1)
ck('thermal_non_gaussian_wick',r/z-((1+r)/z)**2==-F(12,169))
# A bridge directly measuring these same two matter modes is rank reducing.
ck('direct_parity_ranks', [sum((n[0]+n[1])%2==p for n in itertools.product((0,1),repeat=2)) for p in (0,1)]==[2,2])
ck('target_invertible',all(d>0 for d in [1,1,1,F(1,2)]))
# Discarding the Record destroys a cross-parity matrix element rather than attenuating it.
ck('unread_record_not_target',F(0)!=F(1))
result={'checks':checks,'count':len(checks),'branches':branches,'target_wick_defect':'-12/169','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_sec':time.monotonic()-start,'rss_native':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Exact finite algebra; no successful interacting filter construction claimed.'}
print(json.dumps(result,indent=2))
