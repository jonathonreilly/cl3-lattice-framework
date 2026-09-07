#!/usr/bin/env python3
"""Finite controls for the conditional native Record locality theorem.

No parent runner imports. Battery contractions are independently checked by
direct energy-coordinate integration; the native Pauli spectrum is checked
against a separately constructed fixed-number CAR matrix. Numerical checks do
not replace the note's all-volume proof. Optional mutations change actual
scientific computations, and must produce a nonzero exit.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import os
from pathlib import Path
import time

os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import numpy as np
from scipy.integrate import quad, quad_vec
from scipy.linalg import eigh, expm

I2 = np.eye(2, dtype=complex)
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Y2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z2 = np.diag([1, -1]).astype(complex)
CHECKS: list[dict] = []
DATA: dict = {}
MUTATION = "none"


def check(name, condition, **details):
    ok = bool(condition)
    CHECKS.append(dict(name=name, passed=ok, **details))
    print(f"{'PASS' if ok else 'FAIL'} {name}: {json.dumps(details, sort_keys=True)}")


def norm(a):
    return float(np.linalg.norm(a, 2))


def comm(a, b):
    return a @ b - b @ a


def site(n, at, op):
    a = np.array([[1]], dtype=complex)
    for j in range(n):
        a = np.kron(a, op if j == at else I2)
    return a


def projectors(a):
    vals, vecs = eigh(a)
    groups = []
    for j, val in enumerate(vals):
        if groups and abs(val - groups[-1][0]) < 1e-10:
            groups[-1][1].append(j)
        else:
            groups.append([float(val), [j]])
    return [(v, vecs[:, js] @ vecs[:, js].conj().T) for v, js in groups]


def kernel(s, w):
    x = np.abs(np.asarray(s, dtype=float)) / w
    return np.where(x < 1, (1-x)*np.cos(np.pi*x)+np.sin(np.pi*x)/np.pi, 0.)


def packet(e, offset, w):
    x = (np.asarray(e)-offset)/w
    return np.where((x >= 0) & (x <= 1), math.sqrt(2/w)*np.sin(np.pi*x), 0.)


def fourier_density(tau, w):
    # Dimensionless q=w*tau avoids a removable pole in the raw formula.
    q = w*tau
    if abs(abs(q)-math.pi) < 1e-6:
        value = w/(4*math.pi)
    else:
        value = 4*math.pi*w*math.cos(q/2)**2/(q*q-math.pi**2)**2
    return value * (0.5 if MUTATION == "fourier_half" else 1.)


def tail_bound(w, cutoff):
    if w*cutoff < 2*math.pi:
        raise ValueError("sine tail bound requires w*T >= 2*pi")
    return min(1., 128*math.pi/(27*(w*cutoff)**3))


def battery_components(hin, hout, qs, psi):
    result = []
    for q in qs:
        cols, shifts = [], []
        for a, pa in projectors(hin):
            for b, pb in projectors(hout):
                cols.append(pb @ q @ pa @ psi)
                shifts.append(b-a if MUTATION == "reverse_shift" else a-b)
        result.append((np.column_stack(cols), np.array(shifts)))
    return result


def contract(components, offset, w, labels=None):
    rhos, energy = [], 0.
    for vectors, shifts in components:
        k = kernel(shifts[:, None]-shifts[None, :], w)
        if labels is not None and MUTATION == "reset_shared":
            k = np.ones_like(k)
            for axis in range(labels.shape[1]):
                k *= kernel(labels[:, axis, None]-labels[None, :, axis], w)
        rho = vectors @ k @ vectors.conj().T
        moment = (offset+w/2+(shifts[:, None]+shifts[None, :])/2)*k
        energy += float(np.trace(vectors @ moment @ vectors.conj().T).real)
        rhos.append(rho)
    return rhos, energy


def direct_energy_integral(components, offset, w):
    """Integrate the actual vector sum x_s beta(E-s), without using K_w."""
    rhos, total_energy, maximum_error = [], 0., 0.
    for vectors, shifts in components:
        dim = vectors.shape[0]
        breaks = sorted(set(np.concatenate((offset+shifts, offset+w+shifts))))

        def integrand(e):
            wave = vectors @ packet(e-shifts, offset, w)
            rho = np.outer(wave, wave.conj())
            return np.r_[rho.reshape(-1), e*np.vdot(wave, wave)]

        out, err = quad_vec(integrand, breaks[0], breaks[-1], points=breaks[1:-1],
                            epsabs=3e-11, epsrel=3e-11)
        rhos.append(out[:dim*dim].reshape(dim, dim))
        total_energy += float(out[-1].real)
        maximum_error = max(maximum_error, float(err))
    return rhos, total_energy, maximum_error


def battery_tests():
    # One-variable quadrature checks the Fourier normalization; the omitted
    # tail is independently bounded. Direct packet integration checks overlap.
    u = 200.
    mass, err = quad(lambda q: fourier_density(q, 1.), -u, u,
                     points=[-math.pi, math.pi], epsabs=2e-11, limit=400)
    tail = tail_bound(1., u)
    overlap_error = 0.
    for w, s in [(1., 0.), (1., .2), (1., .999), (1., 1.2), (8., 2.)]:
        val, _ = quad(lambda e: packet(e, 3., w)*packet(e-s, 3., w),
                      min(3., 3.+s), max(3.+w, 3.+w+s),
                      points=sorted(set([3., 3.+s, 3.+w, 3.+w+s])), epsabs=2e-12)
        overlap_error = max(overlap_error, abs(val-kernel(s, w)))
    # Derivative norm fixes the second moment by Parseval, with no fourth
    # moment assumption. Independent energy-domain derivative quadrature.
    derivative_norm, _ = quad(lambda e: 2*math.pi**2*math.cos(math.pi*e)**2, 0., 1.)
    check("sine_packet_and_Fourier_normalization",
          1-tail-err <= mass <= 1+err and overlap_error < 2e-10
          and abs(derivative_norm-math.pi**2) < 1e-10,
          truncated_Fourier_mass=mass, tail_upper=tail, overlap_error=overlap_error,
          derivative_norm=derivative_norm)
    # Tail estimate is checked by separate oscillatory quadrature on a finite
    # interval; the tail beyond its end is bounded, not assigned zero.
    tail_rows = []
    for cutoff in [2*math.pi, 10., 20.]:
        val, err = quad(lambda q: 2*fourier_density(q, 1.), cutoff, 500.,
                        epsabs=2e-11, limit=500)
        bound = tail_bound(1., cutoff)
        upper = val+err+tail_bound(1., 500.)
        tail_rows.append(dict(T=cutoff, quadrature_estimate_minus_error=val-err,
                              quadrature_plus_analytic_remainder=upper, analytic_upper=bound))
    check("integrable_tail_control", all(r["quadrature_plus_analytic_remainder"] < r["analytic_upper"]
          for r in tail_rows), cases=tail_rows)


def local_energy_and_memory():
    n = 3
    xs = [site(n, j, X2) for j in range(n)]
    zs = [site(n, j, Z2) for j in range(n)]
    ident = np.eye(2**n)
    h = xs[0]+xs[1]+xs[2]+zs[0]@zs[1]+zs[1]@zs[2]
    hout = h-xs[0]-xs[1]
    qs = [(ident+s*zs[0])@(ident+t*zs[1])/4 for s, t in itertools.product([-1, 1], repeat=2)]
    psi = np.zeros(2**n, complex); psi[0] = 1
    labels = np.array(list(itertools.product([-1., 1.], repeat=2)))
    ps = [(ident+a*xs[0])@(ident+b*xs[1])/4 for a, b in labels]
    local = [(np.column_stack([q@p@psi for p in ps]), labels.sum(axis=1)) for q in qs]
    global_components = battery_components(h, hout, qs, psi)
    cases = []
    max_rho_error = max_eb_error = max_global_drift = 0.
    for w in [1., 8., 32.]:
        offset = 16.
        gr, ge = contract(global_components, offset, w)
        lr, le = contract(local, offset, w, labels=labels)
        for label, comp, rr, eb in [("global", global_components, gr, ge), ("local", local, lr, le)]:
            qr, qe, qerr = direct_energy_integral(comp, offset, w)
            max_rho_error = max(max_rho_error, max(norm(a-b) for a,b in zip(rr, qr)))
            max_eb_error = max(max_eb_error, abs(eb-qe))
            check(f"joint_energy_integral_{label}_w{w:g}",
                  max(norm(a-b) for a,b in zip(rr, qr)) < 2e-9 and abs(eb-qe) < 2e-8,
                  density_error=max(norm(a-b) for a,b in zip(rr, qr)),
                  battery_energy_error=abs(eb-qe), quadrature_estimated_error=qerr)
        initial = float(np.vdot(psi, h@psi).real)+offset+w/2
        global_drift = ge+sum(float(np.trace(hout@rho).real) for rho in gr)-initial
        local_drift = le+sum(float(np.trace(hout@rho).real) for rho in lr)-initial
        max_global_drift = max(max_global_drift, abs(global_drift))
        # Exactly evaluated classical-history trace norm, upper-bounded by
        # the proved channel norm; no optimization over favorable observables.
        trace_distance = sum(float(np.abs(eigh(a-b, eigvals_only=True)).sum()) for a,b in zip(gr,lr))
        channel_bound = min(2., 6*math.pi**2/w**2)  # delta*B=1+2
        energy_bound = 6*math.pi/w
        cases.append(dict(w=w, channel_trace_norm=trace_distance,
                          channel_upper=channel_bound, local_energy_drift=local_drift,
                          energy_upper=energy_bound, global_energy_drift=global_drift))
    check("global_energy_and_nonvacuous_local_bounds",
          max_global_drift < 2e-8 and all(r["channel_trace_norm"] <= r["channel_upper"]+2e-8
          and abs(r["local_energy_drift"]) <= r["energy_upper"]+2e-8 for r in cases)
          and cases[-1]["channel_upper"] < .06,
          cases=cases)
    lr, _ = contract(local, 16., 1., labels=labels)
    shared_probs = np.array([np.trace(r).real for r in lr])
    expected_shared = np.array([3/8, 1/8, 1/8, 3/8])
    reset_probs = np.full(4, 1/4)
    tv = float(np.abs(shared_probs-reset_probs).sum()/2)
    check("retained_battery_is_not_reset_batteries",
          np.max(np.abs(shared_probs-expected_shared)) < 1e-12 and abs(tv-.25) < 1e-12,
          shared_probabilities=shared_probs.tolist(), reset_probabilities=reset_probs.tolist(), TV=tv)
    # The cap follows from actual support, not the mean. Local two-event
    # shifts are in [-2,2]; the chosen offset is conservative for both models.
    shift_min = min(float(s.min()) for _,s in global_components+local)
    shift_max = max(float(s.max()) for _,s in global_components+local)
    check("spectral_support_cap", 16.+shift_min > 0 and 16.+32.+shift_max < 64.,
          all_fixture_shift_min=shift_min, all_fixture_shift_max=shift_max,
          common_initial_offset=16., tested_cap=64.)
    DATA["three_qubit_joint_battery"] = cases


def native_bksf():
    edges = [(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)]
    ne = len(edges); dim = 2**ne; ident = np.eye(dim, dtype=complex)
    zz = [site(ne, j, Z2) for j in range(ne)]
    xx = [site(ne, j, X2) for j in range(ne)]
    edge_id = {e:j for j,e in enumerate(edges)}
    neighbors = {v:sorted(w if u==v else u for u,w in edges if v in (u,w)) for v in range(6)}
    bs = []
    for v in range(6):
        b = ident.copy()
        for j,e in enumerate(edges):
            if v in e: b = b@zz[j]
        bs.append(b)

    def aa(i,j):
        e = edge_id[tuple(sorted((i,j)))]; a = xx[e].copy()
        for v,other in [(i,j),(j,i)]:
            for k in neighbors[v]:
                if k < other:
                    a = a@zz[edge_id[tuple(sorted((v,k)))]]
        return a if i < j else -a

    hops = [.5j*aa(i,j)@(bs[i]-bs[j]) for i,j in edges]
    number = sum((ident-b)/2 for b in bs)
    cycles = []
    for vs in [(0,1,4,3,0),(1,2,5,4,1)]:
        s = ident.copy()
        for i,j in zip(vs,vs[1:]): s = s@aa(i,j)
        cycles.append(s)  # i**4 = +1 for these two squares
    p = (ident+cycles[0])@(ident+cycles[1])/4
    pn = np.diag(np.isclose(np.diag(number), 2.).astype(float))
    pp = p@pn
    vals, vv = eigh(pp); basis = vv[:, vals>.5]
    h = sum(hops)
    native_spectrum = eigh(basis.conj().T@h@basis, eigvals_only=True)
    # Separate occupation-sign CAR construction; no Pauli dictionary imported.
    masks = [sum(1<<j for j in comb) for comb in itertools.combinations(range(6),2)]
    index = {m:j for j,m in enumerate(masks)}; car = np.zeros((15,15),complex)
    for col,m in enumerate(masks):
        for i,j in edges:
            for dest,src in [(i,j),(j,i)]:
                if (m>>src)&1 and not (m>>dest)&1:
                    sign = (-1)**((m&((1<<src)-1)).bit_count())
                    after = m^(1<<src)
                    sign *= (-1)**((after&((1<<dest)-1)).bit_count())
                    car[index[after^(1<<dest)], col] += sign
    spectrum_error = float(np.max(np.abs(native_spectrum-eigh(car,eigvals_only=True))))
    native_residual = max([norm(p@p-p), norm(comm(cycles[0],cycles[1]))] +
                          [norm(comm(number,a)) for a in hops] +
                          [norm(a-a.conj().T) for a in hops])
    check("native_Pauli_and_independent_CAR_dictionary",
          basis.shape[1]==15 and abs(np.trace(p).real-32)<1e-10
          and native_residual < 1e-10 and spectrum_error < 1e-10,
          code_dimension=float(np.trace(p).real), N2_dimension=basis.shape[1],
          algebra_residual=native_residual, spectrum_error=spectrum_error)
    psi = basis@np.exp(1j*.37*np.arange(15)); psi /= np.linalg.norm(psi)
    positions = {v:(v%3,v//3,0) for v in range(6)}
    centers = [tuple(positions[i][a]+positions[j][a] for a in range(3)) for i,j in edges]
    supports = []
    for i,j in edges:
        supports.append({k for k,f in enumerate(edges) if i in f or j in f})
    x = supports[0]; delta = norm(hops[0]); rows = []
    max_identity = max_locality = max_preservation = 0.
    for radius in [0,2,4]:
        patch = {j for j in range(ne) if min(sum(abs(a-b) for a,b in zip(centers[j],centers[k])) for k in x)<=radius}
        inside = [j for j,s in enumerate(supports) if s <= patch]
        crossing = [j for j,s in enumerate(supports) if s&patch and not s <= patch]
        hp = sum((hops[j] for j in inside), np.zeros_like(h))
        exterior = h-hp; hpo = hp-hops[0]; boundary = sum(norm(hops[j]) for j in crossing)
        for tau in [.05,.3]:
            c = expm(-1j*tau*(h-hops[0]))@expm(1j*tau*h)
            cr = expm(-1j*tau*hpo)@expm(1j*tau*hp)
            derivative = -1j*hpo@cr+1j*cr@hp
            defect = (h-hops[0])@cr-cr@h-1j*derivative
            expected = np.zeros_like(defect) if MUTATION == "drop_boundary" else comm(exterior,cr)
            max_identity = max(max_identity, norm(defect-expected))
            max_locality = max(max_locality, norm(c-cr)-delta*boundary*tau*tau)
            prob = []
            for sign in [-1,1]:
                q = (ident+sign*zz[0])/2; out=q@cr@psi
                prob.append(float(np.vdot(out,out).real))
                max_preservation=max(max_preservation,norm((number-2*ident)@out[:,None]),
                                     norm((zz[0]-sign*ident)@out[:,None]),
                                     norm((cycles[1]-ident)@out[:,None]))
            max_preservation=max(max_preservation,max(abs(v-.5) for v in prob))
            rows.append(dict(radius=radius,tau=tau,patch_edges=len(patch),inside_terms=len(inside),
                             crossing_norm_sum=boundary,cocycle_error=norm(c-cr),energy_defect=norm(defect)))
    check("native_localization_and_boundary_work", max_identity<1e-10 and max_locality<1e-10
          and any(r["energy_defect"]>.01 for r in rows),
          defect_identity_residual=max_identity, worst_crude_bound_excess=max_locality, cases=rows)
    check("native_nonbridge_number_and_Record_preservation", max_preservation<1e-10,
          maximum_residual=max_preservation)
    # A fixed branch deletes two nonbridges, then the remaining edge incident
    # to vertex 1 is a bridge. Its parity includes both old Record signs.
    state=psi.copy(); signs=[-1,1]; old=[]
    for e,sign in zip([0,1], signs):
        state=(ident+sign*zz[e])@state/2; state/=np.linalg.norm(state);old.append((e,sign))
    bridge=5; boundary_sign=signs[0]*signs[1]
    parity_residual=norm((zz[bridge]-boundary_sign*bs[1])@state[:,None])
    probs=[]
    for sign in [-1,1]:
        out=(ident+sign*zz[bridge])@state/2;probs.append(float(np.vdot(out,out).real))
        for e,s in old: parity_residual=max(parity_residual,norm((zz[e]-s*ident)@out[:,None]))
    check("bridge_old_sign_parity_control", parity_residual<1e-10 and abs(sum(probs)-1)<1e-10,
          residual=parity_residual, actual_bridge_probabilities=probs)
    DATA["native_ladder"] = rows


def analytic_constants():
    def ball(r): return (4*r**3+6*r**2+8*r+3)//3
    enumerated = [sum(abs(x)+abs(y)+abs(z)<=r for x,y,z in itertools.product(range(-r,r+1),repeat=3))
                  for r in range(7)]
    check("cubic_boundary_count", enumerated==[ball(r) for r in range(7)], volumes=enumerated)
    # A deliberately loose all-cubic native bound, fixed before actual matrix
    # calculations. Finite resources; no claim that this radius is practical.
    mu=.25; delta=1.; support=11; g=11.; kappa=121*math.exp(4*mu); lam=2*kappa
    r=256; interaction_range=4; w=10**6
    b=g*support*(ball(r)-ball(r-interaction_range))
    cutoff=mu*(r-interaction_range)/(2*lam)
    prefactor=2*delta*support*b*math.exp(-mu*(r-interaction_range))
    short_energy=prefactor*(math.expm1(lam*cutoff)/lam-cutoff)
    short_channel=prefactor*(math.expm1(lam*cutoff)/lam**2-cutoff/lam-cutoff**2/2)
    tail=tail_bound(w,cutoff)
    joint_bound=2*math.sqrt(short_channel**2+4*tail)
    energy_bound=short_energy+2*b*tail
    check("nonvacuous_volume_uniform_resource_prescription", joint_bound<.01 and energy_bound<.01,
          r=r,w=w,kappa=kappa,T=cutoff,B_boundary_upper=b,
          joint_channel_upper=joint_bound,energy_drift_upper=energy_bound,
          note="loose analytical prescription; not an optimized apparatus or a simulated giant patch")


def finite_lr_and_free_dwell():
    n=5; ident=np.eye(2**n, dtype=complex)
    xs=[site(n,j,X2) for j in range(n)];zs=[site(n,j,Z2) for j in range(n)]
    terms=[(x,{j}) for j,x in enumerate(xs)]+[(zs[j]@zs[j+1],{j,j+1}) for j in range(n-1)]
    h=sum(a for a,_ in terms); deleted=xs[0]; mu=1.;kappa=1+4*math.e;lam=2*kappa
    rows=[]
    for r in [1,2,3]:
        patch=set(range(r+1));hp=sum(a for a,s in terms if s<=patch)
        cross=sum(norm(a) for a,s in terms if s&patch and not s<=patch)
        pref=2*cross*math.exp(-mu*(r-1))
        for tau in [.02,.1]:
            c=expm(-1j*tau*(h-deleted))@expm(1j*tau*h)
            cr=expm(-1j*tau*(hp-deleted))@expm(1j*tau*hp)
            error=norm(c-cr);drift=norm(comm(h-hp,cr))
            eps=pref*(math.expm1(lam*tau)/lam**2-tau/lam-tau*tau/2)
            b=pref*(math.expm1(lam*tau)/lam-tau)
            rows.append(dict(r=r,tau=tau,cocycle_error=error,LR_upper=eps,
                             energy_defect=drift,energy_upper=b))
    check("explicit_LR_double_integration_constants",all(a["cocycle_error"]<=a["LR_upper"]+1e-12
          and a["energy_defect"]<=a["energy_upper"]+1e-12 for a in rows),cases=rows)
    # Independent collapse of the two global fibers through free dwells.
    h0=xs[0]+xs[1]+zs[0]@zs[1];h1=h0-xs[0];h2=h1-xs[1]
    d1=.13;d2=.17;u=.21;maximum=0.;wrong=0.
    for s,t in itertools.product([-1,1],repeat=2):
        q1=(ident+s*zs[0])/2;q2=(ident+t*zs[1])/2
        def fiber(tau,ha,hb,q): return expm(-1j*tau*hb)@q@expm(1j*tau*ha)
        actual=fiber(u+d1+d2,h1,h2,q2)@expm(-1j*d2*h1)@fiber(u+d1,h0,h1,q1)@expm(-1j*d1*h0)
        collapsed=expm(-1j*(u+d1+d2)*h2)@q2@q1@expm(1j*u*h0)
        omitted=fiber(u,h1,h2,q2)@expm(-1j*d2*h1)@fiber(u,h0,h1,q1)@expm(-1j*d1*h0)
        maximum=max(maximum,norm(actual-collapsed));wrong=max(wrong,norm(omitted-collapsed))
    check("laboratory_free_dwell_translation",maximum<1e-11 and wrong>.01,
          correct_collapse_residual=maximum,omitted_Fourier_shift_error=wrong)


def asymmetric_time_control():
    """Independent review fixture: positive/negative Heisenberg norms differ."""
    n=3; ident=np.eye(2**n, dtype=complex)
    xs=[site(n,j,X2) for j in range(n)]
    zs=[site(n,j,Z2) for j in range(n)]
    y1=site(n,1,Y2)
    deleted=xs[0]
    remaining_terms=[-zs[0]@xs[1],2*y1,-zs[0]@zs[1],3*zs[1]@xs[2]]
    patch_remaining=sum(remaining_terms[:3]); exterior=remaining_terms[3]
    remaining=patch_remaining+exterior; h=remaining+deleted
    hp=patch_remaining+deleted; tau=.4
    c=expm(-1j*tau*remaining)@expm(1j*tau*h)
    cp=expm(-1j*tau*patch_remaining)@expm(1j*tau*hp)
    def difference(u,sign):
        full=expm(1j*sign*u*remaining)
        patch=expm(1j*sign*u*patch_remaining)
        return norm(full@deleted@full.conj().T-patch@deleted@patch.conj().T)
    forward,forward_err=quad(lambda u:difference(u,1),0,tau,epsabs=1e-11)
    symmetric,symmetric_err=quad(lambda u:difference(u,1),
                                 0,tau,epsabs=1e-11)
    record=(ident+zs[0])/2
    hypotheses=max([norm(comm(record,a)) for a in remaining_terms]
                   +[norm(comm(exterior,deleted))])
    error=norm(c-cp)
    check("both_Heisenberg_time_directions_required",
          hypotheses<1e-12 and error>forward+forward_err+1e-3
          and error<=symmetric+symmetric_err+1e-10,
          premise_residual=hypotheses,cocycle_error=error,
          invalid_positive_time_integral=forward,correct_symmetric_integral=symmetric)


def main():
    global MUTATION
    ap=argparse.ArgumentParser()
    ap.add_argument("--mutation",choices=["none","drop_boundary","reverse_shift","reset_shared","fourier_half"],default="none")
    ap.add_argument("--json-output",type=Path)
    args=ap.parse_args();MUTATION=args.mutation;start=time.monotonic()
    battery_tests();local_energy_and_memory();native_bksf();finite_lr_and_free_dwell();analytic_constants();asymmetric_time_control()
    failed=sum(not r["passed"] for r in CHECKS)
    result=dict(scope="conditional finite controls; no audit verdict",mutation=MUTATION,
                checks=CHECKS,data=DATA,elapsed_seconds=time.monotonic()-start,
                pass_count=len(CHECKS)-failed,fail_count=failed)
    if args.json_output:
        args.json_output.write_text(json.dumps(result,indent=2)+"\n")
    print(f"TOTAL: PASS={len(CHECKS)-failed} FAIL={failed}")
    return int(failed>0)


if __name__ == "__main__":
    raise SystemExit(main())
