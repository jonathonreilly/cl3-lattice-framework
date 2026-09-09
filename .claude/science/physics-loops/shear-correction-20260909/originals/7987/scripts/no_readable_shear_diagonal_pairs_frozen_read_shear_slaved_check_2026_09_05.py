"""No readable shear without a supplied coupling: the length-dressed nearest-neighbour law is a
function of the axis edge lengths only, the nearest diagonal pair statistics are frozen on the
vacuum, and the read shear is slaved to the read diagonal.

CLASS A, finite-dimensional. Every object is a finite matrix on an L^3 coarse torus, a 15-class
edge space of the landed 4D cubic-Coxeter complex, or the 24-element proper cubic rotation group;
every statement is decided by exact linear algebra on it. NO random number, NO seed, NO fitted
constant, NO measured value.

PROVENANCE OF THE CODE. Self-contained apart from the landed Regge module declared in
AUDIT_INPUT_PATHS, which lives on origin/main; nothing is imported from any unmerged branch.
Every block below is COPIED from the probe scripts of scratchpad/G5 and names its source block:
  FD/BD/AX/POL_PAIRS/CORNERS/PLAQ, tensor_from_coords, coords_from_tensor, tt_basis, eta_ks,
  Lattice, twist_table, choose_twist, Sea, shifts, fourier, bond_fields_declared, bond_fields_p2,
  numerical_rank, kvec
                        reproduce the same names in g5_lib.py, whose first blocks are themselves a
                        verbatim copy of G2's runner (PR #7951): KS signs eta_1 = 1,
                        eta_2 = (-1)^{v1}, eta_3 = (-1)^{v1+v2}; twist[a] = 1 flips the bonds
                        crossing v_a = L-1 -> 0; H0 = M + m Eps; P = projector on the N/2 lowest
                        eigenvectors; pair law C_uv = -|K_uv|^2.
  PAIR_GROUPS, stat_names, adjugate4, _safe_div, KernelStats, sea_kel, sea_response_columns,
  rows_at_shifts, conditioned_kernel, conditioned_dkel, support_by_separation
                        reproduce the same names in g5_lib.py (the extended statistic catalogue:
                        body-diagonal, second-neighbour, connected corner three-point, the
                        Lueders-conditioned corner pair, the conditioned collinear diagonal and
                        the plaquette joint occupation, with their exact first variations).
  star_tick_kernel, dressing_directions, dP_full
                        reproduce the same names in g5_lib.py, themselves T3's G_dG (PR #7986) on
                        G2's Lattice: G = prod exp(-i tau h_R) over the star tick, h_R = M with the
                        recorded edges' hops zeroed and closed corners dropped.
  cubic_group, CHAR, decompose, fmt, shape_rep, shapes_of
                        reproduce g5_lib.py's finite-group blocks (characters of O on the classes
                        of a statistic under the full, even-sum and 2Z^3 translation groups).
  READ_EDGES, edge_map6, gauge_projectors, S_SEA, read_map, read_analyse
                        reproduce g5_lib.py's read-metric machinery and g5_task3_reading.py's
                        read_map / analyse.
  precompute_terms, Q_of, M_am, h10_from_c6
                        reproduce g5_task3_reading.py, itself G1's runner (PR #7940) precompute_terms
                        / Q_grid / M_grid('am'), written against the landed bloch_Q.
  the check bodies      reproduce g5_validate.py (V1-V4), g5_task1_kinematics.py (K1-K5),
                        g5_task2_response.py (a, b', c, d, e), g5_task2_rotated.py (R0-R2) and
                        g5_task3_reading.py (P0, V, the per-configuration read lines).

SETTING. Coarse tori L^3, L in {6, 8, 12}; the pi-flux half-filled staggered sea with the
Kogut-Susskind signs and the minimum-energy twist ((0,0,0), (1,1,1), (1,1,1)); record-native mass
m in {0, 1}. Dressing (the ruler chain with beta = nu_r = 1, G1's endpoint-mean rule on the sea's
own axis bonds): t_e = t(1 - h_e), h_e = h_bb (e^{ik.v} + e^{ik.(v+b)})/4 for the b-bond based at v.
Polarisations: the Frobenius-orthonormal E_xx, E_yy, E_zz, E_xy, E_yz, E_zx; TT basis at the
continuum k = 2 pi n / L. R(k): eleven statistic groups x eight half-reciprocal shifts x six
polarisations; rank counts singular values above 1e-9 of the largest. Configurations: the sea at
m in {0, 1}; the filled 32-fold particle multiplet above it; the mass domain wall m(v) = +1 for
v_1 < L/2 and -1 otherwise; the Lueders (Schur) conditioning on one occupied record at v0 = 0; the
zero-flux control; the star tick's rotated law K = G P G^+ on 6^3 with tau = 0.5 over T3's 27-order
even-translation family. The reading of T4: l_e/l_0 = J_e/J_e^0 with J_e = <n_v n_{v+e}>, unit
coefficient per class, the body diagonal kept as the metricity check.

DECLARED SUB-FAMILY. The source result's shear-column table covers 90 (configuration, momentum)
pairs and 990 group lines. To stay inside the time budget this runner recomputes 28 of those pairs
from scratch -- sea 6^3 m in {0,1} at (1,0,0), (1,1,1), (1,2,5); sea 8^3 m in {0,1} at (1,0,0),
(1,1,0), (1,1,1), (1,2,5), (2,3,5); sea 12^3 m=0 at (1,0,0), (1,1,1), (1,2,3) and m=1 at (1,0,0);
the filled multiplet on 8^3 at (1,0,0), (1,1,1); the mass wall on 8^3 at (1,0,0), (1,1,1); the
conditioned law on 8^3 at (1,0,0), (1,1,1); the zero-flux control on 8^3 at m in {0,1}, (1,1,1);
and the rotated law on 6^3 at (1,0,0) -- and quotes the remaining 62 from the source output lines
out_task2_table.txt, out_task2_rot6.txt and out_task2_rot8.txt, which are not re-executed here.
The rotated law is run at one momentum only (the source ran five on 6^3 and one on 8^3), and the
8^3 single-order spot check is dropped. The reading is recomputed on 15 of the source's 36 lines,
and the period-2 frozen-register test on the 8^3 half of the source's eight blocks.

CHECKS (thirteen; grouped as T1-T5 in the note).
  (i)    provenance: G2's sea, its TT singular values and plaquette response, and the copied Regge
         operator against the landed bloch_Q.
  (ii)   T1: the representation content of every candidate statistic under the three translation
         groups, and the T2 multiplicities.
  (iii)  T1: the six-edge map is invertible with h_ab = 2 dl_{a+b} - dl_a - dl_b, the body diagonal
         is forced, and the shear dressing fields are an exact floating-point zero.
  (iv)   T2: the parity zero Z2 -- every function of H0 is supported on separations with at most
         one odd coordinate, on 8^3 and 12^3.
  (v)    T2: the chiral zero Z1 -- at m = 0 the same-sublattice block of P is exactly I/2.
  (vi)   T2: the frozen register under the supplied period-2 coupling.
  (vii)  T3: the shear columns are exactly 0.0 for all eleven groups on the declared sub-family.
  (viii) T3: the alive T2 carriers on the vacuum -- the conditioned corner pair and, with mass, the
         second-neighbour diagonals.
  (ix)   T3: what breaks the vacuum zero -- zero flux, the wall, conditioning, a single particle.
  (x)    T3: the rotated law -- alive nearest face diagonals, shear-blind, corner three-point zero.
  (xi)   T4: rank(H_read) = 3 and the read shear slaved to the read diagonal.
  (xii)  T4: the gauge-invariant content of the read metric and its Regge residual.
  (xiii) T4: the vacuum's uniform statistics are flat and the seven-class read geometry is non-metric.

MEMORY: largest dense object (1728, 1728) real. RUNTIME: about 100 s.
SUPPLIED, NOT DERIVED: the designed fermion law; the pi-flux sea, its KS signs, twist rule and m;
beta = nu_r = 1 and the endpoint-mean rule; the pair-statistic reading of an edge length and the
joint-occupation reading with its unit coefficient; T3's star tick, tau = 0.5 and its order family;
the Lueders clause; G2's period-2 coupling and kappa = 1/2; the wall profile, the multiplet, v0;
the Regge action, the complex, its orientation and G; the TT conventions.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

import itertools
import os
import sys

sys.dont_write_bytecode = True
import numpy as np

_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS not in sys.path:
    sys.path.insert(0, _SCRIPTS)

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4      # noqa: E402

PASS = 0
FAIL = 0


def check(tag, title, cond, detail):
    global PASS, FAIL
    print("%s %s %s | %s" % ("PASS" if cond else "FAIL", tag, title, detail), flush=True)
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


# ================================================================ conventions (g5_lib.py, from G2)
FD = [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)]
FD_NAMES = ['x+y', 'x-y', 'x+z', 'x-z', 'y+z', 'y-z']
BD = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1)]
BD_NAMES = ['x+y+z', 'x+y-z', 'x-y+z', 'x-y-z']
AX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
POL_NAMES = ['xx', 'yy', 'zz', 'xy', 'yz', 'zx']
POL_PAIRS = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (2, 0)]
CORNERS = [((a, sa), (b, sb)) for a, b in [(0, 1), (0, 2), (1, 2)] for sa in (1, -1) for sb in (1, -1)]
PLAQ = [(0, 1), (0, 2), (1, 2)]


def tensor_from_coords(c):
    h = np.zeros((3, 3), dtype=np.result_type(np.asarray(c), float))
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
        self.JD = [self.sep(d) for d in FD]
        self.JB = [self.sep(d) for d in BD]
        self.JA2 = [self.sep(tuple(2 * x for x in d)) for d in AX]
        self.JD2 = [self.sep(tuple(2 * x for x in d)) for d in FD]
        self.JB2 = [self.sep(tuple(2 * x for x in d)) for d in BD]
        self.JC = [(self.sep(tuple(sa * x for x in AX[a])), self.sep(tuple(sb * x for x in AX[b])))
                   for ((a, sa), (b, sb)) in CORNERS]
        self.JP = [(self.J[a], self.J[b], self.sep(tuple(AX[a][i] + AX[b][i] for i in range(3))))
                   for (a, b) in PLAQ]
        self.JDm = [self.sep(tuple(-x for x in d)) for d in FD]

    def sep(self, d):
        return self.idx((self.sites + np.array(d)) % self.L)

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
    def __init__(self, lat, D, n_occ=None):
        self.lat = lat
        self.D = np.asarray(D, float)
        w, U = np.linalg.eigh(lat.M() + np.diag(self.D))
        n = lat.N // 2 if n_occ is None else int(n_occ)
        self.w = w
        self.n, self.gap, self.E = n, float(w[n] - w[n - 1]), float(w[:n].sum())
        self.Uo, self.Ue = np.ascontiguousarray(U[:, :n]), np.ascontiguousarray(U[:, n:])
        self.P = self.Uo @ self.Uo.T
        self.Dn = 1.0 / (w[:n, None] - w[None, n:])

    def dP_half(self, f, pot=None):
        lat = self.lat
        A = np.zeros((lat.N, lat.N - self.n))
        for a in range(3):
            g = (f[a] * lat.S[a])[:, None]
            np.add.at(A, lat.I, g * self.Ue[lat.J[a]])
            np.add.at(A, lat.J[a], g * self.Ue[lat.I])
        if pot is not None:
            A += pot[:, None] * self.Ue
        return self.Uo @ ((self.Uo.T @ A) * self.Dn)

    def ent(self, Y, i, j):
        return np.einsum('nk,nk->n', Y[i], self.Ue[j]) + np.einsum('nk,nk->n', Y[j], self.Ue[i])


def shifts(L):
    return [tuple((L // 2) * g for g in gg) for gg in itertools.product((0, 1), repeat=3)]


def fourier(lat, field, nq):
    return (np.conj(lat.phase(nq)) @ field) / lat.N


def bond_fields_declared(lat, c, nk, beta=1.0):
    """G1's endpoint-mean rule on the sea's own axis bonds: t_e = t(1 - beta h_e)."""
    h = tensor_from_coords(c)
    ph = lat.phase(nk)
    return [-beta * h[b, b] * (ph + ph[lat.J[b]]) / 4.0 for b in range(3)]


def bond_fields_p2(lat, c, nk, kappa=0.5):
    """SUPPLIED (G2 T7): the unique multiplicity-one T2 nearest-neighbour coupling on 2Z^3."""
    h = tensor_from_coords(c)
    ph = lat.phase(nk)
    par = [(-1.0) ** lat.sites[:, i] for i in range(3)]
    f = [np.zeros(lat.N, complex) for _ in range(3)]
    for cc in range(3):
        a, b = (cc + 1) % 3, (cc + 2) % 3
        f[cc] += kappa * h[a, b] * (par[cc] * (par[a] - par[b])) * (ph + ph[lat.J[cc]]) / 2.0
    return f


def numerical_rank(A, rel=1e-9):
    s = np.linalg.svd(A, compute_uv=False)
    return (0, s) if s.size == 0 or s[0] == 0 else (int(np.sum(s > rel * s[0])), s)


def kvec(nk, L):
    return 2 * np.pi * np.asarray(nk, float) / L


# ================================================================ the statistic catalogue (g5_lib)
PAIR_GROUPS = [('ax', 'J', AX, ['x', 'y', 'z']), ('fd', 'JD', FD, FD_NAMES), ('bd', 'JB', BD, BD_NAMES),
               ('ax2', 'JA2', [tuple(2 * x for x in d) for d in AX], ['2x', '2y', '2z']),
               ('fd2', 'JD2', [tuple(2 * x for x in d) for d in FD], ['2(' + s + ')' for s in FD_NAMES]),
               ('bd2', 'JB2', [tuple(2 * x for x in d) for d in BD], ['2(' + s + ')' for s in BD_NAMES])]


def stat_names():
    names = ['site']
    for g, attr, dirs, nms in PAIR_GROUPS:
        names += [g + ':' + s for s in nms]
    names += ['corner%d' % i for i in range(12)]
    names += ['ccorner%d' % i for i in range(12)]
    names += ['cfd%d' % i for i in range(6)]
    names += ['plaq%d' % i for i in range(3)]
    return names


NAMES = stat_names()
GROUP_ORDER = ['site', 'ax', 'fd', 'bd', 'ax2', 'fd2', 'bd2', 'corner', 'ccorner', 'cfd', 'plaq']


def group_of(nm):
    if nm == 'site':
        return 'site'
    if ':' in nm:
        return nm.split(':')[0]
    return nm.rstrip('0123456789')


GIDX = {g: [i for i, nm in enumerate(NAMES) if group_of(nm) == g] for g in GROUP_ORDER}
NIDX = {nm: i for i, nm in enumerate(NAMES)}


def adjugate4(A):
    adj = np.zeros_like(A)
    idx = list(range(4))
    for i in range(4):
        for j in range(4):
            rows = [r for r in idx if r != j]
            cols = [c for c in idx if c != i]
            minor = A[:, rows][:, :, cols]
            adj[:, i, j] = ((-1) ** (i + j)) * np.linalg.det(minor)
    return adj


def _safe_div(num, den, tol=1e-12):
    ok = np.abs(den) > tol
    out = np.zeros(np.broadcast(num, den).shape, dtype=np.result_type(num, den))
    out[ok] = (num / np.where(ok, den, 1.0))[ok]
    return out


class KernelStats:
    def __init__(self, lat, kel):
        self.lat, self.kel = lat, kel

    def _pairs(self):
        out = []
        for g, attr, dirs, nms in PAIR_GROUPS:
            for jj in getattr(self.lat, attr):
                out.append(jj)
        return out

    def values(self):
        lat, kel, I = self.lat, self.kel, self.lat.I
        vals = [np.real(kel(I, I))]
        for jj in self._pairs():
            vals.append(-np.abs(kel(I, jj)) ** 2)
        for (ju, jw) in lat.JC:
            vals.append(2 * np.real(kel(I, ju) * kel(ju, jw) * kel(jw, I)))
        for (ju, jw) in lat.JC:
            kc = kel(ju, jw) - _safe_div(kel(ju, I) * kel(I, jw), kel(I, I))
            vals.append(-np.abs(kc) ** 2)
        for jd, jm in zip(lat.JD, lat.JDm):
            kc = kel(jm, jd) - _safe_div(kel(jm, I) * kel(I, jd), kel(I, I))
            vals.append(-np.abs(kc) ** 2)
        for (ja, jb, jab) in lat.JP:
            S = np.stack([I, ja, jab, jb], axis=1)
            KS = np.stack([np.stack([kel(S[:, u], S[:, w]) for w in range(4)], -1) for u in range(4)], 1)
            vals.append(np.real(np.linalg.det(KS)))
        return np.array(vals)

    def variations(self, dkel):
        lat, kel, I = self.lat, self.kel, self.lat.I
        out = [np.real(dkel(I, I))]
        for jj in self._pairs():
            out.append(-2 * np.real(np.conj(kel(I, jj)) * dkel(I, jj)))
        for (ju, jw) in lat.JC:
            a, b, c = kel(I, ju), kel(ju, jw), kel(jw, I)
            da, db, dc = dkel(I, ju), dkel(ju, jw), dkel(jw, I)
            out.append(2 * np.real(da * b * c + a * db * c + a * b * dc))
        for (ju, jw) in lat.JC:
            kvv, kuv, kvw = kel(I, I), kel(ju, I), kel(I, jw)
            kc = kel(ju, jw) - _safe_div(kuv * kvw, kvv)
            dkc = (dkel(ju, jw) - _safe_div(dkel(ju, I) * kvw + kuv * dkel(I, jw), kvv)
                   + _safe_div(kuv * kvw * dkel(I, I), kvv ** 2))
            out.append(-2 * np.real(np.conj(kc) * dkc))
        for jd, jm in zip(lat.JD, lat.JDm):
            kvv, kuv, kvw = kel(I, I), kel(jm, I), kel(I, jd)
            kc = kel(jm, jd) - _safe_div(kuv * kvw, kvv)
            dkc = (dkel(jm, jd) - _safe_div(dkel(jm, I) * kvw + kuv * dkel(I, jd), kvv)
                   + _safe_div(kuv * kvw * dkel(I, I), kvv ** 2))
            out.append(-2 * np.real(np.conj(kc) * dkc))
        for (ja, jb, jab) in lat.JP:
            S = np.stack([I, ja, jab, jb], axis=1)
            KS = np.stack([np.stack([kel(S[:, u], S[:, w]) for w in range(4)], -1) for u in range(4)], 1)
            dKS = np.stack([np.stack([dkel(S[:, u], S[:, w]) for w in range(4)], -1) for u in range(4)], 1)
            out.append(np.real(np.einsum('nij,nji->n', adjugate4(KS), dKS)))
        return np.array(out)


def sea_kel(sea):
    P = sea.P
    return lambda i, j: P[i, j]


def sea_response_columns(lat, sea, nk, rule='declared', kappa=0.5):
    ks = KernelStats(lat, sea_kel(sea))
    cols = []
    for p in range(6):
        c = np.zeros(6)
        c[p] = 1.0
        if rule == 'declared':
            fields = bond_fields_declared(lat, c, nk)
        elif rule == 'p2':
            fields = bond_fields_p2(lat, c, nk, kappa)
        elif rule == 'declared+p2':
            fields = [x + y for x, y in zip(bond_fields_declared(lat, c, nk), bond_fields_p2(lat, c, nk, kappa))]
        else:
            raise ValueError(rule)
        acc = 0
        for part in (np.real, np.imag):
            Y = sea.dP_half([part(x) for x in fields])
            var = ks.variations(lambda i, j: sea.ent(Y, i, j))
            acc = acc + (var if part is np.real else 1j * var)
        cols.append(acc)
    return ks.values(), cols


def rows_at_shifts(lat, cols, nk):
    keys = [(nm, G) for G in shifts(lat.L) for nm in NAMES]
    R = np.zeros((len(keys), 6), complex)
    for p in range(6):
        rows = {}
        for G in shifts(lat.L):
            nq = tuple((nk[i] + G[i]) % lat.L for i in range(3))
            for si, nm in enumerate(NAMES):
                rows[(nm, G)] = fourier(lat, cols[p][si], nq)
        R[:, p] = [rows[key] for key in keys]
    return keys, R


def group_rows(keys, g):
    gi = set(GIDX[g])
    return [i for i, key in enumerate(keys) if NIDX[key[0]] in gi]


def conditioned_kernel(P, v0):
    """Lueders/Schur (the determinantal note T3): K' = P - P e e^T P / P_v0v0."""
    p = P[:, v0]
    return P - np.outer(p, p) / P[v0, v0]


