import os,sys,ast,copy,hashlib,json,signal,time
from pathlib import Path
p=Path(__file__).resolve().parent;src=p.parent/'detuned-energy-moment'
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['NUMBA_CACHE_DIR']=str(p/'numba-cache');sys.dont_write_bytecode=True;signal.alarm(60);start=time.monotonic()
def fn(file,name):return next(x for x in ast.parse((src/file).read_text()).body if isinstance(x,ast.FunctionDef) and x.name==name)
a=fn('producer_original.py','prepare_population');b=fn('prepare_derivative.py','prepare_with_samples');b.name=a.name
assert len(b.body[-1].value.elts)==5 and ast.unparse(b.body[-1].value.elts[-1])=='count_samples.copy()'
b.body[-1].value.elts.pop();assert ast.dump(a)==ast.dump(b)
a=fn('producer_original.py','measure_correlation_block');b=fn('measurement_derivative.py','measure_raw_block');b.name=a.name;b.body[-1].value.elts[2]=copy.deepcopy(a.body[-1].value.elts[2]);assert ast.dump(a)==ast.dump(b)
import numpy as np
from numba import njit
sys.path[:0]=[str(src),'/private/tmp/toe-physical-supplier-24h-20260908/scripts']
import producer_original as prod
from prepare_derivative import prepare_with_samples
from measurement_derivative import measure_raw_block
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import initial_ice
@njit(cache=True)
def seed(s):np.random.seed(s)
g=prod.build_geometry(2);cr,ci,_=prod.transverse_coefficients(2,(1,));rows=[]
for vi,V in enumerate([.93,.94,.95,.96,.97]):
 args=(initial_ice(2).ravel(),V-1,32,20,80,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8,930004)
 a=prod.prepare_population(*args);b=prepare_with_samples(*args)
 assert all(np.array_equal(x,y) for x,y in zip(a,b[:4]));assert b[4].shape==(40,) and b[2]==np.mean(b[4])
 rows.append({'V':V,'state_counts_energy_ESS_equal':True,'forty_samples_mean_equal':True})
st,ct=b[:2]
def measure(F,ss):
 seed(ss);return measure_raw_block(st.copy(),ct.copy(),-.03,0,F,cr,ci,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8)
a=measure(6,1930040);b=measure(6,1930040);assert all(np.array_equal(x,y) for x,y in zip(a,b))
def advance(ss):
 seed(ss);x=st.copy();c=ct.copy();anc=np.arange(len(x),dtype=np.int32);labels=np.full((1,len(x)),-1,np.int32)
 for _ in range(3):x,c,anc,labels,_=prod.propagate_sweep(x,c,anc,labels,-.03,g.plaquette_links,g.affected_plaquettes,g.affected_counts,8)
 return x,c
x=advance(2930040);measure(12,1930041);y=advance(2930040);assert all(np.array_equal(a,b) for a,b in zip(x,y))
# Replicas independent seed namespaces; paired V share only their intended seed.
prep=[930000+10000*pi+r for pi in range(2) for r in range(16)]
ms=[1930000+100000*pi+1000*r+10*o+fi for pi in range(2) for r in range(16) for o in range(4) for fi in range(2)]
adv=[2930000+100000*pi+1000*r+o for pi in range(2) for r in range(16) for o in range(3)]
assert len(set(prep))==32 and len(set(ms))==256 and len(set(adv))==96
assert len(set(prep+ms+adv))==384
out={'AST_prepare_only_return_copy':True,'AST_measure_only_raw_return':True,'five_V_fixed_seed_checks':rows,'measurement_seed_repeat':True,'advance_independent_of_suffix_consumption':True,'seed_namespaces_unique':True,'seconds':time.monotonic()-start,'hashes':{n:hashlib.sha256((src/n).read_bytes()).hexdigest() for n in ['production.py','prepare_derivative.py','measurement_derivative.py','producer_original.py','run_production.py','STOCHASTIC_PROTOCOL.md']}}
(p/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
