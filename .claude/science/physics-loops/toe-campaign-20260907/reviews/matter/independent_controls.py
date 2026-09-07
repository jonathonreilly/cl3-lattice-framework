#!/usr/bin/env python3
"""Independent finite controls. No candidate runner or repository imports.

This is a diagnostic mathematical check, not a formal scientific audit.
The main control builds sequential spectral translations in energy space and
integrates their actual battery wavefunction, including free dwell phases.
"""
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import hashlib
import itertools
import json
from pathlib import Path
import platform
import sys
import numpy as np
import scipy
from scipy.integrate import quad, quad_vec
from scipy.linalg import eigh

OUT = Path(__file__).resolve().parent
ROOT = Path('/Users/jonreilly/Projects/Physics-worktrees/toe-campaign-20260907')
SOURCES = [ROOT/'docs/NATIVE_RECORD_BATTERY_FINITE_PATCH_LOCALITY_NOTE_2026-09-07.md',
           ROOT/'scripts/native_record_battery_finite_patch_locality_2026_09_07.py']
BOUND = ['de7ec27441c5690af8f07018ad0bfce598d4f84cf69ee2e918cfcac4d7ebdaed',
         'b8c14302200be820a6d14357939bd7a35c19a0602192c80df0669ad8241d4a41']
CHECKS = []

def check(label, condition, **data):
    CHECKS.append(dict(label=label, passed=bool(condition), **data))
    print(('PASS ' if condition else 'FAIL ') + label)

def opnorm(a):
    return float(np.linalg.svd(a, compute_uv=False)[0])

def trace_norm(a):
    return float(np.sum(np.linalg.svd(a, compute_uv=False)))

def commutator(a,b):
    return a@b-b@a

def embed_one(n, pos, matrix):
    out = np.array([[1]],complex)
    for site in range(n):
        out = np.kron(out, matrix if site == pos else np.eye(2))
    return out

def propagator(matrix):
    eigenvalues, basis = eigh(matrix)
    return lambda time: (basis*np.exp(1j*time*eigenvalues))@basis.conj().T

X = np.array([[0,1],[1,0]],complex)
Z = np.diag([1.,-1.]).astype(complex)
n = 4
dim = 2**n
eye = np.eye(dim)
xs = [embed_one(n,j,X) for j in range(n)]
zs = [embed_one(n,j,Z) for j in range(n)]
x_coeffs = [.53,.79,1.11,.91]
z_coeffs = [.23,-.17,.19,-.31]
zz_coeffs = [.8,-.37,1.23]
terms = [(x_coeffs[j]*xs[j],frozenset([j])) for j in range(n)]
terms += [(z_coeffs[j]*zs[j],frozenset([j])) for j in range(n)]
terms += [(zz_coeffs[j]*zs[j]@zs[j+1],frozenset([j,j+1])) for j in range(n-1)]
H0 = sum(a for a,_ in terms)
events = []
current_terms = list(terms)
for location, patch in [(0,frozenset([0,1])),(3,frozenset([2,3]))]:
    deleted = x_coeffs[location]*xs[location]
    full_before = sum(a for a,_ in current_terms)
    patch_before = sum(a for a,s in current_terms if s <= patch)
    full_after, patch_after = full_before-deleted, patch_before-deleted
    crossing = [(a,s) for a,s in current_terms if s&patch and not s<=patch]
    boundary = sum(opnorm(a) for a,_ in crossing)
    projectors = [(eye+sign*zs[location])/2 for sign in [-1,1]]
    events.append(dict(site=location, patch=patch, h=deleted, before=full_before,
                       after=full_after, pin=patch_before, pout=patch_after,
                       cross=crossing, B=boundary, delta=opnorm(deleted), qs=projectors))
    current_terms = [(a,s) for a,s in current_terms
                     if not (s == frozenset([location]) and np.array_equal(a,deleted))]
H2 = events[-1]['after']

def packet(energy,offset,width):
    coordinate = (np.asarray(energy)-offset)/width
    return np.sqrt(2/width)*np.sin(np.pi*coordinate)*((coordinate >= 0)&(coordinate <= 1))

def fourier_amplitude(tau,width,offset=0.):
    # Derived from sin(pi*x)=(e^(i*pi*x)-e^(-i*pi*x))/(2i).
    def oscillatory_integral(q):
        return width*np.exp(.5j*q*width)*np.sinc(q*width/(2*np.pi))
    return np.exp(1j*tau*offset)*(oscillatory_integral(tau+np.pi/width)
        -oscillatory_integral(tau-np.pi/width))/(2j*np.sqrt(np.pi*width))