def conditioned_dkel(sea, Y, v0):
    P = sea.P
    pv = P[v0, v0]

    def dkel(i, j):
        dPij = sea.ent(Y, i, j)
        dPi0 = sea.ent(Y, i, np.full_like(i, v0))
        dP0j = sea.ent(Y, np.full_like(j, v0), j)
        dP00 = sea.ent(Y, np.array([v0]), np.array([v0]))[0]
        return dPij - (dPi0 * P[v0, j] + P[i, v0] * dP0j) / pv + P[i, v0] * P[v0, j] * dP00 / pv ** 2
    return dkel


def support_by_separation(lat, K):
    out = {}
    for s in itertools.product(range(lat.L), repeat=3):
        out[s] = float(np.max(np.abs(K[lat.I, lat.sep(s)])))
    return out


def by_odd(sup):
    b = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0}
    for s, v in sup.items():
        n = sum(x % 2 for x in s)
        b[n] = max(b[n], v)
    return b


# ================================================================ the star tick (g5_lib, from T3)
def star_tick_kernel(lat, order, tau, dhs):
    N = lat.N
    M = lat.M()
    edges = {}
    for a in range(3):
        for v in range(N):
            i, j = int(v), int(lat.J[a][v])
            edges[(min(i, j), max(i, j))] = len(edges)
    EDGES = [None] * len(edges)
    for e, q in edges.items():
        EDGES[q] = e
    STAR = [[] for _ in range(N)]
    for q, (i, j) in enumerate(EDGES):
        STAR[i].append(q)
        STAR[j].append(q)
    NBR = [set() for _ in range(N)]
    for (i, j) in EDGES:
        NBR[i].add(j)
        NBR[j].add(i)
    NQ = len(EDGES)
    G = np.eye(N, dtype=complex)
    dG = [np.zeros((N, N), dtype=complex) for _ in dhs]
    rec = np.zeros(NQ, dtype=bool)
    closed = np.zeros(N, dtype=bool)
    for v in order:
        st = STAR[v]
        new = [q for q in st if not rec[q]]
        rec[st] = True
        if not new or rec.all():
            continue
        for u in {v} | NBR[v]:
            if all(rec[q] for q in STAR[u]):
                closed[u] = True
        act = np.flatnonzero(~closed)
        pos = {int(a): n for n, a in enumerate(act)}
        hR = M[np.ix_(act, act)].copy()
        zero_pairs = []
        for q in np.flatnonzero(rec):
            i, j = EDGES[q]
            if not closed[i] and not closed[j]:
                zero_pairs.append((pos[i], pos[j]))
        for (pi, pj) in zero_pairs:
            hR[pi, pj] = hR[pj, pi] = 0.0
        w, Q = np.linalg.eigh(hR)
        e = np.exp(-1j * tau * w)
        dw = w[:, None] - w[None, :]
        with np.errstate(divide='ignore', invalid='ignore'):
            Phi = (e[:, None] - e[None, :]) / dw
        same = np.abs(dw) < 1e-10
        Phi[same] = (-1j * tau * e[:, None] * np.ones_like(Phi))[same]
        Gi = (Q * e[None, :]) @ Q.T
        Gact = G[act, :]
        for d, dh in enumerate(dhs):
            E = dh[np.ix_(act, act)].copy()
            for (pi, pj) in zero_pairs:
                E[pi, pj] = E[pj, pi] = 0.0
            dGi = Q @ ((Q.T @ E @ Q) * Phi) @ Q.T
            dG[d][act, :] = Gi @ dG[d][act, :] + dGi @ Gact
        G[act, :] = Gi @ Gact
    return G, dG


