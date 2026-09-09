#!/usr/bin/env python3
"""Partial coordinate-class deletion: finite spectrum and packet propagation.

Conditional calculation for the supplied free one-particle Hamiltonian
    h(k) = -2 sum_mu cos(k_mu) gamma_mu.
Deleting an even coordinate class means geometrically deleting that row and
column.  This runner does not show that the edge-qubit record instrument realizes
this physical matter process, select a clock/rate, or establish infinite-volume
vacuum stability.  It contains no Fock-space construction.
"""
from __future__ import annotations

import itertools
import math
import resource
import time

import numpy as np
import scipy.linalg as la

# Import makes the separate checker reachable in the restricted audit packet.
# Its standalone main is guarded, and none of its algorithms is used below.
import record_formation_partial_class_dispersion_independent_check_2026_09_04 as packet_checker

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    "scripts/record_formation_partial_class_dispersion_independent_check_2026_09_04.py",
)


T0 = time.monotonic()
PASS = 0
FAIL = 0
TOL = 2e-11


def check(label, condition):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    print(("PASS " if ok else "FAIL ") + label)


def bound_report(value, tolerance):
    return f"<{tolerance:.1e}" if value < tolerance else f"={value:.3e}"


I2 = np.eye(2, dtype=np.int64)
X = np.array([[0, 1], [1, 0]], dtype=np.int64)
Z = np.array([[1, 0], [0, -1]], dtype=np.int64)
GAMMA = (
    np.kron(np.kron(X, I2), I2),
    np.kron(np.kron(Z, X), I2),
    np.kron(np.kron(Z, Z), X),
)
COORDS = tuple(itertools.product((0, 1), repeat=3))
EVEN = (0, 3, 5, 6)
ODD = (1, 2, 4, 7)
BITS = (4, 2, 1)


def exact_algebra():
    eye8 = np.eye(8, dtype=np.int64)
    clifford_residual = 0
    for mu, nu in itertools.product(range(3), repeat=2):
        anti = GAMMA[mu] @ GAMMA[nu] + GAMMA[nu] @ GAMMA[mu]
        target = 2 * eye8 if mu == nu else np.zeros((8, 8), dtype=np.int64)
        clifford_residual = max(clifford_residual, int(np.max(np.abs(anti - target))))

    row_blocks = [g[np.ix_(EVEN, ODD)] for g in GAMMA]
    row_residual = 0
    eye4 = np.eye(4, dtype=np.int64)
    for mu, nu in itertools.product(range(3), repeat=2):
        coeff = row_blocks[mu] @ row_blocks[nu].T + row_blocks[nu] @ row_blocks[mu].T
        target = 2 * eye4 if mu == nu else np.zeros((4, 4), dtype=np.int64)
        row_residual = max(row_residual, int(np.max(np.abs(coeff - target))))

    mutated = [g.copy() for g in GAMMA]
    a, b = 0, 1  # one undirected gamma_3 edge
    mutated[2][a, b] *= -1
    mutated[2][b, a] *= -1
    weights = (2, 3, 5)
    gm = sum(w * g for w, g in zip(weights, mutated))
    mutation_residual = int(np.max(np.abs(gm @ gm - sum(w * w for w in weights) * eye8)))
    return clifford_residual, row_residual, mutation_residual


def canonical_cos(k):
    c = np.cos(np.asarray(k, dtype=float))
    c[np.abs(c) < 1e-14] = 0.0
    return c


def bloch_h(k):
    c = canonical_cos(k)
    h = sum((-2.0 * c[mu]) * GAMMA[mu] for mu in range(3))
    epsilon = 2.0 * float(np.linalg.norm(c))
    return h, epsilon


def reduced_h(k, removed):
    h, epsilon = bloch_h(k)
    keep_even = tuple(a for a in EVEN if a not in removed)
    order = keep_even + ODD
    return h[np.ix_(order, order)], epsilon, keep_even


def predicted_spectrum(epsilon, r):
    if epsilon == 0.0:
        return np.zeros(8 - r)
    return np.array([-epsilon] * (4 - r) + [0.0] * r + [epsilon] * (4 - r))