def spectral_projectors(matrix):
    values,vectors = eigh(matrix)
    groups = []
    for k,value in enumerate(values):
        if groups and abs(value-groups[-1][0]) < 1e-9:
            groups[-1][1].append(k)
        else:
            groups.append([float(value),[k]])
    return [(value, vectors[:,ids]@vectors[:,ids].conj().T) for value,ids in groups]

def shift_operators(event):
    incoming = spectral_projectors(event['pin'])
    outgoing = spectral_projectors(event['pout'])
    return [[(float(a-b), pb@q@pa) for a,pa in incoming for b,pb in outgoing]
            for q in event['qs']]

for event in events:
    event['shifts'] = shift_operators(event)

def propagate_in_energy(initial,dwells):
    # f(E) = exp(-i*elapsed_free*E) sum_s coeff[s] beta(E-s).
    # Translation u acts directly on this formula and supplies exp(i*free*u).
    branches = [([(0.,initial)],())]
    elapsed_free = 0.
    cumulative = []
    for event,(duration,free) in zip(events,dwells):
        matter_dwell = propagator(event['before'])(-duration)
        branches = [([(s,matter_dwell@c) for s,c in components],history)
                    for components,history in branches]
        elapsed_free += duration if free else 0.
        cumulative.append(elapsed_free)
        next_branches = []
        for components,history in branches:
            for outcome,ops in enumerate(event['shifts']):
                # All terms are retained, including numerical zero coefficients.
                new = [(s+u,np.exp(1j*elapsed_free*u)*(matrix@coefficient))
                       for u,matrix in ops for s,coefficient in components]
                next_branches.append((new,history+(outcome,)))
        branches = next_branches
    return branches,elapsed_free,cumulative

def product_fiber(tau,dwells,local):
    operators = [(eye,())]
    elapsed_free = 0.
    for event,(duration,free) in zip(events,dwells):
        d = propagator(event['before'])(-duration)
        elapsed_free += duration if free else 0.
        before,after = ((event['pin'],event['pout']) if local
                        else (event['before'],event['after']))
        left,right = propagator(after)(-tau-elapsed_free),propagator(before)(tau+elapsed_free)
        operators = [(left@q@right@d@op,hist+(outcome,))
                     for op,hist in operators for outcome,q in enumerate(event['qs'])]
    return operators

