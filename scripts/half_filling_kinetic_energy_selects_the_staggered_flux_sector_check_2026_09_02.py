#!/usr/bin/env python3
"""Finite signed-hopping comparisons at supplied occupation and energy scale.

The edge carrier has even total parity; odd-N values are abstract Fock
comparisons. Exact bit/integer/surd certificates are distinguished from finite
floating ladders, exhaustive eight-twist comparisons, the unchanged2000 draws
and500-subset protocol, finite descent and numerical Bloch integrals. The
L=96 crossing is an interpolation diagnostic, not certified limiting digits.
No physical state selection, Record readout, clock or sector dynamics follows.
All original19 check IDs and computational sample parameters are retained.
"""

from __future__ import annotations

import itertools
import math
import hashlib
from pathlib import Path
import sys
from collections import deque

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 120

# Publication/governing/attribution context; no imported scientific helper.
AUDIT_INPUT_PATHS = ('docs/HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/COMPOSITION_DISCRIMINATOR_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-02.md')
INPUT_SHA256 = {'docs/HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02.md': '90d54fc40515a39a318f23d21d7c2fcaa54e0d92dc4872e573a9a63705b28af1', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/COMPOSITION_DISCRIMINATOR_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-02.md': 'fd39a661c586a52610b6bce3907fd857c7ab94e6fdc0c9b7cc2e14dc179763a9'}

def verify_inputs():
    root = Path(__file__).resolve().parents[1]
    if set(AUDIT_INPUT_PATHS) != set(INPUT_SHA256):
        raise RuntimeError("input declaration/pin mismatch")
    for rel in AUDIT_INPUT_PATHS:
        if hashlib.sha256((root / rel).read_bytes()).hexdigest() != INPUT_SHA256[rel]:
            raise RuntimeError("changed publication/premise input: " + rel)

verify_inputs()

PASS = 0
FAIL = 0


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


# ================================================ coarse lattice and KS phases

EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
DIRS = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(v, a):
    """KS link sign of the coarse bond (v, v + e_a); axes 0,1,2 = 1,2,3."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def va(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def wrap(v, dims):
    return tuple(v[i] % dims[i] for i in range(3))


def pcnt(n):
    return bin(n).count("1")


class Q:
    """i^k X^x Z^z on a register of qubits indexed by bit position."""

    __slots__ = ("k", "x", "z")

    def __init__(self, k, x, z):
        self.k = k & 3
        self.x = x
        self.z = z

    def __mul__(a, b):
        return Q(a.k + b.k + 2 * pcnt(a.z & b.x), a.x ^ b.x, a.z ^ b.z)

    def scal(s, t):
        return Q(s.k + t, s.x, s.z)

    def neg(s):
        return Q(s.k + 2, s.x, s.z)

    def isI(s):
        return s.x == 0 and s.z == 0 and s.k == 0

    def ismI(s):
        return s.x == 0 and s.z == 0 and s.k == 2

    def vec(s, n):
        return s.x | (s.z << n)


IDQ = Q(0, 0, 0)


def qprod(seq):
    o = IDQ
    for p in seq:
        o = o * p
    return o


class Lat:
    """Coarse cubic block or torus with the BK superfast encoding on its edges."""

    def __init__(self, dims, periodic):
        self.dims = tuple(dims)
        self.per = periodic
        self.V = list(itertools.product(*(range(d) for d in dims)))
        self.nv = len(self.V)
        self.E = []
        for v in self.V:
            for ax in range(3):
                if self.step(v, EX[ax]) is not None:
                    self.E.append((v, ax))
        self.ei = {e: i for i, e in enumerate(self.E)}
        self.nq = len(self.E)
        self.inc = {}
        for v in self.V:
            d = {}
            for r in range(6):
                w = self.step(v, DIRS[r])
                if w is None:
                    continue
                d[r] = (w, self.ei[(v, r - 3) if r >= 3 else (w, r)])
            self.inc[v] = d
        self.star = {v: sum(1 << q for (_, q) in self.inc[v].values()) for v in self.V}
        self.idx = {v: i for i, v in enumerate(self.V)}
        self.rows = np.array([self.idx[self.step(v, EX[ax])] for (v, ax) in self.E])
        self.cols = np.array([self.idx[v] for (v, ax) in self.E])

    def step(self, v, d):
        w = va(v, d)
        if self.per:
            return wrap(w, self.dims)
        return w if all(0 <= w[i] < self.dims[i] for i in range(3)) else None

    def A(self, v, r):
        w, q = self.inc[v][r]
        x, z = 1 << q, 0
        for r2, (_, q2) in self.inc[v].items():
            if r2 < r:
                z ^= 1 << q2
        rb = (r + 3) % 6
        for r2, (_, q2) in self.inc[w].items():
            if r2 < rb:
                z ^= 1 << q2
        p = Q(pcnt(x & z) & 1, x, z)
        return p if r >= 3 else p.neg()

    def Aij(self, i, j):
        for r in range(6):
            if r in self.inc[i] and self.inc[i][r][0] == j:
                return self.A(i, r)
        raise KeyError("not adjacent")

    def B(self, v):
        return Q(0, 0, self.star[v])

    def faces(self):
        out = []
        for v in self.V:
            for d1 in range(3):
                for d2 in range(d1 + 1, 3):
                    a = self.step(v, EX[d1])
                    b = self.step(v, EX[d2])
                    if a is None or b is None:
                        continue
                    c = self.step(a, EX[d2])
                    if c is None:
                        continue
                    out.append((v, a, c, b))
        return out

    def loop(self, cyc):
        n = len(cyc)
        return qprod([self.Aij(cyc[a], cyc[(a + 1) % n]) for a in range(n)]).scal(n)

    def mat(self, s):
        """Real symmetric hopping matrix of the link-sign vector s (edge order)."""
        M = np.zeros((self.nv, self.nv))
        np.add.at(M, (self.rows, self.cols), np.asarray(s, dtype=float))
        return M + M.T

    def imat(self, s):
        """Integer hopping matrix of the link-sign vector s."""
        M = np.zeros((self.nv, self.nv), dtype=np.int64)
        np.add.at(M, (self.rows, self.cols), np.asarray(s, dtype=np.int64))
        return M + M.T

    def EN(self, s, N):
        return float(np.sum(np.sort(np.linalg.eigvalsh(self.mat(s)))[:N]))


def transport(L, path):
    """Ordered product of the encoded hops T_{i_{k+1} i_k} = (i/2) A (B - B).

    On any configuration where every step is legal -- source occupied, target
    empty -- each factor contributes (i/2)(+1 - (-1)) = i, hence the i^n.
    """
    n = len(path) - 1
    ops = [L.Aij(path[k + 1], path[k]) for k in range(n)]
    return qprod(ops[::-1]).scal(n)


def f2_pivots(gens):
    piv = {}
    for j, g in enumerate(gens):
        v, c = g, 1 << j
        while v:
            p = v.bit_length() - 1
            if p in piv:
                pv, pc = piv[p]
                v ^= pv
                c ^= pc
            else:
                piv[p] = (v, c)
                break
    return piv


def f2_express(target, piv):
    v, c = target, 0
    while v:
        p = v.bit_length() - 1
        if p not in piv:
            return None
        pv, pc = piv[p]
        v ^= pv
        c ^= pc
    return c


def f2_relations(gens):
    piv, rel = {}, []
    for j, g in enumerate(gens):
        v, c = g, 1 << j
        while v:
            p = v.bit_length() - 1
            if p in piv:
                pv, pc = piv[p]
                v ^= pv
                c ^= pc
            else:
                piv[p] = (v, c)
                break
        if v == 0:
            rel.append(c)
    return rel, len(piv)


def bits(m):
    out = []
    while m:
        b = m & -m
        out.append(b.bit_length() - 1)
        m ^= b
    return out


def sector_eta(L, face_vals, wilson=(1, 1, 1)):
    """Link-sign field realising the flux sector S_f = face_vals[f] on Lat L.

    Spanning-tree gauge fixing, then fundamental-cycle transport with the
    residual Z4 phase read off, exactly as in the face-transport theorem;
    the face eigenvalues are supplied rather than fixed at -1.  Returns
    (eta, consistent); eta is None when the sector is inconsistent.
    """
    root = L.V[0]
    par = {root: None}
    dq = deque([root])
    while dq:
        v = dq.popleft()
        for r in range(6):
            if r not in L.inc[v]:
                continue
            w = L.inc[v][r][0]
            if w not in par:
                par[w] = v
                dq.append(w)
    tree = {frozenset((v, w)) for w, v in par.items() if v is not None}

    def tpath(v):
        p = [v]
        while par[p[-1]] is not None:
            p.append(par[p[-1]])
        return p[::-1]

    F = L.faces()
    gens = [L.loop(f) for f in F]
    vals = list(face_vals)
    if L.per:
        for ax in range(3):
            cyc = [wrap(tuple((k if i == ax else 0) for i in range(3)), L.dims)
                   for k in range(L.dims[ax])]
            gens.append(transport(L, cyc + [cyc[0]]))
        vals += list(wilson)
    gv = [g.vec(L.nq) for g in gens]
    piv = f2_pivots(gv)
    rels, _ = f2_relations(gv)
    for r in rels:
        idxs = bits(r)
        pr = qprod([gens[j] for j in idxs])
        eps = 1 if pr.isI() else (-1 if pr.ismI() else 0)
        pv = 1
        for j in idxs:
            pv *= vals[j]
        if eps == 0 or pv != eps:
            return None, False
    eta = {}
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        if frozenset((v, w)) in tree:
            eta[(v, ax)] = 1
            continue
        op = transport(L, tpath(v) + [w] + tpath(w)[::-1][1:])
        c = f2_express(op.vec(L.nq), piv)
        if c is None:
            return None, False
        idxs = bits(c)
        resid = (op.k - qprod([gens[j] for j in idxs]).k) & 3
        if resid not in (0, 2):
            return None, False
        e = 1 if resid == 0 else -1
        for j in idxs:
            e *= vals[j]
        eta[(v, ax)] = e
    return eta, True


def hol_list(L, eta):
    """Plaquette holonomy of the sign field eta, one entry per face."""
    out = []
    for (v, a, c, b) in L.faces():
        pr = 1
        for (p, q) in ((v, a), (a, c), (b, c), (v, b)):
            for ax in range(3):
                if L.step(p, EX[ax]) == q and (p, ax) in eta:
                    pr *= eta[(p, ax)]
                    break
                if L.step(q, EX[ax]) == p and (q, ax) in eta:
                    pr *= eta[(q, ax)]
                    break
        out.append(pr)
    return out


def vec_of(L, eta):
    return np.array([eta[(v, ax)] for (v, ax) in L.E], dtype=float)


def ladder(ev):
    """E_N = sum of the N lowest levels, N = 0..V."""
    return np.concatenate(([0.0], np.cumsum(np.sort(ev))))


# ================================================== group A: the 2x2x2 cube

CUBE = Lat((2, 2, 2), False)
FC = CUBE.faces()
sectors = {}
for sgn in itertools.product([1, -1], repeat=len(FC)):
    eta, ok = sector_eta(CUBE, sgn)
    if not ok:
        continue
    if tuple(hol_list(CUBE, eta)) != tuple(sgn):
        sectors = None
        break
    sectors[sgn] = np.linalg.eigvalsh(CUBE.mat(vec_of(CUBE, eta)))

seen, gauge_dev = {}, 0.0
for m in range(1 << CUBE.nq):
    s = np.array([1 - 2 * ((m >> i) & 1) for i in range(CUBE.nq)], dtype=float)
    eta = {e: s[i] for i, e in enumerate(CUBE.E)}
    hol = tuple(int(h) for h in hol_list(CUBE, eta))
    ev = np.linalg.eigvalsh(CUBE.mat(s))
    if hol in seen:
        gauge_dev = max(gauge_dev, float(np.abs(seen[hol] - ev).max()))
    else:
        seen[hol] = ev
nflux = sorted({sum(1 for x in k if x < 0) for k in sectors})
check(
    "A1 [exact count; numerical spectral constancy] open 2x2x2 cube, 6 faces with one F2 relation: %d of 64 face assignments are consistent sectors, "
    "flux counts %s; the 4096 link fields realise exactly those %d patterns, spectrum constant on each (%.0e)" % (len(sectors), nflux, len(seen), gauge_dev),
    len(sectors) == 32 and set(seen) == set(sectors) and gauge_dev < 1e-12 and nflux == [0, 2, 4, 6],
)

ALLP = tuple([1] * 6)
ALLM = tuple([-1] * 6)
exact_lad = {}
for tag, sgn in (("+", ALLP), ("-", ALLM)):
    eta, _ = sector_eta(CUBE, sgn)
    M = sp.Matrix(CUBE.imat(vec_of(CUBE, eta)).tolist())
    ev = sorted(sum(([sp.nsimplify(sp.radsimp(k))] * m for k, m in M.eigenvals().items()), []),
                key=lambda e: float(e))
    exact_lad[tag] = [sp.simplify(sum(ev[:N])) for N in range(CUBE.nv + 1)]
plainrow = [sp.Integer(x) for x in (0, -3, -4, -5, -6, -5, -4, -3, 0)]
sqrt3row = [-min(N, 8 - N) * sp.sqrt(3) for N in range(9)]
check(
    "A2 [exact, sympy] uniform sectors on the cube, exact integer 8x8 matrices: E_N(+1) = %s; E_N(-1) = -N sqrt3 "
    "for N <= 4 and its mirror"
    % ", ".join(str(x) for x in exact_lad["+"]),
    [sp.simplify(a - b) == 0 for a, b in zip(exact_lad["+"], plainrow)] == [True] * 9
    and [sp.simplify(a - b) == 0 for a, b in zip(exact_lad["-"], sqrt3row)] == [True] * 9,
)

lad = {k: ladder(v) for k, v in sectors.items()}
mins, ties, gaps, mflux = {}, {}, {}, {}
for N in range(CUBE.nv + 1):
    vals = {k: lad[k][N] for k in sectors}
    mn = min(vals.values())
    tied = [k for k in vals if vals[k] < mn + 1e-9]
    distinct = sorted({round(v, 9) for v in vals.values()})
    mins[N] = mn
    ties[N] = len(tied)
    gaps[N] = (distinct[1] - distinct[0]) if len(distinct) > 1 else float("nan")
    mflux[N] = sorted({sum(1 for x in k if x < 0) for k in tied})
print("   N=0..8 min E_N: " + " ".join("%.3f" % mins[N] for N in range(9)))
print("   ties/flux     : " + " ".join(
    "%d/%s" % (ties[N], "/".join(map(str, mflux[N])) if len(mflux[N]) < 4 else "all") for N in range(9)))
margin_plain = float(lad[ALLP][4] - lad[ALLM][4])
check(
    "A3 [numerical margins/ties; analytic uniqueness in note] at N = 4 the all-(-1) sector UNIQUELY minimises all 32: margin %.6f to the next value, "
    "4 sqrt3 - 6 = %.6f to plain. Minimiser: plain at N = 1, 7; two-flux at N = 2, 6; four-flux at N = 3, 5; all "
    "32 tie at N = 0, 8" % (gaps[4], margin_plain),
    ties[4] == 1 and mflux[4] == [6] and abs(gaps[4] - 0.456067275) < 1e-8
    and abs(margin_plain - float(4 * sp.sqrt(3) - 6)) < 1e-12
    and [mflux[N] for N in range(9)] == [[0, 2, 4, 6], [0], [2], [4], [6], [4], [2], [0], [0, 2, 4, 6]]
    and [ties[N] for N in (1, 2, 3, 5, 6, 7)] == [1, 3, 12, 12, 3, 1]
    and ties[0] == 32 and ties[8] == 32,
)

# ============================ group B: uniform sectors on tori and open blocks


def bloch_minus(dims, w=(0, 0, 0)):
    """all-(-1) sector: E = +- sqrt(6 + 2 sum_a cos q_a), fourfold, on the
    halved cell lattice, with a half-integer momentum shift per twisted axis."""
    cs = [np.cos(2 * np.pi * (np.arange(d // 2) + 0.5 * w[a]) / (d // 2))
          for a, d in enumerate(dims)]
    s = (cs[0][:, None, None] + cs[1][None, :, None] + cs[2][None, None, :]).ravel()
    e = np.sqrt(np.maximum(6 + 2 * s, 0.0))
    return np.sort(np.repeat(np.concatenate([-e, e]), 4))


def bloch_plus(dims, w=(0, 0, 0)):
    """all-(+1) sector: eps(q) = 2 sum_a cos q_a on the site lattice."""
    cs = [np.cos(2 * np.pi * (np.arange(d) + 0.5 * w[a]) / d) for a, d in enumerate(dims)]
    return np.sort((2 * (cs[0][:, None, None] + cs[1][None, :, None]
                         + cs[2][None, None, :])).ravel())


TORUS4 = Lat((4, 4, 4), True)
KS4 = vec_of(TORUS4, {e: eta_ks(*e) for e in TORUS4.E})
PL4 = np.ones(TORUS4.nq)
x = sp.symbols("x")
EXACT = {}
for tag, s, roots, mult in (
    ("+", PL4, [sp.Integer(0), sp.Integer(2), sp.Integer(4), sp.Integer(6)], [20, 15, 6, 1]),
    ("-", KS4, [sp.Integer(0), sp.Integer(2), 2 * sp.sqrt(2), 2 * sp.sqrt(3)], [8, 12, 12, 4]),
):
    Mi = TORUS4.imat(s)
    poly = sp.Poly(sp.expand(sp.prod([(x - r) * (x + r) if r != 0 else x for r in roots])), x)
    coeffs = [int(c) for c in poly.all_coeffs()[::-1]]
    P = np.zeros((64, 64), dtype=object)
    acc = np.eye(64, dtype=object)
    Mo = Mi.astype(object)
    for c in coeffs:
        P = P + c * acc
        acc = acc.dot(Mo)
    tr, A = {}, np.eye(64, dtype=object)
    for k in range(1, 9):
        A = A.dot(Mo)
        tr[k] = int(np.trace(A))
    pred = {k: sum(2 * m * int(sp.nsimplify(r ** k)) for r, m in zip(roots, mult) if r != 0)
            for k in (2, 4, 6, 8)}
    full = sorted(sum(([r] * m + ([-r] * m if r != 0 else []) for r, m in zip(roots, mult)), []),
                  key=lambda e: float(e))
    EXACT[tag] = (
        not P.any()
        and all(tr[k] == pred[k] for k in (2, 4, 6, 8))
        and all(tr[k] == 0 for k in (1, 3, 5, 7))
        and len(full) == 64,
        [sp.simplify(sum(full[:N])) for N in range(65)],
    )
okp, Ep = EXACT["+"]
okm, Em = EXACT["-"]
dif = [sp.simplify(Em[N] - Ep[N]) for N in range(65)]
Nstar4 = next(N for N in range(1, 64) if sp.sign(dif[N]) == -1)
check(
    "B1 [exact, sympy] torus 4^3: integer minimal-polynomial and trace witnesses fix both spectra. E_32 = "
    "-60 (plain) and %s (staggered); E_N(-) - E_N(+) = c - 24sqrt2 - 8sqrt3 with c = 48 at N = 16 (%+.4f), 36 at "
    "N = 32 (%+.4f), 46 at the first sign change N* = %d (%+.4f)"
    % (Em[32], float(dif[16]), float(dif[32]), Nstar4, float(dif[Nstar4])),
    okp and okm
    and [Ep[16], Ep[32], Ep[48]] == [-48, -60, -48]
    and sp.simplify(dif[16] - (48 - 24 * sp.sqrt(2) - 8 * sp.sqrt(3))) == 0
    and sp.simplify(dif[32] - (36 - 24 * sp.sqrt(2) - 8 * sp.sqrt(3))) == 0
    and sp.simplify(dif[Nstar4] - (46 - 24 * sp.sqrt(2) - 8 * sp.sqrt(3))) == 0
    and Nstar4 == 23,
)

BLOCKS = [((4, 4, 4), True, "T4^3"), ((4, 4, 6), True, "T4x4x6"), ((6, 6, 6), True, "T6^3"),
          ((8, 8, 8), True, "T8^3"), ((3, 3, 3), False, "B3^3"), ((4, 4, 4), False, "B4^3")]
LAD, NSTAR, WINDOW, SECOK = {}, [], True, True
print("   name     V |  E(+) floor(V/4,V/2,3V/4) |  E(-) same        |  N*")
for dims, per, tag in BLOCKS:
    if tag == "T8^3":
        V = 512
        lp, lm = ladder(bloch_plus(dims)), ladder(bloch_minus(dims))
    else:
        L = Lat(dims, per)
        V = L.nv
        ksf = {e: eta_ks(*e) for e in L.E}
        if V <= 64:
            eta, ok = sector_eta(L, [-1] * len(L.faces()))
            SECOK = SECOK and ok and set(hol_list(L, eta)) == {-1} and float(
                np.abs(np.sort(np.linalg.eigvalsh(L.mat(vec_of(L, eta))))
                       - np.sort(np.linalg.eigvalsh(L.mat(vec_of(L, ksf))))).max()) < 1e-9
        if per:
            SECOK = SECOK and float(np.abs(np.sort(np.linalg.eigvalsh(L.mat(vec_of(L, ksf))))
                                           - bloch_minus(dims)).max()) < 1e-9
        lp = ladder(np.linalg.eigvalsh(L.mat(np.ones(L.nq))))
        lm = ladder(np.linalg.eigvalsh(L.mat(vec_of(L, ksf))))
    LAD[tag] = (V, lp, lm)
    d = lm - lp
    sg = np.sign(np.where(np.abs(d) < 1e-9, 0.0, d))[1:V]
    ns = int(np.argmax(sg < 0)) + 1
    NSTAR.append(ns)
    neg = np.where(sg < 0)[0] + 1
    WINDOW = (WINDOW and neg[0] == ns and neg[-1] == V - ns
              and len(neg) == V - 2 * ns + 1 and bool(np.all(sg[:ns - 1] > 0))
              and bool(np.all(sg[V - ns:] > 0))
              and float(np.abs((d - d[::-1])[1:V]).max()) < 1e-8)
    print("   %-6s%4d |%s |%s | %3d"
          % (tag, V, "".join("%7.1f" % lp[k] for k in (V // 4, V // 2, 3 * V // 4)),
             "".join("%7.1f" % lm[k] for k in (V // 4, V // 2, 3 * V // 4)), ns))
check(
    "B2 [numerical, 1e-9] tori 4^3, 4x4x6, 6^3, 8^3 (Bloch) and open blocks 3^3, 4^3: staggered strictly lower at "
    "floor(V/2) on all six, higher at floor(V/4) and floor(3V/4); odd-V entries are not exact fractional fillings; the sector read off S_f matches KS spectrally "
    "where formed",
    SECOK
    and all(LAD[t][2][LAD[t][0] // 2] < LAD[t][1][LAD[t][0] // 2] - 1e-9 for t in LAD)
    and all(LAD[t][2][LAD[t][0] // 4] > LAD[t][1][LAD[t][0] // 4] + 1e-9 for t in LAD)
    and all(LAD[t][2][3 * LAD[t][0] // 4] > LAD[t][1][3 * LAD[t][0] // 4] + 1e-9 for t in LAD),
)
check(
    "B3 [numerical, 1e-9] sign(E_N(-) - E_N(+)) is + below N*, - on all of [N*, V - N*], + above -- one contiguous "
    "window, symmetric under N -> V - N -- with N* = %s in table order"
    % (tuple(NSTAR),),
    WINDOW and NSTAR == [23, 30, 71, 171, 10, 22],
)

# ==================================================== group C: Wilson lines


def twists(L):
    return [np.array([1.0 if not (a == ax and v[ax] == L.dims[ax] - 1) else -1.0
                      for (v, a) in L.E]) for ax in range(3)]


def wilson_scan(L, base):
    out = {}
    cuts = twists(L)
    for w in itertools.product([0, 1], repeat=3):
        s = base.copy()
        for ax in range(3):
            if w[ax]:
                s = s * cuts[ax]
        out[w] = L.EN(s, L.nv // 2)
    return out


TORI = [((4, 4, 4), "4^3"), ((4, 4, 6), "4x4x6"), ((6, 6, 6), "6^3")]
LATS = {tag: Lat(dims, True) for dims, tag in TORI}
WMIN, BLOCH_DEV = {}, 0.0
for dims, tag in TORI:
    L = LATS[tag]
    ksf = vec_of(L, {e: eta_ks(*e) for e in L.E})
    rm, rp = wilson_scan(L, ksf), wilson_scan(L, np.ones(L.nq))
    wm = min(rm, key=rm.get)
    WMIN[tag] = (rm[wm], min(rp.values()), wm, max(rm.values()), max(rp.values()))
    for w in itertools.product([0, 1], repeat=3):
        s = ksf.copy()
        sp_ = np.ones(L.nq)
        for ax in range(3):
            if w[ax]:
                s = s * twists(L)[ax]
                sp_ = sp_ * twists(L)[ax]
        BLOCH_DEV = max(BLOCH_DEV,
                        float(np.abs(np.sort(np.linalg.eigvalsh(L.mat(s))) - bloch_minus(dims, w)).max()),
                        float(np.abs(np.sort(np.linalg.eigvalsh(L.mat(sp_))) - bloch_plus(dims, w)).max()))
check(
    "C1 [numerical, 1e-9] the S_f fix no Wilson line, so fixed face data leave8 Wilson gauge classes (2^(V-1) fields each). Minimised over8 representatives: "
    "%.3f vs %.3f (4^3, staggered W=%s), %.3f vs %.3f (4x4x6), %.3f vs %.3f (6^3); staggered at its WORST twist "
    "beats plain at its best by %.2f, %.2f, %.2f"
    % (WMIN["4^3"][0], WMIN["4^3"][1], "".join("-" if b else "+" for b in WMIN["4^3"][2]),
       WMIN["4x4x6"][0], WMIN["4x4x6"][1], WMIN["6^3"][0], WMIN["6^3"][1],
       WMIN["4^3"][1] - WMIN["4^3"][3], WMIN["4x4x6"][1] - WMIN["4x4x6"][3],
       WMIN["6^3"][1] - WMIN["6^3"][3]),
    all(abs(WMIN[t][0] - v) < 1e-6 for t, v in
        (("4^3", -78.383672), ("4x4x6", -116.809009), ("6^3", -258.857540)))
    and all(abs(WMIN[t][1] - v) < 1e-6 for t, v in
            (("4^3", -67.882251), ("4x4x6", -99.882251), ("6^3", -218.564065)))
    and all(WMIN[t][0] < WMIN[t][1] - 1e-9 for t in WMIN)
    and all(WMIN[t][3] < WMIN[t][1] - 1e-9 for t in WMIN),
)
check(
    "C2 [numerical, 1e-9] the Bloch formulas +-sqrt(6 + 2 sum cos q_a) and 2 sum cos q_a, with a half-integer shift "
    "per twisted axis, reproduce all 48 twisted real-space spectra of the three tori, max deviation %.1e" % BLOCH_DEV,
    BLOCH_DEV < 1e-9,
)

# ========================================== group D: the Cauchy-Schwarz bound

T4 = LATS["4^3"]
V4, E4 = T4.nv, T4.nq
colour = np.array([1 - 2 * ((sum(v)) & 1) for v in T4.V], dtype=np.int64)
deg = np.bincount(np.concatenate([T4.rows, T4.cols]), minlength=V4)
RNG = np.random.default_rng(20260902)
batch = [KS4, PL4] + [RNG.choice([-1.0, 1.0], E4) for _ in range(50)]
trace_ok = sym_ok = True
for s in batch:
    Mi = T4.imat(s)
    trace_ok = trace_ok and int(np.trace(Mi.dot(Mi))) == 6 * V4
    sym_ok = sym_ok and not (colour[:, None] * Mi * colour[None, :] + Mi).any()
BOUND4 = -V4 * float(np.sqrt(1.5))
check(
    "D1 [exact, integer] the 4^3 torus is bipartite (colour (-1)^{|v|}), every degree 6, so ANY link-sign field has "
    "tr M^2 = 2|E| = 6V = %d and D M D = -M, a spectrum symmetric about 0 -- zero-tolerance integer identities on "
    "%d fields" % (6 * V4, len(batch)),
    trace_ok and sym_ok and set(deg.tolist()) == {6} and E4 == 3 * V4,
)
check(
    "D2 [exact] the V/2 lowest levels are minus the V/2 highest, so their squares sum to (1/2) tr M^2 = 3V = %d and "
    "Cauchy-Schwarz gives E_{V/2} >= -V sqrt(3/2) = -32 sqrt6 = %.6f on 4^3, equality iff every |lambda| = sqrt6" % (3 * V4, BOUND4),
    abs(BOUND4 + 32 * float(np.sqrt(6))) < 1e-12
    and abs(BOUND4 + float(np.sqrt((V4 // 2) * 3 * V4))) < 1e-12,
)
sopt = KS4.copy()
for ax in range(3):
    sopt = sopt * twists(T4)[ax]
Mopt = T4.imat(sopt)
flat = not (Mopt.dot(Mopt) - 6 * np.eye(V4, dtype=np.int64)).any()
evopt = np.sort(np.linalg.eigvalsh(T4.mat(sopt)))
r6 = float(np.sqrt(6))
mult_ok = (int(np.sum(np.abs(evopt + r6) < 1e-9)) == 32
           and int(np.sum(np.abs(evopt - r6) < 1e-9)) == 32)
Eopt = float(np.sum(evopt[:32]))
check(
    "D3 [exact, integer] the all-(-1) sector at its optimal twist has M^2 = 6 I EXACTLY (64x64 integer identity), "
    "spectrum +-sqrt6 x32 each, so E_32 = -32 sqrt6 = %.6f attains the bound: a GLOBAL minimiser over all 2^%d "
    "link-sign fields" % (Eopt, E4),
    flat and mult_ok and abs(Eopt - BOUND4) < 1e-9,
)
GAPS = []
for dims, tag in (((4, 4, 6), "4x4x6"), ((6, 6, 6), "6^3"), ((8, 8, 8), "8^3")):
    V = dims[0] * dims[1] * dims[2]
    bm = min(float(np.sum(bloch_minus(dims, w)[:V // 2]))
             for w in itertools.product([0, 1], repeat=3))
    GAPS.append((tag, -V * float(np.sqrt(1.5)), bm))
check(
    "D4 [numerical, 1e-9] elsewhere the spectrum is not flat and the bound is missed: %.2f vs %.2f on "
    "4x4x6 (gap %.3f), %.2f vs %.2f on 6^3 (gap %.3f), %.2f vs %.2f on 8^3 (gap %.2f)"
    % tuple(sum(([b, m, m - b] for _, b, m in GAPS), [])),
    all(m > b + 1e-6 for _, b, m in GAPS)
    and abs(GAPS[0][2] - GAPS[0][1] - 0.766498) < 1e-5
    and abs(GAPS[1][2] - GAPS[1][1] - 5.687352) < 1e-5,
)

# ==================================================== group E: search results

STRUCT_OK, INCONS_OK, SAMP_OK, GREEDY_OK, LOCAL_OK = True, True, True, True, True
srow, grow, lrow = [], [], []
for dims, tag in (((4, 4, 4), "4^3"), ((4, 4, 6), "4x4x6")):
    L = LATS[tag]
    V, nE, N = L.nv, L.nq, L.nv // 2
    ksf = vec_of(L, {e: eta_ks(*e) for e in L.E})
    cuts = twists(L)

    def emin(s, cuts=cuts, L=L, N=N):
        best = np.inf
        for w in itertools.product([0, 1], repeat=3):
            t = s.copy()
            for ax in range(3):
                if w[ax]:
                    t = t * cuts[ax]
            best = min(best, L.EN(t, N))
        return best

    e_ks = L.EN(ksf, N)
    e_ks_w = WMIN[tag][0]
    rng = np.random.default_rng(11235 + V)
    draws = [rng.choice([-1.0, 1.0], nE) for _ in range(2000)]
    raw = np.array([L.EN(s, N) for s in draws])
    sub = np.array([emin(s) for s in draws[:500]])
    SAMP_OK = (SAMP_OK and int(np.sum(raw < e_ks - 1e-9)) == 0
               and int(np.sum(sub < e_ks_w - 1e-9)) == 0)
    srow.append((tag, raw.min(), np.median(raw), raw.max(), sub.min(), np.median(sub), sub.max()))

    plane = {(0, 1): "xy", (0, 2): "xz", (1, 2): "yz"}
    fkey = []
    for (v, a, c, b) in L.faces():
        d1 = next(i for i in range(3) if L.step(v, EX[i]) == a)
        d2 = next(i for i in range(3) if L.step(v, EX[i]) == b)
        fkey.append((v, plane[(d1, d2)]))
    STRUCT = [
        (lambda v, p: -1 if p == "xy" else 1, "xy only"),
        (lambda v, p: -1 if p == "xz" else 1, "xz only"),
        (lambda v, p: -1 if p == "yz" else 1, "yz only"),
        (lambda v, p: -1 if (p == "xy" and v[0] % 2 == 0) else 1, "xy, alternating planes"),
        (lambda v, p: -1 if p != "xy" else 1, "xz+yz"),
    ]
    for fn, name in STRUCT:
        eta, ok = sector_eta(L, [fn(v, p) for (v, p) in fkey])
        STRUCT_OK = STRUCT_OK and ok and L.EN(vec_of(L, eta), N) > e_ks + 1e-9
    for fn, name in ((lambda v, p: -1 if sum(v) % 2 == 0 else 1, "even-parity faces"),
                     (lambda v, p: 1 if p == "xy" else (-1 if v[0] % 2 == 0 else 1),
                      "xz+yz, alternating planes")):
        _, ok = sector_eta(L, [fn(v, p) for (v, p) in fkey])
        INCONS_OK = INCONS_OK and not ok
    fv = [-1] * len(L.faces())
    fv[0] = 1
    _, ok = sector_eta(L, fv)
    INCONS_OK = INCONS_OK and not ok

    sw = ksf.copy()
    for ax in range(3):
        if WMIN[tag][2][ax]:
            sw = sw * cuts[ax]
    rises = [L.EN(sw * np.where(np.arange(nE) == k, -1.0, 1.0), N) - e_ks_w for k in range(nE)]
    LOCAL_OK = LOCAL_OK and min(rises) > 1e-9
    lrow.append((tag, min(rises)))

    best, hits, allminus = None, 0, 0
    for _ in range(24):
        s = rng.choice([-1.0, 1.0], nE)
        e = L.EN(s, N)
        improved = True
        while improved:
            improved = False
            for k in rng.permutation(nE):
                s[k] *= -1
                e2 = L.EN(s, N)
                if e2 < e - 1e-11:
                    e, improved = e2, True
                else:
                    s[k] *= -1
        if set(hol_list(L, {ed: s[i] for i, ed in enumerate(L.E)})) == {-1.0}:
            allminus += 1
        if abs(e - e_ks_w) < 1e-8:
            hits += 1
        best = e if best is None else min(best, e)
    GREEDY_OK = GREEDY_OK and best > e_ks_w - 1e-9 and (tag != "4^3" or abs(best - e_ks_w) < 1e-8)
    grow.append((tag, best, hits, allminus))
check(
    "E1 [numerical, 1e-9] 2000 random link fields per torus: E_{V/2} min/med/max as drawn %.1f/%.1f/%.1f (4^3), "
    "%.1f/%.1f/%.1f (4x4x6), and %.1f/%.1f/%.1f, %.1f/%.1f/%.1f over 500-field Wilson-minimised subsamples; 0 of "
    "2500 beats all-(-1)"
    % (srow[0][1], srow[0][2], srow[0][3], srow[1][1], srow[1][2], srow[1][3],
       srow[0][4], srow[0][5], srow[0][6], srow[1][4], srow[1][5], srow[1][6]),
    SAMP_OK,
)
check(
    "E2 [numerical, 1e-9] structured sectors -- flux only on xy, xz or yz plaquettes, xy on alternating x planes, "
    "xz+yz -- are consistent and all above all-(-1); even-parity-face flux, alternating xz+yz and a one-face flip "
    "are inconsistent",
    STRUCT_OK and INCONS_OK,
)
check(
    "E3 [numerical, 1e-9] greedy single-link descent, 24 random restarts per torus, never beats the Wilson-minimised "
    "all-(-1) field: best %.3f on 4^3, that field's energy within tolerance (%d of 24 reach that energy); best %.3f on 4x4x6, above %.3f"
    % (grow[0][1], grow[0][2], grow[1][1], WMIN["4x4x6"][0]),
    GREEDY_OK,
)
check(
    "E4 [numerical, 1e-9] the all-(-1) field at its optimal twist is a strict local minimum of E_{V/2}: all 192 and "
    "all 288 single-link flips raise it, by at least %.6f (4^3) and %.6f (4x4x6)"
    % (lrow[0][1], lrow[1][1]),
    LOCAL_OK,
)

# ================================================ group F: thermodynamic limit


half, quarter = {}, {}
for L in (4, 8, 16, 32, 64, 96):
    V = L ** 3
    lp, lm = ladder(bloch_plus((L, L, L))), ladder(bloch_minus((L, L, L)))
    half[L] = (lp[V // 2] / V, lm[V // 2] / V)
    quarter[L] = (lp[V // 4] / V, lm[V // 4] / V)
print("   L=4..96 e(+)1/2: " + " ".join("%8.5f" % half[L][0] for L in (4, 8, 16, 32, 64, 96)))
print("           e(-)1/2: " + " ".join("%8.5f" % half[L][1] for L in (4, 8, 16, 32, 64, 96)))
check(
    "F1 [numerical, 1e-9] exact Bloch formulas at L = 4..96 (above): at half filling staggered is lower at "
    "every listed L, with L=96 e(-) = %.8f vs e(+) = %.8f; at quarter filling higher at every L, by +%.5f per site"
    % (half[96][1], half[96][0], quarter[96][1] - quarter[96][0]),
    all(half[L][1] < half[L][0] for L in half) and all(quarter[L][1] > quarter[L][0] for L in quarter)
    and abs(quarter[96][1] - quarter[96][0] - 0.07908) < 5e-5,
)

QUAD = []
for M in (600, 1200, 2400):
    h = M // 2
    v = np.cos(2 * np.pi * np.arange(h + 1) / M)
    w = np.full(h + 1, 2.0)
    w[0] = w[h] = 1.0
    W2 = w[:, None] * w[None, :]
    S2 = v[:, None] + v[None, :]
    ap = am = 0.0
    for i in range(h + 1):
        s = v[i] + S2
        ap += w[i] * float(np.sum(W2 * np.abs(2 * s)))
        am += w[i] * float(np.sum(W2 * np.sqrt(np.maximum(6 + 2 * s, 0.0))))
    QUAD.append((M, -ap / (2 * M ** 3), -am / (2 * M ** 3)))
ep, em = QUAD[-1][1], QUAD[-1][2]
check(
    "F2 [numerical finite quadrature; no certified error] the BZ integrals of |2 sum cos q| and sqrt(6 + 2 sum cos q) on reduced "
    "grids M = 600, 1200, 2400 estimate e(+) = %.8f, e(-) = %.8f at half filling; difference %.8f |t| per site"
    % (ep, em, em - ep),
    abs(ep + 1.00241973) < 5e-8 and abs(em + 1.19380112) < 5e-8
    and abs(em - ep + 0.19138139) < 5e-8
    and abs(QUAD[1][2] - QUAD[2][2]) < 1e-8,
)

NSEQ, dd = [], None
for L in (4, 6, 8, 12, 16, 24, 32, 48, 64, 96):
    V = L ** 3
    d = ladder(bloch_minus((L, L, L))) - ladder(bloch_plus((L, L, L)))
    neg = np.where(d[1:V] < -1e-9)[0] + 1
    NSEQ.append((L, int(neg[0]), int(neg[0]) / V, int(neg[-1]) / V))
    if L == 96:
        dd, i0 = d, int(neg[0])
nst = ((i0 - 1) + (0 - dd[i0 - 1]) / (dd[i0] - dd[i0 - 1])) / 96 ** 3
# Independent two-point equation for the value actually printed below.
interp_residual = dd[i0 - 1] + (nst * 96**3 - (i0 - 1)) * (dd[i0] - dd[i0 - 1])
check("R3 [finite interpolation] displayed L=96 crossing solves its actual two-point equation; no limit-error certificate",
      abs(interp_residual) < 1e-10 and dd[i0] < -1e-9 and dd[i0 - 1] >= -1e-9)

print("   discrete first-negative N*/V by L: " + " ".join("%d:%.4f" % (L, n) for L, _, n, _ in NSEQ if L in (4, 8, 32, 96)))
check(
    "F3 [finite L=96 interpolation, no limit accuracy] crossing n* is %.6f (above), the window ending at the "
    "mirror 1 - n* = %.6f; no universal one-third threshold follows"
    % (nst, 1 - nst),
    abs(nst - 0.339659) < 2e-5 and all(abs(r[3] - (1 - r[2])) < 1e-12 for r in NSEQ)
    and abs(NSEQ[-1][2] - 0.339660) < 1e-5,
)

print(
    "SUMMARY: for the declared free Hamiltonian, all-(-1) has lower supplied half-filled energy on tested even graphs; "
    "odd-N entries are abstract Fock data; no physical selection law or limiting crossing is derived."
)
# Exact carrier parity and constructive diagonal sign-gauge check.
R_CUBE = Lat((2, 2, 2), False)
R_STAR = 0
for z in R_CUBE.star.values():
    R_STAR ^= z
check("R1 [exact] product of actual edge stars is identity; fixed-loop cube code128 equals even Fock128, not full256",
      R_STAR == 0 and 2**(R_CUBE.nq - 5) == sum(math.comb(8, n) for n in range(0, 9, 2)) == 128)
R_eta, R_ok = sector_eta(R_CUBE, [-1] * 6)
R_ks = {(v, ax): eta_ks(v, ax) for v, ax in R_CUBE.E}
R_gauge = {R_CUBE.V[0]: 1}
R_queue = deque([R_CUBE.V[0]])
while R_queue:
    v = R_queue.popleft()
    for r, (w, q) in R_CUBE.inc[v].items():
        key = R_CUBE.E[q]
        gnew = R_gauge[v] * R_eta[key] * R_ks[key]
        if w not in R_gauge:
            R_gauge[w] = gnew
            R_queue.append(w)
R_diagonal = np.diag([R_gauge[v] for v in R_CUBE.V])
R_a = R_CUBE.imat([R_eta[e] for e in R_CUBE.E])
R_b = R_CUBE.imat([R_ks[e] for e in R_CUBE.E])
check("R2 [exact] actual spanning-tree minus field is diagonally sign-gauge conjugate to KS",
      R_ok and np.array_equal(R_diagonal @ R_a @ R_diagonal, R_b))

print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