def spectral_checks():
    momenta = (
        ("generic-a", (0.17, -0.31, 0.44)),
        ("generic-b", (math.pi / 4, -math.pi / 6, math.pi / 8)),
        ("plane-x", (-math.pi / 2, 0.23, -0.41)),
        ("plane-xy", (-math.pi / 2, -math.pi / 2, 0.37)),
        ("node", (-math.pi / 2, -math.pi / 2, -math.pi / 2)),
    )
    max_spec = 0.0
    max_poly = 0.0
    max_prop = 0.0
    zero_count_ok = True
    cases = 0
    for r in range(5):
        for removed in itertools.combinations(EVEN, r):
            for _, k in momenta:
                hr, epsilon, _ = reduced_h(k, removed)
                ev = np.linalg.eigvalsh(hr)
                target = predicted_spectrum(epsilon, r)
                max_spec = max(max_spec, float(np.max(np.abs(ev - target), initial=0.0)))
                max_poly = max(max_poly, float(np.max(np.abs(hr @ hr @ hr - epsilon**2 * hr), initial=0.0)))
                actual_zero = int(np.count_nonzero(np.abs(ev) < 1e-9))
                correct_zero = (8 - r) if epsilon == 0.0 else r
                zero_count_ok &= actual_zero == correct_zero
                t = 0.73
                if epsilon == 0.0:
                    closed = np.eye(len(hr), dtype=complex)
                else:
                    closed = (np.eye(len(hr))
                              + (math.cos(epsilon * t) - 1.0) * (hr @ hr) / epsilon**2
                              - 1j * math.sin(epsilon * t) * hr / epsilon)
                max_prop = max(max_prop, float(np.max(np.abs(la.expm(-1j * t * hr) - closed), initial=0.0)))
                cases += 1
    return cases, max_spec, max_poly, max_prop, zero_count_ok


def staggered_sign(a, mu):
    x, y, _ = COORDS[a]
    if mu == 0:
        return 1
    if mu == 1:
        return -1 if x else 1
    return -1 if (x + y) & 1 else 1


def realspace_h(physical_length, removed):
    """Direct nearest-neighbor torus, allocated independently of Bloch blocks."""
    nc = physical_length // 2
    kept = tuple(a for a in range(8) if a not in removed)
    sites = tuple(itertools.product(range(nc), range(nc), range(nc), kept))
    loc = {site: j for j, site in enumerate(sites)}
    h = np.zeros((len(sites), len(sites)), dtype=float)
    for nx, ny, nz in itertools.product(range(nc), repeat=3):
        n = (nx, ny, nz)
        for a in range(8):
            if a not in kept:
                continue
            for mu, bit in enumerate(BITS):
                if a & bit:
                    continue
                b = a ^ bit
                if b not in kept:
                    continue
                amp = -float(staggered_sign(a, mu))
                i = loc[n + (a,)]
                same = loc[n + (b,)]
                prev_n = list(n)
                prev_n[mu] = (prev_n[mu] - 1) % nc
                prev = loc[tuple(prev_n) + (b,)]
                h[i, same] += amp
                h[same, i] += amp
                h[i, prev] += amp
                h[prev, i] += amp
    return h


def torus_momenta(nc):
    return math.pi * np.fft.fftfreq(nc)