def dressing_directions(lat, nk):
    M = lat.M()
    out = []
    for p in range(6):
        c = np.zeros(6)
        c[p] = 1.0
        f = bond_fields_declared(lat, c, nk)
        for part in (np.real, np.imag):
            dh = np.zeros((lat.N, lat.N))
            for b in range(3):
                fb = part(f[b])
                I, J = lat.I, lat.J[b]
                dh[I, J] += M[I, J] * fb
                dh[J, I] += M[J, I] * fb
            out.append(dh)
    return out


def dP_full(sea, dh):
    A = sea.Uo.T @ dh @ sea.Ue
    Y = sea.Uo @ (A * sea.Dn) @ sea.Ue.T
    return Y + Y.T


# ================================================================ finite group O (g5_lib)
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


def _order(Rm):
    A = np.eye(3, dtype=int)
    for n in range(1, 7):
        A = A @ Rm
        if np.array_equal(A, np.eye(3, dtype=int)):
            return n
    raise RuntimeError


CLASSES = ['E', 'C3', 'C2', 'C4', "C2'"]
CHAR = {'A1': [1, 1, 1, 1, 1], 'A2': [1, 1, 1, -1, -1], 'E': [2, -1, 2, 0, 0],
        'T1': [3, 0, -1, 1, -1], 'T2': [3, 0, -1, -1, 1]}
GO = cubic_group()
CL = []
for _Rm in GO:
    if int(np.trace(_Rm)) == 3:
        CL.append('E')
    elif _order(_Rm) == 3:
        CL.append('C3')
    elif _order(_Rm) == 4:
        CL.append('C4')
    else:
        CL.append('C2' if np.count_nonzero(_Rm - np.diag(np.diag(_Rm))) == 0 else "C2'")


def decompose(chi):
    out = {}
    for irr, ch in CHAR.items():
        s = sum(chi[i] * ch[CLASSES.index(CL[i])] for i in range(24))
        out[irr] = int(round(s / 24))
        assert abs(s / 24 - out[irr]) < 1e-9
    return out


def fmt(mult):
    return '+'.join((f"{v}{k}" if v > 1 else k) for k, v in mult.items() if v)


def shape_rep(shapes, group):
    def canon(S):
        pts = sorted(S)
        m = pts[0]
        base = frozenset(tuple(p[i] - m[i] for i in range(3)) for p in pts)
        if group == 'full':
            return base
        if group == 'even':
            return (base, sum(m) % 2)
        return (base, tuple(x % 2 for x in m))
    classes = set(canon(S) for S in shapes)
    reps = {}
    for S in shapes:
        reps.setdefault(canon(S), S)
    chi = []
    for Rm in GO:
        fixed = 0
        for c, S in reps.items():
            RS = frozenset(tuple(int(x) for x in (Rm @ np.array(p))) for p in S)
            if canon(RS) == c:
                fixed += 1
        chi.append(fixed)
    return len(classes), chi


