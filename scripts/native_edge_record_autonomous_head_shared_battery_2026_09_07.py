#!/usr/bin/env python3
"""Frozen autonomous head, four event-epoch averages, retained sine battery.

All legal edge prefixes are retained; native nonbridge signs have identical
CAR-gauge observables and their exact multiplicities are explicitly reported.
Full graph-only trails continue to traps; no fair-sign assumption is used there.
The 70-dimensional calculation imports reviewed CAR/packet helpers only. It
never executes the parent's main or independent checker. This is a supplied
spectral-global GKSL fixture, not a closed local apparatus or renewal proof.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'
import copy
import subprocess
import tempfile
import hashlib
import json
import math
from fractions import Fraction
from collections import Counter, defaultdict
from pathlib import Path
import resource
import sys
import time
import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh
import native_edge_record_shared_battery_transport_2026_09_07 as parent

AUDIT_INPUT_PATHS = (
    'scripts/native_edge_record_shared_battery_transport_2026_09_07.py',
    'scripts/native_edge_record_autonomous_head_orbital_check_2026_09_07.py',
)
COMPARISON_TOL = 2e-9
MAX_CHECKER_BYTES = 2_000_000
AUDIT_TIMEOUT_SEC = 180
RSS_LIMIT_MIB = 180
TOL = 2e-9
FULL = (1 << 12)-1
LOW, HIGH, MEAN, CAP = 48.,49.,48.5,97.
GAMMA, DELTA = 1.,1.


def choices(head, mask):
    return [(i, v if u == head else u) for i,(u,v) in enumerate(parent.EDGES)
            if mask & (1 << i) and head in (u,v)]


def enumerate_trails():
    levels = defaultdict(list)
    terminals = []
    def walk(path, head, mask, rates, weight):
        record = dict(path=path, head=head, mask=mask, rates=rates, weight=weight)
        levels[len(path)].append(record)
        incident = choices(head,mask)
        if not incident:
            terminals.append(record)
            return
        for edge, destination in incident:
            walk(path+(edge,), destination,mask ^ (1 << edge),
                 rates+(len(incident),), weight/Fraction(len(incident)))
    walk((),0,FULL,(),Fraction(1))
    return levels,terminals


def rational(x):
    return f'{x.numerator}/{x.denominator}'


def laplace(values,rates):
    gap = values[:,None]-values[None,:]
    result = np.ones(gap.shape,complex)
    for rate in rates:
        result *= rate/(rate+1j*gap)
    return result


class Calculation:
    def __init__(self):
        self.basis,self.hops,self.currents,self.numbers = parent.build_sector()
        self.h0 = parent.hamiltonian(self.hops,FULL)
        groups,ev,vectors,residual = parent.spectral_groups(self.h0)
        self.spectral_error = residual
        self.psi = vectors[:,0].astype(complex)
        self.psi *= np.array([np.exp(-.7j*((b & 1)-((b >> 1) & 1))) for b in self.basis])
        self.psi /= np.linalg.norm(self.psi)
        self.a = np.array([g.energy for g in groups])
        self.sources = np.column_stack([g.projector @ self.psi for g in groups])
        self.initial_energy = float(np.vdot(self.psi,self.h0@self.psi).real)
        self.cache = {}

    def endpoint(self,mask):
        """Retain initial-energy coherences and one common battery at all events.

        A[b,a]=<b|Pi_a psi>. rho[b,c]=sum_ad A[b,a] A*[c,d]
        K(a-b-d+c). EB uses the same joint amplitudes, b=c, and the
        first moment (48.5 + (a+d)/2-b+k Delta) K(a-d).
        No 4900-by-4900 kernel is allocated.
        """
        if mask in self.cache:
            return self.cache[mask]
        h = parent.hamiltonian(self.hops,mask)
        b,V = eigh(h)
        self.spectral_error = max(self.spectral_error,parent.max_abs(h@V-V*b))
        A = V.conj().T @ self.sources
        rho = np.zeros((70,70),complex)
        energy0 = 0j
        for i in range(70):
            for j in range(70):
                K = parent.sine_overlap(self.a[:,None]-self.a[None,:]-b[i]+b[j])
                rho[i,j] = A[i] @ K @ A[j].conj()
            K = parent.sine_overlap(self.a[:,None]-self.a[None,:])
            M = (MEAN + (self.a[:,None]+self.a[None,:])/2-b[i])*K
            energy0 += A[i] @ M @ A[i].conj()
        if abs(energy0.imag)>TOL:
            raise AssertionError('nonreal direct battery moment')
        self.cache[mask] = (h,b,V,rho,float(energy0.real))
        return self.cache[mask]

    def surface(self,mask,rates,k):
        h,b,V,rho0,eb0 = self.endpoint(mask)
        rho = V @ (rho0 * laplace(b,rates)) @ V.conj().T
        eb = eb0 + k*DELTA*float(np.trace(rho).real)
        return rho,eb

    def reset_surface(self,path,rates):
        """Deliberately wrong reset model, used only as a mutation control."""
        rho = np.outer(self.psi,self.psi.conj())
        mask = FULL
        for edge,rate in zip(path,rates):
            h,b,V,_,_ = self.endpoint(mask)
            rho = V @ ((V.conj().T@rho@V)*laplace(b,(rate,))) @ V.conj().T
            newmask = mask ^ (1<<edge)
            _,c,W,_,_ = self.endpoint(newmask)
            # Independent fresh battery dephasing at this single deletion.
            A = W.conj().T@V
            incoming = V.conj().T@rho@V
            out = np.zeros((70,70),complex)
            for i in range(70):
                for j in range(70):
                    K = parent.sine_overlap(b[:,None]-b[None,:]-c[i]+c[j])
                    out[i,j] = np.sum(A[i,:,None]*incoming*A[j,None,:].conj()*K)
            rho = W@out@W.conj().T
            mask = newmask
        return rho


def parse_checker(text):
    def unique(pairs):
        obj = {}
        for key,value in pairs:
            if key in obj:
                raise ValueError('duplicate checker JSON key: '+key)
            obj[key] = value
        return obj
    def bad_constant(value):
        raise ValueError('nonfinite checker JSON token: '+value)
    return json.loads(text,object_pairs_hook=unique,parse_constant=bad_constant)


def compare_checker(rows,actual):
    """Compare independently produced observations, translating mask convention.

    Primary stores LIVE mask, orbital checker stores DELETED mask. Orbital
    epsilon has h=-epsilon, hence it equals minus the primary coefficient;
    both implement the same oriented physical current, with no sign repair.
    """
    def finite_tree(value):
        if isinstance(value,float) and not math.isfinite(value):
            raise ValueError('nonfinite checker number')
        if isinstance(value,dict):
            for item in value.values(): finite_tree(item)
        elif isinstance(value,list):
            for item in value: finite_tree(item)
    finite_tree(actual)
    if not isinstance(actual,dict) or actual.get('path_counts') != [1,3,6,12,24]:
        raise ValueError('checker header/census mismatch')
    edges=[[u,v,-int(c)] for (u,v),c in zip(parent.EDGES,parent.COEFFICIENTS)]
    if actual.get('edges') != edges:
        raise ValueError('checker physical edge convention mismatch')
    if actual.get('contract') != dict(timeout_seconds=180,blas_threads=1,rss_limit_MiB=180):
        raise ValueError('checker resource contract mismatch')
    if not isinstance(actual.get('rows'),list) or len(actual['rows']) != len(rows) or len(rows)!=90:
        raise ValueError('checker must contain all 90 surfaces')
    maximum=0.
    def number(a,b,label):
        nonlocal maximum
        if type(b) not in (int,float) or not math.isfinite(b):
            raise ValueError(label+': invalid numeric value')
        delta=abs(a-b)
        if delta>COMPARISON_TOL:
            raise ValueError(label+f': disagreement {delta}')
        maximum=max(maximum,delta)
    def exact(a,b,label):
        if type(a) is not type(b) or a!=b:
            raise ValueError(label+': discrete mismatch')
        if isinstance(a,list):
            for left,right in zip(a,b): exact(left,right,label)
    indexed={}
    for other in actual['rows']:
        if not isinstance(other,dict) or not isinstance(other.get('path'),list):
            raise ValueError('invalid checker row')
        key=(tuple(other['path']),other.get('surface'))
        if key in indexed:
            raise ValueError('duplicate checker surface')
        indexed[key]=other
    for row in rows:
        key=(tuple(row['path']),row['side'])
        if key not in indexed:
            raise ValueError('missing checker path/side')
        other=indexed[key]
        for a,b,label in ((row['path'],other['path'],'path'),(row['step'],other['event'],'event'),
                          (row['side'],other['surface'],'side'),(row['head'],other['head'],'head'),
                          ('deleted_edge_bits',other['mask_convention'],'mask convention'),
                          (FULL^row['mask'],other['mask'],'mask'),
                          (row['rates'],other['rates'],'rates'),(row['spent_fuel'],other['deletions'],'fuel'),
                          (row['support'],other['support_count'],'support'),
                          (row['density_window_ok'],other['density_pass'],'density comparator')):
            exact(a,b,label)
        if type(other['weight']) is not str or Fraction(row['weight'])!=Fraction(other['weight']):
            raise ValueError('exact rational weight mismatch')
        if not isinstance(other['density'],list) or len(other['density'])!=8:
            raise ValueError('density shape mismatch')
        if not isinstance(other['currents'],list) or len(other['currents'])!=12:
            raise ValueError('current shape mismatch')
        for a,b in zip(row['densities'],other['density']): number(a,b,'density')
        for edge,value in enumerate(other['currents']):
            number(row['currents'].get(str(edge),0.),value,'oriented current')
        number(row['matter_energy'],other['energy'],'matter energy')
        number(row['battery_energy'],other['battery']['mean'],'direct battery energy')
        number(1.,other['battery']['norm'],'battery norm')
        number(4.,other['N'],'particle number')
        if row['side']=='pre':
            number(row['front_current'],other['selected_edge_current'],'selected front')
        else:
            exact(None,other['selected_edge_current'],'post selected front')
    for item in actual['mutations'].values():
        exact(True,item['detected'],'independent mutation status')
    number(0.,actual['max_ledger_residual'],'independent energy ledger')
    number(0.,actual['max_battery_norm_error'],'independent battery normalization')
    resources=actual['resources']
    if not (0<=resources['seconds']<=180 and 0<resources['peak_rss_MiB']<180):
        raise ValueError('checker execution envelope exceeded')
    return maximum


def invoke_checker(command,timeout):
    """Use disk-backed capture; nonzero/timeout/oversize fail closed."""
    with tempfile.TemporaryFile(mode='w+b') as output, tempfile.TemporaryFile(mode='w+b') as errors:
        child=subprocess.run(command,stdout=output,stderr=errors,timeout=timeout,check=False)
        if child.returncode:
            raise ValueError(f'checker nonzero exit {child.returncode}')
        if output.tell()>MAX_CHECKER_BYTES or errors.tell()>MAX_CHECKER_BYTES:
            raise ValueError('checker output exceeds bounded response contract')
        output.seek(0)
        return parse_checker(output.read(MAX_CHECKER_BYTES).decode('utf-8'))


def validate_live(rows,started,check):
    command=[sys.executable,str(Path(__file__).resolve().parent/Path(AUDIT_INPUT_PATHS[1]).name),'--json']
    try:
        remaining=AUDIT_TIMEOUT_SEC-(time.perf_counter()-started)
        if remaining<=0: raise ValueError('no checker runtime remains')
        actual=invoke_checker(command,min(180,remaining))
        residual=compare_checker(rows,actual)
        check('live_independent_all90',True,max_residual=residual,tolerance=COMPARISON_TOL,
              checker_resources=actual['resources'])
        # Mutants start from the actual live response, never primary expectations.
        mutations={}
        def rejected(name,mutate):
            wrong=copy.deepcopy(actual)
            mutate(wrong)
            try: compare_checker(rows,wrong)
            except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError,OverflowError): mutations[name]=True
            else: mutations[name]=False
        rejected('missing_row',lambda d:d['rows'].pop())
        rejected('duplicate_row',lambda d:d['rows'].__setitem__(1,d['rows'][0]))
        rejected('density_shape',lambda d:d['rows'][0]['density'].pop())
        rejected('missing_field',lambda d:d['rows'][0].pop('battery'))
        rejected('NaN',lambda d:d['rows'][0].__setitem__('energy',float('nan')))
        rejected('fuel',lambda d:d['rows'][0].__setitem__('deletions',1))
        rejected('head',lambda d:d['rows'][0].__setitem__('head',1))
        rejected('mask',lambda d:d['rows'][0].__setitem__('mask',1))
        rejected('rate',lambda d:d['rows'][0]['rates'].__setitem__(0,2))
        rejected('weight',lambda d:d['rows'][0].__setitem__('weight','1/4'))
        rejected('current_sign',lambda d:d['rows'][0]['currents'].__setitem__(0,-d['rows'][0]['currents'][0]))
        rejected('battery',lambda d:d['rows'][0]['battery'].__setitem__('mean',0.))
        rejected('post_front',lambda d:d['rows'][1].__setitem__('selected_edge_current',0.))
        for name,code in (('malformed_live_response',"print('{corrupt')"),
                          ('failed_live_process',"raise SystemExit(7)"),
                          ('duplicate_json',"print('{\"rows\": [], \"rows\": []}')"),
                          ('nonfinite_json',"print('{\"rows\": NaN}')")):
            try: invoke_checker([sys.executable,'-c',code],5)
            except (ValueError,subprocess.SubprocessError): mutations[name]=True
            else: mutations[name]=False
        check('live_comparison_mutations',all(mutations.values()),detected=mutations)
    except (OSError,ValueError,KeyError,TypeError,IndexError,ZeroDivisionError,OverflowError,subprocess.SubprocessError) as error:
        check('live_independent_all90',False,error=f'{type(error).__name__}: {error}')


def main():
    started = time.perf_counter()
    if sys.argv[1:] not in ([],['--json']):
        raise SystemExit('usage: native_edge_record_autonomous_head_shared_battery_2026_09_07.py [--json]')
    checks = []
    def check(name,ok,**details):
        checks.append(dict(name=name,ok=bool(ok),**details))
    levels,terminals = enumerate_trails()
    counts = [len(levels[j]) for j in range(1,5)]
    weights = [sum((r['weight'] for r in levels[j]),Fraction()) for j in range(1,5)]
    connected = all(parent.component_count(r['mask']) == 1 for j in range(5) for r in levels[j])
    degrees = sorted({r['rates'] for r in levels[4]})
    check('exact_first_four_census',counts == [3,6,12,24] and all(w==1 for w in weights)
          and connected and degrees == [(3,2,2,2)],counts=counts,weights=list(map(rational,weights)),degree_sequences=degrees)
    terminal_mass = sum((r['weight'] for r in terminals),Fraction())
    # At every depth, reached mass plus all earlier terminal mass must be one.
    mass_errors = [sum((r['weight'] for r in levels[j]),Fraction())+
                   sum((r['weight'] for r in terminals if len(r['path'])<j),Fraction())-1
                   for j in levels]
    check('full_trail_mass_to_traps',terminal_mass==1 and not any(mass_errors),
          terminal_count=len(terminals),terminal_mass=rational(terminal_mass))
    check('mutation_dropped_path',sum((r['weight'] for r in levels[4][1:]),Fraction()) != 1)
    check('mutation_wrong_rate',Fraction(1,3)*Fraction(1,3) != levels[2][0]['weight'])
    # Direct scalar exponential integrals, with a stated deterministic tail bound.
    gap = 1.37
    integration_error = 0.
    direct = 1+0j
    for r in (3,2,2,2):
        re = quad(lambda t:r*math.exp(-r*t)*math.cos(gap*t),0,20,epsabs=1e-12)[0]
        im = quad(lambda t:-r*math.exp(-r*t)*math.sin(gap*t),0,20,epsabs=1e-12)[0]
        val = re+1j*im
        integration_error = max(integration_error,abs(val-r/(r+1j*gap)))
        direct *= val
    exact = np.prod([r/(r+1j*gap) for r in (3,2,2,2)])
    check('exponential_gap_integral',max(integration_error,abs(direct-exact))<1e-11,
          residual=max(integration_error,abs(direct-exact)),tail_bound=4*math.exp(-40))
    check('mutation_gap_sign',abs(direct-exact.conjugate())>1e-3)
    meanrate = (sum((3,2,2,2))/4)
    check('mutation_mean_rate',abs(exact-(meanrate/(meanrate+1j*gap))**4)>1e-3)
    # First moment quadrature is separate from the ledger, including common fuel.
    moment_error=0.
    for u,v in ((0.,0.),(.2,-.3),(3.2,2.7),(-.7,.1),(2.,-2.)):
        lo,hi=max(LOW+u,LOW+v),min(HIGH+u,HIGH+v)
        directmoment=0. if lo>=hi else quad(lambda e:2*e*math.sin(math.pi*(e-u-LOW))*math.sin(math.pi*(e-v-LOW)),lo,hi,epsabs=1e-11)[0]
        kernel=(MEAN+(u+v)/2)*parent.sine_overlap_scalar(u-v)
        moment_error=max(moment_error,abs(directmoment-kernel))
    check('direct_packet_first_moments',moment_error<1e-10,residual=moment_error)
    # Uniform full-system norm <=24 gives invariant support, even after bridges.
    check('continuous_cap_enclosure',LOW-2*24>=0 and HIGH+2*24<=CAP,
          enclosure=[LOW-48,HIGH+48],cap=CAP)
    check('mutation_insufficient_cap',HIGH+48>CAP-1)
    calc=Calculation()
    rows=[]
    worst=defaultdict(float)
    for j in range(1,5):
        for path in levels[j]:
            for side in ('pre','post'):
                k=j-1 if side=='pre' else j
                mask=path['mask'] | (1<<path['path'][-1]) if side=='pre' else path['mask']
                rho,eb=calc.surface(mask,path['rates'],k)
                h,b,V,_,_=calc.endpoint(mask)
                measure=parent.measure(rho,h,mask,calc.currents,calc.numbers)
                herm,trace,mineig=parent.density_numerics(rho)
                drift=abs(measure['energy']+eb+(12-k)*DELTA-(calc.initial_energy+MEAN+12*DELTA))
                worst['hermiticity']=max(worst['hermiticity'],herm)
                worst['trace']=max(worst['trace'],trace)
                worst['negative_eigenvalue']=max(worst['negative_eigenvalue'],-mineig)
                worst['number']=max(worst['number'],abs(measure['number']-4))
                worst['energy_drift']=max(worst['energy_drift'],drift)
                worst['cap_excess']=max(worst['cap_excess'], -(LOW+float(calc.a.min()-b.max())+k), HIGH+float(calc.a.max()-b.min())+k-CAP)
                front_current=measure['currents'].get(path['path'][-1])
                rows.append(dict(path=list(path['path']),step=j,side=side,head=path['head'] if side=='post' else (0 if j==1 else next(r['head'] for r in levels[j-1] if r['path']==path['path'][:-1])),
                    edge=path['path'][-1],mask=mask,spent_fuel=k,live_fuel=12-k,rates=list(path['rates']),
                    weight=rational(path['weight']),sign_histories=2**k,weight_per_sign=rational(path['weight']/2**k),
                    densities=list(measure['densities']),currents={str(e):x for e,x in measure['currents'].items()},
                    matter_energy=measure['energy'],battery_energy=eb,total_energy=measure['energy']+eb+12-k,
                    support=measure['support'],front_current=front_current,
                    battery_support_enclosure=[LOW+float(calc.a.min()-b.max())+k, HIGH+float(calc.a.max()-b.min())+k],
                    density_window_ok=min(measure['densities'])>=.1 and max(measure['densities'])<=.9,
                    support_comparator_ok=measure['support']>=4))
    check('all_prefix_state_energy_N',len(rows)==90 and max(worst.values())<TOL,**worst)
    check('fixedN_spectral_resolution',len(calc.basis)==70 and calc.spectral_error<TOL,residual=calc.spectral_error)
    # A common fuel translation leaves rho invariant but moves EB by exactly k.
    p=levels[2][0]; rho,eb=calc.surface(p['mask'],p['rates'],2)
    ledger=calc.initial_energy+MEAN+12
    em=float(np.trace(rho@calc.endpoint(p['mask'])[0]).real)
    check('mutation_missing_or_double_fuel',abs(em+(eb-2)+10-ledger)>1 and abs(em+(eb+2)+10-ledger)>1)
    wrongmask=p['mask']|(1<<p['path'][-1])
    wrongrho,_=calc.surface(wrongmask,p['rates'],2)
    check('mutation_mask_timing',parent.max_abs(rho-wrongrho)>1e-4,residual=parent.max_abs(rho-wrongrho))
    no_wait,_=calc.surface(wrongmask,p['rates'][:-1],1)
    pre,_=calc.surface(wrongmask,p['rates'],1)
    check('mutation_omitted_pre_wait',parent.max_abs(pre-no_wait)>1e-4,residual=parent.max_abs(pre-no_wait))
    reset=calc.reset_surface(p['path'],p['rates'])
    check('mutation_reset_battery',parent.max_abs(rho-reset)>1e-4,residual=parent.max_abs(rho-reset))
    summary=[]
    for j in range(1,5):
        for side in ('pre','post'):
            chosen=[r for r in rows if r['step']==j and r['side']==side]
            summary.append(dict(step=j,side=side,paths=len(chosen),weight=rational(sum((Fraction(r['weight']) for r in chosen),Fraction())),
                support_min=min(r['support'] for r in chosen),support_max=max(r['support'] for r in chosen),
                support_pass_paths=sum(r['support_comparator_ok'] for r in chosen),
                density_min=min(min(r['densities']) for r in chosen),density_max=max(max(r['densities']) for r in chosen),
                matter_energy_min=min(r['matter_energy'] for r in chosen),matter_energy_max=max(r['matter_energy'] for r in chosen),
                battery_energy_min=min(r['battery_energy'] for r in chosen),battery_energy_max=max(r['battery_energy'] for r in chosen),
                front_max=max((abs(r['front_current']) for r in chosen if r['front_current'] is not None),default=None),
                weighted_matter_energy=sum(float(Fraction(r['weight']))*r['matter_energy'] for r in chosen),
                weighted_battery_energy=sum(float(Fraction(r['weight']))*r['battery_energy'] for r in chosen)))
    trajectory_front=[]
    for path in levels[4]:
        pre=[next(r for r in rows if r['path']==list(path['path'][:j]) and r['side']=='pre') for j in range(1,5)]
        frontmax=max(abs(r['front_current']) for r in pre)
        trajectory_front.append(dict(path=list(path['path']),weight=rational(path['weight']),
            selected_pre_currents=[r['front_current'] for r in pre],front_max=frontmax,
            front_comparator_ok=frontmax>=.05,all_pre_support_ok=all(r['support_comparator_ok'] for r in pre)))
    trap_summary=[]
    for depth in sorted({len(r['path']) for r in terminals}):
        ts=[r for r in terminals if len(r['path'])==depth]
        trap_summary.append(dict(events=depth,count=len(ts),weight=rational(sum((r['weight'] for r in ts),Fraction()))))
    census=[dict(events=j,count=len(levels[j]),mass=rational(sum((r['weight'] for r in levels[j]),Fraction())),
                 disconnected=sum(parent.component_count(r['mask'])>1 for r in levels[j]),
                 degree_sequences=[dict(rates=list(key),count=count) for key,count in sorted(Counter(r['rates'] for r in levels[j]).items())]) for j in sorted(levels)]
    validate_live(rows,started,check)
    elapsed=time.perf_counter()-started
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform=='darwin' else 1024)
    check('execution_envelope',elapsed<=AUDIT_TIMEOUT_SEC and rss<RSS_LIMIT_MIB,elapsed_seconds=elapsed,rss_mib=rss)
    payload=dict(schema='autonomous-head-shared-battery-v1',validation_ok=all(c['ok'] for c in checks),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependencies={p:hashlib.sha256((Path(__file__).resolve().parents[1]/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},
        fixture=dict(gamma=GAMMA,t=1.,Delta=DELTA,head=0,N=4,packet=[LOW,HIGH],cap=CAP,initial_matter_energy=calc.initial_energy),
        checks=checks,summary=summary,census=census,traps=trap_summary,surfaces=rows,trajectory_front=trajectory_front,
        benchmark_failures=dict(support_surfaces=sum(not r['support_comparator_ok'] for r in rows), density_surfaces=sum(not r['density_window_ok'] for r in rows)),
        scope='Path-conditioned event-epoch mean states; no fixed-time ensemble or every-wait bound. First-four signs are gauge-equivalent nonbridges. Later census is graph-only with complete sign sum.',
        unresolved=['Supplied carrier, pulse and role scaffold','Spectrally global lift; no local closed-unitary apparatus','Continuous battery coherence and degenerate history memory','External time, Markov reservoir and entropy sink','No replenishment or indefinite renewal'])
    if '--json' in sys.argv:
        print(json.dumps(payload,allow_nan=False))
    else:
        print('AUTONOMOUS HEAD retained sine[48,49] cap97 gamma=t=Delta=1 N4 head0')
        for s in summary:
            print(f"DATA j={s['step']} {s['side']} paths={s['paths']} mass={s['weight']} support={s['support_min']}..{s['support_max']} pass={s['support_pass_paths']} density=[{s['density_min']:.8f},{s['density_max']:.8f}] E=[{s['matter_energy_min']:.8f},{s['matter_energy_max']:.8f}] EB=[{s['battery_energy_min']:.8f},{s['battery_energy_max']:.8f}] front_max={s['front_max']}")
        for r in rows:
            print(f"PREFIX path={','.join(map(str,r['path']))} {r['side']} mask={r['mask']} fuel={r['live_fuel']} weight={r['weight']} rates={r['rates']} support={r['support']} E={r['matter_energy']:.9f} EB={r['battery_energy']:.9f} front={r['front_current']}")
        for c in checks:
            print(('PASS' if c['ok'] else 'FAIL')+' '+c['name']+' '+json.dumps({k:v for k,v in c.items() if k not in ('name','ok')}))
        print('BENCHMARK '+json.dumps(payload['benchmark_failures'])+f" trajectory_front_pass={sum(r['front_comparator_ok'] for r in trajectory_front)}/24 all_pre_support_pass={sum(r['all_pre_support_ok'] for r in trajectory_front)}/24")
        print('TRAPS '+json.dumps(trap_summary))
        print('SOURCE_SHA256 '+payload['source_sha256'])
        print('SCOPE '+payload['scope'])
        print('UNRESOLVED '+ '; '.join(payload['unresolved']))
        print('per_element: checked every live-edge current and selected pre-event edge on all ninety path-prefix surfaces.')
        print('per_site: checked all eight site densities and their fixed-number sum on every reported event-epoch mean state.')
        print('per_mode: checked complete fixed-N spectral resolutions, retaining degenerate and nonstationary energy coherences.')
        print('per_block: checked all forty-five edge prefixes with exact path weights, both timing surfaces and direct battery moments.')
        print('lattice_wide: checked and not executed -- this finite supplied cube generator does not resolve an infinite-lattice formation or renewal law.')
        print(f"TOTAL: PASS={sum(c['ok'] for c in checks)} FAIL={sum(not c['ok'] for c in checks)}")
    return int(not payload['validation_ok'])


if __name__=='__main__':
    raise SystemExit(main())
