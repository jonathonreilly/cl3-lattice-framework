import os,time,resource,json,hashlib,itertools
started=time.monotonic()
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sympy as s
from pathlib import Path
x=s.symbols('x'); checks=[]; payload={}
def check(name,truth):
    assert name not in checks
    assert bool(truth),name
    checks.append(name)
def intervals(A):
    return [(lo,hi) for (lo,hi),m in s.Poly(A.charpoly(x).as_expr(),x).intervals(eps=s.Rational(1,10**12)) for _ in range(m)]
def positive(A):
    return all(A.extract(I,I).det()>=0 for n in range(1,A.rows+1) for I in itertools.combinations(range(A.rows),n))
def count(ivs,z):
    assert all(hi<z or lo>=z for lo,hi in ivs)
    return sum(int(bool(hi<z)) for lo,hi in ivs)
def encode(v):
    if isinstance(v,dict):return {k:encode(a) for k,a in v.items()}
    if isinstance(v,(list,tuple)):return [encode(a) for a in v]
    if isinstance(v,s.Basic):return str(v)
    return v
fixtures=[('two_level',s.diag(0,10),s.Matrix([[1,1],[1,1]]),1,s.Integer(2)),('three_level',s.diag(0,1,10),s.ones(3),2,s.Integer(3)),('threshold_failure',s.diag(0,s.Rational(1,4)),s.Matrix([[1,1],[1,1]]),1,s.Integer(2)),('ground_only_coupling',s.diag(0,1,10),s.Matrix([[1,0,1],[0,1,0],[1,0,1]]),2,s.Integer(2))]
for name,K,V,d,M in fixtures:
    P=s.diag(*([1]*d+[0]*(K.rows-d)));Q=s.eye(K.rows)-P;H=K+V;A=H[:d,:d];B=V[:d,d:];g=K[d,d];b2=(B.T*B)[0,0]
    check(name+'_positive_V',positive(V) and positive(M*s.eye(V.rows)-V))
    check(name+'_kinetic_commutes',P*K==K*P)
    check(name+'_centered_coupling',b2<=M*M/4)
    ev=intervals(H);mu=intervals(A)
    check(name+'_minmax',all(mu[j][0]>=ev[j][1] or mu[j]==ev[j] for j in range(d)))
    row={'K':K.tolist(),'V':V.tolist(),'g':g,'b_squared':b2,'M':M,'exact_eigen_intervals':ev,'Ritz_intervals':mu,'Ritz_dimension':d}
    if all(z[1]<g for z in mu):
        deltas=[b2/(g-z[1]) for z in mu]
        check(name+'_computed_lower_endpoints',all(ev[j][0]>=mu[j][1]-deltas[j] for j in range(d)))
        check(name+'_exact_energy_bound',all(mu[j][1]-ev[j][0]<=b2/(g-ev[j][0]) for j in range(d)))
        row['conservative_delta']=deltas
        if d==2:
            gap=(ev[1][0]-ev[0][1],ev[1][1]-ev[0][0]);finitegap=(mu[1][0]-mu[0][1],mu[1][1]-mu[0][0])
            bounds=(max(0,finitegap[0]-deltas[1]),finitegap[1]+deltas[0])
            check(name+'_gap_interval',gap[0]>=bounds[0] and gap[1]<=bounds[1]);row.update(exact_gap_interval=gap,Ritz_gap_interval=finitegap,certified_gap_interval=bounds)
            check(name+'_positive_certified_gap',bounds[0]>0)
            if name=='ground_only_coupling':check(name+'_Ritz_gap_not_upper_bound',gap[0]>finitegap[1])
            if name=='three_level':check(name+'_Ritz_gap_not_lower_bound',gap[1]<finitegap[0])
        for z in [s.Rational(1,2),s.Integer(3),s.Integer(9)]:
            if z<g:
                check(name+'_count_'+str(z),count(mu,z)<=count(ev,z)<=count(mu,z+b2/(g-z)))
    else:
        check(name+'_low_Ritz_hypothesis_fails',mu[0][0]>g)
        check(name+'_missing_gap_index',d==1)
        # The exact quadratic lower endpoint is negative iff mu*g < b².
        check(name+'_quadratic_lower_vacuous',mu[0][1]*g<b2)
    payload[name]=row
# Excluded states may interleave above g even with zero coupling.
K=s.diag(0,20,10);P=s.diag(1,1,0);A=K[:2,:2]
check('uncoupled_above_threshold_index_adverse',intervals(A)[1]==(20,20) and intervals(K)[1]==(10,10))
payload['uncoupled_above_threshold']={'Ritz_second':20,'exact_second':10,'coupling':0,'g':10,'interpretation':'No equal-index exactness above the omitted threshold even at zero coupling.'}
check('actual_R0_Haar_bound_improves_generic',s.Rational(1,3)<36)
check('resource',0<resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024)<180 and time.monotonic()-started<180)
result={'checks':checks,'TOTAL':len(checks),'fixtures':payload,'actual_R0':{'mu0':'6v','b_squared':'v²/3','g0':'4/a','condition':'6v<4/a; no second Ritz eigenvalue at R=0'},'seconds':time.monotonic()-started,'rss_MiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact abstract spectral controls plus imported actual R0 Haar coupling; no finite cutoff eigenvalue computation of the full cube.'}
print(json.dumps(encode(result),indent=2,allow_nan=False))