def shapes_of(kind):
    def all_base(offs):
        out = []
        for b in itertools.product((0, 1), repeat=3):
            out.append(frozenset(tuple(b[i] + o[i] for i in range(3)) for o in offs))
        return out
    Z = (0, 0, 0)
    fam = {'site': [[Z]],
           'ax': [[Z, d] for d in AX],
           'fd': [[Z, d] for d in FD],
           'bd': [[Z, d] for d in BD],
           'ax2': [[Z, tuple(2 * x for x in d)] for d in AX],
           'fd2': [[Z, tuple(2 * x for x in d)] for d in FD],
           'bd2': [[Z, tuple(2 * x for x in d)] for d in BD],
           'corner': [[Z, tuple(sa * x for x in AX[a]), tuple(sb * x for x in AX[b])]
                      for ((a, sa), (b, sb)) in CORNERS],
           'cfd': [[tuple(-x for x in d), Z, d] for d in FD],
           'plaq': [[Z, AX[a], AX[b], tuple(AX[a][i] + AX[b][i] for i in range(3))] for (a, b) in PLAQ]}[kind]
    shapes = []
    for offs in fam:
        shapes += all_base(offs)
    return shapes


# ================================================================ the read metric (g5_lib, task 3)
READ_EDGES = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
WBD = np.array([1, 1, 1])
S_SEA = -(1 / np.sqrt(2)) * np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1]], float)


def edge_map6():
    rows = []
    for w in READ_EDGES:
        w = np.array(w)
        rows.append([w @ tensor_from_coords(np.eye(6)[p]) @ w / (2.0 * (w @ w)) for p in range(6)])
    return np.array(rows)


def gauge_projectors(k):
    k = np.asarray(k, float)
    n = k / np.linalg.norm(k)
    T = tt_basis(k)
    Pab = np.eye(3) - np.outer(n, n)
    psi = coords_from_tensor(Pab / np.sqrt(2.0))
    gauge = []
    for a in range(3):
        xi = np.eye(3)[a]
        gauge.append(coords_from_tensor(np.outer(n, xi) + np.outer(xi, n)))
    Gq, _ = np.linalg.qr(np.array(gauge).T)
    return T, psi, Gq


READ7 = ['site', 'ax:x', 'ax:y', 'ax:z', 'fd:x+y', 'fd:x+z', 'fd:y+z', 'bd:x+y+z']
READ7_IDX = [NIDX[n] for n in READ7]
E6 = edge_map6()
E6I = np.linalg.inv(E6)


def read_map(lat, vals, cols, nk):
    """g5_task3_reading.read_map: l_e/l_0 = J_e/J_e^0 with J_e = <n_v n_w> = K_vv K_ww - |K_vw|^2."""
    v7 = vals[READ7_IDX]
    c7 = [c[READ7_IDX] for c in cols]
    jmaps = [lat.J[0], lat.J[1], lat.J[2], lat.JD[0], lat.JD[2], lat.JD[4], lat.JB[0]]
    k = kvec(nk, lat.L)
    site0 = v7[0]
    J0, dJ, phases, spread = [], [], [], []
    for e, jm in enumerate(jmaps):
        Je = site0 * site0[jm] + v7[1 + e]
        J0.append(float(Je.mean()))
        spread.append(float(np.max(np.abs(Je - Je.mean()))))
        w = np.array(READ_EDGES[e]) if e < 6 else WBD
        phases.append(0.5 * (1.0 + np.exp(1j * (k @ w))))
        dJ.append([fourier(lat, site0[jm] * c7[p][0] + site0 * c7[p][0][jm] + c7[p][1 + e], nk)
                   for p in range(6)])
    J0, dJ, phases = np.array(J0), np.array(dJ), np.array(phases)
    dl = dJ / J0[:, None]
    H = E6I @ (dl[:6] / phases[:6, None])
    return dict(L=lat.L, nk=nk, k=k, J0=J0, spread=spread, dl=dl, phases=phases, H=H)


def read_analyse(rd):
    """g5_task3_reading.analyse: rank, slaving, metricity, gauge content, Regge residual."""
    k, H = rd['k'], rd['H']
    rk, sv = numerical_rank(H)
    S = H[3:, :3] @ np.linalg.pinv(H[:3, :3])
    slav = float(np.max(np.abs(H[3:, :] - S @ H[:3, :])))
    dS = float(np.max(np.abs(S - S_SEA)))
    ph_bd = rd['phases'][6]
    bd_read = abs(rd['dl'][6][0])
    bd_pred = abs(ph_bd * (WBD @ tensor_from_coords(H[:, 0]) @ WBD) / 6.0)
    T, psi, Gq = gauge_projectors(k)

    def frac(h):
        n2 = float(np.vdot(h, h).real)
        if n2 < 1e-300:
            return (0.0, 0.0, 0.0)
        return (float(np.linalg.norm(T.T @ h) ** 2 / n2), float(abs(np.vdot(psi, h)) ** 2 / n2),
                float(np.linalg.norm(Gq.T @ h) ** 2 / n2))
    Htt = H @ T
    rtt, stt = numerical_rank(T.T @ Htt)
    fr_tt = [frac(Htt[:, j]) for j in range(2)]
    k4 = np.r_[k, 0.0]
    Q, M = Q_of(k4), M_am(k4)
    QM = Q @ M
    sv_sp = np.linalg.svd(QM[:, [0, 1, 2, 4, 5, 7]], compute_uv=False)
    nzero = int(np.sum(sv_sp < 1e-9 * sv_sp[0]))
    phys = np.stack([M.conj().T @ QM @ h10_from_c6(T[:, 0]), M.conj().T @ QM @ h10_from_c6(T[:, 1]),
                     M.conj().T @ QM @ h10_from_c6(psi)], 1)
    regge = {}
    for lab, hin, hrd in [('plus', T[:, 0], Htt[:, 0]), ('cross', T[:, 1], Htt[:, 1])]:
        Ein = M.conj().T @ QM @ h10_from_c6(hin)
        Erd = M.conj().T @ QM @ h10_from_c6(hrd)
        nin, nrd = np.linalg.norm(Ein), np.linalg.norm(Erd)
        cosang = abs(np.vdot(Ein, Erd)) / (nin * nrd) if nin > 0 and nrd > 0 else 0.0
        coef = np.linalg.lstsq(phys, Erd, rcond=None)[0]
        regge[lab] = (float(cosang), np.abs(coef))
    return dict(rank=rk, sv=sv, gain=H[0, 0], slav=slav, dS=dS, bd=(bd_read, bd_pred),
                fr_tt=fr_tt, ttsv=stt, ttrank=rtt, nzero=nzero, regge=regge)


# ================================================================ Regge (g5_task3_reading, from G1)
HC = R4.HCOMPS
DIRS = np.array(R4.DIRS15, float)
L0 = np.sqrt((DIRS ** 2).sum(1))


def precompute_terms():
    """G1's runner precompute_terms: the landed area / deficit gradient rows as sum_j c_j e^{i k a_j}."""
    a_terms, d_terms = [], []
    for tri in R4.TRI_CLASSES:
        vts = [np.array(x) for x in tri]
        qvals, einfo = [], []
        for (i, j) in [(0, 1), (0, 2), (1, 2)]:
            cls, anc = R4.edge_class(tuple(vts[i]), tuple(vts[j]))
            v = np.array(R4.DIRS15[cls])
            qvals.append(float(v @ v))
            einfo.append((cls, anc, float(np.sqrt(v @ v))))
        aout = R4.AREA(*qvals)
        at = [(cls, np.array(anc, float), 2 * ell * float(aout[1 + n])) for n, (cls, anc, ell) in enumerate(einfo)]
        dt = []
        for vs in R4.STARS[tri]:
            loc = {v: i for i, v in enumerate(vs)}
            hl = sorted([loc[tri[0]], loc[tri[1]], loc[tri[2]]])
            miss = tuple(sorted([i for i in range(5) if i not in hl]))
            qv, edata = [], []
            for (i, j) in R4.PAIRS5:
                cls, anc = R4.edge_class(vs[i], vs[j])
                v = np.array(R4.DIRS15[cls])
                qv.append(float(v @ v))
                edata.append((cls, anc, float(np.sqrt(v @ v))))
            out = R4.THETA[miss](*qv)
            dt += [(cls, np.array(anc, float), -2 * ell * float(out[1 + n])) for n, (cls, anc, ell) in enumerate(edata)]
        for src, dst in ((at, a_terms), (dt, d_terms)):
            W = np.zeros((len(src), 15))
            anc = np.zeros((len(src), 4))
            for r, (cls, a, c) in enumerate(src):
                W[r, cls] = c
                anc[r] = a
            dst.append((anc, W))
    return a_terms, d_terms


A_TERMS, D_TERMS = precompute_terms()


def Q_of(k4):
    K = np.asarray(k4, float)[None]
    Q = np.zeros((15, 15), complex)
    for (anc_a, Wa), (anc_d, Wd) in zip(A_TERMS, D_TERMS):
        A = np.exp(1j * (K @ anc_a.T)) @ Wa
        D = np.exp(1j * (K @ anc_d.T)) @ Wd
        Q += 0.5 * (np.conj(A)[0][:, None] * D[0][None, :] + np.conj(D)[0][:, None] * A[0][None, :])
    return Q