def realspace_checks():
    by_length = []
    global_herm = 0.0
    global_spec = 0.0
    max_dimension = 0
    node_blocks = 0
    for physical_length in (4, 6, 8):
        nc = physical_length // 2
        kvals = torus_momenta(nc)
        length_spec = 0.0
        for r in range(5):
            for removed in itertools.combinations(EVEN, r):
                direct = realspace_h(physical_length, removed)
                max_dimension = max(max_dimension, len(direct))
                global_herm = max(global_herm, float(np.max(np.abs(direct - direct.T), initial=0.0)))
                direct_ev = np.linalg.eigvalsh(direct)
                blocks = []
                for k in itertools.product(kvals, repeat=3):
                    hr, epsilon, _ = reduced_h(k, removed)
                    blocks.append(np.linalg.eigvalsh(hr))
                    if epsilon == 0.0:
                        node_blocks += 1
                        if np.count_nonzero(np.abs(blocks[-1]) < 1e-9) != len(hr):
                            length_spec = math.inf
                bloch_ev = np.sort(np.concatenate(blocks))
                err = float(np.max(np.abs(direct_ev - bloch_ev), initial=0.0))
                length_spec = max(length_spec, err)
        global_spec = max(global_spec, length_spec)
        by_length.append((physical_length, length_spec))
    return by_length, global_herm, global_spec, max_dimension, node_blocks


def periodic_delta(k, center):
    return (k - center + math.pi / 2) % math.pi - math.pi / 2


def packet_basis(k, removed):
    hr, epsilon, keep_even = reduced_h(k, removed)
    ne = len(keep_even)
    xi = np.zeros(ne + 4, dtype=complex)
    if epsilon == 0.0:
        xi[0] = 1.0
        zero_part = 1.0
    else:
        u = np.zeros(ne)
        u[0] = 1.0
        q = hr[:ne, ne:]
        xi[:ne] = u / math.sqrt(2.0)
        xi[ne:] = (q.T @ u) / (epsilon * math.sqrt(2.0))
        pzero_xi = xi - (hr @ hr @ xi) / epsilon**2
        zero_part = float(np.vdot(pzero_xi, pzero_xi).real)
    residual = float(np.linalg.norm(hr @ xi - epsilon * xi)) if epsilon else 0.0
    return xi, keep_even + ODD, epsilon, zero_part, residual


def fmt_vec(v):
    return "(" + ",".join(f"{x:+.4f}" for x in v) + ")"


def packet_case(nc, r, sigma=0.20):
    removed = EVEN[:r]
    n0 = nc // 2
    kvals = torus_momenta(nc)
    mesh = np.meshgrid(kvals, kvals, kvals, indexing="ij")
    ks = np.stack([x.ravel() for x in mesh], axis=1)
    k0 = np.full(3, math.pi / 4)
    dk = periodic_delta(ks, k0)
    envelope = np.exp(-np.sum(dk * dk, axis=1) / (4.0 * sigma**2))
    # A source on the chosen even site contributes its internal-position phase.
    # This makes the cell-gauge polarization periodic across the reduced zone.
    source_class = tuple(a for a in EVEN if a not in removed)[0]
    center_phase = np.exp(-1j * (2 * n0 * np.sum(ks, axis=1)
                                + ks @ np.asarray(COORDS[source_class])))
    # Define a positive-band packet only on nonzero-energy fibers. At the node
    # that band label is degenerate, so its supplied envelope is zero there.
    node = np.linalg.norm(np.cos(ks), axis=1) < 1e-14
    envelope[node] = 0.0
    amplitudes = envelope * center_phase
    amplitudes /= np.linalg.norm(amplitudes)
    weights = np.abs(amplitudes) ** 2

    order = tuple(a for a in EVEN if a not in removed) + ODD
    fourier = {a: np.zeros(nc**3, dtype=complex) for a in order}
    energies = np.zeros(nc**3)
    zero_weight = 0.0
    max_eigen_residual = 0.0
    velocity = np.zeros(3)
    for j, k in enumerate(ks):
        xi, xi_order, epsilon, zero_part, residual = packet_basis(k, removed)
        assert xi_order == order
        energies[j] = epsilon
        zero_weight += weights[j] * zero_part
        max_eigen_residual = max(max_eigen_residual, residual)
        if epsilon:
            velocity += weights[j] * (-4.0 * np.sin(k) * np.cos(k) / epsilon)
        physical_phase = np.exp(1j * (k @ np.asarray([COORDS[a] for a in order]).T))
        for p, a in enumerate(order):
            fourier[a][j] = amplitudes[j] * xi[p] * physical_phase[p]

    reference = 2 * n0 + np.asarray(COORDS[source_class])
    axes = []
    for a in order:
        component_axes = []
        for mu in range(3):
            raw = 2 * np.arange(nc) + COORDS[a][mu] - reference[mu]
            component_axes.append((raw + nc) % (2 * nc) - nc)
        axes.append(component_axes)

    means = []
    norms = []
    tails = []
    for t in (0.0, 1.0, 2.0):
        dynamical = np.exp(-1j * energies * t)
        mean = np.zeros(3)
        norm = 0.0
        tail = 0.0
        for p, a in enumerate(order):
            fk = (fourier[a] * dynamical).reshape((nc, nc, nc))
            psi = np.fft.ifftn(fk) * math.sqrt(nc**3)
            probability = np.abs(psi) ** 2
            norm += float(probability.sum())
            dx, dy, dz = axes[p]
            mean[0] += float(np.sum(probability * dx[:, None, None]))
            mean[1] += float(np.sum(probability * dy[None, :, None]))
            mean[2] += float(np.sum(probability * dz[None, None, :]))
            near_wrap = ((np.abs(dx)[:, None, None] > nc - 2)
                         | (np.abs(dy)[None, :, None] > nc - 2)
                         | (np.abs(dz)[None, None, :] > nc - 2))
            tail += float(probability[near_wrap].sum())
        means.append(mean / norm)
        norms.append(norm)
        tails.append(tail / norm)
    displacements = [means[t] - means[0] for t in range(3)]
    errors = [float(np.linalg.norm(displacements[t] - t * velocity)) for t in range(3)]
    return {
        "removed": removed,
        "polarization": tuple(a for a in EVEN if a not in removed)[0],
        "norms": norms,
        "norm_error": max(abs(x - 1.0) for x in norms),
        "zero_weight": zero_weight,
        "velocity": velocity,
        "displacements": displacements,
        "errors": errors,
        "tails": tails,
        "eigen_residual": max_eigen_residual,
    }