def energy_space_check():
    generator = np.random.default_rng(2026090703)
    initial = generator.normal(size=(dim,2))+1j*generator.normal(size=(dim,2))
    initial /= np.linalg.norm(initial)
    # A genuine entangled matter/reference input, rather than a favorable matter eigenstate.
    schmidt = np.linalg.svd(initial,compute_uv=False)
    allowance = sum(opnorm(e['pin'])+opnorm(e['pout']) for e in events)
    width = 3.7
    rows = []
    for dwells in [[(.17,False),(.29,False)],[(.17,False),(.29,True)],[(.17,True),(.29,True)]]:
        branches,free,cumulative = propagate_in_energy(initial,dwells)
        max_fiber = wrong_shift = total_probability = final_energy = 0.
        largest_quad_error = 0.
        reduced_energy_rhos = []
        for components,history in branches:
            shifts = np.array([x[0] for x in components])
            coefficients = np.stack([x[1] for x in components],axis=-1)
            flat = coefficients.reshape(dim*2,-1)
            # Piecewise quadrature of actual energy wavefunction, not overlap kernels.
            cuts = np.unique(np.round(np.r_[allowance+shifts,allowance+width+shifts],12))
            def integrand(energy):
                wave = flat@packet(energy-shifts,allowance,width)
                rho = np.outer(wave,wave.conj())
                expected = np.vdot(wave.reshape(dim,2),H2@wave.reshape(dim,2)).real
                return np.r_[rho.ravel(),expected+energy*np.vdot(wave,wave).real]
            result,error = quad_vec(integrand,cuts[0],cuts[-1],points=cuts[1:-1],
                                    epsabs=1e-9,epsrel=1e-9)
            rho = result[:-1].reshape(dim*2,dim*2)
            reduced_energy_rhos.append(rho)
            total_probability += float(np.trace(rho).real)
            final_energy += float(result[-1].real)
            largest_quad_error = max(largest_quad_error,float(error))
            for tau in [-1.7,-.22,.31,1.1]:
                direct = np.einsum('abs,s->ab',coefficients,np.exp(1j*tau*shifts))
                local = dict((hist,op) for op,hist in product_fiber(tau,dwells,True))[history]@initial
                max_fiber = max(max_fiber,float(np.linalg.norm(direct-local)))
                omitted = dict((hist,op) for op,hist in product_fiber(tau,[(d,False) for d,_ in dwells],True))[history]@initial
                wrong_shift = max(wrong_shift,float(np.linalg.norm(direct-omitted)))
        initial_energy = float(np.vdot(initial,H0@initial).real)+allowance+width/2
        drift = final_energy-initial_energy
        crude_energy = 2*sum(e['delta']*e['B']*(np.pi/width+s) for e,s in zip(events,cumulative))
        quadratic_energy = 2*sum(e['delta']*e['B']*opnorm(e['pout'])*(np.pi**2/width**2+s*s)
                                 for e,s in zip(events,cumulative))
        # Check products on a fixed grid, including a two-dimensional reference.
        max_instrument_excess = 0.
        max_isometry_residual = 0.
        for tau in [-1.7,-.22,0.,.31,1.1]:
            local = np.vstack([op for op,_ in product_fiber(tau,dwells,True)])
            global_op = np.vstack([op for op,_ in product_fiber(tau,dwells,False)])
            telescope = min(2.,sum(min(2.,e['delta']*e['B']*(tau+s)**2)
                                   for e,s in zip(events,cumulative)))
            max_instrument_excess = max(max_instrument_excess,opnorm(local-global_op)-telescope)
            max_isometry_residual = max(max_isometry_residual,opnorm(local.conj().T@local-eye))
        row = dict(dwells=dwells,schmidt_values=schmidt.tolist(),energy_drift=drift,
                   crude_energy_bound=crude_energy,quadratic_energy_bound=quadratic_energy,
                   energy_coordinate_total_probability=total_probability,
                   max_energy_coordinate_quad_error=largest_quad_error,
                   max_energy_vs_fiber_residual=max_fiber,omitted_shift_error=wrong_shift,
                   max_telescope_bound_excess=max_instrument_excess,
                   max_isometry_residual=max_isometry_residual,
                   local_offset=allowance,local_cap=2*allowance+width,
                   actual_shift_min=min(s for c,_ in branches for s,_ in c),
                   actual_shift_max=max(s for c,_ in branches for s,_ in c))
        rows.append(row)
    check('energy_coordinate_sequential_shared_battery_with_reference_and_dwells',
          all(abs(r['energy_coordinate_total_probability']-1)<1e-9
              and r['max_energy_vs_fiber_residual']<1e-10
              and abs(r['energy_drift']) <= min(r['crude_energy_bound'],r['quadratic_energy_bound'])+1e-9
              and r['max_telescope_bound_excess']<1e-10
              and r['max_isometry_residual']<1e-10 for r in rows)
          and rows[1]['omitted_shift_error']>.01 and rows[2]['omitted_shift_error']>.01,
          cases=rows)