def M_am(k4):
    k4 = np.asarray(k4, float)
    M = np.zeros((15, 10), complex)
    for ci, vv in enumerate(DIRS):
        ph = 0.5 * (1.0 + np.exp(1j * (k4 @ vv)))
        for hj, (a, b) in enumerate(HC):
            M[ci, hj] = ph * vv[a] * vv[b] * (2 if a != b else 1) / (2 * L0[ci])
    return M


def h10_from_c6(c):
    h = np.zeros(10, complex)
    h[0], h[1], h[2] = c[0], c[1], c[2]
    h[4] = c[3] / np.sqrt(2)
    h[5] = c[5] / np.sqrt(2)
    h[7] = c[4] / np.sqrt(2)
    return h


# ================================================================ shared configurations
TW, LAT, SEA = {}, {}, {}
for _L in (6, 8, 12):
    TW[_L] = choose_twist(_L, 'pi')[1]
    LAT[_L] = Lattice(_L, TW[_L][0], 'pi')
    for _m in (0.0, 1.0):
        SEA[(_L, _m)] = Sea(LAT[_L], _m * LAT[_L].eps)
LAT0 = Lattice(8, choose_twist(8, 'zero')[1][0], 'zero')
ZERO = {m: Sea(LAT0, m * LAT0.eps) for m in (0.0, 1.0)}

RESP = {}


def resp(tag, lat, sea, nk, rule='declared'):
    key = (tag, nk, rule)
    if key not in RESP:
        vals, cols = sea_response_columns(lat, sea, nk, rule=rule)
        keys, R = rows_at_shifts(lat, cols, nk)
        RESP[key] = (lat, vals, cols, keys, R)
    return RESP[key]


def shear_max(R, keys):
    return max(float(np.max(np.abs(R[group_rows(keys, g)][:, 3:]))) for g in GROUP_ORDER)


def gmax(R, keys, g):
    return float(np.max(np.abs(R[group_rows(keys, g)][:, :3])))


# ================================================================ (i) provenance
E_REF = {6: -258.857540, 8: -611.811768, 12: -2063.196887}
G_REF = {6: 3.464102, 8: 2.651309, 12: 1.793151}
P_REF = {6: 0.199736, 8: 0.199157, 12: 0.198997}
ok = True
prov = []
for L in (6, 8, 12):
    lat, sea = LAT[L], SEA[(L, 0.0)]
    p1 = float(np.max(np.abs(sea.P[lat.I, lat.J[0]])))
    pv = float(np.max(np.abs(np.diag(sea.P) - 0.5)))
    ok &= (abs(sea.E - E_REF[L]) < 1e-5 and abs(sea.gap - G_REF[L]) < 1e-5
           and abs(p1 - P_REF[L]) < 1e-5 and pv < 1e-14)
    prov.append("%d^3 %.6f/%.6f/%.6f" % (L, sea.E, sea.gap, p1))
ax_tt = {}
for (L, m, nk) in ((6, 0.0, (1, 0, 0)), (6, 0.0, (1, 1, 1)), (12, 0.0, (1, 2, 3))):
    _, _, _, keys, R = resp('sea L=%d m=%g' % (L, m), LAT[L], SEA[(L, m)], nk)
    ax_tt[(L, nk)] = numerical_rank(R[group_rows(keys, 'ax')] @ tt_basis(kvec(nk, L)))[1]
s1 = ax_tt[(6, (1, 0, 0))][0]
s2 = ax_tt[(6, (1, 1, 1))]
s3 = ax_tt[(12, (1, 2, 3))]
_, _, _, k12, R12 = resp('sea L=12 m=1', LAT[12], SEA[(12, 1.0)], (1, 0, 0))
plq = gmax(R12, k12, 'plaq')
kp = np.array([0.41, -0.23, 0.67, 0.0])
dq = float(np.max(np.abs(Q_of(kp) - R4.bloch_Q(kp))))
ok &= (abs(s1 - 0.030359) < 1e-6 and abs(s2[0] - 0.013664) < 1e-6 and abs(s2[1] - 0.013664) < 1e-6
       and abs(s3[1] / s3[0] - 0.2924) < 1e-4 and abs(plq - 7.180e-3) < 1e-6 and dq < 1e-14)
check("(i)", "provenance: G2's sea, its TT values, and the landed Regge operator", ok,
      "twists (0,0,0)/(1,1,1)/(1,1,1); E_sea/gap/max|P|sep1 %s; max|P_vv-1/2| <= 1e-14; axis-row TT sv %.6f, "
      "%.6f/%.6f (6^3), ratio %.4f (12^3 (1,2,3)); plaquette %.3e; |Q_of - bloch_Q| %.1e"
      % ("; ".join(prov), s1, s2[0], s2[1], s3[1] / s3[0], plq, dq))

# ================================================================ (ii) T1 representation content
T2mult, ncl = {}, {}
for kind in ['site', 'ax', 'fd', 'bd', 'ax2', 'fd2', 'bd2', 'corner', 'cfd', 'plaq']:
    for grp in ('full', 'even', '2Z3'):
        n, chi = shape_rep(shapes_of(kind), grp)
        T2mult[(kind, grp)] = decompose(chi)['T2']
        ncl[(kind, grp)] = n
met = decompose([(np.trace(Rm) ** 2 + np.trace(Rm @ Rm)) / 2 for Rm in GO])
diag_ev = [k for k in ('fd', 'bd', 'fd2', 'bd2', 'corner', 'cfd') if T2mult[(k, 'even')] >= 1]
ok = (len(diag_ev) == 6 and T2mult[('corner', 'full')] == 2 and T2mult[('corner', 'even')] == 4
      and T2mult[('corner', '2Z3')] == 14 and T2mult[('plaq', 'full')] == 0 and T2mult[('plaq', 'even')] == 1
      and T2mult[('ax', 'full')] == 0 and T2mult[('ax', 'even')] == 0 and T2mult[('ax', '2Z3')] == 1
      and T2mult[('site', 'even')] == 0 and T2mult[('ax2', 'even')] == 0
      and fmt(met) == 'A1+E+T2' and ncl[('fd', 'even')] == 12 and ncl[('corner', 'even')] == 24)
check("(ii)", "T1 every diagonal pair, corner and collinear diagonal carries T2", ok,
      "T2 multiplicity [Z^3|even-sum|2Z^3], thirty decompositions: site 0|0|0, axis 0|0|1, second axis 0|0|0, "
      "face diag 1|2|8, body diag 1|1|4, second face/body diag 1|2 each, corner 2|4|14 (24 vacuum classes), "
      "collinear face diag 1|2|6, staggered plaquette 0|1|4; the metric carries %s" % fmt(met))

# ================================================================ (iii) T1 the six-edge map, the coupling zero
row_xy = E6I[3] / np.sqrt(2)
Efull = np.vstack([E6, [[WBD @ tensor_from_coords(np.eye(6)[p]) @ WBD / 6.0 for p in range(6)]]])
coef7 = np.linalg.lstsq(E6.T, Efull[6], rcond=None)[0]
worst = 0.0
for p in (3, 4, 5):
    c = np.zeros(6)
    c[p] = 1.0
    for nk in ((1, 0, 0), (1, 2, 3), (2, 3, 5)):
        worst = max(worst, max(float(np.max(np.abs(f))) for f in bond_fields_declared(LAT[8], c, nk)))
c = np.zeros(6)
c[0] = 1.0
diag_in = max(float(np.max(np.abs(f))) for f in bond_fields_declared(LAT[8], c, (1, 0, 0)))
ok = (abs(np.linalg.det(E6) + 0.005524) < 1e-6 and np.allclose(row_xy, [-1, -1, 0, 2, 0, 0], atol=1e-12)
      and np.linalg.matrix_rank(Efull, tol=1e-12) == 6
      and np.allclose(coef7, [-1 / 3, -1 / 3, -1 / 3, 2 / 3, 2 / 3, 2 / 3], atol=1e-12)
      and worst == 0.0 and diag_in > 0.4)
check("(iii)", "T1 the six-edge map is invertible and the shear dressing fields are an exact zero", ok,
      "det E6 = %.6f; the h_xy row of E6^-1 is %s, so h_ab = 2 dl_{a+b} - dl_a - dl_b; the seven rows with the "
      "body diagonal have rank 6, forcing dl_{x+y+z} = -(sum dl_a)/3 + 2(sum dl_{a+b})/3 (coefficients %s); "
      "max|h_e| on every axis bond for the three shear polarisations = %.1e against %.3f for h_xx"
      % (np.linalg.det(E6), np.array2string(row_xy, precision=0, suppress_small=True),
         np.array2string(coef7, precision=4, suppress_small=True), worst, diag_in))

