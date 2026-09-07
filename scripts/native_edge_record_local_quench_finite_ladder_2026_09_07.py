#!/usr/bin/env python3
"""Independent full-Fock check of native-CAR quench and energy-defect bounds.

This is a faithful CAR calculation, not an ambient native-code implementation.
The separate native witness checks that representation interface.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
import hashlib
import copy
import subprocess
import tempfile
import json
import math
import resource
import signal
import sys
import time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.linalg import eigh, expm

AUDIT_INPUT_PATHS = ("scripts/native_edge_record_quench_orbital_check_2026_09_07.py",)
signal.alarm(180)
start = time.monotonic()
V = 6
DIM = 1 << V
I = np.eye(DIM, dtype=complex)
ann = []
for site in range(V):
    op = np.zeros((DIM, DIM), complex)
    for bits in range(DIM):
        if bits >> site & 1:
            op[bits ^ (1 << site), bits] = (-1) ** ((bits & ((1 << site)-1)).bit_count())
    ann.append(op)
edges = [(0,1),(1,2),(2,3),(3,4),(4,5)]
weights = [math.sqrt(2)/3, -1., 1., 1., -math.sqrt(3)/4]
hops = [a*(ann[v].conj().T@ann[w]+ann[w].conj().T@ann[v]) for a,(v,w) in zip(weights,edges)]
seed = 2
he = hops[seed]
J = ann[3].conj().T@ann[2]
rem = [0,1,3,4]
H = sum((hops[e] for e in rem), np.zeros_like(I))
checks = 0
worst = 0.

def close(a,b,label,tol=2e-10):
    global checks, worst
    err = float(np.max(abs(np.asarray(a)-np.asarray(b)),initial=0))
    if not math.isfinite(err) or err > tol:
        raise AssertionError((label,err))
    checks += 1
    worst = max(worst,err)

def norm(x):
    return float(np.linalg.svd(x,compute_uv=False)[0])

def tail(m,x):
    if m == math.inf: return 0.
    term = x**m/math.factorial(m)
    total = term
    for n in range(m+1,1000):
        term *= x/n
        total += term
        if term < 1e-18*max(1,total): return total
    raise AssertionError('Taylor sum did not converge')

def radius_order(kept):
    omitted = set(rem)-set(kept)
    if not omitted: return math.inf
    frontier = {2,3}; reached = set(frontier)
    for distance in range(V):
        if any(v in frontier or w in frontier for e in omitted for v,w in [edges[e]]):
            return distance+1
        nxt = set()
        for e in rem:
            v,w=edges[e]
            if v in frontier:nxt.add(w)
            if w in frontier:nxt.add(v)
        frontier=nxt-reached;reached.update(frontier)
    return math.inf

for v in range(V):
    for w in range(V):
        close(ann[v]@ann[w].conj().T+ann[w].conj().T@ann[v],I if v==w else 0,'CAR')
number=sum((a.conj().T@a for a in ann),np.zeros_like(I))
close(H@number,number@H,'full number')
cases=[]
for kept in [[],[1,3],[0,1,3],[0,1,3,4]]:
    HR=sum((hops[e] for e in kept),np.zeros_like(I))
    ext=H-HR
    m=radius_order(kept)
    close(HR@number,number@HR,'whole-hop truncation number')
    for tau in [0.,1/32,1/16,1/8,1/4,1/2,1.,2.]:
        E=expm(-1j*H*tau)@expm(1j*(H+he)*tau)
        ER=expm(-1j*HR*tau)@expm(1j*(HR+he)*tau)
        close(ER.conj().T@ER,I,'complete local echo')
        err=norm(E-ER)
        bound=min(2.,4*tail(m+1,2*abs(tau))) if m!=math.inf else 0.
        assert err <= bound+2e-10,('echo bound',kept,tau,err,bound)
        jf=expm(-1j*H*tau)@J@expm(1j*H*tau)
        jr=expm(-1j*HR*tau)@J@expm(1j*HR*tau)
        feedback_error=norm(jf@E-jr@ER)
        fb_bound=min(2.,4*tail(m,2*abs(tau))+4*tail(m+1,2*abs(tau))) if m!=math.inf else 0.
        assert feedback_error<=fb_bound+2e-10
        # Fourier total-energy defect from the actual derivative, independent
        # of the commutator expression being certified.
        minus_i_derivative=ER@(HR+he)-HR@ER
        defect=minus_i_derivative+H@ER-ER@(H+he)
        close(defect,ext@ER-ER@ext,'global energy defect identity')
        drift=ER.conj().T@defect
        close(drift,ER.conj().T@ext@ER-ext,'Hermitian drift')
        close(drift,drift.conj().T,'drift Hermiticity')
        energy_error=norm(defect)
        g=min(4*tail(m,2*abs(tau)),8*abs(tau)) if m!=math.inf else 0.
        assert energy_error<=g+2e-10
        # KJ cannot be replaced by a constant J followed by the Record echo.
        wrong_feedback=norm(jf@E-J@E)
        cases.append(dict(kept=kept,m=None if m==math.inf else m,tau=tau,
                          echo_error=err,echo_bound=bound,feedback_error=feedback_error,
                          feedback_bound=fb_bound,energy_defect=energy_error,
                          energy_bound=g,wrong_static_feedback_error=wrong_feedback))

assert max(c['wrong_static_feedback_error'] for c in cases)>.1
assert max(c['echo_error'] for c in cases if c['m']==2)>.01
# Exact-rational sufficient finite-battery certificate, conditional on the
# separately reviewed safe-cap comparison theorem; no fitted parameters.
pi_upper=F(22,7)
sqrt2_upper=F(10,7)
root_upper=F(10,3)
assert sqrt2_upper**2>2
assert root_upper**2>pi_upper**2+1
coefficient=3+2*sqrt2_upper*3*root_upper
delta=F(1,320)
trace_bound=coefficient*delta
assert trace_bound<F(1,10)
energy_bound=3*delta+2*delta**2
assert energy_bound<F(1,100)
levels=97/delta
assert levels.denominator==1 and int(levels)==31040
assert 2**14<int(levels)<=2**15
certificate=dict(delta=str(delta),coefficient_upper=str(coefficient),
                 trace_upper=str(trace_bound),mean_energy_upper=str(energy_bound),
                 cap=97,width=1,lab_time=1,total_rate_bound=3,
                 battery_levels=int(levels),battery_storage_qubits=15,
                 total_native_storage_qubits=12+12+8+15+1,
                 supplied_markov_bath_included=False,
                 source='Conditional safe-cap finite-ladder theorem; no many-qubit numerical propagation')
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
assert rss<180 and time.monotonic()-start<180
result=dict(scope='Full64-dimensional six-mode CAR, all N blocks; independent of native edge-code matrix witness. Fourier times are diagnostic inputs, not labtime transport observations.',
                      edges=edges,weights=weights,seed=seed,cases=cases,checks=checks,
                      worst=worst,certificate=certificate,seconds=time.monotonic()-start,
                      rss_MiB=rss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

checker_path=Path(__file__).resolve().parents[1]/AUDIT_INPUT_PATHS[0]
checker_sha=hashlib.sha256(checker_path.read_bytes()).hexdigest()
def decode_json(raw):
    def unique(pairs):
        obj={}
        for key,value in pairs:
            if key in obj:raise ValueError('Duplicate JSON key: '+key)
            obj[key]=value
        return obj
    def bad_constant(value):raise ValueError('Nonfinite JSON constant: '+value)
    value=json.loads(raw,object_pairs_hook=unique,parse_constant=bad_constant)
    def finite(item):
        if isinstance(item,dict):
            for v in item.values():finite(v)
        elif isinstance(item,list):
            for v in item:finite(v)
        elif type(item) is float and not math.isfinite(item):raise ValueError('Nonfinite parsed JSON number')
    finite(value)
    return value

remaining=180-(time.monotonic()-start)
assert remaining>0
with tempfile.TemporaryFile() as output,tempfile.TemporaryFile() as errors:
    child=subprocess.run([sys.executable,str(checker_path),'--json'],stdout=output,stderr=errors,timeout=remaining,check=False)
    assert child.returncode==0,('independent checker exit',child.returncode)
    assert output.tell()<=2_000_000 and errors.tell()<=100_000,'independent output exceeds capture contract'
    output.seek(0);errors.seek(0)
    raw=output.read().decode('utf-8');stderr=errors.read().decode('utf-8')
    assert not stderr.strip(),stderr
independent=decode_json(raw)
assert hashlib.sha256(checker_path.read_bytes()).hexdigest()==checker_sha

def compare(payload):
    assert isinstance(payload,dict)
    assert set(payload)=={'method','rows','source_sha256','dependencies','resources','seconds','rss_MiB'}
    assert payload.get('source_sha256')==checker_sha
    assert payload.get('method')=='6x6 one-particle exterior spectral identities; all 64 occupation subsets via eigenvalue products; no Fock matrices'
    assert payload.get('dependencies')=={}
    resources=payload.get('resources')
    assert isinstance(resources,dict) and set(resources)=={'timeout_seconds','rss_limit_MiB','blas_threads'}
    for k,v in {'timeout_seconds':180,'rss_limit_MiB':180,'blas_threads':1}.items():
        assert type(resources[k]) is int and resources[k]==v
    for field in ('seconds','rss_MiB'):
        assert type(payload.get(field)) in (int,float) and math.isfinite(payload[field]) and 0<=payload[field]<180
    assert payload['rss_MiB']>0
    rows=payload.get('rows')
    assert isinstance(rows,list) and len(rows)==len(cases)
    expected={(tuple(c['kept']),c['tau']):c for c in cases}
    seen=set(); residual=0.
    for row in rows:
        assert isinstance(row,dict)
        assert set(row)=={'cut','tau','m','echo_norm','energy_drift_norm','echo_bound','energy_bound'}
        assert isinstance(row['cut'],list) and all(type(x) is int for x in row['cut'])
        assert type(row['tau']) in (int,float) and math.isfinite(row['tau'])
        key=(tuple(row['cut']),row['tau'])
        assert key in expected and key not in seen
        seen.add(key); own=expected[key]
        assert row['m'] is None or type(row['m']) is int
        assert row['m']==own['m']
        for theirs,ours in [('echo_norm','echo_error'),('energy_drift_norm','energy_defect'),('echo_bound','echo_bound'),('energy_bound','energy_bound')]:
            v=row[theirs]
            assert type(v) in (int,float) and math.isfinite(v) and v>=0
            diff=abs(v-own[ours]);assert diff<2e-10,(key,theirs,diff)
            residual=max(residual,diff)
    assert seen==set(expected)
    return dict(rows=len(seen),max_residual=residual,scope='Independent comparison covers complete echo and global energy-defect norms, not feedback norm or a 48-qubit dynamical simulation.')

live_comparison=compare(independent)
mutations={}
def reject(name,mutate):
    trial=copy.deepcopy(independent);mutate(trial)
    try:compare(trial)
    except (AssertionError,KeyError,TypeError,ValueError):mutations[name]=True
    else:raise AssertionError('Undetected malformed independent payload: '+name)
reject('missing_row',lambda p:p['rows'].pop())
reject('duplicate_row',lambda p:p['rows'].__setitem__(-1,p['rows'][0]))
reject('NaN_norm',lambda p:p['rows'][0].__setitem__('echo_norm',float('nan')))
reject('wrong_norm',lambda p:p['rows'][0].__setitem__('energy_drift_norm',.1))
reject('bool_order',lambda p:p['rows'][0].__setitem__('m',True))
reject('wrong_scope',lambda p:p.__setitem__('method','full cube simulation'))
reject('wrong_hash',lambda p:p.__setitem__('source_sha256','0'*64))
reject('bool_threads',lambda p:p['resources'].__setitem__('blas_threads',True))
reject('missing_resources',lambda p:p.pop('resources'))
reject('exceeded_RSS',lambda p:p.__setitem__('rss_MiB',181))
reject('zero_RSS',lambda p:p.__setitem__('rss_MiB',0))
reject('extra_top_status',lambda p:p.__setitem__('validation_ok',False))
reject('bool_time',lambda p:p['rows'][0].__setitem__('tau',False))
for label,bad in [('duplicate_JSON_key','{"source_sha256":"WRONG",'+raw.lstrip()[1:]),('NaN_JSON','{"x":NaN}'),('overflow_JSON','{"x":1e999}')]:
    try:decode_json(bad)
    except ValueError:mutations[label]=True
    else:raise AssertionError('Undetected decoder mutation: '+label)

result['independent_comparison']=live_comparison
result['malformed_controls']=mutations
result['dependencies']={AUDIT_INPUT_PATHS[0]:checker_sha}
result['resources']={'timeout_seconds':180,'rss_limit_MiB':180,'blas_threads':1}
result['seconds']=time.monotonic()-start
result['rss_MiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
assert result['seconds']<180 and result['rss_MiB']<180
if '--json' in sys.argv:
    print(json.dumps(result,indent=2,allow_nan=False))
else:
    print('PASS native-CAR quench and conditional finite-ladder resource certificate')
    print('CHECKS',checks,'residual identities; 96 further physical bound assertions; all32 live independent norm rows agree.')
    print('INDEPENDENT',json.dumps(live_comparison,sort_keys=True))
    print('CERTIFICATE',json.dumps(certificate,sort_keys=True))
    print('MALFORMED_CONTROLS',json.dumps(mutations,sort_keys=True))
    print('per_element: explicit CAR matrices and all five whole hopping terms; all32 cut/time echo and drift norms.')
    print('per_site: six chain modes and four omitted-edge distance calculations; no ambient edge-qubit matrix claim.')
    print('per_mode: full64-Fock matrices versus independent6x6 exterior spectral identities over all occupation subsets.')
    print('per_block: four truncations, eight Fourier times, evolved-feedback control and exact rational resource arithmetic.')
    print('lattice_wide: checked and not executed -- no infinite-volume dynamics, full48-qubit numerical evolution or physical bath realization.')
    print('SOURCE_SHA256',result['source_sha256'])
    print('DEPENDENCIES',json.dumps(result['dependencies'],sort_keys=True))
    print('RESOURCES',json.dumps({k:result[k] for k in ['seconds','rss_MiB','resources']},sort_keys=True))
    print('TOTAL: PASS FAIL=0')
