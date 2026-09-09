#!/usr/bin/env python3
"""A time-directed formation sweep registers the direction of motion at order one and its screw
sense registers nothing: the record-side image of a current, not a chirality.

Self-contained class-A runner: no seed, no random number, no external input file, no import of any
repository module.  Every enumeration below is complete or a declared sub-family, and every
eigenproblem is a deterministic LAPACK call.  Largest dense matrix built anywhere: 2048 x 2048
(the record-time vortex at N = 16); the 3456-site string and its scans are carried sparse.

Copied source blocks (the probe scripts of 2026-09-05; each copy names the block it reproduces):
  make_geom / build_string / cell_displacement_matrix / sector_basis / diagonalise_sectors /
  restrict / cheb_coeffs / expm_apply / sweep_forward / sweep_backward / screw_schedule /
  schedule_key / map_schedule / rot_mats / plane_syms / sym_name / permute_sp / gauge_between /
  all_patterns / det_law / tv / region_perm / mirror_law / chi_pseudoscalars   <- h5_common.py
  pick / mover_density / odds / kernels / column / scan_case      <- h5_string.py A, B, C, D
  delta / the C2(x) control family / the off-plane core geometry  <- h5_string_extra.py E1, E2, E5
  build_block / fock_sector / hop_matrix / slater / restrict1 / det_law_full / run_case /
  orders_for                                                      <- h5_manybody.py
  chain_ops / H8 / prof_vortex / schedule / restrict_modes / site_density / the C identity /
  the Gamma-product scan                                          <- h5_vortex.py, h5_vortex2.py
  the helicity + alpha_1 alpha_4 certificate                      <- h5_vortex3.py X1
  group / dir_perm / orbits / burnside / cluster / step_pseudoscalar_table / dp_count /
  final_law_asym / screw_orders / xi_of_order / the seven rules   <- h5_rules.py
  the F-fixed chiral orbit census and the slab middle-corner split  <- h5_rules2.py
The dynamic programme of h5_rules.py::dp_count is reproduced here in a vectorised form over the
same 3^V ternary configurations; its integer outputs are the probe's, checked against them below.

Groups: A the string, its movers and its point group; B the directed sweep (T1); C the screw sense
        (T2); D the exact symmetries (T3); E the many-body certification; F the record-time vortex
        (T4); G the rule census on the cube and the slab (T5).

Declared reductions (everything else is recomputed from scratch), with the probe output lines that
carry the rest:
  * The string's transverse-size scan recomputes N_s = 8, 12, 16 and the length scan L_z = 24, 48,
    96 at p = pi/6; the momentum scan recomputes p = pi/24, pi/12, pi/6 and quotes p = pi/8
    (h5_string.py -> out_string.txt:93, plane+ Delta_core = -0.54469).
  * The pitch scan recomputes both screw senses at pitch 4, 8, 12, 24 swept +z and pitch 4 swept
    -z; the -z sweeps at pitch 8, 12, 24 are quoted (out_string.txt:20, 22, 26, 28, 30).
  * The pattern-level laws are recomputed on the 2x2x4 core column; the 2x2x2 column is quoted
    (out_string.txt:55-67: TV(sea+R, sea) = 0.009634, plane+ Delta = -0.011679, exact checks
    0.0e+00 / 1.2e-15 / 6.4e-15).
  * The off-mirror-plane core scan recomputes N_s = 8, 12, 16 and quotes N_s = 20
    (h5_string_extra.py -> out_string_extra.txt:20: mirror difference -1.51e-04, ring weight 0.019).
  * The many-body Lueders tree is walked in full on the open 2x2x2 block and for one order on the
    2x2x3 block; the remaining 2x2x3 orders are quoted (h5_manybody.py -> out_manybody.txt:10,
    12-16: tree = p_K to 1.2e-16, T-pair 0.0e+00).
  * The record-time vortex recomputes N = 16 at p = (0.1 pi, 0, 0) for the plane sweep and the
    outward spirals of pitch 2, 4, 8 in both senses, and the N = 12 certificate at both momenta;
    the inward spirals, plane-, and the whole generic-momentum registration battery are quoted
    (out_vortex.txt:21-46, out_vortex2.txt:9-14: every Delta <= 1.11e-15).
  * The slab rule census recomputes R0, R1, R2, R3 and R4 and quotes the two mirror rules R2m and
    R3m (h5_rules.py -> out_rules.txt:21, 23: identical counts, mean Xi 0.000e+00).

Output: one PASS/FAIL line per check, and a final `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import math
import sys
import time

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp
from scipy.special import jv

AUDIT_TIMEOUT_SEC = 200

T0 = time.time()
PASS = 0
FAIL = 0


def check(msg, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("%s %s" % ("PASS" if ok else "FAIL", msg))


# ==================================================================== h5_common.py: the string
M0, XI, EMAX = 0.7, 2.0, 0.686


def make_geom(NS, LZ, core=None):                                  # h5_common.py::make_geom
    core = ((NS - 1) / 2.0, (NS - 1) / 2.0) if core is None else core
    sidx = {(x, y, z): (x * NS + y) * LZ + z for x in range(NS) for y in range(NS) for z in range(LZ)}
    V = len(sidx)
    xs = np.zeros(V); ys = np.zeros(V); zs = np.zeros(V)
    for (x, y, z), i in sidx.items():
        xs[i], ys[i], zs[i] = x, y, z
    rho = np.hypot(xs - core[0], ys - core[1])
    phi = np.mod(np.arctan2(xs - core[0], ys - core[1]), 2 * np.pi)
    quad = np.floor(4 * phi / (2 * np.pi)).astype(int)
    core_mask = rho < 3.5
    ring_mask = np.minimum.reduce([xs, ys, NS - 1 - xs, NS - 1 - ys]) < 2
    return dict(NS=NS, LZ=LZ, NC=LZ // 2, core=core, sidx=sidx, V=V, xs=xs, ys=ys, zs=zs,
                rho=rho, quad=quad, core_mask=core_mask, ring_mask=ring_mask,
                bulk_mask=~core_mask & ~ring_mask, eps=(-1.0) ** (xs + ys + zs))


def build_string(g, n_wind):                                       # h5_common.py::build_string
    NS, LZ, sidx, core = g["NS"], g["LZ"], g["sidx"], g["core"]
    rows, cols, vals = [], [], []

    def add(i, j, val):
        rows.append(i); cols.append(j); vals.append(val)
    for (x, y, z), i in sidx.items():
        if x + 1 < NS:
            j = sidx[(x + 1, y, z)]; add(i, j, 1.0); add(j, i, 1.0)
        if y + 1 < NS:
            j = sidx[(x, y + 1, z)]; add(i, j, float((-1) ** x)); add(j, i, float((-1) ** x))
        j = sidx[(x, y, (z + 1) % LZ)]; add(i, j, float((-1) ** (x + y))); add(j, i, float((-1) ** (x + y)))

    def mass(px, py):
        r = np.hypot(px - core[0], py - core[1])
        return M0 * np.tanh(r / XI), n_wind * np.arctan2(py - core[1], px - core[0])
    for (x, y, z), i in sidx.items():
        mag, ph = mass(x, y)
        add(i, i, mag * np.cos(ph) * (-1) ** (x + y + z))
    for X in range(NS // 2):
        for Y in range(NS // 2):
            mag, ph = mass(2 * X + 0.5, 2 * Y + 0.5)
            m2c = mag * np.sin(ph)
            for Z in range(LZ // 2):
                for b in itertools.product((0, 1), repeat=3):
                    s = sidx[(2 * X + b[0], 2 * Y + b[1], 2 * Z + b[2])]
                    sb = sidx[(2 * X + 1 - b[0], 2 * Y + 1 - b[1], 2 * Z + 1 - b[2])]
                    add(sb, s, m2c * 1j * (-1) ** b[1])
    H = sp.csr_matrix((np.array(vals, dtype=complex), (rows, cols)), shape=(g["V"], g["V"]))
    H.sum_duplicates()
    return H


def cell_displacement_matrix(g, H):                    # h5_common.py::cell_displacement_matrix
    NC = g["NC"]
    Hc = H.tocoo()
    d = ((g["zs"][Hc.row] // 2).astype(int) - (g["zs"][Hc.col] // 2).astype(int)) % NC
    d = np.where(d > NC // 2, d - NC, d)
    return sp.csr_matrix((-1j * d * Hc.data, (Hc.row, Hc.col)), shape=H.shape)


def sector_basis(g, q):                                            # h5_common.py::sector_basis
    NS, NC, sidx = g["NS"], g["NC"], g["sidx"]
    B = np.zeros((g["V"], 2 * NS * NS), dtype=complex)
    col = 0
    for x in range(NS):
        for y in range(NS):
            for b in range(2):
                for Z in range(NC):
                    B[sidx[(x, y, 2 * Z + b)], col] = np.exp(1j * q * Z) / np.sqrt(NC)
                col += 1
    return B


def diagonalise_sectors(g, H, want_W=True):               # h5_common.py::diagonalise_sectors
    NC = g["NC"]
    Hv = cell_displacement_matrix(g, H)
    Wcols, modes = [], []
    resid = 0.0
    for jq in range(NC):
        q = 2 * np.pi * jq / NC
        p = (q % (2 * np.pi)) - np.pi
        B = sector_basis(g, q)
        Hq = B.conj().T @ (H @ B)
        Hq = (Hq + Hq.conj().T) / 2
        w, U = np.linalg.eigh(Hq)
        Vq = B.conj().T @ (Hv @ B)
        if want_W:
            Wcols.append(B @ U[:, w < 0])
        for k in np.flatnonzero(np.abs(w) < EMAX):
            psi = B @ U[:, k]
            resid = max(resid, float(np.linalg.norm(H @ psi - w[k] * psi)))
            dens = np.abs(psi) ** 2
            modes.append(dict(E=float(w[k]), p=float(p), psi=psi,
                              core=float(dens[g["core_mask"]].sum()),
                              ring=float(dens[g["ring_mask"]].sum()),
                              v=float(np.real(np.vdot(U[:, k], Vq @ U[:, k])))))
    W = np.concatenate(Wcols, axis=1) if want_W else None
    return W, modes, resid


def restrict(H, recorded):                                             # h5_common.py::restrict
    D = sp.diags((~recorded).astype(float))
    return (D @ H @ D).tocsr()


def cheb_coeffs(tau_a, tol=1e-17):                                  # h5_common.py::cheb_coeffs
    k, coeffs = 0, []
    while True:
        b = jv(k, tau_a)
        coeffs.append(b)
        if k > abs(tau_a) + 5 and abs(b) < tol:
            break
        k += 1
        if k > 4000:
            break
    c = np.array(coeffs, dtype=complex)
    c[1:] *= 2 * (-1j) ** np.arange(1, len(c))
    return c


def expm_apply(H, tau, X, a=None):                                   # h5_common.py::expm_apply
    if a is None:
        a = float(np.abs(H).sum(axis=1).max())
    if a == 0.0 or tau == 0.0:
        return X.copy()
    c = cheb_coeffs(tau * a)
    Hs = H / a
    T0_, T1 = X, Hs @ X
    Y = c[0] * T0_ + c[1] * T1
    for k in range(2, len(c)):
        T2 = 2 * (Hs @ T1) - T0_
        Y += c[k] * T2
        T0_, T1 = T1, T2
    return Y


def sweep_forward(H, schedule, tau, X, a=None):                   # h5_common.py::sweep_forward
    rec = np.zeros(H.shape[0], dtype=bool)
    Y = X.copy()
    for i, S in enumerate(schedule):
        rec[S] = True
        if i == len(schedule) - 1:
            break
        Y = expm_apply(restrict(H, rec), tau, Y, a)
    return Y


def sweep_backward(H, schedule, tau, X, a=None):                 # h5_common.py::sweep_backward
    recs, rec = [], np.zeros(H.shape[0], dtype=bool)
    for S in schedule[:-1]:
        rec = rec.copy(); rec[S] = True
        recs.append(rec)
    Y = X.copy()
    for rec in reversed(recs):
        Y = expm_apply(restrict(H, rec), -tau, Y, a)
    return Y


def screw_schedule(g, s, pitch, direction=+1):                   # h5_common.py::screw_schedule
    t = g["zs"].astype(int) - s * pitch * (g["quad"] + 0.5) / 4.0
    t = np.round(t * 4) / 4.0
    sched = [np.flatnonzero(t == tv) for tv in np.unique(t)]
    return sched[::-1] if direction < 0 else sched


def schedule_key(sched):                                          # h5_common.py::schedule_key
    return tuple(tuple(sorted(int(v) for v in S)) for S in sched)


def map_schedule(sched, perm):                                     # h5_common.py::map_schedule
    return [np.sort(perm[S]) for S in sched]


def rot_mats():                                                       # h5_common.py::rot_mats
    mats, dets = [], []
    for P in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3))
            for i in range(3):
                M[i, P[i]] = sg[i]
            mats.append(M); dets.append(int(round(np.linalg.det(M))))
    return mats, dets


def plane_syms(g):                                                  # h5_common.py::plane_syms
    out = []
    cz = (g["LZ"] - 1) / 2.0
    core, sidx, LZ = g["core"], g["sidx"], g["LZ"]
    for M, d in zip(*rot_mats()):
        perm = np.zeros(g["V"], dtype=int)
        ok = True
        for (x, y, z), v in sidx.items():
            gc = M @ np.array([x - core[0], y - core[1], z - cz])
            s_ = (gc[0] + core[0], gc[1] + core[1], gc[2] + cz)
            si = tuple(int(round(t)) for t in s_)
            if any(abs(si[a] - s_[a]) > 1e-9 for a in range(3)):
                ok = False; break
            si = (si[0], si[1], si[2] % LZ)
            if si not in sidx:
                ok = False; break
            perm[v] = sidx[si]
        if ok:
            out.append((M, d, perm))
    return out


def sym_name(M):                                                      # h5_common.py::sym_name
    names = {(1, 1, 1): "identity", (-1, 1, 1): "sigma_x", (1, -1, 1): "sigma_y",
             (1, 1, -1): "sigma_z", (-1, -1, 1): "C2(z)", (-1, 1, -1): "C2(y)",
             (1, -1, -1): "C2(x)", (-1, -1, -1): "inversion"}
    if np.allclose(np.abs(M), np.eye(3)):
        return names[tuple(int(M[i, i]) for i in range(3))]
    return "other"


def permute_sp(A, perm):                                            # h5_common.py::permute_sp
    P = sp.csr_matrix((np.ones(len(perm)), (perm, np.arange(len(perm)))), shape=A.shape)
    return (P @ A @ P.T).tocsr()


def gauge_between(H, Hp):                                        # h5_common.py::gauge_between
    H, Hp = H.tocsr().copy(), Hp.tocsr().copy()
    for A in (H, Hp):
        A.data[np.abs(A.data) < 1e-12] = 0.0
        A.eliminate_zeros(); A.sort_indices()
    V = H.shape[0]
    if not (np.array_equal(H.indptr, Hp.indptr) and np.array_equal(H.indices, Hp.indices)):
        return None, float("inf")
    D = np.zeros(V, dtype=complex)
    D[0] = 1.0
    stack, seen = [0], {0}
    while stack:
        u = stack.pop()
        for t in range(H.indptr[u], H.indptr[u + 1]):
            v = H.indices[t]
            if v not in seen and abs(H.data[t]) > 1e-12:
                seen.add(v)
                D[v] = np.conj(Hp.data[t] / (D[u] * H.data[t]))
                D[v] /= abs(D[v])
                stack.append(v)
    rowsi = np.repeat(np.arange(V), np.diff(H.indptr))
    return D, float(np.max(np.abs(Hp.data - D[rowsi] * np.conj(D[H.indices]) * H.data)))


def all_patterns(n):                                              # h5_common.py::all_patterns
    return ((np.arange(1 << n)[:, None] >> np.arange(n)[None, :]) & 1).astype(float)


def det_law(K, bits, chunk=1 << 13):                                   # h5_common.py::det_law
    n = K.shape[0]
    out = np.empty(len(bits))
    I = np.eye(n)
    for s in range(0, len(bits), chunk):
        b = bits[s:s + chunk]
        M = b[:, :, None] * K[None, :, :] + (1 - b)[:, :, None] * (I - K)[None, :, :]
        out[s:s + chunk] = np.real(np.linalg.det(M))
    return out


def tv(p, q):                                                                # h5_common.py::tv
    return 0.5 * float(np.abs(p - q).sum())


def region_perm(region, perm):                                    # h5_common.py::region_perm
    pos = {v: i for i, v in enumerate(region)}
    return np.array([pos[int(perm[v])] for v in region])


def mirror_law(law, bits, rp):                                      # h5_common.py::mirror_law
    return law[(bits[:, rp] * (1 << np.arange(bits.shape[1]))).sum(axis=1).astype(int)]


def chi_pseudoscalars(K, rp, kmax=3):                        # h5_common.py::chi_pseudoscalars
    n = K.shape[0]
    out = {}
    for k in range(2, kmax + 1):
        tot = 0.0
        for S in itertools.combinations(range(n), k):
            Sm = tuple(sorted(int(rp[i]) for i in S))
            if Sm <= S:
                continue
            tot += float(np.real(np.linalg.det(K[np.ix_(S, S)]) - np.linalg.det(K[np.ix_(Sm, Sm)])))
        out[k] = tot
    return out


# ============================================ A. the string, its movers and its point group
NS, LZ = 12, 24
g = make_geom(NS, LZ)
Hs = build_string(g, +1)
Ha = build_string(g, -1)
A_BOUND = float(np.abs(Hs).sum(axis=1).max())
W, MODES, resid = diagonalise_sectors(g, Hs)
check("A1 [1e-14] string 12x12x24, open plane, periodic axis, M0 0.7, xi 2: V %d, Herm %.0e, anti ="
      " conj(h) %.0e, sea %d, resid %.1e, bound %.4f"
      % (g["V"], abs(Hs - Hs.getH()).max(), abs(Ha - Hs.conjugate()).max(), W.shape[1], resid, A_BOUND),
      g["V"] == 3456 and W.shape[1] == 1728 and abs(Hs - Hs.getH()).max() == 0.0
      and abs(Ha - Hs.conjugate()).max() == 0.0 and resid < 1e-14 and abs(A_BOUND - 7.0353) < 1e-4)


def pick(modes, p, esign, region, n=2):                                  # h5_string.py::pick
    cand = [m for m in modes if abs(m["p"] - p) < 1e-9 and np.sign(m["E"]) == esign]
    cand.sort(key=lambda m: -m[region])
    return cand[:n]


P0 = np.pi / 6
R_, L_, H_ = pick(MODES, +P0, +1, "core"), pick(MODES, -P0, +1, "ring"), pick(MODES, -P0, -1, "core")
PsiR = np.stack([m["psi"] for m in R_], axis=1)
PsiL = np.stack([m["psi"] for m in L_], axis=1)
PsiH = np.stack([m["psi"] for m in H_], axis=1)
anti_res = max(float(np.linalg.norm(Ha @ np.conj(PsiR[:, k]) - R_[k]["E"] * np.conj(PsiR[:, k]))) for k in range(2))
check("A2 [1e-14] core R doublet p +pi/6: E %+.5f, v %+.4f, core %.3f, ring %.3f; ring L p -pi/6: v"
      " %+.4f, ring %.3f; the core hole at -pi/6 also has v %+.4f: no core left-mover on one "
      "string; conj(psi_R) on the anti-string %.1e"
      % (R_[0]["E"], R_[0]["v"], R_[0]["core"], R_[0]["ring"], L_[0]["v"], L_[0]["ring"], H_[0]["v"], anti_res),
      abs(R_[0]["E"] - 0.51019) < 1e-5 and abs(R_[0]["v"] - 0.8809) < 1e-4 and abs(L_[0]["v"] + 0.8809) < 1e-4
      and abs(H_[0]["v"] - 0.8809) < 1e-4 and abs(R_[0]["core"] - 0.619) < 1e-3
      and abs(L_[0]["ring"] - 0.876) < 1e-3 and anti_res < 1e-14)

SYMS = plane_syms(g)
PERM = {sym_name(M): pm for M, d, pm in SYMS}
eps = sp.diags(g["eps"])
Dx, rx = gauge_between(Hs, permute_sp(Hs, PERM["sigma_x"]))
_, r_inv = gauge_between(Ha, permute_sp(Hs, PERM["inversion"]))
_, r_c2x = gauge_between(Ha, permute_sp(Hs, PERM["C2(x)"]))
Dy, r_y = gauge_between(-(eps @ Ha @ eps), permute_sp(Hs, PERM["sigma_y"]))
r_z = abs(permute_sp(Hs, PERM["sigma_z"]) + eps @ Hs @ eps).max()
Ux = PsiR.conj().T @ (np.conj(Dx)[:, None] * PsiR[PERM["sigma_x"], :])
evx = np.linalg.eigvals(Ux)
check("A3 [1e-14] point group, %d elements: s_x h = D h D+ %.0e; inversion, C2(x) -> anti-string "
      "%.0e, %.0e; s_z h = -eps h eps %.0e; s_y h = D(-eps h_a eps)D+ %.0e, D real %s; R doublet D "
      "s_x unitary %.0e, eigs %s"
      % (len(SYMS), rx, r_inv, r_c2x, r_z, r_y, bool(np.max(np.abs(Dy.imag)) < 1e-12),
         np.abs(Ux.conj().T @ Ux - np.eye(2)).max(), np.round(evx.real, 6).tolist()),
      len(SYMS) == 16 and rx < 1e-14 and r_inv < 1e-14 and r_c2x == 0.0 and r_z == 0.0 and r_y == 0.0
      and np.max(np.abs(Dy.imag)) < 1e-12 and np.abs(Ux.conj().T @ Ux - np.eye(2)).max() < 1e-13
      and np.allclose(np.sort(evx.real), [-1.0, -1.0], atol=1e-9))

SW = {"plane+": screw_schedule(g, +1, 0, +1), "plane-": screw_schedule(g, +1, 0, -1)}
for pitch in (4, 8, 12, 24):
    for s, sn in ((+1, "+"), (-1, "-")):
        for d, dn in ((+1, "+z"), (-1, "-z")):
            SW["screw%s p%d %s" % (sn, pitch, dn)] = screw_schedule(g, s, pitch, d)
okx = all(schedule_key(map_schedule(SW["screw+ p%d +z" % p], PERM["sigma_x"])) == schedule_key(SW["screw- p%d +z" % p]) for p in (4, 8, 12, 24))
okz = all(schedule_key(map_schedule(SW["screw+ p%d +z" % p], PERM["sigma_z"])) == schedule_key(SW["screw- p%d -z" % p]) for p in (4, 8, 12, 24))
okp = (schedule_key(map_schedule(SW["plane+"], PERM["sigma_x"])) == schedule_key(SW["plane+"])
       and schedule_key(map_schedule(SW["plane+"], PERM["sigma_z"])) == schedule_key(SW["plane-"]))
g2 = make_geom(4, 8)
H2 = build_string(g2, +1)
rec2 = np.zeros(g2["V"], bool); rec2[:20] = True
HR2 = restrict(H2, rec2)
X2 = np.exp(1j * np.arange(g2["V"]) * 0.37)[:, None] * np.ones((1, 3)); X2 = X2 / np.linalg.norm(X2, axis=0)
cheb_err = max(np.abs(expm_apply(HR2, t, X2) - sla.expm(-1j * t * HR2.toarray()) @ X2).max() for t in (0.1, 0.5, 2.0))
check("A4 [exact / 1e-15] sweeps by (z-slice, quadrant), steps 24/27/30/33/42: s_x(screw+) = screw-"
      " %s, s_z(screw+, +z) = screw- swept -z %s, s_x(plane+) = plane+, s_z(plane+) = plane- %s; "
      "Chebyshev vs expm %.0e"
      % (okx, okz, okp, cheb_err),
      okx and okz and okp and cheb_err < 1e-15
      and [len(SW[k]) for k in ("plane+", "screw+ p4 +z", "screw+ p8 +z", "screw+ p12 +z", "screw+ p24 +z")] == [24, 27, 30, 33, 42])


# ================================ B. T1: a directed sweep registers the direction of motion
REGS = {"core": g["core_mask"], "bulk": g["bulk_mask"], "ring": g["ring_mask"]}


def mover_density(H, sched, tau, Psi, a=A_BOUND):                # h5_string.py::mover_density
    return (np.abs(sweep_forward(H, sched, tau, Psi, a)) ** 2).sum(axis=1) / Psi.shape[1]


def odds(mu, regs=REGS):                                                 # h5_string.py::odds
    return {r: float(mu[m].sum()) for r, m in regs.items()}


def delta(H, sched, tau, Psi, regs=REGS, a=A_BOUND):            # h5_string_extra.py::delta
    op = odds(mover_density(H, sched, tau, Psi, a), regs)
    om = odds(mover_density(H, sched, -tau, Psi, a), regs)
    return {r: op[r] - om[r] for r in regs}


MU = {}
for name in SW:
    for sgn in (+1, -1):
        MU[(name, 0.5, sgn)] = mover_density(Hs, SW[name], sgn * 0.5, PsiR)
DEL = {name: {r: float(MU[(name, 0.5, +1)][m].sum() - MU[(name, 0.5, -1)][m].sum()) for r, m in REGS.items()} for name in SW}
muA = mover_density(Ha, SW["plane+"], 0.5, np.conj(PsiR))
check("B1 [exact] under plane+, anti-string+conj(psi_R) at +tau and string+psi_R at -tau register "
      "identically site by site, %.1e: D = O(+tau)-O(-tau) is core R vs its T-partner"
      % (np.abs(muA - MU[("plane+", 0.5, -1)]).max(),),
      np.abs(muA - MU[("plane+", 0.5, -1)]).max() == 0.0)

op, om = odds(MU[("plane+", 0.5, +1)]), odds(MU[("plane+", 0.5, -1)])
check("B2 [1e-4] plane+ tau 0.5: core odds %.4f vs the T-partner's %.4f, D_core %+.5f, D_ring "
      "%+.5f; plane- exactly the negative %+.5f; pitch 4/8/12/24 at +z: %+.5f, %+.5f, %+.5f, %+.5f"
      % (op["core"], om["core"], DEL["plane+"]["core"], DEL["plane+"]["ring"], DEL["plane-"]["core"],
         DEL["screw+ p4 +z"]["core"], DEL["screw+ p8 +z"]["core"], DEL["screw+ p12 +z"]["core"],
         DEL["screw+ p24 +z"]["core"]),
      abs(op["core"] - 0.1366) < 1e-4 and abs(om["core"] - 0.6048) < 1e-4
      and abs(DEL["plane+"]["core"] + 0.46825) < 1e-5 and abs(DEL["plane+"]["ring"] - 0.54803) < 1e-5
      and abs(DEL["plane+"]["core"] + DEL["plane-"]["core"]) < 1e-14
      and abs(DEL["screw+ p4 +z"]["core"] + 0.43744) < 1e-5 and abs(DEL["screw+ p8 +z"]["core"] + 0.39396) < 1e-5
      and abs(DEL["screw+ p12 +z"]["core"] + 0.32929) < 1e-5 and abs(DEL["screw+ p24 +z"]["core"] + 0.25016) < 1e-5)

TAUS = (0.05, 0.1, 0.25, 0.5, 1.0, 2.0)
dtau = [delta(Hs, SW["plane+"], t, PsiR)["core"] for t in TAUS]
check("B3 [1e-4] D_core(plane+), tau 0.05/0.1/0.25/0.5/1/2: %s; D/tau %s at the first three, "
      "falling as tau -> 0: small-tau growth faster than linear, saturating near -0.5"
      % (", ".join("%+.4f" % v for v in dtau), ", ".join("%.2f" % (v / t) for v, t in zip(dtau[:3], TAUS))),
      all(abs(a - b) < 1e-4 for a, b in zip(dtau, (-0.01092, -0.05289, -0.20208, -0.46825, -0.49816, -0.23069)))
      and dtau[0] / 0.05 > dtau[1] / 0.1 > dtau[2] / 0.25 > dtau[3] / 0.5)


def scan_case(NS_, LZ_, p_target, names, tau=0.5, core=None):        # h5_string.py::scan_case
    gg = make_geom(NS_, LZ_, core=core)
    H = build_string(gg, +1)
    a = float(np.abs(H).sum(axis=1).max())
    _, ms, _ = diagonalise_sectors(gg, H, want_W=False)
    Rm = pick(ms, +p_target, +1, "core")
    Psi = np.stack([m["psi"] for m in Rm], axis=1)
    regs = {"core": gg["core_mask"], "bulk": gg["bulk_mask"], "ring": gg["ring_mask"]}
    SWg = {"plane+": screw_schedule(gg, +1, 0, +1), "screw+ p4 +z": screw_schedule(gg, +1, 4, +1),
           "screw- p4 +z": screw_schedule(gg, -1, 4, +1)}
    out = {"core_w": Rm[0]["core"], "ring_w": Rm[0]["ring"], "E": Rm[0]["E"]}
    for nm in names:
        out[nm] = delta(H, SWg[nm], tau, Psi, regs, a)
    return out

sz = [scan_case(n_, 24, P0, ("plane+",))["plane+"]["core"] for n_ in (8, 16)]
lz48 = scan_case(12, 48, P0, ("plane+",))
g96 = make_geom(12, 96)
H96 = build_string(g96, +1)
a96 = float(np.abs(H96).sum(axis=1).max())
_, m96, _ = diagonalise_sectors(g96, H96, want_W=False)
r96 = {}
for pt in (np.pi / 24, np.pi / 6):
    Rm = pick(m96, +pt, +1, "core")
    Psi = np.stack([m["psi"] for m in Rm], axis=1)
    regs96 = {"core": g96["core_mask"], "bulk": g96["bulk_mask"], "ring": g96["ring_mask"]}
    r96[pt] = delta(H96, screw_schedule(g96, +1, 0, +1), 0.5, Psi, regs96, a96)["core"]
del H96, m96
p12 = scan_case(12, 48, np.pi / 12, ("plane+",))["plane+"]["core"]
check("B4 [1e-4] N_s 8/12/16: %+.4f, %+.4f, %+.4f; L_z 24/48/96 at p pi/6: %+.4f, %+.4f, %+.4f; p "
      "pi/24, pi/12, pi/6: %+.4f, %+.4f, %+.4f (pi/8 quoted)"
      % (sz[0], DEL["plane+"]["core"], sz[1], DEL["plane+"]["core"], lz48["plane+"]["core"],
         r96[np.pi / 6], r96[np.pi / 24], p12, DEL["plane+"]["core"]),
      abs(sz[0] + 0.43525) < 1e-4 and abs(sz[1] + 0.45069) < 1e-4
      and abs(lz48["plane+"]["core"] + 0.50312) < 1e-4 and abs(r96[np.pi / 6] + 0.52641) < 1e-4
      and abs(r96[np.pi / 24] + 0.54437) < 1e-4 and abs(p12 + 0.52697) < 1e-4)


# ============================================= C. T2: the screw sense registers exactly nothing
mir = []
for pitch in (4, 8, 12, 24):
    dirs = ("+z", "-z") if pitch == 4 else ("+z",)
    for dn in dirs:
        a_, b_ = DEL["screw+ p%d %s" % (pitch, dn)], DEL["screw- p%d %s" % (pitch, dn)]
        mp, mm = MU[("screw+ p%d %s" % (pitch, dn), 0.5, +1)], MU[("screw- p%d %s" % (pitch, dn), 0.5, +1)]
        mir.append((max(abs(a_[r] - b_[r]) for r in REGS), float(np.abs(mp - mm[PERM["sigma_x"]]).max())))
check("C1 [exact] screw sense registers nothing: D(screw+)-D(screw-) <= %.1e in core, bulk, ring at"
      " every pitch and direction; densities pointwise s_x images to %.1e"
      % (max(m[0] for m in mir), max(m[1] for m in mir)),
      max(m[0] for m in mir) < 1e-15 and max(m[1] for m in mir) < 1e-16)

off = []
for NS_ in (8, 12, 16):
    r = scan_case(NS_, 24, P0, ("plane+", "screw+ p4 +z", "screw- p4 +z"), core=(NS_ / 2 - 1.5, NS_ / 2 - 0.5))
    off.append((r["ring_w"], r["screw+ p4 +z"]["core"] - r["screw- p4 +z"]["core"], r["plane+"]["core"]))
check("C2 [1e-5] core off the mirror plane, screw difference at N_s 8/12/16: %s (N_s 20 quoted); "
      "directed bias %+.3f, %+.3f, %+.3f"
      % (", ".join("%+.1e (%.3f)" % (o[1], o[0]) for o in off), off[0][2], off[1][2], off[2][2]),
      abs(off[0][1] + 3.97e-3) < 1e-5 and abs(off[1][1] + 7.82e-4) < 1e-6 and abs(off[2][1] - 2.09e-4) < 1e-6
      and abs(off[0][0] - 0.551) < 1e-3 and abs(off[2][0] - 0.057) < 1e-3
      and all(abs(o[2] + 0.46) < 0.03 for o in off))


# ================================================================ D. T3: the exact symmetries
c2t = []
for name in ("plane+", "screw+ p4 +z", "screw+ p8 +z", "screw+ p12 +z", "screw+ p24 +z", "screw- p4 +z"):
    S = SW[name]
    Sc = map_schedule(S, PERM["C2(x)"])
    dS, dSc = DEL[name]["core"], delta(Hs, Sc, 0.5, PsiR)["core"]
    pw = float(np.abs(MU[(name, 0.5, +1)] - mover_density(Hs, Sc, -0.5, PsiR)[PERM["C2(x)"]]).max())
    c2t.append((dS + dSc, pw))
rev = [0.25 * sum(DEL["screw%s p%d %s" % (s_, p_, d_)]["core"] for s_ in "+-" for d_ in ("+z", "-z")) for p_ in (4, 8, 12, 24)]
check("D1 [exact] C2(x) o T: mu_R(S, +tau) = C2(x) mu_R(C2(x)S, -tau) %.1e, D(S) = -D(C2(x)S) %.1e,"
      " every C2(x)-closed family averages exactly zero; reversal-closed screw families keep the "
      "seam, %s, plane %+.5f"
      % (max(c[1] for c in c2t), max(abs(c[0]) for c in c2t),
         ", ".join("%+.3f" % v for v in rev), 0.5 * (DEL["plane+"]["core"] + DEL["plane-"]["core"])),
      max(c[1] for c in c2t) < 1e-16 and max(abs(c[0]) for c in c2t) < 1e-15
      and abs(0.5 * (DEL["plane+"]["core"] + DEL["plane-"]["core"])) < 1e-15
      and all(abs(a - b) < 1e-4 for a, b in zip(rev, (0.00236, 0.00314, 0.00640, 0.00605))))

MUH = {}
for name in ("plane+", "plane-", "screw+ p4 +z", "screw- p4 -z"):
    MUH[name] = mover_density(Hs, SW[name], -0.5, PsiH)
pairs = {}
for name in ("plane+", "screw+ p4 +z"):
    tw = {"plane+": "plane-", "screw+ p4 +z": "screw- p4 -z"}[name]
    pairs[name] = float(np.abs(MU[(name, 0.5, +1)] - MUH[tw][PERM["sigma_z"]]).max())
oL = odds(mover_density(Hs, SW["plane+"], 0.5, PsiL))["ring"]
check("D2 [exact] mu_R(S, +tau) = s_z mu_hole(s_z S, -tau) %.1e (plane), %.1e (screw): the kernel "
      "is even under s_z x particle-hole x tau reversal; under plane+ core R keeps %.4f of the "
      "core, ring L %.4f of the ring"
      % (pairs["plane+"], pairs["screw+ p4 +z"], odds(MU[("plane+", 0.5, +1)])["core"], oL),
      pairs["plane+"] < 1e-16 and pairs["screw+ p4 +z"] < 1e-16 and abs(oL - 0.8540) < 1e-4)


def column(zlist):                                                     # h5_string.py::column
    return [g["sidx"][(x, y, z)] for z in zlist for x in (5, 6) for y in (5, 6)]


def kernels(H, Wsea, sched, tau, reg, Psi=None):                      # h5_string.py::kernels
    E = np.zeros((g["V"], len(reg)), dtype=complex)
    E[reg, np.arange(len(reg))] = 1.0
    B = sweep_backward(H, sched, tau, E, A_BOUND) if (sched is not None and tau != 0.0) else E
    X = Wsea.conj().T @ B
    K0 = X.conj().T @ X
    if Psi is None:
        return K0
    Y = Psi.conj().T @ B
    return K0 + Y.conj().T @ Y


REG4 = column([10, 11, 12, 13])
BITS = all_patterns(16)
rpx, rpz = region_perm(REG4, PERM["sigma_x"]), region_perm(REG4, PERM["sigma_z"])
p0s = det_law(kernels(Hs, W, None, 0.0, REG4), BITS)
pRs = det_law(kernels(Hs, W, None, 0.0, REG4, PsiR), BITS)
SigR = pRs > p0s
LAW = {}
for cnm, sc in (("plane+", SW["plane+"]), ("screw+ p4 +z", SW["screw+ p4 +z"]), ("screw- p4 +z", SW["screw- p4 +z"])):
    LAW[cnm] = (det_law(kernels(Hs, W, sc, 0.5, REG4, PsiR), BITS),
                det_law(kernels(Hs, W, sc, -0.5, REG4, PsiR), BITS))
p0p = det_law(kernels(Hs, W, SW["plane+"], 0.5, REG4), BITS)
p0m = det_law(kernels(Hs, W, SW["plane+"], -0.5, REG4), BITS)
cxp = chi_pseudoscalars(kernels(Hs, W, SW["screw+ p4 +z"], 0.5, REG4, PsiR), rpx)
cxm = chi_pseudoscalars(kernels(Hs, W, SW["screw- p4 +z"], 0.5, REG4, PsiR), rpx)
dpl = LAW["plane+"][0][SigR].sum() - LAW["plane+"][1][SigR].sum()
Ax_s = tv(LAW["screw+ p4 +z"][0], mirror_law(LAW["screw+ p4 +z"][0], BITS, rpx))
Ax_p = tv(LAW["plane+"][0], mirror_law(LAW["plane+"][0], BITS, rpx))
check("D3 [1e-5] 2x2x4 column+sea, 65536 patterns: static TV %.5f, |Sigma_R| %d, mass %.5f; plane+ "
      "tau 0.5: D %+.5f, TV(R+,R-) %.5f vs sea %.5f; screw chi_2 %+.5f/%+.5f, chi_3 %+.5f/%+.5f, "
      "A_x %.5f vs plane %.5f"
      % (tv(p0s, pRs), int(SigR.sum()), float(pRs[SigR].sum()), dpl, tv(*LAW["plane+"]), tv(p0p, p0m),
         cxp[2], cxm[2], cxp[3], cxm[3], Ax_s, Ax_p),
      abs(tv(p0s, pRs) - 0.015232) < 1e-6 and int(SigR.sum()) == 32020
      and abs(float(pRs[SigR].sum()) - 0.480775) < 1e-6 and abs(dpl + 0.015482) < 1e-6
      and abs(tv(*LAW["plane+"]) - 0.018923) < 1e-6 and abs(tv(p0p, p0m) - 0.006452) < 1e-6
      and abs(cxp[2] - 0.023666) < 1e-6 and abs(cxp[2] + cxm[2]) < 1e-13
      and abs(cxp[3] - 0.057275) < 1e-6 and abs(cxp[3] + cxm[3]) < 1e-13
      and abs(Ax_s - 0.044366) < 1e-6 and Ax_p < 1e-14)

pR_a = det_law(kernels(Ha, np.conj(W), SW["plane+"], 0.5, REG4, np.conj(PsiR)), BITS)
e1 = tv(pR_a, LAW["plane+"][1])
e2 = tv(LAW["screw+ p4 +z"][0], mirror_law(LAW["screw- p4 +z"][0], BITS, rpx))
hole_cols = [int(np.argmax(np.abs(W.conj().T @ PsiH[:, k]))) for k in range(2)]
W_hole = np.delete(W, hole_cols, axis=1)
flip = ((1 << 16) - 1) - (BITS @ (1 << np.arange(16))).astype(int)
e3 = tv(LAW["plane+"][0], mirror_law(det_law(kernels(Hs, W_hole, SW["plane-"], -0.5, REG4), BITS), BITS, rpz)[flip])
check("D4 [1e-14] pattern level: (i) anti+conj(psi_R) at +0.5 vs string+psi_R at -0.5, TV %.1e; "
      "(ii) screw+ vs s_x screw- %.1e; (iii) R at (plane+,+0.5) vs hole at (plane-,-0.5), s_z-"
      "relabelled, complemented, %.1e"
      % (e1, e2, e3),
      e1 == 0.0 and e2 < 1e-14 and e3 < 1e-13)


# ============================================== E. the many-body certification of the tick model
def build_block(Lx, Ly, Lz, n_wind=+1):                          # h5_manybody.py::build_block
    sidx = {(x, y, z): (x * Ly + y) * Lz + z for x in range(Lx) for y in range(Ly) for z in range(Lz)}
    V = len(sidx)
    h = np.zeros((V, V), dtype=complex)
    core = ((Lx - 1) / 2 + 0.7, (Ly - 1) / 2 - 0.4)
    for (x, y, z), i in sidx.items():
        if (x + 1, y, z) in sidx:
            j = sidx[(x + 1, y, z)]; h[i, j] += 1; h[j, i] += 1
        if (x, y + 1, z) in sidx:
            j = sidx[(x, y + 1, z)]; h[i, j] += (-1) ** x; h[j, i] += (-1) ** x
        if (x, y, z + 1) in sidx:
            j = sidx[(x, y, z + 1)]; h[i, j] += (-1) ** (x + y); h[j, i] += (-1) ** (x + y)
        r = np.hypot(x - core[0], y - core[1]); ph = n_wind * np.arctan2(y - core[1], x - core[0])
        h[i, i] += M0 * np.tanh(r / XI) * np.cos(ph) * (-1) ** (x + y + z)
    for X in range(Lx // 2):
        for Y in range(Ly // 2):
            r = np.hypot(2 * X + 0.5 - core[0], 2 * Y + 0.5 - core[1])
            ph = n_wind * np.arctan2(2 * Y + 0.5 - core[1], 2 * X + 0.5 - core[0])
            m2c = M0 * np.tanh(r / XI) * np.sin(ph)
            for Z in range(Lz // 2):
                for b in itertools.product((0, 1), repeat=3):
                    s_ = sidx[(2 * X + b[0], 2 * Y + b[1], 2 * Z + b[2])]
                    sb = sidx[(2 * X + 1 - b[0], 2 * Y + 1 - b[1], 2 * Z + 1 - b[2])]
                    h[sb, s_] += m2c * 1j * (-1) ** b[1]
    return h, sidx


def fock_sector(n, N):                                            # h5_manybody.py::fock_sector
    states = [s for s in range(1 << n) if bin(s).count("1") == N]
    return states, {s: i for i, s in enumerate(states)}


def hop_matrix(h, states, pos, n):                                # h5_manybody.py::hop_matrix
    H = np.zeros((len(states), len(states)), dtype=complex)
    for i, s in enumerate(states):
        for v in range(n):
            if not (s >> v) & 1:
                continue
            s1 = s ^ (1 << v); sign_v = (-1) ** bin(s & ((1 << v) - 1)).count("1")
            for u in range(n):
                if h[u, v] == 0 or (s1 >> u) & 1:
                    continue
                s2 = s1 | (1 << u); sign_u = (-1) ** bin(s1 & ((1 << u) - 1)).count("1")
                H[pos[s2], i] += h[u, v] * sign_u * sign_v
    return H


def slater(Wm, states):                                                # h5_manybody.py::slater
    amp = np.zeros(len(states), dtype=complex)
    for i, s in enumerate(states):
        amp[i] = np.linalg.det(Wm[[v for v in range(Wm.shape[0]) if (s >> v) & 1], :])
    return amp


def restrict1(h, rec):                                              # h5_manybody.py::restrict1
    keep = np.where(rec, 0.0, 1.0)
    return keep[:, None] * h * keep[None, :]


def run_case(Lx, Ly, Lz, order, tau, conj=False):                    # h5_manybody.py::run_case
    h, _ = build_block(Lx, Ly, Lz)
    if conj:
        h = np.conj(h)
    n = h.shape[0]; N = n // 2 + 1
    w, U = np.linalg.eigh(h)
    Wm = U[:, :N]
    states, pos = fock_sector(n, N)
    amp = slater(Wm, states)
    rec = np.zeros(n, bool); G = np.eye(n, dtype=complex)
    for i, S in enumerate(order):
        rec[list(S)] = True
        if i == len(order) - 1:
            break
        G = sla.expm(-1j * tau * restrict1(h, rec)) @ G
    Wg = G @ Wm; K = Wg @ Wg.conj().T
    law1 = det_law(K, all_patterns(n))
    occ = np.array([[(s >> v) & 1 for v in range(n)] for s in states], dtype=float)
    Br = amp[:, None].copy(); leaf_bits = np.zeros((1, n)); rec = np.zeros(n, bool)
    for i, S in enumerate(order):
        S = list(S)
        newB, newbits = [], []
        for pat in itertools.product((0, 1), repeat=len(S)):
            mask = np.ones(len(states))
            for v, b in zip(S, pat):
                mask *= (occ[:, v] == b)
            newB.append(Br * mask[:, None])
            nb = leaf_bits.copy(); nb[:, S] = pat
            newbits.append(nb)
        Br = np.concatenate(newB, axis=1); leaf_bits = np.concatenate(newbits, axis=0)
        rec[S] = True
        if i == len(order) - 1:
            break
        Br = sla.expm(-1j * tau * hop_matrix(restrict1(h, rec), states, pos, n)) @ Br
    prob = (np.abs(Br) ** 2).sum(0)
    idx = (leaf_bits * (1 << np.arange(n))).sum(1).astype(int)
    law_mb = np.zeros(1 << n); np.add.at(law_mb, idx, prob)
    vec = amp.copy(); rec = np.zeros(n, bool)
    for i, S in enumerate(order):
        rec[list(S)] = True
        if i == len(order) - 1:
            break
        vec = sla.expm(-1j * tau * hop_matrix(restrict1(h, rec), states, pos, n)) @ vec
    law_inv = np.zeros(1 << n); np.add.at(law_inv, np.array(states), np.abs(vec) ** 2)
    return dict(law1=law1, law_mb=law_mb, law_inv=law_inv, leaves=Br.shape[1],
                sum_mb=float(law_mb.sum()), K2=float(np.abs(K @ K - K).max()),
                trK=float(np.real(np.trace(K))))


def orders_for(Lx, Ly, Lz, sidx):                                  # h5_manybody.py::orders_for
    ring_p = [(0, 0), (1, 0), (1, 1), (0, 1)]
    ring_m = [(0, 0), (0, 1), (1, 1), (1, 0)]
    return {"raster": [(sidx[(x, y, z)],) for x in range(Lx) for y in range(Ly) for z in range(Lz)],
            "screw+": [(sidx[(x, y, z)],) for z in range(Lz) for (x, y) in ring_p],
            "screw-": [(sidx[(x, y, z)],) for z in range(Lz) for (x, y) in ring_m],
            "slices": [tuple(sidx[(x, y, z)] for x in range(Lx) for y in range(Ly)) for z in range(Lz)]}


hb, sidxb = build_block(2, 2, 2)
ORDB = orders_for(2, 2, 2, sidxb)
mb = {}
for onm in ("raster", "screw+", "screw-", "slices"):
    mb[(onm, 0.5)] = run_case(2, 2, 2, ORDB[onm], 0.5)
mb[("screw+", 2.0)] = run_case(2, 2, 2, ORDB["screw+"], 2.0)
mb_a = run_case(2, 2, 2, ORDB["screw+"], +0.5, conj=True)
mb_b = run_case(2, 2, 2, ORDB["screw+"], -0.5)
h3, sidx3 = build_block(2, 2, 3)
ORD3 = orders_for(2, 2, 3, sidx3)
mb3 = run_case(2, 2, 3, ORD3["screw+"], 0.5)
check("E1 [1e-15] many-body: 2x2x2 (max|Im h| %.3f, dim 56), one order on 2x2x3 (dim 792); Lueders "
      "tree over all 2^V leaves, 4 orders, tau 0.5 and 2.0: vs one-particle kernel %.1e, invisible-"
      "formation formula %.1e, K^2-K %.1e; 2x2x3 %.1e"
      % (np.abs(hb.imag).max(), max(np.abs(r["law_mb"] - r["law1"]).max() for r in mb.values()),
         max(np.abs(r["law_mb"] - r["law_inv"]).max() for r in mb.values()),
         max(r["K2"] for r in mb.values()), np.abs(mb3["law_mb"] - mb3["law1"]).max()),
      max(np.abs(r["law_mb"] - r["law1"]).max() for r in mb.values()) < 1e-15
      and max(np.abs(r["law_mb"] - r["law_inv"]).max() for r in mb.values()) < 1e-15
      and max(r["K2"] for r in mb.values()) < 1e-14
      and all(abs(r["trK"] - 5.0) < 1e-12 and abs(r["sum_mb"] - 1.0) < 1e-12 for r in mb.values())
      and np.abs(mb3["law_mb"] - mb3["law1"]).max() < 1e-15 and abs(mb3["trK"] - 7.0) < 1e-12)
check("E2 [exact] T-pair many-body, 2x2x2 screw+: tree law of conj(h)+conj(state) at +0.5 = tree "
      "law of h at -0.5, %.1e; against h at +0.5 the laws differ by TV %.6f"
      % (np.abs(mb_a["law_mb"] - mb_b["law_mb"]).max(),
         0.5 * np.abs(mb[("screw+", 0.5)]["law_mb"] - mb_b["law_mb"]).sum()),
      np.abs(mb_a["law_mb"] - mb_b["law_mb"]).max() == 0.0
      and abs(0.5 * np.abs(mb[("screw+", 0.5)]["law_mb"] - mb_b["law_mb"]).sum() - 0.393394) < 1e-6)


# ==================================================== F. T4: the record-time vortex of PR #7935
I2 = np.eye(2, dtype=complex)
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)
A1, A2, A3, A4 = np.kron(S1, S1), np.kron(S1, S2), np.kron(S1, S3), np.kron(S2, I2)
B4 = A1 @ A2 @ A3 @ A4
GAM = [np.kron(s, B4) for s in (S1, S2, S3)] + [np.kron(I2, a) for a in (A1, A2, A3, A4)]
CHI8 = np.kron(I2, B4)
M_DEF, R_S, R_SPACE = 0.8, 1.0, 1.0


def chain_ops(n):                                                    # h5_vortex.py::chain_ops
    k = np.zeros((n, n), dtype=complex); lap = np.zeros((n, n), dtype=complex)
    for s_ in range(n - 1):
        k[s_, s_ + 1] += -0.5j; k[s_ + 1, s_] += 0.5j
        lap[s_, s_] += 0.5; lap[s_ + 1, s_ + 1] += 0.5; lap[s_, s_ + 1] += -0.5; lap[s_ + 1, s_] += -0.5
    lap[0, 0] += 0.5; lap[n - 1, n - 1] += 0.5
    return k, lap


def H8(n, m1, m2, p):                                                      # h5_vortex.py::H8
    k1, l1 = chain_ops(n); e = np.eye(n, dtype=complex)
    K1, K2, L = np.kron(k1, e), np.kron(e, k1), np.kron(l1, e) + np.kron(e, l1)
    w_ = R_SPACE * sum(1.0 - math.cos(x) for x in p)
    d1 = np.diag(np.asarray(m1).ravel() + w_) + R_S * L
    d2 = np.diag(np.asarray(m2).ravel())
    h = np.kron(K1, GAM[3]) + np.kron(K2, GAM[4]) + np.kron(d1, GAM[5]) + np.kron(d2, GAM[6])
    for i, pi_ in enumerate(p):
        if math.sin(pi_) != 0.0:
            h += np.kron(np.eye(n * n, dtype=complex), math.sin(pi_) * GAM[i])
    return h


def prof_vortex(n, wnd=1, mag=M_DEF):                              # h5_vortex.py::prof_vortex
    u = np.arange(n)[:, None] - (n - 1) / 2.0
    v = np.arange(n)[None, :] - (n - 1) / 2.0
    th = np.arctan2(v, u)
    return mag * np.cos(wnd * th) + 0 * u, mag * np.sin(wnd * th) + 0 * u


def internal_conj(Mx, Uu, nn):
    """U conj(M) U+ for U = I_(nn x nn) kron Uu, without building the full kron."""
    M4 = np.conj(Mx).reshape(nn, 8, nn, 8)
    X = np.tensordot(Uu, M4, axes=([1], [1]))
    return np.tensordot(X, np.conj(Uu), axes=([3], [1])).transpose(1, 0, 2, 3).reshape(8 * nn, 8 * nn)


NV = 16
PV = (0.1 * math.pi, 0.0, 0.0)
mv1, mv2 = prof_vortex(NV, +1)
HV = H8(NV, mv1, mv2, PV)
HVa = H8(NV, mv1, -mv2, PV)
NS2 = NV * NV
Cint = np.kron(S2, A2 @ A3 @ A4)
rT = float(np.abs(internal_conj(HV, Cint, NS2) - HVa).max())
monomial = all((np.abs(Cint[i]) > 1e-12).sum() == 1 for i in range(8))
wv, Uv = np.linalg.eigh(HV)
u_ = np.arange(NV)[:, None] - (NV - 1) / 2.0
v_ = np.arange(NV)[None, :] - (NV - 1) / 2.0
rr = np.hypot(u_, v_).ravel()
s1v = np.repeat(np.arange(NV), NV); s2v = np.tile(np.arange(NV), NV)
core_v = rr < 3.0
interior = (s1v >= 2) & (s1v < NV - 2) & (s2v >= 2) & (s2v < NV - 2)
edge_v = ~interior
phiv = np.mod(np.arctan2(u_, v_).ravel(), 2 * np.pi)
quadv = np.floor(4 * phiv / (2 * np.pi)).astype(int)
shell = np.maximum(np.abs(u_), np.abs(v_)).ravel()
Vint = math.cos(PV[0]) * GAM[0] + R_SPACE * math.sin(PV[0]) * GAM[5]


def site_density(vec):                                          # h5_vortex.py::site_density
    return (np.abs(vec.reshape(NS2, 8)) ** 2).sum(1)


def internal_exp(vec, Op):
    r = vec.reshape(NS2, 8)
    return float(np.real(np.einsum("ai,ij,aj->", np.conj(r), Op, r)))


light = [k for k in range(HV.shape[0]) if abs(abs(wv[k]) - math.sin(PV[0])) < 0.05]
vm = []
for k in light:
    psi = Uv[:, k]; d = site_density(psi)
    vm.append(dict(E=float(wv[k]), chi=internal_exp(psi, CHI8), core=float(d[core_v].sum()),
                   edge=float(d[edge_v].sum()), v=internal_exp(psi, Vint), psi=psi))
INT = [m for m in vm if m["E"] > 0 and m["chi"] > 0][0]
EDG = [m for m in vm if m["E"] > 0 and m["chi"] < 0][0]
check("F1 [exact] PR #7935 vortex, N 16, Cl(7), M 0.8, p (0.1pi,0,0), dim 2048, sea 1024: anti-"
      "vortex = C conj(H) C+, site-indep C = s2 x a2a3a4, %.1e, monomial %s; light modes |E| %.6f, "
      "CHI %+.0f core %.3f, %+.0f edge %.3f, both +x, v %+.4f"
      % (rT, monomial, math.sin(PV[0]), INT["chi"], INT["core"], EDG["chi"], EDG["edge"], INT["v"]),
      rT == 0.0 and monomial and int((wv < 0).sum()) == 1024 and abs(INT["chi"] - 1) < 1e-5
      and abs(EDG["chi"] + 1) < 1e-5 and abs(INT["core"] - 0.965) < 1e-3 and abs(EDG["edge"] - 0.991) < 1e-3
      and abs(INT["v"] - 0.9511) < 1e-4 and abs(EDG["v"] - 0.9511) < 1e-4)

HVsp = sp.csr_matrix(HV)
HVasp = sp.csr_matrix(HVa)
AV = float(np.abs(HVsp).sum(axis=1).max())


def restrict_modes(Hs_, rec_sites):                            # h5_vortex.py::restrict_modes
    keep = np.ones(Hs_.shape[0]); keep.reshape(NS2, 8)[rec_sites, :] = 0.0
    D = sp.diags(keep)
    return (D @ Hs_ @ D).tocsr()


def vsweep(Hs_, sched, tau, X):                                 # h5_vortex.py::sweep_forward
    rec = np.zeros(NS2, bool); Y = X.copy()
    for i, S in enumerate(sched):
        rec[S] = True
        if i == len(sched) - 1:
            break
        Y = expm_apply(restrict_modes(Hs_, rec), tau, Y, AV)
    return Y


def vschedule(kind, s=+1, pitch=0, direction=+1):                  # h5_vortex.py::schedule
    t = s1v.astype(float) if kind == "plane" else shell - s * pitch * (quadv + 0.5) / 4.0
    t = np.round(t * 4) / 4
    sched = [np.flatnonzero(t == tv_) for tv_ in np.unique(t)]
    return sched[::-1] if direction < 0 else sched


permS = np.zeros(NS2, int)
for a_ in range(NV):
    for b_ in range(NV):
        permS[a_ * NV + b_] = (NV - 1 - a_) * NV + b_
VSW = {"plane+": vschedule("plane")}
for pitch in (2, 4, 8):
    for s_, sn in ((+1, "+"), (-1, "-")):
        VSW["spiral%s p%d out" % (sn, pitch)] = vschedule("spiral", s_, pitch)
mir_ok = all(schedule_key([np.sort(permS[S]) for S in VSW["spiral+ p%d out" % pp]])
             == schedule_key(VSW["spiral- p%d out" % pp]) for pp in (2, 4, 8))
VR = {}
for name in VSW:
    for mn, m in (("interior", INT), ("edge", EDG)):
        taus = (0.5, 0.1, 2.0) if name == "plane+" else (0.5,)
        for t_ in taus:
            VR[(name, t_, mn)] = (site_density(vsweep(HVsp, VSW[name], t_, m["psi"][:, None])[:, 0]),
                                  site_density(vsweep(HVsp, VSW[name], -t_, m["psi"][:, None])[:, 0]))
dmax = max(abs(float(a[core_v].sum() - b[core_v].sum())) for a, b in VR.values())
dmaxe = max(abs(float(a[edge_v].sum() - b[edge_v].sum())) for a, b in VR.values())
psiT = (Cint @ np.conj(INT["psi"]).reshape(NS2, 8).T).T.reshape(8 * NS2)
eT = float(np.abs(site_density(vsweep(HVasp, VSW["plane+"], 0.5, psiT[:, None])[:, 0]) - VR[("plane+", 0.5, "interior")][1]).max())
check("F2 [1e-14] vortex registration exactly time-even: both modes, plane sweep and outward "
      "spirals p 2/4/8, both senses, tau 0.1/0.5/2.0, O(+tau) = O(-tau) to %.1e core, %.1e edge; "
      "T-partner %.1e"
      % (dmax, dmaxe, eT),
      dmax < 1e-14 and dmaxe < 1e-14 and eT < 1e-16 and mir_ok)

NC12 = 12
mc1, mc2 = prof_vortex(NC12, +1)
cert = []
for pc in ((0.1 * math.pi, 0.0, 0.0), (0.1 * math.pi, 0.06 * math.pi, 0.03 * math.pi)):
    Hc = H8(NC12, mc1, mc2, pc)
    ps = np.array([math.sin(x) for x in pc]); ps = ps / np.linalg.norm(ps)
    helint = np.kron(ps[0] * S1 + ps[1] * S2 + ps[2] * S3, np.eye(4))
    nn = NC12 * NC12
    rec = np.zeros(nn, bool); rec[: nn // 3] = True
    keep = np.ones(8 * nn); keep.reshape(nn, 8)[rec, :] = 0.0
    HcR = keep[:, None] * Hc * keep[None, :]
    hel = np.kron(np.eye(nn), helint)
    c1 = float(np.abs(Hc @ hel - hel @ Hc).max()); c2 = float(np.abs(HcR @ hel - hel @ HcR).max())
    k1, l1 = chain_ops(NC12); e = np.eye(NC12, dtype=complex)
    K1, K2, L = np.kron(k1, e), np.kron(e, k1), np.kron(l1, e) + np.kron(e, l1)
    w_ = R_SPACE * sum(1.0 - math.cos(x) for x in pc)
    D4 = (np.kron(K1, A1) + np.kron(K2, A2) + np.kron(np.diag(mc1.ravel() + w_) + R_S * L, A3)
          + np.kron(np.diag(mc2.ravel()), A4))
    spn = math.sqrt(sum(math.sin(x) ** 2 for x in pc))
    keep4 = np.ones(4 * nn); keep4.reshape(nn, 4)[rec, :] = 0.0
    res = []
    for lam in (+1, -1):
        hl = lam * spn * np.kron(np.eye(nn), B4) + D4
        hlR = keep4[:, None] * hl * keep4[None, :]
        M4a = np.conj(hl).reshape(nn, 4, nn, 4)
        M4b = np.conj(hlR).reshape(nn, 4, nn, 4)
        UU = A1 @ A4
        for M4x, tgt in ((M4a, hl), (M4b, hlR)):
            X = np.tensordot(UU, M4x, axes=([1], [1]))
            Y = np.tensordot(X, np.conj(UU), axes=([3], [1])).transpose(1, 0, 2, 3).reshape(4 * nn, 4 * nn)
            res.append(float(np.abs(Y - tgt).max()))
    wD, VD = np.linalg.eigh(D4)
    UU = A1 @ A4
    ovs = []
    for k in np.argsort(np.abs(wD))[:2]:
        ph = VD[:, k]
        uph = (UU @ np.conj(ph).reshape(nn, 4).T).T.reshape(4 * nn)
        ovs.append(abs(complex(np.vdot(ph, uph))))
    cert.append((c1, c2, max(res), min(ovs)))
check("F3 [exact] mechanism at N 12, both momenta: helicity site-diagonal, [H, hel] %.1e, [H_R, "
      "hel] %.1e; U = a1a4 gives U conj(h_lam) U+ = h_lam at %.1e full and restricted, both lam; "
      "light modes have |<phi|U conj phi>| %.4f"
      % (max(c[0] for c in cert), max(c[1] for c in cert), max(c[2] for c in cert), min(c[3] for c in cert)),
      max(c[0] for c in cert) < 1e-16 and max(c[1] for c in cert) < 1e-16
      and max(c[2] for c in cert) == 0.0 and min(c[3] for c in cert) > 1 - 1e-9)

spir = {pp: (float(VR[("spiral+ p%d out" % pp, 0.5, "interior")][0][core_v].sum()),
             float(VR[("spiral- p%d out" % pp, 0.5, "interior")][0][core_v].sum())) for pp in (2, 4, 8)}
edge_sp = (float(VR[("spiral+ p2 out", 0.5, "edge")][0][edge_v].sum()),
           float(VR[("spiral- p2 out", 0.5, "edge")][0][edge_v].sum()))
Pi = np.zeros((NS2, NS2)); Pi[permS, np.arange(NS2)] = 1.0
Hmir = np.kron(Pi, np.eye(8)) @ HV @ np.kron(Pi, np.eye(8)).T
Hm1 = H8(NV, -mv1, mv2, PV)
Uu = GAM[1] @ GAM[3]
M4 = Hmir.reshape(NS2, 8, NS2, 8)
Xc = np.tensordot(Uu, M4, axes=([1], [1]))
Hmc = np.tensordot(Xc, np.conj(Uu), axes=([3], [1])).transpose(1, 0, 2, 3).reshape(8 * NS2, 8 * NS2)
rm1 = float(np.abs(Hmc - Hm1).max()); rmv = float(np.abs(Hmc - HV).max()); rma = float(np.abs(Hmc - HVa).max())
check("F4 [1e-4] record-time mirror of the Wilson vortex = m1 -> -m1 up to G2G4 (%.1e), not the "
      "vortex (%.1f) or anti-vortex (%.1f); spiral+/spiral- core odds %.4f/%.4f, %.4f/%.4f, "
      "%.4f/%.4f at pitch 2/4/8, edge %.4f/%.4f"
      % (rm1, rmv, rma, spir[2][0], spir[2][1], spir[4][0], spir[4][1], spir[8][0], spir[8][1],
         edge_sp[0], edge_sp[1]),
      rm1 < 1e-14 and rmv > 1.0 and rma > 1.0 and abs(spir[2][0] - 0.9196) < 1e-4
      and abs(spir[2][1] - 0.9469) < 1e-4 and abs(spir[4][0] - 0.9473) < 1e-4
      and abs(spir[4][1] - 0.9605) < 1e-4 and abs(spir[8][0] - 0.8979) < 1e-4
      and abs(spir[8][1] - 0.9459) < 1e-4 and abs(edge_sp[0] - 0.9909) < 1e-4
      and abs(edge_sp[0] - edge_sp[1]) < 1e-4)
del HV, HVa, Hmir, Hmc, Hm1, Uv


# ============================================ G. T5: can a covariant rule select the sweep?
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
OPEN = 2


def group(proper_only):                                                  # h5_rules.py::group
    out = []
    for Pm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3):
                M[i, Pm[i]] = sg[i]
            d = int(round(np.linalg.det(M)))
            if proper_only and d != 1:
                continue
            out.append((M, d))
    return out


G24, G48 = group(True), group(False)


def dir_perm(M, offs=DIRS):                                           # h5_rules.py::dir_perm
    return [offs.index(tuple(int(x) for x in (M @ np.array(d)))) for d in offs]


PROFS = list(itertools.product((OPEN, 0, 1), repeat=6))


def act(M, prof):                                                          # h5_rules.py::act
    pp = dir_perm(M)
    out = [None] * 6
    for i in range(6):
        out[pp[i]] = prof[i]
    return tuple(out)


def orbits(Gr):                                                        # h5_rules.py::orbits
    seen, orbs = {}, []
    for pr in PROFS:
        if pr in seen:
            continue
        orb = set(act(M, pr) for M, d in Gr)
        for q in orb:
            seen[q] = len(orbs)
        orbs.append(orb)
    return orbs, seen


ORB24, OID24 = orbits(G24)
ORB48, OID48 = orbits(G48)
chiral = [i for i, o in enumerate(ORB24) if len(o) != len(ORB48[OID48[next(iter(o))]])]
A_prof = (0, 1, 0, OPEN, 1, OPEN)
A_id = OID24[A_prof]
B_id = [i for i in chiral if i != A_id][0]
PW6 = 3 ** np.arange(6)
OID_ARR = np.zeros(729, dtype=int)
for pr, oi in OID24.items():
    OID_ARR[int(sum(pr[i] * PW6[i] for i in range(6)))] = oi


def burnside(offs):                                                 # h5_rules.py::burnside
    res = {}
    for nm, Gr in (("proper", G24), ("full", G48)):
        tot = 0
        for M, d in Gr:
            img = dir_perm(M, offs)
            seen = [False] * len(offs); cyc = 0
            for i in range(len(offs)):
                if seen[i]:
                    continue
                cyc += 1; j = i
                while not seen[j]:
                    seen[j] = True; j = img[j]
            tot += 3 ** cyc
        res[nm] = tot // len(Gr)
    return res


WIN = [("NN", DIRS),
       ("NN+2e", DIRS + [(2 * a_, 2 * b_, 2 * c_) for (a_, b_, c_) in DIRS]),
       ("NN+fd", DIRS + [t for t in itertools.product((-1, 0, 1), repeat=3) if sum(abs(x) for x in t) == 2]),
       ("shell", [t for t in itertools.product((-1, 0, 1), repeat=3) if any(t)])]
BW = [burnside(o) for nm, o in WIN]
check("G1 [exact] 729 profiles give %d proper and %d full orbits, so one chiral pair; Burnside: %d "
      "chiral pairs on the 12-offset window, %d on 18-offset, %d on the 26-shell, none constructed "
      "here"
      % (len(ORB24), len(ORB48), BW[1]["proper"] - BW[1]["full"], BW[2]["proper"] - BW[2]["full"],
         BW[3]["proper"] - BW[3]["full"]),
      len(ORB24) == 57 and len(ORB48) == 56 and len(chiral) == 2
      and BW[0] == {"proper": 57, "full": 56} and BW[1]["proper"] - BW[1]["full"] == 7140
      and BW[2]["proper"] - BW[2]["full"] == 7960311 and BW[3]["proper"] - BW[3]["full"] == 52932198249)


def cluster(L):                                                       # h5_rules.py::cluster
    sites = [(x, y, z) for x in range(L[0]) for y in range(L[1]) for z in range(L[2])]
    idx = {s: i for i, s in enumerate(sites)}
    nbr = [[idx.get((s[0] + d[0], s[1] + d[1], s[2] + d[2]), -1) for d in DIRS] for s in sites]
    centre = np.array([(l - 1) / 2 for l in L])
    return dict(L=L, sites=sites, idx=idx, nbr=np.array(nbr), V=len(sites),
                R=np.array(sites, float) - centre, centre=centre)


def step_pseudoscalar_table(C):                      # h5_rules.py::step_pseudoscalar_table
    V = C["V"]; Rr = C["R"]
    D = np.linalg.norm(Rr[:, None, :] - Rr[None, :, :], axis=2)
    det3 = np.zeros((V, V, V))
    for v in range(V):
        det3[:, :, v] = np.einsum("ui,wj,ijk,k->uw", Rr, Rr,
                                  np.array([[[int((i - j) * (j - k) * (k - i) / 2) for k in range(3)]
                                             for j in range(3)] for i in range(3)], float), Rr[v])
    E = all_patterns(V)
    tab = np.zeros((1 << V, V))
    for v in range(V):
        Av = det3[:, :, v] * (D[:, v][:, None] < D[:, v][None, :])
        tab[:, v] = ((E @ Av) * E).sum(1)
    return tab


def dp_count(C, allow0, allow1, ftab):                               # h5_rules.py::dp_count
    V = C["V"]
    pw3 = (3 ** np.arange(V)).astype(np.int64)
    cnt = np.zeros(int(3 ** V), dtype=np.int64)
    xis = np.zeros(int(3 ** V))
    cnt[0] = 1
    cur = np.zeros(1, dtype=np.int64)
    dead = 0
    pw2 = (1 << np.arange(V)).astype(np.int64)
    for lev in range(V):
        digits = (cur[:, None] // pw3[None, :]) % 3
        ext = np.concatenate([digits, np.zeros((len(cur), 1), dtype=np.int64)], axis=1)
        mint = ((digits > 0) * pw2).sum(1)
        c0, x0 = cnt[cur], xis[cur]
        moved = np.zeros(len(cur), dtype=bool)
        nxt = []
        for v in range(V):
            free = digits[:, v] == 0
            if not free.any():
                continue
            nb = ext[:, C["nbr"][v]]
            code = (np.where(nb == 0, 2, nb - 1) * PW6).sum(1)
            orb = OID_ARR[code]
            f = ftab[mint, v]
            for a_, allow in ((0, allow0), (1, allow1)):
                sel = free & allow[orb]
                if not sel.any():
                    continue
                moved |= sel
                tgt = cur[sel] + (a_ + 1) * pw3[v]
                cnt[tgt] += c0[sel]
                xis[tgt] += x0[sel] + c0[sel] * f[sel]
                nxt.append(tgt)
        dead += int(c0[~moved].sum())
        cur = np.unique(np.concatenate(nxt)) if nxt else np.zeros(0, dtype=np.int64)
        if len(cur) == 0:
            break
    total = int(cnt[cur].sum()) if len(cur) else 0
    xi = float(xis[cur].sum()) if len(cur) else float("nan")
    return total, dead, (xi / total if total else float("nan")), cnt, cur


def final_law_asym(C, cnt, fin):                              # h5_rules.py::final_law_asym
    V = C["V"]
    pw3 = (3 ** np.arange(V)).astype(np.int64)
    total = int(cnt[fin].sum())
    digits = (fin[:, None] // pw3[None, :]) % 3
    out = []
    for M, d in G48:
        if d != -1:
            continue
        perm, ok = [], True
        for s_ in C["sites"]:
            img = M @ (np.array(s_) - C["centre"]) + C["centre"]
            t = tuple(int(round(x)) for x in img)
            if t not in C["idx"] or np.abs(img - np.array(t)).max() > 1e-9:
                ok = False; break
            perm.append(C["idx"][t])
        if not ok:
            continue
        pm = np.array(perm)
        img_cfg = (digits * pw3[pm]).sum(1)
        out.append(0.5 * float(np.abs(cnt[fin].astype(float) - cnt[img_cfg].astype(float)).sum()) / total)
    return out


def screw_orders(C):                                            # h5_rules.py::screw_orders
    L = C["L"]
    rp = [(0, 0), (1, 0), (1, 1), (0, 1)]
    rm = [(0, 0), (0, 1), (1, 1), (1, 0)]
    return ([C["idx"][(x, y, z)] for z in range(L[2]) for (x, y) in rp],
            [C["idx"][(x, y, z)] for z in range(L[2]) for (x, y) in rm])


def xi_of_order(order, ftab):                                    # h5_rules.py::xi_of_order
    m, tot = 0, 0.0
    for v in order:
        tot += ftab[m, v]; m |= 1 << v
    return tot


def menus_of(assign):                                          # h5_rules.py::rule_menus
    a0 = np.ones(len(ORB24), dtype=bool)
    a1 = np.ones(len(ORB24), dtype=bool)
    for i, menu in assign.items():
        a0[i] = 0 in menu
        a1[i] = 1 in menu
    return a0, a1


def r3(nrec_max):                                                           # h5_rules.py::r3
    d = {}
    for i, o in enumerate(ORB24):
        pr = next(iter(o))
        if sum(1 for x in pr if x != OPEN) > nrec_max and i != A_id:
            d[i] = ()
    return d


RULES = [("R0", {}), ("R1", {A_id: (0,), B_id: (1,)}), ("R2", {B_id: ()}), ("R2m", {A_id: ()}),
         ("R3", r3(2)), ("R3m", {**{k: v for k, v in r3(2).items() if k != B_id}, A_id: ()}),
         ("R4", {**r3(2), A_id: ()})]


def order_completions(C, a0, a1, order):                       # h5_rules.py::admissible_count
    V = C["V"]
    vals = ((np.arange(1 << V)[:, None] >> np.arange(V)[None, :]) & 1)
    cfg = np.zeros((1 << V, V), dtype=np.int64)
    alive = np.ones(1 << V, dtype=bool)
    for j, v in enumerate(order):
        ext = np.concatenate([cfg, np.zeros((1 << V, 1), dtype=np.int64)], axis=1)
        nb = ext[:, C["nbr"][v]]
        orb = OID_ARR[(np.where(nb == 0, 2, nb - 1) * PW6).sum(1)]
        a = vals[:, j]
        alive &= np.where(a == 0, a0[orb], a1[orb])
        cfg[:, v] = a + 1
    return int(alive.sum())


RES = {}
for L in ((2, 2, 2), (2, 2, 3)):
    C = cluster(L)
    ftab = step_pseudoscalar_table(C)
    sp_, sm_ = screw_orders(C)
    RES[L] = dict(xi=(xi_of_order(sp_, ftab), xi_of_order(sm_, ftab),
                      xi_of_order(list(range(C["V"])), ftab)), rules={}, C=C, ftab=ftab,
                  orders=(sp_, sm_, list(range(C["V"]))))
    for rname, assign in RULES:
        if L == (2, 2, 3) and rname in ("R2m", "R3m"):
            continue
        a0, a1 = menus_of(assign)
        total, dead, xim, cnt, fin = dp_count(C, a0, a1, ftab)
        asym = max(final_law_asym(C, cnt, fin)) if total else float("nan")
        RES[L]["rules"][rname] = (total, dead, xim, asym)
    RES[L]["r5"] = {rn: tuple(order_completions(C, *menus_of(dict(RULES)[rn]), o) for o in RES[L]["orders"])
                    for rn in ("R2", "R3", "R3m")}

cu, sl = RES[(2, 2, 2)], RES[(2, 2, 3)]
check("G2 [exact] cube 2x2x2, 6561 cfgs, Xi(screw+/-/raster) %+.1f/%+.1f/%+.1f: R0/R1/R2/R2m each "
      "give %d complete paths = 8! x 2^8, 0 dead, mean Xi %+.3e, asymmetry %.0e; R3/R3m/R4 give 0 "
      "complete, %d dead"
      % (cu["xi"][0], cu["xi"][1], cu["xi"][2], cu["rules"]["R0"][0], cu["rules"]["R1"][2],
         cu["rules"]["R1"][3], cu["rules"]["R3"][1]),
      abs(cu["xi"][0] - 1.0) < 1e-12 and abs(cu["xi"][1] + 1.0) < 1e-12 and abs(cu["xi"][2]) < 1e-12
      and all(cu["rules"][r][0] == 10321920 and cu["rules"][r][1] == 0 and abs(cu["rules"][r][2]) < 1e-12
              and cu["rules"][r][3] < 1e-12 for r in ("R0", "R1", "R2", "R2m"))
      and all(cu["rules"][r][0] == 0 and cu["rules"][r][1] == 1636608 for r in ("R3", "R3m", "R4")))

check("G3 [exact] slab 2x2x3, 531441 cfgs, Xi(screw+/-) %+.1f/%+.1f: R0 %d = 12! x 2^12, 0 dead; "
      "R1, R2 %d; R3 %d with %d dead; R4 0; mean Xi %+.3e for all; mirror asymmetry %.0e, %.3e, "
      "%.3e"
      % (sl["xi"][0], sl["xi"][1], sl["rules"]["R0"][0], sl["rules"]["R1"][0], sl["rules"]["R3"][0],
         sl["rules"]["R3"][1], max(abs(sl["rules"][r][2]) for r in ("R0", "R1", "R2", "R3")),
         sl["rules"]["R0"][3], sl["rules"]["R1"][3], sl["rules"]["R3"][3]),
      abs(sl["xi"][0] - 6.0) < 1e-12 and abs(sl["xi"][1] + 6.0) < 1e-12
      and sl["rules"]["R0"][0] == 1961990553600 and sl["rules"]["R0"][1] == 0
      and sl["rules"]["R1"][0] == 1771922718720 and sl["rules"]["R2"][0] == 1771922718720
      and sl["rules"]["R2"][1] == 39063306240 and sl["rules"]["R3"][0] == 1405870080
      and sl["rules"]["R3"][1] == 19345547712 and sl["rules"]["R4"][0] == 0
      and max(abs(sl["rules"][r][2]) for r in ("R0", "R1", "R2", "R3")) < 1e-12
      and sl["rules"]["R0"][3] < 1e-12 and abs(sl["rules"]["R1"][3] - 6.845e-2) < 1e-5
      and abs(sl["rules"]["R3"][3] - 5.154e-1) < 1e-4)

check("G4 [exact] under R2 all %d value assignments complete screw+, screw- and raster alike on the"
      " slab, all %d on the cube; under R3/R3m none completes any, %s"
      % (sl["r5"]["R2"][0], cu["r5"]["R2"][0],
         "%d/%d/%d and %d/%d/%d" % (sl["r5"]["R3"] + sl["r5"]["R3m"])),
      sl["r5"]["R2"] == (4096, 4096, 4096) and cu["r5"]["R2"] == (256, 256, 256)
      and sl["r5"]["R3"] == (0, 0, 0) and sl["r5"]["R3m"] == (0, 0, 0))


def census(offs):                                                      # h5_rules2.py::census
    n = len(offs)
    perms = [dir_perm(M, offs) for M, d in G24]
    pinv = dir_perm(-np.eye(3, dtype=int), offs)
    pw = 3 ** np.arange(n)
    allp = ((np.arange(3 ** n)[:, None] // pw[None, :]) % 3).astype(np.int8)

    def canon(arr):
        best = None
        for pp in perms:
            img = np.empty_like(arr); img[:, pp] = arr
            code = (img.astype(np.int64) * pw).sum(1)
            best = code if best is None else np.minimum(best, code)
        return best
    reps = np.unique(canon(allp))
    rep_arr = ((reps[:, None] // pw[None, :]) % 3).astype(np.int8)
    img = np.empty_like(rep_arr); img[:, pinv] = rep_arr
    can_sigma = canon(img)
    F = rep_arr.copy(); F[F == 0] = 9; F[F == 1] = 0; F[F == 9] = 1
    can_F = canon(F)
    ch = can_sigma != reps
    return len(reps), int(ch.sum()), int((ch & (can_F == reps)).sum()), int((ch & (can_F != reps) & (can_F != can_sigma)).sum())


cen6 = census(DIRS)
cen12 = census(DIRS + [(2 * a_, 2 * b_, 2 * c_) for (a_, b_, c_) in DIRS])
counts = {"A": 0, "B": 0, "achiral": 0}
pair_ok = True
for ax, ay, ap, am in itertools.product((0, 1), repeat=4):
    o = OID24[(ax, OPEN, ay, OPEN, ap, am)]
    oz = OID24[(ax, OPEN, ay, OPEN, am, ap)]
    counts["A" if o == A_id else ("B" if o == B_id else "achiral")] += 1
    if (o == A_id and oz != B_id) or (o == B_id and oz != A_id):
        pair_ok = False
check("G5 [exact] value flip fixes A and B (%d of %d chiral orbits at NN); slab middle-corner "
      "combinations split %s, z-pair reversal maps A to B at every one (%s); 12-offset: %d orbits, "
      "%d chiral, %d F-fixed, %d moved"
      % (cen6[2], cen6[1], "A %d, B %d, achiral %d" % (counts["A"], counts["B"], counts["achiral"]),
         pair_ok, cen12[0], cen12[1], cen12[2], cen12[3]),
      cen6 == (57, 2, 2, 0) and cen12[0] == 23355 and cen12[1] == 14280 and cen12[2] == 128
      and cen12[3] == 14144 and counts == {"A": 2, "B": 2, "achiral": 12} and pair_ok)

print("SUMMARY: a directed sweep separates a mover from its T-partner at order one and is blind to "
      "screw sense.  [%.1f s]" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