def packet_checks():
    out = []
    max_norm_error = 0.0
    max_eigen_residual = 0.0
    for nc in (8, 12, 16):
        for r in range(4):
            result = packet_case(nc, r)
            max_norm_error = max(max_norm_error, *(abs(x - 1.0) for x in result["norms"]))
            max_eigen_residual = max(max_eigen_residual, result["eigen_residual"])
            out.append((nc, r, result))
    return out, max_norm_error, max_eigen_residual


def bipartite_sea(h_ordered):
    m = len(h_ordered) // 2
    q = h_ordered[:m, m:]
    evals, vecs = np.linalg.eigh(q @ q.T.conj())
    k = (vecs * np.sqrt(evals)) @ vecs.T.conj()
    kinv = (vecs * (1.0 / np.sqrt(evals))) @ vecs.T.conj()
    u = kinv @ q
    f = np.vstack([np.eye(m), -u.T.conj()]) / math.sqrt(2.0)
    return k, u, f, float(evals.min())


def conditioned_slater(f, measured, outcomes):
    """Condition independently via occupied-row nullspace, formed modes, and restriction."""
    dim, particles = f.shape
    ones = [i for i, n in zip(measured, outcomes) if n]
    empty = [i for i, n in zip(measured, outcomes) if not n]
    null = (la.null_space(f[ones, :]) if ones else np.eye(particles))
    rest = f @ null
    rest[empty, :] = 0.0
    if rest.shape[1]:
        left, singular, _ = np.linalg.svd(rest, full_matrices=False)
        rank = int(np.count_nonzero(singular > 1e-10))
        rest_basis = left[:, :rank]
    else:
        rest_basis = np.zeros((dim, 0))
    formed = np.eye(dim)[:, ones]
    w = np.column_stack([formed, rest_basis])
    return w @ w.T.conj(), float(np.max(np.abs(w.T.conj() @ w - np.eye(w.shape[1])), initial=0.0))


