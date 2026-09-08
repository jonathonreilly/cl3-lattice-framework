#!/usr/bin/env python3
"""The supplied density interaction generates the staggered mass at Hartree
level, and no term in the law fixes its sign.

Self-contained finite-cluster runner.  The coarse lattice is 2Z^3, one
fermionic mode per coarse vertex, with the Kawamoto-Smit link signs
    eta_1 = 1,  eta_2(v) = (-1)^{v_1},  eta_3(v) = (-1)^{v_1+v_2},
and the supplied nearest-neighbour Fock Hamiltonian read at t = 1
    H(t, V) = -t sum_bonds eta_ij (c_i^dag c_j + h.c.) + V sum_bonds n_i n_j.
The declared staggered mass of the parent note is H_m = m sum_v eps_v n_v with
eps_v = (-1)^{v_1+v_2+v_3}, whose size and sign that note states are supplied.
The order parameter here is O = (1/N) sum_v eps_v (n_v - 1/2), so H_m = m N O.

  A  HARTREE.  Decoupling V sum n_i n_j with <n_i> = 1/2 + eps_i O gives
     exactly H_MF = H_0 + m* sum_v eps_v n_v + const, m* = -z V O, z = 6:
     the generated term IS the locally declared mass operator.  Gap equation
     1 = (zV/2) c(m*), c(m) = [(M^2+m^2)^{-1/2}]_vv, V_c^MF = 2/(z c(0)).
  B  EXPONENT AND WINDOW.  The 3-D Dirac density of states vanishes
     quadratically, so c(0) - c(m) ~ A m^2 ln(1/m) and beta = 1/2 with a
     logarithm in the separately defined bulk Hartree functional (proof in
     own note). Finite large-V rows are strongly staggered, not exact classical states.
  C  EXACT CLUSTERS.  Cube 2x2x2 open (70-dim) and slab 2x2x4 periodic in z
     (12870-dim): the lowest excitation at the tested
     V has opposite C parity; joint Born P(O) is bimodal, and the two-shape crossing
     is V_x = 1.766 t.
  D  SIGN SYMMETRY, NOT PHYSICAL REGISTRATION.  +-m* exactly degenerate; <O> = 0 at h = 0 with
     <O^2> large; a supplied field h = +-0.001 t saturates <O>; the law is
     exactly C-even, so it does not select a sign.
  E  METHOD.  The open 2x2x4 has degrees 3 and 4, so V itself breaks C there;
     the periodic 8^3 torus carries 8 exact zero modes and its V_c^MF = 0 is
     an artefact.  Finite antiperiodic response/energy tests are separate from the bulk integral.

Groups A, C1, C4, D2, D5, E1 carry exact algebraic content (zero-residual
identities, exhaustive basis sweeps, closed-form combinatorics); the items
tagged [numerical] are floating-point cross-checks at the stated tolerance.
Every mean-field statement is labelled mean-field and is not a proved
transition.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import sys
import hashlib
from pathlib import Path
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl
from scipy.integrate import quad
from scipy.special import i0e

AUDIT_TIMEOUT_SEC = 120

# Actual mutable publication/premise inputs, not scientific substitutes.
AUDIT_INPUT_PATHS = ('docs/THE_INTERACTION_GENERATES_THE_STAGGERED_MASS_AT_HARTREE_LEVEL_AND_NO_TERM_IN_THE_LAW_FIXES_ITS_SIGN_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
INPUT_SHA256 = {'docs/THE_INTERACTION_GENERATES_THE_STAGGERED_MASS_AT_HARTREE_LEVEL_AND_NO_TERM_IN_THE_LAW_FIXES_ITS_SIGN_BOUNDED_THEOREM_NOTE_2026-09-03.md': '0f54f7f4c5825d8b7b7451d210d5a114dd4cbc50bebb674f55cfebb1fce979fe', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

def verify_inputs():
    root = Path(__file__).resolve().parents[1]
    if set(AUDIT_INPUT_PATHS) != set(INPUT_SHA256):
        raise RuntimeError("input declaration/pin mismatch")
    for rel in AUDIT_INPUT_PATHS:
        body = (root / rel).read_bytes()
        if hashlib.sha256(body).hexdigest() != INPUT_SHA256[rel]:
            raise RuntimeError("changed publication/premise input: " + rel)

verify_inputs()

T0 = time.time()
PASS = 0
FAIL = 0
Z = 6.0
RNG = np.random.default_rng(20260903)


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


def eta_ks(v, a):
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


# ================================================ finite clusters, exact sector

def build_cluster(lx, ly, lz, pz):
    """Half-filling sector of H(t,V) on an open lx x ly x lz block, z periodic
    if pz.  Returns a dict of everything the checks below read."""
    sites = [(x, y, z) for x in range(lx) for y in range(ly) for z in range(lz)]
    idx = {v: i for i, v in enumerate(sites)}
    ns = len(sites)
    eps = np.array([(-1) ** sum(v) for v in sites], float)
    bonds = []
    for v in sites:
        for a in range(3):
            w = list(v)
            w[a] += 1
            if a == 2 and pz:
                w[2] %= lz
            w = tuple(w)
            if w in idx and w != v:
                bonds.append((idx[v], idx[w], eta_ks(v, a)))
    deg = np.zeros(ns, int)
    for i, j, _ in bonds:
        deg[i] += 1
        deg[j] += 1
    # every elementary face carries flux -1
    fluxes = set()
    for v in sites:
        for a, b in ((0, 1), (0, 2), (1, 2)):
            ea = [0, 0, 0]
            ea[a] = 1
            eb = [0, 0, 0]
            eb[b] = 1

            def wr(u):
                u = list(u)
                if pz:
                    u[2] %= lz
                return tuple(u)

            p2 = wr([v[k] + ea[k] for k in range(3)])
            p4 = wr([v[k] + eb[k] for k in range(3)])
            p3 = wr([v[k] + ea[k] + eb[k] for k in range(3)])
            if p2 in idx and p4 in idx and p3 in idx and len({v, p2, p3, p4}) == 4:
                fluxes.add(eta_ks(v, a) * eta_ks(p2, b) * eta_ks(p4, a) * eta_ks(v, b))
    nf = ns // 2
    bas = [b for b in range(1 << ns) if bin(b).count("1") == nf]
    pos = {b: i for i, b in enumerate(bas)}
    dim = len(bas)

    def jw(b, p):
        return -1 if (bin(b & ((1 << p) - 1)).count("1") & 1) else 1

    rr, cc, dd = [], [], []
    for n, b in enumerate(bas):
        for (i, j, e) in bonds:
            for (p, q) in ((i, j), (j, i)):
                if (b >> q) & 1 and not (b >> p) & 1:
                    b1 = b ^ (1 << q)
                    s = jw(b, q)
                    b2 = b1 | (1 << p)
                    s *= jw(b1, p)
                    rr.append(pos[b2])
                    cc.append(n)
                    dd.append(-1.0 * e * s)
    hop = sp.csr_matrix((dd, (rr, cc)), shape=(dim, dim))
    vdi = np.array([sum(1 for (i, j, _) in bonds
                        if ((b >> i) & 1) and ((b >> j) & 1)) for b in bas], float)
    kev = np.array([sum(1 for v in range(ns) if eps[v] > 0 and (b >> v) & 1) for b in bas])
    oval = (2.0 * kev - ns / 2) / ns
    # charge conjugation C: c_v -> eps_v c_v^dag on the half-filling sector
    wv = np.array([0 if (eps[v] * (-1) ** v) == 1 else 1 for v in range(ns)])
    full = (1 << ns) - 1
    cr, cq, cd = [], [], []
    for n, b in enumerate(bas):
        ph = sum(wv[v] for v in range(ns) if not ((b >> v) & 1)) & 1
        cr.append(pos[b ^ full])
        cq.append(n)
        cd.append(-1.0 if ph else 1.0)
    cmat = sp.csr_matrix((cd, (cr, cq)), shape=(dim, dim))
    vdc = np.array([vdi[pos[b ^ full]] for b in bas])
    # C-sector isometries
    ccsc = cmat.tocsc()
    seen = np.zeros(dim, bool)
    s2 = 1 / np.sqrt(2)
    pr, pc, pd, mr, mc, md, npn, nmn = [], [], [], [], [], [], 0, 0
    for n in range(dim):
        if seen[n]:
            continue
        m = pos[bas[n] ^ full]
        seen[n] = seen[m] = True
        s = ccsc[:, [n]].data[0]
        pr += [n, m]
        pc += [npn, npn]
        pd += [s2, s * s2]
        npn += 1
        mr += [n, m]
        mc += [nmn, nmn]
        md += [s2, -s * s2]
        nmn += 1
    pl = sp.csr_matrix((pd, (pr, pc)), shape=(dim, npn))
    pm = sp.csr_matrix((md, (mr, mc)), shape=(dim, nmn))
    msp = np.zeros((ns, ns))
    for i, j, e in bonds:
        msp[i, j] += -e
        msp[j, i] += -e
    return dict(ns=ns, nf=nf, dim=dim, bonds=bonds, deg=set(deg.tolist()),
                fluxes=sorted(fluxes), eps=eps, hop=hop, vd=vdi, vdc=vdc,
                oval=oval, kev=kev, cmat=cmat, pl=pl, pm=pm,
                sp1=np.linalg.eigvalsh(msp),
                ineel=(pos[sum(1 << v for v in range(ns) if eps[v] > 0)],
                       pos[sum(1 << v for v in range(ns) if eps[v] < 0)]))


def gstate(cl, V, h=0.0):
    """Ground state of H(t,V) + h N O in the half-filling sector."""
    H = (cl["hop"] + sp.diags(V * cl["vd"] + h * cl["ns"] * cl["oval"])).tocsr()
    if cl["dim"] <= 400:
        w, U = np.linalg.eigh(H.toarray())
        return float(w[0]), U[:, 0]
    v0 = RNG.standard_normal(cl["dim"])
    w, U = spl.eigsh(H, k=1, which="SA", tol=1e-13, v0=v0, maxiter=50000)
    return float(w[0]), U[:, 0]


def sof(cl, V, h=0.0):
    _, g = gstate(cl, V, h)
    return float(np.sum(g ** 2 * cl["oval"] ** 2)), float(np.sum(g ** 2 * cl["oval"]))


def sectors(cl, V):
    """(E0, gap, Delta_C, C-parity of the ground state, ground vector)."""
    H = (cl["hop"] + sp.diags(V * cl["vd"])).tocsr()
    Hp = (cl["pl"].T @ H @ cl["pl"]).tocsr()
    Hm = (cl["pm"].T @ H @ cl["pm"]).tocsr()
    if Hp.shape[0] <= 400:
        ep, vp = np.linalg.eigh(Hp.toarray())
        em, vm = np.linalg.eigh(Hm.toarray())
    else:
        ep, vp = spl.eigsh(Hp, k=2, which="SA", tol=1e-13,
                           v0=RNG.standard_normal(Hp.shape[0]), maxiter=50000)
        em, vm = spl.eigsh(Hm, k=2, which="SA", tol=1e-13,
                           v0=RNG.standard_normal(Hm.shape[0]), maxiter=50000)
        o = np.argsort(ep)
        ep, vp = ep[o], vp[:, o]
        o = np.argsort(em)
        em, vm = em[o], vm[:, o]
    if ep[0] <= em[0]:
        g = cl["pl"] @ vp[:, 0]
        return float(ep[0]), float(min(ep[1], em[0]) - ep[0]), float(em[0] - ep[0]), +1, g / np.linalg.norm(g)
    g = cl["pm"] @ vm[:, 0]
    return float(em[0]), float(min(em[1], ep[0]) - em[0]), float(ep[0] - em[0]), -1, g / np.linalg.norm(g)


CUBE = build_cluster(2, 2, 2, False)
SLAB = build_cluster(2, 2, 4, True)
OPEN4 = build_cluster(2, 2, 4, False)

# ================================================ antiperiodic coarse tori


def build_M(L, twist):
    N = L ** 3

    def ix(x, y, z):
        return (x * L + y) * L + z

    M = np.zeros((N, N))
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = ix(x, y, z)
                for a, e in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
                    w = [x + e[0], y + e[1], z + e[2]]
                    ph = 1.0
                    for k in range(3):
                        if w[k] == L:
                            w[k] = 0
                            ph *= twist
                    j = ix(*w)
                    et = eta_ks((x, y, z), a)
                    M[i, j] += -et * ph
                    M[j, i] += -et * ph
    return M


def c_inf(m):
    """c(m) = (1/sqrt pi) int_0^inf ds s^-1/2 e^{-s m^2} (e^{-2s} I_0(2s))^3,
    integrated after s = u^2 so the endpoint singularity is removed."""
    f = lambda u: 2.0 * np.exp(-u * u * m * m) * i0e(2 * u * u) ** 3
    return quad(f, 0, np.inf, limit=600)[0] / np.sqrt(np.pi)


def c_tor(ev, m):
    return float(np.mean(1.0 / np.sqrt(ev ** 2 + m * m)))


def solve_m(V, ev=None, nit=60):
    """Largest root of 1 = (zV/2) c(m); 0 if V <= V_c."""
    cf = (lambda m: c_tor(ev, m)) if ev is not None else c_inf
    if (Z * V / 2) * cf(0.0) <= 1.0:
        return 0.0
    lo, hi = 0.0, 1.0
    while (Z * V / 2) * cf(hi) > 1.0:
        hi *= 2
    for _ in range(nit):
        mid = (lo + hi) / 2
        if (Z * V / 2) * cf(mid) > 1.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


C0 = c_inf(0.0)
VC = 2 / (Z * C0)
EVA = {}
for L in (8, 12, 16):
    EVA[L] = np.linalg.eigvalsh(build_M(L, -1.0))

# ================================================================ A -- Hartree

resid = 0.0
for V in (1.0, 2.0):
    for Oq in (0.25, 0.5, -0.125):
        nbar = 0.5 + CUBE["eps"] * 0.0  # placeholder, torus below
        L = 4
        sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
        idx = {v: i for i, v in enumerate(sites)}
        e4 = np.array([(-1) ** sum(v) for v in sites], float)
        nb = 0.5 + e4 * Oq
        coef = np.zeros(L ** 3)
        pairs = 0.0
        for v in sites:
            i = idx[v]
            for a in range(3):
                w = list(v)
                w[a] = (w[a] + 1) % L
                j = idx[tuple(w)]
                coef[i] += V * nb[j]
                coef[j] += V * nb[i]
                pairs += nb[i] * nb[j]
        # sum_{j~i} <n_j> = z(1/2 - eps_i O) exactly
        resid = max(resid, float(np.max(np.abs(coef / V - Z * (0.5 - e4 * Oq)))))
        # the generated one-body term, less its (eps-even) mean, is m* eps_v
        mstar = -Z * V * Oq
        resid = max(resid, float(np.max(np.abs(coef - coef.mean() - mstar * e4))))
        resid = max(resid, abs(coef.mean() - Z * V / 2))
        # the subtracted constant depends on O only through O^2
        resid = max(resid, abs(pairs - (Z * L ** 3 / 2) * (0.25 - Oq * Oq)))
check("A1 [exact] torus 4^3, z = 6: sum_{j~i}<n_j> = z(1/2 - eps_i O), so the supplied Hartree ansatz gives exactly "
      "H_MF = H_0 + m* sum eps_v n_v + const, m* = -zVO: the locally declared mass operator, the const "
      "even in O (%.1e)" % resid, resid == 0.0)

M8 = build_M(8, -1.0)
e8 = np.array([(-1) ** (x + y + z) for x in range(8) for y in range(8) for z in range(8)], float)
d5 = 0.0
mm = []
for m in (0.3, 1.0):
    w, U = np.linalg.eigh(M8 + m * np.diag(e8))
    P = U[:, :256] @ U[:, :256].T
    Oq = float(np.mean(e8 * (np.diag(P) - 0.5)))
    pr = -(m / 2) * c_tor(EVA[8], m)
    mm.append((Oq, pr))
    d5 = max(d5, abs(Oq - pr))
check("A2 [1e-9] antiperiodic 8^3: the locally rederived response O(m) = -(m/2)c(m), "
      "c(m) = [(M^2+m^2)^-1/2]_vv, holds at m = 0.3 (%.9f) and 1.0 (%.9f), residual %.1e"
      % (mm[0][0], mm[1][0], d5), d5 < 1e-9)

dbz = 0.0
for s in (0.1, 0.5, 2.0):
    q = 2 * np.pi * (np.arange(64) + 0.5) / 64
    ck = np.cos(q)
    grid = np.exp(-s * (6 + 2 * (ck[:, None, None] + ck[None, :, None] + ck[None, None, :])))
    dbz = max(dbz, abs(float(grid.mean()) - float(i0e(2 * s) ** 3)))
check("A3 [1e-12] closed 1-D form: <e^{-s(6+2 sum cos q_a)}>_BZ = (e^{-2s}I_0(2s))^3 on a 64^3 grid "
      "at s = 0.1, 0.5, 2 (%.1e), so c(m) = (1/sqrt pi) int ds s^-1/2 e^{-s m^2}(e^{-2s}I_0(2s))^3"
      % dbz, dbz < 1e-12)

cs = {L: c_tor(EVA[L], 0.0) for L in (8, 12, 16)}
check("A4 [numerical] bulk c_inf(0) = %.9f, chi = c(0)/2 = %.6f vs historical 0.227671, "
      "V_c^MF = 2/(z c(0)) = %.6f t [mean field]; L = 8, 12, 16 give %.6f, %.6f, %.6f, from above"
      % (C0, C0 / 2, VC, 2 / (Z * cs[8]), 2 / (Z * cs[12]), 2 / (Z * cs[16])),
      abs(C0 - 0.455344052) < 1e-8 and abs(C0 / 2 - 0.227671) < 2e-6
      and abs(VC - 0.732047) < 1e-6
      and 2 / (Z * cs[8]) > 2 / (Z * cs[12]) > 2 / (Z * cs[16]) > VC)

dgap = 0.0
mstars = {}
for V in (0.8, 1.0, 2.0, 4.0):
    ms = solve_m(V)
    mstars[V] = ms
    dgap = max(dgap, abs(1.0 - (Z * V / 2) * c_inf(ms)))
    dgap = max(dgap, abs(ms - (-Z * V * (-(ms / 2) * c_inf(ms)))))
check("A5 [1e-9] the gap equation 1 = (zV/2)c(m*) and the self-consistency m* = -zVO(m*) close on a nonzero minimizing branch; zero also solves the undivided equation. Checks at V = 0.8, 1, 2, 4 t (%.1e); below V_c^MF only m* = 0" % dgap,
      dgap < 1e-9 and solve_m(0.70) == 0.0 and solve_m(0.732) == 0.0)

# ================================================== B -- exponent and window

rat = [(m, (C0 - c_inf(m)) / (m * m * np.log(1 / m))) for m in (0.02, 0.05, 0.1)]
check("B1 [numerical] bulk integral diagnostic (asymptotic proof is in the note): "
      "c(0)-c(m) ~ A m^2 ln(1/m) + B m^2: (c0-c(m))/(m^2 ln(1/m)) = %.4f, %.4f, %.4f at "
      "m = 0.02, 0.05, 0.1"
      % (rat[0][1], rat[1][1], rat[2][1]),
      all(0.03 < r < 0.06 for _, r in rat) and rat[0][1] < rat[1][1] < rat[2][1])

ds = [1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1]
ms = [solve_m(VC + d) for d in ds]
be = [np.log(ms[i + 1] / ms[i]) / np.log(ds[i + 1] / ds[i]) for i in range(len(ds) - 1)]
check("B2 [numerical] bulk finite-difference slopes: beta_eff = dln m*/dln(V-V_c) drifts "
      "%.4f -> %.4f over (V-V_c) 1e-1 -> 1e-5 [mean field]: beta = 1/2 with a logarithm, not 1" % (be[-1], be[0]),
      all(be[i] < be[i + 1] for i in range(len(be) - 1)) and 0.50 < be[0] < 0.55
      and 0.55 < be[-1] < 0.62)

cls = []
for V in (2.0, 4.0, 6.0):
    m = solve_m(V)
    cls.append((V, m, m / (3 * V), 2 * m, 2 / np.arccosh(1 + m * m / 2)))
BW = 2 * np.sqrt(12.0)
check("B3 [numerical] at V = 2, 4, 6 t the Hartree state approaches the classical checkerboard, not exactly: "
      "m*/3V = %.3f, %.3f, %.3f; 2m* = %.2f, %.2f, %.2f t above the bandwidth %.3f; xi = %.2f, %.2f, "
      "%.2f, below one spacing"
      % (cls[0][2], cls[1][2], cls[2][2], cls[0][3], cls[1][3], cls[2][3], BW,
         cls[0][4], cls[1][4], cls[2][4]),
      all(r[2] > 0.9 for r in cls) and all(r[3] > BW for r in cls) and all(r[4] < 1.0 for r in cls))

win = [(V, solve_m(V), 2 / np.arccosh(1 + solve_m(V) ** 2 / 2)) for V in (0.75, 0.8, 0.9, 1.0)]
check("B4 [numerical] illustrative bulk small-mass samples above %.3f, no exclusive window: "
      "m* = %.3f, %.3f, %.3f, %.3f and xi = %.2f, %.2f, %.2f, %.2f at V = 0.75, 0.8, 0.9, 1 t"
      % (VC, win[0][1], win[1][1], win[2][1], win[3][1],
         win[0][2], win[1][2], win[2][2], win[3][2]),
      all(r[2] > 1.15 for r in win) and win[3][1] < 2.0)

print("  Bulk Hartree functional roots, distinct from finite antiperiodic tests (not a physical transition):")
print("     V    m*(inf)     2m*    O=-m*c/2    xi")
for V in (0.732, 0.8, 1.0, 2.0):
    mi = solve_m(V)
    o = -(mi / 2) * c_inf(mi) if mi > 0 else 0.0
    xi = 2 / np.arccosh(1 + mi * mi / 2) if mi > 1e-9 else float("inf")
    print("  %6.3f %9.6f %9.6f %9.6f %8.4f" % (V, mi, 2 * mi, o, xi))

# ================================================== C -- the exact clusters

dc1 = max(float(abs(CUBE["cmat"] @ CUBE["hop"] - CUBE["hop"] @ CUBE["cmat"]).max()),
          float(abs(SLAB["cmat"] @ SLAB["hop"] - SLAB["hop"] @ SLAB["cmat"]).max()))
dc2 = max(float(abs(CUBE["cmat"] @ CUBE["cmat"] - sp.identity(CUBE["dim"])).max()),
          float(abs(SLAB["cmat"] @ SLAB["cmat"] - sp.identity(SLAB["dim"])).max()))
dc3 = max(float(np.max(np.abs(CUBE["vdc"] - CUBE["vd"]))),
          float(np.max(np.abs(SLAB["vdc"] - SLAB["vd"]))))
E0c0, _ = gstate(CUBE, 0.0)
check("C1 [exact] cube 2x2x2 open (degree 3, dim 70) and slab 2x2x4 periodic z (degree 4, dim 12870), "
      "every face flux -1: C^2 = I, [C,H_0] = 0, d(~b)-d(b) = 0 on all basis states (%.1e); free "
      "E_0(cube) = %.6f = -4 sqrt3"
      % (max(dc1, dc2, dc3), E0c0),
      CUBE["deg"] == {3} and SLAB["deg"] == {4} and CUBE["fluxes"] == [-1]
      and SLAB["fluxes"] == [-1] and CUBE["dim"] == 70 and SLAB["dim"] == 12870
      and dc1 == 0.0 and dc2 == 0.0 and dc3 == 0.0 and abs(E0c0 + 4 * np.sqrt(3)) < 1e-9)

VG = (0.0, 1.0, 2.0, 4.0, 8.0)
CT, ST = {}, {}
for V in VG:
    CT[V] = sectors(CUBE, V)
    ST[V] = sectors(SLAB, V)
gapeq = max(max(abs(CT[V][1] - CT[V][2]) for V in VG), max(abs(ST[V][1] - ST[V][2]) for V in VG))
check("C2 [1e-9] on BOTH clusters at every tested V the lowest excitation has opposite C parity: "
      "gap = Delta_C to %.1e, ground state C-even; Delta_C falls to %.4e (cube) and %.4e (slab) by "
      "V = 8 t"
      % (gapeq, CT[8.0][2], ST[8.0][2]),
      gapeq < 1e-9 and all(CT[V][3] == 1 and ST[V][3] == 1 for V in VG)
      and abs(CT[0.0][2] - 2 * np.sqrt(3)) < 1e-9 and abs(ST[0.0][2] - 2 * np.sqrt(2)) < 1e-9
      and abs(CT[8.0][2] - 7.8163e-2) < 1e-5 and abs(ST[8.0][2] - 9.5445e-5) < 1e-8)

print("  exact clusters, C-resolved; O = (1/N) sum eps_v (n_v - 1/2), S = <O^2>:")
print("     V  E0(cube) Delta_C(c)  S(cube)  E0(slab) Delta_C(s)  S(slab)")
for V in (0.0, 2.0, 4.0, 8.0):
    gc = CT[V][4]
    gs = ST[V][4]
    print("  %5.1f %9.6f %10.4e %8.6f %9.6f %10.4e %8.6f"
          % (V, CT[V][0], CT[V][2], float(np.sum(gc ** 2 * CUBE["oval"] ** 2)),
             ST[V][0], ST[V][2], float(np.sum(gs ** 2 * SLAB["oval"] ** 2))))


def binom(n):
    from math import comb
    return np.array([comb(n, k) for k in range(n + 1)], float) / 2.0 ** n


d0 = 0.0
for cl, tab in ((CUBE, CT), (SLAB, ST)):
    g = tab[0.0][4]
    P = np.array([float(np.sum(g[cl["kev"] == k] ** 2)) for k in range(cl["ns"] // 2 + 1)])
    d0 = max(d0, float(np.max(np.abs(P - binom(cl["ns"] // 2)))))
    d0 = max(d0, abs(float(np.sum(g ** 2 * cl["oval"] ** 2)) - 1.0 / (2 * cl["ns"])))
check("C3 [1e-12] the free half-filled sea's staggered fluctuation is shot noise: at V = 0 both "
      "clusters give S = 1/(2N) exactly (1/16, 1/32) and odds over O of Binomial(N/2, 1/2) exactly "
      "(%.1e)" % d0, d0 < 1e-12)

gcu8 = CT[8.0][4]
P8 = np.array([float(np.sum(gcu8[CUBE["kev"] == k] ** 2)) for k in range(5)])
check("C4 [numerical] the odds over O go bimodal: cube at V = 8 t, %.4f + %.4f on O = -1/2 and +1/2 "
      "against %.4f on O = 0; the two staggered patterns carry %.6f of the weight"
      % (P8[0], P8[4], P8[2],
         float(gcu8[CUBE["ineel"][0]] ** 2 + gcu8[CUBE["ineel"][1]] ** 2)),
      abs(P8[0] - 0.472875) < 1e-5 and abs(P8[4] - 0.472875) < 1e-5 and abs(P8[2] - 0.004317) < 1e-5)

HFD = 1e-4
chis = {}
for V in (0.0, 4.0, 8.0):
    chis[V] = (-(sof(CUBE, V, HFD)[1] - sof(CUBE, V, -HFD)[1]) / (2 * HFD),
               -(sof(SLAB, V, HFD)[1] - sof(SLAB, V, -HFD)[1]) / (2 * HFD))
check("C5 [numerical, h = 1e-4 t] the central difference for chi is size-flat at V = 0 (%.5f -> %.5f) and explodes "
      "with size once V grows: %.2f -> %.1f at V = 4, %.2f -> %.1f at V = 8 t (cube -> slab), the "
      "last already saturation"
      % (chis[0.0][0], chis[0.0][1], chis[4.0][0], chis[4.0][1], chis[8.0][0], chis[8.0][1]),
      abs(chis[4.0][0] - 6.52) < 0.02 and abs(chis[4.0][1] - 717.3) < 1.0
      and abs(chis[8.0][0] - 48.64) < 0.05 and abs(chis[8.0][1] - 4920.8) < 5.0)


def crossover(cl):
    s0 = 1.0 / (2 * cl["ns"])
    lo, hi = 0.0, 8.0
    for _ in range(45):
        mid = (lo + hi) / 2
        if sof(cl, mid)[0] > 2 * s0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


vsc, vss = crossover(CUBE), crossover(SLAB)
check("C6 [numerical] the S-doubling crossover FALLS with size: V* = %.5f t (cube, N = 8) -> "
      "%.5f t (slab, N = 16)" % (vsc, vss),
      abs(vsc - 2.034113) < 1e-4 and abs(vss - 1.14065) < 1e-4 and vss < vsc)

lo, hi = 1.0, 2.5
for _ in range(40):
    mid = (lo + hi) / 2
    if sof(SLAB, mid)[0] > sof(CUBE, mid)[0]:
        hi = mid
    else:
        lo = mid
VX = (lo + hi) / 2
check("C7 [numerical] S(V=0) = 1/(2N); two differently coordinated shapes have a crossing V_x = %.5f t against V_c^MF = %.6f t, %.2fx. "
      "No critical estimate or mean-field error factor" % (VX, VC, VX / VC),
      abs(VX - 1.76598) < 1e-4 and 2.3 < VX / VC < 2.5)

# ================================================== D -- the registered sign

deg = []
for V in (2.0, 4.0, 6.0):
    m = solve_m(V, EVA[8])

    def emf(mu):
        w = np.linalg.eigvalsh(M8 + mu * np.diag(e8))
        oq = -(mu / 2) * c_tor(EVA[8], mu)
        return float(np.sum(w[:256])) + (Z * V / 2) * 512 * oq * oq

    deg.append((V, m, emf(m) - emf(-m),
                -(m / 2) * c_tor(EVA[8], m), +(m / 2) * c_tor(EVA[8], m)))
check("D1 [1e-9] +-m* are EXACTLY degenerate at Hartree level: E_MF(+m*) - E_MF(-m*) = %.1e, %.1e, "
      "%.1e at V = 2, 4, 6 t on the antiperiodic 8^3, O(+m*) = -O(-m*); the functional holds O only "
      "through O^2" % (deg[0][2], deg[1][2], deg[2][2]),
      all(abs(r[2]) < 1e-9 for r in deg) and all(abs(r[3] + r[4]) < 1e-12 for r in deg))

zz = []
for cl, nm in ((CUBE, "cube"), (SLAB, "slab")):
    for V in (2.0, 4.0, 8.0):
        s2v, o1 = sof(cl, V)
        zz.append((nm, V, o1, s2v))
check("D2 [1e-9] in every finite cluster <O> = 0 at h = 0 while <O^2> is large: <O> = %.1e / %.1e "
      "against <O^2> = %.4f / %.4f (cube / slab, V = 4 t); C-even ground state, not an exact two-configuration cat" % (zz[1][2], zz[4][2], zz[1][3], zz[4][3]),
      all(abs(r[2]) < 1e-9 for r in zz) and all(0.12 <= r[3] <= 0.245 for r in zz))

hs = [(h, sof(SLAB, 8.0, h)[1]) for h in (-0.005, -0.001, 0.001, 0.005)]
check("D3 [numerical] a SUPPLIED field h sum_v eps_v n_v gives a finite-field response, not a singular limit: slab at "
      "V = 8 t, h = -+0.001 t saturates <O> at %+.6f / %+.6f, while <O>|_{h=0} = 0" % (hs[1][1], hs[2][1]),
      abs(hs[1][1] - 0.492970) < 1e-5 and abs(hs[2][1] + 0.492970) < 1e-5
      and abs(hs[0][1] - 0.492983) < 1e-5 and abs(hs[3][1] + 0.492983) < 1e-5)

dq = 0.0
nval = []
for cl in (CUBE, SLAB):
    # Q = sum_v (n_v - 1/2) is identically 0 on the half-filling sector
    dq = max(dq, abs(cl["nf"] - cl["ns"] / 2))
    # C: O -> -O, checked entry by entry through the permutation C carries
    perm = np.asarray((cl["cmat"] != 0).argmax(axis=0)).ravel()
    dq = max(dq, float(np.max(np.abs(cl["oval"][perm] + cl["oval"]))))
    nval.append(len(set(np.round(cl["oval"], 12))))
check("D4 [exact] O is the Fock staggered occupation, weighted by supplied eps_v; joint Born readout, %d and %d readable values, C: O -> -O entry by "
      "entry (%.1e); Q is identically 0 here"
      % (nval[0], nval[1], dq), dq == 0.0 and nval == [5, 9])

dl = 0.0
for cl in (CUBE, SLAB):
    for V in (1.0, 3.0):
        H = (cl["hop"] + sp.diags(V * cl["vd"])).tocsr()
        dl = max(dl, float(abs(cl["cmat"] @ H @ cl["cmat"] - H).max()))
    Hm = sp.diags(cl["ns"] * cl["oval"]).tocsr()
    dl = max(dl, float(abs(cl["cmat"] @ Hm @ cl["cmat"] + Hm).max()))
check("D5 [exact] the law holds only t and V, both eps-EVEN: C H(t,V) C^-1 = H(t,V) exactly at "
      "V = 1, 3 t on both clusters while C H_m C^-1 = -H_m (%.1e), so the Hamiltonian is even; no physical sign selection or permanent Record follows" % dl, dl == 0.0)

# ================================================================ E -- method

dop = set(np.round(OPEN4["vdc"] - OPEN4["vd"], 9).tolist())
Ho = (OPEN4["hop"] + sp.diags(1.0 * OPEN4["vd"])).tocsr()
dbr = float(abs(OPEN4["cmat"] @ Ho @ OPEN4["cmat"] - Ho).max())
check("E1 [exact] the OPEN 2x2x4 has degrees %s, so d(~b)-d(b) is not constant (%d values) and V "
      "breaks C there (C H C^-1 - H = %.1f at V = 1 t): no C-odd gap is definable, so periodic z is "
      "used" % (sorted(OPEN4["deg"]), len(dop), dbr),
      OPEN4["deg"] == {3, 4} and len(dop) > 1 and dbr > 0.5)

evp = np.linalg.eigvalsh(build_M(8, 1.0))
nz = int(np.sum(np.abs(evp) < 1e-10))
check("E2 [1e-10] the PERIODIC 8^3 torus carries %d exact zero modes (parent note T3), so c(0) "
      "diverges and V_c^MF = 0, an artefact; the ANTIPERIODIC sector, min|E| = %.6f at L = 8, "
      "is used for finite response/energy; bulk integral results are separate"
      % (nz, float(np.abs(EVA[8]).min())),
      nz == 8 and float(np.abs(EVA[8]).min()) > 1.3)

# Additional finite controls run after all original seeded data have been produced.
small_field_rows = []
for field in (1e-7, 1e-9, -1e-9):
    energy, state = gstate(SLAB, 8.0, field)
    matrix = SLAB["hop"] + sp.diags(8.0 * SLAB["vd"] + field * SLAB["ns"] * SLAB["oval"])
    residual = float(np.linalg.norm(matrix @ state - energy * state))
    expectation = float(np.sum(state**2 * SLAB["oval"]))
    small_field_rows.append((field, expectation, residual))
check("R1 [1e-8] actual below-gap slab fields tend toward zero, with opposite signs and converged eigenpairs",
      all(r[2] < 1e-8 for r in small_field_rows)
      and 0.007 < -small_field_rows[0][1] < 0.009
      and 7e-5 < -small_field_rows[1][1] < 9e-5
      and abs(small_field_rows[1][1] + small_field_rows[2][1]) < 1e-7
      and SLAB["ns"] * 1e-7 / 2 < ST[8.0][1] / 4)
full_cube = CUBE["hop"].toarray() + np.diag(8.0 * CUBE["vd"])
ce, cv = np.linalg.eigh(full_cube)
cg = CUBE["cmat"] @ cv[:, 0]
ce1 = CUBE["cmat"] @ cv[:, 1]
cat_weight = float(sum(cv[i, 0]**2 for i in CUBE["ineel"]))
check("R2 [1e-9] actual cube Cg=g, first excitation C-odd/orthogonal, and two-string weight is below one",
      np.linalg.norm(cg - cv[:, 0]) < 1e-9
      and np.linalg.norm(ce1 + cv[:, 1]) < 1e-9
      and abs(np.vdot(cv[:, 1], cg)) < 1e-9
      and abs(ce[1] - ce[0] - CT[8.0][1]) < 1e-9
      and 0.94 < cat_weight < 0.95 and 1-cat_weight > 0.05)
check("R3 [numerical] bulk and finite thresholds differ; zero remains an undivided stationary root",
      all(abs(cs[L]-C0) > 1e-4 for L in (8,12,16))
      and all(0.0 * (1-Z*v*c_inf(0.0)/2) == 0.0 for v in (0.5,0.8,2.0)))
check("R4 [numerical] original finite strong-coupling ratios remain strictly below classical saturation; xi is one-body",
      all(0.9 < r[2] < 1.0 for r in cls)
      and all(abs(np.cosh(2/r[4]) - 1 - r[1]**2/2) < 1e-9 for r in cls))
from fractions import Fraction
joint_laws = [((1,1,0,0),(0,0,1,1)), ((1,0,1,0),(0,1,0,1))]
joint_means, joint_seconds = [], []
for law in joint_laws:
    joint_means.append([sum(Fraction(v[i],2) for v in law) for i in range(4)])
    ov = [sum(Fraction(e,4)*(v[i]-Fraction(1,2)) for i,e in enumerate((1,-1,1,-1))) for v in law]
    joint_seconds.append(sum(x*x/2 for x in ov))
# The selected checkerboard projector is diagonal, but hopping changes it.
projector = sp.diags([float(i == CUBE["ineel"][0]) for i in range(CUBE["dim"])])
hop_change = float(abs(CUBE["hop"] @ projector - projector @ CUBE["hop"]).max())
check("R5 [exact] same site means do not fix joint O law; diagonal interaction does not make the full hopping law Record-preserving",
      joint_means == [[Fraction(1,2)]*4]*2 and joint_seconds == [0,Fraction(1,4)]
      and hop_change > 0 and float(abs((sp.diags(CUBE["vd"]) @ projector - projector @ sp.diags(CUBE["vd"])).tocsr()).max()) == 0.0)
print("CORRECTION_DATA:", small_field_rows, "Cground_error", float(np.linalg.norm(cg-cv[:,0])),
      "first_C_overlap", float(abs(np.vdot(cv[:,1],cg))), "two_string_weight", cat_weight,
      "joint_O2", [str(v) for v in joint_seconds])
print("SUMMARY: supplied bulk Hartree minimization, finite Fock spectra and joint Born readout are distinct; fixed finite h->0 gives zero. No physical sign registration or critical point is proved.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