def defect_and_duhamel_check():
    event=events[0]
    h,hin,hout,hp,hpp = (event[k] for k in ['h','before','after','pin','pout'])
    outside=hin-hp
    U,Uo,Up,Uop=map(propagator,[hin,hout,hp,hpp])
    mu=.4
    activity = max(sum(opnorm(a)*len(s)*np.exp(mu*(max(s)-min(s)))
                       for a,s in terms if x in s) for x in range(n))
    lam=2*activity
    A=2*event['delta']*event['B']
    rows=[]
    for tau in [.03,.17,.43,-.43]:
        sign=1 if tau>=0 else -1
        time=abs(tau)
        cp=lambda t: Uop(-t)@Up(t)
        c=Uo(-tau)@U(tau)
        local=cp(tau)
        step=2e-5
        derivative=(cp(tau+step)-cp(tau-step))/(2*step)
        direct_defect=hout@local-local@hin-1j*derivative
        comm=commutator(outside,local)
        identity_error=opnorm(direct_defect-comm)
        def boundary_integrand(s):
            evolved=Uop(sign*s)@h@Uop(-sign*s)
            return sum(opnorm(commutator(a,evolved)) for a,_ in event['cross'])
        first,_=quad(boundary_integrand,0,time,epsabs=1e-11)
        second,_=quad(lambda s:(time-s)*boundary_integrand(s),0,time,epsabs=1e-11)
        a_actual=opnorm(Uo(tau)@h@Uo(-tau)-Uop(tau)@h@Uop(-tau))
        # Integrate exp(lambda*u)-1 numerically before comparing stated closed forms.
        f1_quad,_=quad(lambda s:np.expm1(lam*s),0,time,epsabs=1e-12)
        f2_quad,_=quad(lambda s:(time-s)*np.expm1(lam*s),0,time,epsabs=1e-12)
        f1=np.expm1(lam*time)/lam-time
        f2=np.expm1(lam*time)/lam**2-time/lam-time*time/2
        rows.append(dict(tau=tau,finite_difference_defect_error=identity_error,
                         full_energy_defect=opnorm(comm),cocycle_error=opnorm(c-local),
                         heisenberg_difference=a_actual,first_duhamel_integral=first,
                         second_duhamel_integral=second,F1_integral_residual=abs(f1-f1_quad),
                         F2_integral_residual=abs(f2-f2_quad),LR_energy_bound=A*f1,
                         LR_cocycle_bound=A*f2))
    check('independent_derivative_both_duhamel_integrations_and_LR_constants',
          all(r['finite_difference_defect_error']<3e-9
              and r['full_energy_defect']<=r['first_duhamel_integral']+1e-10
              and r['heisenberg_difference']<=r['first_duhamel_integral']+1e-10
              and r['cocycle_error']<=r['second_duhamel_integral']+1e-10
              and r['cocycle_error']<=r['LR_cocycle_bound']+1e-10
              and r['full_energy_defect']<=r['LR_energy_bound']+1e-10
              and max(r['F1_integral_residual'],r['F2_integral_residual'])<1e-10 for r in rows)
          and rows[-1]['full_energy_defect']>.001,activity=activity,cases=rows)

def fourier_check():
    rows=[]
    for width in [.4,1.,3.7]:
        for tau in [0.,np.pi/width,-np.pi/width,2*np.pi/width,13.4/width]:
            real,_=quad(lambda e:np.cos(tau*e)*packet(e,0.,width),0,width,epsabs=1e-12)
            imag,_=quad(lambda e:np.sin(tau*e)*packet(e,0.,width),0,width,epsabs=1e-12)
            actual=(real+1j*imag)/np.sqrt(2*np.pi)
            rows.append(dict(width=width,tau=tau,error=abs(actual-fourier_amplitude(tau,width))))
    tails=[]
    for dimensionless_cutoff in [2*np.pi,9.,17.]:
        # sinc form and quadrature never divide by the removable rational poles.
        cut=dimensionless_cutoff
        observed,error=quad(lambda t:2*abs(fourier_amplitude(t,1.))**2,cut,1000.,
                            epsabs=1e-11,limit=1500)
        end_bound=128*np.pi/(27*1000.**3)
        bound=128*np.pi/(27*cut**3)
        tails.append(dict(cutoff=cut,quadrature=observed,quad_error=error,
                          plus_remainder=observed+error+end_bound,analytic_bound=bound))
    check('sine_fourier_transform_from_energy_including_removable_poles_and_tail',
          max(r['error'] for r in rows)<1e-11
          and all(r['plus_remainder']<=r['analytic_bound'] for r in tails),
          transform_cases=rows,tail_cases=tails)

def cubic_geometry_check():
    ball=lambda r:(4*r**3+6*r*r+8*r+3)//3
    box=list(itertools.product(range(-4,5),repeat=3))
    l1=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))
    sources=[[(0,0,0)],[(-3,0,0),(2,1,0)],[(4,4,4),(3,4,4),(4,3,4)]]
    supports=[]
    box_set=set(box)
    for x in box:
        supports.append((frozenset([x]),.2))
        for axis in range(3):
            y=tuple(x[j]+(j==axis) for j in range(3))
            z=tuple(x[j]+2*(j==axis) for j in range(3))
            if y in box_set:
                supports += [(frozenset([x,y]),.31),(frozenset([x,y]),.07)]
            if z in box_set:
                supports.append((frozenset([x,y,z]),.13))
    g=max(sum(weight for support,weight in supports if x in support) for x in box)
    rows=[]
    for source in sources:
        distance={x:min(l1(x,y) for y in source) for x in box}
        for radius in [2,3,4]:
            patch={x for x in box if distance[x]<=radius}
            crossing=[(s,w) for s,w in supports if s&patch and not s<=patch]
            shell={x for x in patch if distance[x]>radius-2}
            boundary=sum(w for _,w in crossing)
            shell_upper=len(source)*(ball(radius)-ball(radius-2))
            rows.append(dict(source=source,radius=radius,shell_size=len(shell),
                             shell_upper=shell_upper,crossing_boundary=boundary,
                             boundary_upper=g*shell_upper,
                             every_crossing_touches_shell=all(bool(s&shell) for s,_ in crossing)))
    check('clipped_cubic_shell_with_repeated_supports_and_three_body_terms',
          all(r['every_crossing_touches_shell'] and r['shell_size']<=r['shell_upper']
              and r['crossing_boundary']<=r['boundary_upper']+1e-10 for r in rows),g=g,cases=rows)

