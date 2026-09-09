"""The two TT graviton polarisations are read by the axis-bond pair record statistics of the
pi-flux sea at every momentum off the coordinate planes; the shear sector is invisible to a
length-dressed nearest-neighbour hop, and exactly one period-2 coupling would read it.

CLASS A, finite-dimensional. Every object is a finite matrix on an L^3 coarse torus or a
24-element finite group; every statement is decided by exact linear algebra on it. NO random
number, NO seed, NO fitted constant, NO imported module from this repository or any branch.

PROVENANCE OF THE CODE. Self-contained: every block below is COPIED from the probe scripts of
scratchpad/G2 and each names the source function it reproduces.
  eta_ks, Lattice, twist_table  reproduce g2_lib.eta_ks / g2_lib.Lattice / g2_lib.twist_table
                    (KS signs eta_1 = 1, eta_2 = (-1)^{v1}, eta_3 = (-1)^{v1+v2}; twist[a] = 1
                    flips the bonds crossing v_a = L-1 -> 0), themselves the determinantal
                    runner's conventions (record_statistics_of_the_half_filled_sea_are_
                    determinantal_check_2026_09_03.py).
  Sea, dP_half, ent reproduce g2_lib.Sea and g2_lib.Sea.dP, the exact first-order projector
                    response dP = sum_{i occ, a emp} (|i><i|dH|a><a| + h.c.)/(eps_i - eps_a),
                    factored so that only the requested matrix elements of dP are formed.
  stats0, dstats    reproduce g2_lib.stats0 / g2_lib.dstats (site <n_v>, axis-bond and
                    face-diagonal connected pair correlators -P_uv^2 and their first variation).
  tt_basis, tensor_from_coords, coords_from_tensor  reproduce the same names in g2_lib.
  bond_fields_declared / _p2 / _curl                reproduce the same names in g2_lib.
  response_matrix, rows_at_shifts, fourier, shifts  reproduce the same names in g2_lib.
  cubic_group, decompose, perm_rep_classes, D_T2, edge_map  reproduce g2_kinematics.py.
  three_site_and_plaquette                          reproduces g2_escape.py.
  the scalar control block                          reproduces g2_response.py block S.scalar.
  the M^2 / P_fd mechanism block                    reproduces g2_checks.py block C1.

SETTING. Coarse torus L^3, L in {6, 8, 12}; pi-flux (framework vacuum) and zero-flux control;
H0 = M + m Eps, eps_v = (-1)^{v1+v2+v3}, m in {0, 1}; twist chosen by minimum half-filled energy
of M, fallback maximum gap. P = projector onto the N/2 lowest eigenvectors. Readable statistics
at a coarse site: s_v = <n_v>, axis-bond pairs C_a(v) = <n_v n_{v+a}> - <n_v><n_{v+a}> = -P_{v,v+a}^2,
face-diagonal pairs C_d(v) = -P_{v,v+d}^2. Declared dressing t_e = t (1 - beta h_e), beta = nu_r = 1,
with the endpoint-mean edge rule h_e = (h_bb(v) + h_bb(v+b))/4 on the sea's own axis bonds.
Metric polarisations: Frobenius-orthonormal E_xx, E_yy, E_zz, E_xy, E_yz, E_zx; TT basis at the
continuum k-vector k = 2 pi n / L. R(k): 80 rows (10 statistics x 8 half-reciprocal shifts) x 6
polarisations. Rank = singular values above 1e-9 of the largest.

CHECKS (T1-T7 = section 6 items (i)-(xii) of the source result).
  T1  (i)    provenance: E_sea, gaps, max|P| at separation 1 and P_vv = 1/2 on the declared tori.
  T2a (ii)   cubic content: site A1; axis-bond pairs A1+E; face-diagonal pairs A1+E+T2; h_ij A1+E+T2.
  T2b (iii)  edge-length map: axis rank 3 (h_aa/2 only), face-diagonal rank 6, h_xy from the two
             face diagonals of its plane.
  T2c (iv)   TT rank decided kinematically: det = -2 k1 k2 k3, dim(TT n T2) = 1 on the coordinate
             planes and 0 off them.
  T3a (vi)   declared dressing: T2max = 0 exactly at every momentum, torus and sea.
  T3b (vi)   TT rank 1 on coordinate-plane momenta and 2 off them, on 6^3, 8^3, 12^3; the cross
             polarisation's response column is exactly zero on the planes.
  T3c (vi)   conditioning: s_max in 0.010-0.035, flat in |k|; s_min/s_max = the kinematic ratio.
  T3d (x)    endpoint-mean zero: at k_a = pi the h_aa column vanishes and rank(R) drops to 2.
  T4  (5.2)  three-site corner and plaquette statistics: T2 response 0 at every momentum tested.
  T5  (viii) the sublattice cancellation is the site statistic's uniform part only: site@0 <= 1e-17
             for every polarisation and for the scalar at (alpha,beta) = (1,1) and (2,1), bond
             average <= 1e-17, staggered site@Q alive with mass; axis pair statistics ~2e-2.
  T6  (vii)  the pi-flux exact zero: M^2 has no face-diagonal element (0 against 2 at zero flux),
             P_fd = 0 and dC_fd = 0 with and without the record-native mass; alive at zero flux.
  T7a (ix)   leakage and covariance of the declared dressing <= 1e-16.
  T7b (v)    bond-modulation multiplicities (uniform A1+E; period-2 3A1+A2+4E+3T1+T2; face-diagonal
             A1+E+T2) and the one-dimensional intertwiner with its closed form.
  T7c (xi)   declared + period-2 coupling: rank 6, TT rank 2 at axis momenta, covariance exact, and
             the m=0 null direction is the uniform dilation.
  T7d (xii)  the O(k) curl coupling does not read the cross mode: |cos| = 1 at axis momenta.

RUNTIME. The 14^3 spot check of the source result is DROPPED to stay inside the time budget; the
k -> 0 trend is therefore quoted from 6^3, 8^3 and 12^3 only.

SUPPLIED, NOT DERIVED: the fermion law; the pi-flux half-filled sea with the KS pattern, the twist
rule and m; beta = nu_r = 1; the endpoint-mean edge rule; the pair-statistic reading of an edge
length; the polarisation conventions; and, in T7c, the existence and coefficient kappa of the
period-2 shear coupling.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300

import itertools
import sys
import time

sys.dont_write_bytecode = True
import numpy as np                                                              # noqa: E402

PASS = 0
FAIL = 0
T0 = time.time()


def check(label, cond, detail=""):
    global PASS, FAIL
    print(("PASS " if cond else "FAIL ") + label + (" | " + detail if detail else ""))
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


# ------------------------------------------------------------------ g2_lib: conventions
FD = [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)]
FD_NAMES = ['x+y', 'x-y', 'x+z', 'x-z', 'y+z', 'y-z']
POL_NAMES = ['xx', 'yy', 'zz', 'xy', 'yz', 'zx']
POL_PAIRS = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (2, 0)]
STAT_NAMES = ['site'] + ['ax' + s for s in 'xyz'] + ['fd' + s for s in FD_NAMES]


def tensor_from_coords(c):
    h = np.zeros((3, 3))
    for p, (a, b) in enumerate(POL_PAIRS):
        if a == b:
            h[a, a] = c[p]
        else:
            h[a, b] = h[b, a] = c[p] / np.sqrt(2)
    return h


def coords_from_tensor(h):
    c = np.zeros(6)
    for p, (a, b) in enumerate(POL_PAIRS):
        c[p] = h[a, a] if a == b else np.sqrt(2) * h[a, b]
    return c


def tt_basis(k):
    """Frobenius-orthonormal TT basis (plus, cross) at the continuum k-vector; 6x2 coordinates."""
    k = np.asarray(k, float)
    n = k / np.linalg.norm(k)
    trial = np.array([1.0, 0.0, 0.0]) if abs(n[0]) < 0.9 else np.array([0.0, 1.0, 0.0])
    u1 = trial - n * (trial @ n)
    u1 /= np.linalg.norm(u1)
    u2 = np.cross(n, u1)
    plus = (np.outer(u1, u1) - np.outer(u2, u2)) / np.sqrt(2)
    cross = (np.outer(u1, u2) + np.outer(u2, u1)) / np.sqrt(2)
    return np.stack([coords_from_tensor(plus), coords_from_tensor(cross)], axis=1)


def eta_ks(v, a):
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


class Lattice:
    def __init__(self, L, twist, flux='pi'):
        self.L, self.N, self.twist, self.flux = L, L ** 3, tuple(twist), flux
        self.sites = np.array(list(itertools.product(range(L), repeat=3)))
        self.eps = np.array([(-1) ** int(s) for s in self.sites.sum(1)], float)
        self.I = np.arange(self.N)
        self.J, self.S = [], []
        for a in range(3):
            w = self.sites.copy()
            w[:, a] = (w[:, a] + 1) % L
            e = np.array([(eta_ks(tuple(v), a) if flux == 'pi' else 1) for v in self.sites], float)
            s = np.where(self.sites[:, a] == L - 1, -e, e) if twist[a] else e
            self.J.append(self.idx(w))
            self.S.append(s)
        self.JD = [self.idx((self.sites + np.array(d)) % L) for d in FD]

    def idx(self, w):
        return (w[:, 0] * self.L + w[:, 1]) * self.L + w[:, 2]

    def M(self):
        M = np.zeros((self.N, self.N))
        for a in range(3):
            M[self.I, self.J[a]] += self.S[a]
            M[self.J[a], self.I] += self.S[a]
        return M

    def phase(self, nq):
        return np.exp(2j * np.pi * (self.sites @ np.asarray(nq, float)) / self.L)


def twist_table(L, flux, m=0.0):
    rows = []
    for tw in itertools.product((0, 1), repeat=3):
        lat = Lattice(L, tw, flux)
        w = np.linalg.eigvalsh(lat.M() + m * np.diag(lat.eps))
        n = L ** 3 // 2
        rows.append((tw, float(w[:n].sum()), float(w[n] - w[n - 1])))
    return rows


def choose_twist(L, flux):
    tab = twist_table(L, flux, 0.0)
    best = min(tab, key=lambda r: r[1])
    if best[2] < 1e-8:
        best = max(tab, key=lambda r: r[2])
    return tab, best


class Sea:
    def __init__(self, lat, m):
        self.lat, self.m = lat, m
        w, U = np.linalg.eigh(lat.M() + m * np.diag(lat.eps))
        n = lat.N // 2
        self.n, self.gap, self.E = n, float(w[n] - w[n - 1]), float(w[:n].sum())
        self.Uo, self.Ue = np.ascontiguousarray(U[:, :n]), np.ascontiguousarray(U[:, n:])
        self.P = self.Uo @ self.Uo.T
        self.D = 1.0 / (w[:n, None] - w[None, n:])

    def dP_half(self, lat, f):
        """Y with dP_{ij} = Y_i . Ue_j + Y_j . Ue_i: the exact first-order projector response
        to dH = sum_a f_a(v) s_a(v) (|v><v+a| + h.c.), formed without the full N x N product."""
        A = np.zeros((lat.N, lat.N - self.n))
        for a in range(3):
            g = (f[a] * lat.S[a])[:, None]
            np.add.at(A, lat.I, g * self.Ue[lat.J[a]])
            np.add.at(A, lat.J[a], g * self.Ue[lat.I])
        return self.Uo @ ((self.Uo.T @ A) * self.D)

    def dP_site(self, lat, f, pot):
        """Same, with an extra diagonal potential (the ruler chain's beta term)."""
        A = np.zeros((lat.N, lat.N - self.n))
        for a in range(3):
            g = (f[a] * lat.S[a])[:, None]
            np.add.at(A, lat.I, g * self.Ue[lat.J[a]])
            np.add.at(A, lat.J[a], g * self.Ue[lat.I])
        A += pot[:, None] * self.Ue
        return self.Uo @ ((self.Uo.T @ A) * self.D)

    def ent(self, Y, i, j):
        return np.einsum('nk,nk->n', Y[i], self.Ue[j]) + np.einsum('nk,nk->n', Y[j], self.Ue[i])


def stats0(lat, P):
    out = {'site': np.diag(P).copy()}
    for a in range(3):
        out['ax' + 'xyz'[a]] = -P[lat.I, lat.J[a]] ** 2
    for jd, nm in zip(lat.JD, FD_NAMES):
        out['fd' + nm] = -P[lat.I, jd] ** 2
    return out


def dstats(lat, sea, Y):
    out = {'site': sea.ent(Y, lat.I, lat.I)}
    for a in range(3):
        out['ax' + 'xyz'[a]] = -2 * sea.P[lat.I, lat.J[a]] * sea.ent(Y, lat.I, lat.J[a])
    for jd, nm in zip(lat.JD, FD_NAMES):
        out['fd' + nm] = -2 * sea.P[lat.I, jd] * sea.ent(Y, lat.I, jd)
    return out


def shifts(L):
    return [tuple((L // 2) * g for g in gg) for gg in itertools.product((0, 1), repeat=3)]


def fourier(lat, field, nq):
    return (np.conj(lat.phase(nq)) @ field) / lat.N


# ------------------------------------------------------------------ g2_lib: dressings
def bond_fields_declared(lat, c, nk, beta=1.0):
    """G1's endpoint-mean rule on the sea's own axis bonds: t_e = t (1 - beta h_e),
    h_e = delta l_e/l_0 = (h_bb(v) + h_bb(v+b))/4 for the b-bond based at v."""
    h = tensor_from_coords(c)
    ph = lat.phase(nk)
    return [-beta * h[b, b] * (ph + ph[lat.J[b]]) / 4.0 for b in range(3)]


def bond_fields_p2(lat, c, nk, kappa=0.5):
    """SUPPLIED: the unique multiplicity-one T2 nearest-neighbour coupling on the vacuum's
    period-2 pattern; the c-bond carries h_ab times (-1)^{v_c}[(-1)^{v_a} - (-1)^{v_b}]."""
    h = tensor_from_coords(c)
    ph = lat.phase(nk)
    par = [(-1.0) ** lat.sites[:, i] for i in range(3)]
    f = [np.zeros(lat.N, complex) for _ in range(3)]
    for cc in range(3):
        a, b = (cc + 1) % 3, (cc + 2) % 3
        f[cc] += kappa * h[a, b] * (par[cc] * (par[a] - par[b])) * (ph + ph[lat.J[cc]]) / 2.0
    return f


def bond_fields_curl(lat, c, nk, kappa=0.5):
    """SUPPLIED: the O(k) proper-rotation-covariant coupling (curl h)_bb on the b-bond."""
    h = tensor_from_coords(c)
    k = 2 * np.pi * np.asarray(nk, float) / lat.L
    ph = lat.phase(nk)
    e3 = np.zeros((3, 3, 3))
    e3[0, 1, 2] = e3[1, 2, 0] = e3[2, 0, 1] = 1
    e3[0, 2, 1] = e3[2, 1, 0] = e3[1, 0, 2] = -1
    f = []
    for b in range(3):
        coef = sum(e3[b, cc, d] * 1j * np.sin(k[cc]) * h[d, b] for cc in range(3) for d in range(3))
        f.append(kappa * coef * (ph + ph[lat.J[b]]) / 2.0)
    return f


def make_fields(lat, c, nk, rule, kappa=0.5):
    if rule == 'declared':
        return bond_fields_declared(lat, c, nk)
    if rule == 'p2':
        return bond_fields_p2(lat, c, nk, kappa)
    if rule == 'declared+p2':
        return [x + y for x, y in zip(bond_fields_declared(lat, c, nk),
                                      bond_fields_p2(lat, c, nk, kappa))]
    if rule == 'declared+curl':
        return [x + y for x, y in zip(bond_fields_declared(lat, c, nk),
                                      bond_fields_curl(lat, c, nk, kappa))]
    raise ValueError(rule)


def response_matrix(lat, sea, nk, rule, kappa=0.5):
    """R(k): rows (statistic, half-reciprocal shift G) x 6 Frobenius-orthonormal polarisations."""
    keys = [(nm, G) for G in shifts(lat.L) for nm in STAT_NAMES]
    R = np.zeros((len(keys), 6), complex)
    for p in range(6):
        c = np.zeros(6)
        c[p] = 1.0
        fields = make_fields(lat, c, nk, rule, kappa)
        resp = {}
        for part in (np.real, np.imag):
            Y = sea.dP_half(lat, [part(x) for x in fields])
            for nm, arr in dstats(lat, sea, Y).items():
                resp[nm] = resp.get(nm, 0) + (arr if part is np.real else 1j * arr)
        rows = {}
        for G in shifts(lat.L):
            nq = tuple((nk[i] + G[i]) % lat.L for i in range(3))
            for nm in STAT_NAMES:
                rows[(nm, G)] = fourier(lat, resp[nm], nq)
        R[:, p] = [rows[key] for key in keys]
    return keys, R


def numerical_rank(A, rel=1e-9):
    s = np.linalg.svd(A, compute_uv=False)
    return (0, s) if s.size == 0 or s[0] == 0 else (int(np.sum(s > rel * s[0])), s)


def kvec(nk, L):
    return 2 * np.pi * np.asarray(nk, float) / L


def keyrows(keys, R, pred):
    return R[[i for i, key in enumerate(keys) if pred(key)], :]


# ------------------------------------------------------------------ g2_kinematics: finite group O
def cubic_group():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            Rm = np.zeros((3, 3), int)
            for i in range(3):
                Rm[i, perm[i]] = signs[i]
            if int(round(np.linalg.det(Rm))) == 1:
                mats.append(Rm)
    return mats


def order(Rm):
    A = np.eye(3, dtype=int)
    for n in range(1, 7):
        A = A @ Rm
        if np.array_equal(A, np.eye(3, dtype=int)):
            return n
    raise RuntimeError


CLASSES = ['E', 'C3', 'C2', 'C4', "C2'"]
CHAR = {'A1': [1, 1, 1, 1, 1], 'A2': [1, 1, 1, -1, -1], 'E': [2, -1, 2, 0, 0],
        'T1': [3, 0, -1, 1, -1], 'T2': [3, 0, -1, -1, 1]}
G = cubic_group()
CL = []
for Rm in G:
    if int(np.trace(Rm)) == 3:
        CL.append('E')
    elif order(Rm) == 3:
        CL.append('C3')
    elif order(Rm) == 4:
        CL.append('C4')
    else:
        CL.append('C2' if np.count_nonzero(Rm - np.diag(np.diag(Rm))) == 0 else "C2'")


def decompose(chi):
    out = {}
    for irr, ch in CHAR.items():
        s = sum(chi[i] * ch[CLASSES.index(CL[i])] for i in range(24))
        out[irr] = int(round(s / 24))
        assert abs(s / 24 - out[irr]) < 1e-9
    return out


def fmt(mult):
    return '+'.join((f"{v}{k}" if v > 1 else k) for k, v in mult.items() if v)


FDV = [np.array(d) for d in FD]
LINES = {'axis': [np.array(e) for e in np.eye(3, dtype=int)], 'face': FDV}


def edge_map(names):
    rows = []
    for nm in names:
        for v in LINES[nm]:
            rows.append([v @ tensor_from_coords(np.eye(6)[p]) @ v / (2.0 * (v @ v)) for p in range(6)])
    return np.array(rows)


def perm_rep_classes(dirs, periodic2):
    reps = [np.array(d) for d in dirs]
    rhos = list(itertools.product((0, 1), repeat=3)) if periodic2 else [(0, 0, 0)]
    classes = [(i, r) for i in range(len(reps)) for r in rhos]
    index = {c: n for n, c in enumerate(classes)}
    mats = []
    for Rm in G:
        Pm = np.zeros((len(classes), len(classes)), int)
        for (i, r) in classes:
            Rd = Rm @ reps[i]
            j = next(jj for jj, dd in enumerate(reps) if np.array_equal(Rd, dd) or np.array_equal(Rd, -dd))
            rev = np.array_equal(Rd, -reps[j])
            if periodic2:
                Rr = (np.abs(Rm) @ np.array(r)) % 2
                if rev:
                    Rr = (Rr + np.abs(reps[j])) % 2
                new = (j, tuple(int(x) for x in Rr))
            else:
                new = (j, (0, 0, 0))
            Pm[index[new], index[(i, r)]] = 1
        mats.append(Pm)
    return classes, mats, [int(np.trace(Pm)) for Pm in mats]


def D_T2(Rm):
    D = np.zeros((3, 3))
    for q, (a, b) in enumerate([(0, 1), (1, 2), (2, 0)]):
        h = np.zeros((3, 3))
        h[a, b] = h[b, a] = 1
        hh = Rm @ h @ Rm.T
        for q2, (a2, b2) in enumerate([(0, 1), (1, 2), (2, 0)]):
            D[q2, q] = hh[a2, b2]
    return D


# ------------------------------------------------------------------ g2_escape: higher statistics
def three_site_and_plaquette(lat, sea, nk):
    """Response of the connected three-point function on the corner (v, v+x, v+y),
    <n n n>_c = 2 P_vu P_uw P_wv, and of the xy-plaquette joint occupation det P_S."""
    I, Jx, Jy = lat.I, lat.J[0], lat.J[1]
    Jxy = lat.J[1][lat.J[0]]
    P = sea.P
    S = np.stack([I, Jx, Jxy, Jy], axis=1)
    PS = P[S[:, :, None], S[:, None, :]]
    adj = np.linalg.det(PS)[:, None, None] * np.linalg.inv(PS)
    R3, R4 = [], []
    for p in range(6):
        c = np.zeros(6)
        c[p] = 1.0
        fields = bond_fields_declared(lat, c, nk)
        r3 = r4 = 0
        for part in (np.real, np.imag):
            Y = sea.dP_half(lat, [part(x) for x in fields])
            da, db, dc = sea.ent(Y, I, Jx), sea.ent(Y, Jx, Jy), sea.ent(Y, Jy, I)
            d3 = 2 * (da * P[Jx, Jy] * P[Jy, I] + P[I, Jx] * db * P[Jy, I] + P[I, Jx] * P[Jx, Jy] * dc)
            dPS = np.zeros((lat.N, 4, 4))
            for u in range(4):
                for w in range(4):
                    dPS[:, u, w] = sea.ent(Y, S[:, u], S[:, w])
            d4 = np.einsum('nij,nji->n', adj, dPS)
            r3 = r3 + (d3 if part is np.real else 1j * d3)
            r4 = r4 + (d4 if part is np.real else 1j * d4)
        col3, col4 = [], []
        for Gs in shifts(lat.L):
            nq = tuple((nk[i] + Gs[i]) % lat.L for i in range(3))
            col3.append(fourier(lat, r3, nq))
            col4.append(fourier(lat, r4, nq))
        R3.append(col3)
        R4.append(col4)
    return np.array(R3).T, np.array(R4).T


# ================================================================== T1  (i) provenance
DECL = {6: [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0), (1, 2, 5), (1, 2, 3), (1, 1, 2)],
        8: [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0), (1, 2, 3), (1, 1, 2), (2, 1, 3)],
        12: [(1, 0, 0), (2, 0, 0), (3, 0, 0), (1, 1, 0), (1, 1, 1), (2, 2, 2), (1, 2, 0),
             (1, 2, 3), (1, 1, 2), (2, 3, 5), (1, 3, 4)]}
COV = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
LATS, SEAS, TWS = {}, {}, {}
for L in (6, 8, 12):
    for flux in (('pi', 'zero') if L == 8 else ('pi',)):
        tab, (tw, E0, g0) = choose_twist(L, flux)
        TWS[(L, flux)] = (tw, E0, g0)
        LATS[(L, flux)] = Lattice(L, tw, flux)
        for m in (0.0, 1.0):
            SEAS[(L, flux, m)] = Sea(LATS[(L, flux)], m)

prov = []
for L, e_ref, g_ref, p_ref in ((6, -258.857540, 3.464102, 0.199736), (8, -611.811768, 2.651309, 0.199157)):
    tw, E0, g0 = TWS[(L, 'pi')]
    lat, sea = LATS[(L, 'pi')], SEAS[(L, 'pi', 0.0)]
    pmax = float(np.max(np.abs(sea.P[lat.I, lat.J[0]])))
    prov.append((abs(E0 - e_ref) < 5e-6 and abs(g0 - g_ref) < 5e-6 and abs(pmax - p_ref) < 5e-7
                 and float(np.max(np.abs(np.diag(sea.P) - 0.5))) < 1e-13, L, tw, E0, g0, pmax))
E12, g12 = TWS[(12, 'pi')][1], TWS[(12, 'pi')][2]
check("T1 (i) provenance of the pi-flux sea against the determinantal note",
      all(p[0] for p in prov) and abs(E12 + 2063.196887) < 5e-6,
      "6^3 twist %s E=%.6f gap=%.6f max|P|sep1=%.6f; 8^3 twist %s E=%.6f gap=%.6f max|P|sep1=%.6f; "
      "12^3 E=%.6f gap=%.6f; max|P_vv-1/2| <= 1e-13"
      % (prov[0][2], prov[0][3], prov[0][4], prov[0][5], prov[1][2], prov[1][3], prov[1][4],
         prov[1][5], E12, g12))

# ================================================================== T2a (ii) cubic content
chi_site = [1] * 24
chi_axes = [sum(1 for a in range(3) if abs(Rm[:, a]).tolist() == np.eye(3, dtype=int)[:, a].tolist())
            for Rm in G]
chi_fd = [sum(1 for d in FDV if np.array_equal(Rm @ d, d) or np.array_equal(Rm @ d, -d)) for Rm in G]
chi_sym = [(np.trace(Rm) ** 2 + np.trace(Rm @ Rm)) / 2 for Rm in G]
c_site, c_ax, c_fd = fmt(decompose(chi_site)), fmt(decompose(chi_axes)), fmt(decompose(chi_fd))
c_h = fmt(decompose(chi_sym))
c_all = fmt(decompose([a + b + c for a, b, c in zip(chi_site, chi_axes, chi_fd)]))
check("T2a (ii) cubic-group content of the readable statistics (proper rotations O, order 24)",
      len(G) == 24 and c_site == 'A1' and c_ax == 'A1+E' and c_fd == 'A1+E+T2' and c_h == 'A1+E+T2'
      and c_all == '3A1+2E+T2',
      "site %s; axis-bond pairs %s; face-diagonal pairs %s; metric h_ij %s; all ten %s -- T2 is "
      "carried by the face-diagonal pairs only" % (c_site, c_ax, c_fd, c_h, c_all))

# ================================================================== T2b (iii) edge-length map
Eax, Efc = edge_map(['axis']), edge_map(['face'])
r_ax = int(np.sum(np.linalg.svd(Eax, compute_uv=False) > 1e-12))
r_fc = int(np.sum(np.linalg.svd(Efc, compute_uv=False) > 1e-12))
r_both = int(np.sum(np.linalg.svd(edge_map(['axis', 'face']), compute_uv=False) > 1e-12))
shear_col = float((Efc[0] - Efc[1])[3])
check("T2b (iii) G1's endpoint-mean edge-length map delta l_e/l_0 = w^T h w/(2|w|^2) at first order",
      r_ax == 3 and r_fc == 6 and r_both == 6
      and np.allclose(Eax, np.diag([0.5, 0.5, 0.5]) @ np.eye(3, 6)) and abs(shear_col - 1 / np.sqrt(2)) < 1e-14
      and np.max(np.abs(Eax[:, 3:])) == 0.0,
      "axis rows rank %d and give h_aa/2 and nothing else (shear columns exactly 0); face-diagonal "
      "rows rank %d; both rank %d; (dl_{x+y}-dl_{x-y})/l_0 = %.6f E_xy = h_xy: a shear changes no "
      "axis edge" % (r_ax, r_fc, r_both, shear_col))

# ================================================================== T2c (iv) TT rank criterion
kin = {}
worst_det, ok2c = 0.0, True
for L, ks in DECL.items():
    for nk in ks:
        k = kvec(nk, L)
        dg = tt_basis(k)[:3, :]
        s = np.linalg.svd(dg, compute_uv=False)
        Km = np.array([[k[1], k[2], 0], [k[0], 0, k[2]], [0, k[0], k[1]]])
        det = float(np.linalg.det(Km))
        worst_det = max(worst_det, abs(det + 2 * float(np.prod(k))))
        nullity = 2 - int(np.linalg.matrix_rank(dg, tol=1e-12))
        generic = all(x % L != 0 for x in nk)
        ok2c &= (nullity == (0 if generic else 1))
        kin[(L, nk)] = (s[0], s[1], generic)
check("T2c (iv) the TT rank is decided kinematically: a TT tensor with zero diagonal exists iff k1k2k3 = 0",
      ok2c and worst_det < 1e-14,
      "on pure T2 h, transversality is [[k2,k3,0],[k1,0,k3],[0,k1,k2]](a,b,c)=0, det = -2k1k2k3 to "
      "%.1e over the 25 declared momenta; dim(TT n T2) = 1 on every coordinate plane, 0 off it; "
      "sv(diag.TT) = (%.3f, %.3f) at 12^3 (1,2,3)"
      % (worst_det, kin[(12, (1, 2, 3))][0], kin[(12, (1, 2, 3))][1]))

# ================================================================== T3 the declared response
RES = {}
for (L, flux, m) in [(6, 'pi', 0.0), (6, 'pi', 1.0), (8, 'pi', 0.0), (8, 'pi', 1.0),
                     (8, 'zero', 1.0), (12, 'pi', 0.0), (12, 'pi', 1.0)]:
    lat, sea = LATS[(L, flux)], SEAS[(L, flux, m)]
    for nk in DECL[L] + [c for c in COV if c not in DECL[L]]:
        RES[(L, flux, m, nk)] = response_matrix(lat, sea, nk, 'declared')

t2max = 0.0
rank_ok = True
for (L, flux, m, nk), (keys, R) in RES.items():
    t2max = max(t2max, float(np.max(np.abs(R[:, 3:]))))
    zone = any(2 * x == L for x in nk)
    rank_ok &= (numerical_rank(R)[0] == (2 if zone else 3))
check("T3a (vi) the declared dressing t_e = t(1 - h_e) never couples to a shear: the T2 columns of "
      "R(k) are identically zero",
      t2max == 0.0 and rank_ok,
      "T2max = %.1e over %d (torus, sea, momentum) triples on 6^3/8^3/12^3, pi-flux m in {0,1} and "
      "the zero-flux control; rank(R) = rank(diagonal columns) = 3, and 2 where an endpoint-mean "
      "factor vanishes" % (t2max, len(RES)))

tt = {}
for key, (keys, R) in RES.items():
    L, nk = key[0], key[3]
    T = tt_basis(kvec(nk, L))
    tt[key] = (numerical_rank(R @ T)[1], float(np.max(np.abs(R @ T[:, 1]))))
ok3b = True
cross_zero = 0.0
for key, (s, xz) in tt.items():
    L, nk = key[0], key[3]
    generic = all(x % L != 0 for x in nk)
    ok3b &= (int(np.sum(s > 1e-9 * s[0])) == (2 if generic else 1))
    if not generic:
        cross_zero = max(cross_zero, xz)
check("T3b (vi) TT rank of R(k) is 2 where k1k2k3 != 0 and 1 on the coordinate planes, on 6^3, 8^3, "
      "12^3, both masses",
      ok3b and cross_zero == 0.0,
      "the dynamics never lowers the kinematic rank; on every coordinate-plane momentum R(k)T_cross "
      "is exactly zero (max %.1e): the cross polarisation has no response at all there" % cross_zero)

def ratio(L, m, nk):
    s = tt[(L, 'pi', m, nk)][0]
    return s[1] / s[0]


smax = [tt[key][0][0] for key in tt if not any(2 * x == key[0] for x in key[3])]
kin123 = kin[(12, (1, 2, 3))][1] / kin[(12, (1, 2, 3))][0]
r12 = [ratio(12, m, (1, 2, 3)) for m in (0.0, 1.0)]
r8 = [ratio(8, m, (1, 2, 3)) for m in (0.0, 1.0)]
rbd = [ratio(12, m, nk) for m in (0.0, 1.0) for nk in ((1, 1, 1), (2, 2, 2))]
plus_axis = [tt[(L, 'pi', 0.0, (1, 0, 0))][0][0] for L in (6, 8, 12)]
bd = [tt[(L, 'pi', 0.0, (1, 1, 1))][0][0] for L in (6, 8, 12)]
check("T3c (vi) conditioning: TT singular values O(0.02-0.03), flat in |k| and torus size; s_min/s_max "
      "tracks the kinematic plane distance",
      min(smax) > 0.010 and max(smax) < 0.035 and max(abs(r - kin123) for r in r12) < 0.01
      and max(abs(r - 1.0) for r in rbd) < 1e-6,
      "s_max in [%.4f, %.4f] over the declared momenta with no endpoint-mean zero; plus mode at "
      "(1,0,0): %.6f, %.6f, %.6f for L = 6, 8, 12; (1,1,1): %.6f, %.6f, %.6f; 12^3 (1,2,3): "
      "s_min/s_max %.4f (m=0), %.4f (m=1) vs kinematic %.4f, 1.0000 on the body diagonals; "
      "8^3 %.4f, %.4f"
      % (min(smax), max(smax), plus_axis[0], plus_axis[1], plus_axis[2], bd[0], bd[1], bd[2],
         r12[0], r12[1], kin123, r8[0], r8[1]))

keys6, R6 = RES[(6, 'pi', 0.0, (1, 2, 3))]
cn = [float(np.linalg.norm(R6[:, p])) for p in range(3)]
fac = [abs((1 + np.exp(2j * np.pi * n / 6)) / 2) for n in (1, 2, 3)]
keys6b, R6b = RES[(6, 'pi', 0.0, (1, 2, 5))]
check("T3d (x) the endpoint-mean factor (1 + e^{ik_b})/2 vanishes at k_b = pi and removes h_bb exactly",
      cn[2] < 1e-15 and fac[2] < 1e-15 and numerical_rank(R6)[0] == 2 and numerical_rank(R6b)[0] == 3,
      "6^3 n = (1,2,3): |(1+e^{ik_b})/2| = %.3f, %.3f, %.1e and column norms %.5f, %.5f, %.1e, "
      "rank 2; the neighbouring n = (1,2,5) has rank 3" % (fac[0], fac[1], fac[2], cn[0], cn[1], cn[2]))

# ================================================================== T4 higher statistics
t2_hi, diag_hi, rk_hi = 0.0, [], []
for L in (8, 12):
    for m in (0.0, 1.0):
        for nk in ((1, 0, 0), (1, 2, 3)):
            R3, R4 = three_site_and_plaquette(LATS[(L, 'pi')], SEAS[(L, 'pi', m)], nk)
            t2_hi = max(t2_hi, float(np.max(np.abs(R3[:, 3:]))), float(np.max(np.abs(R4[:, 3:]))))
            diag_hi.append((float(np.max(np.abs(R3[:, :3]))), float(np.max(np.abs(R4[:, :3])))))
check("T4 (5.2) no higher-order readable statistic escapes: the three-site corner statistic and the "
      "plaquette joint occupation det P_S have zero shear response",
      t2_hi == 0.0 and max(d[1] for d in diag_hi) > 1e-3,
      "T2max = %.1e on 8^3 and 12^3, m in {0,1}, at n = (1,0,0) and (1,2,3); the diagonal response "
      "is alive: plaquette to %.3e, three-site to %.3e"
      % (t2_hi, max(d[1] for d in diag_hi), max(d[0] for d in diag_hi)))

# ================================================================== T5 (viii) sublattice cancellation
site0 = max(float(np.max(np.abs(keyrows(keys, R, lambda key: key[0] == 'site' and key[1] == (0, 0, 0)))))
            for (L, flux, m, nk), (keys, R) in RES.items())
ax0 = min(float(np.max(np.abs(keyrows(keys, R, lambda key: key[0].startswith('ax') and key[1] == (0, 0, 0)))))
          for (L, flux, m, nk), (keys, R) in RES.items() if flux == 'pi')
sc = {}
for m in (0.0, 1.0):
    lat, sea = LATS[(12, 'pi')], SEAS[(12, 'pi', m)]
    Q = (6, 6, 6)
    for nk in ((1, 0, 0),):
        ph = lat.phase(nk)
        for (al, be) in ((1.0, 1.0), (2.0, 1.0)):
            acc = {}
            for part in (np.real, np.imag):
                f = [part(al * (ph + ph[lat.J[a]]) / 2.0) for a in range(3)]
                Y = sea.dP_site(lat, f, part(be * m * lat.eps * ph))
                for nm, v in dstats(lat, sea, Y).items():
                    acc[nm] = acc.get(nm, 0) + (v if part is np.real else 1j * v)
            dn = acc['site']
            bavg = (np.mean(np.conj((ph + ph[lat.J[0]]) / 2) * (dn + dn[lat.J[0]]) / 2)
                    / np.mean(np.abs((ph + ph[lat.J[0]]) / 2) ** 2))
            sc[(m, al)] = (abs(fourier(lat, dn, nk)), abs(fourier(lat, dn, tuple((nk[i] + Q[i]) % 12
                                                                                for i in range(3)))),
                           abs(bavg), max(abs(fourier(lat, acc['ax' + a], nk)) for a in 'xyz'))
check("T5 (viii) the sublattice cancellation that forced the rate ruler is confined to the uniform part "
      "of the SITE statistic",
      site0 <= 1e-17 and max(sc[k][0] for k in sc) <= 1e-17 and max(sc[k][2] for k in sc) <= 1e-17
      and abs(sc[(1.0, 2.0)][1] - 0.159) < 5e-4 and ax0 > 8e-3 and sc[(1.0, 2.0)][3] > 1e-2,
      "metric polarisations: site@0 <= %.1e everywhere, axis-bond pair response >= %.3e; ruler "
      "scalar H(alpha,1) at 12^3 n=(1,0,0): site@0 <= %.1e, bond average <= %.1e at (1,1) and (2,1), "
      "both masses; staggered site@Q = %.4f at (2,1) m=1; axis pair %.3e"
      % (site0, ax0, max(sc[k][0] for k in sc), max(sc[k][2] for k in sc), sc[(1.0, 2.0)][1],
         sc[(1.0, 2.0)][3]))

# ================================================================== T6 (vii) the pi-flux exact zero
mech = {}
for flux in ('pi', 'zero'):
    lat = LATS[(8, flux)]
    M2 = lat.M() @ lat.M()
    fdm = max(float(np.max(np.abs(M2[lat.I, jd]))) for jd in lat.JD)
    row = [fdm]
    for m in (0.0, 1.0):
        sea = SEAS[(8, flux, m)]
        c = np.zeros(6)
        c[0] = 1.0
        Y = sea.dP_half(lat, [np.real(x) for x in bond_fields_declared(lat, c, (1, 2, 3))])
        pfd = max(float(np.max(np.abs(sea.P[lat.I, jd]))) for jd in lat.JD)
        cfd = max(float(np.max(np.abs(sea.P[lat.I, jd] ** 2))) for jd in lat.JD)
        dcfd = max(float(np.max(np.abs(-2 * sea.P[lat.I, jd] * sea.ent(Y, lat.I, jd)))) for jd in lat.JD)
        row += [pfd, cfd, dcfd]
    mech[flux] = row
check("T6 (vii) the pi-flux vacuum's own exact zero: the face-diagonal pair statistics, the only "
      "readable pair statistics carrying T2, vanish identically",
      mech['pi'][0] == 0.0 and abs(mech['zero'][0] - 2.0) < 1e-12 and max(mech['pi'][1], mech['pi'][4]) < 1e-14
      and max(mech['pi'][3], mech['pi'][6]) < 1e-16 and mech['zero'][5] > 1e-4 and mech['zero'][6] > 1e-4,
      "the two two-step paths around a plaquette carry opposite KS signs, so max|(M^2)_{v,v+fd}| = "
      "%.1f against %.1f at zero flux; hence max|P_fd| <= %.1e and max|dC_fd| <= %.1e at m = 0 and 1; "
      "the zero-flux control at m = 1 is alive: C0_fd = %.2e, dC_fd = %.2e"
      % (mech['pi'][0], mech['zero'][0], max(mech['pi'][1], mech['pi'][4]),
         max(mech['pi'][3], mech['pi'][6]), mech['zero'][5], mech['zero'][6]))

# ================================================================== T7a (ix) leakage and covariance
leak = pairQ = 0.0
for (L, flux, m, nk), (keys, R) in RES.items():
    Q = (L // 2, L // 2, L // 2)
    leak = max(leak, float(np.max(np.abs(keyrows(keys, R, lambda key: key[1] not in ((0, 0, 0), Q))))))
    pairQ = max(pairQ, float(np.max(np.abs(keyrows(keys, R, lambda key: key[1] == Q and key[0] != 'site')))))
cov = 0.0
for L in (6, 8, 12):
    for m in (0.0, 1.0):
        sv = {nk: tt[(L, 'pi', m, nk)][0] for nk in COV}
        cov = max(cov, max(float(np.max(np.abs(sv[a] - sv[COV[0]]))) for a in COV[1:3]),
                  max(float(np.max(np.abs(sv[a] - sv[COV[3]]))) for a in COV[4:]))
check("T7a (ix) translation and rotation covariance of the reading are exact on the gauge-invariant "
      "record statistics",
      leak < 1e-16 and pairQ < 1e-16 and cov < 1e-16,
      "response outside the shifts {0, Q} <= %.1e, pair statistics at Q <= %.1e; TT singular values "
      "agree across the three axis momenta and across the three face-diagonal momenta to <= %.1e on "
      "all three tori, both masses" % (leak, pairQ, cov))

# ================================================================== T7b (v) the period-2 intertwiner
counts = {}
for lab, dirs, per in (('uniform axis', [np.eye(3, dtype=int)[:, a] for a in range(3)], False),
                       ('period-2 axis', [np.eye(3, dtype=int)[:, a] for a in range(3)], True),
                       ('uniform face-diagonal', FDV, False)):
    classes, mats, chi = perm_rep_classes(dirs, per)
    counts[lab] = fmt(decompose(chi))
classes, mats, chi = perm_rep_classes([np.eye(3, dtype=int)[:, a] for a in range(3)], True)
A = np.vstack([np.kron(np.eye(3), Pm) - np.kron(D_T2(Rm).T, np.eye(len(classes)))
               for Pm, Rm in zip(mats, G)])
nullity = A.shape[1] - int(np.linalg.matrix_rank(A, tol=1e-9))
Fm = np.linalg.svd(A)[2][-1].reshape(3, len(classes)).T
Fm = Fm / np.max(np.abs(Fm))
scale, dev = None, 0.0
for q, (a, b, cc) in enumerate([(0, 1, 2), (1, 2, 0), (2, 0, 1)]):
    pred = np.array([((-1) ** r[cc]) * (((-1) ** r[a]) - ((-1) ** r[b])) / 2.0 if i == cc else 0.0
                     for (i, r) in classes])
    if scale is None:
        scale = pred @ Fm[:, q] / (pred @ pred)
    dev = max(dev, float(np.max(np.abs(Fm[:, q] - scale * pred))))
check("T7b (v) exactly one covariant nearest-neighbour shear coupling exists, on a period-2 pattern, "
      "unique up to scale",
      counts['uniform axis'] == 'A1+E' and counts['period-2 axis'] == '3A1+A2+4E+3T1+T2'
      and counts['uniform face-diagonal'] == 'A1+E+T2' and nullity == 1 and dev < 1e-12,
      "uniform axis-bond modulations carry %s and no T2; the 24 period-2 axis-bond classes carry %s, "
      "one T2; the intertwiner space is %d-dimensional and equals delta t_c = kappa h_ab (-1)^{v_c}"
      "[(-1)^{v_a} - (-1)^{v_b}], (a,b,c) cyclic, to %.1e; face-diagonal bonds carry T2 uniformly "
      "(%s), and the adjacency has none"
      % (counts['uniform axis'], counts['period-2 axis'], nullity, dev, counts['uniform face-diagonal']))

# ================================================================== T7c (xi) the escape, computed
esc, esc_rank = {}, True
for L in (8, 12):
    for m in ((0.0, 1.0) if L == 8 else (1.0,)):
        for nk in COV + [(1, 2, 0), (1, 1, 1), (1, 2, 3)]:
            keys, R = response_matrix(LATS[(L, 'pi')], SEAS[(L, 'pi', m)], nk, 'declared+p2', kappa=0.5)
            rk, sa = numerical_rank(R)
            st = numerical_rank(R @ tt_basis(kvec(nk, L)))[1]
            esc[(L, m, nk)] = (rk, sa, st)
            esc_rank &= (rk == 6 and int(np.sum(st > 1e-9 * st[0])) == 2)
keysn, Rn = response_matrix(LATS[(12, 'pi')], SEAS[(12, 'pi', 0.0)], (1, 0, 0), 'declared+p2', kappa=0.5)
sN, vtN = np.linalg.svd(Rn, full_matrices=False)[1:]
vN = vtN[-1] / vtN[-1][int(np.argmax(np.abs(vtN[-1])))]
esc_cov = 0.0
for L in (8, 12):
    for m in ((0.0, 1.0) if L == 8 else (1.0,)):
        esc_cov = max(esc_cov, max(float(np.max(np.abs(esc[(L, m, a)][2] - esc[(L, m, COV[0])][2])))
                                   for a in COV[1:3]),
                      max(float(np.max(np.abs(esc[(L, m, a)][2] - esc[(L, m, COV[3])][2]))) for a in COV[4:]))
s100 = esc[(12, 1.0, (1, 0, 0))][2]
check("T7c (xi) SUPPLIED period-2 coupling added to the declared dressing: all six polarisations, and "
      "both TT modes at every declared momentum, are read",
      esc_rank and esc_cov < 1e-16 and abs(s100[0] - 0.027929) < 5e-6 and abs(s100[1] - 0.027220) < 5e-6
      and np.max(np.abs(np.abs(vN[:3]) - 1.0)) < 0.02 and np.max(np.abs(vN[3:])) < 1e-6,
      "rank(R) = 6 and TT rank 2 at all %d (torus, mass, momentum) triples on 8^3 and 12^3; 12^3 m=1 "
      "(1,0,0): TT sv %.6f, %.6f (ratio %.4f); covariance <= %.1e; at m=0 the sixth sv %.1e has null "
      "direction (%.2f,%.2f,%.2f,0,0,0), the uniform dilation that rescales the massless H0, not TT"
      % (len(esc), s100[0], s100[1], s100[1] / s100[0], esc_cov, sN[5], vN[0].real, vN[1].real, vN[2].real))

# ================================================================== T7d (xii) the curl coupling
curl = {}
lat12 = LATS[(12, 'pi')]
for nk in ((1, 0, 0), (1, 1, 0), (1, 2, 0)):
    k = kvec(nk, 12)
    T = tt_basis(k)
    ph = lat12.phase(nk)
    fp = bond_fields_declared(lat12, T[:, 0], nk)
    fc = bond_fields_curl(lat12, T[:, 1], nk, kappa=0.5)
    a = np.array([np.mean(fp[b] / ph) for b in range(3)])
    c = np.array([np.mean(fc[b] / ph) for b in range(3)])
    cosang = abs(np.vdot(a, c)) / (np.linalg.norm(a) * np.linalg.norm(c))
    st = numerical_rank(response_matrix(lat12, SEAS[(12, 'pi', 1.0)], nk, 'declared+curl', kappa=0.5)[1]
                        @ T)[1]
    curl[nk] = (float(cosang), st)
check("T7d (xii) the O(k) curl coupling is NOT an escape: it modulates the cross mode's bonds parallel "
      "to the plus mode's",
      abs(curl[(1, 0, 0)][0] - 1.0) < 5e-7 and abs(curl[(1, 1, 0)][0] - 1.0) < 5e-7
      and all(curl[n][1][1] < 1e-9 * curl[n][1][0] for n in ((1, 0, 0), (1, 1, 0))),
      "|cos| between the curl(cross) and the declared-plus bond amplitudes = %.6f at (1,0,0), %.6f "
      "at (1,1,0), %.6f at (1,2,0); TT rank stays 1 on the axis (s_min %.1e); the residual %.1e at "
      "(1,2,0) is the sin k/k anisotropy"
      % (curl[(1, 0, 0)][0], curl[(1, 1, 0)][0], curl[(1, 2, 0)][0], curl[(1, 0, 0)][1][1],
         curl[(1, 2, 0)][1][1]))

print("SUPPLIED, not derived: the fermion law; the pi-flux sea, KS pattern, twist rule and m; "
      "beta = nu_r = 1; the endpoint-mean rule; the pair-statistic reading of an edge length; kappa. "
      "Runtime %.0f s." % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
raise SystemExit(0 if FAIL == 0 else 1)