# ================================================================ (iv) T2 the parity zero Z2
odd_max = 0.0
mult_info, supp_lines = [], []
MULT = {}
for L in (8, 12):
    lat = LAT[L]
    odd_max = max(odd_max, max(by_odd(support_by_separation(lat, lat.M() @ lat.M()))[n] for n in (1, 2, 3)))
    sea0 = SEA[(L, 0.0)]
    n = lat.N // 2
    g = int(np.sum(np.abs(sea0.w - sea0.w[n]) < 1e-9))
    MULT[L] = Sea(lat, 0.0 * lat.eps, n_occ=n + g)
    mult_info.append("%d^3 mult %d gap %.6f" % (L, g, MULT[L].gap))
    kernels = [SEA[(L, 0.0)].P, SEA[(L, 1.0)].P, MULT[L].P]
    for m in (0.0, 1.0):
        wT, UT = np.linalg.eigh(lat.M() + m * np.diag(lat.eps))
        kernels.append((UT * (1.0 / (1.0 + np.exp(wT)))[None, :]) @ UT.T)
    worst_L = 0.0
    for K in kernels:
        b = by_odd(support_by_separation(lat, K))
        worst_L = max(worst_L, b[2], b[3])
    supp_lines.append("%d^3 %.1e" % (L, worst_L))
    globals()['Z2_%d' % L] = worst_L
M2z = LAT0.M() @ LAT0.M()
fdz = max(float(np.max(np.abs(M2z[LAT0.I, jd]))) for jd in LAT0.JD)
ok = (odd_max == 0.0 and max(Z2_8, Z2_12) < 8e-16 and abs(fdz - 2.0) < 1e-12)
check("(iv)", "T2 the parity zero: every function of H0 has at most one odd coordinate", ok,
      "max|(M^2)_{v,v+s}| = %.1e on every odd separation, so M^2 lives on 2Z^3; with Eps M = -M Eps every f(H0) "
      "is supported on 2Z^3 union (2Z^3 +- e_a). Over the sea (m = 0, 1), the filled 32-fold multiplet (%s) and "
      "the thermal kernel at T = 1, max|K| on 2- and 3-odd separations is %s; zero flux has M^2 face element %.1f"
      % (odd_max, "; ".join(mult_info), " and ".join(supp_lines), fdz))

# ================================================================ (v) T2 the chiral zero Z1
z1, alive = [], []
for L in (8, 12):
    lat = LAT[L]
    ev = np.flatnonzero(lat.eps > 0)
    od = np.flatnonzero(lat.eps < 0)
    for m in (0.0, 1.0):
        P = SEA[(L, m)].P
        d = max(float(np.max(np.abs(P[np.ix_(ev, ev)] - 0.5 * np.eye(len(ev))))),
                float(np.max(np.abs(P[np.ix_(od, od)] - 0.5 * np.eye(len(od))))))
        s220 = float(np.max(np.abs(P[lat.I, lat.sep((2, 2, 0))])))
        s222 = float(np.max(np.abs(P[lat.I, lat.sep((2, 2, 2))])))
        (z1 if m == 0.0 else alive).append("%d^3 %.1e/%.1e/%.1e" % (L, d, s220, s222))
        globals()['Z1_%d_%d' % (L, int(m))] = (d, s220, s222)
ok = (Z1_8_0[0] < 1e-15 and Z1_12_0[0] < 1e-15 and Z1_8_0[1] < 1e-15 and Z1_12_0[1] < 1e-15
      and Z1_8_1[1] > 3e-3 and Z1_12_1[1] > 3e-3 and Z1_8_1[2] > 1e-3)
check("(v)", "T2 the chiral zero: at m = 0 the same-sublattice block of P is exactly I/2", ok,
      "max|P_same-sublattice - I/2| / (2,2,0) / (2,2,2): m = 0 %s on both sublattices, so every even-separation "
      "element vanishes and only one-odd separations are alive; m = 1 %s -- the second-neighbour diagonals come "
      "alive with mass, the nearest ones do not"
      % ("; ".join(z1), "; ".join(alive)))

# ================================================================ (vi) T2 the frozen register
p2rows = []
p2ok = True
p2worst = {0: 0.0, 1: 0.0}
p2bd = 0.0
p2min = {'ax': 9.9, 'cc': 9.9, 'pl': 9.9}
p2rk = set()
for m in (0.0, 1.0):
    for nk in ((1, 0, 0), (1, 1, 1)):
        _, _, _, keys, R = resp('sea L=8 m=%g' % m, LAT[8], SEA[(8, m)], nk, rule='p2')
        g = {gg: float(np.max(np.abs(R[group_rows(keys, gg)][:, 3:]))) for gg in GROUP_ORDER}
        _, _, _, keys2, R2 = resp('sea L=8 m=%g' % m, LAT[8], SEA[(8, m)], nk, rule='declared+p2')
        rk = numerical_rank(R2)[0]
        fdrows = float(np.max(np.abs(R2[group_rows(keys2, 'fd')])))
        lim = 1e-30 if m == 0.0 else 1e-18
        p2worst[int(m)] = max(p2worst[int(m)], g['fd'], fdrows)
        p2bd = max(p2bd, g['bd'])
        p2ok &= (g['fd'] <= lim and g['bd'] <= 1e-18 and fdrows <= lim and g['ax'] >= 1.4e-2
                 and g['ccorner'] >= 2.5e-3 and g['plaq'] >= 3.0e-3 and rk == 6)
        for gg, vv in (('ax', g['ax']), ('cc', g['ccorner']), ('pl', g['plaq'])):
            p2min[gg] = min(p2min[gg], vv)
        p2rk.add(rk)
check("(vi)", "T2 the nearest diagonal pair statistics are frozen", p2ok,
      "under G2's period-2 coupling (kappa = 1/2) on the 8^3 sea at m in {0,1}, n = (1,0,0) and (1,1,1): the "
      "nearest face diagonals respond at <= %.1e (m = 0) and <= %.1e (m = 1), the body diagonals at <= %.1e, "
      "against axis pairs >= %.1e, conditioned corners >= %.1e, plaquettes >= %.1e; rank(R) = %s for "
      "declared+p2. The 12^3 blocks are quoted, not re-run."
      % (p2worst[0], p2worst[1], p2bd, p2min['ax'], p2min['cc'], p2min['pl'], sorted(p2rk)))

# ================================================================ (vii) T3 the shear columns
FAM = []
for L, moms in ((6, [(1, 0, 0), (1, 1, 1), (1, 2, 5)]),
                (8, [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 5), (2, 3, 5)])):
    for m in (0.0, 1.0):
        for nk in moms:
            FAM.append(('sea L=%d m=%g' % (L, m), LAT[L], SEA[(L, m)], nk))
for nk in ((1, 0, 0), (1, 1, 1), (1, 2, 3)):
    FAM.append(('sea L=12 m=0', LAT[12], SEA[(12, 0.0)], nk))