def factorization_case(h, u, f, measured, outcomes):
    m = len(h) // 2
    measured = tuple(measured)
    outcomes = tuple(outcomes)
    remaining_even = tuple(i for i in range(m) if i not in measured)
    keep = remaining_even + tuple(range(m, 2 * m))
    empty = tuple(i for i, n in zip(measured, outcomes) if not n)

    c_full, ortherr = conditioned_slater(f, measured, outcomes)
    c_independent = c_full[np.ix_(keep, keep)]
    f_t = f[np.ix_(keep, remaining_even)]
    z_full = np.vstack([np.zeros((m, m)), u.T.conj()])
    z_empty = z_full[np.ix_(keep, empty)]
    c_formula = f_t @ f_t.T.conj() + z_empty @ z_empty.T.conj()
    hr = h[np.ix_(keep, keep)]

    ev, vv = np.linalg.eigh(hr)
    neg = vv[:, ev < -1e-9]
    pneg = neg @ neg.T.conj()
    match = float(np.max(np.abs(c_independent - c_formula), initial=0.0))
    comm = float(np.max(np.abs(c_formula @ hr - hr @ c_formula), initial=0.0))
    complete = float(np.max(np.abs(f_t @ f_t.T.conj() - pneg), initial=0.0))
    zeroann = float(np.max(np.abs(hr @ z_empty), initial=0.0))
    idem = float(np.max(np.abs(c_formula @ c_formula - c_formula), initial=0.0))
    traceerr = abs(float(np.trace(c_formula).real) - (m - sum(outcomes)))
    return np.array([match, comm, complete, zeroann, idem, traceerr, ortherr])


def state_factorization_checks():
    # Open 2x2x2 cube: every deletion subset and every occupation outcome.
    open_full = -sum(GAMMA).astype(float)
    open_order = EVEN + ODD
    open_h = open_full[np.ix_(open_order, open_order)]
    _, open_u, open_f, open_gap2 = bipartite_sea(open_h)
    open_metrics = np.zeros(7)
    open_cases = 0
    for r in range(5):
        for measured in itertools.combinations(range(4), r):
            for outcomes in itertools.product((0, 1), repeat=r):
                open_metrics = np.maximum(open_metrics, factorization_case(
                    open_h, open_u, open_f, measured, outcomes))
                open_cases += 1

    # Non-flat L=6 torus: one whole coordinate class, three declared patterns.
    l6 = realspace_h(6, ())
    sites = tuple(itertools.product(range(3), range(3), range(3), range(8)))
    e_global = tuple(j for j, site in enumerate(sites) if site[-1] in EVEN)
    o_global = tuple(j for j, site in enumerate(sites) if site[-1] in ODD)
    h6 = l6[np.ix_(e_global + o_global, e_global + o_global)]
    k6, u6, f6, gap2_6 = bipartite_sea(h6)
    measured6 = tuple(i for i, j in enumerate(e_global) if sites[j][-1] == EVEN[0])
    cell_parity = tuple((sum(sites[e_global[i]][:3]) & 1) for i in measured6)
    patterns = ((0,) * len(measured6), (1,) * len(measured6), cell_parity)
    l6_metrics = np.max(np.stack([
        factorization_case(h6, u6, f6, measured6, pattern) for pattern in patterns
    ]), axis=0)
    selector = np.zeros(len(k6))
    selector[list(measured6)] = 1.0
    commute = float(np.max(np.abs(k6 * selector[None, :] - selector[:, None] * k6), initial=0.0))
    singleton = np.zeros(len(k6))
    singleton[measured6[0]] = 1.0
    singleton_commute = float(np.max(np.abs(k6 * singleton[None, :]
                                           - singleton[:, None] * k6), initial=0.0))
    nonflat = float(np.ptp(np.linalg.eigvalsh(k6)))
    return open_cases, open_metrics, open_gap2, len(measured6), l6_metrics, gap2_6, commute, nonflat, singleton_commute