def cap_counterexample():
    xx=[embed_one(2,j,X) for j in range(2)]
    zz=[embed_one(2,j,Z) for j in range(2)]
    before=xx[0]+xx[1]+4*zz[0]@zz[1]
    after=before-xx[0]
    qs=[(np.eye(4)+s*zz[0])/2 for s in [-1,1]]
    records=[]
    for a,pa in spectral_projectors(before):
        for b,pb in spectral_projectors(after):
            for q in qs:
                weight=opnorm(pb@q@pa)
                if weight>1e-10:
                    records.append((a-b,weight))
    minimum=min(records)
    check('positive_local_cap_does_not_imply_positive_global_comparator',
          minimum[0]<-1 and minimum[1]>.01,local_sufficient_offset=1.,width=.25,
          global_negative_shift=minimum[0],nonzero_transition_norm=minimum[1],
          global_reachable_support_lower=1+minimum[0])

def native_support_check():
    vertices=list(itertools.product(range(4),repeat=3))
    vertices_set=set(vertices)
    edges=[]
    for vertex in vertices:
        for axis in range(3):
            other=tuple(vertex[j]+(j==axis) for j in range(3))
            if other in vertices_set:
                edges.append((vertex,other))
    centers=[tuple(a+b for a,b in zip(u,v)) for u,v in edges]
    stars={v:{i for i,e in enumerate(edges) if v in e} for v in vertices}
    supports=[stars[u]|stars[v] for u,v in edges]
    sizes=list(map(len,supports))
    diameter=max(sum(abs(a-b) for a,b in zip(centers[i],centers[j]))
                 for s in supports for i in s for j in s)
    radius=max(sum(abs(a-b) for a,b in zip(centers[i],centers[j]))
               for i,s in enumerate(supports) for j in s)
    incidence=max(sum(i in s for s in supports) for i in range(len(edges)))
    # Algebraic bit support: A_e flips exactly the bit e; B_v is diagonal
    # with Z support star(v). Hence anticommutation occurs exactly at endpoints.
    endpoint_residual=all((int(e in stars[v]) == int(v in edges[e]))
                          for e in range(len(edges)) for v in vertices)
    check('native_physical_edge_midpoint_support_enumeration',
          max(sizes)==11 and diameter==4 and radius==2 and incidence==11 and endpoint_residual,
          vertices=len(vertices),edge_qubits=len(edges),max_support=max(sizes),
          max_physical_diameter=diameter,max_midpoint_radius=radius,max_incidence=incidence)

def main():
    before=[hashlib.sha256(p.read_bytes()).hexdigest() for p in SOURCES]
    if before!=BOUND:
        raise RuntimeError('Frozen source hash changed before independent controls')
    defect_and_duhamel_check()
    fourier_check()
    cubic_geometry_check()
    cap_counterexample()
    native_support_check()
    energy_space_check()
    after=[hashlib.sha256(p.read_bytes()).hexdigest() for p in SOURCES]
    check('source_hashes_unchanged',before==after,paths=list(map(str,SOURCES)),sha256=after)
    result=dict(scope='Independent focused check; no audit verdict or grade',
                environment=dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform()),
                checks=CHECKS,pass_count=sum(c['passed'] for c in CHECKS),
                fail_count=sum(not c['passed'] for c in CHECKS))
    (OUT/'independent-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('TOTAL: PASS=%s FAIL=%s'%(result['pass_count'],result['fail_count']))
    return int(result['fail_count']>0)

if __name__=='__main__':
    sys.exit(main())