FAM.append(('sea L=12 m=1', LAT[12], SEA[(12, 1.0)], (1, 0, 0)))
G8 = int(np.sum(np.abs(SEA[(8, 0.0)].w - SEA[(8, 0.0)].w[LAT[8].N // 2]) < 1e-9))
MULT8 = MULT[8]
WALL8 = Sea(LAT[8], np.where(LAT[8].sites[:, 0] < 4, 1.0, -1.0) * LAT[8].eps)
for nk in ((1, 0, 0), (1, 1, 1)):
    FAM.append(('mult L=8 g=%d' % G8, LAT[8], MULT8, nk))
    FAM.append(('wall L=8', LAT[8], WALL8, nk))
for m in (0.0, 1.0):
    FAM.append(('zero L=8 m=%g' % m, LAT0, ZERO[m], (1, 1, 1)))
shear_all = site_shear = 0.0
for tag, lat, sea, nk in FAM:
    _, vals, cols, keys, R = resp(tag, lat, sea, nk)
    shear_all = max(shear_all, shear_max(R, keys))
    site_shear = max(site_shear, max(float(np.max(np.abs(cols[p]))) for p in range(3, 6)))
sea8 = SEA[(8, 0.0)]
Kc = conditioned_kernel(sea8.P, 0)
ksc = KernelStats(LAT[8], lambda i, j: Kc[i, j])
cond_shear = 0.0
cond_fd = {}
for nk in ((1, 0, 0), (1, 1, 1)):
    ccols = []
    for p in range(6):
        c = np.zeros(6)
        c[p] = 1.0
        fields = bond_fields_declared(LAT[8], c, nk)
        acc = 0
        for part in (np.real, np.imag):
            Y = sea8.dP_half([part(x) for x in fields])
            v = ksc.variations(conditioned_dkel(sea8, Y, 0))
            acc = acc + (v if part is np.real else 1j * v)
        ccols.append(acc)
    ckeys, CR = rows_at_shifts(LAT[8], ccols, nk)
    cond_shear = max(cond_shear, shear_max(CR, ckeys))
    cond_fd[nk] = (max(float(np.max(np.abs(ccols[p][GIDX['fd']]))) for p in range(3)),
                   max(float(np.max(np.abs(ccols[p][GIDX['ax']]))) for p in range(3)))
ok = (shear_all == 0.0 and site_shear == 0.0 and cond_shear == 0.0)
check("(vii)", "T3 the shear columns are an exact zero on every configuration", ok,
      "over %d of the source's 90 (configuration, momentum) pairs -- sea 6^3/8^3/12^3 at m in {0,1}, filled "
      "multiplet, mass wall, Lueders-conditioned law, zero flux -- and all eleven groups, max|R[:, shear]| = "
      "%.1e in momentum space and %.1e in site space, the shear inputs being the zero vector of (iii); the "
      "conditioned law's face diagonals do respond to the diagonal metric, %.3e against %.3e for the axis "
      "pairs. The other 62 pairs are quoted, not re-run."
      % (len(FAM) + 2, shear_all, site_shear, cond_fd[(1, 0, 0)][0], cond_fd[(1, 0, 0)][1]))

# ================================================================ (viii) T3 the alive T2 carriers
cc = {}
for (L, m, nk) in ((8, 0.0, (1, 0, 0)), (8, 1.0, (1, 0, 0)), (12, 0.0, (1, 1, 1))):
    _, vals, cols, keys, R = resp('sea L=%d m=%g' % (L, m), LAT[L], SEA[(L, m)], nk)
    rtt, stt = numerical_rank(R[group_rows(keys, 'ccorner')] @ tt_basis(kvec(nk, L)))
    cc[(L, m)] = (float(np.max(np.abs(vals[GIDX['ccorner']]))), gmax(R, keys, 'ccorner'), rtt, stt)
_, v81, c81, k81, R81 = resp('sea L=8 m=1', LAT[8], SEA[(8, 1.0)], (1, 0, 0))
fd2v, fd2r, cor_r = float(np.max(np.abs(v81[GIDX['fd2']]))), gmax(R81, k81, 'fd2'), gmax(R81, k81, 'corner')
_, v80, c80, k80, R80 = resp('sea L=8 m=0', LAT[8], SEA[(8, 0.0)], (1, 0, 0))
cor0, corv, fd0 = gmax(R80, k80, 'corner'), float(np.max(np.abs(v80[GIDX['corner']]))), float(np.max(np.abs(v80[GIDX['fd']])))
ok = (abs(cc[(8, 0.0)][0] - 6.3e-3) < 2e-4 and abs(cc[(8, 1.0)][0] - 1.3e-2) < 5e-4
      and 3e-3 < cc[(8, 0.0)][1] < 4.5e-3 and 3e-3 < cc[(8, 1.0)][1] < 4.5e-3
      and cc[(12, 0.0)][2] == 2 and abs(cc[(12, 0.0)][3][0] - 5.522e-3) < 1e-6
      and abs(cc[(12, 0.0)][3][1] - 5.522e-3) < 1e-6 and fd2v > 1e-5 and fd2r > 1e-5
      and cor0 < 1e-18 and corv < 1e-16 and cor_r > 3e-4 and fd0 < 1e-30)
check("(viii)", "T3 the alive T2 carriers on the vacuum read no shear", ok,
      "the conditioned corner pair -|K_uw - K_uv K_vw/K_vv|^2 is alive at %.3e (m = 0) and %.3e (m = 1), "
      "responds to the diagonal metric at %.1e and %.1e, TT rank %d on 12^3 (1,1,1), sv %.3e/%.3e; second face "
      "diagonals alive only with mass (%.1e, response %.1e); connected corner %.1e, response %.1e (m = 0) and "
      "%.1e (m = 1); nearest face diagonals %.1e"
      % (cc[(8, 0.0)][0], cc[(8, 1.0)][0], cc[(8, 0.0)][1], cc[(8, 1.0)][1], cc[(12, 0.0)][2],
         cc[(12, 0.0)][3][0], cc[(12, 0.0)][3][1], fd2v, fd2r, corv, cor0, cor_r, fd0))

# ================================================================ (ix) T3 what breaks the vacuum zero
brk = {}
for m in (0.0, 1.0):
    b = by_odd(support_by_separation(LAT0, ZERO[m].P))
    brk[m] = (b[2], b[3])
wfd = [float(np.max(np.abs(WALL8.P[LAT[8].I, jd]))) for jd in LAT[8].JD]
bw = by_odd(support_by_separation(LAT[8], WALL8.P))
bc = by_odd(support_by_separation(LAT[8], Kc))
a0, b0 = sea8.P[0, LAT[8].J[0][0]], sea8.P[0, LAT[8].J[1][0]]
cf = Kc[LAT[8].J[0][0], LAT[8].J[1][0]]
Pm = MULT8.P - sea8.P
psi1 = Pm[:, 0] / np.linalg.norm(Pm[:, 0])
b1 = by_odd(support_by_separation(LAT[8], sea8.P + np.outer(psi1, psi1)))
bmul = by_odd(support_by_separation(LAT[8], MULT8.P))
ok = (brk[0.0][0] < 1e-15 and brk[0.0][1] > 5e-2 and brk[1.0][0] > 2e-2
      and min(wfd[:4]) > 2.8e-2 and max(wfd[4:]) < 1e-15 and bw[3] < 1e-15
      and bc[2] > 7e-2 and bc[3] < 1e-15 and abs(cf + 2 * a0 * b0) < 1e-15 and abs(cf + 0.079327) < 1e-6
      and b1[2] > 1e-2 and b1[3] < 1e-15 and bmul[2] < 8e-16 and bmul[3] < 8e-16)
check("(ix)", "T3 what breaks the vacuum zero, and what does not", ok,
      "face/body-diagonal max|K|: zero flux m = 0 %.1e/%.1e (Z1 intact), m = 1 %.1e/%.1e; the wall breaks only "
      "the diagonals crossing it, x+-y and x+-z at %.1e against %.1e for y+-z, never the body diagonal (%.1e); "
      "conditioning at v0 = 0 gives %.1e/%.1e with K'_{v0+x,v0+y} = -2 P_{v0,v0+x} P_{v0,v0+y} = %.6f exact to "
      "%.1e; a symmetry-breaking multiplet member %.1e/%.1e, the filled multiplet %.1e/%.1e"
      % (brk[0.0][0], brk[0.0][1], brk[1.0][0], brk[1.0][1], min(wfd[:4]), max(wfd[4:]), bw[3],
         bc[2], bc[3], cf, abs(cf + 2 * a0 * b0), b1[2], b1[3], bmul[2], bmul[3]))

# ================================================================ (x) T3 the rotated law
TAU, RNK = 0.5, (1, 0, 0)
lat6, sea6 = LAT[6], SEA[(6, 0.0)]
dhs = dressing_directions(lat6, RNK)
dPs = [dP_full(sea6, dh) for dh in dhs]
orders = [[int(i) for i in lat6.idx((lat6.sites + np.array(t)) % 6)]
          for t in itertools.product(range(0, 6, 2), repeat=3)]
Ssum, Rsum, Ksum = 0, None, 0
for o in orders:
    G, dG = star_tick_kernel(lat6, o, TAU, dhs)
    GP = G @ sea6.P
    K = GP @ G.conj().T
    Ksum = Ksum + K
    ks = KernelStats(lat6, lambda i, j: K[i, j])
    Ssum = Ssum + ks.values()
    dKs = [dG[d] @ GP.conj().T + G @ dPs[d] @ G.conj().T + GP @ dG[d].conj().T for d in range(12)]
    rc = []
    for p in range(6):
        dK, dKi = dKs[2 * p], dKs[2 * p + 1]
        rc.append(ks.variations(lambda i, j: dK[i, j]) + 1j * ks.variations(lambda i, j: dKi[i, j]))
    Rsum = rc if Rsum is None else [a + b for a, b in zip(Rsum, rc)]
nord = len(orders)
rvals = Ssum / nord
rcols = [c / nord for c in Rsum]
rkeys, RR = rows_at_shifts(lat6, rcols, RNK)
ekept = float(np.trace(lat6.M() @ (Ksum / nord)).real / sea6.E)
ax_mean = float(rvals[GIDX['ax']].mean())
fd_val = float(np.max(np.abs(rvals[GIDX['fd']])))
fd_rows = float(np.max(np.abs(RR[group_rows(rkeys, 'fd')])))
ax_ttsv = numerical_rank(RR[group_rows(rkeys, 'ax')] @ tt_basis(kvec(RNK, 6)))[1][0]
cor_val = float(np.max(np.abs(rvals[GIDX['corner']])))
cor_res = gmax(RR, rkeys, 'corner')
rot_shear = shear_max(RR, rkeys)
site_dev = float(np.max(np.abs(rvals[0] - 0.5)))
ok = (rot_shear == 0.0 and abs(ax_mean + 0.011307) < 1e-6 and abs(fd_val - 8.720e-3) < 1e-5
      and abs(fd_rows - 4.301e-3) < 1e-5 and abs(ax_ttsv - 0.018187) < 1e-6 and abs(ekept - 0.2346) < 1e-4
      and cor_val < 2.5e-17 and cor_res < 2.5e-17 and site_dev < 1e-13)
check("(x)", "T3 the rotated law: alive nearest face diagonals, still shear-blind", ok,
      "6^3, twist %s, tau = 0.5, T3's %d-order even family at (1,0,0): energy kept %.4f, site 1/2 to %.1e, axis "
      "pair mean %.6f, nearest face diagonals alive at %.3e with diagonal response %.3e, axis-row TT sv %.6f -- "
      "all T3's; the connected corner three-point is exactly zero in value (%.1e) and response (%.1e) on every "
      "rotated law; shear columns %.1e. The four other momenta are quoted, not re-run."
      % (str(TW[6][0]), nord, ekept, site_dev, ax_mean, fd_val, fd_rows, ax_ttsv, cor_val, cor_res, rot_shear))

# ================================================================ the reading
READS = {}
READ_FAM = [('sea L=8 m=0', LAT[8], SEA[(8, 0.0)], [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 5), (2, 3, 5)]),
            ('sea L=8 m=1', LAT[8], SEA[(8, 1.0)], [(1, 0, 0), (1, 1, 1)]),
            ('sea L=12 m=0', LAT[12], SEA[(12, 0.0)], [(1, 0, 0), (1, 1, 1)]),
            ('sea L=6 m=0', LAT[6], SEA[(6, 0.0)], [(1, 0, 0), (1, 1, 1)]),
            ('mult L=8 g=%d' % G8, LAT[8], MULT8, [(1, 0, 0), (1, 1, 1)]),
            ('zero L=8 m=1', LAT0, ZERO[1.0], [(1, 1, 1)])]
for rtag, rlat, rsea, rmoms in READ_FAM:
    for rnk in rmoms:
        _, rv, rc2, _, _ = resp(rtag, rlat, rsea, rnk)
        READS[(rtag, rnk)] = read_analyse(read_map(rlat, rv, rc2, rnk))
READS[('rot L=6 even', (1, 0, 0))] = read_analyse(read_map(lat6, rvals, rcols, (1, 0, 0)))

# ================================================================ (xi) T4 rank 3 and the slaved shear
ranks = set(r['rank'] for r in READS.values())
slav = max(r['slav'] for r in READS.values())
dS0 = max(r['dS'] for k, r in READS.items() if k[0].startswith('sea') and k[0].endswith('m=0'))
dS1 = min(r['dS'] for k, r in READS.items() if k[0] == 'sea L=8 m=1')
dSr = READS[('rot L=6 even', (1, 0, 0))]['dS']
gains = [abs(READS[('sea L=%d m=0' % L, (1, 0, 0))]['gain']) for L in (6, 8, 12)]
ok = (ranks == {3} and slav < 2.0e-13 and dS0 <= 2.2e-12 and dS1 > 0.3 and dSr > 2.0
      and abs(gains[0] - 0.2360) < 1e-4 and abs(gains[1] - 0.2195) < 1e-4 and abs(gains[2] - 0.2073) < 1e-4)
check("(xi)", "T4 the read metric has rank 3 and its shear is slaved", ok,
      "under l_e/l_0 = J_e/J_e^0 with J_e = <n_v n_{v+e}>: rank(H_read) = %s on all %d recomputed lines of the "
      "source's 36, |H_read[shear] - S H_read[diag]| <= %.1e; on the massless sea S is exactly h_ab = "
      "-(h_aa + h_bb)/2, |S - S_sea| <= %.1e everywhere, calibration-free; with mass >= %.2f, rotated %.2f with "
      "an O(1) phase; gain at (1,0,0) %.4f/%.4f/%.4f on 6^3/8^3/12^3, under-reading by 4-5"
      % (sorted(ranks), len(READS), slav, dS0, dS1, dSr, gains[0], gains[1], gains[2]))

# ================================================================ (xii) T4 the gauge-invariant content
ax8, bd8, bd12 = READS[('sea L=8 m=0', (1, 0, 0))], READS[('sea L=8 m=0', (1, 1, 1))], READS[('sea L=12 m=0', (1, 1, 1))]
gen = [READS[('sea L=8 m=0', (1, 2, 5))], READS[('sea L=8 m=0', (2, 3, 5))]]
psi_ax = ax8['fr_tt'][0][1]
psi_bd = max(bd8['fr_tt'][0][1], bd8['fr_tt'][1][1], bd12['fr_tt'][0][1], bd12['fr_tt'][1][1])
psi_gen = [g['fr_tt'][0][1] for g in gen]
ok = (abs(ax8['fr_tt'][0][0] - 2 / 3) < 1e-9 and abs(ax8['fr_tt'][0][2] - 1 / 3) < 1e-9 and psi_ax < 1e-31
      and abs(bd8['fr_tt'][0][0] - 8 / 9) < 1e-9 and abs(bd8['fr_tt'][1][0] - 8 / 9) < 1e-9 and psi_bd < 1e-31
      and abs(bd8['ttsv'][0] - 0.1846) < 1e-4 and abs(bd8['ttsv'][1] - 0.1846) < 1e-4
      and abs(bd12['ttsv'][0] - 0.1918) < 1e-4 and abs(bd12['ttsv'][1] - 0.1918) < 1e-4
      and abs(ax8['regge']['plus'][0] - 1.0) < 1e-9 and ax8['regge']['plus'][1][1] < 1e-16
      and abs(bd8['regge']['plus'][0] - 1.0) < 1e-9 and abs(bd8['regge']['cross'][0] - 1.0) < 1e-9
      and bd8['regge']['plus'][1][1] < 1e-16 and bd8['regge']['cross'][1][0] < 1e-16
      and ax8['nzero'] == 3 and bd8['nzero'] == 2 and min(psi_gen) > 0.12 and max(psi_gen) < 0.26)
check("(xii)", "T4 on the axis and body-diagonal momenta the slaved shear is pure gauge", ok,
      "(TT, psi, gauge) of a TT input: (%.4f, %.1e, %.4f) on the axis, (%.4f, %.1e, %.4f) on the body diagonal "
      "-- the exact 2/3 + 1/3 and 8/9 + 1/9, no scalar part -- with equal TT gains, TT-in -> TT-read sv "
      "%.4f/%.4f (8^3), %.4f/%.4f (12^3); the Regge residual is parallel to the input's, cos %.3f and %.3f, "
      "cross coefficient %.1e; Q M_AM has %d zero modes on the axis, %d elsewhere; at (1,2,5) and (2,3,5) the "
      "scalar admixture is %.2f and %.2f and the TT modes mix"
      % (ax8['fr_tt'][0][0], psi_ax, ax8['fr_tt'][0][2], bd8['fr_tt'][0][0], bd8['fr_tt'][0][1],
         bd8['fr_tt'][0][2], bd8['ttsv'][0], bd8['ttsv'][1], bd12['ttsv'][0], bd12['ttsv'][1],
         ax8['regge']['plus'][0], bd8['regge']['cross'][0], bd8['regge']['plus'][1][1],
         ax8['nzero'], bd8['nzero'], psi_gen[0], psi_gen[1]))

# ================================================================ (xiii) T4 flat vacuum, non-metric reading
Q0, M0 = Q_of(np.zeros(4)), M_am(np.zeros(4))
flat = 0.0
for c in (np.array([1.0, 1, 1, 0, 0, 0]), np.array([1.02, 1.03, 1.09, 0, 0, 0]),
          np.array([1.0, 1.0, 1.0, 0.3, -0.2, 0.1])):
    flat = max(flat, float(np.max(np.abs(Q0 @ M0 @ h10_from_c6(c)))))
_, jv, jc, _, _ = resp('sea L=8 m=0', LAT[8], SEA[(8, 0.0)], (1, 0, 0))
J0sea = read_map(LAT[8], jv, jc, (1, 0, 0))
bd_lines, rels = [], []
for key, lab in ((('sea L=8 m=0', (1, 0, 0)), 'sea m=0'), (('sea L=8 m=1', (1, 0, 0)), 'sea m=1'),
                 (('mult L=8 g=%d' % G8, (1, 0, 0)), 'multiplet'), (('zero L=8 m=1', (1, 1, 1)), 'zero flux'),
                 (('rot L=6 even', (1, 0, 0)), 'rotated')):
    r, p = READS[key]['bd']
    rels.append(abs(r - p) / max(r, p, 1e-300))
    bd_lines.append("%s %.1e/%.1e" % (lab, r, p))
ok = (flat <= 3e-15 and min(rels) > 0.2 and abs(J0sea['J0'][0] - 0.21034) < 1e-5
      and max(abs(J0sea['J0'][e] - 0.25) for e in (3, 4, 5)) < 1e-14 and max(J0sea['spread']) < 1e-14)
check("(xiii)", "T4 the vacuum is flat and the read geometry is non-metric", ok,
      "the vacuum's joint-occupation values are uniform -- axis %.5f, face diagonals 0.25 exactly, site spread "
      "<= %.1e -- so a uniform read metric (isotropic, 1.02:1.03:1.09, or sheared) is flat: |Q(0) M_AM(0) h| "
      "<= %.1e. Body-diagonal read/predicted per unit h_xx: %s -- the seventh statistic contradicts the metric "
      "the six define by %.0f-%.0f %%"
      % (J0sea['J0'][0], max(J0sea['spread']), flat, "; ".join(bd_lines), 100 * min(rels), 100 * max(rels)))

print("SUPPLIED, not derived: the fermion law; the pi-flux sea, its KS signs, twist rule and m; beta = nu_r = 1 "
      "and the endpoint-mean rule; the joint-occupation reading and its unit per-class coefficient; the star "
      "tick, tau = 0.5 and its order family; the Lueders clause; the period-2 coupling and kappa; the wall, the "
      "multiplet, v0; the Regge action and G; the TT conventions.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