def main():
    print("SCOPE supplied free h(k), geometric deletion and occupation instrument; physical record mapping/rate open")
    cliff, rows, mutation = exact_algebra()
    check("exact integer Clifford coefficients", cliff == 0)
    check("exact even-to-odd row orthogonality coefficients", rows == 0)
    check("sign-flipped gamma edge breaks square identity", mutation > 0)
    print(f"ALGEBRA clifford={cliff} row_orthogonality={rows} mutation_residual={mutation}")

    cases, spec, poly, prop, zeros = spectral_checks()
    check("all-subset spectra and multiplicities", spec < TOL and zeros)
    check("minimal polynomial h_R^3=epsilon^2 h_R", poly < TOL)
    check("closed propagator including node", prop < TOL)
    print(f"BLOCH cases={cases} max_spec{bound_report(spec, TOL)}"
          f" max_poly{bound_report(poly, TOL)} max_prop{bound_report(prop, TOL)}")

    by_length, herm, rspec, max_dimension, node_blocks = realspace_checks()
    check("direct nearest-neighbor tori are Hermitian", herm == 0.0)
    check("direct torus spectra equal Bloch multisets", rspec < TOL)
    check("real-space size cap and explicit node degeneracies", max_dimension == 512 and node_blocks == 32)
    print("TORUS " + " ".join(f"L={length}:err{bound_report(err, TOL)}" for length, err in by_length)
          + f" maxdim={max_dimension} node_blocks={node_blocks}")

    fac = state_factorization_checks()
    open_cases, open_metrics, open_gap2, measured6, l6_metrics, gap2_6, commute, nonflat, singleton_commute = fac
    open_err = float(open_metrics.max())
    l6_err = float(l6_metrics.max())
    joint_metrics = np.maximum(open_metrics, l6_metrics)
    check("conditional Slater factorization on open cube", open_cases == 81 and open_err < 5e-10)
    check("conditional Slater factorization on non-flat L=6 torus", measured6 == 27 and l6_err < 5e-10)
    check("class projectors commute with invertible K; L=6 K is non-flat",
          open_gap2 > 1e-8 and gap2_6 > 1e-8 and commute < TOL and nonflat > 1e-2)
    check("single-site selector detects a nonzero K commutator", singleton_commute > 1e-3)
    print(f"STATE separate fermion-number instrument open_cases={open_cases} err{bound_report(open_err, 5e-10)}"
          f" L6_patterns=all0,all1,cell-parity sites={measured6}"
          f" err{bound_report(l6_err, 5e-10)} Kspread={nonflat:.6f}"
          f" Kclass{bound_report(commute, TOL)} Ksingle={singleton_commute:.6f}")
    print("STATE_TESTS " + " ".join(
        f"{name}{bound_report(joint_metrics[i], 5e-10)}"
        for i, name in enumerate(("C", "comm", "Pneg", "zero", "idem", "trace", "orth"))))
    print("STATE_SCOPE finite BKSF bridge unchecked; no edge-Z-star equivalence or three-generation claim")

    packets, norm_error, eigen_residual = packet_checks()
    check("packet normalization at t=0,1,2", norm_error < 2e-12)
    check("packet fibers lie in positive band away from node", eigen_residual < TOL)
    print("PACKET k0=(pi/4)^3 sigma=0.20 n0=N/2; transfer errors are reported, not fitted")
    for nc, r, result in packets:
        print(f"PK N={nc:2d} r={r} pol={result['polarization']:03b}"
              f" normerr{bound_report(result['norm_error'], 2e-12)}"
              f" zero={result['zero_weight']:.3e} vg={fmt_vec(result['velocity'])}"
              f" d1={fmt_vec(result['displacements'][1])} e1={result['errors'][1]:.3e}"
              f" d2={fmt_vec(result['displacements'][2])} e2={result['errors'][2]:.3e}"
              f" wrap={max(result['tails']):.3e}")

    elapsed = time.monotonic() - T0
    peak_mib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024.0 * 1024.0)
    check("runtime under 60 seconds", elapsed < 60.0)
    check("peak memory under 1 GiB", peak_mib < 1024.0)
    print(f"RESOURCES seconds={elapsed:.3f} peak_MiB={peak_mib:.1f}")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    raise SystemExit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
